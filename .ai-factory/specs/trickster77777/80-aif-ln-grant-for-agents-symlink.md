# aif: grant `Bash(ln *)` for the AGENTS.md symlink step

Phase 19. `aif`'s `## AGENTS.md Generation` section runs a `ln` command to create the `AGENTS.md → CLAUDE.md` symlink that the harness contract requires (AGENTS.md is a symlink to the sibling CLAUDE.md — see `docs/sakshi-harness/sakshi-harness.md`), but `ln` is not in the skill's `allowed-tools`. The step therefore has no standing grant: interactively it raises a permission prompt, and in a headless orchestrator run it can block. Pre-existing gap, unrelated to Phase 19's config retirement — surfaced by task 19.1, which edits the same frontmatter line but is guarded off this section.

## Current state (grounded, verified live)

- `src/skills/aif/SKILL.md` L5 — `allowed-tools: Read Glob Grep Write Bash(mkdir *) Bash(node *update-config.mjs*) Skill AskUserQuestion`. It grants `Bash(mkdir *)` and `Bash(node *update-config.mjs*)`, but no `Bash(ln *)`.
- `src/skills/aif/SKILL.md` `## AGENTS.md Generation` (L199–207) instructs `ln -sfn CLAUDE.md AGENTS.md` (L204), with a follow-on replace-if-regular-file rule. This is the only `ln` invocation in the file.

## Change

- Add `Bash(ln *)` to the `allowed-tools` list on `aif/SKILL.md` L5, so the AGENTS.md symlink step has a standing grant. Insert it alongside the other `Bash(...)` grants; keep the rest of the list unchanged in content and order.

## Files & types

- edit: `src/skills/aif/SKILL.md` (frontmatter `allowed-tools` only)

## Guards

- **AGENTS.md Generation section is not touched** — it is correct as written; this task only widens the grant so the existing `ln` step is pre-approved. No behavior in that section changes.
- **Shared line with task 19.1.** 19.1's first task also edits this same L5 — it *drops* the `Bash(node *update-config.mjs*)` grant (the script it names is retired). The two edits are independent concerns landing on one line; whichever runs second must preserve the other's change. After both land, the line reads `Read Glob Grep Write Bash(mkdir *) Bash(ln *) Skill AskUserQuestion`.
- **Grant only what the step needs** — add `Bash(ln *)`, not a broader `Bash(*)`; no other grant is widened.

## Verification

- `grep -n 'allowed-tools' src/skills/aif/SKILL.md` shows `Bash(ln *)` present in the list.
- The `ln -sfn CLAUDE.md AGENTS.md` step in `## AGENTS.md Generation` now falls within a standing grant — a fresh `/aif` run reaches the symlink step without a permission prompt for `ln`.
