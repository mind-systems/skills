# Plan Review 2: aif-roadmap — render milestones via roadmap-engine (two-tier)

**Plan:** `.ai-factory/plans/21-aif-roadmap-render-milestones-via-roadmap-engine-two-tier.md`
**Files Reviewed:** 4 (plan, `aif-roadmap/SKILL.md`, `roadmap-engine/SKILL.md`, `CLAUDE.md`) + `roadmap-decompose/SKILL.md` (reference pattern), plan-review-1
**Risk Level:** 🟢 Low

## Round-2 focus

This is the second review pass. Round 1 raised three non-blocking recommendations. All three are now folded into the plan text:

- **Rec 1 (orphaned-note risk):** Addressed. Task 2 now carries an explicit "Orphaned-note guard (review rec 1)" — draft contract lines with a `` Spec: `<note pending>`. `` placeholder in 1.3, write notes only for the **confirmed set after Step 1.4**, then replace the placeholder with the real tag before saving. This mirrors `roadmap-decompose` Step 1.4 verbatim in intent (`"Milestones removed or rewritten during options 2–4 receive no note; only the confirmed set gets notes."`). ✅
- **Rec 2 (dropped vision-sourcing cue):** Addressed. Task 2's glue now states "The roadmap vision line is sourced from `DESCRIPTION.md` or user input (per Step 0)." ✅
- **Rec 3 (`---` separator not orphaned):** Addressed. Task 4 has a "Separator note (review rec 3)" explicitly instructing the implementer to leave the `---` before `## Critical Rules` in place and treat the collapse-orphaned-separator guard as a no-op. ✅

## Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md`):** present. The plan honors the composition model (mechanism vs policy): `aif-roadmap` retains only its granularity *policy* (5–15 high-level goals) and delegates the two-tier artifact *mechanism* to `roadmap-engine`. This is exactly the engine/philosophy split the architecture prescribes. No boundary violation. **OK.**
- **Rules (`.ai-factory/RULES.md`):** not present — no rules gate to apply. **WARN (optional file absent).**
- **Roadmap (`.ai-factory/ROADMAP.md`):** present; the milestone maps 1:1 to this plan. Milestone linkage explicit. **OK.**
- **skill-context (`aif-review/SKILL.md`):** not present — no project-specific review overrides. **WARN (optional).**

## Verification performed

- **Task 1 string is exact.** `allowed-tools` line 5 = `Read Write Edit Glob Grep Bash(git *) AskUserQuestion Questions`, matching the string Task 1 quotes. Adding `Skill` is correct and sufficient — the sibling `roadmap-decompose` uses `... AskUserQuestion Skill` to load the engine and `aif-note`. `aif-roadmap` already carries `Write`/`Edit`, so it can author both the notes and `ROADMAP.md` after loading the format. No missing tool (no separate `aif-note` entry is needed — it is loaded via `Skill`). ✅
- **Task 2 targets the right block.** Step 1.3 inline ```markdown``` render = lines 77–87; the "Rules for milestones:" list to preserve = lines 89–93. The placeholder/confirmation mechanism is a faithful port of `roadmap-decompose` Steps 1.3/1.3.1/1.4 minus the Atomicity Gate (correctly excluded per the carve-out). ✅
- **Task 3 targets the right block.** Step 2.4 = lines 155–159. Keeping "Ask user to describe new milestones" + "Insert them in logical order among existing milestones" verbatim and swapping only the produce/write step matches `roadmap-decompose` 2.4. Mode 2.3/2.5/2.6 and Mode 3 are correctly identified as mark/reorder-only (no new render). ✅
- **Task 4 targets the right block.** `## ROADMAP.md Format` = lines 233–245; the `---` divider is line 231 and is genuinely a Mode-3 → Critical-Rules separator, not orphaned. ✅
- **Task 5 is accurate against CLAUDE.md.** The `aif-roadmap` bullet is line 124 under "Intentionally diverged"; the "Custom skills — never overwrite" inline list is line 117. Moving it is justified now that it depends on the local-only `roadmap-engine`. After the move, "Intentionally diverged" retains only `aif-plan` — coherent. ✅
- **Commit message** conforms to house style (sentence case, no type prefix). ✅

## Critical Issues

None.

## Recommendations (non-blocking)

### 1. Minor: clarify where the "write notes after 1.4" instruction physically lives

The carve-out (plan line 14) lists **Step 1.4 among the byte-identical preserved sections**, while Task 2 instructs "after 1.4 confirmation, write each confirmed milestone's note and replace the placeholder … then save `ROADMAP.md`." Since 1.4 must stay verbatim, that deferred action has to be expressed entirely inside Step 1.3's glue text (a "later, at 1.4, do X" clause) rather than by editing 1.4. `roadmap-decompose` sidesteps this by physically placing the equivalent instruction *inside* its Step 1.4 (`"After 'Looks good — save it': …"`). The plan's approach is workable, but the implementer should be conscious that 1.3's glue must describe the full lifecycle (draft-with-placeholder → confirm at 1.4 → write notes → replace tag → save) without touching the 1.4 block. No correctness risk; the existing 1.4 line 109 ("…then save to `.ai-factory/ROADMAP.md`") stays compatible — it now simply saves the file with real `Spec:` tags.

### 2. Minor: the Step 1.3 lead-in sentence

Line 75 ("Create `.ai-factory/ROADMAP.md` with this format:") is the lead-in to the block being deleted. When the inline block is replaced with engine glue, that lead-in sentence should be folded into / replaced by the glue so it doesn't dangle referring to a format that is no longer inline. Trivial mechanical detail, called out only so it isn't left orphaned.

## Positive Notes

- All three round-1 recommendations were incorporated in place, each tagged to its source rec — clean traceability and no scope creep.
- Excellent carve-out discipline: the "preserve byte-identical EXCEPT the render sites" framing plus the explicit regression guard pre-empt the paraphrase/contradiction loops that cost earlier roadmap-family milestones multiple review rounds.
- The orphaned-note guard now matches `roadmap-decompose`'s confirmed-set-only rule exactly, closing the one substantive gap from round 1.
- Faithful to `roadmap-engine`'s format and to the "coarse (strategic) granularity" distinction that is the sole philosophy separating `aif-roadmap`'s output from `roadmap-decompose`'s.
- Dependency chain (Task 1 → 5) is coherent; the CLAUDE.md upstream-sync bookkeeping is a real and often-forgotten consequence of taking a local-only dependency, and it is captured correctly.

The plan is solid and safe to implement. The two remaining notes are clarity refinements for the implementer, not blockers.

PLAN_REVIEW_PASS
