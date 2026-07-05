# Plan Review — Roadmap family: two-level phase grammar

**Plan:** `.ai-factory/plans/52-roadmap-family-two-level-phase-grammar-outline-emits-phase-n-headers-decompose-skeleton-emit-n-m-tasks.md`
**Governing spec:** `.ai-factory/specs/06-roadmap-family-two-level-grammar.md`
**Roadmap line:** ROADMAP.md:115
**Files Reviewed:** plan + 5 target skill bodies (roadmap-engine, -outline, -decompose, -decompose-skeleton, -prune) + spec + roadmap contract line
**Risk Level:** 🟢 Low

## Context Gates

- **Roadmap linkage** — OK. Plan heading matches ROADMAP.md:115 verbatim; the contract line's `Spec:` tag resolves to `.ai-factory/specs/06-roadmap-family-two-level-grammar.md`, which exists and is the tree this plan is judged against.
- **Architecture / composition rule (`CLAUDE.md` → mechanism vs policy)** — OK. The plan keeps the engine caller-agnostic (mechanism = the render format/numbering), pushes "who emits which level" into the callers' hooks (policy). Verified `roadmap-engine` has exactly three loaders (`grep -l`): outline, decompose, skeleton — matching the spec's "engine callers are the contract" guard. All three hooks are touched (Tasks 3–5), so no caller is left incoherent. `roadmap-test-coverage` does **not** load the engine, so the format change cannot regress it (and `ROADMAP_TESTS.md` stays flat via the fallback).
- **Line-reference accuracy** — OK. Every `lines ~N–M` claim in the plan matches the current files:
  - engine format section 44–56 ✓, contract-line rules 58–65 ✓, draft step 132–135 ✓, finalize 149–153 ✓
  - outline hook (a) 20–41 ✓, spec-note clause 33–40 ✓, Critical Rules 57–64 ✓
  - decompose hook (a) 26–38 ✓, hook (d) 60–72 ✓
  - skeleton disposition 128–134 ✓
  - prune Step 6 216–225 ✓; the "never copy a phase/section header as a feature name" rule at line 101 exists and the plan correctly leaves it untouched; the retain-last-phase-header rule at 222–224 exists and the plan correctly requires coexistence.
- **RULES.md / ROADMAP_TESTS.md** — no `.ai-factory/RULES.md` present; not applicable. Settings (Testing: no, Docs: no) are correct — this is skill-body prose only, no runtime surface.

## Critical Issues

**1. Task 2 freezes the create-mode finalize step byte-identical, leaving it contradicting decision 6 for outline's phase entries.** (`src/skills/roadmap-engine/SKILL.md`:149–153, via Task 2)

Decision 8 loosens only the **draft** step so it no longer hard-mandates two-tier. Task 2 faithfully implements that narrow scope — "the finalize step that swaps placeholders for real tags stays byte-identical." But the finalize step reads:

> "write **each confirmed entry's** spec note, then replace its `Spec: <note pending>` placeholder with the real `Spec:` tag …"

This is unconditional. When outline runs the engine's create mode under the new grammar, its confirmed entries are **phases** — which by decision 6 have no spec note and no `Spec:` tag, and by the loosened draft step carry no `<note pending>` placeholder. An implementing agent reading the frozen finalize step will still be told to "write each confirmed entry's spec note," which is exactly the "force two-tier mechanics on outline" failure decision 8 set out to prevent — it just moved from the draft step to the finalize step.

The draft-step loosening alone does not neutralize this, because the conditional ("placeholder mechanics apply only when the shape is two-tier") lives in a different sentence than finalize. Since this is inside Task 2's own file boundary, it is fixable within the milestone: Task 2 should extend the loosening so the finalize step's note-write + placeholder-swap is explicitly gated on the two-tier shape (e.g. "for each confirmed **two-tier** entry, write its note and swap the placeholder; entries whose shape carries no placeholder need neither"). This keeps outline's phases from tripping the note-writing instruction while leaving decompose/skeleton (genuinely two-tier) unaffected.

## Positive Notes

- The plan is an unusually faithful, decision-by-decision projection of the spec — each task cites the exact decision block it implements, and the guards (caller-agnostic engine, no skill names in the format section, prose-not-bullets output register, ≤500 lines, flat fallback) are carried into every task's guard clause.
- The flat-fallback is stated in the right places (Task 4 for decompose, Task 5 for skeleton) and explicitly names `ROADMAP_TESTS.md`, legacy roadmaps, and this repo's own ROADMAP.md — the lazy-migration invariant is preserved.
- Task 6 pre-empts the real hazard in prune — the interaction between the new emptied-phase sweep and the existing retain-last-phase-header rule — and correctly forbids renumbering (gaps are historic).
- The sub-numbering rule (impl becomes last child `N.M.k`, no cascade renumber) is consistently stated in the engine (Task 1c), decompose split (Task 4d), and skeleton (Task 5), so all three consumers agree.
- Commit split (engine first, then the four callers) respects the Task 1 dependency and the mechanism-before-policy layering.

## Deferred observations

- Affects: `src/skills/roadmap-prune/SKILL.md` (a future prune-language reconciliation, outside this milestone's grammar-emission scope) — Step 6 still refers to the section it prunes as `## Milestones` (lines 218, 222), but new-grammar roadmaps use `## <Direction name>` section headers, not a literal `## Milestones` block. This milestone's deliverable is the *emission* of the two-level grammar; the spec (decision 5 / file-section 5) deliberately scopes prune's change to the single emptied-phase-header sweep rule and nothing else, so reconciling prune's section-name vocabulary against the new direction-header shape belongs to a separate pass, not this task's boundary. Worth a follow-up so prune's Step 6 language matches the grammar it is now expected to prune. [promoted → .ai-factory/specs/08-prune-direction-section-vocabulary.md]
