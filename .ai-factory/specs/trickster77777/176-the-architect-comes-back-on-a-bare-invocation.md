# 63.1 — the architect comes back on a bare invocation

## What is true now

This task is sequenced after 62.2, so `src/skills/agent-architect/SKILL.md` is read here as spec 175 leaves it.

§ "Spawn once, message thereafter" decides a start by what the head is handed. The first half of the passage is the file's own; the second half is spec 175's pinned text:

> Second, the buffer — and which of two starts this is decides what you do: a memory snapshot naming a buffer — the handoff below that carries your buffer's path — means you work in that buffer, the same memory resumed, never a new one under an old name; no such pointer means you are a new architect and found your own folder first, at the path and numbering the engine defines: create `buffer.md` in it, seeded in full from `templates/buffer-seed.md` at the moment of its founding — read once, copied whole, never reread for a buffer that is merely resumed — and write `address.md`. Either way the buffer exists before any editor does.

The paragraph spec 175 adds after it, opening "On every start and every rehydration, new head or resumed, `address.md` is made true again.", reads the session id by the nonce probe and ends "and carry on" when the probe does not yield exactly one file.

The snapshot paragraph opens "The memory snapshot continuing this same architect has two occasions: before a compact, and whenever the user asks for one mid-session — no other handoff has any reason to mention the buffer or the handle." It carries spec 175's clause "Either occasion writes the snapshot into your own folder — numbered as `architect-editor-engine` defines — and records your buffer's path and a digest of what the editor has accumulated;", and it closes: "Of the recorded state, only the buffer's path travels: the pointer, never a copy of the handle or of any assigned pairing role, both of which live in the buffer."

The recovery block that follows the spawn's handle-write is built on that pointer. Its first paragraph, opening "Continue in the same conversation if the editor is still alive.", holds the liveness test — the next channel-message is the probe, `ListAgents` is never the signal — and ends "recover no handle from a listing, for the same reason." Its sentence "Where you hold no handle at recovery — never recorded, or recorded into a buffer whose path did not reach you … — fall back to reading `~/.claude/projects/<project-key>/<session-id>/subagents/agent-<id>.meta.json`" belongs to that paragraph. The paragraphs that follow it are these: "A handle recovered this way came with no buffer pointer of your own, so the conditional rule at the top of this section applies unchanged", which carries spec 175's clause "you are a new architect and found your own folder at the path and numbering `architect-editor-engine` defines, exactly as you would with no recovered handle at all" and the re-pointing of the editor to the new buffer; "The liveness probe is unchanged: attempting to send the next channel-message to the recorded handle is still the probe, and the naming rides inside that very message"; and "Leaving both buffers live — your new one and the editor's old one — is not a resolution but the defect itself". The dead-editor paragraph, opening "If the send fails, the editor is dead: this is never a stop and never a question", follows them.

§ "Your buffer is shared; you alone write it" says: "The memory snapshot continuing you carries this buffer's path alone: of the state recorded there, the pointer, never a copy of the handle or role it holds — see "Spawn once, message thereafter" for the rest of what is recorded, when, and the liveness test at recovery; this section does not restate any of that." § "On every invocation" says: "You are re-invoked fresh after every compact and every new session — rebuild your working state from whatever the user hands you and, if one exists, the latest memory snapshot that recorded your buffer's path — written before a compact or on the user's request, either one recovers you the same way."

The frontmatter `description` and `argument-hint`, and the opening paragraph ("this file is the operating discipline you rehydrate into on every invocation, whatever unit of work `$ARGUMENTS` names"), say nothing that recognition by session id makes false.

`docs/paired-loop.md` § "Where the memory lives" has the head read its own session id, find the folder that holds it, and rehydrate from the latest snapshot there, a session no folder claims being a new head. Phase note `172-…` records the measurement behind it: a session's id holds across a compact and across reopening the chat, and an agent reads its own id by a nonce probe.

## What must be true after

The founding passage in § "Spawn once, message thereafter" reads:

> Second, the buffer — and which of two starts this is decides what you do: you read your session id, by the probe this section describes, and look under `.ai-factory/architects/` for the folder whose `address.md` holds it on its `session-id:` line. A folder found is yours: you work in its `buffer.md`, rebuilding from the buffer and, if the folder holds one, its latest snapshot. No folder found, for whatever reason, means you are a new head — you never ask the user which — and you found your own folder first, at the path and numbering the engine defines: create `buffer.md` in it, seeded in full from `templates/buffer-seed.md` at the moment of its founding — read once, copied whole, never reread for a buffer that is merely resumed — and write `address.md`. Either way the buffer exists before any editor does.

