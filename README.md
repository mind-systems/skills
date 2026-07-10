# mind-systems/skills

Generic AI Factory skills available globally to all projects via Claude Code's personal skill scope.

## Setup (one-time, per machine)

```bash
ln -s ~/projects/skills/active/skills ~/.claude/skills
ln -s ~/projects/skills/active/commands ~/.claude/commands
ln -s ~/projects/skills/active/agents ~/.claude/agents
```

`~/.claude` points at `active/` — the curated working set. `active/skills/`, `active/commands/`, and `active/agents/` hold per-item symlinks into `src/` (ours) or `upstream/ai-factory/` (upstream originals we use), so only skills actually in use are loaded, not every skill that exists.

## Project-specific skills

If a project needs custom skills alongside the generic ones, place them in `.claude/skills/` inside that project directory. Claude Code loads both: personal scope (`~/.claude/skills`) and project scope (`.claude/skills`).

## Invoke skills

```
/aif                 — set up AI context for a project
/roadmap-outline     — strategic roadmap (high-level milestones)
/roadmap-decompose   — break milestones into atomic, spec'd tasks
/aif-skill-generator — create or validate skills
```

## Structure

Our skills live under `src/skills/`; a pristine mirror of upstream `lee-to/ai-factory` lives under `upstream/ai-factory/` (refresh with `scripts/sync-upstream.sh`); `active/` symlinks the curated working set. Each skill is a directory containing a `SKILL.md` (frontmatter + instructions) and optional `references/`, `scripts/`, and `templates/` subdirectories.

## Adding Skills

```bash
# Generate a new skill interactively
/aif-skill-generator <name>

# Generate from documentation URLs (Learn Mode)
/aif-skill-generator <url1> [url2]

# Validate an existing skill
/aif-skill-generator validate src/skills/<name>
```

External skills from [skills.sh](https://skills.sh) must pass a two-level security scan before use. See `upstream/ai-factory/aif-skill-generator/SKILL.md` for details.
