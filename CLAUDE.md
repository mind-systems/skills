# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repo (`~/projects/skills`) is the **source of truth for generic AI Factory skills** shared across all of Max's projects. Skills are available globally via `~/.claude/skills` → `~/projects/skills/src/skills` (personal scope in Claude Code).

Skills and commands are treated as **executable code** — they define agent runtime behavior, not documentation. They live under `src/` (skills in `src/skills/`, commands in `src/commands/`), deliberately outside `.claude/`, which holds Claude Code's own config that the agent must not self-edit.

This is a meta-repo: its product is skills, not application code.

## Repository Structure

```
skills/
├── src/
│   ├── skills/             # Skill packages (symlinked to ~/.claude/skills)
│   │   ├── aif/            #   project setup & MCP configuration
│   │   ├── aif-plan/       #   feature planning → .ai-factory/plans/
│   │   ├── aif-*/          #   other AI Factory lifecycle skills
│   │   ├── detangle/       #   untangle complex diffs / branches
│   │   ├── milestone-rescue/
│   │   ├── roadmap-prune/
│   │   ├── temporal-tree/
│   │   └── ui-ux-pro-max/
│   └── commands/           # Slash commands (symlinked to ~/.claude/commands)
│       ├── command-handoff.md
│       └── command-pin-gaps.md
├── .claude/                # Claude Code project config (.mcp.json, settings.local.json)
├── .ai-factory/            # Roadmap, notes, architecture, plans
├── CLAUDE.md
├── AGENTS.md
└── README.md
```

Each skill directory contains:
- `SKILL.md` — required, main instructions (frontmatter + body ≤ 500 lines)
- `references/` — optional detailed docs referenced from SKILL.md
- `scripts/` — optional executable helpers (e.g. `security-scan.py`)
- `templates/` — optional output templates

## Skill Authoring

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

Skills from this repo are available globally to all projects via Claude Code's personal skill scope (`~/.claude/skills`). No per-project configuration needed. Projects with custom skills place them in their own `.claude/skills/` directory — Claude Code loads both scopes simultaneously. Skills are invoked as slash commands (e.g. `/aif-plan`, `/aif-implement`). The `$ARGUMENTS` variable receives everything typed after the command name.

## Key Skill Interactions

- `/aif` → sets up project context (skills + MCP + AGENTS.md + architecture doc)
- `/aif-plan` → creates `.ai-factory/plans/<NN>-<slug>.md`, then **stops** — never implements
- `/aif-implement` → executes an existing plan file
- `/aif-architecture` → generates `.ai-factory/ARCHITECTURE.md`
- `/aif-skill-generator` → creates or validates skills

The plan → stop → implement-in-separate-session pattern is a hard constraint (see global CLAUDE.md).

## Upstream Sync

Upstream source: `https://github.com/lee-to/ai-factory` (skills live in `skills/` subdirectory).

**Custom skills — never overwrite from upstream:**
- `detangle`, `milestone-rescue`, `milestone-rescue-audit`, `roadmap-decompose`, `roadmap-prune`, `temporal-tree`, `ui-ux-pro-max`, `aif-note`, `aif-docs`

**`src/commands/` — ours, never synced from upstream:**
- All slash commands under `src/commands/` are local to this repo and are never overwritten by upstream syncs.

**Intentionally diverged from upstream — review diff before updating:**
- `aif-plan` — uses `TaskCreate`/`TaskUpdate`, custom logging defaults
- `aif-roadmap` — no Completed table (history managed by `roadmap-prune` → ARCHITECTURE.md)

**All other skills** — safe to overwrite directly from upstream.

**Procedure:**
```bash
git clone https://github.com/lee-to/ai-factory /tmp/ai-factory-upstream
# Compare
diff -rq /tmp/ai-factory-upstream/skills/<name> ~/.claude/skills/<name>
# Copy new skills
cp -r /tmp/ai-factory-upstream/skills/<name> ~/.claude/skills/<name>
```
