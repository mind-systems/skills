## Code Review Summary

**Files Reviewed:** 1 target (`src/skills/task-rescue/SKILL.md` at HEAD `4d79472`). I checked it against:
- the plan;
- task spec `0255`;
- contract line 80.3 and the phase 80 header in `.ai-factory/roadmaps/trickster77777.md`;
- the governing spec `docs/names-and-reasons-not-laws.md`;
- `roadmap-engine` § "Named roadmaps";
- `orchestrator-artifacts` § "2. Signals" and § "3. Sidecar fields";
- the rescue report `rescue-reports/skills/10-80-3-each-plan-review-found-one-new-small-thing.md`;
- plan-reviews 1 and 2.

**Risk Level:** 🟢 Low

### Context Gates

- **Architecture: OK.** The plan touches one skill file and changes no `loads:` edge (`orchestrator-artifacts roadmap-engine note` stay). Both load-once paragraphs stay true: the named-roadmap resolution is still used in Step 1, and the signal semantics are still used in Step 2.
- **Rules: WARN (optional file missing).** There is no `.ai-factory/RULES.md` and no `.ai-factory/skill-context/aif-review/SKILL.md`.
- **Roadmap: OK.**
  - Contract line 80.3 links to `0255` through its `Spec:` tag.
  - Phase 80 names `Governing spec: docs/names-and-reasons-not-laws.md`.
  - The Context names the `0226` phase note.
  - Every plan task maps to a clause of `0255` § "What must be true after". The rescue repair in commit `4d79472` covers:
    - the widened tripwire;
    - the new subject sentence;
    - the open reach of a repair;
    - the § 5.6 pin timing;
    - the § 5.7 cut of "and complete the rescue anyway".

    The frame task and the § 5.6 and § 5.7 tasks carry all of it.
- **Outside references: OK.** I grepped `src/`, `docs/`, `../orchestrator/orchestrator`, `../orchestrator/docs` and `../orchestrator/prompts` for "Choose repair depth", "Propagate findings to open", "Diagnosis Report", "depth menu" and "Step 5.5". Outside the skill itself, nothing matches. `orchestrator-artifacts` § "3. Sidecar fields" still finds the closed set in § "Valid sidecar `step` states", which this task leaves untouched.

**The round-2 finding is resolved.** The reach bullet now says the cases `0024` and `0038` are "for the implementer only: the skill names no case and no note number". The skill body therefore cannot pick up a citation to the plan layer.

**I checked the plan's claims against the file at HEAD:**
- **Step 1.**
  - The sidecar bullet says "`$TARGET_FILE` is already resolved above". Moving the resolution ahead of **Capture the report facts.** satisfies it.
  - The phrase "at some repair depths" is in the capture paragraph, and the plan rewords it.
  - The guards of the governing-spec paragraph are the ones the spec drops.
- **Steps 2 and 3.**
  - The five classifications, the severity paragraph, the categories and the special forms are all removed.
  - The plan names every paragraph it deletes or keeps, and each one sits where the plan says it does.
  - The sentence on inconsistent formats stays in Step 3, and the signal pointer stays only in Step 2.
- **Step 4, § 5.5 and § "What NOT to do".** Each deletion range ends on a `---`. Once the range is cut, the separators around it still divide the sections correctly:
  - after Step 5's rollback states;
  - after the test-mode line;
  - after § 5.7.
- **Step 5.** The four paragraphs keyed to options and their separators sit between the rollback states and § "Valid sidecar `step` states". Deleting them leaves the table and the four states byte-identical.
- **§ 5.6 and § 5.7.**
  - The § 5.6 sentence the plan rewrites is quoted exactly.
  - The § 5.7 sentences on "the depth chosen…", "a branch that produces no root cause…" and "complete the rescue anyway" are quoted exactly.
  - The finders paragraph's "this section" / "The section holds" are quoted exactly. Naming `## Who found what` keeps them from pointing at the new `## Intended repair`.
- **`## Intended repair`.** The section's placement and content match the shape of the rescue report the skill produced for this very task. That report carries the intended repair and the rollback (`planned:1`) under that heading, after `## Who found what`, ahead of the dated sections.
- **The sweep.** After the edits, the spec's grep hits only the three allowed places:
  - the `allowed-tools` line;
  - § 5.6's "routing", if the new sentence keeps it;
  - "for `roadmap-prune`'s gate to flag".

  The leftover grep also catches the "Diagnosis Report" label and the phrase "inside the Diagnosis Report" in Step 3. Step 3's item 2 already names their replacement, "the diagnosis".

**Edges I checked that do not need a change:**
- Read with the § 5.6 sentence the plan rewrites, the rest of § 5.6 ("pins each entry … at the moment it disposes of it") stays consistent. Disposal now happens when the repair is applied, so the one-sentence limit the spec sets holds without a contradiction.
- The template keeps **Root cause found by:** after the "no root cause" sentence is deleted. An escalation can still fill it: the root is the undecided decision, and its finder is the escalating role, or "not stated". The deletion is the spec's own, and the template is left without a gap.
- The plan says nothing about a failed first write at the stop. This matches the spec, which explicitly carries no further resolution of a failed first write. Head 09's cut in the rescue report gives the reason.

### Critical Issues

None.

### Positive Notes

- Every decision the spec leaves open is grounded in the file and given its reason under Assumptions:
  - the twin "Describe what…" sentence;
  - the event-neutral wording of the narrative;
  - the "(2+)" qualifier;
  - the fences that get no new home;
  - "first" removed from the appended section.

  None of the after-text drafts is an answer written in advance. Each is a fact, a reason or a question, as the governing spec requires.
- Dropping the test-sibling guess and defining the roadmap in play as "the one whose contract line carries the slug" follows `0255` exactly.
- The intended-rollback assumption ("one of Step 5's four, or that the task's state is left as it is") covers commit-as-is and an unresolved escalation without adding a state. This keeps the closed set and the four rollback states untouched.
- The final task includes mechanical guards on what must not change:
  - the table of valid states;
  - the four rollback states;
  - the single-hunk § 5.6 diff.

PLAN_REVIEW_PASS
