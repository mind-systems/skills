## Code Review Summary

**Files Reviewed:** 1 product file (`src/skills/task-rescue/SKILL.md`). I checked it against the plan, task spec `0255` (as amended at `4d79472`), phase note `0226` and the governing spec `docs/names-and-reasons-not-laws.md`. The staged change to `.ai-factory/architects/trickster77777/07/buffer.md` is the architect's buffer and is not part of this task's product, so it is not reviewed here.
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture — OK.** The change stays inside one skill. `loads:` (`orchestrator-artifacts roadmap-engine note`) is unchanged, and `allowed-tools` keeps `AskUserQuestion` as the spec requires. `orchestrator-artifacts` § "3. Sidecar fields" still finds the closed set: § "Valid sidecar `step` states" and the four rollback states show no hunk in `git diff HEAD`.
- **Rules — WARN (optional file missing).** There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`.
- **Roadmap — OK.** Contract line 80.3 in `.ai-factory/roadmaps/trickster77777.md` links to `0255` through its `Spec:` tag. Phase 80's governing spec and phase note were read.
- **Spec sweep — OK.**
  - The spec's grep returns only the `allowed-tools` line and § 5.6's "for `roadmap-prune`'s gate to flag".
  - The plan's leftover grep (`depth menu|chosen depth|classification|root-cause sentence|Diagnosis Report|option [123]|first appended|Step 3 ends with`) returns nothing.
  - § 5.6 and § 5.7 each differ in exactly the one sentence the spec names.
  - The `description:` is about 590 chars, under the 1024 limit. It keeps "repairs to the depth of the root cause", which `docs/reserved-words.md` binds, and every trigger phrase.

### Critical Issues

**1. The second opening paragraph still pins the list the spec removes (Low).**
`src/skills/task-rescue/SKILL.md`, the paragraph opening "The roadmap contract line (in `$TARGET_FILE`)…", now ends: "A repair may go above the task — putting a phase in front of it, closing a phase, or deleting the task — as well as into the task spec, the contract line, the plan `.md` or the working-tree code."

Spec `0255`, § "What must be true after", in its paragraph on the opening, says: "the pinned list of task spec and contract line, plan, or working-tree code goes from the second paragraph". The implementation keeps that list in full and only adds "as well as". An agent reading the opening still meets the four depths of the removed depth menu, enumerated next to the new reach. That is the closed shape the phase removes: the phase note says a root "that is not a missing constraint has no place to be said".

*Fix:* end the sentence after the reach above the task, for example: "A repair may go above the task — putting a phase in front of it, closing a phase, or deleting the task." The first paragraph already says the repair "reaches as deep as the root cause, steered by that word", and the two-tier sentence before it already names the task spec and contract line as what a spec-tier repair edits.

**2. Two edited paragraphs in § 5.7 lost the file's hard wrap (Low, cosmetic).**
The plan's Context asks for the file's hard wrap of about 86 columns. Two changed lines break it:
- In the finders paragraph after the template, the edited line "outside it. *Who* is one of: the user; head N, by its number; the editor; the plan-reviewer or the" is 98 columns.
- In **When the write cannot happen.**, the edited line "Either way, **say so plainly to the user.** Never" stops at about 50 columns, and the next line is not reflowed.

*Fix:* reflow both paragraphs to the file's wrap. Change no words.

### Positive Notes

- **Steps 2 and 3 carry exactly what the spec asks.** Step 2 holds two facts, each with its reason: the escalation is read first, and a resumed implementer can return with no diff. Step 3 asks the five questions verbatim and says none of them routes to a repair. The classification, categories, root sentence, special forms and depth routing are all gone, and nothing replaces them with a new answer.
- **The narrative was reworded without presuming a defect or an implementation.** It now reads "the story of the attempt", "what each round did, what its review found…", and "findings from every round the narrative tells". It keeps its prose form and its ban on tables and bullets.
- **The pause has one clear shape.** Step 3 makes the first write and then stops, saying where the report lies. Step 5 opens on the user's word and folds question five's open-task clauses into what that word releases. § 5.6's pin waits for the same word. § 5.7's appended section no longer claims to be "first", so readings appended during the pause fit.
- **Step 1 is ordered by its own dependency.** `$TARGET_FILE` is resolved before the sidecar bullet that relies on it. The test-sibling guess is gone, and the governing-spec read is one sentence, as specified.
- **The template's sections are referenced by name.** `## Intended repair` gives the intended rollback, an escalation's options and question five a literal home. The finders paragraph names `## Who found what` by its heading, so the new section cannot capture it.
- **§ "What NOT to do" is gone.** Its two repair-logic fences were not moved into any step.

## Deferred observations

- Affects: Phase 80 / task spec `.ai-factory/specs/trickster77777/0255-the-answers-become-questions-and-the-rescue-pauses-on-the-report.md` — § "Step 5.6 — Pin disposed observations" opens with "A rescue pins each deferred-observation entry it disposes of this session at the moment it disposes of it". Its second paragraph now says "A pin is written when the repair is applied, on the user's word, and not at the moment of a judgment made before it". A rescue that disposes of an entry in Step 3, while it writes its intended repair, gets two different times from these sentences. The spec allows only the one-sentence change and says "The rest of § 5.6 stays", so the opening sentence cannot be aligned within this task. Aligning it (for example, "disposes of" read as "on the word that applies the disposal") is for whoever owns the spec or a later task that places § 5.6. [routed → .ai-factory/specs/trickster77777/0256-section-5-6-states-one-moment-for-a-pin.md]
- Affects: `docs/sakshi-harness/skill-cycle.md` (another phase's doc, per `0255` § "What breaks on contact") — the doc still describes the rescue as diagnosing the depth of the root cause and says nothing of the report-then-pause. It stays true at its own level of abstraction. Reconciling it belongs to the phase that owns the doc. [routed → .ai-factory/roadmaps/trickster77777.md § Phase 95]
