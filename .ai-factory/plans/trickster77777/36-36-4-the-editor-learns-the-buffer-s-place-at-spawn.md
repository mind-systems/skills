# Plan: 36.4 — the editor learns the buffer's place at spawn

## Context
`docs/paired-loop.md` § "How the memory begins, and how it survives" states "Each half holds the other's address. At the moment a hand joins, its own address is recorded in the memory, and the memory's place is given to the hand in turn." Today only one direction exists: `src/skills/agent-architect/SKILL.md` records the editor's handle at spawn but never gives the editor the buffer's path, and `src/agents/editor.md` (post-36.1) names the buffer in its opening appositive but is given no path to it. This task adds the other direction in both files, through the spawn prompt only — the same act that already writes the handle.

Ground truth verified fresh: 36.1 (`4eb7b0c`), 36.2 (`053797a`), and 36.3 (`056cd82`) are committed. `agent-architect` § "Spawn once, message thereafter" holds the sentence "The first channel-message is the spawn — the first `::` relay or, where none has arrived, the first authored apply work-order — and its content *is* the spawn prompt; there is no spawn before one exists." and the paragraph opening "At the moment you spawn the editor (see above), write its handle into the buffer — a write into a file that exists by then, whichever of the two starts above you came through." `editor.md`'s opening paragraph loads `architect-editor-engine` "holding the two channel-message formats and the definition of the architect's buffer, whose settled zone you hold as your own working context from birth". Nowhere in either file does the word "path" reach the editor (`grep -n "path" src/agents/editor.md` returns only the pinned-skill-path sentences, unrelated). `architect-editor-engine` § "The architect's buffer" owns the path and numbering (`.ai-factory/notes/<NN>-architect-buffer.md`) — nothing here restates them.

Assumptions pinned for the implementer:
- The widening attaches to the *spawn act* itself. A respawn after a dead editor is also an `Agent` spawn on a channel-message, so it inherits the widened definition of a spawn prompt without a sentence of its own; the respawn paragraph ("If the send fails, the editor is dead…") is not edited.
- The format token still opens the message (the engine's mode rule keys off it). The path therefore sits *after* the channel-message it accompanies — never before the token, never inside the before-mark payload. The exact wording/position of that trailing line is the implementer's, per the spec.
- Neither file's `description:` enumerates spawn-moment content, so no frontmatter changes. No new `loads:` edge; the engine, `architect-pairing-engine`, and `docs/paired-loop.md` are untouched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The architect gives the path at spawn

- [x] **Widen "its content *is* the spawn prompt" so the spawn prompt also carries the buffer's path**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", rewrite the sentence "The first channel-message is the spawn — the first `::` relay or, where none has arrived, the first authored apply work-order — and its content *is* the spawn prompt; there is no spawn before one exists." so it states, in the file's own voice: the spawn prompt is that first channel-message plus, at the spawn and only there, the buffer's path (the pointer — never a copy of what the buffer holds); the path travels *alongside* the channel-message, never inside the before-mark payload, and carries no reading, no finding, no conclusion — so it is not the enrichment § "Relay on the marker" forecloses; the format token still literally opens the message. Keep "there is no spawn before one exists." Keep the surrounding sentences ("Spawn the editor with `Agent` on that first channel-message and keep it for the whole session…") intact. One to two sentences of growth; the section is loaded on every architect rehydration, so no restatement of what the engine already holds (path form, zones, re-read, drain).

- [x] **Bind the path-giving to the same act that records the handle** (depends on the task above)
  Files: `src/skills/agent-architect/SKILL.md`
  Extend the paragraph opening "At the moment you spawn the editor (see above), write its handle into the buffer — a write into a file that exists by then, whichever of the two starts above you came through." with one clause or sentence stating that in that same act the editor is given the buffer's path — through the spawn prompt, as defined above — so each half holds the other's address from the spawn on; later rounds via `SendMessage` do not repeat it. Do not touch the `name:`-parameter sentence, the pairing-role sentence, or anything after them. Do not edit § "Relay on the marker; author a prompt in exactly one case" (the spec settles that the ban is not reopened; the widened spawn sentence says so itself), § "Your buffer is yours alone", or § "On every invocation". No mention of a task, phase, plan, or `.ai-factory/` path in the skill text.

### The editor receives it

- [x] **Add the account of receiving the path to the editor's spawn paragraph** (depends on the two tasks above for wording symmetry, not for mechanics)
  Files: `src/agents/editor.md`
  In the opening paragraph of "# Editor — the two-mode half of the paired loop", alongside the existing instruction to load `architect-editor-engine` as the very first action on spawn, add the account — stated as something that happens to the editor, not something it derives or looks up — that the spawn prompt gives it the architect's buffer's path alongside the first channel-message, and that it holds that path from birth: it is where the settled zone it already holds "as your own working context from birth" lives. State that the path is not part of the channel-message: the format token still opens the message and decides the mode (the paragraph "Tell which strictly by which of the two format tokens literally opens the message" stays as is and is not contradicted). Keep it to one sentence or a widened clause inside the existing appositive — the file is loaded at every editor spawn. Do **not** add a recovery account, a re-read instruction, the path's literal form or numbering (the engine's), or any reference to the plan layer. `description:`, `tools:`, `model:`, `effort:` and every other section stay untouched.

### Verify both halves state one exchange

- [x] **Confirm symmetry, the untouched files, and the file boundary** (depends on all tasks above)
  Files: `src/skills/agent-architect/SKILL.md`, `src/agents/editor.md`
  Re-read both edited paragraphs in full and confirm they describe the same event from each side: architect gives the buffer's path in the spawn prompt in the act that writes the handle; editor receives and holds it at spawn alongside loading the engine. Run `grep -n "spawn prompt" src/skills/agent-architect/SKILL.md src/agents/editor.md` and confirm the path is named on both sides; run `git diff --stat` and confirm only these two tracked files changed (`src/skills/architect-editor-engine/SKILL.md`, `src/skills/architect-pairing-engine/SKILL.md`, `docs/paired-loop.md` unchanged; the untracked plan/plan-review artifacts under `.ai-factory/` are expected). Confirm `wc -l src/skills/agent-architect/SKILL.md` stays ≤ 500 and that no `loads:` line changed in either file.
