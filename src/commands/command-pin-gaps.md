---
description: >-
  Scan a plan/note/task for "fantasy holes" — anything the implementing agent
  would have to guess — and close each one now with a concrete value read from
  the actual code/proto. Pass "scan" to only list holes without editing.
argument-hint: "[path | scan]"
allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git grep *)
---

Target: the file in `$ARGUMENTS`, else the newest `.ai-factory/plans/*.md`, else the task under discussion.

Any question that would need an answer *during implementation* is space for the agent to fantasize. Close all of it now.

Find every place the agent would have to guess: TODO/TBD/«решим по ходу»/«либо…либо», open forks with no decision, unpinned symbols (enum names **and values**, error codes, exact strings, versions, paths, field **types**), unspecified edge cases (error/timeout/reconnect/cancel/empty/race), magic numbers, and unstated task ordering.

For each: go read the code/proto and pin the **exact** value with a `file:line` citation — never invent. If it's a genuine product decision that the code can't settle, don't fabricate it: raise it as a one-line question under `## Blocking decisions` at the top of the file.

**scan mode** (`$ARGUMENTS` contains `scan`/`report`/`только скан`): list findings as `[file:line] → what's missing → fix` and stop.
**default:** edit the file in place — replace each vague spot with the concrete value + source — then report `N closed from source · M blocking`.
