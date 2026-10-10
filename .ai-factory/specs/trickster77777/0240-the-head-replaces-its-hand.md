# 78.3 — the head replaces its hand

## What is true now

`src/skills/agent-architect/SKILL.md`, § "Spawn once, message thereafter", has one spawn and then "every subsequent round goes into the same conversation via `SendMessage` — never a fresh spawn per task", and "If the send fails, the editor is dead"; a fresh hand appears only after a dead one. It names nothing of replacing a live hand.

As 78.1 leaves it, the paragraph that opens "The memory snapshot continuing this same architect has two occasions" ends: "Either occasion writes the snapshot into your own folder — numbered as `architect-editor-engine` defines — with a digest of what the editor has accumulated; the digest is your own recovery note and is never sent to the editor, and for the same reason the snapshot itself is never delegated to the editor to compose — the conversation is the surface a snapshot reports on, and only the head that held it can write what happened there. What a snapshot carries, and how a new one supersedes the last, is the genre `architect-editor-engine` defines; yours reports on the conversation."

§ "Relay on the marker; author the apply work-order and your own legwork" says the `APPLY-EDIT` channel "**never** carries your own analysis of an analysis target — nor, ever, the memory snapshot: composing that file is forbidden to the editor outright, not merely absent from this channel's ordinary cases (see "Spawn once, message thereafter")." § "The user rules the forks and owns the commits" says "The user greenlights each apply work-order and authorizes every commit", with the greenlight unscoped. The same section's Relay neighbour opens: "You author your own prompt in two cases: the **apply work-order**, once the user has confirmed the edits, and a `REPORT-ONLY` round on your own initiative…", so every apply work-order waits on the user's confirmation.

As 78.2 leaves it, the engine makes the head the buffer's only writer and `editor/`, the hand's snapshots, the hand's to write, each opening with the line ``Writer: `<handle>`, relieved <date>.``. `docs/paired-loop.md`, § "How the memory begins, and how it survives", states the replacement: before the hand compacts, in the user's window, as the head's quiet act, with a relieved hand reachable at its handle.

## What must be true after

In `src/skills/agent-architect/SKILL.md`, § "Spawn once, message thereafter", a paragraph reads:

"You replace your hand before it compacts, because a compact loses the pinned values the pair's reliability rests on. The window is the user's decision: from half the hand's context, a firm floor, with no replacement before it, to four fifths, a soft mark, to aim to have replaced it by then and not a line to police; between the two you pick the seam. You ask the hand for its snapshot, which lies in the pair's own folder and needs no greenlight, in an `APPLY-EDIT` message. The replacement is your quiet act and never a topic for the user: no token counts, no forecasts, no asking; name it in one line in passing, like a dead hand."

and the paragraph that opens "The memory snapshot continuing this same architect has two occasions" ends:

"Either occasion writes the snapshot into your own folder — numbered as `architect-editor-engine` defines — and points to the hand's latest snapshot in `editor/`, where what the editor has accumulated is kept. The snapshot is yours to write — the conversation is the surface a snapshot reports on, and only the head that held it can write what happened there — and the hand writes its own. What a snapshot carries, and how a new one supersedes the last, is the genre `architect-editor-engine` defines; yours reports on the conversation."

In § "The user rules the forks and owns the commits", the sentence reads: "The user greenlights each apply work-order on a shared artifact and authorizes every commit".

In § "Relay on the marker; author the apply work-order and your own legwork", the sentence that opens "You author your own prompt in two cases" reads: "You author your own prompt in two cases: the **apply work-order**, once the user has confirmed the edits to a shared artifact, and a `REPORT-ONLY` round on your own initiative…". The ask for the hand's snapshot stays inside the first case, an apply work-order that needs no confirmation, and the two cases stay two.

In the same section, the sentence reads: "…nor, ever, your own memory snapshot: composing that file is forbidden to the editor outright, not merely absent from this channel's ordinary cases (see "Spawn once, message thereafter")."

## What breaks on contact

**Rule:** a text breaks on this change if it has the head keep a digest of what the editor holds, forbids the editor to compose a snapshot without saying whose, or leaves the head's ask for the hand's snapshot waiting on a greenlight.

**Sweep:**
```
grep -rn "digest of what" src docs CLAUDE.md
grep -rn "forbidden to the editor" src docs CLAUDE.md
grep -rn "never delegated" src docs CLAUDE.md
grep -rn "greenlights" src docs CLAUDE.md
grep -rn "has confirmed" src docs CLAUDE.md
grep -rn "fresh spawn" src docs CLAUDE.md
```

**Finding.** The search for `digest of what` returns the snapshot paragraph of `agent-architect`, the target. The search for `forbidden to the editor` returns `agent-architect`'s § "Relay on the marker; author the apply work-order and your own legwork", and the search for `never delegated` returns the snapshot paragraph, each a target. The search for `greenlights` returns `agent-architect`'s § "The user rules the forks and owns the commits", whose sentence "The user greenlights each apply work-order and authorizes every commit" scopes the greenlight to no artifact; it is a target. The search for `has confirmed` returns `agent-architect`'s § "Relay on the marker; author the apply work-order and your own legwork", whose sentence "You author your own prompt in two cases" is a target. The search for `fresh spawn` returns `agent-architect`'s "never a fresh spawn per task", which stays true: a replacement is made at a seam and not per task. No doc, `CLAUDE.md` text or other skill appears in any output.
