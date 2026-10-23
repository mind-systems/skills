# Plan: 90.1 — Lens 3 triggers on the unit that holds the hazard

## Context
In `src/skills/roadmap-decompose-skeleton/SKILL.md`, "Lens 3 — Concurrency" currently fires on "a **heavy** task (the 45–80 min wall-clock kind)" that touches two of three hazard classes. In the field this cut a contract-task over a whole mixed surface, although the hazard lived in one unit of it. After this task the lens fires on the unit that holds the lifecycle hazard together with async I/O or a stateful buffer, and it carries the reason: a red suite written against a skeleton has never run an assertion, so its coverage can only be judged by imagination, which has no floor. The rest of the surface is built with its tests. The wall-clock clause, the "Restraint" bullet and the label "Canon (m37)" go. The drain-and-merge example stays, told whole. The `description:` follows.

The task spec `.ai-factory/specs/trickster77777/0258-lens-3-triggers-on-the-unit-that-holds-the-hazard.md` is authoritative. The phase has no governing spec yet. Its phase note (`.ai-factory/specs/trickster77777/0250-a-contract-task-pays-only-for-the-unit-that-holds-the-hazard.md`) names `docs/names-and-reasons-not-laws.md` as what governs the form: the lens carries a reason, not a rule written ahead of the case. No `.ai-factory/RULES.md` exists.

Assumptions:
- The spec gives no exact after-text. The drafts below follow its "What must be true after" wording and keep the file's hard wrap of about 88 columns. The implementer may re-wrap but must keep the sense.
- The lens now names its trigger exactly (lifecycle plus one of async I/O or a stateful buffer), so the "≥2 of" count goes with the old trigger. All three hazard classes stay listed by their letters.
- Scope boundary with 90.2: § "Load-once / dependencies" (its "restraint" item), Lens 1's "Restraint" bullet, Lens 2's "Canon (m36)", the opening, Step 3 and § "Critical Rules / What NOT to do" (including rule 5, "Do not split simple tasks…") are not touched here. The spec's "What breaks on contact" finding says these hits stay, and 90.2 owns their removal.
- No file outside the skill names the wall-clock clause, "Canon (m37)" or "surfaces mixing". This was checked with `grep -rn -i -E "45.80|Canon \(m37\)|surfaces mixing|wall-clock" docs src README.md AGENTS.md CLAUDE.md`, which returns only the skill's own lines.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit `src/skills/roadmap-decompose-skeleton/SKILL.md`

- [x] **Lens 3 fires on the unit and carries the reason**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In Step 1, replace the whole "Lens 3 — Concurrency" paragraph and its "Restraint" bullet, which ends "…instead of in the field." The new text is two paragraphs with no bullet. Draft:
  > **Lens 3 — Concurrency.** Three hazard classes: (a) async I/O, (b) stateful buffer /
  > event queue, (c) lifecycle (create / deactivate). The lens fires on the **unit** that
  > holds the lifecycle hazard together with async I/O or a stateful buffer. A unit is a
  > part of a task's surface, not the task. For that unit, split out a **contract-task**:
  > invariant definition plus test scenarios per concurrent caller, **no production
  > code**, before the impl task. Cutting the rest of the surface into tasks stays with
  > `roadmap-decompose`'s atomicity, and the rest of the surface is built with its tests.
  >
  > The contract-task has a price. It is a skeleton and a red suite written against it,
  > and none of that suite's assertions has ever run. Whether it covers the next task's
  > wrong implementations can only be judged by imagining them, and imagination has no
  > floor: each review imagines another wrong implementation that would pass. A test
  > that runs has a floor. So the lens pays this price only for the unit where the
  > lifecycle hazard lives. What the price buys: `clearHeap()` traded double-commit for
  > silent loss, and `drainHeap()` plus a dedup-key merge, with buffered winning, fixed
  > it. Had the drain-and-merge invariant been a contract-task first, it would have been
  > caught at plan review instead of in the field.

  Required outcome:
  - The trigger is the unit, not the task or the surface.
  - "heavy", "45–80 min wall-clock", "≥2 of", "Restraint", "never split a simple task" and "Canon (m37)" are gone from Lens 3.
  - The example keeps all three parts: what the first fix traded, what fixed it, and that a contract-task first would have caught it at plan review.

  Leave Lens 1, Lens 2 and Step 2 onward unchanged.

- [x] **The `description:` names the unit**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In the frontmatter `description:`, change only the contract-task clause. It currently reads "and no-prod-code contract tasks for surfaces mixing async I/O + stateful buffer + lifecycle." Change it to:
  > and no-prod-code contract tasks for the unit that holds the lifecycle hazard together with async I/O or a stateful buffer.
  Re-wrap the folded `>-` block to about 80 columns, as it is now. Keep the rest word for word: the opening sentence, "Use when a task is heavy/hazardous or shares a type surface and needs splitting before implementation." and the Trigger list. Check that the description stays at or under 1024 characters, for example with `awk '/^description:/{f=1;next} /^[a-z-]+:/{f=0} f' src/skills/roadmap-decompose-skeleton/SKILL.md | tr -s ' \n' ' ' | wc -c`.

- [x] **Sweep confirms only out-of-scope hits remain** (depends on Lens 3 fires on the unit and carries the reason, The `description:` names the unit)
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Run the spec's sweep: `grep -n -i -E "heavy|surface|simple task|wall-clock|Canon|Restraint" src/skills/roadmap-decompose-skeleton/SKILL.md`.
  - Expected inside Lens 3: the only hits are "surface" in three places. These are the sentence that defines a unit as a part of a task's surface, the "Cutting the rest of the surface" sentence, and "the rest of the surface is built with its tests". The spec requires all three wording points. None of them reads the trigger as the task or as a surface, so keep them. No "heavy", "simple task", "wall-clock", "Canon" or "Restraint" may fall inside Lens 3.
  - Expected in the `description:`: no "surfaces mixing".
  - Hits that may remain outside Lens 3:
    - "heavy/hazardous" and "type surface" in the `description:`.
    - "surface", "hazardous concurrent surface", "heavy or hazardous" and "shared type surfaces" in the opening.
    - "restraint" in § "Load-once / dependencies".
    - Lens 1's "Restraint" bullet.
    - Lens 2's "surface" and "Canon (m36)".
    - Rule 5 of § "Critical Rules / What NOT to do": "blanket-cover surfaces", "loud-failure surfaces", "restraint is first-class", "heavy" and "shared-surface tasks".
  - All of these belong to 90.2 or sit outside Lens 3's trigger. Leave them.
  - Also confirm that `grep -n "wall-clock\|Canon (m37)\|surfaces mixing" src/skills/roadmap-decompose-skeleton/SKILL.md` returns nothing.
