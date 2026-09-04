---
name: engineering-design
description: Clarify an engineering need in system-behavior language, inspect the real system, and turn the aligned result into either a compact direct-implementation brief or a lightweight technical Engineering Bundle with a cognitively adapted human-readable mapping. Use when software, robotics, infrastructure, or app behavior is still being discussed, challenged, or designed before implementation. Do not use to implement code, execute an existing Bundle, manage project trackers, or publish externally.
---

# Engineering Design

Help a technical owner decide what the system must do without requiring them to review every implementation detail. Keep the conversation in human-readable behavior and outcome language while doing the technical reasoning needed to protect architecture, safety, compatibility, and acceptance boundaries.

This skill owns:

```text
human-language problem -> aligned engineering definition
                         -> direct implementation brief OR Engineering Bundle
                         -> human-readable confirmation
```

`BUILD` remains outside this skill. A confirmed Engineering Bundle is the stable interface to `$engineering-build`; a direct implementation brief is a small, one-time handoff to the current execution workflow and does not become a Bundle.

## Boundaries

- Inspect and reason about the current system read-only. Do not edit code, run experiments, operate hardware, deploy, commit, push, or begin implementation under this skill alone.
- Do not turn the user into the implementation reviewer. Ask them to decide observable behavior, priority, risk, responsibility, and acceptance; derive ordinary technical details yourself.
- Do not create persistent documents unless the user selects the Bundle route or supplies an existing Bundle for revision.
- Do not manage issues, owners, deadlines, branches, pull requests, or status synchronization.
- External publication is a separate workflow and requires explicit confirmation after local review.

## Load References as Needed

- Read [requirements-interview.md](references/requirements-interview.md) for a new or resumed design discussion and when new evidence invalidates a Bundle assumption.
- Read [research-for-decisions.md](references/research-for-decisions.md) when public mechanisms, similar incidents, alternatives, or counterexamples can change the decision.
- Read [document-model.md](references/document-model.md) only after the user selects the Bundle route or when an existing Bundle is in scope.
- Read [plan-interpretation.md](references/plan-interpretation.md) after creating or materially revising a Bundle, or when the user asks to understand or challenge an existing technical plan.

## Design Route

1. Extract the observed behavior, desired outcome, constraints, unacceptable outcomes, claimed success, existing evidence, and any proposed solution from what the user already supplied.
2. Inspect the smallest relevant set of architecture, code, configuration, history, internal knowledge, and evidence before asking for facts that can be discovered safely.
3. Speak first in system behavior: what happens now, what should happen instead, what must remain true, what may not be traded away, and what observation would accept or reject the change. Add a technical term only when it helps preserve a consequential boundary or lets the user return to the source.
4. State the current interpretation and any materially different reading in three to five short sentences, then advance one decision-relevant question. Do not expose an internal requirements framework or stack several questions.
5. Challenge false premises, solution fixation, contradictions, vague success, and scope growth. When the user challenges a technical premise, treat it as a potentially design-changing input: verify the discoverable mechanism, downgrade unsupported completion claims, and revise the affected model instead of asking the user for implementation parameters.
6. Track facts, assumptions, preferences, unknowns, scope, and acceptance internally. Research or inspect before asking. Compare approaches only at a real engineering fork and lead with a recommendation.
7. Choose the least expensive evidence capable of falsifying the current hypothesis. Escalate to controlled A/B, parameter matrices, simulation, or hardware evidence only when causal uncertainty or consequence justifies it.
8. Before handoff, pressure-test the problem, proposed scope, hidden dependencies, safety and interface boundaries, and rejection conditions.
9. When the need, behavior, consequential tradeoffs, scope, and acceptance evidence are ready, ask the user to choose exactly one route: **direct implementation** or **Engineering Bundle**. If the user already selected one explicitly, do not ask again.

## Direct Implementation Route

Use this only when the change has one bounded outcome, a small affected surface, no unresolved architecture or safety decision, and no need for a durable multi-stage design record.

Return a compact implementation brief in the conversation:

```text
Goal
Keep
Do not
Acceptance
Rejection signal
```

Adapt the labels to the project's language and omit no consequential boundary. Do not create a file or invoke `$engineering-build`. Make the transition to the current execution workflow explicit; implementation permissions still come from the current environment and the user's request.

## Engineering Bundle Route

Use this when the work spans dependent outcomes, has consequential architecture, safety, interface, or verification decisions, is likely to be revised across evidence cycles, or the user wants a durable technical design.

- Require a user-designated local workspace, locate an equivalent Bundle first, and follow [document-model.md](references/document-model.md).
- Keep `MAP.md` and stage documents technical and implementation-grade. Record behavior, technical analysis, selected design, affected responsibilities, interfaces, safety boundaries, implementation slices, acceptance evidence, rejection conditions, and unresolved decisions.
- Make the current stage concrete, the next directional, and later stages skeletal. Update only the affected stage unless the route, current stage, shared boundary, or key cross-stage decision changes.
- Preserve direct human edits. Verify factual or technical claims and surface contradictions; never silently restore an earlier AI formulation.
- After creating or materially revising the Bundle, form the domain-owned mapping packet from [plan-interpretation.md](references/plan-interpretation.md), then load `$cognitive-bridge` to compose the conversation-only Human-readable Mapping. Preserve the Bundle's semantic block order, technical anchors, coverage, status, and acceptance meaning so the user can move between outcome language and technical detail.
- If the user corrects the mapping, first revise the affected technical block, then retranslate that block. When corrections settle, present the complete mapping again.
- A Bundle becomes ready for `$engineering-build` only after the user explicitly confirms that the mapped behavior, boundaries, and acceptance match their intent. Confirmation does not authorize commit, push, deployment, remote actions, or hardware operation.
- If `$cognitive-bridge` is unavailable, apply the domain mapping contract directly, label the result `Cognitive adaptation unavailable`, and still return every required anchor and boundary. Do not install a missing companion automatically or omit the mapping.

## Diagram Composition

- Do not create, propose, draft, or invoke tooling for a diagram unless the user explicitly requests one. A multi-stage Bundle does not imply a route diagram by default.
- When the user explicitly requests a diagram, invoke `$mermaid-skill`. This skill owns meaning and placement; `$mermaid-skill` owns diagram form, source, syntax validation, rendered preview, and readability review.
- Preserve an existing diagram during ordinary document updates. If a requested design change would make it materially false, surface the inconsistency and ask whether to update or remove it; do not silently redraw it.
- Without a designated local workspace, keep a requested draft diagram session-local and do not send private source to an external renderer.
- If `$mermaid-skill` is unavailable, preserve the requested diagram intent and draft source without claiming validation or installing it automatically.

## Evidence Re-entry

When implementation, test, simulation, field, or research evidence returns, identify which assumption, decision, status, or acceptance claim it changes. Update only the affected technical material, retain conclusions still supported, and regenerate the affected mapping packet before invoking `$cognitive-bridge` again. A new design or implementation decision requires a new confirmation; evidence does not silently broaden the authorized scope.

## Handoff

For direct implementation, return the compact brief and state that no Bundle was created.

For a Bundle, finish with:

- the Bundle path and current stage;
- the complete Human-readable Mapping;
- assumptions and unresolved decisions that remain;
- the next acceptance and rejection observations;
- whether the user has confirmed it for `$engineering-build` or it remains under design.

If implementation reveals `Bundle assumption invalid` or `Design decision required`, reopen only the affected design branch, revise the Bundle after the decision, and produce a new mapping for confirmation.
