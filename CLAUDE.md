## Purpose

This repo (`~/projects/skills`) is the **source of truth for generic AI Factory skills** shared across all of Max's projects.

The repo keeps two concerns physically apart:
- **`src/`** — skills and commands **authored or reworked by us** (the real product).
- **`active/`** — the **curated working set**: `active/skills/`, `active/commands/`, and `active/agents/` hold per-item symlinks into `src/`. This is the only layer `~/.claude` points at, and it lists **only skills actually in use** — not every skill that exists.

Skills are available globally via `~/.claude/skills` → `~/projects/skills/active/skills`, `~/.claude/commands` → `~/projects/skills/active/commands`, and `~/.claude/agents` → `~/projects/skills/active/agents` (personal scope in Claude Code).

The **global CLAUDE.md** (user-level instructions loaded into every session of every project) is version-controlled here too: `src/global/CLAUDE.md` is the source; `~/.claude/CLAUDE.md` → `active/CLAUDE.md` → `../src/global/CLAUDE.md`. Any write through `~/.claude/CLAUDE.md` lands in this repo's working tree and shows up in `git diff`.

Skills and commands are treated as **executable code** — they define agent runtime behavior, not documentation. Ours live under `src/` (skills in `src/skills/`, commands in `src/commands/`), deliberately outside `.claude/`, which holds Claude Code's own config that the agent must not self-edit.

This is a meta-repo: its product is skills, not application code.

## Documentation

### The language — read first

The whole package is written in one semantic vocabulary — the tech stack everything below is written in. These three docs are its home:

- **[Reserved words](docs/reserved-words.md)** — which words are fixed, each with one meaning, across the product we author. English reference lexicon.
- **[Using the language](docs/using-the-language.md)** — where that vocabulary binds and where it is only available.
- **[skill-description-field](docs/skill-description-field.md)** — how that vocabulary loads as always-present context.

### Guides

| Doc | What it covers |
|-----|----------------|
| [Sakshi harness](docs/sakshi-harness/sakshi-harness.md) | How an otherwise-independent fleet of project repos is wired into one authoring system, and what loads where. Narrative explainer (Russian); the entry point for this folder. |
| [Skill cycle](docs/sakshi-harness/skill-cycle.md) | In what order the package is used over one project cycle. Descriptive sequence (Russian), the authoritative home of the order. |
| [Skill graph](docs/sakshi-harness/skill-graph.md) | How skills divide into engines and lenses, and the shape that division takes at scale. Narrative explainer (Russian). |
| [Always-loaded discipline](docs/always-loaded-discipline.md) | What the always-loaded layer holds, and how it produces behaviour with no skill invoked. Narrative explainer (English). |
| [Reference by name](docs/reference-by-name.md) | Why a reference addresses a thing by name and never by position. Narrative explainer (English). |
| [Context tree](docs/philosophy/context-tree.md) | How a project's knowledge is one tree, and how a session raises its map and walks a branch to the leaf. Narrative explainer (Russian). |
| [Context grove](docs/philosophy/context-grove.md) | How the tree extends over several repositories under one coordinating root. Narrative explainer (Russian). |
| [Multiuser roadmaps](docs/philosophy/multiuser-roadmaps.md) | How each developer keeps a named roadmap and its artifacts beside the default layout. Governing spec (Russian). |
| [Paired loop](docs/paired-loop.md) | How the architect↔editor pair works as one working memory, and how architects work with one another. Governing spec (English). |
| [Test-coverage pass](docs/test-coverage-pass.md) | Why `roadmap-test-coverage` works as it does, and where its gaps lie. Governing spec (English). |
| [What a task carries](docs/what-a-task-carries.md) | What a task spec holds, who reads it, and where a task's source lies. Governing spec (English). |
| [Instruction in data](docs/instruction-in-data.md) | Why a rule written into the artifact it governs does not execute, and where it has to live instead. |
| [Self-analysis](docs/self-analysis.md) | What an agent's account of its own behaviour is worth. |
| [Counts go stale](docs/counts-go-stale.md) | What a number in a durable artifact is, and why it goes stale. |
| [Names and reasons, not laws](docs/names-and-reasons-not-laws.md) | What a durable text gives an agent reader: a name, a reason or a question, never a law written in advance. |
| [Principles at their moment](docs/philosophy/principles-at-their-moment.md) | How a well-known principle is carried as one question, asked where its decision is made. |
| [The pipeline speaks to an architect](docs/the-pipeline-speaks-to-an-architect.md) | How the orchestrator's agents reach an architect directly. Narrative (English). |
| [A head that speaks as the customer](docs/futures/a-head-that-speaks-as-the-customer.md) | A possible future, not decided — ideas, not a governing spec: a head with no hand that speaks as the customer. Narrative (English). |
| [A monthly analysis sprint, and the service that holds the environment](docs/futures/a-monthly-analysis-sprint-and-the-service-that-holds-the-environment.md) | A possible future, not decided — ideas, not a governing spec: a monthly analysis sprint and the service that holds its environment. Narrative (English). |

