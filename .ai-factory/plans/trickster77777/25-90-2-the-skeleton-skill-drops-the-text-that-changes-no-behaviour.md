# Plan: 90.2 — The skeleton skill drops the text that changes no behaviour

## Context
`src/skills/roadmap-decompose-skeleton/SKILL.md` still holds text that changes no behaviour. Some of it repeats what stands elsewhere: `loads:`, the steps that load each engine, and `polymorphism-philosophy`'s firing condition. Some of it fences against calls that never happen, and some is written for whoever authors the skill. This task removes that text. Every sentence that carries behaviour stays. Lens 2's example is kept as a story told whole, without a label. Step 0 loads `roadmap-engine` at the point where it first needs it.

The task spec `.ai-factory/specs/trickster77777/0259-the-skeleton-skill-drops-the-text-that-changes-no-behaviour.md` is authoritative. The phase (Phase 90) has no governing spec yet ("Governing spec: none written yet"). No `.ai-factory/RULES.md` exists.

Assumptions and checks:
- The skill is in the state 90.1 left it. Lens 3 already fires on the unit and carries the reason. Lens 3's two paragraphs are out of scope and must not change.
- The frontmatter stays unchanged: `description:`, `loads:`, `allowed-tools:`. The spec names none of them. `loads:` is the declaration the removed section restated, so it remains the one home.
- No text outside the skill cites the removed sections, sentences or label. I checked this with `grep -rn -E "m36|PassThroughIndicator|Load-once / dependencies|roadmap-tdd" src docs`. The only hit outside the skill is `roadmap-outline-deep`'s own `## Load-once / dependencies` heading, which belongs to that skill and stays. `test-philosophy` and `polymorphism-philosophy` name `roadmap-decompose-skeleton` only as a caller, and that stays true.
- The spec gives no exact after-text. The drafts below follow its wording and keep the file's hard wrap of about 88 columns. The implementer may re-wrap but must keep the sense.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit `src/skills/roadmap-decompose-skeleton/SKILL.md`

- [x] **Remove § "Load-once / dependencies" and load `roadmap-engine` in Step 0**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Delete the whole `## Load-once / dependencies` section, from its heading through "…It never reads or modifies the orchestrator." The opening paragraph is followed directly by `## Targeting`.
  In Step 0, rewrite the "Read the target roadmap" paragraph so it first loads the engine at the point of use. Mirror the phrasing of Lens 1 and Lens 2 ("Load `…` once via the `Skill` tool, then …"). Drop the closing sentence "Never touch closed `- [x]` tasks — those are `roadmap-prune` / `roadmap-test-coverage` territory." Draft:
  > **Load `roadmap-engine` once via the `Skill` tool, then read the target roadmap**
  > (resolved per its named-roadmap resolution order — argument → "my roadmap" →
  > default `.ai-factory/ROADMAP.md`) and collect its open **`- [ ]`** tasks — this is
  > the set the three lenses run over.
  The `ARCHITECTURE.md` paragraph of Step 0 stays unchanged.

- [x] **Drop "Do not over-engineer targeting."**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In § "Targeting", delete only the final sentence "Do not over-engineer targeting." The default (infer the open-`[ ]` set from context) and the single-task reach stay word for word.

- [x] **Lens 1 loses its "Restraint" bullet; Lens 2's example is told whole without a label**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Lens 1: delete the bullet "- Restraint: contracts/protos are usually laid first anyway — … never on style." The paragraph keeps its load of `polymorphism-philosophy`, its question and what it extracts: interfaces, types and abstract classes, no implementation bodies, the scaffold the TDD lens writes tests against.
  Lens 2: keep the first sentences ("Against the skeleton's public surface, insert a **tests-first task**. Load `test-philosophy` once via the `Skill` tool, then apply its silent-failure discriminator to that surface. Not blanket coverage."). Replace "Canon (m36): a stateless … would have caught it." with the same story told whole and unlabeled. The text must say what the stateless double let pass and what a stateful double, forced by the test against the skeleton, would have caught. Do not use a reference to case numbers the reader cannot see. Draft:
  > A stateless `PassThroughIndicator` double let two test cases pass even though
  > `loadHistory` omitted re-instantiation; a stateful double, which writing the test
  > against the skeleton first would have forced, would have caught it.
  Lens 3 is not touched.

- [x] **Drop Step 3's orchestrator sentence**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In Step 3, delete "The orchestrator does exactly what the spec describes — this skill neither reads nor modifies it." The account of what "deliverable" means stays: a coherent reviewable artifact, a skeleton-only commit that compiles, TDD/contract commits that are red tests.

- [x] **Remove § "Critical Rules / What NOT to do"**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Delete the whole section, heading and its six numbered rules. Step 4's "**Numbering:**" paragraph becomes the end of the file. Step 2 (order and fuse), Step 4's render, its disposition of the original task and its numbering all stay unchanged. This includes Step 4's "Ensure `roadmap-engine` is loaded once this chat", which the spec keeps.

### Verify

- [x] **Run the spec's sweep** (depends on all tasks above)
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Run `grep -n -i -E "load-once|Critical Rules|What NOT|restraint|Canon|over-engineer|never touch|neither reads" src/skills/roadmap-decompose-skeleton/SKILL.md`. It must return nothing. Also confirm the following:
  - `roadmap-engine` is loaded in Step 0 before its named-roadmap resolution is used, and it is still loaded in Step 4.
  - The three lenses' questions, the three hazard classes, Step 2's fuse and exception, Step 3's deliverability and Step 4's render are all unchanged apart from the edits above.
  - The frontmatter is byte-identical.
  - The body stays well under 500 lines.
