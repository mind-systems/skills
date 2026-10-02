# 42.1 — the always-loaded rule separates a number assigned once from a heading's ordinal

## What is true now

`src/global/CLAUDE.md` § "Grounding claims" holds this sentence in its paragraph on addressing by name: "A heading, a bolded rule, a symbol, a numbered item survives every insertion above it; a line number survives none, and nothing reports it when it rots." The sentence after it begins "A `file:line` is a defect report against its target". The text wraps in the file at a fixed column.

`docs/reference-by-name.md` § "Granularity, not size" draws the line the sentence lacks: "A number holds only where it is assigned once and split, never shifted, when something is inserted: a task's `N.M`, a skill's step, which splits like a task number. A heading's ordinal is a position, like a line number, so a section of a document is cited by its heading's text." The always-loaded sentence lists a numbered item with no such distinction.

## What must be true after

The sentence reads: "A heading, a bolded rule, a symbol survives every insertion above it, and so does a number assigned once and split rather than shifted — a task's `N.M`, a skill's step. A line number survives none, and nothing reports it when it rots; a heading's ordinal is the same kind of position, so a document's section is cited by its heading's text."

## What breaks on contact

**Rule:** a text breaks on this change if it restates the list of what survives an insertion, or states a rule about citing a section by its number.

**Sweep:**
```
grep -rn "numbered item" src/ docs/ CLAUDE.md
grep -rn "survives every insertion" src/ docs/ CLAUDE.md
grep -rn "unique string" src/ docs/ CLAUDE.md
```

**Finding.** The global file is read in every session of every project: `~/.claude/CLAUDE.md` links to `active/CLAUDE.md`, which links to `src/global/CLAUDE.md`, so the new sentence reaches each session at its next start. The first search reaches that sentence, the task's own target, and the project `CLAUDE.md` row for `docs/reference-by-name.md`, which describes the document's units of naming as "(a heading, a bold lead-in, a numbered item — anything that will be depended on)"; the row states the old list in compressed form and does not contradict the new sentence. The second reaches the global sentence alone. The third reaches the anchor list in `agent-architect`, "a heading, a bolded rule, a symbol, a unique string — never a position": a different list for a different purpose, the anchors a match is asserted against, and it agrees with the new sentence. `docs/reference-by-name.md` no longer carries the old list, since it states the distinction itself, and no other skill, command or doc lists what survives an insertion.
