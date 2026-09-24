## Plan Review Summary

**Files Reviewed:** 1 plan, 1 target file (`src/skills/roadmap-engine/SKILL.md`), spec `155-…`, spec `154-…`, phase 56 contract lines, `src/commands/command-pin-gaps.md`, `docs/counts-go-stale.md`
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy") — OK. The edit stays inside an engine's own shared content; no boundary, no `loads:` edge, no caller contract moves. The repo's editing rule "before touching an engine, grep for its callers" is satisfied upstream: spec `155-…` records the nine-file caller sweep and the plan carries its conclusion (only `command-pin-gaps` names the paragraph, and only by heading).
- **Rules** — `.ai-factory/RULES.md` is absent in this repo (WARN, informational only; the repo's conventions live in CLAUDE.md and ARCHITECTURE.md, both checked).
- **Roadmap** — OK. The plan is task 56.2 of `.ai-factory/roadmaps/trickster77777.md`, the `[x]`/`[ ]` seam, and matches its contract line word for word in scope: third clause reworded, heading and neighbours byte-identical.
- **Governing spec** (`docs/counts-go-stale.md`, named on the phase header) — OK. Replacing an instruction that reads as "write the list" with one that reads as "state it precisely" is exactly the contract/census split the doc draws; "pinned" is the doc's own word for the keep side ("a pinned literal").

### Verified against ground truth

- `src/skills/roadmap-engine/SKILL.md` line 49 is `*what breaks on contact*, enumerated rather than hedged.` and is the file's sole `enumerat` match — the plan's claim holds.
- Every position the plan pins is accurate: heading at line 46, "Why two tiers" at 42–44, "Never write a full spec inline…" at 51–52. The paragraph wraps at ~78 columns and `pinned` is shorter, so the no-rewrap instruction is right.
- The post-change paragraph the plan specifies is character-for-character the text spec `155-…` § "The change" quotes.
- `active/skills/roadmap-engine` is a symlink to `src/skills/roadmap-engine`, so editing `src/` is the whole deployment — no second copy to keep in sync.
- No paraphrase dependent hides outside the sweep: `grep -rn "breaks on contact" src/ docs/` returns only the engine line and `command-pin-gaps.md`, and no doc restates the three-part shape.

### Issues

**1. The verify step's expected-results list is already incomplete against the sweep it runs** — `.ai-factory/plans/trickster77777/02-…md`, second task.

The step says every remaining match "is one of the four categories the spec's `## Blast radius` invariant names", then lists five things. Two problems, one of them operational:

- The sweep `grep -rln "What a task spec holds\|enumerated rather than hedged" src/ docs/ .ai-factory/` run right now returns 11 paths, and one of them is **the plan file itself** — it quotes the old wording in its `## Context` and in both task bodies. The plan file appears in no listed category. An implementer executing the step literally hits a match the plan says cannot exist, and must either read the invariant as broken (a loop) or decide on their own authority that it is fine. The plan-review and review artifacts this task will itself produce add further matches for the same reason.
- The plan attributes "the phase's prior plan-review/review artifacts" to the spec's invariant, but spec `155-…` names only four categories — the target, this task's own spec plus its contract line, the phase note `150-…`, and handoff `27-…`. 56.1's three plan-reviews and its review are the plan's own addition, presented as the spec's.

The fix is the one the phase itself is about: state the residual set as a **rule**, not as a list of hits. Something like — *every remaining match quotes the old wording as the problem it describes or as a record of a past moment (this task's spec, its contract line, the phase note, the handoff, and the run artifacts of phase 56 including this plan and its own reviews), never as a claim about the engine's present wording; the engine is the only file that had to change.* That passes counts-go-stale's own test — it still reads true after another artifact quoting the old wording lands — while the current list falsifies itself the moment one does, which it already has.

### Positive Notes

- Scope discipline is exact: one word on one line, with the untouched set spelled out down to the italic span, the comma and the trailing period, and an explicit "no other file is edited".
- The heading `**What a task spec holds:**` is correctly identified as the load-bearing name `command-pin-gaps.md` resolves against, and held byte-identical — reference by name preserved.
- The "Do not touch `command-pin-gaps.md`" paragraph is the right call, and it is argued from the two specs' file boundaries rather than from taste; it also names where the residue is already recorded instead of silently dropping it.
- Position addresses (line 49, line 36) appear only in the plan — a work-order thrown away when applied — and are each anchored to exact text, so they survive being slightly wrong.

## Deferred observations

- Affects: phase 56 / `.ai-factory/specs/trickster77777/154-the-repair-clause-writes-the-rule-and-the-sweep-not-the-tally.md` — Carried forward from 56.1's review and re-verified against the files as they stand. Once this task lands, the engine's root clause says *pinned* while `src/commands/command-pin-gaps.md` still advertises enumeration as its own product in two sentences spec `154-…` pins as untouched: line 36 ("a blast-radius hole by enumerating *what breaks on contact*"), which derives its wording from the very paragraph this task rewords, and line 38 ("it pins values and enumerates breakage"). The plan is right to leave them — both specs' file boundaries exclude them — but after 56.2 the phase closes with the derived wording contradicting the root it names, and phase 56 has no third task. This wants a task of its own or an amendment to 154's scope; the observation is outside 56.2's boundary either way.
- Affects: phase 56 / `docs/sakshi-harness/skill-cycle.md` — Also carried forward from 56.1's review and still open: the cycle doc paraphrases the blast-radius repair as an enumeration found by code search. It is a paraphrase, so neither spec's verbatim-quote sweep reaches it, and it is a doc rather than a run artifact, so no "describes a moment" exception covers it. Not this task's file boundary.

