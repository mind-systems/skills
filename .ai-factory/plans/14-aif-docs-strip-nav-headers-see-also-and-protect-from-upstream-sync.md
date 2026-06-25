# Plan: aif-docs — strip nav headers / See Also and protect from upstream sync

## Context
Remove every prev/next navigation-header and "See Also" mandate from the `aif-docs` skill (which conflicts with the global ban in `~/.claude/CLAUDE.md`), and reclassify `aif-docs` in this repo's Upstream Sync policy as a never-overwrite custom skill since the divergence is now a permanent policy conflict.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Strip nav / See Also from the skill body

- [x] **Task 1: Remove Core Principle 4 and renumber**
  Files: `src/skills/aif-docs/SKILL.md`
  In the `## Core Principles` list (lines ~19–25), delete the entire Principle 4 ("Navigation. Every doc file … ends with a 'See Also' section …"). Renumber the remaining principles: current 5 (Cross-links) → 4, current 6 (Scannable) → 5, current 7 (State, not process) → 6. Update any in-document references to the renumbered principles — note Step 1 (line ~107) and Step 4 (line ~515) both reference "Principle 7 (state, not process)"; change these to "Principle 6".
  **Collision note:** line ~515 is also edited by Task 2 (removing "navigation checks,"). Apply both edits as one coherent final line so the tasks don't collide on a stale `old_string`: "...Readability & Completeness checklist, README length, no-motivation pass (Principle 6)."

- [x] **Task 2: Strip nav / See Also from all 8 remaining SKILL.md spots**
  Files: `src/skills/aif-docs/SKILL.md`
  Apply these edits (line numbers approximate, find by content):
  - **3D mode key rules (line ~108):** strip "navigation, " from the line "All formatting, navigation, language-matching, scannability, and ownership rules apply unchanged." → "All formatting, language-matching, scannability, and ownership rules apply unchanged." (the navigation rule no longer exists; the lowercase `navigation` token would otherwise trip Task 5's case-sensitive grep). This is line 108, distinct from line 107 which Task 1 edits for the Principle-7→6 renumber.
  - **Step 1.1, item 1 (line ~206):** remove the clause "with prev/next navigation header (following Documentation table order) and 'See Also' footer" so the step just creates the target file in the resolved docs directory.
  - **Step 2.3 template (lines ~320–342):** delete the leading prev/next navigation header line from the markdown template, delete the `## See Also` section block, and delete the entire "Navigation link order" explanatory paragraph plus its fenced example block (the `getting-started.md: … architecture.md: …` listing).
  - **Step 2B 2.3, item 2 (line ~426):** strip "+ prev/next navigation header (following Documentation table order) + 'See Also' footer" so it reads as creating each doc file with content from README only.
  - **Step 2C 2.1 audit list (line ~440):** delete the bullet "Navigation — do all docs have prev/next header links and 'See Also'?".
  - **Step 2C 2.1.1 (line ~447):** remove "missing navigation, missing 'See Also'," from the gaps sentence (keep "stale formats").
  - **Step 2C 2.2 example (line ~457 and proposed-fix line ~463):** delete the "⚠️ Docs pages … missing prev/next navigation — will add" line (line 457 only; line 458 `api.md is missing` stays) and the "Add prev/next navigation to all doc pages …" proposed-fix line; renumber the remaining proposed-fix list.
  - **Step 4 "Keep fully active in 3D" (line ~515):** remove "navigation checks," from the list (apply together with the Task 1 Principle 7→6 renumber on this same line — see Task 1 collision note).
  Do not touch the HTML `{nav_links}` / nav-bar references in Step 3 (3.2/3.3) — that is the generated HTML site nav bar, unrelated to markdown doc headers.

### Phase 2: Strip nav / See Also from the review checklist reference

- [x] **Task 3: Remove the 7 nav / See Also entries in REVIEW-CHECKLISTS.md** (depends on Task 2)
  Files: `src/skills/aif-docs/references/REVIEW-CHECKLISTS.md`
  - **Technical Checklist (lines 9–11):** delete the three items — "Each docs/ file has prev/next navigation header …", "First doc page has no '← Previous' link; last page has no 'Next →' link", and "Each docs/ file has 'See Also' section at bottom …".
  - **Readability Checklist, "Navigation and flow" (line 47):** delete the item "After finishing any docs/ page, do prev/next links and 'See Also' guide me logically forward?". Keep the `### Navigation and flow` heading (line 45) and its other two items (lines 46, 48) — they concern README flow and doc-table order, not prev/next chrome. The heading's capital-N `Navigation` is not matched by Task 5's case-sensitive grep.
  - **Standards Compliance table (lines 61–63):** delete three rows — "No prev/next navigation" (line 61), "No 'See Also' section" (line 62), and "Old 'Back to README' format" (line 63). Line 63 must go too: Task 2 removes the `[Back to README]` backlink from the doc template entirely, so a compliance rule policing its format would be a self-contradictory leftover. ("Back to README" contains none of Task 5's grep terms, so this row would otherwise survive verification silently.)
  - **Sample output (line 81):** delete the "✅ All pages have navigation" line.

### Phase 3: Update upstream sync policy

- [x] **Task 4: Reclassify aif-docs as never-overwrite in CLAUDE.md** (depends on Task 3)
  Files: `CLAUDE.md`
  In the `## Upstream Sync` section:
  - Append `` `aif-docs` `` to the "Custom skills — never overwrite from upstream" bullet list (line ~104).
  - Remove the `aif-docs` line from the "Intentionally diverged from upstream — review diff before updating" list (line ~112).
  Result: `aif-docs` appears only in the never-overwrite list.

### Phase 4: Verify

- [x] **Task 5: Confirm zero residual matches** (depends on Tasks 2, 3, 4)
  Files: (verification only)
  From `src/skills/aif-docs/` run `grep -n "nav\|See Also\|prev/next" SKILL.md references/REVIEW-CHECKLISTS.md` — expect zero matches except the unrelated HTML nav-bar references in Step 3 of SKILL.md (`{nav_links}`, "generate nav bar"), which are intentionally retained. Keep the grep case-sensitive as written: `### Navigation and flow` (REVIEW-CHECKLISTS.md line 45) has a capital N and is an intentional survivor — a case-sensitive grep does not match it; do not add `-i`. From the repo root run `grep "aif-docs" CLAUDE.md` — expect `aif-docs` only on the "Custom skills — never overwrite" line. If any unexpected match remains, return to the relevant task and remove it.
