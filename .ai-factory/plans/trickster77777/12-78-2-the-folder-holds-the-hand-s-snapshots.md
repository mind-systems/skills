# Plan: 78.2 — the folder holds the hand's snapshots

## Context
`architect-editor-engine` § "The architect's buffer" defines the architect's folder as `buffer.md`, `address.md` and the head's own snapshots. It has no `editor/` and no history of hands. Its body and its frontmatter description also make the head the only writer and say the hand never writes. This change brings the engine in line with the governing spec `docs/paired-loop.md` § "Where the memory lives". The folder also holds `editor/`, the hand's snapshots, numbered on their own. Each of them opens with a `Writer:` line, and `editor/` is the only list of hands. The head writes only the buffer and its own snapshots; `editor/` is the hand's to write.

All three after-texts are pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0239-the-folder-holds-the-hands-snapshots.md`, under "What must be true after". Copy them from there byte-for-byte, keeping the em dashes and the double-backtick span around ``Writer: `<handle>`, relieved <date>.``. The spec is the one home of the wording, so this plan does not restate it.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Engine body

- [x] **Add `editor/` to the folder's definition**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  This edit is in § "The architect's buffer", in the first paragraph, the one that opens "The pair shares one working memory".
  - Find the sentence that opens "The folder holds `buffer.md`, the buffer itself;" and ends "…the highest number being the latest.".
  - Replace that sentence with the spec's first pinned sentence. It ends "…and `editor/`, the hand's snapshots, named and numbered the same way and on their own.".
  - Directly after it, insert the spec's second pinned sentence, the one that opens "Each hand snapshot opens with the line".
  - The rest of the paragraph stays word for word: the `address.md` sentences, the numbering sentence and "This engine is the home of that path…".
  - The paragraph stays one unwrapped line, which is the engine's folder style.

- [x] **Rewrite the writer rule's opening** (depends on Add `editor/` to the folder's definition)
  Files: `src/skills/architect-editor-engine/SKILL.md`
  This edit is in the same section, in the paragraph that currently opens "The head is the memory's only writer.". It comes after the snapshot-genre paragraph that 78.1 added.
  - Replace the whole paragraph with the paragraph pinned in the spec. It opens "The head is the buffer's only writer, as it is of its own snapshots; `editor/` is the hand's to write." and closes "…instead of restating the discipline every time.".
  - The visible changes are three:
    - "memory's only writer" becomes "buffer's only writer…; `editor/` is the hand's to write.".
    - "The hand reads it in full" becomes "The hand reads the buffer in full".
    - "It holds the working discipline" becomes "The buffer holds the working discipline".
  - Every other word stays.
  - Leave the snapshot-genre paragraph and every later paragraph alone: the re-read, the ride-along, the drain rule and the peers rule.

### Engine description

- [x] **Rewrite the writer clause in the frontmatter description**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  - In the `description: >-` block, replace the clause "the rule that the head is its only writer and the hand reads it in full and never writes to it" with the spec's text: "the rule that the head alone writes the buffer and the hand reads it in full and writes only `editor/`".
  - In the file the clause spans the wrapped lines "their path and numbering — the rule that the head is its only writer and the / hand reads it in full and never writes to it, the editor's re-read of the".
  - Re-wrap only the lines that are touched, keeping the block's ~80-column folded style. Leave the rest of the description word for word, including "its buffer, its snapshots and its address file", which the spec's finding keeps.
  - Cap check: the folded description is 1010 characters now. With the new clause it measures 1018, which is under the 1024 cap. Once the edit is done, confirm this by joining the folded lines with single spaces and counting.

### Sweep

- [x] **Verify no other text breaks on contact** (depends on all tasks above)
  Files: none (read-only check)
  Run the spec's sweep:
  - `grep -rn "head's own snapshots" src docs CLAUDE.md`
  - `grep -rn "its snapshots" src docs CLAUDE.md`
  - `grep -rn "your snapshots" src docs CLAUDE.md`
  - `grep -rn "only writer" src docs CLAUDE.md`
  - `grep -rn "never writes to it" src docs CLAUDE.md`

  These hits are expected, and the spec's finding says each one still reads true and stays:
  - The engine's own new sentences.
  - The engine's description, at "its buffer, its snapshots and its address file".
  - The `CLAUDE.md` paragraph on `.ai-factory/`.
  - `agent-architect`'s "your snapshots", "you are their only writer" and "the hand reads the buffer in full and never writes to it".
  - The sentence in `docs/paired-loop.md`.

  No file other than `src/skills/architect-editor-engine/SKILL.md` changes. `src/agents/editor.md` and `agent-architect` are left to 78.3 and 78.4.
