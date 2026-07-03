# milestone-rescue: discard the implementer session with the implementation; legalize `plan_reviewed`

**Date:** 2026-07-03
**Source:** conversation context (task-56 pipeline stall postmortem)

## Key Findings

- Live incident: a spec+plan rescue rolled task 56 back to `"planned"` and, per the skill's rule "update **only** the `step` key — preserve every other key," kept the `implementer` session id from the discarded attempt. The orchestrator resumes the implementer session from the sidecar (`orchestrator/main.py:296`, `implementer.session_id = sessions.get("implementer")`); that session's memory says it already implemented the milestone (the reverted version), so on re-run it made **no edits** — three implement iterations produced a working tree byte-identical to HEAD, and three code reviews blocked on "the implementation is absent."
- The preserve-all-keys rule is correct only while the implementation the session produced **still exists**. When the rescue discards the implementation, the session's memory is stale and must be discarded with the code: at **spec+plan** depth, delete the `implementer` key alongside setting `step: "planned"` (at **spec** depth the whole sidecar is deleted already; at **spec+plan+code** the implementation is kept, so the session stays).
- A second gap surfaced by the same incident: the failure state "plan ratified, implementation absent" has no repair path in the skill. The correct rollback is `step: "plan_reviewed"` — keep the plan and its passing plan-reviews, delete the no-op reviews, drop the `implementer` key — so the orchestrator resumes directly at implement, iteration 1 (`main.py:466-467`) with a fresh session, instead of re-running plan review. The skill currently declares `"plan_reviewed"` as "intentionally not written by this skill"; that note is now wrong and must be amended.

## Details

### Edit 1 — spec+plan depth discards the implementer session

In `src/skills/milestone-rescue/SKILL.md`, Step 5 "Depth: spec + plan": alongside updating `step` to `"planned"`, **delete the `implementer` key** from the sidecar. Amend the sidecar-update wording ("Preserve every other key — `planner`, `implementer`, `elapsed` …") and the What-NOT-to-do line ("Do not overwrite `planner`, `implementer`, or `elapsed`…") to carve this exception: `implementer` is deleted whenever the repair discards the implementation the session produced; `planner` and `elapsed` stay untouched everywhere.

### Edit 2 — new rollback: plan ratified, implementation absent

Add the repair path for the state where a passing plan-review exists but the product diff is empty (or the implementation was discarded while the plan remained valid): keep the plan `.md` and all plan-review files, delete all review and patch files for the slug, set `step: "plan_reviewed"`, delete the `implementer` key. Note the validation contract: `"plan_reviewed"` requires a plan-review file ending with `PLAN_REVIEW_PASS` (the sidecar table already states this) — never write it otherwise.

Amend the closed-set table's trailing note: `"plan_reviewed"` **is** written by this skill, exactly in this rollback; the other unwritten values (`plan_review_failed:N`, `review_failed:N`) remain reference-only.

### Constraints

- Diagnosis (Steps 2–3) should recognize the state: all review rounds report the product file(s) byte-identical to HEAD → the defect is pipeline state, not spec/plan/code; the Diagnosis Report says so and the depth menu offers the Edit-2 rollback instead of the standard three depths.
- The sidecar table's values and artifact requirements are unchanged — they mirror the orchestrator; only the "who writes what" note changes.
- No orchestrator changes — `main.py` behavior is the fixed contract this skill writes against.

## What NOT to do

- Do not delete `planner` or `elapsed` at any depth — the planner session's memory stays valid (it amended the plan correctly through review rounds in the same incident).
- Do not write `"plan_reviewed"` without a `PLAN_REVIEW_PASS` plan-review on disk — the orchestrator silently clears invalid steps and falls back to the disk heuristic.
- Do not keep the `implementer` key at spec+plan depth "for the elapsed stats" — the stats live in `elapsed`, which stays; the session id is the only thing discarded.
