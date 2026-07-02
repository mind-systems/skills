# Plan: roadmap-test-coverage — hand findings to decompose via chat; legalize Class-A test patching

## Context
Stop `roadmap-test-coverage` from writing underspecified plain-text tasks into `$ROADMAP_PATH`; instead collect refactor + Class-B findings into a handoff list that Layer 8 prints as `/roadmap-decompose` task descriptions, and reword Critical Rule 1 so Layer 7's Class-A test patching is a legal exception rather than a contradiction.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Collect findings instead of writing roadmap

- [x] **Task 1: Rework Layer 6 to collect refactor findings**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  In Layer 6 (lines ~191–201), remove step 1's write of a task to `$ROADMAP_PATH` under a `## Test Infra` phase. Replace it with: for each `needs-refactor` verdict, append an entry to an in-memory handoff list — area name + one-sentence refactor description (from the verdict) + pointer to its Layer-4 note path. **Keep step 2 unchanged** — appending the `## Refactor Required` section to the corresponding Layer-4 note stays (it is note content). Rename the layer heading to reflect collection, e.g. "Layer 6 — Refactor Collect". Keep the "No user confirmation needed — collect and continue" logging behavior.

- [x] **Task 2: Rework Layer 7 Class B handling to collect instead of write**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  In Layer 7 (lines ~257–259), remove the write of a task to `$ROADMAP_PATH` under a `## Bugs` phase for Class B failures. Replace with: add each Class B failure to the same handoff list from Task 1 — area name + reason from the classification table + the **source file** path (the classification table already has a `Source file` column, line ~247). Capturing the source file matters because a Class B failure can belong to an area that never got a Layer-4 note (Layer 7 runs the whole suite, so a failing test may be in a "Full coverage" area dropped in Layer 2 or a loud-failure area dropped in Layer 3) — those items have no note path, so the source file is the fallback pointer for the handoff line. Keep the "Do NOT touch the test" instruction. Leave the Layer 7 classification table (lines ~245–250), the agent prompt, and the Class-A patch instruction ("patch the failing test to match the current source API. Keep assertions intact — only update the call signature") untouched. Keep the re-run `$TEST_CMD` / all-green requirement.

### Phase 2: Handoff output and rule reconciliation

- [x] **Task 3: Extend Layer 8 to print the handoff list** (depends on Task 1, Task 2)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  In Layer 8 (lines ~264–282), after the existing summary block, print the collected handoff list as concrete one-line task descriptions for `/roadmap-decompose` — refactor items and Class B bug items. Specify the per-item pointer explicitly: attach the Layer-4 note path when the item's area was researched (always true for refactor items, and for Class B items whose failing test belongs to a researched area); otherwise — for Class B items from an area that was never researched (dropped in Layer 2 or 3) — print the source file path captured in Task 2. This makes the handoff line well-defined for every item, with no blank note paths. Update the summary lines so they reflect handoff rather than roadmap writes: change "Refactor tasks added to roadmap: M" → refactor items handed off, and "Silent bugs escalated to roadmap: J" → Class B items handed off. Keep "Existing tests patched (API drift): K". Keep the "Do not run `/roadmap-decompose` automatically" line — handoff is via chat, user triggers decompose.

- [x] **Task 4: Reword Critical Rule 1 to legalize Class-A patching** (depends on Task 2)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Rewrite Critical Rule 1 (line ~288) from "Never write test files — research and planning only" to: never write **new** test files (research and planning only); the single allowed test write is Layer 7's patching of existing Class-A (API-drift) failures — tests broken because the source API changed, not by implementation bugs — keeping assertions intact and updating only the call signature. Verify the reworded rule no longer contradicts Layer 7. Confirm the body stays ≤ 500 lines.
  One permitted frontmatter tweak: the `description` (line 7) reads "…emits refactor tasks…", which now implies a roadmap write that no longer happens. Change that phrase to reflect collection/handoff (e.g. "collects refactor findings"). This is the only frontmatter edit — `name`, `argument-hint`, `allowed-tools`, `loads`, and the invocation flags stay unchanged. Do not treat "frontmatter unchanged" from the spec note as a hard prohibition against correcting this now-inaccurate phrase.
