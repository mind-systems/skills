# AGENTS.md

> Project map for AI agents. Keep up-to-date as skills are added or renamed.

## Project Overview

Generic AI Factory skills shared across all programming projects. Skills are injected into projects via `.claude/skills` symlink and invoked as slash commands in Claude Code.

## Tech Stack

- **Format:** Markdown (SKILL.md)
- **Scripts:** Python 3, Bash
- **Distribution:** symlinks + `npx skills` (skills.sh)
- **Runtime:** Claude Code

## Project Structure

```
skills/
├── .claude/skills/           # All skill packages (symlinked from ~/.claude/skills)
│   ├── aif/                  # Project setup & MCP configuration
│   ├── aif-plan/             # Feature planning
│   ├── aif-implement/        # Plan execution
│   ├── aif-architecture/     # Architecture document generation
│   ├── aif-skill-generator/  # Skill authoring + security scanning
│   ├── aif-*/                # Other lifecycle skills
│   ├── detangle/             # Context reconstruction for complex diffs
│   ├── milestone-rescue/     # Rescue derailed milestones
│   ├── roadmap-prune/        # Prune completed roadmap items
│   ├── temporal-tree/        # Temporal decision context visualization
│   └── ui-ux-pro-max/        # UI/UX generation (67 styles, 96 palettes)
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
| `.claude/skills/aif-skill-generator/SKILL.md` | Authoring new skills — start here |
| `.claude/skills/aif-skill-generator/scripts/security-scan.py` | Security scanner for external skills |
| `.claude/skills/aif-skill-generator/scripts/validate.sh` | Structural validator |
| `.claude/skills/aif/SKILL.md` | Project setup entry point |

## AI Context Files

| File | Purpose |
|------|---------|
| AGENTS.md | This file — project structure map |
| .ai-factory/DESCRIPTION.md | Project specification and tech stack |
| .ai-factory/ARCHITECTURE.md | Architecture decisions |
| CLAUDE.md | Agent instructions and constraints |
