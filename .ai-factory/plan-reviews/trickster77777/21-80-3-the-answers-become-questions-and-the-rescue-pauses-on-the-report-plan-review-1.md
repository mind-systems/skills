## Code Review Summary

**Files Reviewed:** 1 target (`src/skills/task-rescue/SKILL.md` at HEAD `4d79472`), against the plan, task spec `0255`, phase note `0226`, governing spec `docs/names-and-reasons-not-laws.md`, `roadmap-engine` § "Named roadmaps", `orchestrator-artifacts` § "3. Sidecar fields", and the rescue report `rescue-reports/skills/10-80-3-each-plan-review-found-one-new-small-thing.md`
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture — OK.** `.ai-factory/ARCHITECTURE.md` does not name `task-rescue`; the plan stays inside one skill file and changes no `loads:` edge (`orchestrator-artifacts roadmap-engine note` stay).
- **Rules — WARN (missing optional file).** No `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`; nothing to check against.
- **Roadmap — OK.** Contract line 80.3 in `.ai-factory/roadmaps/trickster77777.md` is linked through `Spec:` to `0255`. Phase 80 names `Governing spec: docs/names-and-reasons-not-laws.md` and `Phase note: …0226…`; I read both. Every plan task maps to a clause of `0255` § "What must be true after". The rescue's spec changes from commit `4d79472` (opening subject sentence, open reach list, § 5.6 timing, § 5.7 "complete the rescue anyway") are all in the plan.
- **Outside references — OK, as the plan says.** A grep over `src/`, `docs/`, `../orchestrator/orchestrator` and `../orchestrator/docs` finds nothing outside this skill that cites Step 4, § 5.5, § "What NOT to do", "Diagnosis Report" or a depth menu. `orchestrator-artifacts` § "3. Sidecar fields" points only at the closed set, which stays untouched. `docs/sakshi-harness/skill-cycle.md` § "Когда task не сходится" still says the rescue "диагностирует глубину корня". The spec assigns that doc to another phase (95), so it is not a finding here.

I checked the plan's claims against the file one by one, and they hold:
- the governing-spec paragraph's guards and its "Diagnosis Report" reference are in Step 1;
- Step 1's sidecar bullet depends on `$TARGET_FILE` being resolved above it;
- Step 2's five classes and its severity paragraph are as described;
- Step 3 holds every paragraph the plan names: the "Recurring issues" paragraph, the categories, the governing-spec judgment, "carry into Step 4", the special forms, the "Describe what…" sentence, the root sentence and the category attachment;
- Step 4's resolution and both menus are as described;
- Step 5's opening and its four option paragraphs, each set off by `---`, are as described;
- § 5.5 and its trailing `---` are as described;
- the § 5.6 sentence is as quoted;
- § 5.7's "Extending the file.", title-phrase and finders paragraphs and its "When the write cannot happen." sentence are as quoted;
- § "What NOT to do" holds the bullets the plan lists.

The deletion boundaries leave exactly one `---` between the remaining sections. The sweep's allowed hits match what will survive.

### Critical Issues

None blocking. Two low findings sit in sentences this task rewrites or keeps. Both are fixable inside the plan's own tasks.

**1. § 5.7 "Extending the file." keeps "the first appended section" for the repair's record, but the pause makes appends before the repair the normal case (task "Update § 5.7 for the intended repair and the post-repair section").**
The plan says: "rewrite the description of the first appended section. It is made once the repair is done, on the user's word…". This task adds a pause in which the user reads the report. Remarks made during that reading are appended under their date while the rescue is hot, and the skill allows that ("Each addition is a section headed by its date… appended directly to the path the first write returned").

The ground truth already shows this order. `rescue-reports/skills/10-80-3-each-plan-review-found-one-new-small-thing.md` is the rescue of this very task. It holds `## 2026-10-22` (head 09's reading and a cut to the intended repair, before the word), and only then `## 2026-10-22 — the repair, on the user's word`.

Calling the repair's section "the first appended section" is therefore false of the shape the pause creates. An agent could also read it as a ban on appending anything during the pause, which is exactly when the user's and a head's readings arrive. Spec `0255` says only "The section appended to the report after the repair says what the repair did…", with no "first".
*Fix:* describe it as the section appended once the repair is done, on the user's word, without "first". Keep the rest of the bullet as planned: what the repair did, the rollback state the task was left in, what was deleted or kept, and the removal of "the depth chosen, the escalation option taken, or the non-convergence choice made". The last sentence of the paragraph ("When the first write returned no path…, nothing is appended") is about the *first write*, not the first append, so it stays as it is.

**2. Step 3 keeps "Step 3 ends with the first write of the durable report." verbatim, but the plan puts the stop after it (task "Rewrite Step 3 as five questions, the narrative, the intended repair and the stop", items 4–5).**
Item 4 says "Keep the existing **Write the durable report.** paragraph". That paragraph opens "Step 3 ends with the first write of the durable report." Item 5 then adds "The stop. The rescue then stops. In the conversation it says where the report lies…" after it.

The result would be a step that says it ends on the write, followed by another paragraph of the same step. That paragraph is now the step's real end, and it is the part this task exists to add.
*Fix:* reword only that opening clause so it no longer claims the step ends there, for example "Step 3 makes the first write of the durable report." Keep the rest of the paragraph (per § 5.7, through `note`, destination, hooks, topic slug, the returned path) and item 4's addition as planned. § 5.7's own "The first write happens at the end of Step 3" stays true and needs no change.

### Positive Notes

- The plan's Assumptions ground every non-obvious call in the file or the spec:
  - the twin "Describe what…" sentence and the defect-chain sentence;
  - the "(2+)" qualifier and why it would hide the non-recurring findings that question 1 asks about;
  - the three fences of "What NOT to do" that go with no home, and the explicit ban on re-housing them in Step 3 or Step 5;
  - the signal pointer kept in Step 2 only.
- The plan moves `$TARGET_FILE` resolution and the contract-line locate ahead of **Capture the report facts.** on purpose, because that section's sidecar bullet depends on them. The plan names that dependency. It also drops the test-sibling guess, as the spec requires.
- The new `## Intended repair` template section resolves the "first write must hold the intended repair beside the diagnosis" requirement within a template that is "given literally". It gives question five and an escalation's options a home. It also changes the finders paragraph to name `## Who found what` by its heading, so "this section" cannot point at the wrong place. That is reference by name, applied.
- The § 5.7 "When the write cannot happen." change does exactly what the rescue's head-09 cut asks: it drops the clause and adds no resolution.
- The final sweep task runs the spec's grep and a second grep for leftovers. It also checks byte-identity of the closed-set table and the four rollback states, and that § 5.6 has a single-sentence diff. These are mechanical guards on the hunks this task must not touch.
