# 78.1 — what a snapshot carries lives in the engine

## What is true now

`src/skills/agent-architect/SKILL.md`, § "Spawn once, message thereafter", in the paragraph that opens "The memory snapshot continuing this same architect has two occasions", holds the snapshot's genre. It has the snapshot written into the head's folder "with a digest of what the editor has accumulated", "never delegated to the editor to compose", and says: "What a snapshot carries is the volatile residue — where the work stands, what the hand knows, what will slip first, what must not be resolved by inference — and the reasoning that shaped it: why one option was taken over another, which premise proved false and how, what the user's own correction was and in what words; everything durable already lives outside the conversation, so restating it is never the point, and a snapshot that drops the reasoning is an inventory, not a history. It is thick by default, carrying that reasoning in full; thin only when asked for, or when what is plainly meant is a pointer list for raising context rather than a stretch's history. Each new snapshot supersedes the last by name — the numerically higher-numbered one is the current one — so a reader never follows a stale next action; what goes stale is the next action alone, and the record beside it stays."

`src/skills/architect-editor-engine/SKILL.md`, § "The architect's buffer", names a snapshot only as a file of the folder, "each a `<NN>-<slug>.md` file with a lowercase-hyphenated slug, numbered inside the folder, the highest number being the latest", and holds no genre.

`docs/paired-loop.md`, § "How the memory begins, and how it survives", adds to the reasoning how the knowledge was got: the method of any measurement or analysis, or where it is kept; the shape of what was studied when its source lies outside the reader's reach, a pointer being enough where the source is at hand; and pointers to where the detail lives.

## What must be true after

In `src/skills/architect-editor-engine/SKILL.md`, § "The architect's buffer", a paragraph reads:

"A snapshot continues the memory of one half of the pair, and only whoever held a context can report on it. It carries the volatile residue — where the work stands, what its writer knows, what will slip first, what must not be resolved by inference — and the reasoning that shaped it: why one option was taken over another, which premise proved false and how, what the user's own correction was and in what words; a snapshot that drops the reasoning is an inventory, not a history. It also carries how the knowledge was got: the method of any measurement or analysis, or where that method is kept; the shape of what was studied, when its source lies outside the reader's reach — where the source is at hand, a pointer is enough; and pointers to where the detail lives. A conclusion kept without its method cannot be re-checked or redone. The measure is where a thing lies: the snapshot keeps everything that lies in no file — the user's words, the reasoning, the method, the shape of what was studied — and whatever does lie in a file is replaced by a pointer, since everything durable already lives outside the conversation and restating it is never the point. It is thin only when asked for, or when what is plainly meant is a pointer list for raising context rather than a stretch's history. Each new snapshot supersedes the last by name — the numerically higher-numbered one is the current one — so a reader never follows a stale next action; what goes stale is the next action alone, and the record beside it stays."

In `src/skills/agent-architect/SKILL.md`, § "Spawn once, message thereafter", the paragraph that opens "The memory snapshot continuing this same architect has two occasions" ends:

"Either occasion writes the snapshot into your own folder — numbered as `architect-editor-engine` defines — with a digest of what the editor has accumulated; the digest is your own recovery note and is never sent to the editor, and for the same reason the snapshot itself is never delegated to the editor to compose — the conversation is the surface a snapshot reports on, and only the head that held it can write what happened there. What a snapshot carries, and how a new one supersedes the last, is the genre `architect-editor-engine` defines; yours reports on the conversation."

The paragraph's sentences before "Either occasion" stand as they are.

## What breaks on contact

**Rule:** a text breaks on this change if it states what a snapshot carries, or how one supersedes another, beside the engine's genre.

**Sweep:**
```
grep -rn "volatile residue" src docs CLAUDE.md
grep -rn "supersedes the last" src docs CLAUDE.md
grep -rn "thick by default" src docs CLAUDE.md
```

**Finding.** Each search returns the one paragraph of `agent-architect` that holds the genre, the target; no doc, `CLAUDE.md` text or other skill appears in any output. `command-handoff` names the architect's own snapshot as a different genre from its handoff and states no content, and `agent-architect`'s § "On every invocation" reads the latest snapshot without describing it; each stays true. The engine's frontmatter description names no genre.
