# Plan: 76.1 — the engine puts a head's folder in its user's folder

## Context
`src/skills/architect-editor-engine/SKILL.md`, § "The architect's buffer", is the one home of the head's folder path and its numbering. It still places the folder at the flat `.ai-factory/architects/<NN>/` and numbers a new head above the highest folder under `.ai-factory/architects/`, so all users share one number space. This task rewrites the two sentences that state this, using the after-text pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0230-the-engine-puts-a-heads-folder-in-its-users-folder.md`, § "What must be true after". After the change, the folder sits inside its user's folder and is numbered within it. The governing spec `docs/paired-loop.md` § "Where the memory lives" already describes that layout.

Scope boundary: only these two sentences change, inside the paragraph that opens "The pair shares one working memory". The rest of that paragraph stays exactly as it is: `buffer.md`, `address.md` and its two lines, the snapshot's `<NN>-<slug>.md` (there `<slug>` is a file title, not the user), and the closing "This engine is the home of that path and that numbering…" sentence. The rest of the section also stays, including "Several architects coexist under the numbering above" in the paragraph that opens "Two architects are two heads". Three things are out of scope:
- The peer-address path in `src/skills/agent-architect/SKILL.md` § "Working with another architect" belongs to 76.2.
- The seed's `## Team` placeholder belongs to 76.3.
- The skill's `description:` frontmatter is unchanged, because it names no path.

The `roadmap-engine` slug line that the new sentence leans on already reads as 83.2 left it: "the user's slug is given at session start, as the line `The user's slug: <user-slug>`; a session that holds no such line runs `scripts/user-slug.sh`…". The script `src/skills/roadmap-engine/scripts/user-slug.sh` exists.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The engine's buffer paragraph

- [x] **Rewrite the folder-path sentence to the pinned after-text**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  In § "The architect's buffer", the first paragraph is a single unwrapped line. Its first sentence is currently:
  `The pair shares one working memory, and it lives in the architect's own folder, \`.ai-factory/architects/<NN>/\`; the folder's number is the head's identity.`
  Replace that sentence with this text, verbatim:

  ```
  The pair shares one working memory, and it lives in the architect's own folder, `.ai-factory/architects/<user-slug>/<NN>/`, inside its user's own folder: `<user-slug>` is the user's slug, the one the session holds in the line `The user's slug: <user-slug>` or otherwise takes from running `roadmap-engine`'s `scripts/user-slug.sh`, and the folder's number, counted within that user's folder, is the head's identity there.
  ```

  Keep the paragraph on one line, as it is now; do not wrap it. Match the spec character for character, including the backtick spans, the colon after "inside its user's own folder", and "there" at the end. The next sentence, which starts "The folder holds `buffer.md`…", follows unchanged.

- [x] **Rewrite the numbering sentence to the pinned after-text** (depends on Rewrite the folder-path sentence)
  Files: `src/skills/architect-editor-engine/SKILL.md`
  In the same paragraph, the sentence that starts `A new head's folder takes the number one above the highest folder under \`.ai-factory/architects/\`, …` becomes this text, verbatim:

  ```
  A new head's folder takes the number one above the highest folder under its user's folder, `.ai-factory/architects/<user-slug>/`, and a new snapshot the number one above the highest snapshot in its folder; both start at `01` and are at least two digits wide, so several architects coexist without colliding.
  ```

  Only the phrase "under `.ai-factory/architects/`" changes. It becomes "under its user's folder, `.ai-factory/architects/<user-slug>/`". The rest of the sentence stays as it is. Do not edit any other sentence in the paragraph or the section.

### Contact check

- [x] **Run the spec's breakage sweep** (depends on Rewrite the numbering sentence)
  Files: none (read-only)
  From the repo root, run the two greps the spec names:
  - `grep -rn "architects/<NN>" src docs CLAUDE.md` should now return only `src/skills/agent-architect/SKILL.md` § "Working with another architect" (the peer address that 76.2 changes). Leave it unedited. The engine must no longer appear.
  - `grep -rn "highest folder" src docs CLAUDE.md` should return only the engine's rewritten sentence.
  Also confirm that `grep -n "architects/<user-slug>" src/skills/architect-editor-engine/SKILL.md` returns the paragraph, and that the snapshot's `<NN>-<slug>.md` is still in the engine unchanged.