## Repository Structure

```
skills/
├── src/                          # OURS — authored or reworked by us
│   ├── skills/                   #   custom + reworked-from-upstream + originally ours
│   │   ├── roadmap-decompose/    #     atomic-deliverability decomposition
│   │   ├── roadmap-decompose-skeleton/ # skeleton/TDD/concurrency lens
│   │   ├── roadmap-engine/       #     two-tier artifact format
│   │   ├── roadmap-outline/      #     strategic high-level roadmap
│   │   ├── roadmap-prune/
│   │   ├── roadmap-test-coverage/
│   │   ├── note/                 #     research-summary note writer
│   │   ├── test-philosophy/      #     shared silent-failure testing rule
│   │   ├── task-rescue/          #     … and detangle,
│   │   └── …                     #     temporal-tree, observe-logs, aif-docs, aif-plan, ui-ux-pro-max
│   ├── commands/                 #   slash commands (all ours)
│   ├── agents/                   #   agent definitions (editor — the paired-loop subagent)
│   └── global/                   #   global CLAUDE.md — user-level instructions, symlinked from ~/.claude
├── active/                       # CURATED working set — the only layer ~/.claude points at
│   ├── skills/                   #   per-skill symlinks → src/skills/*
│   ├── commands/                 #   per-command symlinks → src/commands/*
│   ├── agents/                   #   per-item symlinks → src/agents/* (e.g. editor.md)
│   └── CLAUDE.md                 #   symlink → ../src/global/CLAUDE.md (target of ~/.claude/CLAUDE.md)
├── upstream/                     # the sources we follow, one tracked file each; their local clones beside them, git-ignored
├── scripts/
│   └── compare-sources.sh        # fetch the sources we follow and diff our counterparts against them; writes nothing tracked
├── .claude/                      # Claude Code project config (.mcp.json, settings.local.json)
├── .ai-factory/                  # Roadmap, specs, notes, handoffs, architect folders, architecture, plans
├── CLAUDE.md
├── AGENTS.md
└── README.md
```

**The active set** (what `~/.claude` actually loads): our skills — `detangle`, `task-rescue`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-engine`, `roadmap-prune`, `roadmap-test-coverage`, `temporal-tree`, `note`, `aif`, `aif-architecture`, `aif-docs`, `test-philosophy`, `polymorphism-philosophy`, `roadmap-outline`, `roadmap-outline-deep`, `observe-logs`, `orchestrator-artifacts`, `agent-architect`, `architect-editor-engine`. Everything else (our `aif-plan`, `ui-ux-pro-max`) is stored but **not** symlinked into `active/`. Adding a skill to the working set = create a symlink under `active/skills/`.

Each skill directory contains:
- `SKILL.md` — required, main instructions (frontmatter + body ≤ 500 lines)
- `references/` — optional detailed docs referenced from SKILL.md
- `scripts/` — optional executable helpers (e.g. `design_system.py`)
- `templates/` — optional output templates

## Skill Authoring

### Composition — mechanism vs policy

Factor a capability into its own skill only when it carries **shared content** (a mechanism, rule, or format) used by ≥2 callers — every loaded line is a recurring context cost, so a pure router with no content of its own is negative value. **Engine** skills hold mechanism (the shared *how*); **philosophy** skills hold policy (the gate/lens that decides) and invoke engines, staying in control. Full model: `.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy".

### Dependencies and the skill graph

Every skill that loads another declares it in its own frontmatter `loads:` field (space-separated skill names) — colocated with the depending skill, not in a separate map. Direction is one-way: engines never list their callers, so there is no `loaded-by:` field anywhere.

- **Forward graph** (what a skill loads): read its `loads:` field.
- **Reverse graph** (who loads a skill): `grep -l "<name>" src/skills/*/SKILL.md src/commands/*.md`.

The declarations *are* the map — there is no central dependency map to generate or keep in sync. Do not add one.

The coupling is declared on both sides: the caller's frontmatter states *whom* it loads; the engine's body states *that it is loaded* and how to find by whom — every engine (any skill named in a `loads:` field) carries a reverse-graph marker in its body, added when the first `loads:` edge to it appears.

