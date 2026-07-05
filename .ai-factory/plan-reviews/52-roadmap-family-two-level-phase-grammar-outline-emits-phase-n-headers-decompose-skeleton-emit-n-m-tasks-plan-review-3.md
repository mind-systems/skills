# Plan Review 3 — Roadmap family: two-level phase grammar

**Plan:** `.ai-factory/plans/52-roadmap-family-two-level-phase-grammar-outline-emits-phase-n-headers-decompose-skeleton-emit-n-m-tasks.md`
**Governing spec:** `.ai-factory/specs/06-roadmap-family-two-level-grammar.md`
**Roadmap line:** ROADMAP.md:115
**Files Reviewed:** plan + 5 target skill bodies (roadmap-engine, -outline, -decompose, -decompose-skeleton, -prune) + spec + roadmap contract line + plan-review-1 + plan-review-2
**Risk Level:** 🟢 Low

## Context Gates

- **Roadmap linkage** — OK. The plan's `# Plan:` heading matches ROADMAP.md:115 verbatim; the contract line's `Spec:` tag resolves to `.ai-factory/specs/06-roadmap-family-two-level-grammar.md`, which exists and is the tree this plan is judged against.
- **Composition rule (`CLAUDE.md` → mechanism vs policy)** — OK. Engine stays caller-agnostic (render format + numbering = mechanism); "who emits which level" lives in the callers' hooks (Tasks 3–5). Confirmed by `grep -l "roadmap-engine"` that the engine has exactly three loaders — outline, decompose, skeleton — and all three hooks are touched, so no caller is left incoherent. `roadmap-test-coverage` does not load the engine, so the format change cannot regress it, and `ROADMAP_TESTS.md` stays flat via the fallback.
- **Round-1 critical issue (finalize step)** — RESOLVED. Plan-review-1 flagged that Task 2 froze the create-mode finalize step (engine 149–153) byte-identical, forcing note mechanics on outline's phases. Task 2 item 2 now explicitly gates the note-write + placeholder-swap on the two-tier shape. Correct.
- **Round-2 critical issue (update-mode Add action)** — RESOLVED. Plan-review-2 flagged the update-mode "Add" action (engine 177–179) carrying the identical unconditional two-tier mandate — the dominant outline call (adding phases to an existing ROADMAP.md). Task 2 item 3 now loosens the Add action's "produce its two-tier artifacts" to hook (a)'s shape, and correctly leaves Rewrite (inherits the create-mode fix) and Reprioritize (reorder only) untouched. Correct.
- **Round-2 issue (stale `check` in argument-hint)** — RESOLVED. Task 3 now drops the `check` token from outline's `argument-hint` (line 4 → `"[project vision or requirements]"`), and notes decompose keeps its own `check`. Correct.
- **Line-reference accuracy** — OK. Re-verified every `lines ~N–M` claim against the current files:
  - engine format section 44–56 ✓, contract-line rules 58–65 ✓, draft step 132–136 ✓, finalize 149–153 ✓, update-mode Add 177–179 ✓
  - outline `argument-hint` line 4 ✓, hook (a) 20–41 ✓, spec-note clause 35–40 ✓, "milestones later serve as phase names" line 24 ✓, `[x]`-first-run carry-over line 28 ✓, gather-input question 29–31 ✓, Critical Rules 57–64 ✓
  - decompose hook (a) 26–38 ✓, hook (d) "Decompose existing" 60–72 ✓
  - skeleton "Disposition of the original task" 128–134 ✓
  - prune Step 6 216–224 ✓, retain-last-phase-header rule 222–224 ✓, "Never copy a phase or section header as a feature name" at line 101 ✓ (plan correctly leaves it untouched)
- **Note-forcing-spot completeness** — OK. Walked the engine's whole flow for every point that forces note/placeholder mechanics: draft (132–134, item 1), finalize (149–153, item 2), update-mode Add (177–179, item 3). Review progress (marks `[x]`, no note), Reprioritize (reorder), Rewrite (inherits the create fix), Check mode (marks `[x]`, no note) do not write notes. All three unconditional two-tier mandates are now covered — no fourth spot remains.
- **RULES.md** — no `.ai-factory/RULES.md` present; not applicable. Settings (Testing: no, Logging: minimal, Docs: no) are correct — this is skill-body prose only, no runtime surface. `≤500 lines` guards satisfiable (engine is 246 lines today).

