## Code Re-Review — 4.7 roadmap-prune (round 2)

Re-read `src/skills/roadmap-prune/SKILL.md` in full against the prior review, the plan, spec `.ai-factory/specs/49-prune-sweep-per-roadmap-subdirs.md`, layout owner `orchestrator-artifacts` §1, and `docs/multiuser-roadmaps.md`. `git diff HEAD` shows only one hunk changed since round 1 — the Step 8 line — the rest of the diff is byte-identical to what round 1 already validated.

### Verdicts on round-1 findings

**Finding 1 (Low — Step 8 default-pair branch omits flat `test-runs/`): FIXED.**
Current `src/skills/roadmap-prune/SKILL.md:349-352`:
> "List the dirs swept in Step 5 — the flat three dirs **(plus flat `test-runs/` in tests mode)** for a default-pair prune, or the pruned stem's `plans/<stem>/`, `plan-reviews/<stem>/`, `reviews/<stem>/` (plus `test-runs/<stem>/` in tests mode) for a named prune — and the spec files deleted in Step 5."

The parenthetical is now mirrored onto the default-pair branch, so a default `ROADMAP_TESTS.md` prune's swept `test-runs/` is reported. Matches Step 5's sweep rule (`:296-300`, "`test-runs/` is swept only when the pruned target is the **test** roadmap … flat `test-runs/` for the default pair"). Symmetric with the named branch. Resolved.

**Deferred observation (default-pair `rm -rf plan-reviews/` recursively deletes named stem subdirs): unchanged, as expected — non-blocking, out of this diff's mandate.**
Current `:277-289` still specifies whole-directory `rm -rf plans/ plan-reviews/ reviews/` for the default pair, which is correct per spec 49 §Guards (byte-stable default-pair sweep). This was flagged for the sweep-scoping-policy owner, not as a defect in this milestone; no change was expected and none was made. It remains a latent hazard only in the undocumented mixed scenario (a default roadmap actively pruned while named subdirs exist).

### Full re-review — new issues

Re-verified every spec change point against the current file:
- **`patches/` retired:** `grep -n "patches" src/skills/roadmap-prune/SKILL.md` → no output, exit 1. Zero hits. ✔ (spec verification met)
- **Step 5 sweep (`:277-300`):** default pair → three flat dirs; named → `plans/<stem>/`, `plan-reviews/<stem>/`, `reviews/<stem>/` with `-tests`→main-stem stripping grounded in `orchestrator-artifacts` §1; sibling stems and flat dirs excluded; `test-runs/` gated to test-roadmap prunes only. ✔
- **Step 0 gate (`:40-52`):** scans at any depth, repo-wide by design; hand-off to step 6 scoped to Step 5's sweep set. ✔
- **Item 6 (`:71-78`):** phrase-check scoped to the sweep set with explicit "at any depth, scoped to the sweep, never repo-wide"; both stale "Step 5 deletes these files" clauses reconciled (item 2 hand-off and item 6 premise now agree). ✔
- **Step 8 (`:349-359`):** enumeration now accurate for all four modes; "deleted the swept files" wording aligned with sweep scope. ✔
- **Untouched guards:** 3.1's ledger text (`:16-28`, `:208-263`) and 4.4's integration-branch sentences (`:210-213`) unchanged; commit policy (`:363-368`) unchanged; specs sweep via `Spec:` tags only (`:290-294`) unchanged. ✔

No new correctness, security, or runtime concerns. The `docs/multiuser-roadmaps.md` working-tree edit remains out of this milestone's file boundary (engine's named-roadmap task) and is internally consistent.

REVIEW_PASS
