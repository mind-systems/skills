# What the architect writes with its own hands is named

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md` names only the buffer as a file the architect edits directly: § "Your buffer is yours alone" (`:220-237`) — "it is the one file you edit directly, because it isn't a shared artifact" (`:236-237`).

Rescue reports appear nowhere in the file — confirmed by a direct search, zero occurrences. Handoffs appear once, in a narrow aside about carrying the buffer's path across a compact: "the handoff continuing this same architect across it — no other handoff has any reason to mention the buffer or the handle" (`:47-48`); three further mentions (`:78-79`, `:224`, `:252`) are all the same pre-compact mechanic, never a general statement that the architect authors handoffs with its own hands.

`src/commands/command-handoff.md` and `~/.claude/skills/task-rescue/SKILL.md` (its own `.ai-factory/rescue-reports/<project>/` destination, `:583`) each already write their own artifact; neither states who — architect or editor — holds the pen.

## The change

`agent-architect` names the class directly: a handoff, a rescue report, the buffer, and anything else the architect authors from its own reading, are the architect's own hand to write — never the editor's. State why: the content is the architect's own context, and a retelling by something that does not hold that context is unpredictable. Everything else — every shared artifact: roadmap, specs, code, docs — goes to the editor, exactly as the skill's opening paragraph (`:25-26`) already has it.

## Blast radius

`command-handoff` and `task-rescue` keep their own mechanics unchanged — this names who holds the pen when either is invoked, not how either artifact is composed or where it is written.
