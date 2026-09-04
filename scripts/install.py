#!/usr/bin/env python3
"""Install selected Skills from this repository with delete-style parity."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = REPO_ROOT / "skills-manifest.json"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skills", nargs="*")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--target-root", type=Path, default=Path.home() / ".codex" / "skills")
    args = parser.parse_args()

    catalog = json.loads(MANIFEST.read_text())
    entries = {item["name"]: item for item in catalog["skills"]}
    selected = list(entries) if args.all else args.skills
    if not selected:
        parser.error("name at least one skill or pass --all")
    unknown = sorted(set(selected) - set(entries))
    if unknown:
        parser.error(f"unknown skills: {', '.join(unknown)}")

    target_root = args.target_root.expanduser().resolve()
    if target_root == Path(target_root.anchor):
        parser.error("target root may not be a filesystem root")
    target_root.mkdir(parents=True, exist_ok=True)

    for name in selected:
        source = (REPO_ROOT / entries[name]["path"]).resolve()
        target = target_root / name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target, ignore=shutil.ignore_patterns(".git"))
        print(f"installed {name} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

