# Engineering Build

An Agent Skill for implementing a confirmed Engineering Bundle against the real codebase, verifying the result, updating evidence-backed status, and explaining what actually became true.

```text
engineering-design
       |
       v
confirmed Engineering Bundle
       |
       v
engineering-build
       |
       +-- implementation + evidence --> updated Bundle
       `-- invalid design assumption --> engineering-design

evidence-bounded result -> cognitive-bridge -> user-facing explanation
```

## Use

```text
Use $engineering-build to implement the confirmed Bundle at /path/to/example-engineering-bundle/.
```

The skill reads the Map and current stage, checks the real repository and current revision, implements the authorized slice, runs proportionate verification, updates actual Bundle status, and reports results in the Bundle's original semantic order.

## Design boundary

The Bundle defines system behavior, safety, interfaces, important architecture responsibility, acceptance, and rejection conditions. Engineering Build may decide local code organization, helpers, private data structures, ordinary corner cases, and test mechanics.

If implementation would require changing the Bundle's consequential contract, it stops with `Bundle assumption invalid` or `Design decision required` and returns the issue to [`engineering-design`](../engineering-design).

The Bundle does not authorize commit, push, deployment, remote mutation, hardware operation, or destructive actions. Those remain subject to the user's current request and environment rules.

## Install

Clone [`Bolpccc/engineering-skills`](https://github.com/Bolpccc/engineering-skills), then run:

```bash
python3 scripts/install.py engineering-build
```

Install [`cognitive-bridge`](https://github.com/Bolpccc/cognitive-bridge) for
cognitively adapted results. Without it, the Skill retains a labeled,
domain-complete fallback.

## Repository structure

```text
SKILL.md
agents/openai.yaml
references/bundle-build-protocol.md
README.md
LICENSE
```

MIT License. See [LICENSE](LICENSE).
