## Code Review Summary

**Files Reviewed:** 1 product file, `src/skills/task-rescue/SKILL.md`, re-read in full from disk. I checked it against the plan, task spec `0255`, phase note `0226` and the governing spec `docs/names-and-reasons-not-laws.md`. The staged change to `.ai-factory/architects/trickster77777/07/buffer.md` is the architect's buffer, not this task's product.
**Risk Level:** 🟢 Low

### Previous findings (review 1)

**1. The second opening paragraph still pins the list the spec removes — Fixed.**
The paragraph now ends:
> "spec tier is repaired. A repair may go above the task — putting a phase in front of it,
> closing a phase, or deleting the task."

The four-item list ("as well as into the task spec, the contract line, the plan `.md` or the working-tree code") is gone, as spec `0255` requires ("the pinned list … goes from the second paragraph"). The first paragraph still carries "The repair then reaches as deep as the root cause, steered by that word".

**2. Two edited paragraphs in § 5.7 lost the file's hard wrap — Fixed.**
- The finders paragraph is reflowed. Its widest line is "plan-review and review file carries; the user and the heads come from the conversation." at 87 columns, and the 98-column line is gone. Its words are unchanged: "The diagnosis keeps its prose form; the finders live only in `## Who found what`, / outside it. *Who* is one of: the user; head N, by its number; the editor; the / plan-reviewer or the reviewer at round R; …"
- **When the write cannot happen.** is reflowed, and its words are unchanged: "Either way, **say so plainly to the user.** Never invent a fallback path, never fall / back to any directory inside the project being rescued, never invoke `note` a second / time, and never defer the write to a later run."

### Context Gates

- **Architecture — OK.** The change stays inside one skill, and `loads:` is unchanged. `allowed-tools` keeps `AskUserQuestion`.
- **Rules — WARN (missing optional file).** There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`.
- **Roadmap — OK.** Contract line 80.3 links to `0255` through `Spec:`. Phase 80's governing spec and phase note were read.
- **Spec sweep — OK.**
  - The spec's grep returns only the `allowed-tools` line and § 5.6's "for `roadmap-prune`'s gate to flag".
  - The leftover grep (`depth menu|chosen depth|classification|root-cause sentence|Diagnosis Report|option [123]|first appended|Step 3 ends with`) returns nothing.
  - No diff line touches the table of valid states, the four rollback states, the closed-set paragraph, or the silent-failure and test-mode lines.
  - § 5.6 and § 5.7 each change in exactly the sentence the spec names, plus the reflow the previous review asked for.

### Full review: new issues

None. Steps 1 to 3, the stop, Step 5's opening, § 5.6, § 5.7, the `description:` and the opening paragraphs all match spec `0255` § "What must be true after":
- **The facts and questions.** Step 2 holds the two facts. Step 3 asks the five questions verbatim and says none of them routes to a repair.
- **The diagnosis and the stop.** The narrative is in prose and presumes no defect. Step 3 makes the first write and then stops.
- **Step 5.** It opens on the user's word and releases the clauses for open tasks named under question five.
- **Removed sections.** Step 4, § 5.5 and § "What NOT to do" are gone, and the step numbers are kept.
- **Frontmatter.** The `description:` is under the field limit and keeps the root-cause clause and every trigger phrase.

### Positive Notes

- The fix to the opening is minimal and precise. It removes the pinned list and keeps the reach above the task, so the repair's depth comes only from the root cause and the user's word.
- The reflow changed no word. A word diff of § 5.7 shows only the one-sentence edits the spec names.
- The file now reads as one shape, report → stop → word → repair, with no leftover reference to a menu, a flag or a depth choice.

## Deferred observations

- Affects: Phase 80 / task spec `.ai-factory/specs/trickster77777/0255-the-answers-become-questions-and-the-rescue-pauses-on-the-report.md`. The two paragraphs of § "Step 5.6 — Pin disposed observations" give a pin two different times:
  - the opening paragraph: "A rescue pins each deferred-observation entry it disposes of this session at the moment it disposes of it";
  - the second paragraph: "A pin is written when the repair is applied, on the user's word, and not at the moment of a judgment made before it".

  A disposal judged in Step 3 is therefore told two different times. The spec allows only the one-sentence change ("The rest of § 5.6 stays"). Aligning the opening sentence belongs to the spec owner or to a later task that places § 5.6.
- Affects: `docs/sakshi-harness/skill-cycle.md`, which belongs to another phase per `0255` § "What breaks on contact". The doc still describes the rescue as diagnosing the depth of the root cause, and it does not mention the report-then-pause. It is still true at its own level of abstraction. Reconciling it belongs to the phase that owns the doc.

REVIEW_PASS
