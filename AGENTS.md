# AGENTS.md

> Project map for AI agents. Keep up-to-date as skills are added or renamed.

## Project Overview

Generic AI Factory skills shared across all programming projects. Skills are injected into projects via the `~/.claude/skills` symlink (→ `src/skills`) and invoked as slash commands in Claude Code.

## Tech Stack

- **Format:** Markdown (SKILL.md)
- **Scripts:** Python 3, Bash
- **Distribution:** symlinks + `npx skills` (skills.sh)
- **Runtime:** Claude Code

## Project Structure

```
skills/
├── src/
│   ├── skills/               # All skill packages (symlinked from ~/.claude/skills)
│   │   ├── aif/              #   project setup & MCP configuration
│   │   ├── aif-plan/         #   feature planning
│   │   ├── aif-skill-generator/  # skill authoring + security scanning
│   │   ├── aif-*/            #   other lifecycle skills
│   │   ├── detangle/         #   context reconstruction for complex diffs
│   │   ├── milestone-rescue/ #   rescue derailed milestones
│   │   ├── roadmap-prune/    #   prune completed roadmap items
│   │   ├── temporal-tree/    #   temporal decision context visualization
│   │   └── ui-ux-pro-max/    #   UI/UX generation (67 styles, 96 palettes)
│   └── commands/             # Slash commands (symlinked from ~/.claude/commands)
│       └── command-handoff.md
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
| `src/skills/aif-skill-generator/SKILL.md` | Authoring new skills — start here |
| `src/skills/aif-skill-generator/scripts/security-scan.py` | Security scanner for external skills |
| `src/skills/aif-skill-generator/scripts/validate.sh` | Structural validator |
| `src/skills/aif/SKILL.md` | Project setup entry point |

## AI Context Files

| File | Purpose |
|------|---------|
| AGENTS.md | This file — project structure map |
| .ai-factory/DESCRIPTION.md | Project specification and tech stack |
| .ai-factory/ARCHITECTURE.md | Architecture decisions |
| CLAUDE.md | Agent instructions and constraints |
