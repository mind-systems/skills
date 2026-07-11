# roadmap-engine: grants restored to what the flow does

Source observation: `plan-reviews/86-1-17-frontmatter-skill-joins-allowed-tools-…-plan-review-1.md:36`, re-verified live 2026-07-12: `src/skills/roadmap-engine/SKILL.md:10` is `allowed-tools: Read Skill`. The observation asked whether the `Read`-only grant is deliberate; decision pinned here: it is a regression, not a design.

## Current state

The engine was created (milestone 41) with `allowed-tools: Read Write Edit Glob Grep Skill`; the reduction to `Read` appeared during the note-38/43 rewrites with no recorded intent. Meanwhile the body's maintenance flow both explores (`Glob` for structure, `Grep` for features, `git log --oneline -20` for completed work) and writes (spec notes via `note`, then `$TARGET_FILE` — "Then write `$TARGET_FILE`"). When the engine is loaded into a caller's context the caller's grants happen to cover the gap, which is why nothing broke — but the grant must describe the skill's own body, not lean on every caller's.

## Change

Frontmatter only, one line: `allowed-tools: Read Write Edit Glob Grep Bash(git *) Skill`. The `Bash(git *)` addition (beyond milestone 41's original set) covers the flow's own `git log` exploration — the same body-vs-grant alignment class as milestone 1.17.

## Files & types

- edit `src/skills/roadmap-engine/SKILL.md` line 10 only.

## Guards

- Body byte-identical; no other frontmatter key changes (`user-invocable`, `loads:` stay).

## Verification

- `sed -n '10p' src/skills/roadmap-engine/SKILL.md` shows the new grant line; `git diff` is one line.
