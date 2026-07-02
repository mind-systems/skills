# Code Review: aif-docs diet to ≤500 — rare branches to `references/`, drop the aif-evolve block

**Scope reviewed:** `src/skills/aif-docs/SKILL.md` and the three new `references/*.md` files. Plan/plan-review/JSON artifacts are metadata, not runtime code — noted but not scrutinized for behavior.

## What the change does
- Deletes the Step 0 skill-context / aif-evolve block (~21 lines).
- Extracts three rare-branch sections into new self-contained references, leaving a rule + when-to-read pointer in the body:
  - `references/topic-guides.md` (Step 2.3 per-topic content guidelines)
  - `references/html-generation.md` (Step 3.1–3.4 HTML mechanics)
  - `references/consolidation.md` (Step 1.1 table, stays-in-root list, sample dialog)

## Verification performed
- **Line count:** `wc -l` = 486 lines, under the ≤500 norm (target ~450 approximately met). ✓
- **Verbatim preservation:** diffed each extracted block against `git HEAD`.
  - Consolidation table + stays-in-root list: **byte-identical**. ✓
  - Topic guidelines: bullet content **byte-identical**; only the old inline heading `**Content guidelines per topic:**` and surrounding blank lines dropped, replaced by the reference's own `# Content Guidelines Per Topic` title. Expected, correct. ✓
  - HTML 3.1–3.4: reproduced **verbatim** in the reference. ✓
- **Dead-machinery removal:** no `skill-context` or `aif-evolve` mentions remain anywhere under `src/skills/aif-docs/`. Step 0 paragraph flow is clean — "Check for existing README…" → "Scan for scattered markdown files…" with no dangling blank lines. ✓
- **Contract text intact:** all AskUserQuestion dialogs (Step 1 State-C-with-web, Step 1.1 consolidation options, Step 2.1 topic selection, Step 4.1 cleanup) remain verbatim in the body. Core Principles, 3D mode, Step 4, Step 4.1, Step 5, Artifact Ownership, Important Rules untouched. ✓
- **Task 48 preserved:** CLAUDE.md documentation-index edits (Principle 3, Step 2.2b, State C legacy-README-table check) all still present and unmodified. ✓
- **No dangling cross-references:** the only external mention of aif-docs is `src/skills/aif-plan/SKILL.md:66` (`/aif-docs` invocation), which does not depend on any removed step anchor. ✓
- **Isolation:** `active/skills/aif-docs` symlinks into `src/`, so the edited file is the live one; `upstream/ai-factory/` mirror is untouched. ✓
- **Relative paths:** all three body pointers use skill-relative `references/*.md` paths, matching the existing `references/REVIEW-CHECKLISTS.md` convention. ✓

## Findings
No correctness, security, or behavior-divergence defects. The moved content is verbatim, all decision branches remain reachable, and every extraction leaves a rule + when-to-read pointer in the body so no branch loses information it needs.

## Non-blocking observations (no action required)
- **File-mapping line duplicated.** `File mapping: README.md → index.html, <resolved docs dir>/*.md → *.html.` now appears in both the body (SKILL.md:385) and `references/html-generation.md:20`. This is a harmless consequence of moving Step 3.3 verbatim while the plan also asked to keep the one-liner in the body. It is an instruction, not state that can drift into contradiction, so it does not affect behavior. Leaving it in the reference actually helps that file stay self-contained. Optional to dedupe; not a defect.
- The consolidation pointer ("Consolidation targets and the sample proposal dialog → read `references/consolidation.md`.") states its *what* but leans on Step 1.1's surrounding context for the *when* (scattered files found), a touch weaker than the `--web`/State-A pointers that name their trigger explicitly. Behavior is unaffected. Optional polish.

Both observations are cosmetic. The change meets its byte-identical-behavior contract. The plan's Task 5 still requires a live State C run to confirm interaction shape end-to-end; that runtime check is outside a static diff review's reach and remains the author's to perform.

REVIEW_PASS
