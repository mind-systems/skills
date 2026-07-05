# Plan Review 2 — Roadmap family: two-level phase grammar

**Plan:** `.ai-factory/plans/52-roadmap-family-two-level-phase-grammar-outline-emits-phase-n-headers-decompose-skeleton-emit-n-m-tasks.md`
**Governing spec:** `.ai-factory/specs/06-roadmap-family-two-level-grammar.md`
**Roadmap line:** ROADMAP.md:115
**Files Reviewed:** plan + 5 target skill bodies (roadmap-engine, -outline, -decompose, -decompose-skeleton, -prune) + spec + roadmap contract line + plan-review-1
**Risk Level:** 🟡 Medium

## Context Gates

- **Roadmap linkage** — OK. Plan `# Plan:` heading matches ROADMAP.md:115 verbatim; the contract line's `Spec:` tag resolves to `.ai-factory/specs/06-roadmap-family-two-level-grammar.md`, which exists and is the tree this plan is judged against.
- **Round-1 critical issue** — RESOLVED. Plan-review-1 flagged that Task 2 froze the create-mode finalize step (engine 149–153) byte-identical, leaving its unconditional "write each confirmed entry's spec note … replace its `Spec: <note pending>` placeholder" wording to force note mechanics on outline's phases (decision 6/8). Task 2 now explicitly loosens **both** the draft step (item 1) and the finalize step (item 2), gating the note-write + placeholder-swap on the two-tier shape. Correct.
- **Composition rule (`CLAUDE.md` → mechanism vs policy)** — OK. Engine stays caller-agnostic (render format + numbering = mechanism); "who emits which level" lives in the callers' hooks (Tasks 3–5). Confirmed by grep that `roadmap-engine` has exactly three loaders — outline, decompose, skeleton — and all three hooks are touched, so no caller is left incoherent. `roadmap-test-coverage` does not load the engine; the format change cannot regress it, and `ROADMAP_TESTS.md` stays flat via the fallback.
- **Line-reference accuracy** — OK. All `lines ~N–M` claims verify against the current files: engine format 44–56 ✓, contract-line rules 58–65 ✓, draft step 132–136 ✓, finalize 149–153 ✓; outline hook (a) 20–41 ✓, spec-note clause 33–40 ✓, Critical Rules 57–64 ✓; decompose hook (a) 26–38 ✓, hook (d) 60–72 ✓; skeleton disposition 128–134 ✓; prune Step 6 216–225 ✓ with the retain-last-phase-header rule at 222–224 ✓.
- **RULES.md / ROADMAP_TESTS.md** — no `.ai-factory/RULES.md` present. Settings (Testing: no, Docs: no) correct — skill-body prose only, no runtime surface. `≤500 lines` guards satisfiable (engine is 246 lines today).

## Critical Issues

**1. Task 2 loosens only the *create-mode* two-tier mandate; the *update-mode* "Add" action (engine 177–179) carries the identical unconditional two-tier wording and will trip outline the same way — this is the round-1 finding repeated in a different mode.** (`src/skills/roadmap-engine/SKILL.md`:177–179, via Task 2)

Decision 8 and Task 2 loosen the create-mode draft/finalize steps so an outline **phase** (no note, no `Spec:` tag, no placeholder) doesn't trip note-writing. But outline keeps the engine's full maintenance flow including **update mode** (spec decision 7 says so explicitly; outline hook (d) registers the built-in menu — "review progress / add / reprioritize / rewrite"). The update-mode **Add** action reads:

> "**Add:** explore the codebase for each new entry, **produce its two-tier artifacts per the format above** …, and insert each in logical order among existing entries."

This is unconditional two-tier, exactly parallel to the create-mode draft step. The dominant real-world outline call is **adding phases to an existing ROADMAP.md** — which routes to update mode → Add. An implementing agent following Task 2's instruction "Touch only these two steps' two-tier/placeholder sentences — the rest of the flow stays byte-identical" will deliberately freeze the Add action, leaving "produce its two-tier artifacts" intact. Outline adding a phase would then be told to produce a two-tier artifact (note + `Spec:` tag) for something that decision 6 says has neither. This is the same failure decision 8 exists to prevent, one action over.

