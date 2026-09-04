#!/usr/bin/env python3
"""Validate repository catalog, Skill metadata, links, and dependency cycles."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = REPO_ROOT / "skills-manifest.json"
LINK_RE = re.compile(r"\[[^]]*\]\(([^)]+)\)")


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
        metadata = frontmatter(skill_file.read_text())
        if metadata.get("name") != name or not metadata.get("description"):
            errors.append(f"invalid frontmatter for {name}")
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

    if errors:
        print("\n".join(sorted(set(errors))), file=sys.stderr)
        return 1
    print(f"validated {len(entries)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
