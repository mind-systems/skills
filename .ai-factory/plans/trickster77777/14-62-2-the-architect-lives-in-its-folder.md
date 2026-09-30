# Plan: 62.2 — the architect lives in its folder

## Context
`src/skills/agent-architect/SKILL.md` still founds a new head's buffer as a bare file "at the path and numbering the engine defines", keeps no address, and names no destination for a snapshot, while `architect-editor-engine` (62.1, landed) now defines the folder `.ai-factory/architects/<NN>/` holding `buffer.md`, `address.md` and the head's own `<NN>-<slug>.md` snapshots. This task makes the architect's skill live in that folder: it founds the folder, seeds `buffer.md`, writes and refreshes `address.md` (session id by a nonce probe, session name from `ListAgents`), writes snapshots into the folder, and points its recovery passage and buffer section at the folder. Task spec: `.ai-factory/specs/trickster77777/175-the-architect-lives-in-its-folder.md`; governing spec: `docs/paired-loop.md` § "Where the memory lives".

The task spec pins the target wording of every changed sentence verbatim; the implementer reproduces those quotations exactly (re-wrapped to the file's existing ~76-column hard wrap), and changes nothing else. The one file touched is `src/skills/agent-architect/SKILL.md`. `templates/buffer-seed.md` is not edited — its citation of § "Spawn once, message thereafter" still resolves and "the new buffer file" is now `buffer.md`. The handle-recovery block (the `meta.json` fallback, its `<project-key>` definition naming separators only, re-pointing, the two-live-buffers paragraph) and § "On every invocation" stay as they are apart from the one recovery clause below — their removal/rewrite is 63.1's scope.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite agent-architect to live in its folder

- [x] **Frontmatter: add `ListAgents` to `allowed-tools`**
  Files: `src/skills/agent-architect/SKILL.md`
  Replace the frontmatter line `allowed-tools: Read Grep Glob Bash Write Edit AskUserQuestion Agent SendMessage Skill` with exactly `allowed-tools: Read Grep Glob Bash Write Edit AskUserQuestion Agent SendMessage ListAgents Skill`. No other frontmatter field changes (the `description:` stays byte-identical).

- [x] **Founding passage: found the folder, seed `buffer.md`, write `address.md`**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", first paragraph, keep everything up to and including "…means you work in that buffer, the same memory resumed, never a new one under an old name;" unchanged. Replace the remainder of the paragraph — from "no such pointer means you are a new architect and create your own buffer first, …" through "…never reread for a buffer that is merely resumed." — with the task spec's quoted text, verbatim:
  "no such pointer means you are a new architect and found your own folder first, at the path and numbering the engine defines: create `buffer.md` in it, seeded in full from `templates/buffer-seed.md` at the moment of its founding — read once, copied whole, never reread for a buffer that is merely resumed — and write `address.md`. Either way the buffer exists before any editor does."
  (The old separate sentence "A newly created buffer is seeded in full from …" is absorbed into this text and removed; "Either way the buffer exists before any editor does." now closes the paragraph.)

- [x] **New paragraph: `address.md` made true on every start and rehydration** (depends on Founding passage)
  Files: `src/skills/agent-architect/SKILL.md`
  Insert a new paragraph in § "Spawn once, message thereafter" immediately after the founding paragraph and immediately before the paragraph opening "Until the first channel-message arrives". Its text is the task spec's quoted paragraph, verbatim — beginning "On every start and every rehydration, new head or resumed, `address.md` is made true again." and ending "Write both into `address.md`, `session-id: <id>` on the first line and `session-name: <name>` on the second, replacing what was there." It must carry, in the spec's words: the nonce probe over the `.jsonl` files directly under `~/.claude/projects/<project-key>/` with `<project-key>` defined as the working directory's path with every character that is not a letter or a digit replaced by a hyphen; exactly one match → its name without `.jsonl` is the session id; not exactly one → write no session id, leave `address.md` as it was (or unwritten at a founding), mention it in passing, never ask/stop/pick/guess; session name from the first line `ListAgents` returns (`This session is <name> [<ref>] —`), keeping the bare name because `SendMessage` takes it as the address. Do not touch the existing `ListAgents` liveness sentence ("`ListAgents` is never that signal …") — it concerns the editor and stays.

- [x] **Snapshot paragraph: the snapshot goes into the architect's own folder**
  Files: `src/skills/agent-architect/SKILL.md`
  In the snapshot paragraph of § "Spawn once, message thereafter" (the one opening "The memory snapshot continuing this same architect has two occasions"), replace the clause "Either occasion records your buffer's path (defined in `architect-editor-engine`) and a digest of what the editor has accumulated;" with exactly "Either occasion writes the snapshot into your own folder — numbered as `architect-editor-engine` defines — and records your buffer's path and a digest of what the editor has accumulated;". The rest of the paragraph (including "the numerically higher-numbered one is the current one" and "only the buffer's path travels") stays unchanged.

- [x] **Recovery passage: a recovered handle with no pointer founds a folder**
  Files: `src/skills/agent-architect/SKILL.md`
  In the paragraph opening "A handle recovered this way came with no buffer pointer of your own", replace the clause "you are a new architect and create your own buffer at the path and numbering `architect-editor-engine` defines, exactly as you would with no recovered handle at all." with exactly "you are a new architect and found your own folder at the path and numbering `architect-editor-engine` defines, exactly as you would with no recovered handle at all." Nothing else in the recovery block changes (its `meta.json` fallback and `<project-key>` definition stay for 63.1 to remove).

- [x] **§ "Your buffer is shared; you alone write it": closing sentence points at the folder**
  Files: `src/skills/agent-architect/SKILL.md`
  In the last paragraph of that section, replace "The buffer's path and numbering, the rule that the hand reads it in full and never writes to it, the editor's re-read of the memory, and the drain rule are `architect-editor-engine`'s, loaded at birth" with exactly "The folder's path and numbering, what `address.md` holds and who reads it, the rule that the hand reads the buffer in full and never writes to it, the editor's re-read of the memory, and the drain rule are `architect-editor-engine`'s, loaded at birth". Keep "— this section points there and restates none of them." unchanged, but replace the final sentence "It is the one file you edit directly: you are its only writer." — which the new text makes false, since the head now also writes `address.md` itself (at a founding before any editor exists, and on every start and rehydration) and writes its own snapshots into the folder (never delegated to the editor) — with exactly: "The buffer, `address.md` and your snapshots — your own folder — are the only files you edit directly: you are their only writer." The task spec pins the sentence only up to "loaded at birth", so this tail is inside the task's boundary; it keeps the head as the buffer's only writer (`docs/paired-loop.md`: the head is the memory's only writer) and stops claiming the buffer is its only direct write.

- [x] **Confirm headings and neighbours hold** (depends on all above)
  Files: `src/skills/agent-architect/SKILL.md`, `src/skills/agent-architect/templates/buffer-seed.md`
  Every `##` heading of the skill keeps its exact words (so the seed's citation of "Spawn once, message thereafter" and the skill's internal cross-references resolve). Re-run the task spec's sweep (`grep -rn "create your own buffer" src/ docs/ CLAUDE.md` must now return nothing; `grep -rn "AskUserQuestion Agent SendMessage" src/ docs/ CLAUDE.md` must reach only the updated frontmatter line). Leave `buffer-seed.md`, `command-handoff`, `roadmap-prune`, `docs/`, and `CLAUDE.md` untouched. Do not commit.
