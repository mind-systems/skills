# command-pin-gaps: default target = open roadmap tasks / chat scope, not newest plans/*.md

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- `src/commands/command-pin-gaps.md` line 10 sets the fallback target chain: "the file in `$ARGUMENTS`, else the newest `.ai-factory/plans/*.md`, else the task under discussion". But per `docs/workflow.md` §5 this command is the last pass **before** the orchestrator — at that point `plans/` contains only committed plans from *previous* milestones (plans are orchestrator output). The default silently picks a stale plan instead of the specs about to be executed.
- User's intended semantics: the target is the open task set — the `- [ ]` tasks above `---STOP---` in `.ai-factory/ROADMAP.md` (their contract lines + `Spec:` notes) — or whatever scope was named in chat. Explicitly passing a file (including a plan) still works via `$ARGUMENTS`.

## Details

Rewrite the target line to this priority order:

1. The file(s) in `$ARGUMENTS`, if given.
2. Else the scope under discussion in chat (a named task, phase, or note).
3. Else all open `- [ ]` tasks above `---STOP---` in `.ai-factory/ROADMAP.md` — scanning each contract line **and** its `Spec:` note file.

Drop the `newest .ai-factory/plans/*.md` fallback entirely. Everything else in the command (the hole taxonomy, pin-with-`file:line` rule, `## Blocking decisions`, scan mode, report format) stays unchanged.

## What NOT to do

- Do not remove the ability to target a plan file explicitly via `$ARGUMENTS`.
- Do not change scan/default mode behavior or the closing report format.