(The **Rewrite** action re-runs the create-mode draft→confirm cycle, so it inherits the fix — no separate change needed there. **Reprioritize** only reorders. Only **Add** is left contradictory.)

Fixable within Task 2's own file boundary (`roadmap-engine/SKILL.md`), same class as the round-1 finalize fix: extend Task 2 to also loosen the update-mode Add action's "produce its two-tier artifacts" phrasing to hook (a)'s shape — the two-tier/placeholder mechanics apply only when that shape is two-tier — so decompose/skeleton (genuinely two-tier) stay unaffected while outline's phase-add doesn't trip note mechanics.

## Issues

**2. Dropping check mode leaves outline's `argument-hint` advertising `check` — stale after this milestone.** (`src/skills/roadmap-outline/SKILL.md`:4, via Task 3)

Task 3 has outline "explicitly opt out — outline registers no check mode." But the frontmatter still reads `argument-hint: "[check | project vision or requirements]"`. Once check mode is gone, the hint advertises a mode the skill no longer honors — a stale artifact the milestone itself creates, in the same file Task 3 already rewrites. Task 3 should drop the `check` token from the argument-hint (decompose keeps its `check`; outline should not). Low severity, but in-scope and introduced by this diff, so it is a finding rather than a deferral.

## Positive Notes

- The plan is a faithful, decision-by-decision projection of the spec; each task cites the decision block it implements, and every guard (caller-agnostic engine, no skill names in the format section, prose-not-bullets output register, ≤500 lines, flat fallback) is carried into the task guards.
- Round-1's finalize-step gap is cleanly closed by Task 2 item 2, with the "removed/rewritten entries receive no note" and `$TARGET_FILE` write kept byte-identical.
- The sub-numbering rule (impl becomes last child `N.M.k`, no cascade renumber) is stated consistently in the engine (Task 1c), decompose split (Task 4d), and skeleton (Task 5) — all three consumers agree.
- Flat fallback is stated where it matters (Task 4 decompose, Task 5 skeleton) and explicitly names `ROADMAP_TESTS.md`, legacy roadmaps, and this repo's own ROADMAP.md.
- Task 6 pre-empts the real prune hazard — the interaction between the emptied-phase sweep and the existing retain-last-phase-header rule — and correctly forbids renumbering (gaps are historic).

## Deferred observations

- Affects: `src/skills/roadmap-engine/SKILL.md` update-mode "Review progress" action (177 / 174–176) and its Check mode — the engine's "Review progress" action and check mode both mark `[ ]` entries `[x]`, which at the phase tier has nothing to mark. Decision 7 consciously drops check *mode* while keeping the update-mode flow, and phase-tier progress is deliberately delegated to the `N.M` task checkboxes (decompose/prune territory) that physically coexist in the same file. Reconciling whether outline's retained "Review progress" action should scan the shared `N.M` checkboxes or defer entirely is a flow-semantics question the spec did not open; it sits outside this milestone's grammar-*emission* scope. Worth a follow-up once the grammar is live. [promoted → .ai-factory/specs/07-engine-shape-condition-checkbox-flows.md]
- Affects: `src/skills/roadmap-prune/SKILL.md` Step 6 (218, 222) — prune still names the section it prunes `## Milestones`, but new-grammar roadmaps use `## <Direction name>` section headers. Spec decision 5 scopes prune's change to the single emptied-phase-header sweep rule and nothing else, so reconciling prune's section-name vocabulary against the direction-header shape belongs to a separate pass. (Carried from plan-review-1; still out of this milestone's boundary.) [promoted → .ai-factory/specs/08-prune-direction-section-vocabulary.md]
