# Phase 63 — the architect comes back on a bare invocation

Governing spec: `docs/paired-loop.md`

`docs/paired-loop.md` § "Where the memory lives" has the head read its own session id, find the folder whose address file holds it, and rehydrate from that folder's latest snapshot, on invocation alone; a session no folder claims founds its own folder, and a brand-new chat never adopts an existing one, however it is asked or whatever it is handed. `agent-architect` holds the opposite rule: a memory snapshot naming a buffer means the same memory resumes in whatever chat receives it, and no such pointer means a new architect creates its own. That rule is what the phase replaces, and it lives in § "Spawn once, message thereafter" (the two starts, the pointer a snapshot carries, and the recovery passage), § "Your buffer is shared; you alone write it", and § "On every invocation" — none of them reads a session id or consults a folder.

Measured 2026-09-29 and 2026-09-30, across two sessions: a session's id holds across a compact and across reopening the chat a day later, while its name holds across a compact and changes on reopening. An agent reads its own id with no hook: it runs a command carrying a random nonce, then greps the project's transcripts under `~/.claude/projects/<project-key>/` for that nonce — exactly one file matches, and its name is the id.

Nothing under `docs/` is written.
