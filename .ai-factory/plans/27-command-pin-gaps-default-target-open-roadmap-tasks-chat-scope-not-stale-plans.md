# Plan: command-pin-gaps: default target = open roadmap tasks / chat scope, not stale plans

## Context
Rewrite the target-resolution line of `command-pin-gaps` so its default is the open roadmap task set (contract lines + `Spec:` notes) or the chat scope, dropping the stale `.ai-factory/plans/*.md` fallback while keeping explicit `$ARGUMENTS` targeting.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Retarget the command

- [x] **Task 1: Replace the target-resolution line**
  Files: `src/commands/command-pin-gaps.md`
  Rewrite line 10 (`Target: the file in $ARGUMENTS, else the newest .ai-factory/plans/*.md, else the task under discussion.`) into the new priority chain from `.ai-factory/notes/37-pin-gaps-default-target.md`:
  1. The file(s) in `$ARGUMENTS`, if given (explicit plan targeting still works).
  2. Else the scope under discussion in chat (a named task, phase, or note).
  3. Else all open `- [ ]` tasks above `---STOP---` in `.ai-factory/ROADMAP.md` — scanning each contract line **and** its `Spec:` note file.
  Drop the `newest .ai-factory/plans/*.md` fallback entirely. Keep the wording tight and consistent with the file's existing terse style. Do NOT touch the hole-taxonomy paragraph, the `file:line` pinning rule, `## Blocking decisions`, scan mode, or the closing report format — all unchanged.

- [x] **Task 2: Verify frontmatter tooling covers the new default** (depends on Task 1)
  Files: `src/commands/command-pin-gaps.md`
  Confirm `allowed-tools` (`Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git grep *)`) already supports reading `.ai-factory/ROADMAP.md` and its `Spec:` notes for the new default target — Read/Grep/Glob suffice, so no frontmatter change is expected. Only adjust if the rewrite introduces a genuinely new tool need; otherwise leave frontmatter untouched.
