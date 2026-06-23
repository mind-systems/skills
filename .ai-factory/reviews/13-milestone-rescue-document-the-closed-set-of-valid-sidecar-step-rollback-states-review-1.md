# Review 1 — milestone-rescue: document the closed set of valid sidecar `step` rollback states

## Scope
Doc-only change to `src/skills/milestone-rescue/SKILL.md` Step 5. No code, no migrations, no runtime surface. Verified the diff against the authoritative spec note (`.ai-factory/notes/23-task-milestone-rescue-document-rollback-states.md`) since the orchestrator (`orchestrator/main.py`) lives in another repo and is not present here.

## What's correct
- The "Valid sidecar `step` states" table reproduces all five values, resume phases, and required artifacts **exactly** as the spec note specifies (lines 18–24 of the note). No transcription errors.
- Test-mode swap (`review_failed:N` → `test_run_failed:N`, `test-runs/{seq}-{slug}-test-N.txt`) matches the note.
- Silent-failure-mode and always-valid-guard prose match the note's guards, including the explicit "never write `"planned"` after deleting the plan `.md`" failure mode.
- The new "Re-plan-review (plan corrected in place)" outcome (keep plan `.md`, delete plan-reviews + reviews + patches, keep sidecar, `step: "planned"`) matches Change B.
- The `Emit:` message was correctly generalized away from the hardcoded `"plan_reviewed"`.
- "What NOT to do" guard added consistently with the always-valid caveat.
- All three tasks in the plan are satisfied.

## Findings

### Low — `Sidecar doesn't exist` decision-table row conflicts with the new `"planned"` row on the re-plan-review path
The sidecar-update decision table (SKILL.md:325–329) now reads:

| Situation after cleanup | Write `step` |
|---|---|
| Plan `.md` corrected in place; plan-reviews, reviews deleted | `"planned"` |
| Plan-reviews exist and pass, reviews deleted | `"plan_reviewed"` |
| Sidecar doesn't exist | create it with `"plan_reviewed"` |

On the re-plan-review path the plan-reviews have been deleted, so there are no passing plan-reviews on disk. If the sidecar also happens to be absent, rows 1 and 3 both match and prescribe **conflicting** values (`"planned"` vs `"plan_reviewed"`). Row 3 was written for the re-implement context and silently assumes a passing plan-review exists. An operator following row 3 on the re-plan-review path would write `"plan_reviewed"`, which the orchestrator then clears (no `PLAN_REVIEW_PASS` file present) and falls through to the heuristic — exactly the "silently loses the intended resume" failure this task exists to prevent. Suggest scoping row 3 to the re-implement case (e.g. "Sidecar doesn't exist (re-implement) → create with `"plan_reviewed"`") or adding a corrected-plan + missing-sidecar row writing `"planned"`.

### Informational — sidecar-update procedure is filed only under a "Re-implement (plan `.md` kept)" heading
The only sub-section describing *how* to read, update (`step`-only), and re-serialize the sidecar is headed **"Re-implement (plan `.md` kept):"** (SKILL.md:316). The re-plan-review outcome also keeps the plan and needs that exact procedure, but the heading names only "Re-implement", so an operator on the re-plan-review path could skip it. Consider generalizing the heading to cover both plan-kept dispositions (e.g. "Plan `.md` kept (re-implement or re-plan-review)").

### Informational — "the sub-step below handles both cases" now understates the count
SKILL.md:269–270 still says the sidecar is deleted only on full reset, "the sub-step below handles both cases." There are now three cleanup outcomes (full reset, re-plan-review, re-implement). The sidecar dispositions are still two (delete vs keep-and-update), so the statement is not wrong, but "both cases" reads as stale against the three-outcome list directly above it. Minor wording only.

## Verdict
No blocking or correctness-breaking issues; the documented table is accurate and the new outcome is correct. The Low finding is a genuine internal-consistency gap that could reproduce the wrong-`step` failure mode in one edge case (re-plan-review with a missing sidecar) and is worth tightening, but it does not block.
