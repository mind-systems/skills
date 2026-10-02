# 52.1 — the coverage researcher can write, and the note takes the researched name

## What is true now

`src/skills/roadmap-test-coverage/SKILL.md` § "Layer 4 — Deep Research (parallel agents)" reads: "Launch one `Explore` agent per area in a **single message** (parallel). Each agent writes its note to disk and returns one line to the orchestrator." The agent prompt template says, after the area and source lines: "Choose the note's slug yourself, only after you have read the source below — short, lowercase, hyphens, named for what the area actually turns out to be, not for the Area label above." It later says "Write the document below to <Note directory><NN>-<slug>.md — the note number handed in above and the slug you chose from reading the source. You write the file yourself, at the path you just chose, in the same act:" and the template opens "# <Area Name> — Test Plan". The text wraps in the file at a fixed column.

`Explore` has every tool except `Edit`, `Write` and `NotebookEdit`, so an `Explore` agent cannot write the file it is told to write. The later layers launch `general-purpose` agents. The title's `<Area Name>` fills from the Area label, the name the area had before research, while the slug is chosen after.

## What must be true after

The launch sentence reads: "Launch one `general-purpose` agent per area in a **single message** (parallel)." The sentence after it is as it stands.

The slug paragraph of the prompt reads: "Choose the note's slug yourself, only after you have read the source below — short, lowercase, hyphens, named for what the area actually turns out to be, not for the Area label above. The note's title carries that same name, in words."

The template's first line reads: "# <the name you chose, in words> — Test Plan".

## What breaks on contact

**Rule:** a text breaks on this change if it names the research agent's type, reads the note's title, or fills a label from the note's name.

**Sweep:**
```
grep -rn "Explore\|general-purpose" src/skills/roadmap-test-coverage/ docs/ CLAUDE.md
grep -rn "Test Plan\|Area Name" src/ docs/ CLAUDE.md
grep -n "area name" src/skills/roadmap-test-coverage/SKILL.md
```

**Finding.** The first search reaches `Explore` at the launch sentence alone, the task's target, and `general-purpose` at the later layers, which already launch that type for the testability review and the failing-test repair, so Layer 4 now matches them. No doc or `CLAUDE.md` names either type: `docs/test-coverage-pass.md` § "Research runs in disposable hands, never a persistent one" says only "one throwaway agent per area", so it does not contradict the change. The second search reaches the template's title line, and no other text reads a note's title: the later layers open a note by its path, as Layer 6 does to append its refactor section. The third reaches the later layers' annotations, the testability review prompt, its return lines, the refactor and failure hand-off lists, and the final report. They fill from the orchestrator's own label for the area as it scoped it, and a report line carries the note's path beside the label, so a title that follows the researched name does not disturb them. The `saved:` return line is unchanged: it carries the path the agent wrote, and with an agent that can write the line reports a write that happened. The doc's § "A number is fixed before research; a name is not" says the name is pinned "late enough to still be true once research has actually looked", which the title now follows.
