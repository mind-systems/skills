# 90.2 — the skeleton skill drops the text that changes no behaviour

## What is true now

The skill is as 90.1 leaves it, in everything 90.1 changes.

`src/skills/roadmap-decompose-skeleton/SKILL.md` holds, beside its behaviour, text that restates what stands elsewhere or fences against what does not happen:
- § "Load-once / dependencies" says the skill "owns no reusable body of its own — only the three lenses below" and follows with a list of six; says each shared skill is loaded once per chat and never re-invoked per task, which Lens 1, Lens 2 and Step 4 each say where they load one and the frontmatter's `loads:` declares; gives each shared skill's role, which the step that uses it states; and says the skill "does **not** call `roadmap-decompose` at runtime" and "never reads or modifies the orchestrator". The section sits above Step 0, which uses `roadmap-engine`'s named-roadmap resolution, and no other text above Step 0 loads the engine.
- § "Targeting" ends "Do not over-engineer targeting."
- Step 0 ends "Never touch closed `- [x]` tasks — those are `roadmap-prune` / `roadmap-test-coverage` territory", after saying the open tasks are the set the lenses run over.
- Lens 1 ends in a bullet headed "Restraint": "contracts/protos are usually laid first anyway — do not blanket-cover tasks with abstract classes. The question is the gate; it fires only on the event, never on style." `polymorphism-philosophy` states the second half as its own firing condition.
- Lens 2 tells an example under the label "Canon (m36)": a stateless `PassThroughIndicator` double let two cases pass although `loadHistory` omitted re-instantiation, which a stateful double, forced by writing the test against the skeleton first, would have caught.
- Step 3 ends "The orchestrator does exactly what the spec describes — this skill neither reads nor modifies it."
- § "Critical Rules / What NOT to do" lists six: no `roadmap-tdd` middle skill; do not copy `roadmap-engine`'s render machinery or `test-philosophy`'s discriminator into the skill; do not call `roadmap-decompose`; do not read or modify the orchestrator; do not split simple tasks, blanket-cover surfaces or test loud-failure surfaces; do not touch closed tasks. The first two are rules for whoever authors the skill, the third, fourth and sixth copy sentences above, and the fifth repeats the restraint and the opening's reach.

## What must be true after

Each text named above goes, and the skill keeps every sentence that carries behaviour: the lenses' questions and what each extracts, the hazard classes, Step 2's order and fuse, Step 3's account of what deliverable means, Step 4's render mechanics and numbering, the opening's reach, Targeting's default and single-task reach, and Step 0's open set.

Lens 2's example stays as a story told whole, with no label: what the stateless double let pass and what a stateful double, forced by the test against the skeleton, would have caught.

Step 0 loads `roadmap-engine` where it first needs it, the way Lens 1 and Lens 2 load theirs at the point of use, since § "Load-once / dependencies" sits above Step 0 and is where a top-down reader loads the engine today, and `loads:` is a declaration the harness does not execute. Step 4's "Ensure `roadmap-engine` is loaded once this chat" stays.

## What breaks on contact

**Rule:** a text breaks on this change if it points at a removed section, sentence or label, or counts the lenses by a list that no longer exists.

**Sweep:**
```
grep -n -i -E "load-once|Critical Rules|What NOT|restraint|Canon|over-engineer|never touch|neither reads" src/skills/roadmap-decompose-skeleton/SKILL.md
```

**Finding.** The search returns the sections and sentences named above; each is a target. No text outside the skill cites one of them by name: the same headings in other skills are those skills' own. Step 0 uses `roadmap-engine`'s named-roadmap resolution, and § "Load-once / dependencies", above it, is where the engine is loaded today; once the section goes, Step 0's own load, stated above, is the instruction a top-down reader meets.
