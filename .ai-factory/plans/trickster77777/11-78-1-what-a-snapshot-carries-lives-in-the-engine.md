# Plan: 78.1 — what a snapshot carries lives in the engine

## Context
The snapshot's genre (what a snapshot carries, how it supersedes the last) moves from `agent-architect` § "Spawn once, message thereafter" into `architect-editor-engine` § "The architect's buffer" as one paragraph, enriched with `docs/paired-loop.md` § "How the memory begins, and how it survives" (governing spec of phase 78) — how the knowledge was got — and with "thick by default" replaced by the measure "what lies in no file is kept, what lies in a file becomes a pointer". `agent-architect` keeps its two occasions and the conversation as the head's subject and points to the engine. Both after-texts are pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0238-what-a-snapshot-carries-lives-in-the-engine.md`; copy them from there byte-for-byte (the spec is the home of the wording — this plan does not restate it).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Engine takes the genre

- [x] **Add the snapshot-genre paragraph to the engine**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  In § "The architect's buffer", insert the paragraph pinned in the task spec under "What must be true after" (it opens "A snapshot continues the memory of one half of the pair, and only whoever held a context can report on it." and closes "…what goes stale is the next action alone, and the record beside it stays.") as a new paragraph directly after the section's first paragraph (the one defining the folder, `buffer.md`, `address.md`, the snapshot files and their numbering, ending "…the architect's own skill points here rather than restating them.") and before the paragraph opening "The head is the memory's only writer." — the genre sits beside the definition of the snapshot files it describes. Follow the engine's folder style: each paragraph is one unwrapped line, separated by blank lines. Copy the text verbatim from the spec, em dashes included. No other paragraph of the engine, and not its frontmatter `description:` (the spec's sweep finds it names no genre), is touched.

### The lens points to the engine

- [x] **Rewrite the tail of the occasions paragraph in `agent-architect`** (depends on Add the snapshot-genre paragraph to the engine)
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", in the paragraph that opens "The memory snapshot continuing this same architect has two occasions", replace everything from "Either occasion writes the snapshot into your own folder —" through the paragraph's end ("…and the record beside it stays.") with the ending pinned in the task spec (opens "Either occasion writes the snapshot into your own folder — numbered as `architect-editor-engine` defines —" and closes "What a snapshot carries, and how a new one supersedes the last, is the genre `architect-editor-engine` defines; yours reports on the conversation."). This removes the "What a snapshot carries is the volatile residue …", "It is thick by default …" and "Each new snapshot supersedes the last by name …" sentences from this skill. The paragraph's sentences before "Either occasion" stand word-for-word as they are. Keep the file's hard-wrapped style (~72-char lines); re-wrap only the lines of the replaced tail (the current odd break after "into your own folder —" may be smoothed as part of that re-wrap). Nothing else in the skill changes.

### Sweep

- [x] **Verify no second home of the genre remains** (depends on both tasks above)
  Files: none (read-only check)
  Run the spec's sweep: `grep -rn "volatile residue" src docs CLAUDE.md`, `grep -rn "supersedes the last" src docs CLAUDE.md`, `grep -rn "thick by default" src docs CLAUDE.md`. Expected after the change: "volatile residue" hits only `src/skills/architect-editor-engine/SKILL.md` (the new paragraph); "supersedes the last" hits the engine's new paragraph and the pointer sentence in `agent-architect` ("how a new one supersedes the last, is the genre `architect-editor-engine` defines") — a pointer, not a restatement — and nothing else; "thick by default" returns nothing. `docs/paired-loop.md`, `command-handoff` and `agent-architect` § "On every invocation" stay untouched, per the spec's finding.
