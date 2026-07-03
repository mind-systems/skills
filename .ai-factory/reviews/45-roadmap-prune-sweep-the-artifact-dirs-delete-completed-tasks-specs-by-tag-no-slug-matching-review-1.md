# Code Review — roadmap-prune sweep (rm mechanism), implemented

**Reviewed:** `git diff HEAD` / `git status` in full; `src/skills/roadmap-prune/SKILL.md` (now blob `25d0178`, changed from HEAD `d8f5931`) read in full; against the plan and governing note 56.
**Risk level:** 🟢 Clean — the milestone is now implemented and faithful to the spec; no correctness, safety, or consistency defects found.

The implementation finally landed (47 insertions, 9 deletions in `SKILL.md`). This pass reviews the real code.

---

## Plan conformance — all four tasks present and correct

- **Task 1 (sweep step):** new `## Step 5 — Sweep completed artifacts and specs`, placed after Step 4 and before the ROADMAP.md edit. Capture-first of every `[x]` line's `Spec:` tag (tagless lines skipped, never synthesized); `rm -rf` the four dirs under `<target repo root>/.ai-factory/`; `rm -f` each captured spec path. Invariant stated (deletion only via `[x]` tags; open `[ ]` specs never touched). `allowed-tools` gains `Bash(rm *)`; `description` updated. ✔
- **Task 2 (ordering):** Step 6 "Delete the pruned `[x]` tasks … only after Step 5's tag capture has run." ✔
- **Task 3 (rule replacement + description):** the old `Do not delete the notes/ directory…` line is gone; replaced by the sweep-model rules (tag-only deletion, `handoffs/` untouched, no `git rm`, no per-task resolution, instructions-only, no auto-commit). ✔
- **Task 4 (commit policy / report / parity):** `## Commit (on request only, never automatic)` with `git add -A` + one `Roadmap prune` commit; `## Step 8 — Summary report`; `ROADMAP_TESTS.md`/`test-runs/` parity in Step 5. ✔

## Correctness checks — all pass

- **Path-base model (the safety-critical, plan-review-2 item) is correctly two-base.** Step 5 derives the target repo root as the parent of the target `.ai-factory/`; the four dirs resolve under `<root>/.ai-factory/`, and captured tag paths (already `.ai-factory/`-prefixed) are joined onto the **root**, not re-prefixed. A captured `.ai-factory/notes/NN.md` correctly resolves to `<root>/.ai-factory/notes/NN.md` — no doubled segment, no silent `rm -f` miss. Matches note 56 line 22 and the contract line verbatim in intent.
- **Staging is clean under `rm`.** Plain `rm` leaves deletions unstaged; the ARCHITECTURE.md (4.2) and ROADMAP.md (Step 6) edits are unstaged too. The single `git add -A` at commit time stages all of them together (deletions + modifications) — the earlier `git rm` staging-split (which dropped the markdown edits from a plain `git commit`) cannot occur here. This is the mechanism change working as intended.
- **Step renumbering is internally consistent.** Grep of all `Step N` references: Step 3/4/4.1/2.2 back-refs intact; new tail is 5 (Sweep) → 6 (Update ROADMAP) → 7 (Verify) → 8 (Summary report), and every cross-reference ("after Step 4 and before Step 6", "after Step 5's tag capture", "swept in Step 5") resolves. No dangling old numbers.
- **Snapshot ordering holds.** Step 4.1 records HEAD "before touching any files" — ahead of the 4.2 ARCHITECTURE write and the Step 5 `rm`. The drop-history snapshot remains the pre-change restore point.
- **Verify (Step 7) left intact;** the summary report (Step 8) is additive and informational — "no extended verify" scope honored.
- **`Reading the history later` still valid.** Its `git diff <hash>~1 <hash> -- .ai-factory/plans/` reads pruned plans at their pre-prune completion hashes; the HEAD-only sweep doesn't touch history. Correctly left unchanged.
- **Instructions-only discipline followed.** No counter-reset claims, no git-semantics or tracked-vs-untracked rationale prose in the body — the imprecise-prose failure mode of the prior attempt is not reintroduced.
- **`docs/overview.md`** references no step numbers and no `git rm`/old rules (grep-clean) — not contradicted by the change; Docs were out of scope for this plan.

## Accepted-by-design (verified as spec-faithful, NOT findings)

These are deliberate decisions recorded in note 56 (Constraints line 40, "instructions only / no guards"); the implementation encodes them exactly, so they are not defects — flagged only so the operational assumption is explicit:

- **`rm -rf` also deletes untracked/uncommitted files** in the four dirs. Safe only on a settled tree; the spec accepts this and forbids guards or tracked-file filtering. The skill correctly omits any guard.
- **`git add -A` at commit is broad** — it stages every change in the target repo into the `Roadmap prune` commit. Same settled-tree premise; accepted by the spec, and "scoped to the target repo root" bounds it for sub-repo roadmaps.

Both were re-litigated against the note rather than the earlier (rejected) `git rm` design; they are the intended tradeoffs, not regressions.

---

The milestone is implemented and matches the plan and note 56 on every task, with the safety-critical path base correct and the staging model clean. No bugs, security issues, or correctness problems.

REVIEW_PASS
