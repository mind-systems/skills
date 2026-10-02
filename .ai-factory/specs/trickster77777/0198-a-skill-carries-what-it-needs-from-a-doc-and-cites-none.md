# 71.1 — a skill carries what it needs from a doc, and cites none

## What is true now

Three skill-side files cite `docs/paired-loop.md`, the only doc any skill names. The text wraps in each file at a fixed column.

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter", the snapshot paragraph, reads: "…a request meant for whoever comes next, on the project rather than on this conversation, is the different genre `command-handoff` writes, and does not reach here (`docs/paired-loop.md` § "How the memory begins, and how it survives" draws the line by reader, subject, and lifetime). The on-request one is the architect's own capability, reached by a request rather than a command: no command is invoked and no template is consulted."

`src/commands/command-handoff.md` has a paragraph reading: "A request meant to continue the same architect's own memory across a break is a different genre — the architect's own on-request snapshot, not this command — and never reaches here, however it is phrased; `docs/paired-loop.md` § "How the memory begins, and how it survives" draws that line by reader, subject, and lifetime."

`src/skills/agent-architect/templates/buffer-seed.md` § `## Team` holds the placeholder: "<Where this head sits in a team, as `docs/paired-loop.md` § "The team" has it: the goal it serves, linked to where it is written; its liaison above; those it leads below — each by repository and folder number, never by session name.>"

The sentence before each of the first two citations already draws the line by who reads and what it is about: in the skill, a request that continues this head or one meant for whoever comes next, on the project; in the command, a request meant to continue the same architect's own memory. The third cites the doc for a model it does not state: the doc's § "The team" says each node holds its own links, not the whole network, that after a compact the head knows its place from them, and that "A liaison is the head that another repository's work reaches through". No skill defines "liaison".

## What must be true after

None of the three cites a doc. In the skill, the sentence reads: "…a request meant for whoever comes next, on the project rather than on this conversation, is the different genre `command-handoff` writes, and does not reach here. The on-request one is the architect's own capability, reached by a request rather than a command: no command is invoked and no template is consulted."

In the command, the sentence reads: "A request meant to continue the same architect's own memory across a break is a different genre — the architect's own on-request snapshot, not this command — and never reaches here, however it is phrased."

In the seed, the placeholder under `## Team` reads: "<Where this head sits in a team, by its own links and not the whole network's: the goal it serves, linked to where it is written; its liaison above, the head that another repository's work reaches through; and those it leads below — each by repository and folder number, never by session name. After a compact this is how the head knows its place.>"

## What breaks on contact

**Rule:** a text breaks on this change if it reads one of these sentences, or if it cites the doc's § "How the memory begins, and how it survives" for a line these files draw.

**Sweep:**
```
grep -rn "paired-loop" src/
grep -rn "How the memory begins" src/ docs/ CLAUDE.md
grep -rn "## Team" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches the three carriers above and nothing else under `src/`. The second reaches the same two citations and the doc's own heading, which stays and still states the line the skills draw in their own words. The third reaches the seed's heading and placeholder, and no skill, command or doc reads the placeholder's wording. The skill sentence is read by the architect at every start, and the command sentence when the command is invoked; each reads as a complete rule once the parenthetical or the clause is gone, since the line it draws stands in the words before it. The seed is copied whole into a buffer at founding, so the new placeholder reaches buffers founded afterwards. A head founded before keeps its own `## Team` text, since the refresh matches standing entries by their bold lead-in and this section has none, so no existing buffer changes. No skill defines or uses "liaison" besides this placeholder, which is why the definition goes into it.
