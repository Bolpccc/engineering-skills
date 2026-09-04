# Lightweight Engineering Bundle

Use this model only after the user selects the Engineering Bundle route or supplies an existing Bundle. The Bundle is the technical, implementation-grade interface between `$engineering-design` and `$engineering-build`: one global map and one continuous document per outcome-based stage. Requirements, plans, and decision notes remain semantic responsibilities inside that writing, not a page taxonomy.

## Persistence Boundary

- Do not create a document during ordinary discussion or for the direct implementation route.
- A new Bundle requires both the user's Bundle choice and a designated local workspace. Without a location, keep the aligned design in the conversation and ask for the destination before persisting it.
- In a designated workspace, locate an existing equivalent before creating anything. Preserve useful content, links, evidence, and the existing local structure.
- Use a Bundle when work spans dependent outcomes, carries consequential architecture, safety, interface, or verification decisions, is likely to change across evidence cycles, or needs a durable technical handoff.
- Keep the Human-readable Mapping in the conversation. It is not a second document layer or a simplified copy of the Bundle.
- Do not duplicate a source of truth merely to make the bundle look self-contained.

## Local Markdown Shape

Use one flat directory:

```text
<project-key>-<topic-key>-engineering-bundle/
├── MAP.md
├── 01-<outcome-key>.md
├── 02-<outcome-key>.md
├── 03-<outcome-key>.md
└── assets/                    # only when real non-embedded artifacts exist
```

Do not create `stages/`, stage directories, stage `README.md` files, or files named after internal categories such as `requirements.md`, `architecture.md`, `implementation-plan.md`, `verification.md`, or `decisions.md`. Those separations force a reviewer to reconstruct one design argument across several files.

Create `assets/` only for an image, raw attachment, or other real artifact that cannot reasonably be embedded or linked at its existing source. Name a local artifact `<stage-id>-<purpose-key>.<ext>`. Do not create an empty assets directory.

## Stable Naming Contract

Bundle and stage names are derived, not improvised:

- Bundle directory: `<project-key>-<topic-key>-engineering-bundle`.
- Stage document: `NN-<outcome-key>.md`, with a two-digit stage number.
- Appendix, only after explicit user approval: `appendix-<purpose-key>.md`.

Use lowercase English ASCII kebab-case for filesystem keys and the project's main language for reader-facing Markdown titles.

Derive keys in this order:

1. `project-key` comes from the repository, product, or project's existing canonical identifier. Do not create a shorter alias for convenience.
2. `topic-key` comes from the aligned engineering problem. Do not name the bundle after a proposed solution unless that solution has become the agreed scope.
3. `outcome-key` names the observable engineering result of the stage, preferably with a concrete verb and object, such as `understand-current-system` or `define-target-architecture`.

Reject weak keys such as `phase-1`, `misc`, `optimization`, `new-design`, or another label that does not say what becomes true. Do not add dates, status, authors, or content versions to filenames.

Reuse an existing confirmed key for the same project, topic, or stage. When no stable English key exists, propose one recommended key, state which agreed phrase it represents, and wait for confirmation before creating the bundle or new stage. Once confirmed, keep the key stable across later wording changes. Rename it only when the engineering scope or outcome materially changes, then update every affected link in the same bounded edit.

## MAP.md

Use [MAP.template.md](../assets/engineering-bundle/MAP.template.md) as a responsibility guide. The map should be understandable in under a minute and contain only:

- why the bundle exists and what overall success means;
- the current stage, why it is current, and what it unlocks;
- numbered stage outcomes, entry conditions, completion evidence, dependencies, and links;
- shared constraints and confirmed decisions that affect more than one stage;
- a route diagram only when the user explicitly requested one.

The map is not a dashboard or executive summary. Do not add owners, deadlines, issue state, evidence taxonomies, change logs, or repeated stage summaries. Keep one current stage unless the work is explicitly paused or all stages are complete.

