# The editor learns the buffer's place at spawn

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md`'s spawn-moment paragraph has the architect write the editor's handle into the buffer — "At the moment you spawn the editor (see above), write its handle into the buffer, creating the buffer at its existing path if it does not exist yet" — but nothing in that paragraph, or anywhere else in the file, has the architect tell the editor where the buffer itself is.

`src/agents/editor.md` says nothing about a buffer at all — the word never occurs in the file. Its own account of spawn reads: "As the very first action on spawn, before processing the first channel-message, load `architect-editor-engine` via the `Skill` tool — it is the shared channel-message-format contract for this pair and must be resident before you read anything sent to you." Nothing in that account, or anywhere else in the file, gives the editor a buffer's path to hold.

Task 36.1 — "the buffer's definition moves into the engine both halves load" — gives the editor the buffer's *shape*: the two zones, what each holds, the re-read rule, the drain rule, all stated in the engine both halves already load at birth. It does not give the editor the buffer's *path*. A hand that knows the shape of a memory it cannot locate still cannot read it, much less re-read it on change.

## The change

At the moment of spawn, each half learns the other's address, stated symmetrically in both files. `agent-architect` gains the obligation: alongside writing the editor's handle into the buffer, that same spawn moment gives the editor the buffer's path. `editor.md` gains the account of receiving it: at spawn, alongside loading `architect-editor-engine`, the editor holds the buffer's path as part of what it is given — something that happens to it, not something it derives.

The obligation to give the path belongs to the architect, because the architect already controls the spawn moment and already writes into the buffer at that exact point — the same act that names the handle can name the path. The account of receiving it belongs to the editor, because the editor's own file already states what happens to it at spawn, and holding the path is exactly that kind of fact, not a decision the editor makes. Splitting it this way keeps each file stating only what it already governs: the architect's own actions at spawn, the editor's own state at spawn.

## Blast radius

Task 36.1's engine gains no new obligation from this task — the path travels through the spawn moment each file already describes, not through the engine both halves load; the engine continues to state the buffer's shape only.

`architect-pairing-engine` is untouched: nothing about an assigned pairing role changes how or when the path is given.

No new file and no new `loads:` edge — the exchange lands inside the spawn moment each file already has.
