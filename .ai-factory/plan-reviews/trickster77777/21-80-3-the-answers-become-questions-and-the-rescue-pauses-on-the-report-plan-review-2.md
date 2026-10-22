## Code Review Summary

**Files Reviewed:** 1 target (`src/skills/task-rescue/SKILL.md` at HEAD `4d79472`), checked against the plan, task spec `0255`, phase note `0226`, governing spec `docs/names-and-reasons-not-laws.md`, `roadmap-engine` § "Named roadmaps", `orchestrator-artifacts` § "3. Sidecar fields", the rescue report `rescue-reports/skills/10-80-3-each-plan-review-found-one-new-small-thing.md`, and plan-review 1
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture: OK.** The plan stays inside one skill file. It changes no `loads:` edge: `orchestrator-artifacts roadmap-engine note` stay.
- **Rules: WARN (optional file missing).** There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`.
- **Roadmap: OK.**
  - Contract line 80.3 in `.ai-factory/roadmaps/trickster77777.md` links to `0255` through `Spec:`.
  - Phase 80 names `Governing spec: docs/names-and-reasons-not-laws.md` and the `0226` phase note. I read both.
  - Every task in the plan maps to a clause of `0255` § "What must be true after".
  - The rescue's repairs from commit `4d79472` are all carried by the plan:
    - the widened tripwire and the new subject sentence;
    - the open list of how far a repair reaches;
    - the § 5.6 pin timing;
    - the § 5.7 cut of "and complete the rescue anyway", with no further resolution of a failed write.
- **Outside references: OK.**
  - A grep over `src/`, `docs/`, `../orchestrator/orchestrator` and `../orchestrator/docs` finds nothing outside the skill that cites "Diagnosis Report", a depth menu or "Choose repair depth".
  - `orchestrator-artifacts` § "3. Sidecar fields" still finds the closed set.
  - `docs/sakshi-harness/skill-cycle.md` belongs to phase 95, as the spec says.

**Plan-review 1 findings are resolved:**
- **First finding (the word "first").** § 5.7's **Extending the file.** now describes "the section appended once the repair is done, on the user's word", without "first". The plan keeps the closing sentence about a first write that returned no path.
- **Second finding (where Step 3 ends).** Step 3's opening clause becomes "Step 3 makes the first write of the durable report.", so the stop is the step's real end.

**The plan's claims match the file at HEAD:**
- the location of each block it deletes: Step 2's five classes and its severity paragraph, Step 3's paragraphs, Step 4, Step 5's opening and its four option paragraphs, § 5.5 and § "What NOT to do";
- the exact sentences it rewrites in § 5.6 and § 5.7;
- the dependency of the sidecar bullet in Step 1 on `$TARGET_FILE`, which the plan's reorder satisfies;
- the `---` separators left after the deletions.

**The sweep is consistent:**
- The spec's grep leaves exactly the hits the plan allows: the `allowed-tools` line, § 5.6's "routing" if the new sentence keeps it, and "for `roadmap-prune`'s gate to flag".
- The leftover grep (`Diagnosis Report`, `root-cause sentence`, `option [123]`, …) also covers the bold "Write the Diagnosis Report" label and the "inside the Diagnosis Report" phrase in Step 3. Item 2 already names their replacement: "the diagnosis", the same name § 5.7's template uses.

### Critical Issues

None blocking. One low finding, in a sentence this task rewrites.

**1. The reach rewrite carries the case numbers `0024` and `0038` in a form the implementer can copy into the skill body (task "Rewrite the `description:` and the opening paragraphs", "Opening paragraphs" bullet).**

The plan says: rewrite "The repair is depth-keyed …" "so that it lists no closed reach: a repair may go above the task, a phase put in front of it, a phase closed, the task deleted (cases `0024` and `0038` in the phase note)."

Spec `0255` uses the same parenthetical, and there it is attribution: it tells the reader where the reach was seen. In the plan the parenthetical sits right after the after-text draft, inside the same sentence. The Context section also says "the after-texts below are drafts" to be written in the skill's register. An implementer following the draft literally would write `(cases 0024 and 0038 in the phase note)` into `SKILL.md`.

That would break the global rule that product text never cites the plan layer. Those case numbers point to `.ai-factory/` rescue cases listed in phase note `0226`. Today the skill body cites no case or note number; its only `.ai-factory/` path is the report destination, which is mechanism. Such a citation would also go stale at the next prune, while the skill keeps loading it on every run.

*Fix:* in that bullet, mark the parenthetical as the source for the implementer and not as text to write. For example: "a repair may go above the task: a phase put in front of it, a phase closed, the task deleted. The source is cases `0024` and `0038` in the phase note; the skill names no case." Change nothing else in the bullet.

### Positive Notes

- Every non-obvious decision is grounded in the file or the spec, with its reason given in Assumptions:
  - the twin "Describe what…" sentence;
  - the defect-chain wording of the narrative;
  - the "(2+)" qualifier;
  - the three fences that get no new home;
  - the signal pointer, kept only in Step 2.
- Moving the `$TARGET_FILE` resolution ahead of **Capture the report facts.** is done because of a dependency the plan names. Dropping the test-sibling guess follows the spec exactly.
- `## Intended repair` gives the first write a literal place in the template for:
  - the intended repair and rollback;
  - an escalation's options;
  - the answer to question five.

  The finders paragraph now names `## Who found what` by its heading, so "this section" cannot point at the wrong place.
- The intended-rollback assumption ("one of Step 5's four, or that the task's state is left as it is") covers commit-as-is and an unresolved escalation without adding a fifth state. It also matches the shape of the rescue report for this very task.
- The final sweep task includes mechanical checks on the hunks that must not change: the closed-set table, the four rollback states and the one-sentence diff in § 5.6.
