# Plan Review: milestone-rescue — repair by depth, roll back to the repaired state

**Plan:** `.ai-factory/plans/15-milestone-rescue-refactor-repair-by-depth-roll-back-to-the-repaired-state.md`
**Target:** `src/skills/milestone-rescue/SKILL.md` (single file, + one CLAUDE.md verification touch)
**Source spec:** `.ai-factory/notes/25-milestone-rescue-rewrite-rollback.md`
**Risk Level:** 🟡 Low–Medium

## Verification performed

- Read the plan, the current `SKILL.md` (401 lines), and the source spec note 25 — the plan is a **faithful, near-1:1 decomposition** of the spec note. Repair-depth → rollback-state mapping, precision-floor list, compression targets, frontmatter rules, and presentation order (spec → spec+plan → spec+plan+code) all match.
- **Line references are accurate.** Intro 16–24, non-convergence 67–90, issue-extraction 95–125, Step 4 templates 128–219, sidecar prose 289–302 — every cited range matches the real file.
- **Cross-skill dependency confirmed.** `milestone-rescue-audit/SKILL.md` (Inputs block, line 30–31) does point at `milestone-rescue` "for the artifact layout and directory structure" — so the precision-floor rule to keep the Step‑1 artifact-discovery block verbatim is correct and necessary.
- **Two-tier spec model confirmed.** Note 09 establishes the "ROADMAP summary line (contract) + per-task spec note" pair, so the plan's "contract line IS edited" framing is grounded, not invented.
- **CLAUDE.md guard confirmed** already present (line 104, "Custom skills — never overwrite from upstream"). Task 8's "confirm, add only if missing" is correct.
- `orchestrator/main.py` is intentionally absent from this meta-repo (it lives in `~/projects/orchestrator`); the `step` table is a documented contract mirror, not a local code reference — consistent with the precision-floor intent.

## Critical Issues

None. No blocking defect; the plan is implementable as written.

## Findings (recommended fixes before implementing)

### 1. `$TARGET_FILE` resolution risks being deleted with the Step 4 templates — Medium
Task 5 says "replace the three large `AskUserQuestion` code blocks … current lines ~128–219." That range **includes the `$TARGET_FILE` determination** (lines 130–133) and the milestone-line lookup (line 135), not just the three code blocks. This logic decides whether the contract line lives in `ROADMAP.md` or `ROADMAP_TESTS.md` — and it is still load-bearing in the new model:
- **Spec-tier repair** edits the contract line, which must target the correct roadmap file.
- **Step 5.5 propagation** (Task 7) scans `$TARGET_FILE` for downstream `- [ ]` milestones (current lines 350, 232, 238, 247 all reference it).
- The plan keeps `argument-hint: "[…ROADMAP.md | ROADMAP_TESTS.md]"` (Task 1), so the dual-file capability is explicitly retained — but no task says to preserve the resolution that consumes it.

**Recommendation:** add an explicit note to Task 5 (and/or Task 6/7) that the `$TARGET_FILE` resolution survives the template removal and feeds both the spec-tier contract-line edit and Step 5.5. Otherwise the implementer may delete it along with the surrounding Step 4 prose and silently break `ROADMAP_TESTS.md` support.

### 2. Non-convergence "commit / leave intact" has no explicit apply home — Low–Medium
The spec compresses non-convergence into one diagnosis outcome ("recommend committing"), and the plan reflects that: Task 3 produces the diagnosis, Task 5 folds the recommendation into the depth menu, Task 7 makes propagation a no-op. But the **apply behavior** for the commit outcome — leave all artifacts in place, do **not** delete anything, do **not** touch the sidecar (current lines 225–229) — lands in no task. Task 6's apply section is "keyed by the three repair depths," and commit-as-is is a fourth, terminal outcome (no rollback at all).

**Recommendation:** have Task 6 explicitly state the non-convergence/commit path performs no cleanup and no sidecar change, so it isn't lost when the apply section is reorganized around the three depths. (Low impact — "commit" ≈ "do nothing to artifacts" — but the precision-floor philosophy argues for making it explicit.)

### 3. The old re-implement path (`step = "plan_reviewed"`) is intentionally retired — Informational
Worth noting so the implementer isn't confused. The current skill writes `"plan_reviewed"` for the re-implement/non-convergence-rerun path (lines 235, 328). In the new model the deepest depth is **spec+plan+code fixed by hand → `step = "implemented"`** (re-runs *review* on the hand-fixed diff), and there is no "keep plan, discard diff, re-run implementer" option. Consequences the implementer should hold in mind:
- The new flow only ever **writes** `"planned"` (spec+plan), **writes** `"implemented"` (spec+plan+code), or **deletes** the sidecar (spec). The other three `step` values (`plan_review_failed:N`, `plan_reviewed`, `review_failed:N`) remain in the closed-set table **as the orchestrator-contract reference only** — correct, and the precision floor rightly keeps the full 5-row table.
- This is a deliberate behavior change, not a regression — confirmed against spec note 25 §"three repair depths." No action needed beyond not re-introducing a `"plan_reviewed"` write.

## Positive Notes

- Excellent precision-floor discipline: the plan calls out the four must-keep-verbatim blocks (per-variant deleted-file set, the 5-value `step` table mirroring the orchestrator, the "only touch `step`" rule, the Step‑1 discovery block) in both the Constraints header and again inside Tasks 6 and 8 — redundancy that protects them through the merge.
- Task 8 is a genuine consistency gate (step renumbering after the Step 4+5 merge, line budget, frontmatter integrity, CLAUDE.md guard) rather than a rubber stamp.
- Phasing and commit grouping are coherent and dependency-ordered; each commit leaves the file in a sensible intermediate state.
- `allowed-tools` correctly kept as-is — `Edit` now legitimately reaches plan/code/contract-line/spec-note, and no new tool is needed.

## Verdict

The plan is solid and faithful to the spec note. The two findings above are refinements that prevent a load-bearing piece (`$TARGET_FILE` resolution) and a terminal outcome (non-convergence commit) from being dropped during the Step 4/5 merge — address them inline in Tasks 5–7 and the implementation will be clean.
