# Plan Review: aif-roadmap — render milestones via roadmap-engine (two-tier)

**Plan:** `.ai-factory/plans/21-aif-roadmap-render-milestones-via-roadmap-engine-two-tier.md`
**Files Reviewed:** 4 (plan, `aif-roadmap/SKILL.md`, `roadmap-engine/SKILL.md`, `CLAUDE.md`) + spec note 32, ROADMAP.md, roadmap-decompose (reference pattern)
**Risk Level:** 🟢 Low

## Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md`):** present. The plan honors the composition model (mechanism vs policy): `aif-roadmap` keeps only its granularity *policy* and delegates the two-tier artifact *mechanism* to `roadmap-engine`. No boundary violation. **OK.**
- **Rules (`.ai-factory/RULES.md`):** not present — no rules gate to apply. **WARN (optional file absent).**
- **Roadmap (`.ai-factory/ROADMAP.md`):** present. Milestone at line 51 ("aif-roadmap: render milestones via roadmap-engine (two-tier)") maps 1:1 to this plan, incl. the `Spec:` pointer to note 32. Milestone linkage is explicit. **OK.**
- **skill-context (`aif-review/SKILL.md`):** not present — no project-specific review overrides. **WARN (optional).**

## Verification performed

- **Line/section references are accurate.** Step 1.3 inline `markdown` block = current lines 77–87; "Rules for milestones:" = lines 89–93; Step 2.4 = lines 155–159; `## ROADMAP.md Format` = lines 233–245; `allowed-tools` = line 5 (matches the string quoted in Task 1 verbatim). All correct.
- **Tool name is correct.** Task 1 adds `Skill`; the sibling `roadmap-decompose` uses exactly `... AskUserQuestion Skill` to load the engine and `aif-note`. Consistent.
- **Delegation is sound.** The current `roadmap-engine` is an *explanation* applied by the caller (`allowed-tools: Read`), so `aif-roadmap` remains the writer of both the notes and `ROADMAP.md` — it retains `Write`/`Edit`. Deferring the note format + `aif-note` load-once to the engine (Task 2) avoids duplication, matching how `roadmap-decompose` glues in the engine.
- **CLAUDE.md Task 5 is accurate.** `aif-roadmap` bullet exists at line 124 under "Intentionally diverged"; the "Custom skills — never overwrite" inline list is line 117. The move is justified (now depends on local-only `roadmap-engine`).
- **Commit message** conforms to house style (sentence case, no type prefix).

## Critical Issues

None.

## Recommendations (non-blocking)

### 1. Note-generation happens before user confirmation (orphaned-note risk)

The plan (Task 2, per spec note 32) places the engine glue in **Step 1.3 (Generate)**, which runs **before Step 1.4 (Confirm with user)**. In Mode 1, Step 1.4 may still "Add more milestones" / "Remove/modify" / "Rewrite". If full spec notes are written for 5–15 milestones in 1.3 and the user then rewrites or removes some in 1.4, those note files (`.ai-factory/notes/<NN>-<slug>.md`) become orphans — the `<NN>` scan just skips the consumed numbers.

Note that the sibling skill deliberately avoids this: `roadmap-decompose` produces notes only **after** "Looks good — save it" and states *"Milestones removed or rewritten during options 2–4 receive no note; only the confirmed set gets notes."* The plan's own Task 2 wording ("produce each **confirmed** milestone") reflects that intent but places the action at pre-confirmation Step 1.3 — a mild internal tension.

This is not a blocker: aif-roadmap's Step 1.3 already writes `ROADMAP.md` before 1.4 today, so pre-confirmation output is the existing pattern, and the spec explicitly fixes the glue at 1.3 (the carve-out keeps 1.4 verbatim). Suggested handling for the implementer, in order of preference:
- Have the Step 1.3 glue instruct that notes are (re)written only for the **confirmed set after 1.4**, mirroring `roadmap-decompose`; or
- If keeping generation at 1.3, add one clause so a 1.4 rewrite/removal does not leave orphaned notes.

Either way, keep it to a glue-sentence tweak — do not restructure the modes.

### 2. Minor: vision-sourcing hint is dropped with the 1.3 block

The current Step 1.3 block carries `> <project vision — one-liner from DESCRIPTION.md or user input>`. The engine's Roadmap File Format only says `> <project vision — one-liner>`. Removing the whole 1.3 block loses the "from DESCRIPTION.md or user input" sourcing cue. Low impact (Step 0 already loads DESCRIPTION.md), but the implementer may want to retain that half-sentence in the glue.

### 3. Minor: the `---` separator at line 231 is not orphaned after Task 4

After deleting `## ROADMAP.md Format` (233–245), the `---` at line 231 cleanly separates Mode 3 from `## Critical Rules` — a valid section divider, consistent with the other `---` separators. Task 4's "collapse any orphaned `---`" guard therefore should be a **no-op** here; the implementer should not delete this separator. Worth calling out so the guard isn't misapplied.

## Positive Notes

- Excellent carve-out discipline: the "preserve byte-identical EXCEPT the render sites" framing and the explicit regression guard directly pre-empt the paraphrase/contradiction loops that cost milestone 30/18 multiple review rounds.
- Correct enumeration of all render sites (1.3 create, 2.4 add, `## ROADMAP.md Format`) — no dangling reference, and Modes 2.3/2.5/2.6 and Mode 3 are correctly identified as mark/reorder-only (no new render).
- Dependency chain (Task 1 → 5) is coherent; the CLAUDE.md upstream-sync bookkeeping is a real and often-forgotten consequence of taking a local-only dependency.
- Faithful to spec note 32 and the ROADMAP contract line, including the "coarse (strategic) granularity" distinction that is the sole philosophy separating aif-roadmap's output from decompose's.

The plan is solid and safe to implement. The recommendations above are refinements, not blockers.
