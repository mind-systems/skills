## Plan Review Summary

**Plan:** 90.2 — The skeleton skill drops the text that changes no behaviour
**Files Reviewed:** 1 target (`src/skills/roadmap-decompose-skeleton/SKILL.md`), plus the task spec `.ai-factory/specs/trickster77777/0259-the-skeleton-skill-drops-the-text-that-changes-no-behaviour.md`, the named roadmap line 90.2, and the outside texts that name the skill
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap — OK.** The plan heading matches the 90.2 line in `.ai-factory/roadmaps/trickster77777.md`, and that line's `Spec:` tag resolves to the task spec the plan treats as authoritative. 90.1 is `[x]`, so this task sits at the seam. The phase's own note covers the dead-text removal ("By the user's word the phase also takes off the skill's dead text").
- **Governing spec — WARN (non-blocking).** Phase 90 says "Governing spec: none written yet." The plan states this correctly. Judging therefore stops at the task spec.
- **Architecture — OK.** `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" (load-once, the caller keeps control) is still honoured. Each engine is still loaded once at its point of use, and `loads:` stays as the one home of the edge declaration.
- **Rules — WARN (missing optional file).** `.ai-factory/RULES.md` does not exist, as the plan notes. `.ai-factory/skill-context/aif-review/SKILL.md` also does not exist.

### Verification against ground truth

- **The 90.1 state is confirmed.** In the current file, Lens 3 fires on "the **unit** that holds the lifecycle hazard together with async I/O or a stateful buffer" and carries the price paragraph. The plan's assumption holds, and leaving Lens 3 out of scope is correct.
- **Every removal target exists as described:**
  - § "Load-once / dependencies", from its heading through "…It never reads or modifies the orchestrator."
  - "Do not over-engineer targeting."
  - Step 0's "Never touch closed `- [x]` tasks…"
  - Lens 1's "Restraint" bullet
  - "Canon (m36)" together with "cases 3 and 4"
  - Step 3's orchestrator sentence
  - § "Critical Rules / What NOT to do" with its six rules

  The plan addresses each one by its heading or literal text, never by line number.
- **The spec's sweep will come back empty after the edits.** The Step 0 draft, "Load `roadmap-engine` once via the `Skill` tool", does not match `load-once` because there is no hyphen. "restraint" occurs only in the removed bullet, the removed Load-once list and Critical Rule 5. No other line matches `canon`, `what not`, `never touch` or `neither reads`.
- **Step 0's engine load meets the spec.** It loads `roadmap-engine` at the point where it first needs it (the named-roadmap resolution), and the phrasing mirrors Lens 1 and Lens 2. Step 4's "Ensure `roadmap-engine` is loaded once this chat" is kept, as the spec requires.
- **The Lens 2 draft meets the spec.** It tells the story whole with no label. It drops the case numbers the reader cannot see ("two test cases"). It says what the stateless double let pass and what the stateful double, forced by writing the test against the skeleton first, would have caught.
- **Nothing outside the skill breaks.** I re-ran a wider sweep over `src`, `docs`, `ARCHITECTURE.md` and the root docs. The headings "Load-once / dependencies" and "Critical Rules / What NOT to do" also appear in `roadmap-outline-deep`, `roadmap-decompose`, `roadmap-outline`, `roadmap-test-coverage` and `roadmap-engine`, but each belongs to its own skill. Other mentions of the skill keep their meaning:
  - `docs/philosophy/principles-at-their-moment.md` quotes Lens 1's "apply its question to the target task(s)", and that text stays.
  - `docs/sakshi-harness/skill-cycle.md` says "Сдержанность первого класса: простые задачи проход не трогает". This is still carried by the opening's "most open tasks pass through untouched", which the plan keeps, and it names no removed section.
  - `test-philosophy` and `polymorphism-philosophy` name the skill only as a caller.
- **The frontmatter is unchanged.** `description:` mentions nothing that is removed, so leaving it byte-identical is correct.
- **Settings fit the work.** This is a text-only skill edit with no runtime surface, so "Testing: no" and "Docs: no" are right.

### Critical Issues

None.

### Positive Notes

- Each task cites the exact sentence or heading it removes, and explicitly lists what stays (Targeting's default and single-task reach, Lens 1's extraction, Step 3's deliverability account, Step 4's disposition and numbering). That gives the implementer and the reviewer a precise diff contract.
- The Verify step reuses the spec's own sweep and adds checks that preserve behaviour: Step 0 loads the engine before it uses it, and the frontmatter stays byte-identical.
- The plan records the scope of its outside-reference search and explains why `roadmap-outline-deep`'s matching heading is not a target.

PLAN_REVIEW_PASS
