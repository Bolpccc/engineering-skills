# Requirements Interview

Use this reference for a fresh design discussion, a resumed discussion, or a return prompted by new engineering evidence. The interview is an active engineering diagnosis, not a neutral questionnaire. Its job is to uncover the real need, challenge a weak framing, and make the next useful verification clear while keeping the user-facing conversation at the level of system behavior and observable outcomes.

## 1. Intake the Input as Given

Accept a brain dump, transcript, sketches, existing documents, bug history, or short goal. The user does not need to restate it in a template.

Extract what is already present:

- the observed problem, affected system or person, and operating context;
- why it matters now and the cost of leaving it alone;
- the desired outcome and any solution already proposed;
- constraints, exclusions, preferences, and authority boundaries;
- claimed success conditions;
- current implementation, prior attempts, and relevant evidence;
- contradictions, assumptions, and unknowns;
- any named local workspace for persistent documents.

Do not praise the input generically. Say what is already strong, what is weak enough to change the direction, and what you currently believe.

The user does not need to supply implementation vocabulary. Translate their behavior, responsibility, risk, and acceptance statements into technical implications internally; do not ask them to invent parameters, class boundaries, data structures, or test mechanics that can be derived from the system.

## 2. Inspect Before Asking

When an existing system is involved, inspect the smallest relevant set of:

- architecture and component boundaries;
- implementation and reusable capabilities;
- configuration and operational constraints;
- tests, logs, experiment results, incidents, and known failures;
- decisions and internal documents that still constrain the work.

Prefer primary engineering evidence over summaries. Keep inspection read-only. Do not ask the user for a discoverable fact, and do not start a build, test run, prototype, remote action, or hardware operation merely to answer the interview.

Read [research-for-decisions.md](research-for-decisions.md) when a public mechanism, similar incident, alternative, or counterexample could answer the uncertainty more reliably than the user. State what was found and distinguish current-system evidence, public evidence, old documentation, and inference.

## 3. Open with a Working Interpretation

Before the first question, briefly cover:

1. **Current reading:** the concrete problem and desired outcome you think the user means.
2. **Silent forks:** materially different interpretations you would otherwise choose between without permission, such as the full system versus one failure path, automatic versus on-demand behavior, or the named solution versus the outcome behind it.
3. **Destination:** what a useful handoff appears to be, such as a decision, a bounded research question, or a staged engineering plan with acceptance evidence.

Keep the whole opener to three to five short sentences. Do not render `Current reading`, `Silent forks`, or `Destination` as visible headings, and do not repeat the opener on later turns unless the interpretation materially changes. State it as a falsifiable interpretation, not a ceremonial summary. If the user named a solution before establishing the problem, say so directly. Do not assume the requested mechanism is the requirement.

For a small request whose problem, boundary, and acceptance evidence are already clear, skip unnecessary interviewing and proceed to the handoff or document update.

## Human-Language Discussion Contract

Discuss the decision in this order when relevant:

1. what the system or person experiences now;
2. what should be observably different;
3. what must remain true;
4. which shortcut or failure is unacceptable;
5. what observation accepts or rejects the result.

Lead with that language. Add a technical term only when it protects an important safety, interface, architecture, or causal boundary, or gives the user a useful anchor for deeper reading. Do not hide consequential technical implications; translate them into their behavioral effect and keep the implementation-grade form for a Bundle if the user later chooses that route.

When the user challenges a plan with a behavior-level objection, do not demand a replacement technical design. Resolve discoverable facts, state which original premise is now doubtful, and explain how the required behavior changes. A challenge may downgrade a previously claimed design or completion state.

## 4. Maintain the Internal Model

Classify consequential statements internally:

| Class | Meaning | Treatment |
| --- | --- | --- |
| Fact | Directly observed or supported by current evidence | Use as the basis for requirements and cite it when useful. |
| Assumption | Believed for now but not verified | Name what would confirm or overturn it. |
| Preference | A chosen tradeoff or desired direction | Preserve it unless it conflicts with a harder constraint. |
| Unknown | Missing information that can change the direction | Inspect, research, ask, or preserve as an open question. |

Track five readiness dimensions internally. Each is `ready` only when supported by concrete evidence, not because the conversation has mentioned the topic:

