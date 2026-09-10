# The editor learns the buffer's place at spawn

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md`'s spawn-moment paragraph has the architect write the editor's handle into the buffer — "At the moment you spawn the editor (see above), write its handle into the buffer, creating the buffer at its existing path if it does not exist yet" — but nothing in that paragraph, or anywhere else in the file, has the architect tell the editor where the buffer itself is.

`src/agents/editor.md`, once Task 36.1 lands, no longer says nothing about a buffer: 36.1 widens the same appositive that already names `architect-editor-engine`, stating its own change as "`editor.md` names the buffer in the same word the engine uses; the file gains no path and no recovery account — those stay outside this task's one clause." Naming the buffer is not locating it — nothing in that widened account, or anywhere else in the file, gives the editor a path to hold. This task lands after 36.1 (see Blast radius), so the editor.md it edits already names the buffer rather than saying nothing about one.

Task 36.1 — "the buffer's definition moves into the engine both halves load" — gives the editor the buffer's *shape*: the two zones, what each holds, the re-read rule, the drain rule, all stated in the engine both halves already load at birth. It does not give the editor the buffer's *path*. A hand that knows the shape of a memory it cannot locate still cannot read it, much less re-read it on change.

## The change

At the moment of spawn, each half learns the other's address, stated symmetrically in both files. `agent-architect` gains the obligation: alongside writing the editor's handle into the buffer, that same spawn moment gives the editor the buffer's path. `editor.md` gains the account of receiving it: at spawn, alongside loading `architect-editor-engine`, the editor holds the buffer's path as part of what it is given — something that happens to it, not something it derives.

The obligation to give the path belongs to the architect, because the architect already controls the spawn moment and already writes into the buffer at that exact point — the same act that names the handle can name the path. The account of receiving it belongs to the editor, because the editor's own file already states what happens to it at spawn, and holding the path is exactly that kind of fact, not a decision the editor makes. Splitting it this way keeps each file stating only what it already governs: the architect's own actions at spawn, the editor's own state at spawn.

The vehicle for that path is the spawn prompt itself, and only there. `agent-architect`'s own sentence forecloses this today: "its content *is* the spawn prompt" pins the first channel-message's content to be nothing but the relayed payload or the authored work-order, with no room stated for anything else. This task widens that sentence so that, at the spawn and only there, the prompt carries the buffer's path in addition to the channel-message it already carries. This does not reopen the enrichment ban in § "Relay on the marker; author a prompt in exactly one case": that ban forecloses the architect folding its own reading into the before-mark payload the editor must reason over independently; the path sits alongside that payload, never inside it, and carries no reading, no finding, no conclusion — it contaminates nothing the ban exists to protect. The format token still opens the message — `architect-editor-engine`'s mode rule keys strictly off the token that opens the message, and nothing here moves it from that position; the path's exact placement relative to the rest of the prompt is left to the implementer. The two channel-message formats themselves are untouched by this — this is an addition to the spawn act in `agent-architect` alone, not a third format (see Blast radius).

## Blast radius

This task lands after 36.1: Current state above already grounds itself on the post-36.1 wording of `editor.md`'s appositive, so this task's own edit adds the path onto an account that already names the buffer, not onto one that names nothing.

Task 36.1's engine gains no new obligation from this task — the path travels through the spawn moment each file already describes, not through the engine both halves load; the engine continues to state the buffer's shape only. `architect-editor-engine` gains no new obligation either, by the same reasoning: the vehicle above widens a sentence already inside `agent-architect`, not the engine's own two formats.

`architect-pairing-engine` is untouched: nothing about an assigned pairing role changes how or when the path is given.

No new file and no new `loads:` edge — the exchange lands inside the spawn moment each file already has.
