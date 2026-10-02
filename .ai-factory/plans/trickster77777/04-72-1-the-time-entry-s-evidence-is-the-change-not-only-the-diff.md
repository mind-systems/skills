# Plan: 72.1 — the time entry's evidence is the change, not only the diff

## Context
`src/skills/polymorphism-philosophy/SKILL.md` § "The two entries" gets a new time-entry sentence. Its evidence becomes the change: the diff where the change has landed, and the task that describes it where it has not. That covers both readers, a direct call on a code area or on closed tasks, and `roadmap-decompose-skeleton` Lens 1 running over open tasks. The replacement sentence is pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0200-the-time-entrys-evidence-is-the-change-not-only-the-diff.md` § "What must be true after". Copy it exactly. The pinned sentence also changes the question's tense from "was a seam cut at that arrival" to "does it cut a seam at that arrival". That change is part of the pinned text, and it is not optional.

Blast radius, from the spec's sweep (re-run while planning, same result): `its evidence is the diff` and `time entry` match only `src/skills/polymorphism-philosophy/SKILL.md`. `roadmap-decompose-skeleton` Lens 1, `docs/sakshi-harness/skill-cycle.md` and the `CLAUDE.md` skill lists name the unit but state no evidence, so they stay unchanged (per the spec). In the unit itself, the sentence "A consumer skill reaches this unit through the time entry; …", § "The trigger" and the frontmatter stay unchanged.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit the unit

- [x] **Replace the time entry's sentence**
  Files: `src/skills/polymorphism-philosophy/SKILL.md`
  In § "The two entries", the sentence currently runs across the wrapped lines as: "The **time** entry takes what a change just brought: does this change bring a second member to a kind, and was a seam cut at that arrival or not — its evidence is the diff." Replace it with this text, verbatim: "The **time** entry takes what a change just brought: does this change bring a second member to a kind, and does it cut a seam at that arrival or not — its evidence is the change, the diff where it has landed and the task that describes it where it has not."
  Keep the opening "One question, reached two ways." and everything from "The **space** entry takes …" onward unchanged, word for word. Re-wrap the paragraph at the file's existing column (lines of at most about 80 characters, as in the surrounding text). Only the lines the edit touches may change. Keep the em dashes (—) as they are in the file.
  Afterwards, `grep -rn "its evidence is the diff\|was a seam cut" src/ docs/ CLAUDE.md` must return nothing. `grep -n "the diff where it has landed" src/skills/polymorphism-philosophy/SKILL.md` must return the edited paragraph. The search runs on the source, so a match that a line break splits must be checked by reading the paragraph.
