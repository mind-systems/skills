# Plan Review: aif-docs — strip nav headers / See Also and protect from upstream sync

**Plan:** `.ai-factory/plans/14-aif-docs-strip-nav-headers-see-also-and-protect-from-upstream-sync.md`
**Risk Level:** 🟡 Medium — solid structure and accurate line numbers, but two real coverage gaps must be closed before implementation.

## Verification Performed
- Read the full target files: `src/skills/aif-docs/SKILL.md`, `src/skills/aif-docs/references/REVIEW-CHECKLISTS.md`, `CLAUDE.md` (Upstream Sync section).
- Cross-checked every line number cited in the plan against the actual content via `grep`.

All line-number references in the plan are accurate (Tasks 1–4). The grep-confirmed locations match the plan's claims for lines 22, 107, 206, 321, 328, 334–341, 426, 440, 447, 457, 463, 486, 490, 515 (SKILL.md) and 9–11, 47, 61–62, 81 (REVIEW-CHECKLISTS.md), and lines 104/112 (CLAUDE.md).

## Critical Issues

### 1. Missing edit — SKILL.md line 108 references "navigation" (not in any task)
Line 108, inside the **3D mode key rules** list, reads:

> `- All formatting, navigation, language-matching, scannability, and ownership rules apply unchanged.`

After this change there is no "navigation" rule anymore, so the word is stale. Crucially, this line is **not** listed in Task 2's seven edit spots, yet it contains the lowercase token `navigation`, which **Task 5's verification grep (`grep -n "nav\|See Also\|prev/next"`, no `-i`) will flag as an unexpected match.** The plan explicitly tells the implementer to expect *only* the HTML nav-bar references (`{nav_links}`, "generate nav bar") in Step 3 — line 108 is neither, so the verification step will trip on a residual the task list never told the implementer to remove.

**Fix:** Add line 108 to Task 2 — strip `navigation, ` so it reads "All formatting, language-matching, scannability, and ownership rules apply unchanged." (mirrors the Task 2 treatment of "navigation checks," on line 515).

### 2. Orphaned audit rule — REVIEW-CHECKLISTS.md line 63 "Old 'Back to README' format" (escapes verification)
Task 3 removes the "No prev/next navigation" (line 61) and "No 'See Also' section" (line 62) rows of the Standards Compliance table, but leaves line 63:

> `| Old "Back to README" format | Link path or text doesn't match current pattern | Update to current format |`

Task 2 (Step 2.3) deletes the *entire* navigation header line from the doc template (line 321), which is the only place the `[Back to README]` link is defined, plus the worked example at lines 337–340. So after implementation **no generated doc will contain a "Back to README" header at all** — yet this compliance row still instructs the auditor to detect and "update to current format" a navigation backlink that the skill no longer produces. It is a self-contradictory leftover.

This residual is **not caught by Task 5's grep**: "Back to README" contains none of the search terms `nav` / `See Also` / `prev/next`, and the `nav` pattern is case-sensitive so it won't match anything on that line. It will silently survive verification.

**Fix:** Either (a) delete the line-63 row as part of Task 3, or (b) make a conscious decision to retain a standalone "Back to README" backlink in docs (the global ban in `~/.claude/CLAUDE.md` targets prev/next and "See Also" specifically, not a single backlink) and adjust the template accordingly. The plan currently does neither — it removes the backlink from the template but keeps the rule that polices it.

## Minor Issues / Notes

- **Task 3 count mismatch (cosmetic):** the task title says "the 6 nav / See Also entries" but enumerates 7 deletions: Technical lines 9, 10, 11 (3) + Readability line 47 (1) + Standards table lines 61, 62 (2) + Sample output line 81 (1) = 7. No functional impact; correct the count for clarity.

- **REVIEW-CHECKLISTS.md line 45 heading `### Navigation and flow`:** after Task 3 removes line 47, the two remaining items (lines 46 "where to go next" and 48 "Documentation table ordering") still concern reading flow, so the heading is defensible. It is also not grep-caught (capital "N"). Acceptable to keep — just confirm the implementer leaves the heading intact rather than deleting an now-single-purpose subsection.

- **Line 515 is touched by both Task 1 and Task 2** (Principle 7→6 renumber *and* removing "navigation checks,"). Both edits are independent and compatible, but the implementer should apply them as one coherent final line: "...Readability & Completeness checklist, README length, no-motivation pass (Principle 6)." Worth an explicit note so the two tasks don't collide on a stale `old_string`.

## Positive Notes
- Line numbers are precise and verified — rare and valuable in a plan; the "find by content" hedging is appropriate.
- Correctly distinguishes the markdown doc nav header (to remove) from the generated HTML site nav bar `{nav_links}` in Step 3 (to retain) — an easy thing to get wrong.
- Task 1 cross-reference handling is complete: the only numbered Principle references in the file are lines 107 and 515, both covered.
- Phase ordering with dependencies (Task 3 → Task 4 → Task 5) and a final grep-based verification gate is sound.
- Task 4 correctly reflects the actual CLAUDE.md structure (never-overwrite list line 104, "intentionally diverged" list line 112) and aligns with the global doc-style ban that motivates the change.

## Verdict
Do not implement as-is. Close Issue #1 (add line 108 to Task 2) and Issue #2 (resolve the line-63 "Back to README" row in Task 3) — both are genuine coverage gaps, and #2 in particular slips past the plan's own verification step. With those two additions the plan is complete and correct.
