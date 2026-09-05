"""Deterministic catalog checks. Runtime availability is opt-in, never an install."""
from pathlib import Path
import re

NAME = r'[a-z][a-z0-9]*(?:-[a-z0-9]+)+'
SEMVER = r'(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)'
LINK = re.compile(r'\[[^]]*\]\(([^)]+)\)')


def active_calls(text):
    """Check explicit invocations in operational prose/tables, not examples/history.

    This is a bounded linter, not a natural-language authority or call tracer.
    Runtime read traces are checked separately in real-task evaluation.
    """
    calls = set()
    fenced = False
    excluded = False
    for line in text.splitlines():
        if line.lstrip().startswith(('```', '~~~')):
            fenced = not fenced
            continue
        if fenced:
            continue
        if line.startswith('#'):
            excluded = bool(re.search(r'example|history|historical|示例|历史', line, re.I))
        if excluded or line.lstrip().startswith('>'):
            continue
        # Split sentences so a later prohibition cannot hide an earlier invocation.
        for clause in re.split(r'[。;；]|\.\s', line):
            if re.search(r'do(?:es)? not|must not|never|不得|不要|禁止', clause, re.I):
                continue
            if re.search(r'\b(load|invoke|route|use)\b|加载|调用|遵循', clause, re.I) or line.startswith('|'):
                calls.update(re.findall(r'`\$?('+NAME+r')`', clause))
    return calls


def operational_files(root):
    """Follow runtime references from SKILL.md; behavior specs are not invocations."""
    pending = [root / 'SKILL.md']
    seen = set()
    while pending:
        f = pending.pop().resolve()
        if f in seen or not f.is_file():
            continue
        seen.add(f)
        yield f
        for link in LINK.findall(f.read_text()):
            link = link.split('#')[0]
            if not link or '://' in link or Path(link).is_absolute():
                continue
            target = (f.parent / link).resolve()
            if target.is_relative_to(root.resolve()) and target.suffix == '.md' and 'behavior-test' not in target.name:
                pending.append(target)


def parse_constraint(value):
    parts = value.split(',') if isinstance(value, str) else []
    result = []
    for part in parts:
        match = re.fullmatch(r'\s*(>=|<=|>|<|==)\s*('+SEMVER+r')\s*', part)
        if not match:
            raise ValueError('expected comma-separated stable SemVer comparisons')
        result.append((match[1], tuple(map(int, match[2].split('.')))))
    if not result:
        raise ValueError('empty constraint')
    return result


def compatible(version, constraint):
    if not re.fullmatch(SEMVER, version):
        return False
    value = tuple(map(int, version.split('.')))
    return all({'>=': value >= target, '<=': value <= target,
                '>': value > target, '<': value < target, '==': value == target}[op]
               for op, target in parse_constraint(constraint))


def catalog_errors(repo, data, installed_root=None):
    repo = repo.resolve()
    errors = []
    entries = data['skills']
    names = {e['name'] for e in entries}
    external = set(data.get('external_skills', []))
    allowed = names | external
    constraints = data.get('external_version_constraints', {})
    for name, bound in constraints.items():
        if name not in external:
            errors.append(f'version constraint target is not external: {name}')
        try:
            parse_constraint(bound)
        except ValueError as exc:
            errors.append(f'invalid constraint for {name}: {exc}')
    graph = {}
    required = set(names)
    for entry in entries:
        name = entry['name']
        declared = set(entry.get('depends_on', [])) | set(entry.get('routes_to', []))
        required.update(declared)
        for target in sorted(declared - allowed):
            errors.append(f'undeclared target: {name} -> {target}')
        root = repo / entry['path']
        for f in operational_files(root):
            for target in sorted(active_calls(f.read_text()) - declared - {name}):
                errors.append(f'unlisted active invocation: {name} -> {target} ({f.relative_to(repo)})')
        graph[name] = [n for n in entry.get('depends_on', []) if n in names]
    visiting, visited = set(), set()
    def visit(name):
        if name in visiting:
            errors.append(f'dependency cycle includes {name}')
            return
        if name in visited:
            return
        visiting.add(name)
        for target in graph[name]:
            visit(target)
        visiting.remove(name)
        visited.add(name)
    for name in graph:
        visit(name)
    if installed_root is not None:
        for name in sorted(required):
            f = installed_root / name / 'SKILL.md'
            if not f.is_file():
                errors.append(f'missing installed target: {name}; degraded use is not integration acceptance')
                continue
            text = f.read_text()
            fm = re.match(r'^---\n(.*?)\n---', text, re.S)
            header = fm.group(1) if fm else ''
            if not re.search(r'^name:\s*'+re.escape(name)+r'\s*$', header, re.M):
                errors.append(f'installed name mismatch: {name}')
            if name in constraints:
                match = re.search(r'^metadata:\s*\n(?:[ \t]+[^\n]*\n)*?[ \t]+version:\s*('+SEMVER+r')\s*$', header, re.M)
                if not match or not compatible(match[1], constraints[name]):
                    errors.append(f'incompatible installed version: {name} requires {constraints[name]}')
    return errors