- **Problem:** who or what experiences which failure, under what condition, with what impact.
- **Goal:** the observable change needed, separate from a preferred implementation.
- **Success Criteria:** evidence that can accept or reject the next iteration, including the check method or named observation.
- **Scope:** what the current iteration owns, excludes, and is authorized to change.
- **Consistency:** contradictions are resolved or priorities are explicit where goals conflict.

Do not print a gate score or readiness dashboard. Re-evaluate all five after each answer, but continue along one decision branch instead of jumping mechanically between dimensions.

For the active branch, remember only: the gap being resolved, evidence already obtained, the number of consecutive answers that did not add concrete evidence, and any blocker. This is conversation state, not a new persistent artifact or tracker.

## 5. Generate and Rank Candidate Gaps

After each answer or inspection result, list candidate gaps internally. Eliminate gaps already answered, safely discoverable, researchable without the user, or too distant to affect the next iteration.

Rank the remaining gaps in this order:

1. a contradiction, weak premise, false problem, or solution treated as a requirement;
2. a missing concrete incident, affected actor or system, operating condition, or cost of inaction;
3. a missing causal link between the desired outcome and the proposed solution;
4. success that cannot yet be observed, falsified, or accepted;
5. a scope or priority conflict that changes the next iteration;
6. details that affect only a later stage.

Ask the highest-ranked gap whose answer can genuinely change the direction. Stay on that branch until it closes, is blocked, or is shown to be lower impact.

## 6. Form One Sharp Question

Every interview turn should contain:

- a **context anchor** from the user's words or engineering evidence;
- the **current judgment, hypothesis, or tension**;
- one **decision-relevant unknown**.

Ask one logical question and wait. A short setup may contain several statements, but it must not hide several questions. End the turn with one question and use no more than one question mark.

Use natural open questions to uncover a lived incident, motivation, dissatisfaction, or missing evidence. Use two or three options with a recommended answer when the user must choose an engineering tradeoff, boundary, or priority. When the need itself is still unformed, challenge the framing but do not recommend a solution before obtaining a concrete incident or equivalent evidence. Do not force an unformed need into premature options.

Do not ask:

- `Can you tell me more?` or another context-free invitation;
- a question already answered by the brain dump or evidence;
- several independent questions in one message;
- repeated abstract `why` questions that do not produce an incident, consequence, or choice;
- a distant design detail that cannot change the current stage;
- a question whose only purpose is to fill a framework field.

## 7. Use the Right Probing Move

Choose the move that matches the gap:

- **Concrete incident:** ask for the most recent real occurrence, including what triggered it and what failed. Use this instead of reasoning about hypothetical users.
- **Remove the proposed solution:** suppose the named mechanism is unavailable; ask which outcome must still be preserved. This separates the need from solution fixation.
- **Cost-of-inaction counterfactual:** ask what continues to fail or cost time, money, safety margin, or attention if nothing changes for a meaningful period.
- **Forced tradeoff:** when goals conflict, state the conflict, recommend a priority, and ask the user to accept or change it.
- **Contradiction replay:** quote the two incompatible claims and require one priority or a condition that reconciles them.
- **Failure falsification:** ask what observed result would prove the proposed direction did not solve the problem.
- **Scope cut:** ask what would be removed first if time, authority, or resources were halved.

Do not infer hidden psychology. A deep requirement is an engineering priority supported by an incident, consequence, tradeoff, or evidence.

## 8. Take a Position Without Leading

Directly challenge vague demand, undefined terms, hypothetical users, contradictory constraints, and weak premises. Explain the evidence or reasoning behind the challenge.

Avoid empty phrases such as `that could work`, `interesting approach`, or `you may want to consider`. Say what you think is wrong, what appears stronger, and why. A recommendation must remain correctable: present the best current position, then let the user confirm or replace it.

Do not use agreement language to conceal uncertainty. Do not turn directness into certainty unsupported by evidence.

## 9. Compare Approaches Only at a Real Fork

When two or more mechanisms or boundaries remain genuinely viable:

1. present two or three approaches;
2. lead with the recommended one and its engineering reason;
3. include a minimum-change or status-quo option when it is credible;
4. compare only the dimensions that affect this decision;
5. ask one choice question after the comparison.

Do not manufacture three versions of the same idea. A factual investigation, a settled small change, or an evidence-gathering stage does not need an artificial approach comparison.

## 10. Right-Size the Next Verification

