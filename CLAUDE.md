# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repo (`~/projects/skills`) is the **source of truth for generic AI Factory skills** shared across all of Max's projects.

The repo keeps three concerns physically apart:
- **`src/`** — skills and commands **authored or reworked by us** (the real product).
- **`upstream/ai-factory/`** — a **pristine mirror** of `lee-to/ai-factory`'s `skills/`, refreshed by `scripts/sync-upstream.sh` and never hand-edited.
- **`active/`** — the **curated working set**: `active/skills/`, `active/commands/`, and `active/agents/` hold per-item symlinks into either `src/` (ours) or `upstream/ai-factory/` (the few upstream originals we actually use). This is the only layer `~/.claude` points at, and it lists **only skills actually in use** — not every skill that exists.

Skills are available globally via `~/.claude/skills` → `~/projects/skills/active/skills`, `~/.claude/commands` → `~/projects/skills/active/commands`, and `~/.claude/agents` → `~/projects/skills/active/agents` (personal scope in Claude Code).

The **global CLAUDE.md** (user-level instructions loaded into every session of every project) is version-controlled here too: `src/global/CLAUDE.md` is the source; `~/.claude/CLAUDE.md` → `active/CLAUDE.md` → `../src/global/CLAUDE.md`. Any write through `~/.claude/CLAUDE.md` lands in this repo's working tree and shows up in `git diff`.

Skills and commands are treated as **executable code** — they define agent runtime behavior, not documentation. Ours live under `src/` (skills in `src/skills/`, commands in `src/commands/`), deliberately outside `.claude/`, which holds Claude Code's own config that the agent must not self-edit.

This is a meta-repo: its product is skills, not application code.

## Documentation

