# 62.2 — the architect lives in its folder

## What is true now

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" decides a start by what the head is handed, and founds a buffer at the engine's path:

> Second, the buffer — and which of two starts this is decides what you do: a memory snapshot naming a buffer — the handoff below that carries your buffer's path — means you work in that buffer, the same memory resumed, never a new one under an old name; no such pointer means you are a new architect and create your own buffer first, at the path and numbering the engine defines. Either way the buffer exists before any editor does. A newly created buffer is seeded in full from `templates/buffer-seed.md` at the moment of its founding — read once, copied whole, never reread for a buffer that is merely resumed.

The snapshot paragraph says "Either occasion records your buffer's path (defined in `architect-editor-engine`) and a digest of what the editor has accumulated" and that "the numerically higher-numbered one is the current one"; the skill states no destination for a snapshot, and the snapshot files that exist sit under `.ai-factory/handoffs/`. The recovery passage sends a recovered handle that came with no buffer pointer down the same new-architect start: "you are a new architect and create your own buffer at the path and numbering `architect-editor-engine` defines, exactly as you would with no recovered handle at all." § "Your buffer is shared; you alone write it" closes by pointing at the engine: "The buffer's path and numbering, the rule that the hand reads it in full and never writes to it, the editor's re-read of the memory, and the drain rule are `architect-editor-engine`'s, loaded at birth".

The skill names no address file and no way for a head to read its own session. Its frontmatter reads `allowed-tools: Read Grep Glob Bash Write Edit AskUserQuestion Agent SendMessage Skill`, with no `ListAgents`, and its one mention of `ListAgents` concerns the editor's liveness ("`ListAgents` is never that signal"), and its recovery passage already defines `<project-key>` as "the working directory's path with separators replaced by hyphens". The directory Claude Code actually stores transcripts under replaces every character of the path that is not a letter or a digit with a hyphen, not only the separators: `/Users/max/projects/mind/mind_api` is stored as `-Users-max-projects-mind-mind-api`. Each session's own transcript is a `.jsonl` file directly in that directory, named by the session id, while the transcripts of an editor or any other subagent sit one level down, under `<session-id>/subagents/`. A probe of this kind has been run in this repository: a nonce echoed, then a `grep -l` of it over `~/.claude/projects/<project-key>/*.jsonl`, returned exactly one file, the session's own. `templates/buffer-seed.md` opens by saying it is read once by the "Spawn once, message thereafter" step when a new buffer is created and copied whole into the new buffer file.

## What must be true after

The founding passage in § "Spawn once, message thereafter" keeps its two starts — a memory snapshot naming a buffer means that memory resumes, no such pointer means a new head — and its second half reads:

> no such pointer means you are a new architect and found your own folder first, at the path and numbering the engine defines: create `buffer.md` in it, seeded in full from `templates/buffer-seed.md` at the moment of its founding — read once, copied whole, never reread for a buffer that is merely resumed — and write `address.md`. Either way the buffer exists before any editor does.

The same section carries this paragraph, after the founding passage and before the paragraph that opens "Until the first channel-message arrives":

> On every start and every rehydration, new head or resumed, `address.md` is made true again. Read your session id by running a command that prints a random nonce, then searching the project's transcripts — the `.jsonl` files directly under `~/.claude/projects/<project-key>/`, `<project-key>` being the working directory's path with every character that is not a letter or a digit replaced by a hyphen — for the printed nonce: exactly one file matches, and its name without `.jsonl` is your session id. When the probe does not yield exactly one file, write no session id and carry on: leave `address.md` as it was, or unwritten at a founding, and mention in passing that you could not read your session id; never ask, never stop, never pick one file and never guess. Read your session name from the first line `ListAgents` returns, which opens `This session is <name> [<ref>] —`, and keep the bare name — the token after `This session is`, up to any bracketed ref that follows it — because `SendMessage` takes the bare name as the address and a ref that was not just read from a listing does not resolve. Write both into `address.md`, `session-id: <id>` on the first line and `session-name: <name>` on the second, replacing what was there.

The snapshot paragraph's clause reads "Either occasion writes the snapshot into your own folder — numbered as `architect-editor-engine` defines — and records your buffer's path and a digest of what the editor has accumulated;". The recovery passage's clause reads "you are a new architect and found your own folder at the path and numbering `architect-editor-engine` defines, exactly as you would with no recovered handle at all." § "Your buffer is shared; you alone write it" closes: "The folder's path and numbering, what `address.md` holds and who reads it, the rule that the hand reads the buffer in full and never writes to it, the editor's re-read of the memory, and the drain rule are `architect-editor-engine`'s, loaded at birth".

The frontmatter line reads `allowed-tools: Read Grep Glob Bash Write Edit AskUserQuestion Agent SendMessage ListAgents Skill`, since the head now calls `ListAgents` to read its own session name.

Every heading of the skill keeps its words, so the seed's citation of § "Spawn once, message thereafter" still resolves, and the seed's statement that it is copied whole into the new buffer file holds with `buffer.md` as that file.

Each architect that already keeps a buffer under `.ai-factory/notes/` is moved into its folder by the user, by hand; the skill describes the folder a head lives in and carries no account of that move.

## What breaks on contact

**Rule:** any file that states where a new architect's memory is founded, where a snapshot is written, or how an architect learns its own session reads stale once these passages change; a citation of a section heading depends on that heading resolving.

**Sweep (re-runnable):**
```
grep -rn "create your own buffer" src/ docs/ CLAUDE.md
grep -rn "Spawn once" src/ docs/ CLAUDE.md
grep -rn "handoffs/" src/ docs/ CLAUDE.md
grep -rn "AskUserQuestion Agent SendMessage" src/ docs/ CLAUDE.md
grep -rn "project-key" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches only the sentences of `agent-architect` this task rewrites, in the founding passage and the recovery passage. The second reaches the seed's opening, which cites the heading as the step that reads it, and the skill's own cross-references to that heading; the heading stays and each sentence stays true. The third reaches `command-handoff` and `roadmap-prune`, which describe the folder for handoffs written for whoever comes next, and `docs/sakshi-harness/skill-graph.md`, which speaks of the same folder as a destination of `note`, and `CLAUDE.md`'s sentence on that folder, which the engine task rewrites; none of them says where a memory snapshot goes, so none is falsified by a snapshot landing in the architect's folder. No file under `src/`, `docs/` or `CLAUDE.md` states a snapshot's destination today. The skill's existing `ListAgents` sentence concerns the editor's liveness and the new reading concerns the architect's own session name, so the old sentence and the new reading do not meet. The fourth search reaches the skill's own frontmatter line alone; nothing in `src/`, `docs/` or `CLAUDE.md` mirrors it. The fifth reaches the recovery passage's own `<project-key>` definition, which names separators only and belongs to the handle fallback that the recovery task removes, and nothing else; the probe paragraph carries the definition it needs in its own words.

**On sequencing against 62.1.** Once the engine task lands, `architect-editor-engine` defines the folder `.ai-factory/architects/<NN>/`, holding `buffer.md`, `address.md` (`session-id: <id>` and `session-name: <name>`) and the head's own `<NN>-<slug>.md` snapshots, with the numbering of folders and snapshots. The founding passage points at that definition for the folder's path and numbering, and the snapshot clause for snapshot numbering, so the engine's text exists before this task's text refers to it. The engine task stands alone: `agent-architect`'s existing sentences already point at the engine for the path and numbering.