Before proposing an experiment, baseline rebuild, or A/B comparison, identify the exact uncertainty it would resolve and the decision that would change. Prefer the cheapest faithful way to disprove the current hypothesis:

| Current state | Next verification |
| --- | --- |
| The interface contract, mechanism, and source agree on the defect | Recommend the direct correction for the build handoff; require a targeted check, one known-good regression, and one relevant failure case. |
| The cause is likely but an operational stage is unobserved | Add the minimum instrumentation needed to locate that stage, then run one representative validation. |
| Several causal explanations remain or attribution changes the design | Freeze only the influential inputs and compare the viable explanations. |
| Safety thresholds, physical envelopes, obstacle retention, irreversible effects, or noisy algorithmic tradeoffs are being changed | Use a controlled A/B or equivalent strict comparison with explicit hazards, counterexamples, and rollback evidence. |

Do not default to a complete baseline rebuild, broad parameter matrix, repeated field replay, or Benchmark because those artifacts appear rigorous. In physical systems, small changes in scene, timing, localization, and sensor observations are normal; require a new baseline only when that drift can alter the current decision. Preserve settled mechanism-level conclusions and refresh only the relevant state.

An A/B proposal must state:

- the unresolved causal fork;
- the minimum variables that must remain controlled;
- the observation that selects between the alternatives;
- why reasoning, existing evidence, a targeted test, or a representative path is insufficient;
- the stopping condition after which further comparison has no decision value.

If those items cannot be stated, do not prescribe A/B yet. Define the smaller observation or direct handoff that is actually needed. This economy does not relax safety: increase verification where a false conclusion has serious consequences, but test the concrete hazard rather than recreating the entire world.

## 11. Detect Stalls and Change Method

Track whether each answer adds concrete evidence to the active gap. After two consecutive answers fail to do so, do not ask a third direct question. The third attempt must change method:

- **Articulation stall:** the user cannot state the need but can react to something concrete. Present the smallest strawman—one sample output, behavior statement, interface, or boundary—and ask what to keep, change, or remove. The reaction is evidence; the strawman is disposable.
- **Empirical unknown:** discussion cannot answer it. Record a `research` or `prototype` gap and the evidence that would close it. Research may proceed read-only under this skill; prototype execution requires a separate handoff.
- **Missing decision input:** record a `decision` gap and what input must exist before the choice is meaningful.
- **Outside work:** record a `task` gap and the precise result that must return.

For every open question, preserve:

- the exact unknown;
- the requirement, stage, or alternative it changes;
- the minimum depth needed;
- closure type: `research`, `prototype`, `decision`, or `task`;
- the evidence that closes it;
- any other open question it depends on.

A written open question is a reason to pause, not a substitute for readiness.

## 12. Pause, Resume, and Re-enter

Pause when the user asks to stop, the remaining uncertainty depends on outside work, or the core need and next useful verification are already clear.

On resume, read the current session state or living documents. Keep settled evidence. Reopen only unresolved questions whose dependencies are now satisfied or whose prior answer has been contradicted. Do not restart the five dimensions from zero.

When new evidence arrives, identify what it changes, retain conclusions still supported, replace obsolete conclusions, and update the next iteration and its acceptance evidence.

## 13. Pressure-Test Before Documenting

Before producing a direct implementation brief or offering an Engineering Bundle, challenge the current model once:

- Are we solving a surface symptom or the real problem?
- Has the proposed scope grown beyond the outcome that justifies it?
- Is a hidden dependency or authority boundary being treated as available?
- Can the next iteration fail in a way that would disprove the current direction?

If this review exposes a consequential gap, ask the single highest-impact question and re-evaluate. Otherwise proceed without announcing an internal review ceremony.

Before stopping, internally confirm four items: the next engineering verification, evidence that accepts it, an observed result that would reject the current direction, and the scope or authority boundary for carrying it out. Stop when these items and the concrete problem, desired change, and consequential tradeoffs are clear enough to begin safely. There is no question limit, but there is also no reward for continuing after the direction is ready. The eventual architecture and distant stages may remain uncertain.

When the direction is ready, ask for one route choice: **direct implementation** or **Engineering Bundle**. Recommend direct implementation only for one bounded outcome without an unresolved architecture or safety decision; recommend a Bundle when the design is multi-stage, consequential, evidence-driven, or likely to be revised. Do not create a persistence artifact before this choice.
