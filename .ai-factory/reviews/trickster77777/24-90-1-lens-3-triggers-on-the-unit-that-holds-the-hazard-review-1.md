## Code Review Summary

**Files Reviewed:** 1 (`src/skills/roadmap-decompose-skeleton/SKILL.md`). The other staged files are orchestrator artifacts: the plan, its sidecar and two plan reviews.
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture:** OK. The change stays inside one lens skill. Its `loads:` edges (`roadmap-engine test-philosophy polymorphism-philosophy`) are unchanged, and no engine's contract is touched.
- **Rules:** WARN, non-blocking. `.ai-factory/RULES.md` does not exist. No `.ai-factory/skill-context/aif-review/SKILL.md` exists either.
- **Roadmap:** OK. The diff implements contract line 90.1 in `.ai-factory/roadmaps/trickster77777.md`. I read down the chain: task spec `0258-…`, then phase note `0250-…`, which names `docs/names-and-reasons-not-laws.md` as governing the form. The phase header says "Governing spec: none written yet".
- **Blast radius:** OK. `grep -rn -i -E "Lens 3|wall-clock|surfaces mixing|Canon \(m37\)" docs src` finds nothing outside the skill itself. Nothing else points at the removed trigger, the restraint bullet or the label.

### Conformance to the task spec ("What must be true after")
- **Trigger:** Lens 3 fires on the **unit** that holds the lifecycle hazard together with async I/O or a stateful buffer. It defines a unit as "a part of a task's surface, not the task". The three hazard classes stay listed.
- **Rest of the surface:** Cutting it into tasks stays with `roadmap-decompose`'s atomicity, and it "is built with its tests". This does not conflict with § "Critical Rules / What NOT to do" rule 3, which forbids calling `roadmap-decompose` at runtime. The lens only names where atomicity lives.
- **Removed text:** The "heavy" / 45–80 min wall-clock clause, the "≥2 of" count, the "Restraint" bullet and the label "Canon (m37)" are gone. The plan stated dropping "≥2 of" as an assumption: the exact trigger makes a class count contradictory.
- **The reason:** The lens now carries it. The red suite against a skeleton has never run an assertion, so imagination judges its coverage and has no floor, while a test that runs has a floor. The lens names this as the price of its contract-task.
- **Drain-and-merge example:** It is told whole: what `clearHeap()` traded, what `drainHeap()` plus the dedup-key merge fixed, and that a contract-task first would have caught it at plan review instead of in the field.
- **`description:`:** It names the unit in place of "surfaces mixing". It measures 516 characters, under the 1024 limit. The rest of the field is word for word, and the folded `>-` YAML block stays well-formed.
- **The spec's sweep:** It returns only the expected hits. Inside Lens 3 there are just the three "surface" mentions the spec requires (lines 85, 87, 88). Everything else is in text owned by 90.2 or outside Lens 3's trigger: the opening, § "Load-once / dependencies", Lens 1's "Restraint", Lens 2's "Canon (m36)", and Critical Rule 5.
- **Size:** The body is 155 lines, well under 500.

### Critical Issues
None.

### Positive Notes
- The lens now gives a reason instead of a law written in advance, as `names-and-reasons-not-laws` asks. "Restraint" was a bare prohibition; the price argument lets the decomposer judge cases the author never saw.
- The edit keeps to its scope with 90.2. Neighbouring lenses, Step 2's fuse and the closing rules are untouched, even though the sweep hits them.
- The wrap stays at the file's width of about 88 columns, so the diff is easy to read.

REVIEW_PASS
