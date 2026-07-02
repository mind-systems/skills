# Review: remove stale `/aif-plan`, `/aif-implement`, `/decompose` references

## Scope
Code changes in `git diff HEAD`:
- `src/skills/roadmap-outline/SKILL.md` (2 edits)
- `src/skills/roadmap-decompose/SKILL.md` (3 edits)

(New plan/plan-review/json artifacts under `.ai-factory/` are process files, not code — no review needed.)

## Verification against plan & spec

**roadmap-outline** — both spots fixed:
- Line 79 (Critical Rule 1): `(that's /aif-plan)` → `(that's /roadmap-decompose)`. Granular tasks correctly point at decompose's tier. ✓
- Line 229 (Critical Rule 5): rephrased to "NO implementation — this skill only plans; implementation is the orchestrator's job (a separate run)". ✓

**roadmap-decompose** — all three spots fixed:
- Line 236 (Mode 3 heading): `(/decompose check)` → `(/roadmap-decompose check)`. ✓
- Line 240 (Mode 3 body): "run `/decompose` first" → "run `/roadmap-decompose` first". ✓
- Line 291 (Critical Rule 5): same rephrase applied, identical wording to outline. ✓

## Correctness checks
- **Leftover-reference grep** on both files for `aif-plan`, `aif-implement`, and bare `/decompose\b`: **no matches**. The cleanup is complete; nothing was missed.
- **Surrounding context** of each edit reads coherently (verified Mode 3 heading + body and both Critical Rule 5 lines). No dangling references, no broken markdown, no orphaned mentions.
- **No logic changes**: edits are pure wording; modes, gates, numbering, and structure are untouched — matches the "reference cleanup only" constraint.
- **`upstream/ai-factory/` untouched**: diff is confined to `src/skills/`. ✓
- **Cross-file consistency**: the two Critical Rule 5 lines now use identical phrasing, as the spec intended.

## Runtime concerns
None applicable — these are skill instruction files (markdown), not executable code. No migrations, types, or race conditions in scope. The replacement targets (`/roadmap-decompose`, "the orchestrator") are real and current per `docs/workflow.md`.

## Findings
None.

REVIEW_PASS
