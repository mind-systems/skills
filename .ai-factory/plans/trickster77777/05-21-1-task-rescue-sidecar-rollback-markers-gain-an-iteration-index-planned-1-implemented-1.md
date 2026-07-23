# Plan: task-rescue: sidecar rollback markers gain an iteration index (`planned:1` / `implemented:1`)

## Context
Re-sync `task-rescue`'s sidecar `step` marker grammar to orchestrator 18.2's indexed form: every value the skill *writes* becomes `"planned:1"` / `"implemented:1"`, and the two closed-set table rows generalise to `"planned:N"` / `"implemented:N"` with a note that the rescue always writes N = 1 and the bare forms are retired.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Index the written marker values

All edits are targeted string replacements in `src/skills/task-rescue/SKILL.md`, preserving the skill's existing voice. Only the literal `step` *value* the skill writes changes; every guard *condition*, the repair-depth deletion/JSON mechanics, `implementer`-key handling, and all reference-only rows stay byte-identical apart from that value. Scope is the marker grammar only.

- [x] **Task 1: Index the Step 4 depth-menu values**
  Files: `src/skills/task-rescue/SKILL.md`
  In the Step 4 depth menu (AskUserQuestion block): option 2's `Rollback: … sidecar step → "planned"` becomes `sidecar step → "planned:1"`, and option 3's `Rollback: … sidecar step → "implemented"` becomes `sidecar step → "implemented:1"`. Leave option 4's `"plan_reviewed"` byte-identical.

- [x] **Task 2: Index the spec + plan rollback procedure**
  Files: `src/skills/task-rescue/SKILL.md`
  In the "Depth: spec + plan" section: the heading "roll back to `"planned"`" → "roll back to `"planned:1"`"; step 4's "Set the `step` key to `"planned"`" → "Set the `step` key to `"planned:1"`"; the Emit line becomes `Sidecar updated: step set to "planned:1"; implementer session dropped.`. Keep the `implementer`-key deletion and the JSON read/update/write mechanics unchanged.

- [x] **Task 3: Index the spec + plan + code rollback procedure**
  Files: `src/skills/task-rescue/SKILL.md`
  In the "Depth: spec + plan + code" section: the heading "roll back to `"implemented"`" → "roll back to `"implemented:1"`"; step 5's "Update the sidecar `step` to `"implemented"`" → "Update the sidecar `step` to `"implemented:1"`"; the Emit line becomes `Sidecar updated: step set to "implemented:1".`. Keep the read/update/write mechanics unchanged.

- [x] **Task 4: Generalise the closed-set table rows and add the N = 1 note**
  Files: `src/skills/task-rescue/SKILL.md`
  In the "Valid sidecar `step` states" table: the row `| "planned" | plan-review, attempt 1 | none — always valid |` becomes `| "planned:N" | plan-review, attempt N | none — always valid |`, and `| "implemented" | review, iter 1 | none — always valid |` becomes `| "implemented:N" | review, iter N | none — always valid |`. Add a one-line note directly under the table stating the rescue always writes **N = 1** (all prior-round plan-reviews/reviews are deleted at both depths, so the next round is always 1) and that the bare `"planned"` / `"implemented"` forms are retired — no longer accepted by the orchestrator. Leave the `"plan_review_failed:N"`, `"plan_reviewed"`, and `"review_failed:N"` rows byte-identical. Note: the table preamble already says it mirrors `_validate_sidecar_step()` / `_detect_task_step()` in `orchestrator/resume.py` — leave that reminder text as is.

- [x] **Task 5: Index the always-valid guard and Note paragraph**
  Files: `src/skills/task-rescue/SKILL.md`
  In the "Always-valid guard" line under the table: `"planned"` → `"planned:1"` and `"implemented"` → `"implemented:1"` as the written values, keeping the preconditions unchanged (write `"planned:1"` only when the plan `.md` is present; write `"implemented:1"` only when the plan `.md` is present and a non-empty working diff exists; never write `"planned:1"` after deleting the plan `.md`). In the following Note paragraph, update "the flow writes only `"planned"` (spec+plan depth), `"implemented"` (spec+plan+code depth)" to `"planned:1"` / `"implemented:1"`. Leave `"plan_reviewed"`, `"plan_review_failed:N"`, and `"review_failed:N"` mentions in this paragraph byte-identical.

- [x] **Task 6: Index the "Do not write" guard**
  Files: `src/skills/task-rescue/SKILL.md`
  In the "What NOT to do" list, the guard "Do not write `"planned"` or `"implemented"` when the corresponding artifact is absent …" gains the `:1` index on both values (`"planned:1"` / `"implemented:1"`), with the guard's semantics — always-valid states written only when the artifact is present — unchanged.

### Phase 2: Confirm the delegation still reads true

- [x] **Task 7: Confirm `orchestrator-artifacts` §3 delegation (no edit)**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Read §3 and verify its line delegating the closed set to `task-rescue` still reads true after the table update — the closed set it points at is now the indexed one. No content edit expected; only make a change if the delegation line names a specific bare value that the retirement makes false.
