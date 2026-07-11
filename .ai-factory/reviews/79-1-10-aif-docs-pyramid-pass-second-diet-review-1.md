# Code Review — 1.10 aif-docs: pyramid pass (second diet)

**Scope:** `src/skills/aif-docs/SKILL.md` + three new `references/` files, plus the accompanying planning-artifact edits (ROADMAP 1.10 line, specs 30/31/32).

**Verdict:** No findings. The change is a behavior-identical progressive-disclosure diet, verified byte-for-byte against `HEAD`.

## What the change does
- Moves the three per-state procedures out of `SKILL.md` into new reference files:
  - `references/generate-state-a.md` (State A: 2.1 topic dialog, 2.2 README template, 2.3 doc-file gen)
  - `references/split-state-b.md` (State B: 2.1 analyze, 2.2 split-proposal dialog, 2.3 execute)
  - `references/audit-state-c.md` (State C: 2.1 audit checks, 2.1.1 standards, 2.2 audit-results dialog)
- Lifts former subsection **2.2b** into a first-class body section `### Update the CLAUDE.md Documentation Index`, positioned before the State A/B/C pointers (single home reached by State A and State B).
- Replaces each removed procedure with a one-line `→ read references/<file>` pointer in the established style.

## Verification performed (against `git show HEAD:.../SKILL.md`)
- **Byte-identical moves — confirmed by `diff`:**
  - State A 2.1+2.2 blocks vs HEAD 134–222 → identical; 2.3 body vs HEAD 242–251 → identical.
  - State B 2.1+2.2 blocks vs HEAD 259–300 → identical.
  - State C 2.1 block vs HEAD 313–323 → identical; 2.2 audit-results block vs HEAD 331–347 → identical.
  - Lifted CLAUDE.md-index section body vs HEAD 2.2b content (226–240) → identical.
- **Every `AskUserQuestion` dialog preserved byte-identical:** the State A topic-selection dialog (moved), the State B split-proposal block (moved), the State C audit-results block (moved); the State-C-`--web` routing dialog, the Step 1.1 consolidation dialog, and the Step 4.1 cleanup dialog all remain untouched in the body.
- **Genre sentence at `:19` and Core Principles 1–6 (incl. state-not-process):** unchanged — outside the diff hunks.
- **Documented deviations, each correct and grep-scoped:**
  - `generate-state-a.md:106` — `references/topic-guides.md` → sibling `topic-guides.md` (target exists beside it).
  - `audit-state-c.md:17` — `references/REVIEW-CHECKLISTS.md` → sibling `REVIEW-CHECKLISTS.md` (target exists beside it).
  - State A 2.2b slot and State B 2.3 both re-pointed to the body's "Update the CLAUDE.md Documentation Index" section (exact header match).
  - Step 5 (`SKILL.md:251`) `(Step 2.2b)` re-pointed to `(see "Update the CLAUDE.md Documentation Index")` — the one allowed Step 5 edit.
- **No dangling labels:** `grep '2.2b'` over the skill dir → none. State-C-internal refs `(see 2.1.1)` and `(Step 2.2)` travel together into `audit-state-c.md`, staying coherent.
- **Routing resolves:** the State-C-`--web` branches ("Generate HTML only" → Step 3 → `html-generation.md`; "Audit & improve"/"Audit only" → Step 2 State C → `audit-state-c.md`) all land on existing references.
- **Line count:** body is 271 lines — materially under the 300-line gate; no content lost (every removed line reappears byte-identical in a reference or the lifted body section).

## Sequencing note (not a defect)
Inside State A, the CLAUDE.md-index update keeps its original position between README generation (2.2) and doc-file generation (2.3) — `generate-state-a.md:93` inserts the pointer exactly where 2.2b sat — so run order is preserved. The lifted section sitting before the State pointers in the body is the plan-approved placement ("adjacent to the state-routing flow so its first-class status is visible").

## Planning artifacts
ROADMAP 1.10 line and specs 30/31/32 add the shared "Re-basing rule" (the one documented exception to byte-identical) consistently across the sibling pyramid-pass milestones. The 1.10 checkbox correctly remains `[ ]`. No correctness concerns.

REVIEW_PASS
