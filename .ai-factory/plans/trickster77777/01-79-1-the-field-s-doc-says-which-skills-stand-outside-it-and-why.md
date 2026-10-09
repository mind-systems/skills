# Plan: 79.1 — the field's doc says which skills stand outside it, and why

## Context
`docs/skill-description-field.md` and `docs/always-loaded-discipline.md` describe the skill description field as holding the description of every skill, but skills flagged `disable-model-invocation: true` are not in it. This task narrows both opening paragraphs to "each skill the agent may call on its own" and adds one sentence to the field doc saying which skills stay out, and why. The after-texts are pinned verbatim in the task spec (`.ai-factory/specs/trickster77777/0228-the-fields-doc-says-which-skills-stand-outside-it-and-why.md`, § "What must be true after"), and the edits below copy them byte for byte. Nothing else in either file changes. `docs/reserved-words.md` ("all skill descriptions loaded at once") and any CLAUDE.md text stay untouched, per the spec's § "What breaks on contact".

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Doc edits

- [x] **Narrow the field doc's opening and state who stands outside the field**
  Files: `docs/skill-description-field.md`
  Make two edits in the opening paragraph, the one that begins "Project knowledge has two layers, not one.":
  1. Replace the parenthesis `(the \`description:\` of every skill in the family)` with `(the \`description:\` of each skill the agent may call on its own)`.
  2. Directly after the sentence `All skill-descriptions loaded at once form one layer — the **skill-description-field**.`, insert this sentence, separated by a single space and kept in the same paragraph. It goes before `The top of the pyramid (...)`:
     `A skill whose work is reviewed only before it happens, with the user present, and never after (deleting files, for one) is called by the user alone, and stays out of the field.`
  Leave every other sentence, link and section of the file unchanged.

- [x] **Align the discipline doc's phrase**
  Files: `docs/always-loaded-discipline.md`
  In the opening paragraph, the one that begins "The always-loaded layer has two halves", replace `every skill's \`description:\` read as one continuous text` with `the \`description:\` of each skill the agent may call on its own, read as one continuous text`. The text before it (`One names what exists: the [skill-description-field](skill-description-field.md), `) and after it (` — vocabulary, surfaces, the moment to invoke.`) stays as is. Nothing else in the file changes.

- [x] **Verify the sweep** (depends on both edits above)
  Files: none (read-only check)
  Run `grep -rn "of every skill in the family\|every skill's \`description:\`\|all skill descriptions" docs CLAUDE.md`. The only remaining hit should be the `docs/reserved-words.md` registry entry, which stays unchanged. Run `git diff --stat` and confirm that only the two doc files changed.
