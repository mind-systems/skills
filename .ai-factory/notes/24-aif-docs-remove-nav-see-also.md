# aif-docs: Remove Nav Headers, See Also, and Protect from Upstream Sync

**Date:** 2026-06-25
**Source:** conversation context

## Key Findings

- Core Principle 4 in `aif-docs/SKILL.md` mandates prev/next nav headers and "See Also" footers — both are explicitly banned by global `~/.claude/CLAUDE.md`. The conflict caused incorrect nav headers to be generated in orchestrator docs this session and rolled back manually.
- After removing these constructs, `aif-docs` has a permanent policy conflict with upstream (upstream mandates what global rules ban) — move it from "Intentionally diverged" to "Custom skills — never overwrite" in `CLAUDE.md`.

## Details

### `src/skills/aif-docs/SKILL.md` — 8 locations

| Line | What to remove |
|------|----------------|
| 22–23 | Entire Core Principle 4 (nav header + See Also mandate); renumber 5→4, 6→5, 7→6 |
| 206 | Step 1.1 item 1: strip "with prev/next navigation header (following Documentation table order) and 'See Also' footer" |
| 320–342 | Step 2.3 template: delete nav header line, See Also section, and the full navigation link order example block |
| 426 | Step 2B 2.3 item 2: strip "+ prev/next navigation header (following Documentation table order) + 'See Also' footer" |
| 443 | Step 2C 2.1: delete the "Navigation — do all docs have prev/next header links and 'See Also'?" audit bullet |
| 447 | Step 2C 2.1.1: remove "missing navigation, missing 'See Also'," from the gaps sentence |
| 457–458 | Step 2C 2.2 example: delete the ⚠️ missing-nav line and the "Add prev/next navigation…" proposed fix line |
| 514 | Step 4: remove "navigation checks" from the "Keep fully active in 3D" list |

### `src/skills/aif-docs/references/REVIEW-CHECKLISTS.md` — 6 locations

| Line | What to remove |
|------|----------------|
| 9 | Checklist item: "Each docs/ file has prev/next navigation header…" |
| 10 | Checklist item: "First doc page has no '← Previous' link; last page has no 'Next →' link" |
| 11 | Checklist item: "Each docs/ file has 'See Also' section at bottom…" |
| 45 | Readability item: "…do prev/next links and 'See Also' guide me logically forward?" |
| 61–62 | Standards compliance auto-fix table rows for "No prev/next navigation" and "No 'See Also' section" |
| 81 | Sample output line: "✅ All pages have navigation" |

### `CLAUDE.md` — Upstream Sync section

1. Remove `aif-docs` line from "Intentionally diverged from upstream — review diff before updating".
2. Append `` `aif-docs` `` to the "Custom skills — never overwrite from upstream" bullet.

"Review diff" made sense for additive features (3D mode). After nav removal the divergence is a permanent policy conflict — no upstream diff can ever be applied.

### Verify

- `grep -n "nav\|See Also\|prev/next\|← \|→" SKILL.md references/REVIEW-CHECKLISTS.md` → zero matches (HTML nav bar in Step 3 is unrelated, stays)
- `grep "aif-docs" CLAUDE.md` → shows only the "Custom skills — never overwrite" line
