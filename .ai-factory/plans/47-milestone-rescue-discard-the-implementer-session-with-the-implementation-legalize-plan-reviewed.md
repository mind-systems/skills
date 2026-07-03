# Plan: milestone-rescue: discard the implementer session with the implementation; legalize `plan_reviewed`

## Context
Fix `src/skills/milestone-rescue/SKILL.md` so a rescue that discards an implementation also discards the stale implementer session id, and add a repair path for the "plan ratified, implementation absent" state that rolls the sidecar back to `plan_reviewed`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

All edits are in a single file: `src/skills/milestone-rescue/SKILL.md`. No orchestrator changes; sidecar table values and artifact requirements stay unchanged.

### Phase 1: Skill edits

- [x] **Task 1: Delete the `implementer` key at spec+plan depth**
  Files: `src/skills/milestone-rescue/SKILL.md`
  In the **Depth: spec + plan** block (Step 5, around lines 262–275): amend the sidecar-update step so that alongside setting `step: "planned"` it **deletes** the `implementer` key from the sidecar. Update the preserve-all-keys wording ("Preserve every other key — `planner`, `implementer`, `elapsed` …") to carve the exception: `implementer` is dropped because the session's memory describes the discarded implementation; `planner` and `elapsed` stay untouched. Update the emit line if needed to mention the dropped session. Follow the existing read/`{}`-if-absent/write-2-space-JSON procedure already described in that block.

- [x] **Task 2: Amend the What-NOT-to-do preserve rule** (depends on Task 1)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Edit the What-NOT-to-do bullet at lines ~370–372 ("Do not overwrite `planner`, `implementer`, or `elapsed` … only `step` is updated"). Carve the exception so it stays consistent with Task 1: `implementer` is deleted whenever the repair discards the implementation the session produced; `planner` and `elapsed` are never deleted at any depth. Add the spec's guidance that the `implementer` key must not be kept "for the elapsed stats" — those stats live in `elapsed`, which is retained.

- [x] **Task 3: Add the "plan ratified, implementation absent" rollback path** (depends on Task 2)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Add a new repair depth for the state where a passing plan-review exists but the product diff is empty (implementation discarded while the plan remained valid). Two touch points, matching the existing structure:
  - **Step 4 depth menu** (the `AskUserQuestion` block at lines ~204–218): add this rollback as a selectable option — keep plan + passing plan-reviews, delete reviews/patches, sidecar `step` → `"plan_reviewed"`, drop `implementer`; orchestrator resumes at implement iteration 1 with a fresh session.
  - **Step 5**: add a new depth block (parallel to the existing spec / spec+plan / spec+plan+code blocks, around lines 262–292) that executes it: keep the plan `.md` and all plan-review files; delete all review and patch files for the slug; set `step: "plan_reviewed"`; delete the `implementer` key (same read/update/write procedure). State the validation contract inline: `"plan_reviewed"` requires a plan-review file ending with `PLAN_REVIEW_PASS` on disk — never write it otherwise. Add an emit line consistent with the others.

- [x] **Task 4: Make diagnosis recognize the state** (depends on Task 3)
  Files: `src/skills/milestone-rescue/SKILL.md`
  In Steps 2–3 (diagnosis / Diagnosis Report), add recognition of the signal: when every review round reports the product file(s) byte-identical to HEAD, the defect is pipeline state (a stale implementer session), not a spec/plan/code defect. The Diagnosis Report should say so, and the Step 4 depth menu should offer the Task 3 rollback rather than the standard three depths. Keep the diagnosis in domain/state language consistent with the existing Step 2–3 wording; do not introduce orchestrator vocabulary into the user-facing Diagnosis Report beyond what the existing text already permits.

- [x] **Task 5: Amend the closed-set table trailing note** (depends on Task 3)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Update the note after the "Valid sidecar `step` states" table (line ~314) which currently states `"plan_reviewed"` is intentionally not written by this skill. Amend it: `"plan_reviewed"` **is** written by this skill, exactly in the Task 3 rollback, and only when a `PLAN_REVIEW_PASS` plan-review file is present on disk. The other reference-only values (`plan_review_failed:N`, `review_failed:N`) remain not written. Leave the table's `step` values and artifact requirements unchanged.

## Commit Plan
- **Commit 1** (after tasks 1-5): "Discard stale implementer session on discarded implementation; add plan_reviewed rollback to milestone-rescue"
