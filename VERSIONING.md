# Versioning

This repository uses Semantic Versioning at two levels. `VERSION` and
`repository_version` identify the tested repository snapshot. Each manifest
entry and matching `SKILL.md` has an independent Skill version.

- Patch: compatible fixes to wording, tests, scripts, or behavior details.
- Minor: backward-compatible capability or contract additions.
- Major: incompatible trigger, Bundle, ownership, safety, input, or output changes.

A release bumps the repository version and only the Skill versions whose behavior
or packaged content changed. Update `CHANGELOG.md` in the same commit, run the
repository validator plus affected install checks, then create tag `vX.Y.Z`.
The tag names the whole tested repository snapshot; manifest versions identify
the individual installed Skills.