## Critical Issues

None. Both prior-round critical issues (finalize step, update-mode Add action) and the round-2 argument-hint issue are resolved within Task 2 and Task 3's own file boundaries, with the genuinely two-tier callers (decompose/skeleton) left unaffected.

## Positive Notes

- The plan is a faithful, decision-by-decision projection of the spec; each task cites the decision block it implements, and every guard (caller-agnostic engine, no skill names in the format section, prose-not-bullets output register, ≤500 lines, flat fallback) is carried into the task guards.
- Task 2 now enumerates all three unconditional two-tier mandates (draft, finalize, Add) and explicitly reasons about why Rewrite and Reprioritize need no change — the "two-tier applies only when the shape is two-tier" conditioning is stated once and applied consistently at each site.
- The sub-numbering rule (impl becomes last child `N.M.k`, no cascade renumber) is stated consistently in the engine (Task 1c), decompose split (Task 4d), and skeleton (Task 5) — all three consumers agree.
- Flat fallback is stated where it matters (Task 4 decompose, Task 5 skeleton) and explicitly names `ROADMAP_TESTS.md`, legacy roadmaps, and this repo's own ROADMAP.md — the lazy-migration invariant holds.
- Task 6 pre-empts the real prune hazard — the interaction between the emptied-phase sweep and the existing retain-last-phase-header rule — and correctly forbids renumbering (gaps are historic).
- Commit split (engine first, then the four callers) respects the Task 1 dependency and the mechanism-before-policy layering.

## Deferred observations

- Affects: `src/skills/roadmap-prune/SKILL.md` Step 6 (218, 222) — prune still names the section it prunes `## Milestones`, but new-grammar roadmaps use `## <Direction name>` direction headers. Spec decision 5 (and file-section 5) deliberately scopes prune's change in this milestone to the single emptied-phase-header sweep rule and nothing else, so reconciling prune's section-name vocabulary against the direction-header shape belongs to a separate pass. Note that `## Milestones` remains correct for flat roadmaps (including this repo's own), so this is a widening-of-coverage follow-up, not a regression. Carried from plan-reviews 1 and 2; still outside this milestone's boundary. [promoted → .ai-factory/specs/08-prune-direction-section-vocabulary.md]
- Affects: `src/skills/roadmap-engine/SKILL.md` update-mode "Review progress" action (174–176) and Check mode (196–235) — both mark `[ ]` entries `[x]`, which at the phase tier has nothing to mark; phase-tier progress is deliberately delegated to the `N.M` task checkboxes (decompose/prune territory) that coexist in the same file. Decision 7 consciously drops check *mode* for outline while keeping the update-mode flow; whether outline's retained "Review progress" (and an explicit `/roadmap-outline check`, which the engine's mode-determination still routes to Check mode) should scan the shared `N.M` checkboxes or defer entirely is a flow-semantics question the spec did not open. Outside this milestone's grammar-*emission* scope; worth a follow-up once the grammar is live. Carried from plan-review-2. [promoted → .ai-factory/specs/07-engine-shape-condition-checkbox-flows.md]
- Affects: `src/skills/roadmap-engine/SKILL.md` "## The two-tier artifact" section (27) — the categorical line "Each milestone is a two-tier entry" becomes slightly overreaching once decision 8's create-mode loosening makes non-two-tier phase entries legal. The loosened flow ("two-tier mechanics apply only when the shape is two-tier") is the authoritative reconciliation and this section remains an accurate description of the two-tier *shape* the task tier uses, so it is coherent as-is; the spec's engine file-section 1 deliberately scoped the engine edits to the format section, numbering rules, and create-mode loosening only. A one-line softening of this sentence would be a tidy follow-up but is neither introduced as a defect by this diff nor required by the spec. [promoted → .ai-factory/specs/07-engine-shape-condition-checkbox-flows.md]

PLAN_REVIEW_PASS
