# Engineering Skills

Canonical public repository for the `engineering-design` and
`engineering-build` Agent Skills.

The two Skills share one Engineering Bundle contract while retaining separate
authority boundaries: Design owns intent and consequential decisions; Build
owns implementation and evidence. User-facing explanations use the external
[`cognitive-bridge`](https://github.com/Bolpccc/cognitive-bridge) companion when
available.

## Install

```bash
python3 scripts/install.py engineering-design engineering-build
```

The installer copies only the selected Skill folders into
`~/.codex/skills/<skill-name>`.

## Validate

```bash
python3 scripts/validate.py
```

See `skills-manifest.json` for the canonical catalog and dependency contract.

