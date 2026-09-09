# The buffer exists from the architect's start, not from the editor's spawn

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md:55-56` creates the buffer at one moment only: "At the moment you spawn the editor (see above), write its handle into the buffer, creating the buffer at its existing path if it does not exist yet."

Before that moment, `:32-33` tells the architect the opposite of holding state: "Until the first channel-message arrives, you work alone on the unit named and tell the user you are working alone until it exists." Nothing between those two passages, or anywhere else in the file, instructs the architect to create or hold a buffer before an editor is spawned.

The consequence is unstated but follows from the file's own recovery mechanism: `:47-53` has the pre-compact handoff record "your buffer's path" so a compact can be recovered from. A compact that happens before the first channel-message has no buffer to record a path to — whatever the architect had already decided in that window is lost with nothing for the handoff to point at.

## The change

The architect creates its buffer when it begins, not when it spawns its editor. Writing the editor's handle into the buffer at spawn time stays exactly as `:55-56` already has it — only the creation moment moves earlier, to the architect's own start.

## Blast radius

The buffer's naming and per-architect numbering convention — `.ai-factory/notes/<NN>-architect-buffer.md`, numbered like the other temporary notes so several architects can coexist without colliding (`agent-architect/SKILL.md:232-234`) — does not change.

A handoff continuing the architect across a compact still carries the buffer's path alone, never a copy of its contents (`:47-53`), unaffected by when the file was first created.
