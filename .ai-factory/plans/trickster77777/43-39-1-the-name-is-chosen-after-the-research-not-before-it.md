# Plan: 39.1 — the name is chosen after the research, not before it

## Context
`roadmap-test-coverage`'s Layer 4 research-agent prompt fixes the note's number and slug together before the agent has read anything; per the governing spec (`docs/test-coverage-pass.md` § "A number is fixed before research; a name is not") the number must be fixed early and the name late. This task moves the slug choice into the agent's own task, after research, leaving the number handoff untouched.

Grounded state (read fresh from `src/skills/roadmap-test-coverage/SKILL.md`): the agent prompt template under Layer 4 carries the pre-fixed pair at exactly three sites — the header line `Note to write: .ai-factory/specs/<NN>-<slug>.md`, the write instruction `Write the following document to .ai-factory/specs/<NN>-<slug>.md:`, and the return line `saved: .ai-factory/specs/<NN>-<slug>.md`. The number computation above the template (`$NEXT_NOTE_NUM`, four-digit bound, landed by 38.2) is not touched. The other placeholder sites in the file (Layer 6 refactor pointer, Layer 8 "Notes written" confirmation, Layer 8 handoff block) carry the bare placeholder whose meaning follows from where the pair is decided — per the task spec they need no edit.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Agent prompt template (Layer 4)

- [x] **Hand the agent the number alone, not a finished path**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  In the Layer 4 "Agent prompt template" code block, replace the header line `Note to write: .ai-factory/specs/<NN>-<slug>.md` with two lines that hand over only the number and the destination directory — `Note number: <NN>` and `Note directory: .ai-factory/specs/` — so no path template and no slug value is carried in from the spawn prompt (the task spec's wording: "the number alone for its destination, not a finished path"). Immediately state, inside the prompt, that the slug is the agent's own choice, made only after it has read the source (short, lowercase, hyphenated — the same shape `note` derives, "lowercase, hyphens"), named for what the area actually turned out to be, not for the `Area:` label handed in. Keep `Area: <area name>`, `Source file(s):`, and `Existing spec file:` lines as they stand.

- [x] **Reword the write instruction so the slug is chosen at the moment of writing** (depends on the task above)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  In the same template, reword `Write the following document to .ai-factory/specs/<NN>-<slug>.md:` so that it reads as the agent's act: write the document to `<Note directory>/<NN>-<slug>.md` where `<NN>` is the number handed in and `<slug>` is the slug the agent derived from its reading — this is the first and only place in the prompt the full path shape is assembled. Make explicit that the agent itself writes the file at the path it chose, in the same act — the caller never applies a name afterward (the task spec calls this out as the point easy to get backwards). The document template body that follows (`# <Area Name> — Test Plan` through `## Gotchas`) is unchanged.

- [x] **Return line reports the exact path written** (depends on the task above)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Replace the closing lines `After writing the file, return exactly one line:` / `saved: .ai-factory/specs/<NN>-<slug>.md` so the return line reports the actual path the agent used, slug included — e.g. `saved: <the exact path you wrote, e.g. .ai-factory/specs/0042-actual-slug.md>` — rather than echoing the placeholder. The line after the code block, `Collect all one-line confirmations.`, stays as is: it already reads the reported path, which is now the only place the real name exists.

### Boundary check

- [x] **Confirm no other site changed** (depends on all above)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  `grep -n "<NN>-<slug>" src/skills/roadmap-test-coverage/SKILL.md` — the Layer 6 pointer, the Layer 8 "Notes written" line, and the two Layer 8 handoff-block pointers still carry the bare placeholder unchanged; the `$NEXT_NOTE_NUM` computation block above the template is byte-identical to before. Nothing outside the three template sentences is edited; body stays ≤ 500 lines; frontmatter untouched.
