# Plan: roadmap-prune: Step 6 speaks the direction-section grammar

## Context
Step 6 of `roadmap-prune/SKILL.md` names the pruned section literally `## Milestones`, which doesn't exist in new-grammar roadmaps that hold tasks under `## <Direction name>` → `### Phase N` sections; this widens Step 6's vocabulary to cover both shapes and adds an emptied-direction sweep, leaving flat-roadmap behavior unchanged.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Widen Step 6 to both roadmap shapes

- [x] **Task 1: Generalize the delete/keep section vocabulary**
  Files: `src/skills/roadmap-prune/SKILL.md`
  In Step 6 only (`:216`–`:231`), replace the two literal `## Milestones` references with shape-covering wording that names "the task-holding sections" of both shapes: a flat `## Milestones` list, and direction sections (`## <Direction name>` → `### Phase N` → `N.M` tasks). Line `:218` ("Delete the pruned `[x]` tasks from `## Milestones`") and line `:222` ("Keep `## Milestones` with all remaining `[ ]` tasks") become the generalized wording. Flat-roadmap behavior must remain exactly correct (this repo's own roadmap uses the flat shape). Instructions only — no rationale prose (prune's own register). Do not touch the existing "always retain the last phase header and its 2 most recent `[x]` tasks" clause or the emptied-phase sweep at `:226`–`:231`.

- [x] **Task 2: Add the emptied-direction sweep with its guard clauses** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In Step 6, add one sentence parallel to and one level up from the existing emptied-phase sweep (`:226`–`:231`): when a direction section loses its last phase (all its phase headers removed by the emptied-phase sweep and no tasks remain), delete the `## <Direction name>` header and its preamble prose too. Include the two guard clauses: (a) never renumber anything — phase numbering is historic and file-global, a deleted direction's phase numbers stay as gaps (same invariant the emptied-phase sweep already states); (b) the existing retain-last-phase-header rule keeps the newest direction alive by construction, so the emptied-direction sweep can only fire on older, fully-pruned directions — mirroring how the emptied-phase rule already declares its coexistence with the retain rule. Keep the instructions-only register.

## Guards (must hold after edits)
- Step 6 only. Steps 0–5, 7, 8, the "Before you start" preamble, the commit policy, the "What NOT to do" list, and the Step 2 "Never copy a phase or section header as a feature name" rule (`:101`) stay byte-identical to HEAD.
- No renumbering anywhere.
- File stays ≤500 lines (306 today).
