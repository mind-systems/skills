# Code Review: aif-docs documentation index moves to CLAUDE.md

**Files changed:** `src/skills/aif-docs/SKILL.md`, `src/skills/aif-docs/references/REVIEW-CHECKLISTS.md`
**Risk level:** 🟢 Low — instructional (skill) markdown; no executable code, no runtime/security surface.

## Verification against the plan

All eight tasks landed and are internally consistent:

- **Task 1 (Principle 3):** reworded — CLAUDE.md named as the index home; README limited to a pointer line. ✅
- **Task 2 (State A template + rules):** README `## Documentation` table removed, replaced by `See [documentation](<readme-to-docs-dir>/) for full docs.`; "Key rules" bullet updated to "single pointer line". ✅
- **Task 3 (new index step 2.2b):** CLAUDE.md `## Documentation | Doc | What it covers |` block added, README not listed, <12-word descriptions, logical-reading-order rule, create-if-absent. ✅
- **Task 4 (Step 1.1 link):** retargeted to CLAUDE.md's Documentation section. ✅
- **Task 5 (State B):** all three sites retargeted (stays-in-README list, proposal example, execute-the-split now creates the CLAUDE.md section). ✅
- **Task 6 (State C audit):** legacy-README-table flag added; generic broken-links check left intact. ✅
- **Task 7 (Step 5):** redirect carve-out sentence added; the dangling ordering reference (old "same order as the README Documentation table") retargeted to the CLAUDE.md section. ✅
- **Task 8b (ownership):** CLAUDE.md's Documentation section added to Artifact Ownership and Important Rule #7, scoped to the section only. ✅
- **Task 8 (REVIEW-CHECKLISTS.md):** the three enforced rules retargeted — line 8 drops "documentation table", line 44 points at CLAUDE.md, and the self-reverting "Add table" auto-fix (line 57) is replaced by a CLAUDE.md create/update row plus a legacy-README-table detector. ✅

## Correctness checks performed

- **Self-revert bug (the plan-review's Critical Issue 1) is resolved.** The Standards-Compliance auto-fix no longer re-adds a README table; on the next State C run it instead maintains the CLAUDE.md section and flags a legacy README table. No path now restores the removed table.
- **No stragglers.** `grep -ni "documentation table|documentation links table|README Documentation"` across `src/skills/aif-docs/` returns nothing — every reference to the old README table was updated.
- **Cross-references resolve.** Step 5's "(Step 2.2b)" points at the real new heading; State B 2.3 and the checklist auto-fix all name the same `## Documentation` section in CLAUDE.md.
- **Scope respected.** Only the two intended files changed; upstream mirror and frontmatter untouched.
- **AGENTS.md double-index** is a deliberate, spec-sanctioned decision (documented in the plan's Scope & invariants), not a regression.

No bugs, security issues, or correctness problems found.

## Advisory notes (non-blocking, no action required for this milestone)

1. **New placeholder token `<repo-root-to-docs-dir>` in 2.2b.** Every other doc-link placeholder in the skill is `<readme-to-docs-dir>` or `<resolved docs dir>`. Since the project's CLAUDE.md sits at repo root alongside README, this new token resolves to the identical relative path as `<readme-to-docs-dir>`. It's self-descriptive and resolves correctly, but introducing a second name for the same computed value is a slight inconsistency an implementing agent must reconcile. Harmless; could reuse `<readme-to-docs-dir>` for uniformity.

2. **Body grew 575 → 587 lines (net +12).** The spec asked not to grow the already-over-500-line body materially and to prefer rewording over adding blocks; the 2.2b block is a genuine ~18-line addition (partly offset by the removed table). This is within reason given the feature must document the new format, and the immediate follow-on milestone (ROADMAP line 87 / note 49) relocates exactly this kind of block to `references/`. Flagged only so task 49 knows 2.2b is a diet candidate.

3. **2.2b ordered before 2.3 in State A** (index written before the doc files it lists are generated). This mirrors the original ordering (the README table also preceded 2.3), the final run state is consistent, and it's a single run — no real inconsistency. Noted for completeness only.

REVIEW_PASS
