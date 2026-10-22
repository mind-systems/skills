## Code Review Summary

**Files Reviewed:** 1 plan (`.ai-factory/plans/trickster77777/20-80-2-step-5-is-mechanics.md`) against its target `src/skills/task-rescue/SKILL.md`, the task spec `.ai-factory/specs/trickster77777/0254-step-5-is-mechanics.md`, the governing spec `docs/names-and-reasons-not-laws.md`, `src/skills/orchestrator-artifacts/SKILL.md` (§ "1. Layout", § "3. Sidecar fields", § "6. Status-marker grammar"), and the neighbouring 80.3 task spec.
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` is present and does not mention `task-rescue`. The plan keeps the engine boundary: § 5.6 points to `orchestrator-artifacts` for the marker grammar and does not restate it, and the sidecar location points to § "1. Layout".
- **Rules** — WARN. There is no `.ai-factory/RULES.md`, so no explicit convention gate applies.
- **Roadmap** — OK. The plan maps to `.ai-factory/roadmaps/trickster77777.md`, task 80.2, under Phase 80 (`Governing spec: docs/names-and-reasons-not-laws.md`). I read the spec named by the task's `Spec:` tag and the phase's governing spec. 80.1 is `[x]` and is the HEAD commit (`d8b10d1`). The § "3. Sidecar fields" pointer the plan matches is present in § 5.7.
- **Skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` is absent, so no overrides apply.

### Verification against ground truth

- **Spec conformance.** Every clause of § "What must be true after" has a plan step, and the plan adds nothing the spec does not cover:
  - one deletion rule, with the "never touch the spec file" sentence removed;
  - one sidecar write;
  - four states, each worded the same as the spec;
  - the table, the silent-failure line and the test-mode line stay;
  - the procedures, `Emit:` lines, notes and closing restatement go;
  - the option-keyed paragraphs name their states;
  - § 5.6 pins by pointer, and only the parenthetical leaves its scope paragraph;
  - Step 4's `Rollback:` lines name their states, option 2's parenthetical goes, and "spec-depth" becomes "the full reset".
- **Sweep.** I ran the spec's grep on the current file. It hits lines in Step 4's escalation menu and routing paragraph, the Step 5 escalation paragraphs and procedures, the notes after the state table, and the last bullet of § "What NOT to do". The plan removes or rewrites every hit, so its post-condition (no lines returned) can be met. The word `bare` appears only in the retired-forms sentence, which the plan deletes.
- **Out-of-target repairs.** The plan's assumptions list three places that break the spec's own rule but are not among its targets:
  - Step 2's "plan-ratified rollback (Step 5)";
  - the sidecar-keys bullet and the `planned:1`/`implemented:1` guard bullet in § "What NOT to do";
  - the "spec-depth full reset verbatim" bullet in § "What NOT to do".

  I confirmed each one in the file. Every repair is minimal and stays inside the task's one-file boundary.
- **Cross-repo.** A grep over `skills/src`, `skills/docs` and `orchestrator/` finds no other reference to the "Depth:" procedures, "spec-depth", or the always-valid guard. `orchestrator/docs/features/resume.md` describes rescue only by concept, so it stays true.
- **Pointers.** The headings `## 1. Layout`, `## 3. Sidecar fields` and `## 6. Status-marker grammar` exist in `orchestrator-artifacts` exactly as the plan cites them. § 1 lays out the flat and `<stem>/` sidecar paths that the old procedures copied. § 6 holds the grammar and the dedup rule (pin every occurrence across that task's review files) that the new § 5.6 paragraph defers to.
- **Facts that leave.** Each fact in the deleted paragraphs either still has a home after the rewrite, or the spec explicitly drops it:
  - Escalation clearing is covered by the sidecar write ("drop `escalation` wherever rewritten") plus the full reset on escalation options 1 and 2.
  - The `planner`/`elapsed` preservation is in the sidecar write.
  - Each state's artifact guard is in the state's own "Requires".
  - Option 4's "resumes at implement, iter 1" is in the table.
  - The repair guidance and `Emit:` lines go because the spec requires it.
- **Untouched dependents stay true.** Each of these still reads correctly after the rewrite:
  - Step 1's mention of Step 5 deleting or rewriting artifacts.
  - § 5.7's "what the repair did — the depth chosen …".
  - The state table's intro, "Step 5 picks one of the six values".
  - § "What NOT to do"'s "chosen rollback depth" bullet.

### Critical Issues

None.

### Positive Notes

- The plan reads the spec's breakage rule as a rule, not a list. It finds the three places the spec's own "Finding" missed, and it cites the grep that proves no other file depends on the removed procedures.
- It cites `orchestrator-artifacts` sections by heading text, consistent with 80.1's § 5.7 pointer. It leaves alone the positional `§6` / `§ 1` mentions in text the spec says stays.
- It keeps the spec's split between 80.2 and 80.3: Step 4's flags, menus and closing line, and Step 2's classification, are left for 80.3, and the plan says so.
- The verification step reuses the spec's sweep verbatim and adds a § 5.6-specific check for the bracketed markers.

## Deferred observations

- Affects: `.ai-factory/specs/trickster77777/0255-the-answers-become-questions-and-the-rescue-pauses-on-the-report.md` — § "What is true now" lists, among the bullets of § "What NOT to do", "the `planner`, `elapsed` and `implementer` keys" and "the guards on writing `planned:1` and `implemented:1`". This plan deletes both bullets in 80.2, so once 80.2 lands, that description of the present is two bullets out of date. 80.3 removes the whole section anyway, so its intended outcome is unaffected, but whoever plans 80.3 will read a "true now" that no longer matches the file. [dismissed]
- Affects: `.ai-factory/specs/trickster77777/0254-step-5-is-mechanics.md` — the spec's sweep "Finding" attributes a hit to "the closing of Step 4". The only hit near there is actually the last bullet of § "What NOT to do". The Finding also does not list the Step 2 stale-implementer pointer or the two § "What NOT to do" bullets that its own rule breaks. The plan already repairs all of these in its Assumptions, so this concerns only the spec's accuracy as a record, not this task's outcome. [dismissed]

PLAN_REVIEW_PASS
