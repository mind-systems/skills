## Code Review — 4.6 orchestrator-artifacts: per-roadmap layout; retire `patches/`

**Scope reviewed:** `src/skills/orchestrator-artifacts/SKILL.md` (the only code/product change). Plan, sidecar, and plan-review artifacts are process files, not reviewed for defects.

**Change type:** Pure protocol-reference documentation edit to a load-once engine. No runtime, no executable code, no migrations. "What breaks at runtime" reduces here to "does a downstream reader of this protocol get misrouted or lose a load-bearing invariant."

### Correctness against spec 48

- **Change #1 (per-roadmap rule):** PRESENT and accurate. §1 now states the flat layout is for the default pair (`ROADMAP.md`/`ROADMAP_TESTS.md`), and a named roadmap's artifacts live under a stem-keyed subdirectory — `roadmaps/kg-wmservice.md` → `plans/kg-wmservice/…`, same stem segment under `plan-reviews/`, `reviews/`, `test-runs/`. Matches the spec's example and the governing `docs/multiuser-roadmaps.md` amendment.
- **Change #2 (`patches/` vanishes):** DONE at both sites — §1 layout clause removed and the frontmatter `description` enumeration dropped `patches`. `grep -n "patches" src/skills/orchestrator-artifacts/SKILL.md` → zero hits (exit 1), satisfying the plan's Task 2 verification.
- **Change #3 (§4 survives verbatim):** HONORED. §4's sentence "tracked artifacts belong to completed tasks, uncommitted ones to failed/in-flight" is byte-identical — the load-bearing resume-gate meaning is intact.
- **Guards:** §5/§6 untouched (confirmed). The edit stays descriptive protocol — no procedure introduced. Section remains lean (a few added lines). The default-pair flat description is behaviorally identical to the prior text (only reordered around the removed `patches/` clause and the new subdirectory sentence).

### Notes (non-blocking, not findings)

- The closing sentence "Numbering is per-directory — each subdirectory carries its own `<seq>` axis" is correct in context: "subdirectory" reads as the stem-keyed roadmap subdirectory established in the preceding sentence, matching spec 48's "each subdirectory has its own axis." A reader who instead took "subdirectory" to mean the sibling `plans/`/`plan-reviews/`/`reviews/` dirs could momentarily misread it as breaking the shared-per-task `<seq>` convention, but the immediately prior sentence anchors the referent to the roadmap-stem subdirectory, so the intended meaning holds. Wording nuance only — matches spec intent; no change required.
- Caller drift (`milestone-rescue` still references `patches/` in rollback/frontmatter/prose) is real but explicitly out of this milestone's single-file boundary — already captured as a deferred observation in the plan-review and left to a dedicated cleanup. Not a defect in this change.

No correctness, security, or contract-fidelity issues found.

REVIEW_PASS
