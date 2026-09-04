# Engineering Plan Interpretation

Use this reference when a technical owner needs to understand or challenge an existing Engineering Bundle, and immediately after the design workflow creates or materially updates one. The output is a Human-readable Mapping in the conversation. It does not replace, simplify, or mutate the technical source by itself.

## Read the Plan as a Decision Map

Read the complete plan before translating it. When it belongs to an Engineering Bundle, read `MAP.md` first, then the current stage and only the linked evidence that can change a consequential status judgment.

Identify the plan's semantic anchors:

- major problem blocks and their original order or numbering;
- the observed failure each block claims to address;
- causal dependencies between proposals;
- existing capability versus proposed change;
- implementation and verification state;
- safety, compatibility, and architecture responsibility boundaries;
- acceptance evidence, rejection conditions, and later stages;
- headings, identifiers, or technical terms that let the reader return to the source.

Preserve these anchors. Small headings, paragraph order inside a block, repeated details, and low-value implementation mechanics may be compressed or rearranged.

## Translate by Semantic Block

For every major block, make the following decision chain understandable without turning it into a rigid form:

1. What is happening now in system or operator-visible terms.
2. What the proposed or implemented change actually changes.
3. How the system will behave differently.
4. Which observed problem it directly solves.
5. What it may improve indirectly and what it cannot solve.
6. What a person should observe to accept it.
7. What result would reject the direction or reveal a different problem.

Lead with behavior and observable effect. Introduce a technical term afterward as an anchor when it helps the reader find or question the source. Do not remove a term that carries architecture, safety, compatibility, or state meaning.

Do not translate sentence by sentence. One technical sentence may require several behavioral sentences; a long parameter table may become one decision-relevant statement.

## Protect Status Truth

Keep these states distinct when they appear:

```text
existing capability
implemented, not validated
validated by targeted source or unit checks
validated offline
validated in simulation or a non-moving closed loop
validated on hardware or in the field
planned, not implemented
optional or disabled
rejected or rolled back
```

Do not infer a stronger state from a weaker one. A build or unit test is not an offline system result; an offline result is not simulation; simulation is not hardware acceptance; a commit or pull request is not delivery acceptance.

Use layered verification:

1. Treat the plan as the source of what it claims.
2. Inspect directly referenced and readily available evidence only when it can confirm or overturn a consequential status.
3. Label the result as source-declared, independently verified, or not independently verified.
4. Stop when further inspection would become a general code, architecture, or delivery audit.

When evidence conflicts with the plan, surface the conflict. Do not silently repair the source or choose the more convenient version.

## Allocate Attention by Decision Value

Expand:

- the root mechanism and the visible failure it produces;
- the behavior change after implementation;
- safety and compatibility boundaries;
- module responsibility changes;
- consequential tradeoffs;
- problem coverage and uncovered causes;
- acceptance observations and rejection signals.

Compress by default:

- function, class, and member names;
- file paths and edit inventories;
- ordinary parameter defaults;
- formulas after their behavioral consequence is clear;
- exhaustive log fields and routine test implementation;
- corner cases that do not affect the user's current decision.

This is written for a technical owner, not a novice. Prefer direct engineering language over analogies or simplified teaching prose.

## Default Conversation Shape

Use two levels of disclosure.

First, in one to three short paragraphs, explain what the whole plan is intended to change and summarize the actual implementation and validation state.

Then follow the source plan's major order. Give each block a recognizable number or anchor and explain its observable behavior, coverage boundary, and acceptance evidence. Do not force identical headings on every block.

Finish by collecting:

- what is already available, what remains planned, and what still lacks real-system validation;
- the smallest next test observations that can change the decision;
- failure signals that would reject the current interpretation or plan;
- source headings or technical anchors for deeper reading.

Make the view easy to scan, but do not reduce it to slogans. Remove repetition before removing safety, status, causal, or rejection information.

## Correction and Confirmation Loop

When the user corrects an effect, boundary, premise, or acceptance interpretation:

1. identify the affected technical semantic block;
2. inspect any discoverable fact that determines whether the objection is valid;
3. revise the technical block before changing the mapping;
4. downgrade any design or completion claim no longer supported;
5. retranslate the affected block in the conversation;
6. after all corrections settle, present the complete mapping again.

Do not treat agreement with one translated block as approval of the whole Bundle. The Bundle is ready for `$engineering-build` only after explicit confirmation that the complete mapped behavior, boundaries, and acceptance reflect the user's intent.

## Misalignment and Non-goals

Interpretation may judge whether the plan addresses the observed problem and whether its claimed state has adequate support. It must not become a redesign, architecture review, code review, mathematical proof, product interview, priority-setting exercise, or approval decision.

If a block solves a different mechanism from the one the user experiences, say precisely what it solves and what remains unexplained. Re-enter requirements discovery only when that mismatch changes the goal, scope, or next iteration.

## Persistence Boundary

The technical Bundle remains pure implementation-grade material. Do not write the Human-readable Mapping into `MAP.md`, a stage document, a new Bundle file, or a template. If the user explicitly wants a persistent interpretation, ask for or use a destination outside the Bundle and preserve a link back to the source plan.
