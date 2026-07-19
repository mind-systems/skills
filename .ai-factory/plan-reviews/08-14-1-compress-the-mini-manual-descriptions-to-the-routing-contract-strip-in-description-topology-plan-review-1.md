# Plan review 1 — 14.1 Compress the mini-manual descriptions to the routing contract; strip in-description topology

## Plan Review Summary

**Plan:** `.ai-factory/plans/08-14-1-compress-the-mini-manual-descriptions-to-the-routing-contract-strip-in-description-topology.md`
**Spec:** `.ai-factory/specs/74-descfield-routing-contract-compression.md`
**Governing spec:** [skill-description-field](../../docs/skill-description-field.md)
**Files targeted:** 12 (10 skills, 1 agent, 1 command) + this plan file's own records
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md`) — PASS. The edit set touches only `description:` frontmatter; it neither adds nor removes a `loads:` edge, so the skill graph and the mechanism/policy split are untouched. Every cut clause's fact keeps a home already present in the repo: the `loads:` line (Tasks 4, 6b, 6c for `roadmap-decompose`/`roadmap-engine`), the engine body's reverse-graph marker (Tasks 6, 6b), or a sibling skill's own description (Task 6c `temporal-tree`).
- **Rules / global CLAUDE.md** — PASS. The plan is a one-home-per-fact application; the "no vocabulary edits, Phase 17 owns word choice" guard correctly keeps this pass off the lexical axis.
- **Roadmap** (`.ai-factory/ROADMAP.md:43`) — PASS. Task 14.1 is `[ ]`, its `Spec:` tag resolves to spec 74, and the plan conforms to both tiers. The contract line enumerates five mini-manuals plus three candidates; the plan additionally opens four already-at-grain entries (`test-philosophy`, `roadmap-decompose`, `roadmap-engine`, `temporal-tree`) for their wiring clause only. This is not scope creep — the contract line's own title, "strip in-description topology", covers the field-wide wiring sweep, and spec 74's disposition list (§ "Wiring clauses across the loaded field") is the two-tier home that authorizes each of the four by name.

### Verification of the plan's factual claims

Every checkable assertion in the plan was verified against the files:

| Claim | Verdict |
|---|---|
| Pre-edit baseline table (12 rows, total 5781) | **Exact.** Independently recomputed whitespace-normalized description bodies: 542 / 739 / 420 / 619 / 628 / 547 / 432 / 420 / 360 / 378 / 303 / 393 → 5781. All twelve match. |
| `test-philosophy`'s reverse-graph marker at `SKILL.md:22-23` | **Correct** — the marker spans lines 20-23; the `grep -l "test-philosophy"` resolver sits on 22-23. |
| `orchestrator-artifacts`' reverse-graph marker present in the body | **Correct** (`SKILL.md:17-19`). |
| `task-rescue` is not on `task-rescue-audit`'s `loads:` line | **Correct** (`loads: orchestrator-artifacts`) — the warm-entry when-anchor is genuinely not a load edge. |
| `detangle` is not on `temporal-tree`'s `loads:` line | **Correct** (`loads: roadmap-engine`). |
| `aif-architecture` carries no `loads:` field at all | **Correct** — the file has none, so "or after /aif setup" cannot be a load edge. The clearest when-anchor, as the plan says. |
| `roadmap-prune`'s own description is the home for the Features-table provenance | **Correct** — its description states it anchors each feature to its commit hash in ARCHITECTURE.md, so cutting `(produced by roadmap-prune)` from `temporal-tree` loses no fact. |
| `roadmap-engine` on `roadmap-decompose`'s `loads:` line; `note` on `roadmap-engine`'s | **Correct** on both. |
| `Orchestrates full test coverage planning for a project.` is unhyphenated in source | **Correct** — the "do not respell it" pin is well-placed and prevents a Phase 17 collision. |
| `command-pin-gaps` is already what + when + concept with no wiring | **Correct** — it loads `roadmap-engine` but names no edge; "no change" is the right expectation. |

**The disposition list is genuinely closed.** I ran an independent sweep of all 23 entries in the loaded field (`active/skills/`, `active/commands/`, `active/agents/`) for cross-references to any other skill in the field. Every hit falls on the plan's list — the five cuts, the three when-anchors, the two concept keeps, and the four declared non-matches. Nothing surfaced outside it. Task 8's sweep is therefore decidable against a list that actually closes, which was the failure mode spec 74 was rewritten to avoid.

### Critical Issues

None.

### Assessment of the risky seams

The three places a plan like this usually breaks are all pinned:

1. **The discriminator is locally decidable.** "Names which skill loads / is loaded by / produces for which" → cut; "names what this skill itself does" → keep. Applied to the two hardest cases it gives the right answer without appeal to authority: `roadmap-test-coverage` keeps "filters areas by silent-failure risk" (own behavior) while `roadmap-decompose-skeleton` loses "filtered by test-philosophy's silent-failure rule" (names the edge). Task 4 catches that the compressed enumeration drops the `test-philosophy` name *with* it — a cut that a less careful plan would have split across two sentences and left half-done.
2. **The keep list has cover for clauses in unopened files.** The note at line 23 — that "already at grain" disposes of grain only and says nothing about wiring, so a kept clause in an unopened file still needs its disposition recorded — is the exact reasoning that keeps Task 8 from raising `aif-architecture`'s "or after /aif setup" as an omission. Without it the verify stage would loop on a file no task is allowed to open.
3. **The `test-philosophy` when-signal is discharged, not hand-waved.** Deleting the caller list removes that entry's only when-shaped clause, and the entry is model-invocable. The plan decides at plan time that the discriminator names its own moment of use, and forbids Task 8 from re-litigating it or adding a `Use when` to compensate. That is the correct call — the no-padding guard and the routing check would otherwise pull in opposite directions at verify time.

### Positive Notes

- **The baseline table is measured, not estimated**, and dated. Task 8's "carry the pre value forward for no-change rows so both columns total all twelve" closes the arithmetic hole that would otherwise let a 12-row pre total face a 9-row post total.
- **Every ambiguity that could cause a verify-stage loop is resolved in advance**, including the four `note`/caller-shaped non-matches listed explicitly "so no sweeper has to adjudicate them live", and the contrast drawn between `roadmap-engine`'s `written via note` (cut — names how the artifact is produced) and `command-handoff`'s "durable note under `.ai-factory/handoffs/`" (kept — names the output's genre). That distinction is subtle and correctly drawn.
- **The when-anchor class carries its own falsifiable test** — the named skill is not on the carrier's `loads:` line — rather than resting on judgment. All three instances verify.
- **Verdict and count destinations are pinned to one legal location** with "no other artifact is a legal destination", removing the usual drift where an implementer invents a sidecar file.
- **`editor`'s sole-caller clause is reasoned, not asserted.** Distinguishing a routing negative the main loop reads before spawning from operational protocol whose home is `agent-architect`'s body is the right cut line, and Task 5 correctly also collapses the genuinely duplicated two-mode statement.
- **Task 8's escape hatch is correct**: a wiring clause found in the field but off the list is reported as a defect in spec 74's inventory to reconcile, not fixed in place. That keeps the closed list closed and prevents the verify stage from silently expanding the edit set.

### Minor note (not blocking)

Task 6b's cut leaves `test-philosophy`'s description with two sentences opening on the same verb — `Holds one rule — …` followed by the re-capitalized `Holds no test-generation or coverage-pipeline logic.` The plan is right to accept this rather than fix it: repairing the repetition would be a word choice edit, which the guard reserves for Phase 17. Flagging only so the outcome reads as deliberate when the diff is reviewed.

## Deferred observations

- Affects: Phase 17 (word choice) — `test-philosophy`'s description will carry two consecutive `Holds …` sentence openers after Task 6b's mechanical cut and capitalization. The repetition is an artifact of removing the clause that separated them, and repairing it means choosing different wording, which is Phase 17's axis, not this task's. Worth picking up when that phase opens the entry, alongside any other lexical smoothing the compression pass leaves behind. [fixed — test-philosophy's description now reads "Carries no test-generation or coverage-pipeline logic", removing the repeated "Holds" opener]

PLAN_REVIEW_PASS
