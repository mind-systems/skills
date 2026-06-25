# Plan Review — aif-docs strip nav headers / See Also + upstream-sync protection (round 3)

**Plan:** `.ai-factory/plans/14-aif-docs-strip-nav-headers-see-also-and-protect-from-upstream-sync.md`
**Risk Level:** 🟢 Low

## Verification Method

Read the plan in full, then verified every file path, line reference, and `old_string`-able anchor against the live codebase:
- `src/skills/aif-docs/SKILL.md` (595 lines, read in full)
- `src/skills/aif-docs/references/REVIEW-CHECKLISTS.md` (read in full)
- `CLAUDE.md` Upstream Sync section (lines 100–119)
- Cross-checked with `grep` for `nav`, `See Also`, `prev/next`, `[Nn]avigation`, `Back to README`.

## Line-Reference Accuracy

Every line number in the plan matches the actual file:

| Plan claim | Actual | Status |
|---|---|---|
| Principle 4 "Navigation" at line ~22 | line 22 | ✅ |
| "Principle 7" refs at lines ~107 / ~515 | lines 107, 515 | ✅ |
| 3D key-rule "navigation, " at line ~108 | line 108 | ✅ |
| Step 1.1 item 1 nav clause at line ~206 | line 206 | ✅ |
| Step 2.3 template nav header / See Also / link-order at ~320–342 | lines 321, 328–331, 334–341 | ✅ |
| Step 2B 2.3 item 2 nav clause at line ~426 | line 426 | ✅ |
| Step 2C 2.1 audit "Navigation" bullet at line ~440 | line 440 | ✅ |
| Step 2C 2.1.1 gaps sentence at line ~447 | line 447 | ✅ |
| Step 2C 2.2 example/fix at ~457 / ~463 | lines 457, 463 | ✅ |
| REVIEW-CHECKLISTS Technical items 9–11 | lines 9–11 | ✅ |
| REVIEW-CHECKLISTS "Navigation and flow" item at 47 (heading 45) | lines 45, 47 | ✅ |
| REVIEW-CHECKLISTS Standards rows 61–63 | lines 61–63 | ✅ |
| REVIEW-CHECKLISTS sample-output line 81 | line 81 | ✅ |
| CLAUDE.md never-overwrite list line ~104 | line 104 | ✅ |
| CLAUDE.md "Intentionally diverged" aif-docs line ~112 | line 112 | ✅ |

## Strengths

- **Collision handling is correct.** Line 515 is touched by both Task 1 (Principle 7→6) and Task 2 (remove "navigation checks,"). The plan explicitly merges them into one coherent final edit, preventing a stale `old_string` failure. Verified the proposed merged line is a valid transform of the actual line 515.
- **Case-sensitivity reasoning is sound.** Task 5 keeps the grep case-sensitive (`nav`, not `-i`) so the intentional survivor `### Navigation and flow` (capital N, REVIEW-CHECKLISTS line 45) is not matched. Confirmed: lowercase `nav` does not match `Navigation`.
- **Intentional survivors correctly scoped.** The HTML `{nav_links}` (line 486) and "generate nav bar" (line 490) in Step 3 are correctly excluded — they belong to the generated HTML site, not markdown doc chrome.
- **Grep-blind leftovers flagged.** The plan proactively notes that REVIEW-CHECKLISTS line 63 ("Back to README") and the Standards rows contain none of Task 5's grep terms, so they must be removed by hand rather than relied on for verification. Good adversarial awareness.
- **Dependency ordering is explicit and correct** (Task 3 → Task 4 → Task 5).
- **Policy reclassification is consistent** with the repo's own Upstream Sync conventions and resolves the genuine permanent conflict between the skill's nav mandate and the global ban in `~/.claude/CLAUDE.md`.

## Observations (non-blocking)

- **WARN — Task 5 grep is also blind to REVIEW-CHECKLISTS line 10.** The item "First doc page has no '← Previous' link; last page has no 'Next →' link" (line 10) contains none of the grep tokens (`nav`/`See Also`/`prev/next`), so a stray leftover would pass verification silently — the same class of blind spot the plan already flagged for line 63. This is mitigated because Task 3 explicitly enumerates line 10 in its "delete the three items" bullet, so it will be removed. Optional hardening: add `← ` or `Next →` to the Task 5 grep. Not required for correctness.
- **INFO — Dropped divergence rationale.** Removing CLAUDE.md line 112 discards the note "3D / target-state docs mode + always-on no-motivation rule added downstream." The never-overwrite list (line 104) carries no per-skill reasons, so this is consistent with the section's format. No action needed.

## Context Gates

- **Architecture:** No `.ai-factory/ARCHITECTURE.md` boundary concerns — change is confined to one skill package plus the repo's own sync policy doc. No gate issue.
- **Rules:** Change directly enforces the global doc-style ban on prev/next nav and "See Also". Aligned, not violated.
- **Roadmap:** Documentation/maintenance change; no milestone linkage required.

## Conclusion

The plan is complete, precise, and internally consistent. All file paths and line references are accurate against the current codebase, edit collisions are pre-resolved, verification handles case-sensitivity and grep-blind leftovers correctly, and dependencies are ordered. No missing steps, wrong assumptions, architectural mistakes, or path/API errors found. The one observation (Task 5 grep blind to line 10) is already covered by Task 3's explicit enumeration.

PLAN_REVIEW_PASS