Cross-file invariants that grep can't derive — a shared output register, a table that must stay mirrored across two files — get one sentence declared at the coupling point in **both** files, not just one.

Editing rules that follow from this:
- Before touching an engine (e.g. `roadmap-engine`, `test-philosophy`), grep for its callers — their expectations are part of its contract.
- Never inline an engine's content into a philosophy skill that calls it; load it instead.
- "Behavior-identical" and "word-for-word" in task specs are contract text — the only type system this code has. Honor them literally.
- A skill's output register (e.g. narrative prose vs. tables) is behavior, not formatting — never simplify a prose-narrative requirement into bullets or tables.
- A refactored skill is unverified until a live run compares its actual output to the pre-refactor baseline.

Pointers: `docs/sakshi-harness/skill-graph.md` (semantics), `docs/sakshi-harness/skill-cycle.md` (pipeline order).

### SKILL.md frontmatter (required fields)

```yaml
---
name: skill-name           # lowercase, hyphens only, ≤ 64 chars, matches directory name
description: >-            # what it does + when to use it, ≤ 1024 chars
  ...
argument-hint: "[arg]"     # MUST quote brackets — unquoted breaks YAML in some agents
allowed-tools: Read Write  # pre-approved tools
---
```

### Key constraints

- `name` must match the directory name exactly
- `argument-hint` values containing `[...]` **must** be quoted (single or double quotes)
- Body ≤ 500 lines — a loaded line costs context on every run, so move to `references/` what only some runs read; a body used whole on every run gains nothing from a split
- All file references within a skill use relative paths

### Security scanning

An external skill is read whole before use, and an instruction that does not serve its stated purpose blocks it.

## Workflow for Skill Development

1. **Authoring a new skill** — write `src/skills/<name>/SKILL.md` to the constraints above

## How Skills Are Used in Projects

Skills from this repo are available globally to all projects via Claude Code's personal skill scope (`~/.claude/skills`). No per-project configuration needed. Projects with custom skills place them in their own `.claude/skills/` directory — Claude Code loads both scopes simultaneously. Skills are invoked as slash commands (e.g. `/roadmap-outline`, `/roadmap-decompose`). The `$ARGUMENTS` variable receives everything typed after the command name.

## Key Skill Interactions

- `/aif` → sets up project context (skills + MCP + AGENTS.md + architecture doc)
- `/aif-architecture` → generates `.ai-factory/ARCHITECTURE.md`

**Planning chain:** `/roadmap-outline` (strategic phases) → `/roadmap-decompose` (atomic, implementation-ready tasks) → `/roadmap-decompose-skeleton` (optional second pass: skeleton/TDD/concurrency splits on heavy tasks). Each writes two-tier artifacts (contract line + task spec) via `roadmap-engine`.

New task specs land in `.ai-factory/specs/`; older ones still sit in `.ai-factory/notes/` and stay valid — every reader resolves the task spec through the contract line's `Spec:` tag, never a hardcoded directory. `.ai-factory/handoffs/` holds session handoffs, a separate genre; `.ai-factory/architects/<user-slug>/` holds one folder per architect of that user, `<NN>`, each with its buffer, its snapshots and its address file.

Planning and implementation are separate processes: this chat produces the roadmap and spec artifacts; the **orchestrator** (a separate run) implements them — never in the planning session. This is a hard constraint (see global CLAUDE.md).

## Sources We Follow

Other people's repositories are sources we compare against, never code we commit. The sources we follow and their check history live in `upstream/`, one file per source: its `URL:`, why we follow it, the skills of ours that share an origin with it (`Counterparts:`), and dated entries, each with a `Last seen:` commit. The clone sits beside its file as `upstream/<repo-name>/`, which git ignores. `scripts/compare-sources.sh` reads those files, clones a source on first use and fetches it after, diffs our counterparts against theirs and prints what moved. It writes nothing tracked, and no source is mirrored.

**Everything else in `src/skills/` is ours** — no counterpart in any source: `detangle`, `task-rescue`, `roadmap-outline`, `roadmap-outline-deep`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-engine`, `roadmap-prune`, `roadmap-test-coverage`, `temporal-tree`, `note`, `test-philosophy`, `polymorphism-philosophy`, `observe-logs`, `ui-ux-pro-max`, `orchestrator-artifacts`, `agent-architect`, `architect-editor-engine`. The same holds for `src/agents/` (the `editor` agent definition) and `src/commands/`.
