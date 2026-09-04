---
name: engineering-build
description: Implement a user-specified Engineering Bundle against the real codebase, verify the result, update evidence-backed Bundle status, and translate actual outcomes back into the Bundle's semantic structure. Use only when the user explicitly asks to build from an existing Bundle path. Do not use for ambiguous requirements, direct implementation briefs, new product or architecture design, or unconfirmed external and high-risk operations.
---

# Engineering Build

Turn a confirmed Engineering Bundle into code and evidence without changing the system intent it defines.

```text
confirmed Engineering Bundle -> inspect reality -> implement -> verify
                             -> update actual status -> explain outcomes
```

The Bundle defines intended behavior, consequential architecture, safety and interface boundaries, acceptance, and rejection conditions. This skill owns implementation mechanics and evidence. It does not silently redesign the Bundle.

## Trigger and Authority

- Use only when the user explicitly asks to implement a specific Engineering Bundle and provides or identifies its path. Merely mentioning, reviewing, or asking about a Bundle is not build authorization.
- The current request authorizes ordinary in-scope code edits and local verification needed to implement the selected Bundle stage or slice.
- A Bundle does not authorize commit, push, remote sync, deployment, production mutation, hardware operation, destructive action, or another high-risk step. Obtain the authority required by the current environment immediately before such an action.
- Do not consume a direct implementation brief. Small direct work belongs to the current execution workflow; this skill exists for the stable Bundle interface.

## Load the Protocol

Always read [bundle-build-protocol.md](references/bundle-build-protocol.md) before acting on a Bundle.

## Build Route

1. Resolve the exact Bundle and implementation workspace. Read applicable `AGENTS.md` or repository rules before changes.
2. Read `MAP.md` first when present, validate its relative links, then read the current stage or explicitly selected slice. Follow only references that can change the current implementation decision. Preserve an existing compatible structure rather than reorganizing it. A broken link may be recovered only when the intended target is unique and supported by the Map's text; ambiguous or conflicting current-stage targets require a design return.
3. Inspect the real repository, current revision, configuration, relevant code, tests, evidence, and existing user changes. Do not rely on the Bundle alone for current-state claims.
4. Check that the selected work explains intended behavior, affected scope, selected design, consequential tradeoffs, safety and interface constraints, acceptance evidence, rejection conditions, and blocking open decisions.
5. Compare the Bundle's assumptions with the real system before editing. Distinguish an ordinary implementation detail from a design-changing conflict using the Design Authority Boundary below.
6. If the contract is valid, implement the smallest coherent slice. Decide helper structure, local data representation, ordinary error handling, and test mechanics autonomously while preserving user changes and repository conventions.
7. Verify in proportion to causal uncertainty and consequence. Run targeted checks, a relevant known-good regression, and failure cases required by the Bundle. Escalate only when the Bundle or observed risk requires stronger evidence.
8. Update the affected Bundle stage with what was actually implemented, the evidence obtained, what remains incomplete, and any new limitations. Do not rewrite design intent to make the implementation appear compliant.
9. Update `MAP.md` only when evidence changes the current stage, route, dependency, shared boundary, or confirmed cross-stage decision.
10. Return a Human-readable Build Result in the Bundle's original semantic order: planned behavior, actual implementation state, what the user can now expect, and what is still unproven.

## Design Authority Boundary

Decide autonomously when the choice does not change externally observable behavior or a consequential contract. Examples include helper functions, local organization, private types, routine error handling, test fixtures, and implementation-level corner cases consistent with the Bundle.

Stop before proceeding when implementation would require changing any of these:

- system behavior or problem scope;
- safety or failure policy;
- public or integration interface;
- acceptance or rejection criteria;
- important architecture ownership or dependency direction;
- an assumption whose failure changes the selected design.

Return exactly one of these headings:

- `Bundle assumption invalid` when current evidence disproves a premise;
- `Design decision required` when multiple valid directions require human choice.

Under that heading, provide the evidence, affected Bundle anchor, implementation impact, safe state of current changes, and the single decision that must return to `$engineering-design`. Do not disguise a design decision as a coding detail or patch the Bundle around it.

## Bundle Update Rules

- Treat direct human edits as part of the contract. Never silently overwrite them.
- Record only evidence-backed state. Keep existing, implemented-not-validated, targeted checks, offline, simulation or non-moving loop, hardware or field, disabled, rejected, and formally accepted states distinct.
- A build, unit test, commit, or pull request is not field acceptance.
- Update only the affected stage by default. Use Git history for change history; do not append a chronological work log merely to show activity.
- Preserve unresolved design questions. Do not mark a stage complete while one still blocks its intended outcome.
- Repair a stale relative link while updating the Bundle only when its intended target was uniquely resolved without changing structure or meaning. Report the repair; do not use Build authority for document reorganization.

## Result Translation

Follow the Bundle's major block order and recognizable anchors. For each implemented or deferred block, explain:

```text
Plan
Actual
What is now true
What is still unproven
```

Use natural headings rather than a rigid form. Lead with observable behavior, retain the minimum technical anchor needed to locate the evidence, and state acceptance and rejection results plainly. Do not call an existing capability newly implemented, or translate a diagnostic-only change as a control-behavior change.

Finish with the exact Bundle path, implementation revision when available, tests and evidence, incomplete items, authority-limited steps not performed, and whether the result is complete or must return to `$engineering-design`.
