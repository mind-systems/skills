# Plan: frontmatter tool hygiene: drop `Questions` pseudo-tool; fix aif-docs Bash rule syntax

## Context
Remove the non-existent `Questions` tool from two skills' `allowed-tools` and fix `aif-docs`'s invalid comma-separated `Bash(mkdir, npx, python)` rule so its shell calls stop prompting. The 1/2/3 menu dialogs already run via `AskUserQuestion` (declared in both) and stay unchanged.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Frontmatter fixes

- [x] **Task 1: Drop `Questions` from roadmap-outline**
  Files: `src/skills/roadmap-outline/SKILL.md`
  In the frontmatter `allowed-tools` line (line 5), change `Read Write Edit Glob Grep Bash(git *) AskUserQuestion Questions Skill` to `Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill` — remove only the `Questions` token, leave everything else (including `AskUserQuestion` and `Skill`) intact. Body unchanged.

- [x] **Task 2: Drop `Questions` and fix Bash rule in aif-docs**
  Files: `src/skills/aif-docs/SKILL.md`
  In the frontmatter `allowed-tools` line (line 5), change `Read Write Edit Glob Grep Bash(mkdir, npx, python) AskUserQuestion Questions WebFetch WebSearch` to `Read Write Edit Glob Grep Bash(mkdir *) Bash(npx *) Bash(python *) AskUserQuestion WebFetch WebSearch` — replace the single comma-separated `Bash(mkdir, npx, python)` rule with three per-command glob rules and remove the `Questions` token. Keep `AskUserQuestion`, `WebFetch`, `WebSearch` and the rest of the frontmatter (`metadata`, `disable-model-invocation`) untouched. Body unchanged — the >500-line body is out of scope.

## Notes
- Both edits are frontmatter-only; dialogs and all other logic stay exactly as-is.
- Never touch the upstream mirror (`upstream/ai-factory/`) — only `src/skills/`.
- Single commit after both tasks: "Drop non-existent Questions tool and fix aif-docs Bash rule syntax".
