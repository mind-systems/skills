## Code Review Summary

**Files Reviewed:** 1 (`src/skills/task-rescue/SKILL.md`; the plan, its sidecar and the plan-reviews are pipeline artifacts)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap — OK.** `# Plan: 80.1 — The report is the chronicle` matches task 80.1 in `.ai-factory/roadmaps/trickster77777.md`, Phase 80. That phase's governing spec is `docs/names-and-reasons-not-laws.md`. I read the task spec `0253-the-report-is-the-chronicle.md` in full and checked each clause of its § "What must be true after" against the diff:
  - Step 3 ends with the first write, made per § 5.7 through `note`, and the rescue keeps the returned path.
  - Each addition is a dated section appended directly to the file, and no earlier line changes. "What was done" became the first appended section.
  - `Stopped at` holds the `step` fact and what stopped the run, and there is no second stop line.
  - `## Who found what` holds a separate line for the root cause's finder and one bullet per finding. It lists the full *who* and *when* sets, names the sources (session keys, file round numbers, conversation), and writes "not stated" when no source names a finder.
  - The "When", "Which runs" and printout paragraphs are gone.
  - The Step 3 vocabulary label and sentence are gone, and the narrative may now name a round and a reviewer.
  - The "What NOT to do" bullet is gone.
  - "When the write cannot happen" is kept unchanged.
- **Spec sweep — OK.** `grep -n -E "reopened|exactly once|reads it back|Zero orch|orchestrator mech" src/skills/task-rescue/SKILL.md` and the plan's second grep (`What was done|Which runs|printout is unchanged|once, at the end|domain language`) both return nothing.
- **Frontmatter — OK.** It is unchanged. `allowed-tools` already grants `Write Edit` for the appends, and `loads:` already holds `note`.
- **Outside the skill — OK.** `docs/the-pipeline-speaks-to-an-architect.md` § "The report travels on" and `docs/self-analysis.md` stay true, as the spec's Finding says.
- **ARCHITECTURE — OK.** The change sits inside one skill and crosses no boundary.
- **RULES / skill-context — WARN (not present).** There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`.

### Critical Issues

1. **Low (cosmetic). A broken hard wrap is left in Step 3's escalation paragraph.**
   In § "Step 3 — Extract root cause", the paragraph that opens "For an escalation classification" now has a line that reads only "artifact's `## Escalation` section. End". The parenthetical was deleted from the middle of the line and the paragraph was not reflowed. The plan's Context says to keep the file's hard wrap at about 86 columns, and every other edited paragraph in the diff was reflowed. The rendered Markdown is the same, but the raw source has a stray short line that a later editor of this paragraph will trip over.
   **Fix:** reflow that paragraph to the surrounding width:
   ```
   For an escalation classification, the narrative has no defect chain to tell either:
   state plainly that [role] stopped on a decision outside its authority, then restate —
   verbatim or lightly paraphrased — the missing decision and its options from the
   artifact's `## Escalation` section. End with that decision restated as a block
   quote, in place of the root-cause sentence — there is no root cause here, only a
   decision still to make.
   ```

### Positive Notes

- The new "**Write the durable report.**" paragraph uses "the durable report" throughout. It does not collide with Step 3's own "the report", which means the printed Diagnosis Report.
- § 5.7 now places the destination resolution at the first write in all three spots: "at the moment of the first write", "re-resolved at the first write" and "resolved fresh at the first write". None of them still points at § 5.7 as the moment of the write.
- "Extending the file" covers the case where the first write failed: nothing is appended and Write creates no file. This keeps "never invent a fallback path" and "never defer the write" intact without changing the kept paragraph.
- The finder section is kept outside the diagnosis, so the diagnosis keeps its prose form, as the spec requires. The existing "title phrase" paragraph already covers the escalation branch, which has no root cause, so no special case was needed.
- The text is in the present tense throughout and does not mention the removed "What was done" section.

## Deferred observations

- Affects: `.ai-factory/specs/trickster77777/0255-the-answers-become-questions-and-the-rescue-pauses-on-the-report.md` — The first write's `## Who found what` section is written at the end of Step 3, before any repair. Its *when* value "after the rescue, for a defect in the repair itself" can therefore never appear there. Such a finding can only arrive in a later dated section, often appended by a head. The skill never says that an appended section names its finder in the same *who*/*when* terms. 80.3, which reworks how the rescue extends its report after the user's word, should decide whether appended sections carry finder lines too. This is the same handoff the plan-reviews already recorded: the scope-overload exit leaves a first write with no dated section. [routed → .ai-factory/specs/trickster77777/0257-the-rescue-report-drops-the-finder-section.md]
