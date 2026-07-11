## Plan Review Summary

**Plan:** 4.7 — roadmap-prune: sweep and gate learn the per-roadmap artifact subdirectories
**Files planned to change:** `src/skills/roadmap-prune/SKILL.md` (only)
**Risk Level:** 🟢 Low

Reviewed against the full reference chain: plan → spec `.ai-factory/specs/49-prune-sweep-per-roadmap-subdirs.md` → layout owner `orchestrator-artifacts` §1 → governing doc `docs/multiuser-roadmaps.md` § «Разрешение целевого файла» (amended). Target file `src/skills/roadmap-prune/SKILL.md` read in full; ROADMAP.md contract line 219 matches the plan; predecessor 4.6 (line 217, `[x]`) did land the subdir layout and `patches/` retirement in `orchestrator-artifacts` §1, so the layout this plan references exists. plan-review-1 read for continuity.

### Context Gates
- **Architecture / composition**: PASS. All three tasks honor the `loads: orchestrator-artifacts` edge — the layout is referenced, never restated (explicit "do not restate the layout" in Task 1). Mechanism/policy split intact.
- **Rules**: PASS. "Instructions only, no rationale prose" preserved (Task 2 caps the single allowed divergence sentence; Tasks 1 & 3 instruction-only). 3.1's ledger text and 4.4's two policy sentences called out as untouched; commit policy untouched.
- **Roadmap alignment**: PASS. Title matches line 219; spec 49's `Governing spec` and layout references resolve.

### Line-reference & grounding accuracy (re-verified against the file)
- The four flat dirs incl. `patches/` sit at line **267** — Task 1's target. `grep -n "patches"` returns **exactly one** hit (267), so Task 3's "grep → zero" verification is achievable.
- The three "Step 5 deletes" premise sites are real and located exactly where the plan claims: line **43** (item-2 hand-off clause), line **67** (item-6 rationale), line **327** (Step-8 parenthetical). The stated grep `"Step 5 delet\|deleted them\|before Step 5"` matches all three and no fourth. Accurate.
- `test-runs/` appears at lines **71** (Step-0 parity) and **274** (Step-5 tests-mode sentence) — both covered by the plan (Task 2 and Task 1 respectively).
- Prior review's Finding 1 (the "either partner" wording in Task 1's test-runs bullet that risked broadening the sweep to a main-roadmap prune) is **resolved** in this revision: Task 1 now separates the two concerns explicitly — "keep the tests-mode gate explicit and unchanged in meaning… Do not broaden the sweep to the main-roadmap prune" — while stating stem-sharing as path resolution only. The regression the prior review warned about is closed.

### Findings
None blocking. The plan is complete, internally consistent, and grounded:
- Default-pair vs. named discrimination is implementable from the argument path (`.ai-factory/ROADMAP.md`/`ROADMAP_TESTS.md` → default; `roadmaps/…` → named).
- The `-tests` → `<name>` stem-stripping is pinned explicitly as a fantasy-hole closure rather than left to raw-basename derivation, and is grounded in `orchestrator-artifacts` §1's "same stem segment under … `test-runs/`".
- The gate-scope (repo-wide) vs. margin-capture-scope (follows the sweep) divergence is stated as an explicit instruction, and all three "Step 5 deletes" premises are reconciled with the sweep-scoped capture so hand-off (line 43), rationale (line 67), and Step-8 echo (line 327) agree.
- Item 3 (spec `rm -f`) and item 1 (tag capture) are correctly left unchanged — `Spec:` tags carry exact paths, so spec deletion is subdir-agnostic for named roadmaps (`specs/<name>/…`) too.
- Task 3's grep-and-reconcile of `## What NOT to do` and the Step-5 preamble is a sound safety net; I confirmed neither currently carries a flat-only assumption beyond the ones the plan already targets, so the residual sweep will find nothing to change — harmless.

### Positive Notes
- Reference discipline is exemplary: every task cites the layout owner and refuses to duplicate it.
- The cross-clause coherence pass (three premises + one grep proof) is the kind of reconciliation that is usually missed; it is spelled out task-by-task.
- Byte-stability of the default-pair path (three flat dirs minus `patches/`) is preserved and stated, matching the spec's solo-repo invariant.
- The verification section is executable and mirrors the spec's own, including the `-tests` dry-read case.

## Deferred observations
- Affects: unknown (orchestrator repo — outside this milestone's file boundary) — the plan's central `-tests` → `<name>` stem-stripping rests on `orchestrator-artifacts` §1's "same stem segment under … `test-runs/`" and the default-pair analogy, which is the correct authoritative reference inside this repo. The Russian governing doc phrases the same rule as "поддиректорию по стему его файла" (line 47), whose literal reading of a `roadmaps/<name>-tests.md` file stem would be `<name>-tests`. The two are reconciled in favor of the shared single segment (matching how `ROADMAP_TESTS.md` shares `ROADMAP.md`'s flat dirs), and the plan pins that reading deliberately — but the true ground truth is the orchestrator's own stem-derivation code (`orchestrator/main.py`, per §7's mirrors-invariant), which lives in a different repo and cannot be verified from here. Worth a one-time confirmation against that code that a named test roadmap's `test-runs` are actually written under `<name>/` and not `<name>-tests/`; if the orchestrator ever wrote the raw basename, prune would leave `test-runs/<name>-tests/` undeleted. No action inside this milestone. [routed → ~/projects/orchestrator/.ai-factory/specs/17-artifact-subdir-strip-tests-suffix.md]

PLAN_REVIEW_PASS
