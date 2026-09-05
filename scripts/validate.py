#!/usr/bin/env python3
"""Validate repository catalog, Skill metadata, links, and dependency cycles."""

from __future__ import annotations

import argparse
from governance import catalog_errors
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = REPO_ROOT / "skills-manifest.json"
LINK_RE = re.compile(r"\[[^]]*\]\(([^)]+)\)")
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values


def metadata_version(text: str) -> str | None:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    lines = match.group(1).splitlines()
    for index, line in enumerate(lines):
        if line.strip() != "metadata:":
            continue
        for child in lines[index + 1 :]:
            if child and not child[0].isspace():
                break
            version = re.match(r"^\s+version:\s*([^\s]+)\s*$", child)
            if version:
                return version.group(1)
    return None


def validate_links(root: Path) -> list[str]:
    errors: list[str] = []
    for markdown in root.rglob("*.md"):
        for raw in LINK_RE.findall(markdown.read_text()):
            link = raw.split("#", 1)[0]
            if not link or "{{" in link or "://" in link or link.startswith(("#", "/")):
                continue
            if not (markdown.parent / link).resolve().exists():
                errors.append(f"broken link: {markdown.relative_to(REPO_ROOT)} -> {raw}")
    return errors


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    entries = data.get("skills", [])
    names = {item["name"] for item in entries}
    allowed = names | set(data.get("external_skills", []))
    errors: list[str] = []
    repo_version = (REPO_ROOT / "VERSION").read_text().strip()

    if data.get("schema_version") != 1:
        errors.append("unsupported manifest schema_version")
    if not SEMVER_RE.fullmatch(repo_version):
        errors.append("VERSION is not stable SemVer")
    if data.get("repository_version") != repo_version:
        errors.append("repository_version does not match VERSION")
    if f"## [{repo_version}]" not in (REPO_ROOT / "CHANGELOG.md").read_text():
        errors.append("CHANGELOG.md has no entry for VERSION")

    if len(names) != len(entries):
        errors.append("duplicate skill names in manifest")
    graph: dict[str, list[str]] = {}
    for item in entries:
        name = item["name"]
        root = REPO_ROOT / item["path"]
        skill_file = root / "SKILL.md"
        agent_file = root / "agents" / "openai.yaml"
        if root.name != name:
            errors.append(f"folder/name mismatch: {item['path']} vs {name}")
        if not skill_file.is_file() or not agent_file.is_file():
            errors.append(f"missing required files for {name}")
            continue
        skill_text = skill_file.read_text()
        metadata = frontmatter(skill_text)
        if metadata.get("name") != name or not metadata.get("description"):
            errors.append(f"invalid frontmatter for {name}")
        skill_version = item.get("version")
        if not isinstance(skill_version, str) or not SEMVER_RE.fullmatch(skill_version):
            errors.append(f"invalid manifest version for {name}")
        if metadata_version(skill_text) != skill_version:
            errors.append(f"SKILL.md metadata.version mismatch for {name}")
        if f"${name}" not in agent_file.read_text():
            errors.append(f"default prompt does not invoke ${name}")
        dependencies = item.get("depends_on", [])
        unknown = sorted(set(dependencies) - allowed)
        if unknown:
            errors.append(f"unknown dependencies for {name}: {', '.join(unknown)}")
        graph[name] = [dep for dep in dependencies if dep in names]
        errors.extend(validate_links(root))

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            errors.append(f"dependency cycle includes {node}")
            return
        if node in visited:
            return
        visiting.add(node)
        for child in graph.get(node, []):
            visit(child)
        visiting.remove(node)
        visited.add(node)

    for name in names:
        visit(name)

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--installed-root', type=Path, help='Check the actual installed dependency surface; never install missing companions')
    args = parser.parse_args()
    errors.extend(catalog_errors(REPO_ROOT, json.loads((REPO_ROOT / 'skills-manifest.json').read_text()), args.installed_root.expanduser().resolve() if args.installed_root else None))
    if errors:
        print("\n".join(sorted(set(errors))), file=sys.stderr)
        return 1
    print(f"validated {len(entries)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
