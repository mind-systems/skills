# Phase 71 — a skill carries what it needs from a doc in its own text

A skill is its own documentation. `docs/` describes the system, and it describes the skills, never the reverse: what a skill needs from a doc is part of the skill's own text, and the skill cites no doc. The user: "зачем вообще в скилах упоминается документация? этого не должно быть… та часть доки, которую мы пытаемся по ссылке в него инжектить — должна быть частью скила". No document states the rule; it lives in the architect's buffer by the user's choice, and this phase writes it into no doc.

What diverges is three skill-side carriers, found by a sweep of `src/` for this repository's doc names, and all cite `docs/paired-loop.md`.

- **`agent-architect`, § "Spawn once, message thereafter", the snapshot paragraph.** After saying a request meant for whoever comes next "is the different genre `command-handoff` writes, and does not reach here", it adds the parenthetical "(`docs/paired-loop.md` § "How the memory begins, and how it survives" draws the line by reader, subject, and lifetime)". The sentence before already draws the line by who reads, this head or whoever comes next, and by what it is about, this conversation or the project.
- **`command-handoff`, the paragraph on a request meant to continue the architect's own memory.** It ends "`docs/paired-loop.md` § "How the memory begins, and how it survives" draws that line by reader, subject, and lifetime", the same citation from the other side. Its own sentence draws the line by what the request is meant to continue.
- **The `## Team` placeholder in `templates/buffer-seed.md`.** It reads "<Where this head sits in a team, as `docs/paired-loop.md` § "The team" has it: …>" and carries the doc's model by reference. The placeholder says what the section holds, and leaves out what the doc added: that the links are the head's own and not the network's, that a liaison is "the head that another repository's work reaches through", a term no skill defines, and that the head knows its place from them after a compact.

Mentions of `docs/` as a working folder, in `aif-docs` and `roadmap-outline-deep`, are not citations.
