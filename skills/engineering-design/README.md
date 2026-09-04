# Engineering Design

An Agent Skill for turning a human-language engineering need into either a compact implementation brief or a confirmed technical Engineering Bundle.

```text
Human-language discussion
          |
          v
Aligned behavior and boundaries
          |
          +-- small change --> Direct implementation brief
          |
          `-- durable design --> Engineering Bundle
                                  + Human-readable Mapping
```

The conversation stays focused on system behavior, observable outcomes, boundaries, and responsibility. The skill performs the technical inspection and reasoning needed to protect architecture, safety, compatibility, and acceptance without asking the user to review every function, parameter, or corner case.

## Two routes

### Direct implementation

For one small, bounded outcome, the skill returns a concise brief covering the goal, what must be preserved, forbidden shortcuts, acceptance, and rejection signals. It creates no persistent document and does not invoke `engineering-build`.

### Engineering Bundle

For multi-stage or consequential work, the skill maintains a local, technical Bundle:

```text
<project-key>-<topic-key>-engineering-bundle/
├── MAP.md
├── 01-<outcome-key>.md
├── 02-<outcome-key>.md
└── ...
```

After creating or revising the Bundle, the skill presents a conversation-only Human-readable Mapping in the same semantic order. The user confirms system behavior and boundaries without losing the ability to return to the technical source.

A confirmed Bundle is the only stable interface to [`engineering-build`](https://github.com/Bolpccc/engineering-build). The Build skill implements it, updates evidence-backed status, and returns design-invalidating discoveries here for a new decision.

## Boundaries

This skill does not implement code, run experiments, operate hardware, deploy, manage project trackers, or publish external documents. It creates persistent files only when the user selects the Bundle route.

## Install

```bash
git clone https://github.com/Bolpccc/engineering-design.git \
  ~/.codex/skills/engineering-design
```

## Use

```text
Use $engineering-design to clarify this behavior change and help me choose a direct implementation brief or an Engineering Bundle.
```

For an existing Bundle:

```text
Use $engineering-design to review and revise the design in /path/to/example-engineering-bundle/.
```

## Repository structure

```text
SKILL.md
agents/openai.yaml
references/requirements-interview.md
references/document-model.md
references/research-for-decisions.md
references/plan-interpretation.md
assets/engineering-bundle/MAP.template.md
assets/engineering-bundle/STAGE.template.md
```

Diagrams are opt-in. The skill does not create or propose one unless the user explicitly requests it; requested diagrams use [`mermaid-skill`](https://github.com/Agents365-ai/creating-mermaid-diagrams). External publication remains a separate, explicitly authorized workflow.

## 中文说明

`engineering-design` 负责把“我想让系统怎样表现”变成可确认的工程定义。讨论阶段优先使用人能直接判断的行为和结果语言；技术分析、架构约束、安全边界和验收条件由 Skill 在后台完成并保存在必要的技术 Bundle 中。

需求收敛后有两条路：

- 小而明确的修改：只输出一次性实施要求，不生成文档。
- 中大型或需要持续修订的工作：生成 Engineering Bundle，并按相同结构给出人话映射，确认后交给 `engineering-build`。

Bundle 是两个 Skill 之间唯一稳定接口。实施发现设计假设不成立时，返回本 Skill 修订，而不是在 Build 阶段偷偷改变系统意图。

MIT License. See [LICENSE](LICENSE).
