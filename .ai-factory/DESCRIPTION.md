# Project: mind-systems/skills

## Overview

Generic AI Factory skills shared across all programming projects. Skills are reusable slash-command packages injected into projects via a symlink from `.claude/skills` → `~/.claude/skills`. This repo is the source of truth — its product is skills, not application code.

## Core Features

- Lifecycle skills: plan → implement → verify → review → evolve
- UI/UX generation with 67 styles, 96 palettes, multi-stack support
- Security scanning for external skills (two-level: automated + semantic)
- Skill authoring toolkit with Learn Mode (generate from documentation URLs)
- Project setup automation (stack detection, MCP config, AGENTS.md)

## Tech Stack

- **Format:** Markdown (SKILL.md frontmatter + body)
- **Scripts:** Python 3, Bash
- **Distribution:** symlinks + `npx skills` CLI (skills.sh registry)
- **Runtime:** Claude Code (claude-code agent)

## Architecture Notes

Each skill is a self-contained directory. Skills reference each other via invocations (e.g., `/aif-plan` calls `/aif-skill-generator` internally). No build step — skills are read directly by the agent at runtime.

## Non-Functional Requirements

- Skill body ≤ 500 lines; details go to `references/`
- Every external skill must pass security scan before use
- `name` in frontmatter must match directory name exactly
