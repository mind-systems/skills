# mind-systems/skills

Generic AI Factory skills shared across all projects. Skills are injected into individual projects via a symlink from `.claude/skills` → `~/.claude/skills`.

## Usage

Install into a project:

```bash
ln -s ~/.claude/skills .claude/skills
```

Then invoke skills as slash commands in Claude Code:

```
/aif          — set up AI context for a project
/aif-plan     — plan a feature (saves to .ai-factory/plans/)
/aif-implement — execute a plan
/aif-skill-generator — create or validate skills
```

## Structure

Each skill is a directory under `skills/` containing a `SKILL.md` (frontmatter + instructions) and optional `references/`, `scripts/`, and `templates/` subdirectories.

## Adding Skills

```bash
# Generate a new skill interactively
/aif-skill-generator <name>

# Generate from documentation URLs (Learn Mode)
/aif-skill-generator <url1> [url2]

# Validate an existing skill
/aif-skill-generator validate skills/<name>
```

External skills from [skills.sh](https://skills.sh) must pass a two-level security scan before use. See `skills/aif-skill-generator/SKILL.md` for details.
