# Code Review: frontmatter tool hygiene

**Scope:** Two frontmatter-only edits — `src/skills/aif-docs/SKILL.md` and `src/skills/roadmap-outline/SKILL.md`. (The plan/plan-review/JSON sidecar files in the diff are pipeline artifacts, not code.)

## Changes reviewed

1. **roadmap-outline** line 5: `Questions` token removed from `allowed-tools`. Everything else (`Bash(git *)`, `AskUserQuestion`, `Skill`) intact.
2. **aif-docs** line 5: `Bash(mkdir, npx, python)` replaced with `Bash(mkdir *) Bash(npx *) Bash(python *)`, and `Questions` token removed. `AskUserQuestion`, `WebFetch`, `WebSearch`, `metadata`, `disable-model-invocation` untouched.

## Verification

- **No dangling references:** grep for `Questions` across both files returns nothing — the removed token was never referenced from the bodies, so removal breaks no logic.
- **Dialogs preserved:** both skills retain `AskUserQuestion` in `allowed-tools`, which is the actual mechanism behind their 1/2/3 menus. No dialog regresses.
- **Bash rule correctness:** the new per-command glob form (`Bash(mkdir *)` etc.) is the valid Claude Code permission syntax and matches convention already used in `src/skills/roadmap-test-coverage/SKILL.md`. The old comma-separated `Bash(mkdir, npx, python)` matched nothing, so this strictly improves (never regresses) permission matching.
- **YAML validity:** both edits leave single-line scalar `allowed-tools` values with balanced parens; frontmatter remains well-formed.
- **Scope discipline:** frontmatter-only, no body edits, no upstream mirror touched — matches spec note 41 and the plan.

## Findings

None.

REVIEW_PASS
