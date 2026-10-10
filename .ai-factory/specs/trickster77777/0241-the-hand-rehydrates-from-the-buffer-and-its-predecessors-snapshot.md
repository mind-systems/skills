# 78.4 — the hand rehydrates from the buffer and its predecessor's snapshot

## What is true now

`src/agents/editor.md` says the editor is "born fresh into this role at every spawn", loads `architect-editor-engine` first, and holds the buffer "as your own working context from birth"; the spawn prompt "gives you the buffer's own path". It names no snapshot, so a hand starts from the buffer alone. Of the hand's own memory it says: "You carry history across rounds — what's been done, where past rounds went wrong — and it sharpens you; you're expected to notice what the architect missed. But never depend on it: every round is self-contained by contract, and a fresh editor picking up from the next round alone must succeed just the same."

As 78.1 and 78.2 leave it, the engine's § "The architect's buffer" holds the snapshot genre and `editor/`, the hand's snapshots in the architect's folder beside `buffer.md`, the highest number being the latest. As 78.3 leaves it, `agent-architect` has the head replace its hand and ask it for its snapshot in an `APPLY-EDIT` message; the new hand is spawned by the skill's existing rule, whose spawn prompt carries the buffer's path and nothing else, so no text has the head name a snapshot to the new hand.

## What must be true after

In `src/agents/editor.md`, directly after the paragraph that ends "and it is where that memory lives.", a paragraph reads:

"Before your first round, with the engine loaded, read the buffer whole and, beside it, the latest snapshot in the `editor/` of its folder where one exists, and take that snapshot as your own memory. The buffer's path is all your spawn gives you; the snapshot lies in the same folder, and you read it the same after a replacement and after a death."

## What breaks on contact

**Rule:** a text breaks on this change if it leaves a hand to start from the buffer alone while a snapshot lies beside it, or has the head name that snapshot to the hand at its spawn.

**Sweep:**
```
grep -rn "buffer's own path" src docs CLAUDE.md
grep -rn "spawn prompt" src docs CLAUDE.md
grep -rn "born fresh" src docs CLAUDE.md
```

**Finding.** The search for `buffer's own path` returns `src/agents/editor.md`, the target, and `agent-architect`'s account of the spawn, where the prompt is "joined at the spawn and only there by the buffer's own path", which stays true: the head names nothing more. The search for `spawn prompt` returns `src/agents/editor.md`, the target, and two sites in `agent-architect`, the spawn's content and "the buffer's path through the spawn prompt", each reading true of a path alone. The search for `born fresh` returns `src/agents/editor.md` alone; "born fresh" stays true of a successor, which is spawned fresh and starts from the snapshot.
