# Plan Review 2: aif-docs — strip nav headers / See Also and protect from upstream sync

**Plan:** `.ai-factory/plans/14-aif-docs-strip-nav-headers-see-also-and-protect-from-upstream-sync.md`
**Files targeted:** `src/skills/aif-docs/SKILL.md`, `src/skills/aif-docs/references/REVIEW-CHECKLISTS.md`, `CLAUDE.md`
**Risk Level:** 🟡 Medium (one missed edit spot that the plan's own verification step would trip on)

## Summary

The plan is well-structured and its line references are accurate. I cross-checked every spot against the live files:

- **Task 1** (remove Principle 4, renumber, fix references): correct. Principle 4 is line 22. The only numbered references to "Principle 7" are lines 107 and 515 — both identified by the plan. A grep for `Principle` confirms no other numbered references exist (line 447 says "Core Principles" generically). ✅
- **Task 2** spots: all seven line references verified accurate (206, 320–342 template, 426, 440, 447, 457/463, 515). ✅
- **Task 3** (REVIEW-CHECKLISTS.md): all six entries verified — Technical lines 9–11, Readability line 47, Standards table lines 61–62, sample output line 81. ✅
- **Task 4** (CLAUDE.md upstream policy): the never-overwrite list is line 104, the "Intentionally diverged" `aif-docs` entry is line 112. Both correctly identified. ✅

## Critical Issues

### 1. Missed nav reference at SKILL.md line 108 — also breaks the Task 5 verification

The plan does not touch **line 108** in the 3D-mode "Key rules" block:

```
- All formatting, navigation, language-matching, scannability, and ownership rules apply unchanged.
```

Two problems:

1. **Stale semantics.** Once the navigation rules are deleted everywhere else, this clause asserts that "navigation … rules apply unchanged" — a reference to a rule set that no longer exists. The word `navigation` should be dropped from this enumeration (leaving "All formatting, language-matching, scannability, and ownership rules apply unchanged.").

2. **Task 5 verification will flag it as an unexpected match — and loop.** Task 5 runs `grep -n "nav\|See Also\|prev/next" SKILL.md …` and expects "zero matches except the unrelated HTML nav-bar references in Step 3 (`{nav_links}`, generate nav bar)". Line 108 contains lowercase `navigation`, which matches `nav`. It is in the Step 1 / 3D section, **not** Step 3, so it is not a permitted exception. The verifier would treat it as a residual match and, per Task 5's own instruction ("If any unexpected match remains, return to the relevant task and remove it"), bounce back — but no task covers line 108, so the loop has no clean exit without improvising.

**Fix:** Add line 108 to Task 2's edit list — remove `navigation, ` from the clause. (Note: line 108 is distinct from line 107, which Task 1 already edits for the Principle-7→6 renumber; both lines need attention but for different reasons.)

## Non-blocking Notes

- **Task 5 grep is case-sensitive, which is fine but worth knowing.** `### Navigation and flow` (REVIEW-CHECKLISTS.md line 45) survives Task 3 and contains capital-N `Navigation`, so a case-sensitive `grep "nav"` will *not* match it — no false positive there. Keeping that subsection header is reasonable since its two remaining items (lines 46, 48) concern README flow and the doc-table order, not prev/next chrome. No change needed, but if the implementer adds `-i` to the grep, line 45 would then trip it. Recommend keeping the grep case-sensitive as written, or explicitly listing line 45 as an allowed exception.
- **Task 2, Step 2C 2.2 line range.** The plan cites "lines ~457–458 and proposed-fix line ~463" but only the single line 457 (the prev/next warning) is deleted; line 458 (`api.md is missing`) stays. The prose is clear about which line to remove, so this is just loose range notation, not an error.

## Positive Notes

- Every line-number citation in the plan matched the live files on verification — unusually precise.
- The plan correctly preserves the HTML site nav bar (`{nav_links}`, Step 3.2/3.3) and explicitly calls out not touching it — the right distinction between markdown doc-header chrome and generated-site navigation.
- Phase ordering with dependencies (Task 3 → 4 → 5) and the closing grep-based verification is a sound shape for a pure find/delete refactor.
- Task 4 correctly results in `aif-docs` appearing in exactly one list, resolving the permanent policy conflict cleanly.

## Verdict

One required fix before implementation: **add SKILL.md line 108 to Task 2** and update Task 5's expected-exceptions note accordingly. Everything else is accurate and ready.
