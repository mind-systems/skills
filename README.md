# mind-systems/skills

Generic AI Factory skills available globally to all projects via Claude Code's personal skill scope.

## Setup — activating the package (one-time, per machine)

*This section is addressed to the agent reading it on a fresh checkout.* Activating the package means pointing `~/.claude` at this repo's `active/` layer. The user may already keep their own global config there, so **do not run this silently** — walk them through it one surface at a time and let them choose per surface.

Four surfaces under `~/.claude`, each with a target in `active/`:

| `~/.claude` surface | target in this repo |
|---|---|
| `CLAUDE.md` | `active/CLAUDE.md` (→ `src/global/CLAUDE.md`) |
| `skills/` | `active/skills/` |
| `commands/` | `active/commands/` |
| `agents/` | `active/agents/` |

For each surface, detect its current state (`readlink`/`test`) and act:

- **absent** — create the symlink to our target. Clean, no question.
- **already ours** (resolves back into this repo) — skip; the flow is idempotent.
- **the user's own file or directory** — stop and ask which of three they want:
  - **replace** — back theirs up (`mv <path> <path>.pre-sakshi.bak`), then symlink ours;
  - **keep theirs** — skip this surface entirely, leave ours unlinked;
  - **merge** — coexist, and *how* depends on the surface's kind:
    - `CLAUDE.md` is a single file → leave theirs a real file and append an import line `@<abs>/active/CLAUDE.md` to its tail (both sets of instructions load);
    - `skills/` `commands/` `agents/` are directories of independent items → leave theirs a real directory and link our items into it one by one (`ln -sfn <abs>/active/<kind>/<item> ~/.claude/<kind>/<item>`), asking on any name collision.

The whole flow is idempotent (a second run is all-skips) and reversible (our links resolve back into this repo; a replaced original sits beside its symlink as `*.pre-sakshi.bak`).

`~/.claude` points at `active/` — the curated working set: `active/skills/`, `active/commands/`, and `active/agents/` hold per-item symlinks into `src/` (ours) or `upstream/ai-factory/` (upstream originals we use), so only skills actually in use are loaded, not every skill that exists.

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

Our skills live under `src/skills/` (commands under `src/commands/`, agent definitions under `src/agents/`); a pristine mirror of upstream `lee-to/ai-factory` lives under `upstream/ai-factory/` (refresh with `scripts/sync-upstream.sh`); `active/` symlinks the curated working set. Each skill is a directory containing a `SKILL.md` (frontmatter + instructions) and optional `references/`, `scripts/`, and `templates/` subdirectories.

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
