# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repo (`~/projects/skills`) is the **source of truth for generic AI Factory skills** shared across all of Max's projects.

The repo keeps three concerns physically apart:
- **`src/`** — skills and commands **authored or reworked by us** (the real product).
- **`upstream/ai-factory/`** — a **pristine mirror** of `lee-to/ai-factory`'s `skills/`, refreshed by `scripts/sync-upstream.sh` and never hand-edited.
- **`active/`** — the **curated working set**: `active/skills/` and `active/commands/` hold per-item symlinks into either `src/` (ours) or `upstream/ai-factory/` (the few upstream originals we actually use). This is the only layer `~/.claude` points at, and it lists **only skills actually in use** — not every skill that exists.

Skills are available globally via `~/.claude/skills` → `~/projects/skills/active/skills` and `~/.claude/commands` → `~/projects/skills/active/commands` (personal scope in Claude Code).

Skills and commands are treated as **executable code** — they define agent runtime behavior, not documentation. Ours live under `src/` (skills in `src/skills/`, commands in `src/commands/`), deliberately outside `.claude/`, which holds Claude Code's own config that the agent must not self-edit.

This is a meta-repo: its product is skills, not application code.

## Documentation

| Doc | What it covers |
|-----|----------------|
| [Skill composition model](docs/skill-composition-model.md) | The mechanism/policy model for authoring skills — engine vs philosophy, the context-cost of abstraction, when to extract a skill. Narrative explainer (Russian); the normative rule lives in `.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy". |

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
│   └── commands/                 #   slash commands (all ours)
├── upstream/
│   └── ai-factory/               # PRISTINE mirror of lee-to/ai-factory skills/ (sync script; never hand-edited)
├── active/                       # CURATED working set — the only layer ~/.claude points at
│   ├── skills/                   #   per-skill symlinks → src/skills/* or upstream/ai-factory/*
│   └── commands/                 #   per-command symlinks → src/commands/*
├── scripts/
│   └── sync-upstream.sh          # refresh upstream/ai-factory from lee-to/ai-factory
├── .claude/                      # Claude Code project config (.mcp.json, settings.local.json)
├── .ai-factory/                  # Roadmap, notes, architecture, plans
├── CLAUDE.md
├── AGENTS.md
└── README.md
```

**The active set** (what `~/.claude` actually loads): our skills — `detangle`, `milestone-rescue`, `milestone-rescue-audit`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-engine`, `roadmap-prune`, `roadmap-test-coverage`, `temporal-tree`, `note`, `aif-docs`, `test-philosophy`, `roadmap-outline`, `observe-logs` — plus three upstream originals we use as-is: `aif`, `aif-architecture`, `aif-skill-generator`. Everything else (our `aif-plan`, `ui-ux-pro-max`; all other upstream skills) is stored but **not** symlinked into `active/`. Adding a skill to the working set = create a symlink under `active/skills/`.

Each skill directory contains:
- `SKILL.md` — required, main instructions (frontmatter + body ≤ 500 lines)
- `references/` — optional detailed docs referenced from SKILL.md
- `scripts/` — optional executable helpers (e.g. `security-scan.py`)
- `templates/` — optional output templates

## Skill Authoring

### Composition — mechanism vs policy

Factor a capability into its own skill only when it carries **shared content** (a mechanism, rule, or format) used by ≥2 callers — every loaded line is a recurring context cost, so a pure router with no content of its own is negative value. **Engine** skills hold mechanism (the shared *how*); **philosophy** skills hold policy (the gate/lens that decides) and invoke engines, staying in control. Full model: `.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy".

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

Planning and implementation are separate processes: this chat produces the roadmap and spec artifacts; the **orchestrator** (a separate run) implements them — never in the planning session. This is a hard constraint (see global CLAUDE.md).

## Upstream Sync

Upstream source: `https://github.com/lee-to/ai-factory` (skills live in the `skills/` subdirectory), mirrored into `upstream/ai-factory/`.

The three-way split makes syncing **conflict-free**: every skill we modified is moved out to `src/skills/`, so `upstream/ai-factory/` stays byte-pristine and refreshing it is an unconditional overwrite — no merge, no conflicts, nothing of ours to protect.

**Refresh the mirror:**
```bash
scripts/sync-upstream.sh      # clones upstream, rsyncs skills/ → upstream/ai-factory/ (--delete)
```

**Reconcile reworked skills (opt-in, manual).** A few of our skills were reworked from an upstream original and still have a counterpart to diff after a refresh — our copy is authoritative and is never auto-overwritten:
- `aif-docs` ↔ `upstream/ai-factory/aif-docs`
- `aif-plan` ↔ `upstream/ai-factory/aif-plan`

```bash
diff -rq src/skills/aif-docs upstream/ai-factory/aif-docs   # port upstream changes by hand if wanted
```

**Everything else in `src/skills/` is ours** — no upstream counterpart to reconcile, sync never touches it: `detangle`, `milestone-rescue`, `milestone-rescue-audit`, `roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-engine`, `roadmap-prune`, `roadmap-test-coverage`, `temporal-tree`, `note`, `test-philosophy`, `observe-logs`, `ui-ux-pro-max`.

**`src/commands/`** — all ours, no upstream source, never synced.

**Adopting a new upstream skill into the active set:** after a refresh, symlink it — `ln -sfn ../../upstream/ai-factory/<name> active/skills/<name>`. To rework one into ours, copy it into `src/skills/` and repoint its `active/` symlink there.
