# The buffer exists from the architect's start, not from the editor's spawn

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md`'s spawn-moment paragraph, in § "Spawn once, message thereafter," is the one place the buffer comes into being, and it happens as a side effect of a different act: "At the moment you spawn the editor (see above), write its handle into the buffer, creating the buffer at its existing path if it does not exist yet." Before that paragraph, the same section's opening line tells the architect the opposite of holding state: "Until the first channel-message arrives, you work alone on the unit named and tell the user you are working alone until it exists."

Nothing between those two passages, or anywhere else in the file, distinguishes an architect that begins from a memory snapshot naming a buffer from an architect that begins with no such pointer at all — both paths run into the same spawn-moment clause, and the clause treats them alike, creating a buffer exactly when the editor is spawned regardless of which path led there.

## The change

The buffer's creation becomes its own moment, at the architect's own start, and conditional rather than unconditional. A memory snapshot naming a buffer means the architect works in that buffer — no new one is created. No such pointer means the architect creates one, before any editor exists — the buffer's creation moves ahead of the spawn-moment paragraph rather than living inside it.

Recording the editor's handle stays exactly where the spawn-moment paragraph already puts it: a write into a buffer that by then already exists, whichever of the two paths produced it.

## Blast radius

36.1 moves the buffer's shape and its naming convention into the engine both halves load; this task must not restate either.

The existing fallback that recovers the editor's handle from session metadata, used when no handle was ever recorded, is untouched.

Two further places in the file read as "the buffer may not exist yet," worth naming rather than left silent: the spawn-moment paragraph's own "if it does not exist yet," which this task's rewrite absorbs into the conditional; and the invocation-time instruction to rebuild working state from whatever the user hands over "and, if one exists, the pre-compact handoff that recorded your buffer's path" — a second place where the file already anticipates an architect that starts with nothing recorded, consistent with the conditional this task states rather than in tension with it.
