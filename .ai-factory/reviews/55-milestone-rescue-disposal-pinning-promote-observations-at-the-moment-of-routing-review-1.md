## Code Review Summary

**Files changed:** `src/skills/orchestrator-artifacts/SKILL.md` (§6 closing sentence), `src/skills/milestone-rescue/SKILL.md` (new Step 5.6 + one What-NOT-to-do bullet)
**Risk Level:** 🟢 Low

Reviewed the full diff against spec `.ai-factory/specs/09-rescue-disposal-pinning.md`, the plan, and the two guard files (`milestone-rescue-audit`, `roadmap-prune`) read where they touch the marker grammar. These are skill-body edits — prose that *is* the executable — so the review targets instruction correctness, cross-file contract coherence, and the stated guards.

### Guards — all hold

- **Writer-set split, nothing else in §6 drifted.** The engine diff replaces exactly the sole-writer sentence; the marker list, append-only accumulation, "Entry text and `Affects:` are never rewritten", the **Pinned** definition, and the sibling dedup rule are byte-identical. `grep` confirms no "written by `milestone-rescue-audit` only" claim survives anywhere (line 60's "markers only accumulate" is unrelated).
- **Audit body and prune gate untouched.** `git status` shows only the two intended `src/` files modified — `milestone-rescue-audit/SKILL.md` and `roadmap-prune/SKILL.md` have empty diffs.
- **≤500 lines.** `wc -l` reports 468 for `milestone-rescue` (was 446; +22 for Step 5.6 and the ban bullet), under budget.
- **No frontmatter change.** `allowed-tools` already grants `Edit`; `loads: orchestrator-artifacts` already declared.

### Correctness

- **Engine ↔ audit coherence.** The new §6 sentence says `[promoted → <path>]` is written by "whichever disposal skill routes the observation into a roadmap task." That is broader than the old audit-only claim by design — it now covers both `milestone-rescue` (Step 5.6) and `milestone-rescue-audit` prune mode. Audit's own `## Write contract` (`:296-306`) already lists `[promoted → <path>]` as a prune-mode write and scopes "the only writes *either one* ever performs" to audit's modes, not to a global monopoly. The two files do not contradict.
- **Caller cites, never redefines.** Step 5.6 references `orchestrator-artifacts §6` and explicitly does not restate the grammar, the pinned definition, or the dedup rule — the load-once engine boundary is respected.
- **Ordering hazard closed.** Step 5.6 scopes the pin to review files "still present on disk at pin time" and names which Step-5 depths delete which genres. Because it runs after Step 5's deletions, this prevents an `Edit` against a file already removed; a deleted file has nothing to pin and nothing left for `roadmap-prune`'s gate to flag. Logically correct in all four depth paths.
- **What-NOT-to-do symmetry.** The new bullet bans `[audit-corroborated]` / `[audit-dismissed]` / `[unrouted-reported]` and marker-based dismissal from rescue, mirroring audit's own prohibition — both contracts stay legible from either file.
- **Behavior baseline reproduced.** The milestone-52 hand-pinned entries (`[promoted → …]` pointing at specs 07/08, every sibling occurrence marked) are exactly what Step 5.6 now prescribes — the live pattern is now documented behavior.

### Notes (non-blocking, no change required)

- The "downstream **disposal** tools" framing technically also umbrellas the evaluative `[audit-corroborated]`/`[audit-dismissed]` marks, which are evaluation rather than disposal. The sentence carves them out per-marker immediately, so meaning is unambiguous, and the wording is verbatim from ratified spec 09 §2 — outside this change's file boundary. Already captured as a deferred observation in plan-review-2 for the spec author; not a code defect.

No correctness, security, or runtime concerns. The change is faithful to the spec and internally consistent across the engine and both guard files.

REVIEW_PASS
