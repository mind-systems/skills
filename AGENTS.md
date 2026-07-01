# AGENTS.md

> Project map for AI agents. Keep up-to-date as skills are added or renamed.

## Project Overview

Generic AI Factory skills shared across all programming projects. Skills are injected into projects via the `~/.claude/skills` symlink (→ `active/skills`, the curated working set) and invoked as slash commands in Claude Code. Our skills live in `src/skills/`; a pristine upstream mirror lives in `upstream/ai-factory/`; `active/` symlinks only what is actually used.

## Tech Stack

- **Format:** Markdown (SKILL.md)
- **Scripts:** Python 3, Bash
- **Distribution:** symlinks + `npx skills` (skills.sh)
- **Runtime:** Claude Code

## Project Structure

```
skills/
├── src/                      # OURS
│   ├── skills/               #   our skill packages
│   │   ├── roadmap-decompose/         # atomic-deliverability decomposition
│   │   ├── roadmap-decompose-skeleton/ # skeleton/TDD/concurrency lens
│   │   ├── roadmap-engine/            # two-tier artifact format
│   │   ├── roadmap-outline/           # strategic roadmap
│   │   ├── note/                      # research-summary writer
│   │   ├── test-philosophy/           # silent-failure testing rule
│   │   ├── milestone-rescue/          # rescue derailed milestones
│   │   ├── detangle/  temporal-tree/  observe-logs/  aif-docs/  aif-plan/  ui-ux-pro-max/  …
│   └── commands/             #   slash commands (all ours)
├── upstream/ai-factory/      # PRISTINE mirror of lee-to/ai-factory skills/ (scripts/sync-upstream.sh)
├── active/                   # CURATED working set — ~/.claude points here
│   ├── skills/               #   per-skill symlinks → src/skills/* or upstream/ai-factory/*
│   └── commands/             #   per-command symlinks → src/commands/*
├── scripts/sync-upstream.sh  # refresh the upstream mirror
├── .claude/                  # Claude Code project config (.mcp.json, settings.local.json)
├── .ai-factory/
│   ├── DESCRIPTION.md        # Project specification
│   ├── ARCHITECTURE.md       # Architecture decisions
│   └── plans/                # Feature plan files
├── CLAUDE.md                 # Agent instructions
├── AGENTS.md                 # This file
└── README.md                 # Project landing page
```

## Key Entry Points

| File | Purpose |
|------|---------|
| `upstream/ai-factory/aif-skill-generator/SKILL.md` | Authoring new skills — start here |
| `upstream/ai-factory/aif-skill-generator/scripts/security-scan.py` | Security scanner for external skills |
| `upstream/ai-factory/aif-skill-generator/scripts/validate.sh` | Structural validator |
| `upstream/ai-factory/aif/SKILL.md` | Project setup entry point |

## AI Context Files

| File | Purpose |
|------|---------|
| AGENTS.md | This file — project structure map |
| .ai-factory/DESCRIPTION.md | Project specification and tech stack |
| .ai-factory/ARCHITECTURE.md | Architecture decisions |
| CLAUDE.md | Agent instructions and constraints |