| Doc | What it covers |
|-----|----------------|
| [Skill cycle](docs/skill-cycle.md) | How the package is used over one project cycle — idea → `roadmap-outline` (phases) → `aif-docs` (ТЗ as the phase's `Governing spec:`) → `roadmap-decompose` (∥ ТЗ amended) → `agent-architect` pass → `roadmap-decompose-skeleton` (feedback edge: skeleton surfaces spec holes → ТЗ edits) → `command-pin-gaps` → orchestrator → `milestone-rescue`/`-audit` → `roadmap-test-coverage` → `roadmap-prune` → final `aif-docs` verification pass. Descriptive sequence (Russian), the authoritative home of the order; the composition model covers the mechanism. |
| [Skill composition model](docs/skill-composition-model.md) | The mechanism/policy model for authoring skills — engine vs philosophy, the context-cost of abstraction, when to extract a skill. Narrative explainer (Russian); the normative rule lives in `.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy". |
| [Skill pyramid](docs/skill-pyramid.md) | The macro-shape of the skill graph — tiny authoritative top-level lenses over expanding engines, the CLAUDE.md analogy, hook-encoded authority (caller overrides engine defaults), the funnel of the whole family into `note`, domains as engine-trunks derived from `loads:`, and folder-carried style. Narrative explainer (Russian); the composition model covers one edge, this covers the shape the repeated rule produces. |
| [Context tree](docs/context-tree.md) | The project's knowledge as one tree — CLAUDE.md the trunk, docs the crown, code the root system, links the edges, the roadmap the time axis (the `[x]`/`[ ]` seam as the entry aim, `[x]` lines as strata with supersession); how a session raises the map at entry and walks a branch to the leaf at the moment of action, why held context decays, and why one-home-per-fact links are the walked edges. Narrative explainer (Russian); the normative rule lives in the global CLAUDE.md § "Grounding claims". |
| [Context grove](docs/context-grove.md) | The multi-repo family layer over the context tree — separate git repos under a coordination root (tradeoxy, mind); the trunk delivered mechanically by harness parent-traversal, the root-README § Setup layout guarantee as hoist's precondition (hoist leaves no pointers behind), why leaves never write upward edges and roots never enumerate consumers. Narrative explainer (Russian); the per-family entry checks live in the alignment-task specs (24/39). |

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
│   │   ├── milestone-rescue/     #     … and milestone-rescue-audit, detangle,
│   │   └── …                     #     temporal-tree, observe-logs, aif-docs, aif-plan, ui-ux-pro-max
│   ├── commands/                 #   slash commands (all ours)
│   ├── agents/                   #   agent definitions (editor — the paired-loop subagent)
│   └── global/                   #   global CLAUDE.md — user-level instructions, symlinked from ~/.claude
├── upstream/
│   └── ai-factory/               # PRISTINE mirror of lee-to/ai-factory skills/ (sync script; never hand-edited)
├── active/                       # CURATED working set — the only layer ~/.claude points at
│   ├── skills/                   #   per-skill symlinks → src/skills/* or upstream/ai-factory/*
│   ├── commands/                 #   per-command symlinks → src/commands/*
│   ├── agents/                   #   per-item symlinks → src/agents/* (e.g. editor.md)
│   └── CLAUDE.md                 #   symlink → ../src/global/CLAUDE.md (target of ~/.claude/CLAUDE.md)
├── scripts/
│   └── sync-upstream.sh          # refresh upstream/ai-factory from lee-to/ai-factory
├── .claude/                      # Claude Code project config (.mcp.json, settings.local.json)
├── .ai-factory/                  # Roadmap, specs, notes, handoffs, architecture, plans
├── CLAUDE.md
├── AGENTS.md
└── README.md
```

**The active set** (what `~/.claude` actually loads): our skills — `detangle`, `milestone-rescue`, `milestone-rescue-audit`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-engine`, `roadmap-prune`, `roadmap-test-coverage`, `temporal-tree`, `note`, `aif`, `aif-architecture`, `aif-docs`, `test-philosophy`, `roadmap-outline`, `observe-logs`, `orchestrator-artifacts`, `agent-architect` — plus one upstream original we use as-is: `aif-skill-generator`. Everything else (our `aif-plan`, `ui-ux-pro-max`; all other upstream skills) is stored but **not** symlinked into `active/`. Adding a skill to the working set = create a symlink under `active/skills/`.

Each skill directory contains:
- `SKILL.md` — required, main instructions (frontmatter + body ≤ 500 lines)
- `references/` — optional detailed docs referenced from SKILL.md
- `scripts/` — optional executable helpers (e.g. `security-scan.py`)
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
- "Behavior-identical" and "word-for-word" in spec notes are contract text — the only type system this code has. Honor them literally.
- A skill's output register (e.g. narrative prose vs. tables) is behavior, not formatting — never simplify a prose-narrative requirement into bullets or tables.
- A refactored skill is unverified until a live run compares its actual output to the pre-refactor baseline.

Pointers: `docs/skill-composition-model.md` (semantics), `docs/skill-cycle.md` (pipeline order).

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
- Body ≤ 500 lines — move details to `references/`
- All file references within a skill use relative paths

### Security scanning

Every external skill (from skills.sh, GitHub, any URL) must pass a two-level scan before use:

```bash
# Level 1 — automated
python3 ~/.claude/skills/aif-skill-generator/scripts/security-scan.py <skill-path>
# Exit 0 = clean, Exit 1 = BLOCKED (delete it), Exit 2 = warnings (proceed to Level 2)

# Level 2 — read SKILL.md and all files yourself; block if any instruction doesn't serve the stated purpose
```

Built-in `aif*` skills are never scanned at install time — only external skills are.

## Workflow for Skill Development

1. **Authoring a new skill** — use `/aif-skill-generator <name>` or Learn Mode (`/aif-skill-generator <url>`)
2. **Validate** — `/aif-skill-generator validate <path>` (structure + security)
3. **Scan only** — `/aif-skill-generator scan <path>`
4. **Publishing** — `npx skills publish <path>` to skills.sh

## How Skills Are Used in Projects

Skills from this repo are available globally to all projects via Claude Code's personal skill scope (`~/.claude/skills`). No per-project configuration needed. Projects with custom skills place them in their own `.claude/skills/` directory — Claude Code loads both scopes simultaneously. Skills are invoked as slash commands (e.g. `/roadmap-outline`, `/roadmap-decompose`). The `$ARGUMENTS` variable receives everything typed after the command name.

## Key Skill Interactions

- `/aif` → sets up project context (skills + MCP + AGENTS.md + architecture doc)
- `/aif-architecture` → generates `.ai-factory/ARCHITECTURE.md`
- `/aif-skill-generator` → creates or validates skills

**Planning chain:** `/roadmap-outline` (strategic milestones) → `/roadmap-decompose` (atomic, implementation-ready tasks) → `/roadmap-decompose-skeleton` (optional second pass: skeleton/TDD/concurrency splits on heavy tasks). Each writes two-tier artifacts (contract line + spec note) via `roadmap-engine`.

New spec notes land in `.ai-factory/specs/`; older ones still sit in `.ai-factory/notes/` and stay valid — every reader resolves the note through the contract line's `Spec:` tag, never a hardcoded directory. `.ai-factory/handoffs/` holds session handoffs, a separate genre.

Planning and implementation are separate processes: this chat produces the roadmap and spec artifacts; the **orchestrator** (a separate run) implements them — never in the planning session. This is a hard constraint (see global CLAUDE.md).

## Upstream Sync

Upstream source: `https://github.com/lee-to/ai-factory` (skills live in the `skills/` subdirectory), mirrored into `upstream/ai-factory/`.

The three-way split makes syncing **conflict-free**: every skill we modified is moved out to `src/skills/`, so `upstream/ai-factory/` stays byte-pristine and refreshing it is an unconditional overwrite — no merge, no conflicts, nothing of ours to protect.

**Refresh the mirror:**
```bash
scripts/sync-upstream.sh      # clones upstream, rsyncs skills/ → upstream/ai-factory/ (--delete)
```

**Reconcile reworked skills (opt-in, manual).** A few of our skills were reworked from an upstream original and still have a counterpart to diff after a refresh — our copy is authoritative and is never auto-overwritten:
- `aif` ↔ `upstream/ai-factory/aif`
- `aif-architecture` ↔ `upstream/ai-factory/aif-architecture`
- `aif-docs` ↔ `upstream/ai-factory/aif-docs`
- `aif-plan` ↔ `upstream/ai-factory/aif-plan`

```bash
diff -rq src/skills/aif upstream/ai-factory/aif             # port upstream changes by hand if wanted
diff -rq src/skills/aif-architecture upstream/ai-factory/aif-architecture
diff -rq src/skills/aif-docs upstream/ai-factory/aif-docs
```

**Everything else in `src/skills/` is ours** — no upstream counterpart to reconcile, sync never touches it: `detangle`, `milestone-rescue`, `milestone-rescue-audit`, `roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-engine`, `roadmap-prune`, `roadmap-test-coverage`, `temporal-tree`, `note`, `test-philosophy`, `observe-logs`, `ui-ux-pro-max`, `agent-architect`. The same holds for `src/agents/` — the `editor` agent definition has no upstream counterpart; a re-sync must never overwrite it.

**`src/commands/`** — all ours, no upstream source, never synced.

**Adopting a new upstream skill into the active set:** after a refresh, symlink it — `ln -sfn ../../upstream/ai-factory/<name> active/skills/<name>`. To rework one into ours, copy it into `src/skills/` and repoint its `active/` symlink there.