The linked stage list is the required route model; a diagram is optional and opt-in. When the user explicitly requests a route diagram, keep it consistent with the linked stage list. During later edits, do not silently redraw an existing diagram. If the changed route would make it materially false, surface the mismatch and ask whether to update or remove it.

## Stage Document

Use [STAGE.template.md](../assets/engineering-bundle/STAGE.template.md) as a responsibility guide, not a form to fill. A stage document should let a person follow one continuous engineering argument from the problem to the proposed implementation and its verification.

For the current stage, preserve the content needed to understand:

- the actual problem, impact, and intended outcome;
- confirmed facts, requirements, constraints, and necessary assumptions;
- how the design developed and which tradeoffs changed it;
- the current architecture or implementation direction and affected scope;
- evidence that accepts the stage and an observed result that would reject the direction;
- unresolved questions that still require human judgment;
- source, evidence, and research links that affect the current decision.

These are content responsibilities, not mandatory headings. Combine them into natural project-language prose, rename or merge headings, and omit empty sections. Do not label every paragraph as fact, assumption, preference, unknown, requirement, or decision.

Keep the next stage directional: goal, entry condition, likely result, and completion boundary. Keep later stages skeletal: purpose, dependency, and completion boundary only. Expand them when evidence brings them closer.

Do not split a stage merely because it becomes long. First remove obsolete process notes, duplicated evidence, and material that belongs at its original source. Only when the document can no longer be reviewed effectively in one pass may the agent recommend one purpose-specific appendix. Create it only after the user explicitly agrees; never introduce a nested stage tree.

## Resume and Joint Editing

On every return to an existing bundle:

1. Read `MAP.md` first.
2. Resolve its current-stage link and read that stage document.
3. Load only linked material that can change the current decision.
4. Inspect relevant current-system evidence before treating a factual edit as verified.
5. Continue from the current gap rather than restarting discovery.

Direct human edits are part of the shared current model. Preserve changed decisions, priorities, and preferences. Check factual, evidentiary, and technical claims against available evidence. If a manual edit conflicts with another constraint, stage boundary, or acceptance condition, state the conflict and resolve the highest-impact decision instead of silently choosing one version or restoring old prose.

## Narrow Update Rule

- Ordinary implementation, simulation, test, field, or research evidence updates only the affected stage.
- Update the map only when the current marker, stage order, dependency, shared constraint, key decision, or document link changes.
- Leave unrelated stages untouched.
- When work advances, expand the newly current stage and compress the completed stage to its durable conclusion, decisive tradeoffs, and valid evidence.
- Remove obsolete current statements rather than leaving contradictory versions or adding a chronological change ledger.
- Use Git or the host workspace's revision history for change history. Do not create a parallel change-request or task system.

## Build Handoff Readiness

The current stage is ready to hand to a separate BUILD workflow only when one document can explain:

- the implementation outcome and affected scope;
- the selected design and consequential tradeoffs;
- constraints and assumptions the implementer must preserve;
- evidence that will accept the implementation;
- a result that would reject the current direction;
- open questions that still block or could materially change implementation.

If a consequential item is missing, continue discovery or frame the precise research, prototype, decision, or outside task that will close it. This skill does not perform the build.

Readiness is necessary but not sufficient. After the technical Bundle is ready, present the complete Human-readable Mapping and incorporate user corrections into the affected technical blocks. The Bundle becomes a valid handoff to `$engineering-build` only after the user explicitly confirms that the mapped behavior, boundaries, and acceptance match their intent.

Record the handoff by returning the Bundle path and, when available, the current Git revision or another stable content identity in the conversation. Do not add owners, status workflow, approval records, or a parallel task system to the Bundle itself.

## External Publication Boundary

This skill produces and revises the local bundle only. Do not publish, synchronize, or adapt it to an external document system during discovery.

After the user has reviewed the local files and explicitly confirmed that the bundle is complete and ready to publish, hand the confirmed paths and current revision to a separate publication workflow. Approval to create, edit, or finish the local bundle is not publication approval. If local content changes after confirmation, require a new publication confirmation for the revised content.
