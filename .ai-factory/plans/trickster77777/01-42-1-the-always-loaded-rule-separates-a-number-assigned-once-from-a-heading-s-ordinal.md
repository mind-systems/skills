# Plan: 42.1 — the always-loaded rule separates a number assigned once from a heading's ordinal

## Context
The paragraph in `src/global/CLAUDE.md` § "Grounding claims" that opens "A reference addresses by **name**, never by position." lists "a numbered item" among what survives every insertion, and does not tell a number assigned once and split (a task's `N.M`, a skill's step) apart from a heading's ordinal. The governing spec, `docs/reference-by-name.md` § "Granularity, not size", already draws that line. This task replaces the one sentence with the wording pinned verbatim in the task spec (`.ai-factory/specs/trickster77777/0197-the-always-loaded-rule-separates-a-number-from-a-heading-ordinal.md` § "What must be true after").

Ground-truth notes (checked against the files while planning):
- The task spec says the text "wraps in the file at a fixed column". It does not: the whole paragraph is one physical line in `src/global/CLAUDE.md`. Keep it as one line. Do not add wrapping.
- The spec's finding says the project `CLAUDE.md` row for `docs/reference-by-name.md` still says "a numbered item". The current row already says "a heading, a bold lead-in, a number assigned once — anything that will be depended on", so it agrees with the new sentence and needs no change.
- The `agent-architect` anchor list ("a heading, a bolded rule, a symbol, a unique string — never a position") is a different list for a different purpose and agrees with the new sentence. Leave it alone.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Replace the sentence

- [x] **Rewrite the survival sentence in the global CLAUDE.md**
  Files: `src/global/CLAUDE.md`
  In § "Grounding claims", in the paragraph that opens "A reference addresses by **name**, never by position.", replace this exact text:

  `A heading, a bolded rule, a symbol, a numbered item survives every insertion above it; a line number survives none, and nothing reports it when it rots.`

  with this text, byte for byte as the task spec pins it:

  `A heading, a bolded rule, a symbol survives every insertion above it, and so does a number assigned once and split rather than shifted — a task's `N.M`, a skill's step. A line number survives none, and nothing reports it when it rots; a heading's ordinal is the same kind of position, so a document's section is cited by its heading's text.`

  Leave the paragraph's first sentence ("A reference addresses by **name**, never by position.") unchanged. Also leave everything from "A `file:line` is a defect report against its target" to the end of the paragraph unchanged. Keep the paragraph on its single physical line. Use the em dash (—) and the backticks around `N.M` exactly as written in the spec. Make the edit in `src/global/CLAUDE.md` itself. `~/.claude/CLAUDE.md` and `active/CLAUDE.md` are symlinks that resolve to it, so do not touch them.

- [x] **Run the blast-radius sweep** (depends on Rewrite the survival sentence in the global CLAUDE.md)
  Files: none modified
  Run the task spec's sweep from the repository root:
  `grep -rn "numbered item" src/ docs/ CLAUDE.md`, `grep -rn "survives every insertion" src/ docs/ CLAUDE.md`, `grep -rn "unique string" src/ docs/ CLAUDE.md`.
  Expected results:
  - "numbered item" returns no hits.
  - "survives every insertion" returns only the new sentence in `src/global/CLAUDE.md`.
  - "unique string" returns only the `agent-architect` anchor list, which stays as is.

  If any other text restates the list of what survives an insertion, or states a rule about citing a section by its number, stop and report it. Do not edit it: it is outside this task's scope.
