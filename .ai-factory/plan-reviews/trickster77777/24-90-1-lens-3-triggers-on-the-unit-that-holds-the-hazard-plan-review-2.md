## Plan Review Summary

**Plan:** 90.1 — Lens 3 triggers on the unit that holds the hazard
**Files targeted:** 1 (`src/skills/roadmap-decompose-skeleton/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** — OK. The edit stays inside one lens skill. The `loads:` edges and the split between engines and lenses do not change.
- **Rules** — WARN (non-blocking). `.ai-factory/RULES.md` does not exist, and the plan says so.
- **Roadmap** — OK. The plan's `# Plan:` heading matches contract line 90.1 in `.ai-factory/roadmaps/trickster77777.md`. I followed the references down from there:
  - task spec `0258-…`
  - phase note `0250-…`
  - `docs/names-and-reasons-not-laws.md`, which the phase note names as governing the form

  The phase header says "Governing spec: none written yet", and the plan states this correctly. The plan also respects the boundary with 90.2 (task spec `0259-…`). It leaves alone everything 90.2 owns: § "Load-once / dependencies", Lens 1's "Restraint", "Canon (m36)", Step 0, Step 3 and § "Critical Rules / What NOT to do".
- **Cross-repo / blast radius** — OK. I grepped `skills/docs`, `skills/src`, the repo's top-level docs, `orchestrator/docs`, `orchestrator/orchestrator` and `repo-stats-herald/docs` for these strings: `45.80 min`, `Canon (m37)`, `surfaces mixing`, `wall-clock kind` and `contract-task`. The only hit outside the skill is `docs/sakshi-harness/skill-cycle.md` ("contract-task для конкурентных зон"). That line describes the whole skill, not Lens 3's trigger as the task or a surface, so it does not break under the spec's "What breaks on contact" rule.

### Verification of the revised plan
- **The finding from plan review 1 is fixed.**
  - The sweep step now expects three "surface" hits inside Lens 3: the unit definition, "Cutting the rest of the surface", and "the rest of the surface is built with its tests". All three are wording the spec requires.
  - The step forbids "heavy", "simple task", "wall-clock", "Canon" and "Restraint" inside Lens 3.
  - It lists the hits from rule 5 one by one.
- **The out-of-scope list matches the current file.** I ran the spec's sweep on the current file. Every hit outside Lens 3 appears in the plan's list:
  - the description's "heavy/hazardous" and "type surface"
  - in the opening: "surface", "hazardous concurrent surface", "heavy or hazardous" and "shared type surfaces"
  - "restraint" in § "Load-once / dependencies"
  - Lens 1's "Restraint"
  - Lens 2's "surface" and "Canon (m36)"
  - the terms in rule 5

  Nothing is left unlisted.
- **The Lens 3 draft meets each point of the spec's "What must be true after":**
  - The trigger is the unit that holds the lifecycle hazard together with async I/O or a stateful buffer.
  - It defines a unit as a part of a task's surface.
  - It hands the rest of the surface to `roadmap-decompose`'s atomicity.
  - It states the price: no assertion has ever run, coverage is judged by imagination, and imagination has no floor. It also says that a test that runs has a floor.
  - The rest of the surface is built with its tests.
  - The drain-and-merge story keeps all three parts.
  - "Canon (m37)", the "Restraint" bullet, "heavy" and the wall-clock clause are gone.
- **Dropping "≥2 of" is consistent with the spec.** The new trigger names its classes exactly, so a count would contradict it. The plan states this as an assumption.
- **The new `description:` fits the limit.** It measures 514 characters (486 now), under 1024. The plan's `awk` check pulls the folded block correctly; I ran it on the current file and it returned 486.
- **The form follows `names-and-reasons-not-laws`.** The draft gives a reason, not a law written in advance.

### Critical Issues
None.

### Positive Notes
- The assumptions are explicit and can be checked: the wrap width, the removal of "≥2 of", the boundary with 90.2 and the outside-reference grep.
- The required-outcome bullets describe intent, not exact text. The implementer can re-wrap freely while the meaning stays fixed.

PLAN_REVIEW_PASS
