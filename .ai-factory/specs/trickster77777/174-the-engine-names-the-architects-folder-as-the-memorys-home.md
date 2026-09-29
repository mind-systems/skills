# 62.1 — the engine names the architect's folder as the memory's home

## What is true now

`src/skills/architect-editor-engine/SKILL.md` § "The architect's buffer" opens by defining the buffer as a file among the notes:

> The pair shares one working memory: the architect's buffer, a file at `.ai-factory/notes/<NN>-architect-buffer.md`, numbered like the other temporary notes in that directory so that several architects coexist without colliding. This engine is the home of that path and that numbering, and of the rule that governs who may write to it and who may only read; the architect's own skill points here rather than restating them.

Its frontmatter description carries the same definition in one clause: "the definition of the architect's buffer the pair shares: its path and numbering, the rule that the head is its only writer and the hand reads it in full and never writes to it, …". The section's last paragraph leans on the numbering by name: "Several architects coexist under the numbering above, and each keeps its own buffer".

`docs/paired-loop.md` § "Where the memory lives" gives each architect one folder under `.ai-factory/architects/`, holding its buffer, its own snapshots and one keeper of its address, and says a peer reads the keeper and never the buffer. It gives the contents by role and leaves file names and numbering to the skill that implements it.

`CLAUDE.md` describes what `.ai-factory/` holds in its repository tree and in its paragraph on where specs land. The tree reads `├── .ai-factory/                  # Roadmap, specs, notes, handoffs, architecture, plans`, and the paragraph on where specs land ends: "`.ai-factory/handoffs/` holds session handoffs, a separate genre."

## What must be true after

The first paragraph of § "The architect's buffer" reads:

> The pair shares one working memory, and it lives in the architect's own folder, `.ai-factory/architects/<NN>/`; the folder's number is the head's identity. The folder holds `buffer.md`, the buffer itself; `address.md`, the architect's address; and the head's own snapshots, each a `<NN>-<slug>.md` file with a lowercase-hyphenated slug, numbered inside the folder, the highest number being the latest. `address.md` is two lines, `session-id: <id>` and `session-name: <name>` — the id of the session the head runs in, which holds across a compact and a reopened chat, and the name by which a peer reaches that session, which changes when the chat is reopened. A peer reads `address.md` and never the buffer. A new head's folder takes the number one above the highest folder under `.ai-factory/architects/`, and a new snapshot the number one above the highest snapshot in its folder; both start at `01` and are at least two digits wide, so several architects coexist without colliding. This engine is the home of that path and that numbering, and of the rule that governs who may write to the buffer and who may only read; the architect's own skill points here rather than restating them.

The frontmatter description's clause reads "the definition of the architect's folder the pair shares — its buffer, its snapshots and its address file, with their path and numbering — the rule that the head is its only writer and the hand reads it in full and never writes to it, …", and the description stays within the 1024-code-point limit. The section's last paragraph keeps its words: "the numbering above" now resolves to the new first paragraph.

`CLAUDE.md`'s tree line reads `├── .ai-factory/                  # Roadmap, specs, notes, handoffs, architect folders, architecture, plans`, and the paragraph's last sentence reads "`.ai-factory/handoffs/` holds session handoffs, a separate genre; `.ai-factory/architects/` holds one folder per architect, each with its buffer, its snapshots and its address file."

Each architect that already keeps a buffer under `.ai-factory/notes/` is moved into its folder by the user, by hand; the engine defines the folder a head lives in and carries no account of that move.

## What breaks on contact

**Rule:** any file that states where an architect's buffer lives or how architect buffers are numbered reads stale once the engine defines the folder — except a record of a past moment (a closed task's spec, plan, plan-review or review, a phase note, a handoff), which documents what was true when it was written.

**Sweep (re-runnable):**
```
grep -rn "architect-buffer" src/ docs/ CLAUDE.md
grep -rn "and numbering" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches the engine alone: the sentence this task replaces is the only place a buffer's file name is written. The second reaches the engine's own description and, in `agent-architect`, the sentences that point at the engine for the buffer's path and numbering — at the founding, in the recovery passage, and in § "Your buffer is shared; you alone write it". Those sentences point at the engine and restate nothing, so they stay true once the engine defines the folder; wording them for the folder is the next task's. Nothing in `docs/` or `CLAUDE.md` states a buffer's path, and in `CLAUDE.md` the lines above are the ones that list what `.ai-factory/` holds.
