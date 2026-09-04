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

## Build the Domain Mapping Packet

For every major block, recover this decision chain before presentation:

1. What is happening now in system or operator-visible terms.
2. What the proposed or implemented change actually changes.
3. How the system will behave differently.
4. Which observed problem it directly solves.
5. What it may improve indirectly and what it cannot solve.
6. What a person should observe to accept it.
7. What result would reject the direction or reveal a different problem.

Keep each link traceable to its source anchor. Do not remove a term that carries architecture, safety, compatibility, or state meaning. The packet is a semantic contract, not a sentence-by-sentence rewrite or a required user-facing template.

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

## Mark Decision Value

Mark these as high decision value so the cognitive presentation cannot compress them away:

- the root mechanism and the visible failure it produces;
- the behavior change after implementation;
- safety and compatibility boundaries;
- module responsibility changes;
- consequential tradeoffs;
- problem coverage and uncovered causes;
- acceptance observations and rejection signals.

Mark these as normally compressible unless they change the user's decision:

- function, class, and member names;
- file paths and edit inventories;
- ordinary parameter defaults;
- formulas after their behavioral consequence is clear;
- exhaustive log fields and routine test implementation;
- corner cases that do not affect the user's current decision.

## Cognitive Composition Handoff

After the domain packet is complete, load `$cognitive-bridge` with:

```text
purpose: review
source_content: the complete domain mapping packet
must_preserve: original block order, anchors, causal links, coverage, safety,
               interfaces, status, acceptance, and rejection conditions
source_anchors: Bundle headings, identifiers, and consequential technical terms
current_model_evidence: the user's own phrases, accepted relations, objections,
                        and demonstrated understanding from this design discussion
desired_depth: quick | standard | deep, inferred from the current request
```

The default result should first make the whole intended behavior and actual plan
state usable, then follow the Bundle's major semantic order. It must finish with
what exists, what is planned, what lacks validation, the next decision-changing
observations, rejection signals, and anchors for deeper reading. Cognitive
composition may change local exposition but must not merge, reorder, or weaken
the Bundle correspondence required for confirmation.

If the companion is unavailable, produce that minimum domain-preserving shape
directly and label it `Cognitive adaptation unavailable`.

## Correction and Confirmation Loop

When the user corrects an effect, boundary, premise, or acceptance interpretation, `$engineering-design` owns this loop:

1. identify the affected technical semantic block;
2. inspect any discoverable fact that determines whether the objection is valid;
3. revise the technical block before changing the mapping;
4. downgrade any design or completion claim no longer supported;
5. rebuild the affected mapping packet and invoke `$cognitive-bridge` again;
6. after all corrections settle, present the complete mapping again.

Do not treat agreement with one translated block as approval of the whole Bundle. The Bundle is ready for `$engineering-build` only after explicit confirmation that the complete mapped behavior, boundaries, and acceptance reflect the user's intent.

## Misalignment and Non-goals

Domain mapping may judge whether the plan addresses the observed problem and whether its claimed state has adequate support. Cognitive composition must not become a redesign, architecture review, code review, mathematical proof, product interview, priority-setting exercise, or approval decision.

If a block solves a different mechanism from the one the user experiences, say precisely what it solves and what remains unexplained. Re-enter requirements discovery only when that mismatch changes the goal, scope, or next iteration.

## Persistence Boundary

The technical Bundle remains pure implementation-grade material. Do not write the Human-readable Mapping into `MAP.md`, a stage document, a new Bundle file, or a template. If the user explicitly wants a persistent interpretation, ask for or use a destination outside the Bundle and preserve a link back to the source plan.
