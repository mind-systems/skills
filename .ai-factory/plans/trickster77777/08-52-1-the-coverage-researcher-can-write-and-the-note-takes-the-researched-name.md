# Plan: 52.1 — the coverage researcher can write, and the note takes the researched name

## Context
`src/skills/roadmap-test-coverage/SKILL.md` § "Layer 4 — Deep Research (parallel agents)" launches a read-only `Explore` agent and tells it to write its note to disk. Its template also titles the note with the area name from before research, while the slug is chosen after research. This task makes three text edits, each pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0204-the-coverage-researcher-can-write-and-the-note-takes-the-researched-name.md` § "What must be true after": the launch names a `general-purpose` agent, the slug paragraph says the title carries the same name, and the template's first line takes that name. The governing spec `docs/test-coverage-pass.md` names neither the agent type nor the title, so it needs no edit.

Blast radius (the spec's three sweeps, re-run while planning, same result):
- `grep -rn "Explore\|general-purpose" src/skills/roadmap-test-coverage/ docs/ CLAUDE.md` finds `Explore` only at the Layer 4 launch sentence, which changes. It finds `general-purpose` only at Layer 5 and Layer 7, which already use that type and stay unchanged. No doc or `CLAUDE.md` names either type.
- `grep -rn "Test Plan\|Area Name" src/ docs/ CLAUDE.md` finds only the template's title line, which changes.
- `grep -n "area name" src/skills/roadmap-test-coverage/SKILL.md` finds the Layer 4 `Area: <area name>` input line and the later layers' labels: the Layer 5 prompt and return lines, the Layer 6 and Layer 7 hand-off lists, and the Layer 8 report. All stay unchanged. They take the orchestrator's own label for the area, not the note's title.
- The `saved:` return line and the sentence "Each agent writes its note to disk and returns one line to the orchestrator." stay unchanged.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Layer 4 launches a writer, and the note's title follows the researched name

- [x] **Rewrite the three Layer 4 texts verbatim from the spec**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  All three edits are in § "Layer 4 — Deep Research (parallel agents)":

  1. **Launch sentence.** The current text is "Launch one `Explore` agent per area in a **single message** (parallel)." Replace it with:
     ```
     Launch one `general-purpose` agent per area in a **single message** (parallel).
     ```
     Leave the next sentence as it is: "Each agent writes its note to disk and returns one line to the orchestrator."

  2. **Slug paragraph in the agent prompt template.** The current paragraph begins "Choose the note's slug yourself, only after you have read the source below —" and ends "not for the Area label above." Replace the whole paragraph with:
     ```
     Choose the note's slug yourself, only after you have read the source below — short, lowercase, hyphens, named for what the area actually turns out to be, not for the Area label above. The note's title carries that same name, in words.
     ```

  3. **Template title line.** Replace `# <Area Name> — Test Plan` with:
     ```
     # <the name you chose, in words> — Test Plan
     ```

  The file hard-wraps prose at about 80 characters, both outside and inside the fenced prompt template. Use exactly this on-disk layout:
  - Edit 1 becomes one line of 79 characters: "Launch one `general-purpose` agent per area in a **single message** (parallel)." The unchanged next sentence keeps its own line below it.
  - Edit 2 becomes these three lines. The first two are the existing lines, unchanged. The third is 80 characters, which fits the file's existing column.
    ```
    Choose the note's slug yourself, only after you have read the source below —
    short, lowercase, hyphens, named for what the area actually turns out to be,
    not for the Area label above. The note's title carries that same name, in words.
    ```
  - Edit 3 stays on one line.

  Do not touch any other line. That includes the `Area: <area name>` input line, the "Write the document below to …" paragraph, the `saved:` return line, and Layers 5–8.

  Verify these in `src/skills/roadmap-test-coverage/SKILL.md`:
  - `grep -n "Explore"` returns nothing.
  - `grep -n "Area Name"` returns nothing.
  - `grep -n "Launch one \`general-purpose\` agent per area"` finds the Layer 4 line as well as Layer 5's existing line.
  - `grep -n "carries that same name"` finds the new prompt sentence.
  - `grep -n "# <the name you chose, in words> — Test Plan"` finds the title line.

  Also check that `git diff` touches only these three places.
