# Plan Review — 20.2 `$TEST_CMD` derivation rule + Layer 7 no-command behavior

## Code Review Summary

**Files Reviewed:** 1 plan + target skill (`src/skills/roadmap-test-coverage/SKILL.md`), spec `82-test-cmd-derivation-rule.md`, roadmap line 20.2, `src/skills/aif/SKILL.md`
**Risk Level:** 🟡 Medium

All line references in the plan verified against the file: `$STACK` block L37–47 ✓, `$TEST_CMD` paragraph L49–54 ✓, Layer 7 L273–333 ✓, run block L275–278 ✓, classifier prompt L288–318 ✓, re-run gate L333 ✓, Layer 8 print block L341–376 ✓. No wrong paths, no missing migrations, no security surface.

### Context Gates

- **Architecture** — WARN (informational): `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" present; this task edits an existing lens body only, adds no skill and no `loads:` edge. No boundary issue.
- **Rules** — WARN: no `.ai-factory/RULES.md` in this repo. Optional file, nothing to check against.
- **Roadmap** — OK: plan heading matches roadmap line 20.2 in `.ai-factory/roadmaps/trickster77777.md` L26; `Spec:` tag resolves to `.ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md`, which was read. Plan's Tasks 1–3 map onto the spec's two Change bullets plus its four static Verification checks. Out-of-scope section correctly honors the spec's "Verification note — out of pipeline".

### Critical Issues

**1. Grounding note #2's central claim is wrong: Layer 8 does not print `$HANDOFF_LIST` verbatim, so the skip entry has no rendering slot.**
`src/skills/roadmap-test-coverage/SKILL.md` L355–376. The note asserts "Layer 8 prints `$HANDOFF_LIST` unchanged, so the skip surfaces with no Layer 8 edit." Ground truth is stronger than that: L355 says print it *"as concrete one-line task descriptions"*, and the template that follows is not a passthrough — it is a fixed two-category structure (`Refactor:`, `Bugs (Class B — silent failures):`) with a mandated per-line pointer, closed by an explicit invariant at L371–376: *"Every handoff line resolves to a pointer; none are left blank."*

A skip entry ("No test command resolved — existing-test gate skipped") belongs to neither category and has no pointer available — no Layer-4 note path (it is not an area) and no source file path (no test failed). It therefore collides with a stated Layer 8 invariant rather than sitting in an awkward-but-harmless seam. The counts block (L348–350: `Refactor items handed off`, `Existing tests patched`, `Class B items handed off`) likewise has no line for it.

Consequence: the spec's requirement at its Change bullet 2 — *"record the skip in the handoff so it is **visible, never silent**"* — is not reliably met by the planned mechanism. The implementing agent, following Layer 8 literally, would have to either drop the entry or invent an unspecified third heading, and the second is the guard violation the note is trying to avoid.

The note's own escape hatch ("if review judges the categorization unacceptable, the fix is a follow-up task that opens Layer 8") is the right instinct but is filed as a contingency rather than as the decision. This review makes the call: **as planned, the visibility requirement is unsatisfied.** Resolve before implementing, by picking one:
- (a) Route the skip somewhere Layer 8 already prints without structure — the plain Layer 7 log line only — and **amend the spec** to drop "record the skip in the handoff", since the guard and the requirement genuinely conflict. This keeps the guard intact and is honest about the reduction.
- (b) Treat the guard's "Layer 8 byte-identical" as scoped to the *classification/pointer machinery* and take a minimal Layer 8 addition (one heading + one counter) inside this task — a guard amendment that must be written into the spec, not assumed.
- (c) Split: land Tasks 1–2 with the log-only skip, and open a follow-up task for Layer 8's skip category.

Whichever is chosen, the decision belongs in the spec before Task 2 is implemented — this is a missing decision the plan surfaces but does not close.

**2. Layer 1's read list does not include `CLAUDE.md`, and no task adds it.**
`src/skills/roadmap-test-coverage/SKILL.md` L27–32. Layer 1's "Read in order (skip if absent)" list names exactly two inputs: `.ai-factory/ARCHITECTURE.md` and the roadmap. Task 1's new **Primary** rule reads the project's `CLAUDE.md` `## Commands` section, but Task 1 is scoped to rewriting L49–54 only, so the file the primary rule depends on is never added to the layer's own input list.

This is precisely the asymmetry with 20.1 that makes it easy to miss: `$STACK`'s primary source (`ARCHITECTURE.md`) was *already* in the read list, so 20.1 needed no such addition. `$TEST_CMD`'s primary source is not.

Relying on the ambient auto-load of the project `CLAUDE.md` is not a substitute — Layer 1 is written as an explicit read procedure, and the skill may run against a roadmap in a sub-repo whose `CLAUDE.md` is not the one loaded (this repo is a grove; the root and each sub-repo have their own). Add `CLAUDE.md` to the L27–32 read list as part of Task 1. Note this touches Layer 1 only, so it stays inside the guard.

### Positive Notes

- **Grounding note #1 is correct and well-earned.** Verified against `src/skills/aif/SKILL.md` § "CLAUDE.md Generation": `## Commands` is specified only as "(from the detected package manager or Makefile targets; leave light if no scaffolding exists yet)" — no mandated table, no mandated `Tests` row. The spec's "the `Tests` row" wording is indeed looser than the code, and the plan's correction — rule against the *section*, table row named as typical shape rather than parse contract — is the right read and prevents a silent fall-through on most real `CLAUDE.md` files. This is a genuine DEVIATION handled properly: ground truth cited, intent preserved.
- Task 3's guard-confirmation step is concrete and checkable (byte-identical `$STACK` block, Layers 2–6/8, four-manifest list unextended, `package.json` fallback intact) and maps 1:1 onto the spec's Verification list.
- Correctly concludes `allowed-tools` needs no change — the primary rule adds a `Read`, already granted at L10.
- Out-of-scope section correctly refuses the live Python run and pre-empts reporting its absence as a gap, exactly as the spec's verification note demands.

## Deferred observations

- Affects: phase 20 / `.ai-factory/specs/trickster77777/82-test-cmd-derivation-rule.md` — The spec's Change bullet 1 says the primary is "the `## Commands` table `aif` writes into `CLAUDE.md` (the `Tests` row…)", which overstates what `aif` actually mandates (see Positive Notes). The plan works around this correctly at the plan tier, but the spec text itself remains inaccurate about its own upstream and will mislead the next reader who consults it directly. Worth a small spec correction on a future pass, independent of this task's implementation.

Critical issue 1 requires a decision recorded in the spec, and issue 2 requires an added task step. Both sit inside this task's file boundary and are findings, not deferrals.
