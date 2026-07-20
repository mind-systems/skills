# Plan Review — 20.2 `$TEST_CMD` derivation rule + Layer 7 no-command behavior (round 2)

## Code Review Summary

**Files Reviewed:** 1 plan + target skill (`src/skills/roadmap-test-coverage/SKILL.md`), spec `82-test-cmd-derivation-rule.md` (and its working-tree diff), roadmap line 20.2, `src/skills/aif/SKILL.md`, round-1 plan-review
**Risk Level:** 🟢 Low

All line references re-verified against the current file: Layer 1 read list L27–32 ✓, `$STACK` block L37–47 ✓, `$TEST_CMD` paragraph L49–54 ✓, Layer 7 L273–333 ✓, run block L275–278 ✓, classifier prompt L288–318 ✓, re-run gate L333 ✓, Layer 8 counts block L348–350 ✓, `$HANDOFF_LIST` print L355–356 ✓, pointer invariant L371–376 ✓, `allowed-tools` L10 ✓. No wrong paths, no missing migrations, no security surface.

### Context Gates

- **Architecture** — WARN (informational): `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" present; this task edits an existing lens body only, adds no skill and no `loads:` edge. No boundary issue.
- **Rules** — WARN: no `.ai-factory/RULES.md` in this repo. Optional file, nothing to check against.
- **Roadmap** — OK: plan heading matches roadmap line 20.2 in `.ai-factory/roadmaps/trickster77777.md`; `Spec:` tag resolves to `.ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md`, read in full along with its uncommitted amendment. Plan Tasks 1–5 map onto the spec's three Change bullets and its six static Verification checks with no orphan on either side.

### Critical Issues

None. Both round-1 blockers are genuinely closed, and closed at the right tier:

- **Round-1 issue 1 (Layer 8 had no rendering slot for the skip)** — resolved by option (b), and resolved *in the spec*, not assumed by the plan. The spec's working-tree diff splits visibility into its own Change bullet, narrows the blanket "Layer 8 byte-identical" guard to "Layer 8 takes exactly one added line" with the `$HANDOFF_LIST` print, both categories, and the pointer invariant explicitly preserved, and adds the matching Verification check. The spec text even records *why* the guard was narrowed — the collision between the broad guard and the task's own visibility requirement. Plan grounding note 2 and Task 4 track that decision faithfully, including the "does not enter `$HANDOFF_LIST`" negative. This is the decision the round-1 review asked to be written down, written down.
- **Round-1 issue 2 (`CLAUDE.md` missing from Layer 1's read list)** — resolved twice over: a new spec Guard ("Layer 1's read list gains `CLAUDE.md`"), a new spec Verification bullet, and a dedicated plan Task 1 that lands ahead of Task 2's dependency edge. Task 1's rationale reproduces the 20.1 asymmetry correctly (`$STACK`'s primary source was already in the read list; `$TEST_CMD`'s is not) and the grove argument against relying on the ambient auto-load.

### Positive Notes

- **Grounding note 1 remains correct and is now load-bearing.** Verified again against `src/skills/aif/SKILL.md` L37: `## Commands` is specified only as "(from the detected package manager or Makefile targets; leave light if no scaffolding exists yet)" — no mandated table, no mandated `Tests` row. The spec's Change bullet 1 and its first Verification bullet both still say "the `Tests` row"; the plan pre-empts a literal reading of that by pinning the rule to the *section* with the table row named as typical shape rather than parse contract. A clean DEVIATION: ground truth cited, spec intent preserved, and the residual spec inaccuracy re-filed rather than silently absorbed.
- **Task decomposition now carries real dependency edges** (1 → 2 → 3 → 4 → 5), and each task names exactly one file with a bounded region. Task 5's guard-confirmation step enumerates the four permitted diff regions and maps 1:1 onto the spec's Verification list.
- **The negative constraints are stated as explicitly as the positive ones** — the `$STACK` block byte-identical, Layers 2–6 untouched, the four-manifest list unextended, Layer 8's handoff machinery and pointer invariant untouched, no `$HANDOFF_LIST` append for the skip. Task 2 also correctly identifies the now-false sentence fragment ("the never-extend rule binds `$STACK` detection, not `$TEST_CMD`'s read") as something that must go with the rewrite, rather than leaving a contradiction behind in the file.
- **Correctly concludes `allowed-tools` needs no change** — the primary rule adds a `Read`, already granted at L10.
- **Out of scope** correctly refuses the live Python run and pre-empts reporting its absence as a gap, exactly as the spec's verification note demands.

One non-blocking wording note for the implementer, inside Task 4's existing scope: Layer 6 annotates its carried state explicitly ("`$HANDOFF_LIST` (in-memory, carried through to Layer 8)"). Phrasing Layer 7's skip the same way — a named flag carried to Layer 8 — would match the file's own convention for cross-layer state. The plan's "prints only when Layer 7 skipped the gate" is unambiguous as written, so this is a register match, not a correction.

## Deferred observations

- Affects: phase 20 / `.ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md` — Change bullet 1 and the first Verification bullet still describe the primary source as "the `## Commands` table `aif` writes into `CLAUDE.md` (the `Tests` row…)", which overstates what `aif` actually mandates: `src/skills/aif/SKILL.md` L37 specifies no table and no row label. The plan handles this correctly at the plan tier, so implementation is unaffected, but the spec text remains inaccurate about its own upstream and will mislead a reader who consults it directly — including a future verifier who might read the `Tests` row as a parse contract. Worth a small spec correction on a future pass.
- Affects: phase 20 / `.ai-factory/roadmaps/trickster77777.md` line 20.2 — the contract line still carries the pre-amendment guard, "Guard: `$STACK` and Layers 2–6/8 byte-identical", and still says the skip is "logged, recorded in the handoff". The spec's amended Guards now supersede both: Layer 8 takes exactly one added counter line, and the skip deliberately stays out of `$HANDOFF_LIST`. The two tiers of the same task therefore disagree, and a reader of the contract line alone would judge this task's Layer 8 edit a guard violation. The roadmap sits outside this plan's file boundary (the plan touches `SKILL.md` only) and contract-line edits belong to the planning tier, so it is not this task's fix — but it should be reconciled before the line is marked `[x]`.

PLAN_REVIEW_PASS
