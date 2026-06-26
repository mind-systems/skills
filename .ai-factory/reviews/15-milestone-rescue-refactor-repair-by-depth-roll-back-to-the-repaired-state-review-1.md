# Code Review: milestone-rescue — refactor — repair by depth, roll back to the repaired state

**Change under review:** `src/skills/milestone-rescue/SKILL.md` (382-line diff: −235 / +147; net file 313 lines)
**Plan:** `.ai-factory/plans/15-milestone-rescue-refactor-repair-by-depth-roll-back-to-the-repaired-state.md`
**Spec:** `.ai-factory/notes/25-milestone-rescue-rewrite-rollback.md`
**Risk Level:** 🟢 Low — doc/skill-instruction change, internally consistent, faithful to spec note 25. Findings below are refinements, none blocking.

## Scope

Only `src/skills/milestone-rescue/SKILL.md` is a behavioral change. The other staged files
(`ROADMAP.md` line flip to `[x]` candidate, `notes/25-…`, plan, plan-reviews, plan `.json`)
are process artifacts, not runtime code; not reviewed for logic.

## Verification performed

- Read the new `SKILL.md` in full and the complete `git diff HEAD` for it.
- **Precision-floor blocks survived intact** (the four the plan mandated keeping verbatim):
  1. Per-variant deleted-file set with git-native commands — present generally (lines 180–181) and restated per depth (spec 200–203, spec+plan 213, spec+plan+code 229). `??`→`git clean -f`, `A `→`git rm -f` preserved.
  2. The 5-row closed-set `step` table mirroring `_validate_sidecar_step()`/`_detect_milestone_step()` in `orchestrator/main.py` — present unchanged (lines 245–251) with the "if the orchestrator's accepted set changes, update this table; do not let them diverge" guard.
  3. "Update **only** the `step` key … preserve `planner`/`implementer`/`elapsed`" — present (216–218, 231–232) and in What-NOT-to-do (306–308).
  4. Step-1 artifact-discovery block — kept essentially verbatim (referenced by `milestone-rescue-audit`); still emits the four-dir filter, slug extraction, and read-all-rounds rule.
- **Sidecar/step transitions are correct against the closed-set table:**
  - spec depth → plan `.md` + sidecar deleted → orchestrator falls to "plan absent → plan attempt 1". ✓
  - spec+plan → keep plan, delete plan-reviews/reviews/patches, `step="planned"` → resumes "plan-review, attempt 1" on the corrected plan. ✓ always-valid guard satisfied (plan `.md` present).
  - spec+plan+code → keep plan + passing plan-reviews + hand-fix diff, delete reviews/patches, `step="implemented"` → resumes "review, iter 1". ✓ always-valid guard satisfied (plan present + non-empty working diff exists from the hand-fix).
- **Retired `"plan_reviewed"` write** — confirmed the skill no longer writes it anywhere; the value remains in the table only as the orchestrator-contract reference, with an explicit note (line 257). Matches plan-review-1 finding 3.
- **`$TARGET_FILE` resolution preserved** (lines 111–116) — survived the Step-4 template removal, as plan-review-1 finding 1 required; feeds both the spec-tier contract-line edit and Step 5.5.
- Frontmatter intact: `name` matches dir, `allowed-tools` and `argument-hint` unchanged; body 313 lines (≤ 500).

## Findings

### 1. All three depths are spec-inclusive — a pure plan- or code-only fix is forced to edit the spec note + contract line (Low)

The three repair blocks each begin by editing the spec note **and** the contract line:
- spec+plan, step 1 (line 211): "Edit the spec note + contract line in `$TARGET_FILE` (same as spec depth above)."
- spec+plan+code, step 1 (line 226): "Edit the spec note + contract line in `$TARGET_FILE`."

There is no depth that repairs *only* the plan, or *only* the code, without also touching the
spec tier. For a genuine **mechanical error** (spec correct, plan correct, one wrong line in
code) the shallowest applicable option is spec+plan+code, which instructs the agent to edit a
correct spec note and a correct contract line — spurious edits that can regress a requirement
that was fine.

Spec note 25 anticipated exactly this and the caveat was compressed away:
> "(In practice the spec may already be fine and only the plan/code need touching — the depth is
> 'how far down the cause reaches,' and the spec tier is just the top of that range, edited only
> when the requirement itself was the problem.)"

**Recommendation:** add one clause to the spec+plan and spec+plan+code blocks making the
higher-tier edits conditional — e.g. "Edit the spec note + contract line *only if the requirement
itself was implicated*; if the spec is already correct, this step is a no-op and you repair only
the plan/code below." This restores the spec-note's intent without changing the cumulative-depth
menu. Low severity: the user picks the depth and an explicit "fix Y" overrides, so an attentive
operator avoids the spurious edit — but the default instruction currently mandates it.

### 2. Non-convergence option 2 (re-run) is routed two ways; both are no-ops, but the wording diverges (Informational)

Step 4 (line 135) routes non-convergence **option 2** straight to Step 5.5: "no artifact changes,
no sidecar update — proceed to Step 5.5 directly." Step 5's non-convergence block (line 188) then
says options "1, 2, or 3 … Leave all artifacts in place … Proceed directly to Step 5.5." The net
effect is identical (nothing is deleted, sidecar untouched, reach 5.5), so there is no functional
bug — but an implementer following Step 4 skips the Step 5 block entirely while Step 5 claims to
handle option 2. Consider routing all three non-convergence options through the single Step 5
block for one source of truth.

Also note the behavior change this encodes: the old skill, on re-run, reset `step` to
`"plan_reviewed"` to restart the implement phase from the approved plan. The new skill leaves the
sidecar at whatever terminal `review_failed:N` the run stopped on, so "re-run the pipeline anyway"
resumes at implement iter N+1 (or immediately re-stops if N is at the cap). This is consistent
with the deliberate retirement of the `"plan_reviewed"` write, and the user is explicitly
overriding the "commit instead" recommendation — so it is acceptable, but it is a real semantic
change worth being aware of.

### 3. Step 5.5 precondition "After `$TARGET_FILE` is updated" is not always true (Informational)

Line 269 opens propagation with "After `$TARGET_FILE` is updated, scan the remaining `- [ ]`
milestones." In the non-convergence path `$TARGET_FILE` is never updated, and even in real-defect
paths the contract-line edit may be a no-op (see finding 1). Propagation is correctly a no-op for
non-convergence (guarded at line 265), so nothing breaks — but the precondition reads as if an
update always preceded it. Minor wording; "After completing the repair (if any)…" would be more
accurate.

## Positive notes

- The depth model maps cleanly and correctly onto the orchestrator's resume contract; every
  `step`/deletion combination lands the orchestrator in the intended phase.
- Precision-floor discipline held through a heavy −235-line compression — the four must-keep
  blocks are all present and the `step` table is byte-identical to before.
- The `$TARGET_FILE` resolution and the retired-`plan_reviewed` note (both called out in
  plan-review-1) were correctly carried into the implementation.
- Compression targets from the spec (non-convergence machinery, 4-attribute issue list, three
  large AskUserQuestion templates, sidecar prose) were all collapsed without losing the
  load-bearing rules.

## Verdict

The refactor is faithful, internally consistent, and safe to commit. No blocking or correctness
defects. Finding 1 (forced spec edit at deeper depths) is the only one worth acting on before
commit — a one-clause conditional restores spec note 25's explicit intent and prevents spurious
edits to correct requirements; findings 2 and 3 are wording/clarity refinements.
