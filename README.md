# Engineering Skills

Canonical public repository for the `engineering-design` and
`engineering-build` Agent Skills.

The two Skills share one Engineering Bundle contract while retaining separate
authority boundaries: Design owns intent and consequential decisions; Build
owns implementation and evidence. User-facing explanations use the external
[`cognitive-bridge`](https://github.com/Bolpccc/cognitive-bridge) companion when
available.

Current repository release: `v1.0.0`. Repository snapshots and individual Skill
versions follow [VERSIONING.md](VERSIONING.md); changes are recorded in
[CHANGELOG.md](CHANGELOG.md).

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

## Validation layers

`python3 scripts/validate.py` checks metadata, links, declared dependencies and routes,
and explicit operational invocation references. The invocation linter skips fenced
examples, history/example sections and prohibitions; it is not a semantic parser.
`depends_on` must be acyclic; `routes_to` may intentionally return to another owner.
Run `python3 -m unittest discover -s tests -v` for deterministic negative cases.

`python3 scripts/validate.py --installed-root ~/.codex/skills` additionally checks
actual target availability and optional `external_version_constraints`. Bounds
use comma-separated stable SemVer comparisons (`>=`, `<`, `<=`, `>`, `==`).
Other external Skills without version metadata are checked for presence and name.
A missing companion can still use the documented fallback, but is not a passing
full-integration check. No command automatically installs dependencies.

Real-task fixtures live in `evals/cases.json`; their rubrics assess actual outputs,
not statements about following rules. Model evaluation is manual, not a CI job.
It does not measure human learning or establish a model/Skill superiority claim.
