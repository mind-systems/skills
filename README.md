# mind-systems/skills

Generic AI Factory skills available globally to all projects via Claude Code's personal skill scope.

## Setup (one-time, per machine)

```bash
ln -s ~/projects/skills/.claude/skills ~/.claude/skills
```

That's it. All skills in this repo are now available as slash commands in every Claude Code session, in every project — no per-project configuration needed.

## Project-specific skills

If a project needs custom skills alongside the generic ones, place them in `.claude/skills/` inside that project directory. Claude Code loads both: personal scope (`~/.claude/skills`) and project scope (`.claude/skills`).

## Invoke skills

```
/aif          — set up AI context for a project
/aif-plan     — plan a feature (saves to .ai-factory/plans/)
/aif-implement — execute a plan
/aif-skill-generator — create or validate skills
```

## Structure

Each skill is a directory under `.claude/skills/` containing a `SKILL.md` (frontmatter + instructions) and optional `references/`, `scripts/`, and `templates/` subdirectories.

## Adding Skills

```bash
# Generate a new skill interactively
/aif-skill-generator <name>

# Generate from documentation URLs (Learn Mode)
/aif-skill-generator <url1> [url2]

# Validate an existing skill
/aif-skill-generator validate .claude/skills/<name>
```

External skills from [skills.sh](https://skills.sh) must pass a two-level security scan before use. See `.claude/skills/aif-skill-generator/SKILL.md` for details.
