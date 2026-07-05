# Code Review — Roadmap family: two-level phase grammar

**Plan:** `.ai-factory/plans/52-roadmap-family-two-level-phase-grammar-outline-emits-phase-n-headers-decompose-skeleton-emit-n-m-tasks.md`
**Governing spec:** `.ai-factory/specs/06-roadmap-family-two-level-grammar.md`
**Files reviewed (in full):** `roadmap-engine`, `roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-prune` SKILL.md — plus repo-wide grep for stale cross-references.
**Nature of the change:** skill-instruction prose only. No runtime code, so "correctness" here means internal contradiction, broken cross-reference, spec divergence, or an instruction that would make an implementing agent emit the wrong artifact shape.

## What was verified

**Spec verification greps (from spec §"How to verify") all pass:**
1. `roadmap-engine` format section shows `### Phase N` (line 55); the stale flat `## Milestones` example is gone (no occurrence remains in the file).
2. `roadmap-outline` hook (a) forbids checkboxes/`Spec:` at the phase tier; the "optional at this tier" clause is fully removed.
3. `N.M` numbering + sub-numbering present in both `roadmap-decompose` (hook a + hook d split) and `roadmap-decompose-skeleton` (disposition).
4. `roadmap-prune` emptied-phase sweep rule present (Step 6).

**Cross-file coherence:**
- Sub-numbering rule (children `N.M.1…N.M.k`, original impl → last child `N.M.k`, no cascade renumber) is stated identically in the engine (numbering rules), decompose hook (d), and skeleton disposition — all three consumers agree.
- Flat fallback stated in decompose (a) and skeleton, naming `ROADMAP_TESTS.md`/legacy/this-repo roadmaps; the engine holds the canonical fallback rule. `roadmap-test-coverage` does not load the engine, so the format change cannot regress it.
- The round-1 and round-2 plan-review findings are both correctly implemented in the diff: the engine's create-mode **draft** (152–160), **finalize** (172–182), *and* update-mode **Add** (201–208) all loosen the two-tier/placeholder mandate to be shape-conditional. Outline's `argument-hint` drops the now-stale `check` token (line 4). Outline's `[x]`-on-first-run carry-over is removed; the gather-input question is kept.

**No dangling references:** repo-wide grep finds no doc/command referencing outline's dropped check mode, and no doc reproducing the old flat `## Milestones` engine format that the diff would leave stale.

**Guards honored:** engine stays caller-agnostic (no skill names added to the format/numbering section); direction preamble and phase intro rendered as prose, not bullets, in the example; every file ≤500 lines (engine 274, outline 71, decompose 91, skeleton 157, prune 305); engine reverse-graph marker and load-once framing untouched. No project roadmap edited (lazy migration preserved).

## Deferred observations

- Affects: `src/skills/roadmap-engine/SKILL.md` §"The two-tier artifact" (line 27) — the section still opens with the universal claim *"Each milestone is a two-tier entry: a contract line … plus a full spec note"*, which is no longer true for outline's phase entries (no contract line, no note). This is **not a live bug**: (a) the spec deliberately scoped the engine change to the format section, numbering rules, and the create/add flow steps — it did not open this reference section; (b) the caller's hook (a) is authoritative under the composition model and outline explicitly overrides it ("never a contract line, no `Spec:` tag"); (c) the engine's actual *flow* steps (draft/finalize/Add) were all correctly made shape-conditional, which is where an agent acts. The wording is an overbroad description in a context section, not an instruction that produces a wrong artifact. Worth a one-sentence softening ("a two-tier entry is a contract line plus a note; some callers emit non-two-tier entries per their hook") in a future engine-language pass, alongside the two prune/outline reconciliations already deferred from plan-review-2 (prune's `## Milestones` vocabulary; outline's retained "Review progress" action at the phase tier).

No blocking findings — the diff is a faithful, internally consistent projection of the spec, and both prior plan-review findings are implemented.

REVIEW_PASS
