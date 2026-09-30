# Plan: 62.1 — the engine names the architect's folder as the memory's home

## Context
`src/skills/architect-editor-engine/SKILL.md` § "The architect's buffer" defines the buffer as a note file at `.ai-factory/notes/<NN>-architect-buffer.md`. This task makes the engine define the architect's own folder, `.ai-factory/architects/<NN>/`, as the home of the memory. The folder holds `buffer.md`, `address.md` and the head's numbered snapshots. The frontmatter description and two lines of `CLAUDE.md` change to match. The task spec is `.ai-factory/specs/trickster77777/174-the-engine-names-the-architects-folder-as-the-memorys-home.md`, and its § "What must be true after" pins every replacement text word for word. The governing spec is `docs/paired-loop.md` § "Where the memory lives". It gives the folder's contents by role and leaves the file names and numbering to this engine.

Ground truth checked before planning:
- In the engine body, the first paragraph of § "The architect's buffer" is one unwrapped line. It starts `The pair shares one working memory: the architect's buffer, a file at` and ends `the architect's own skill points here rather than restating them.`
- The frontmatter `description: >-` is hard-wrapped at about 78–80 characters with a two-space indent. The clause being replaced runs from `the definition of the` (end of one line) through `architect's buffer the pair shares: its path and numbering, the rule that the` (next line).
- With the new clause, the collapsed description is about 867 characters. That is within the 1024 limit.
- The section's last paragraph contains "Several architects coexist under the numbering above". It stays unchanged, and "the numbering above" now resolves to the new first paragraph.
- In `CLAUDE.md`, the tree line reads `├── .ai-factory/                  # Roadmap, specs, notes, handoffs, architecture, plans`. The spec-landing paragraph ends `` `.ai-factory/handoffs/` holds session handoffs, a separate genre. ``
- Sweep per the spec: `grep -rn "architect-buffer\|and numbering" src/ docs/ CLAUDE.md` finds the engine (body and description) and three `agent-architect/SKILL.md` sentences. Those three only point at the engine, so they stay true. Rewording them is task 62.2's work and is out of scope here.

Assumption: each replacement follows the form of the text it replaces. The body paragraph stays one unwrapped line. The description clause is re-wrapped to the description's existing width. Line breaks may change, but the words and punctuation stay exactly as the spec pins them.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The engine defines the folder

- [x] **Replace the first paragraph of § "The architect's buffer"**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  Replace the whole first paragraph of § "The architect's buffer", the single line beginning `The pair shares one working memory: the architect's buffer, a file at`. Use this exact text, kept as one unwrapped line:
  ```
  The pair shares one working memory, and it lives in the architect's own folder, `.ai-factory/architects/<NN>/`; the folder's number is the head's identity. The folder holds `buffer.md`, the buffer itself; `address.md`, the architect's address; and the head's own snapshots, each a `<NN>-<slug>.md` file with a lowercase-hyphenated slug, numbered inside the folder, the highest number being the latest. `address.md` is two lines, `session-id: <id>` and `session-name: <name>` — the id of the session the head runs in, which holds across a compact and a reopened chat, and the name by which a peer reaches that session, which changes when the chat is reopened. A peer reads `address.md` and never the buffer. A new head's folder takes the number one above the highest folder under `.ai-factory/architects/`, and a new snapshot the number one above the highest snapshot in its folder; both start at `01` and are at least two digits wide, so several architects coexist without colliding. This engine is the home of that path and that numbering, and of the rule that governs who may write to the buffer and who may only read; the architect's own skill points here rather than restating them.
  ```
  Leave every other paragraph of the section byte-identical, including the last one ("Several architects coexist under the numbering above…"). Also leave byte-identical the other sections, the H1 title, and the reverse-graph marker sentence. Add no account of moving existing buffers out of `.ai-factory/notes/`. Per the spec, the user does that by hand.

- [x] **Rewrite the frontmatter description's buffer clause** (depends on the paragraph replacement, for consistent wording)
  Files: `src/skills/architect-editor-engine/SKILL.md`
  In `description: >-`, replace the text `the definition of the architect's buffer the pair shares: its path and numbering, the rule that the head is its only writer` with exactly:
  `the definition of the architect's folder the pair shares — its buffer, its snapshots and its address file, with their path and numbering — the rule that the head is its only writer`
  Re-wrap the affected lines to the description's existing width (about 80 characters) and keep the two-space indent. Break lines only between words. Leave every other word of the description unchanged. After the edit, collapse the folded scalar and confirm it stays at or below 1024 characters (expected about 867). Leave the other frontmatter fields (`name`, `user-invocable`, `disable-model-invocation`, `allowed-tools`) untouched.

### CLAUDE.md names the architects' folders

- [x] **Update the `.ai-factory/` tree line and the handoffs sentence**
  Files: `CLAUDE.md`
  1. In the Repository Structure tree, replace the comment on the `.ai-factory/` line. The line becomes exactly:
     `├── .ai-factory/                  # Roadmap, specs, notes, handoffs, architect folders, architecture, plans`
     Keep the existing padding before `#`, so only the comment text changes.
  2. In the paragraph beginning `New task specs land in `.ai-factory/specs/``, replace its last sentence `` `.ai-factory/handoffs/` holds session handoffs, a separate genre. `` with exactly:
     `` `.ai-factory/handoffs/` holds session handoffs, a separate genre; `.ai-factory/architects/` holds one folder per architect, each with its buffer, its snapshots and its address file. ``
  Leave the rest of `CLAUDE.md` unchanged. Do not touch `src/skills/agent-architect/SKILL.md`: its sentences only point at the engine, and wording them for the folder is task 62.2's work.
