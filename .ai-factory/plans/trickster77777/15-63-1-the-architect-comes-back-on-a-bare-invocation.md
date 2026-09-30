# Plan: 63.1 — the architect comes back on a bare invocation

## Context
`src/skills/agent-architect/SKILL.md` currently decides a start by what the user hands it (a snapshot naming a buffer resumes it), and every snapshot carries the buffer's path. After this task the head recognises its own folder by session id (62.2's nonce probe), a session no folder claims founds a new head without asking, the snapshot no longer carries the buffer's path, and the handle-recovery block (`meta.json` fallback, re-pointing, two-live-buffers) is gone — the liveness probe and dead-editor rule stay. Governing spec: `docs/paired-loop.md` § "Where the memory lives". Task spec: `.ai-factory/specs/trickster77777/176-the-architect-comes-back-on-a-bare-invocation.md` — its "What must be true after" section pins the target wording of every passage below; the implementer copies those pinned passages verbatim from the spec.

Assumption: 62.2 has landed (verified — the file already carries the founding passage with `address.md`, the probe paragraph opening "On every start and every rehydration", and the snapshot clause "Either occasion writes the snapshot into your own folder"). Only this one file changes; the sweep in the spec's "What breaks on contact" confirms `architect-editor-engine`, `src/agents/editor.md`, `docs/` and `CLAUDE.md` stay true as they are and must NOT be edited.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite `agent-architect/SKILL.md`

- [x] **Founding passage recognises the folder by session id**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", first paragraph, replace the text from "Second, the buffer — and which of two starts this is decides what you do:" through the end of the paragraph ("Either way the buffer exists before any editor does.") with the spec's pinned passage, verbatim: the head reads its session id by the probe this section describes, looks under `.ai-factory/architects/` for the folder whose `address.md` holds it on its `session-id:` line; a folder found is yours — work in its `buffer.md`, rebuilding from the buffer and, if the folder holds one, its latest snapshot; no folder found, for whatever reason, means a new head — never ask the user which — and "found your own folder first, at the path and numbering the engine defines: …" continues unchanged to "Either way the buffer exists before any editor does." The phrases "a memory snapshot naming a buffer", "the handoff below that carries your buffer's path" and "never a new one under an old name" disappear. The first half of the paragraph (loading `architect-editor-engine`) and the following probe paragraph ("On every start and every rehydration, new head or resumed, …") stay byte-unchanged. Rewrap lines to the file's existing ~75-column prose width.

- [x] **Snapshot paragraph stops carrying the buffer's path**
  Files: `src/skills/agent-architect/SKILL.md`
  In the paragraph opening "The memory snapshot continuing this same architect has two occasions":
  1. Opening sentence ends at "…whenever the user asks for one mid-session." — delete the dash clause "— no other handoff has any reason to mention the buffer or the handle".
  2. The clause "Either occasion writes the snapshot into your own folder — numbered as `architect-editor-engine` defines — and records your buffer's path and a digest of what the editor has accumulated;" becomes "… numbered as `architect-editor-engine` defines — with a digest of what the editor has accumulated;".
  3. Delete the closing sentence "Of the recorded state, only the buffer's path travels: the pointer, never a copy of the handle or of any assigned pairing role, both of which live in the buffer." so the paragraph closes on "…what goes stale is the next action alone, and the record beside it stays."
  Everything else in the paragraph (the `command-handoff` genre line, digest never sent to the editor, what a snapshot carries, thick/thin, supersession) stays as it reads.

- [x] **Recovery block reduced to the liveness test**
  Files: `src/skills/agent-architect/SKILL.md`
  In the paragraph opening "Continue in the same conversation if the editor is still alive.", keep everything through "recover no handle from a listing, for the same reason." and delete the rest of the paragraph (from "Where you hold no handle at recovery" to "…between `agent-` and `.meta.json`."). Delete the three following paragraphs whole: the one opening "A handle recovered this way came with no buffer pointer of your own", the one opening "The liveness probe is unchanged:", and the one opening "Leaving both buffers live". The dead-editor paragraph ("If the send fails, the editor is dead: …") then follows the shortened liveness paragraph directly, unchanged. Do not touch the spawn/handle-write paragraph ("At the moment you spawn the editor…", including its pairing-role sentences — those belong to 64.1) or the spawn-prompt pointer sentences ("joined at the spawn and only there by the buffer's own path", "give the editor the buffer's path through the spawn prompt").

- [x] **§ "Your buffer is shared; you alone write it" agrees**
  Files: `src/skills/agent-architect/SKILL.md`
  Replace the last sentence of the section's first paragraph — "The memory snapshot continuing you carries this buffer's path alone: of the state recorded there, the pointer, never a copy of the handle or role it holds — see … this section does not restate any of that." — with the spec's pinned sentence verbatim: "The memory snapshot continuing you sits in your folder beside this buffer, and you rebuild from the two together — see "Spawn once, message thereafter" for the rest of what is recorded, when, and the liveness test at recovery; this section does not restate any of that." The rest of the section (including its pairing-role mention in the first sentence — 64.1's scope) stays.

- [x] **§ "On every invocation" agrees**
  Files: `src/skills/agent-architect/SKILL.md`
  Replace the section's body with the spec's pinned text verbatim: "You are re-invoked fresh after every compact and every new session. Read your session id and find your folder, as "Spawn once, message thereafter" has it: a folder found, you rebuild from its `buffer.md` and, if it holds one, its latest snapshot — written before a compact or on the user's request, either one recovers you the same way; no folder found, you are a new head and found one."

### Verify

- [x] **Re-run the spec's sweep** (depends on all tasks above)
  Files: `src/skills/agent-architect/SKILL.md` (read-only check)
  Run the five greps from the spec's "What breaks on contact" over `src/ docs/ CLAUDE.md`. Expected: `meta.json`, `naming a buffer`, `handoff below`, `re-point`, `recovered` no longer match in `agent-architect`; `buffer's path` in `agent-architect` matches only line "it is where your buffer's path and rules are defined" and the spawn sentence "give the editor the buffer's path through the spawn prompt"; the `architect-editor-engine` matches remain and are left untouched. Confirm frontmatter (`description`, `argument-hint`, `allowed-tools`, `loads:`) and the opening paragraph are unchanged. Do not commit.
