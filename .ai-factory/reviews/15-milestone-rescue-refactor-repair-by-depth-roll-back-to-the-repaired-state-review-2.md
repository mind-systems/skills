# Code Review (pass 2): milestone-rescue — refactor — repair by depth, roll back to the repaired state

**Change under review:** `src/skills/milestone-rescue/SKILL.md` (diff vs HEAD: +149 / −235; net file 315 lines)
**Plan:** `.ai-factory/plans/15-milestone-rescue-refactor-repair-by-depth-roll-back-to-the-repaired-state.md`
**Spec:** `.ai-factory/notes/25-milestone-rescue-rewrite-rollback.md`
**Prior review:** `…-review-1.md` (3 findings — all resolved, see below)
**Risk Level:** 🟢 Low — faithful skill-instruction refactor, internally consistent, precision floor intact.

## Scope

Only `src/skills/milestone-rescue/SKILL.md` carries behavior. The other staged paths
(`ROADMAP.md`, `notes/25-…`, plan, plan-reviews, plan `.json`, review-1) are process
artifacts and are not runtime logic.

## Review-1 findings — all resolved

1. **(Low) Forced spec edit at deeper depths** — resolved. Both spec+plan (lines 209–211)
   and spec+plan+code (lines 226–228) now read "If the requirement itself was implicated,
   edit the spec note + contract line … If the spec is already correct, this step is a
   no-op," restoring spec note 25's "edited only when the requirement itself was the
   problem" intent.
2. **(Info) Non-convergence option-2 routing divergence** — resolved. Step 4 now ends with
   "Proceed to Step 5 with the user's choice for all three options" (line 137); the
   conflicting "proceed to Step 5.5 directly" instruction was removed, so all three
   non-convergence options flow through the single Step 5 block.
3. **(Info) Step 5.5 "After `$TARGET_FILE` is updated" precondition** — resolved. Reworded
   to "After completing the repair (if any)" (line 271).

## Verification performed

- Read the current `SKILL.md` in full and the complete `git diff HEAD`.
- **Precision-floor blocks preserved** (the four the plan mandated keeping verbatim):
  - Per-variant deleted-file set + git-native commands (`??`→`git clean -f`, `A `→`git rm -f`):
    present generally (178–179) and per depth (spec 198–201, spec+plan 213, spec+plan+code 231).
  - 5-row closed-set `step` table mirroring `orchestrator/main.py` (247–253), with the
    "do not let them diverge" guard.
  - "Update **only** the `step` key … preserve `planner`/`implementer`/`elapsed`" (216–218,
    233–234, 308–310).
  - Step-1 artifact-discovery block (32–55) — intact; still consumed by `milestone-rescue-audit`.
- **Step/sidecar transitions re-checked against the closed-set table — all correct:**
  - spec → delete plan `.md` + sidecar → orchestrator falls to "plan absent → plan attempt 1."
  - spec+plan → keep plan, delete plan-reviews/reviews/patches, `step="planned"` → resumes
    "plan-review, attempt 1"; always-valid guard satisfied (plan `.md` present).
  - spec+plan+code → keep plan + passing plan-reviews + hand-fix diff, delete reviews/patches,
    `step="implemented"` → resumes "review, iter 1"; always-valid guard satisfied (plan present
    + non-empty working diff from the hand-fix).
- **`"plan_reviewed"` retired** — not written anywhere; remains in the table as
  orchestrator-contract reference only, with explicit note (line 259).
- **`$TARGET_FILE` resolution preserved** (111–116) — drives the spec-tier contract-line edit
  and Step 5.5 scan.
- Frontmatter intact (`name` = dir, `allowed-tools`/`argument-hint` unchanged); body 315 lines
  (≤ 500).

## Findings

None against this change. The diff introduces no bugs, contradictions, or incorrect state
transitions, and resolves all three review-1 findings.

## Non-blocking observations (pre-existing, out of scope for this diff)

These predate the refactor and were preserved deliberately (the plan's precision floor required
keeping `$TARGET_FILE` resolution and the artifact sets verbatim). Recording them for future
consideration, not as defects against this change:

- **"Commit the deliverable" option performs no commit.** In the non-convergence path, option 1
  ("Commit the deliverable") and option 3 lead to Step 5 leaving all artifacts in place and Step
  5.5 being a no-op — the skill never runs `git commit`. The disposition is effectively deferred
  to the user/orchestrator. This matches the original skill's behavior, but the label reads as if
  the skill commits. A future tweak could either perform the commit (the skill holds `Bash(git *)`)
  or relabel to "Keep artifacts for manual commit."
- **`$TARGET_FILE` test-routing keyword `spec`.** The heuristic routes to `ROADMAP_TESTS.md` when
  the slug/artifacts contain "test, tests, spec" (line 113). "spec" is core vocabulary of this
  skill's own artifacts ("spec note", "specification gap"), so artifact-content matching risks
  misrouting a non-test milestone. The explicit file argument overrides it, and it is unchanged
  from the original — but worth narrowing (e.g. match the slug, not artifact prose) if revisited.
- **Non-convergence option 2 (re-run) leaves the sidecar at its terminal `review_failed:N`.**
  The user explicitly overrides the "commit instead" recommendation, so the orchestrator resumes
  at implement iter N+1 (or re-stops if N is at the cap). Consistent with retiring the
  `"plan_reviewed"` write; acceptable, just noting the semantics.

## Verdict

The refactor is correct, faithful to spec note 25, and resolves every review-1 finding. The
precision-floor blocks survived a heavy −235-line compression unchanged, and all sidecar/step
transitions land the orchestrator in the intended phase. No findings against this change; the
non-blocking observations are pre-existing and out of scope.

REVIEW_PASS
