# Phase 69 — the session probe prints its nonce in one command and searches for it in the next

**Touches:** 2

`agent-architect` § "Spawn once, message thereafter" has the head read its session id "by running a command that prints a random nonce, then searching the project's transcripts … for the printed nonce". A single command that both prints the nonce and searches for it finds nothing, because its output reaches the transcript only when the command returns. The skill does not say that the printing and the search are two commands.

Under the same section's "No folder found, for whatever reason, means you are a new head — you never ask the user which", a resumed head whose probe fails this way finds no folder and founds a second one, and its whole memory stays in the first, with nothing but the passing mention that the id could not be read. The architect hit it once, moving its own folder by hand. The fix is on the surface: the nonce is printed by one command and searched for by the next. The zero-match policy stays as it is: never ask, never stop.

[paired-loop](../../../docs/paired-loop.md) § "Where the memory lives" says the head "reads its own session id, finds the folder that holds it" and that "A session no folder claims is a new head"; it states no mechanism for reading the id, and a skill is its own documentation, so no document is written.

What leaves the phase. The two findings routed onto it first were a failed probe at founding, which leaves a folder with no `session-id:` line, and a dead hand holding an unforwarded `::` payload. Neither stands. Every architect folder in this repository carries a `session-id:` today, so no orphan exists, and the user no longer uses the relay marker.
