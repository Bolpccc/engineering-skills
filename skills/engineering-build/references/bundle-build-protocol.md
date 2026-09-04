# Bundle Build Protocol

Use this protocol to consume an Engineering Bundle without allowing implementation convenience to change its intent.

## Resolve the Contract

The user must identify the Bundle and explicitly ask for implementation. Resolve the path exactly; do not guess between multiple similarly named Bundles.

Read in this order:

1. applicable workspace and repository instructions;
2. `MAP.md`, when present;
3. the current stage named by the Map, or the slice explicitly selected by the user;
4. linked source, configuration, evidence, or decision material that can change the implementation;
5. the real codebase and its current revision.

New Bundles normally use a flat `MAP.md` plus outcome-based stage documents. Existing Bundles may have a compatible older structure. Preserve it unless structure itself prevents a safe build; a Build task is not authorization to reorganize design documents.

Inventory relative-link failures and validate every link needed to resolve the current contract before treating the Bundle as build-ready. If a current-stage or dependency link is stale but exactly one file within the Bundle matches the intended stage identity and surrounding Map text confirms it, use that target and record a narrow link repair for the Bundle update. A broken historical or unrelated reference is reported but does not block the build. If multiple current candidates exist, nested Maps disagree about the active contract, or recovery would require choosing a different outcome, return `Design decision required` instead of guessing.

## Handoff Readiness

The selected stage or slice must make these decisions recoverable:

- intended observable behavior and the problem it solves;
- affected components and boundaries;
- selected technical direction and consequential tradeoffs;
- public or integration interface expectations;
- safety, fallback, and failure behavior;
- acceptance evidence and a result that rejects the direction;
- open questions, with none remaining that block implementation.

If a missing item can be derived safely from the code and does not alter a consequential contract, derive it. If filling it would select product behavior, risk, architecture, interface, or acceptance policy, return `Design decision required`.

## Reality Preflight

Before editing:

- establish the exact repository root, branch, `HEAD`, upstream, and working-tree state;
- preserve unrelated tracked and untracked user changes;
- inspect the code and tests named or implied by the Bundle;
- check that referenced APIs, modules, parameters, and assumptions still exist;
- identify generated files, submodules, remote-only dependencies, and permission boundaries;
- resolve whether prior implementation already satisfies part of the Bundle.

Do not reset, discard, overwrite, or reformat unrelated work. If current changes overlap the required edit and cannot be preserved safely, stop and report the overlap.

## Implementation Detail or Design Decision

An implementation detail is local and substitutable: changing it does not alter the behavior a user observes, a public contract, a safety property, an acceptance test's meaning, or an important ownership boundary.

A design decision changes at least one of those properties. Common signals include:

- the Bundle's causal premise is contradicted by source or runtime evidence;
- the intended behavior cannot be produced without changing another promised behavior;
- a safety or compatibility invariant must be weakened;
- an API or protocol must change rather than remain compatible;
- the named component cannot own the behavior without reversing a dependency;
- the acceptance condition is impossible, ambiguous, or measures the wrong mechanism.

Do not solve a design conflict by adding a hidden fallback, changing a default, weakening a check, or editing the Bundle after the fact.

## Design Return Contract

When blocked by design, stop at the safest recoverable point and return:

```text
Bundle assumption invalid | Design decision required

Evidence
Affected Bundle anchor
Why implementation cannot continue as written
Current state of any changes already made
Decision required from engineering-design
```

Ask for one consequential decision. Preserve useful read-only findings and safe partial work, but do not claim the selected outcome is implemented.

## Implement and Verify

Implement one coherent stage or explicitly selected slice. Keep changes reviewable and do not fold unrelated cleanup into the work.

Match evidence to risk:

- When source and contract establish the mechanism, use targeted tests, one relevant known-good regression, and one failure case.
- When operating conditions remain uncertain, add the minimum observation needed and one representative validation.
- When competing causes or safety-critical thresholds remain, use the controlled comparison required by the Bundle.

Stop gathering evidence when it can accept the slice, reveal a meaningful regression, and distinguish the rejection condition. Do not treat more test volume as stronger proof when it does not change the decision.

If the environment requires authorization for a later step, complete every safe local action first, then state precisely what remains. Never infer hardware, deployment, commit, push, or remote authority from the Bundle.

## Update the Bundle from Evidence

Update the technical Bundle only after inspecting actual results:

- describe the implementation outcome, not an activity diary;
- link or name the revision, tests, logs, or artifacts that support the state;
- retain failed checks and remaining limitations that affect acceptance;
- distinguish local build, targeted tests, offline, simulation or non-moving loop, hardware or field, and formal acceptance;
- leave unimplemented slices visibly unimplemented;
- do not change the original goal, boundary, or acceptance to match what was easiest to build.

Update only the affected stage. Change `MAP.md` only when evidence moves the current stage, completes a dependency, or changes a shared decision. Preserve human edits and surface contradictions.

## Human-readable Build Result Packet

Use the Bundle's own major order. Before presentation, build a packet for every consequential block:

- what behavior was planned;
- what was actually changed or left unchanged;
- what evidence now supports;
- what the user can observe or rely on;
- what remains unproven or outside this build.

Retain source anchors such as stage numbers and key technical terms. Attach the exact evidence level, acceptance or rejection result, incomplete and authority-limited steps, and any relevant language or distinction the user has already adopted. These are `must_preserve`; never elevate status during composition.

Load `$cognitive-bridge` with `purpose=review`, the complete packet as
`source_content`, the Bundle anchors as `source_anchors`, and the protected state,
coverage, evidence, safety, interface, acceptance, and rejection fields as
`must_preserve`. It may compress functions, file lists, parameters, and routine
test mechanics unless they affect the user's decision. It may not change the
Bundle's semantic order or engineering outcome.

If `$cognitive-bridge` is unavailable, produce the minimum packet directly and
label it `Cognitive adaptation unavailable`; do not omit the result.

End with one of three outcomes:

- **Implemented and accepted at the evidenced level**;
- **Partially implemented**, with the remaining Bundle blocks named;
- **Return to engineering-design**, with the invalid assumption or required decision.
