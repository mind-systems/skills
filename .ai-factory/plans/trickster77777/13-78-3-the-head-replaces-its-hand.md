# Plan: 78.3 — the head replaces its hand

## Context
Today `src/skills/agent-architect/SKILL.md` makes a fresh hand only after a dead one. It also keeps "a digest of what the editor has accumulated", and it forbids the editor to compose any snapshot, without saying whose. This change brings the skill in line with the governing spec `docs/paired-loop.md` § "How the memory begins, and how it survives", building on the `editor/` folder that 78.2 put in `architect-editor-engine`. After it:
- The head replaces its live hand before the hand compacts, inside the user's window.
- The head's snapshot points to the hand's latest snapshot in `editor/` instead of carrying a digest.
- The greenlight covers only work-orders on a shared artifact, so asking the hand for its snapshot needs none.
- The prohibition reads of the head's own memory snapshot.

The task spec `.ai-factory/specs/trickster77777/0240-the-head-replaces-its-hand.md` pins every after-text verbatim, under "What must be true after". Copy each one from there byte for byte, keeping the em dashes and the backticks around `APPLY-EDIT`, `editor/` and `architect-editor-engine`. The spec is the one home of the wording, so this plan names each edit by its anchor and does not restate it.

Folder style: `agent-architect`'s body is hard-wrapped prose at about 72–80 columns. Re-wrap only the lines an edit touches. Rewrapping changes no words.

Scope: only `src/skills/agent-architect/SKILL.md` changes. The new hand reading the buffer and its predecessor's snapshot at spawn belongs to 78.4 (`src/agents/editor.md`), not here. The frontmatter description mentions no snapshot, digest or greenlight, so it stays as it is.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### § "Spawn once, message thereafter"

- [x] **Replace the digest with a pointer to the hand's snapshot**
  Files: `src/skills/agent-architect/SKILL.md`
  - Find the paragraph that opens "The memory snapshot continuing this same architect has two occasions".
  - Keep it word for word up to and including "no template is consulted.".
  - Replace everything from "Either occasion writes the snapshot into your own folder" to the end of the paragraph ("…yours reports on the conversation.") with the spec's pinned ending. That ending opens "Either occasion writes the snapshot into your own folder — numbered as `architect-editor-engine` defines — and points to the hand's latest snapshot in `editor/`…" and closes "…yours reports on the conversation.".
  - After the edit, the clauses "with a digest of what the editor has accumulated", "the digest is your own recovery note and is never sent to the editor" and "the snapshot itself is never delegated to the editor to compose" are gone. The paragraph says instead that the snapshot is yours to write and the hand writes its own.

- [x] **Add the replacement paragraph**
  Files: `src/skills/agent-architect/SKILL.md`
  - Insert the spec's pinned paragraph, the one that opens "You replace your hand before it compacts" and closes "…name it in one line in passing, like a dead hand.", as a new paragraph.
  - Put it at the end of the section, directly after the paragraph that opens "If the send fails, the editor is dead" (which closes "…losing it silently is the defect.") and before the heading `## Relay on the marker; author the apply work-order and your own legwork`.
  - Why there: the new paragraph's closing, "like a dead hand", refers back to that death paragraph.
  - Leave "one spawn, then every subsequent round goes into the same conversation via `SendMessage` — never a fresh spawn per task" alone. The spec's finding keeps it true, because a replacement happens at a seam and not once per task.

### § "Relay on the marker; author the apply work-order and your own legwork"

- [x] **Scope the apply work-order's confirmation to a shared artifact**
  Files: `src/skills/agent-architect/SKILL.md`
  - In the sentence that opens "You author your own prompt in two cases", change "once the user has confirmed the edits," to "once the user has confirmed the edits to a shared artifact,", as the spec pins it.
  - The rest of the sentence and the paragraph stay word for word.
  - It still has two cases. Per the spec, asking for the hand's snapshot is an apply work-order that needs no confirmation, not a third case, so add no sentence about it here.

- [x] **Say whose snapshot the editor may not compose**
  Files: `src/skills/agent-architect/SKILL.md`
  - In the paragraph that opens "The two channel-message formats govern what opens a round", change "nor, ever, the memory snapshot: composing that file is forbidden to the editor outright" to "nor, ever, your own memory snapshot: composing that file is forbidden to the editor outright".
  - The rest of the sentence, through "(see "Spawn once, message thereafter").", stays word for word, matching the spec's pinned text.

### § "The user rules the forks and owns the commits"

- [x] **Scope the greenlight to a shared artifact**
  Files: `src/skills/agent-architect/SKILL.md`
  - Change "The user greenlights each apply work-order and authorizes every commit" to "The user greenlights each apply work-order on a shared artifact and authorizes every commit", as the spec pins it.
  - The rest of the paragraph stays word for word.

### Sweep

- [x] **Verify no other text breaks on contact** (depends on all tasks above)
  Files: none (read-only check)
  Run the spec's sweep from the repo root:
  - `grep -rn "digest of what" src docs CLAUDE.md`
  - `grep -rn "forbidden to the editor" src docs CLAUDE.md`
  - `grep -rn "never delegated" src docs CLAUDE.md`
  - `grep -rn "greenlights" src docs CLAUDE.md`
  - `grep -rn "has confirmed" src docs CLAUDE.md`
  - `grep -rn "fresh spawn" src docs CLAUDE.md`

  Expected results after the edits, given as hit counts and locations. The body is hard-wrapped, so a matching line need not hold the whole edited sentence. Never re-flow text to make a grep line match.
  - `digest of what`: no hits.
  - `never delegated`: no hits.
  - `forbidden to the editor`: exactly one hit, in `src/skills/agent-architect/SKILL.md` § "Relay on the marker; author the apply work-order and your own legwork".
  - `greenlights`: exactly one hit, in `src/skills/agent-architect/SKILL.md` § "The user rules the forks and owns the commits".
  - `has confirmed`: exactly one hit, in `src/skills/agent-architect/SKILL.md` § "Relay on the marker; author the apply work-order and your own legwork".
  - `fresh spawn`: exactly one hit, in `src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter". It is "never a fresh spawn per task", which stays.
  - Nothing turns up in `docs/`, `CLAUDE.md` or any other skill.

- [x] **Verify each pinned after-text landed verbatim** (depends on all tasks above)
  Files: none (read-only check)
  For each passage below, read it in `src/skills/agent-architect/SKILL.md` and join its wrapped lines with single spaces. Then compare it with the matching pinned text in the spec, under "What must be true after". Only line breaks may differ; every word, em dash and backtick must match.
  - The replacement paragraph, from "You replace your hand before it compacts" to "…like a dead hand.".
  - The snapshot paragraph's new ending, from "Either occasion writes the snapshot into your own folder" to "…yours reports on the conversation.".
  - The scoped greenlight sentence: "The user greenlights each apply work-order on a shared artifact and authorizes every commit".
  - The scoped confirmation clause: "You author your own prompt in two cases: the **apply work-order**, once the user has confirmed the edits to a shared artifact, and a `REPORT-ONLY` round on your own initiative".
  - The prohibition clause: "nor, ever, your own memory snapshot: composing that file is forbidden to the editor outright, not merely absent from this channel's ordinary cases (see "Spawn once, message thereafter")."

  No file other than `src/skills/agent-architect/SKILL.md` appears changed in `git status`. Do not commit.