The snapshot paragraph opens "The memory snapshot continuing this same architect has two occasions: before a compact, and whenever the user asks for one mid-session." Its clause reads "Either occasion writes the snapshot into your own folder — numbered as `architect-editor-engine` defines — with a digest of what the editor has accumulated;", and the paragraph closes with the sentence on supersession, "…what goes stale is the next action alone, and the record beside it stays." What a snapshot carries otherwise reads as it does.

The recovery block reduces to its first paragraph: "Continue in the same conversation if the editor is still alive. At recovery the only liveness test is the next channel-message itself: …", running to "recover no handle from a listing, for the same reason." The dead-editor paragraph follows it as it stands. The sentence "Where you hold no handle at recovery" and the paragraphs that open "A handle recovered this way", "The liveness probe is unchanged" and "Leaving both buffers live" are gone from the skill.

In § "Your buffer is shared; you alone write it", the last sentence of the first paragraph, which opens "The memory snapshot continuing you carries this buffer's path alone", reads:

> The memory snapshot continuing you sits in your folder beside this buffer, and you rebuild from the two together — see "Spawn once, message thereafter" for the rest of what is recorded, when, and the liveness test at recovery; this section does not restate any of that.

§ "On every invocation" reads:

> You are re-invoked fresh after every compact and every new session. Read your session id and find your folder, as "Spawn once, message thereafter" has it: a folder found, you rebuild from its `buffer.md` and, if it holds one, its latest snapshot — written before a compact or on the user's request, either one recovers you the same way; no folder found, you are a new head and found one.

## What breaks on contact

**Rule:** any file that leans on the recovery block (the `meta.json` fallback, a recovered handle, the editor re-pointed to a new buffer) or on a snapshot naming a buffer reads stale once these passages go — except a record of a past moment (a closed task's spec, plan, plan-review or review, a phase note, a handoff), which documents what was true when it was written.

**Sweep (re-runnable):**
```
grep -rn "meta.json" src/ docs/ CLAUDE.md
grep -rn "naming a buffer" src/ docs/ CLAUDE.md
grep -rn "different buffer" src/ docs/ CLAUDE.md
grep -rn "buffer's path" src/ docs/ CLAUDE.md
grep -rn "recovered\|re-point\|handoff below" src/ docs/ CLAUDE.md
```

**Finding.** The searches for `meta.json` and for `naming a buffer` reach `agent-architect` alone; nothing in `docs/`, `CLAUDE.md`, the engine, `editor.md` or any other skill states the fallback or a snapshot naming a buffer. The third reaches one sentence of `architect-editor-engine`, the editor's re-read rule: "the same rule covers being named a different buffer's path outright by its architect: either way the memory has moved, and the hand adopts what it is now told, replacing what it held, holding one memory at a time." Once the block is gone no passage of `agent-architect` names a different buffer to the editor, and the sentence reads as it does: a rule about what the editor does when told its memory has moved, which also covers an architect whose buffer the user has moved by hand. The fourth reaches the same engine sentence and the engine's sentence on what rides alongside a message ("a fact about where the shared memory sits — that the memory has moved, or the buffer's path itself"), both true with the spawn as the one place the path is handed; `editor.md` carries only "the spawn prompt gives you the buffer's own path", which the spawn still supplies, and no sentence about being named a different buffer. Inside `agent-architect`, the spawn-prompt pointer sentences ("joined at the spawn and only there by the buffer's own path", "give the editor the buffer's path through the spawn prompt") stand; the sentences of the removed block that lean on § "Your buffer is shared; you alone write it" and § "Relay on the marker; author the apply work-order and your own legwork" for the upkeep rule go with it, and both sections keep that rule. The fifth reaches `agent-architect` alone, and only inside the removed block and the founding passage; what stays — the spawn's handle-write, the liveness test and the dead-editor paragraph — speaks of the recorded handle and of the next message as the probe, and none of it points at a removed passage. The removal also takes a mention of an assigned pairing role with it, in the closing sentence of the snapshot paragraph.

**On sequencing against 62.2.** 63.1 rewrites the first half of the founding passage and its join to the second half, and keeps the rest of it — from "found your own folder first" to the end of the passage — as spec 175 pins it; it leans on 62.2's probe paragraph unchanged; and it removes the recovery paragraph that carries 62.2's rewritten clause. So 62.2 lands first.
