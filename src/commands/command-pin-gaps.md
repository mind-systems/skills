---
description: >-
  Scan a plan/note/task for "fantasy holes" — anything the implementing agent
  would have to guess — and close each one now: pin value holes to a concrete
  value from the actual code/proto, and close meaning holes (edge behavior,
  open forks, unnamed invariants, scope boundaries, ordering) by writing the
  missing constraint as a spec clause grounded in observed code behavior.
  Pass "scan" to only list holes without editing.
argument-hint: "[path | scan]"
allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git grep *)
---

Target, in priority order: the file(s) in `$ARGUMENTS`, if given — else the scope under discussion in chat (a named task, phase, or note) — else all open `- [ ]` tasks above `---STOP---` in `.ai-factory/ROADMAP.md`, scanning each contract line and its `Spec:` note file.

Any question that would need an answer *during implementation* is space for the agent to fantasize. Close all of it now.

**Value holes:** TODO/TBD/«решим по ходу», unpinned symbols (enum names **and values**, error codes, exact strings, versions, paths, field **types**), magic numbers. Repair: read the code/proto and pin the **exact** value with a `file:line` citation — never invent.

**Meaning holes:** undefined behavior at the edges (error/timeout/reconnect/cancel/empty/race), open forks («либо…либо») with no decision, an unnamed invariant or interaction contract between components the task touches, an undrawn scope boundary (which files/services are outside the task's zone), unstated task ordering. Repair: write the missing constraint as a spec clause derived from the observed behavior of the actual code, citing the code that grounds it where a concrete source exists; when the code can't settle it (genuine product decision), don't fabricate it — raise it as a one-line question under `## Blocking decisions` at the top of the file.

**scan mode** (`$ARGUMENTS` contains `scan`/`report`/`только скан`): list findings as `[file:line|spec-location] → value|meaning → what's missing → fix` and stop.
**default:** edit the file in place — replace each vague spot with the concrete value or spec clause + source — then report `N closed from source · M blocking` (optionally split the count by class).
