# Code Review — aif-docs: write the ТЗ, stop refusing docs-ahead-of-code

**Plan:** `.ai-factory/plans/56-aif-docs-write-the-stop-refusing-docs-ahead-of-code.md`
**Spec:** `.ai-factory/specs/10-aif-docs-rewrite-tz.md`
**Changed files:** `src/skills/aif-docs/SKILL.md`, `references/REVIEW-CHECKLISTS.md`, `references/topic-guides.md`

## Scope

This is a prose/skill (markdown) change — agent runtime instructions, no executable code, no migrations, no types, no runtime surface. "Correctness" here means: the deletion is complete and leaves no dangling reference; the reframe is internally consistent; and no spec guard is violated (chiefly the "no lead/lag meta-commentary" guard, whose reintroduction would re-create the `3d` mode this milestone deletes).

## Verification performed

- **Full read** of all three changed files against the diff, not just the hunks.
- **Spec greps**, run from `src/skills/aif-docs/`:
  - `grep -rin "3d\|3д\|MODE = 3D\|Document-Driven" SKILL.md references/` → **zero**.
  - `grep -rin "see also\|next steps\|where to go next\|prev/next" SKILL.md references/` → **zero**.
  - `grep -rin "all modes\|every mode\|MODE = normal\|MODE = " SKILL.md references/` → **zero** (orphaned-mode sweep from plan Task 6).
- **Dangling-reference sweep across the repo**: the only `3d`/`Document-Driven`/`conform to` hits outside this skill are unrelated `ui-ux-pro-max` design data ("3D & Hyperrealism", CSS) — false positives, nothing to do with the deleted mode. The two live consumers of `aif-docs` (`docs/workflow.md`, `aif-plan/SKILL.md`) reference it generically (`/aif-docs`, pipeline position) and never named the `3d` flag or the `argument-hint` — so removing them breaks no caller.
- **Cross-reference integrity**: SKILL.md refers to `REVIEW-CHECKLISTS.md` by checklist name ("Technical Accuracy", "Readability & Completeness"), not by the renamed `### Cross-links` subsection, so the section rename introduces no broken pointer. `consolidation.md` and `html-generation.md` references are untouched and still resolve.

## Spec conformance (each Change item landed)

1. **`3d`/`3д` deleted wholesale.** `argument-hint` is `"[--web]"`; Step 0.1 parses only `--web`; the "Document-Driven Development (3D mode)" section, the `MODE detection` block, the `MODE = 3D`/`MODE = normal` Step 1 branch, the Step 2.1 staleness carve-out, the Step 4 carve-out, the conform-pointer, and all three `REVIEW-CHECKLISTS.md` `MODE = 3D` parentheticals are gone. One mode remains.
2. **The one mode writes the ТЗ code-or-no-code.** Step 1 now determines *the subject* (behavior + invariants), reads code where it exists (treats it as referent), treats the doc as contract where it doesn't — matching spec item 2's authorized phrasing. Referent-dependent checks are **per-item conditional**, not a mode: Step 2.1 stale-content, the Step 4 "Referent-conditional Technical Accuracy checks" block, and `REVIEW-CHECKLISTS.md:11-12`. Readability, README length, and the no-motivation pass are stated as running unconditionally.
3. **Feature-cross-link tree replaces linear nav.** `REVIEW-CHECKLISTS.md`'s "Navigation and flow" → "Cross-links" (relative-path feature-tree edges; ARCHITECTURE.md module→topic-doc links marked **check-only**, honoring the read-only stance); `topic-guides.md` "Next steps links" removed. No See Also / prev-next / next-steps residue survives.
4. **Terse; one home per fact.** Principle 3 rewritten to the role split (structure→ARCHITECTURE.md, behavior→topic docs, index→CLAUDE.md, onboarding→README+relatives; a duplicated fact becomes a link) and points at the existing CLAUDE.md index. The coordination-trio staleness check is wired into the Step 2.1 State C audit with the explicit "check ARCHITECTURE.md for staleness, do not edit it" clause.

## Guards honored

- **No lead/lag meta-commentary** (the spec's strongest guard). Step 1's new wording gives a single present-tense instruction with a conditional content-source ("read the code where it exists… treat the doc as the contract where it doesn't… write it in present tense as if it already ships") — the exact reframe spec item 2 authorizes. It does not editorialize the docs-lead/code-follows temporal duality or invoke the "docs analogue of TDD" framing that the deleted `3d` section carried. Guard intact.
- **No fork this pass.** README/onboarding genre (Step 2 State A), the A/B/C state machine, `--web`/HTML (Step 3), and the review checklists all remain.
- **Principle 6 cited by name** and its "every run, every mode, no exceptions" clause trimmed to "every run, no exceptions" now that no mode distinction exists.
- **Frontmatter trigger phrases intact** ("create docs", "write documentation", "update docs", "generate readme", "document project") — auto-selection unchanged; only the descriptive clause was reframed ТЗ-first.
- `upstream/ai-factory/` and `aif-architecture` untouched.

## Findings

None. The deletion is complete, the reframe is internally consistent, no caller or cross-reference is left dangling, and no spec guard is violated.

REVIEW_PASS
