# Phase 62 — each architect lives in a folder of its own

Governing spec: `docs/paired-loop.md`

`docs/paired-loop.md` § "Where the memory lives" gives each architect one folder under `.ai-factory/architects/`, holding three things: its buffer, its own snapshots, and one address file carrying the session id and the session name, which a peer reads instead of the buffer. Read against the code: `architect-editor-engine` places the buffer at `.ai-factory/notes/<NN>-architect-buffer.md`, a folder holding nothing today but architect buffers. `agent-architect` § "Spawn once, message thereafter" founds and seeds a new buffer there from `templates/buffer-seed.md`, and writes the editor's handle into that same buffer at spawn — but names no folder and no address file anywhere in the section. A snapshot instead travels to `.ai-factory/handoffs/`, a folder holding every other handoff genre beside it. `templates/buffer-seed.md` itself has no section for an address or a session; its headings are the memory's content, not its home.

Nothing under `docs/` is written.
