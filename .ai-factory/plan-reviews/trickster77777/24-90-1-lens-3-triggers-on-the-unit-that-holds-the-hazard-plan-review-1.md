## Plan Review Summary

**Plan:** 90.1 — Lens 3 triggers on the unit that holds the hazard
**Files targeted:** 1 (`src/skills/roadmap-decompose-skeleton/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** — OK. The edit stays inside one lens skill. Its `loads:` edges and the engine/lens split are unchanged.
- **Rules** — WARN (non-blocking). `.ai-factory/RULES.md` does not exist, and the plan says so.
- **Roadmap** — OK. The plan's `# Plan:` heading matches contract line 90.1 in `.ai-factory/roadmaps/trickster77777.md`. I read down the chain: the contract line, then task spec `0258-…`, then phase note `0250-…`, then `docs/names-and-reasons-not-laws.md`, which the phase note names as governing the form. The phase header says "Governing spec: none written yet", and the plan reports that correctly. The scope line with 90.2 (task spec `0259-…`) is drawn correctly. 90.2 owns § "Load-once / dependencies", "Do not over-engineer targeting", Step 0's "Never touch closed" sentence, Lens 1's "Restraint", "Canon (m36)", Step 3's orchestrator sentence and § "Critical Rules / What NOT to do". The plan leaves all of them alone.
- **Cross-repo / blast radius** — OK. I re-ran the plan's grep for `45.80|Canon \(m37\)|surfaces mixing|wall-clock` over `docs src README.md AGENTS.md CLAUDE.md`. It hits only the skill's own lines 7, 82 and 88. Two other places mention the skill: `docs/sakshi-harness/skill-cycle.md` ("contract-task для конкурентных зон", and restraint as a rule for the whole skill) and the planning-chain lines in the global and repo CLAUDE.md ("on heavy tasks"). Both describe the whole skill, not Lens 3's trigger. Neither breaks under the spec's "What breaks on contact" rule.

### What the plan gets right
- The Lens 3 draft meets every point of the spec's "What must be true after":
  - The trigger is the unit that holds the lifecycle hazard together with async I/O or a stateful buffer.
  - It says what a unit is.
  - It hands cutting the rest of the surface to `roadmap-decompose`'s atomicity.
  - It states the price (no assertion has ever run, so imagination judges coverage, and imagination has no floor), and that a test that runs has a floor.
  - The drain-and-merge story is told whole, in all three parts.
  - "heavy", the wall-clock clause, "≥2 of", "Restraint" and "Canon (m37)" are gone.
- Dropping "≥2 of" is a sound call. The new trigger is exact (lifecycle plus one of the other two), so a count of classes would contradict it. The plan states this as an assumption.
- The new `description:` measures 515 characters after the change (486 now), well under the 1024 limit. The plan's `awk` check pulls the folded block correctly.
- The draft gives a reason, not a law written ahead of the case, as `names-and-reasons-not-laws` requires.

### Issues

1. **The sweep's expected result contradicts the plan's own draft** (task "Sweep confirms only out-of-scope hits remain").
   - The step says: "Expected: no hit falls inside Lens 3". But the Lens 3 draft in the first task uses "surface" three times:
     - "A unit is a part of a task's **surface**, not the task."
     - "Cutting the rest of the **surface** into tasks…"
     - "the rest of the **surface** is built with its tests"
   - All three are wording the spec requires ("A unit is a part of a task's surface, not a task"; "the rest of the surface is built with its tests").
   - **What goes wrong:** `grep -n -i -E "heavy|surface|simple task|wall-clock|Canon|Restraint"` will return those lines inside Lens 3. The implementer then either reports the check as failed, or "fixes" it by cutting "surface" from the lens. That would delete the unit definition and the "rest of the surface" sentence the spec demands. The reviewer then flags either the failed check or the missing spec wording, and the task burns review rounds.
   - The spec's breakage rule is about meaning, not the word. A text breaks only if it reads Lens 3's trigger *as* the task or a surface. Mentioning the surface the unit is a part of is not that.
   - **Fix:** change the expected result to something like:
     > Expected: inside Lens 3, hits are only "surface" in the sentence defining a unit as a part of a task's surface and in the two "rest of the surface" sentences; none reads the trigger as the task or a surface, and no "heavy", "simple task", "wall-clock", "Canon" or "Restraint" falls inside Lens 3. The `description:` has no "surfaces mixing".

   Also add the 90.2-owned hits the list leaves out, so the implementer has no unlisted hit to puzzle over. All of them are in rule 5 of § "Critical Rules / What NOT to do", which the plan covers only as "rule 5": "blanket-cover surfaces", "loud-failure surfaces", "restraint is first-class", "heavy" and "shared-surface tasks". This is minor; listing them by rule is enough.
