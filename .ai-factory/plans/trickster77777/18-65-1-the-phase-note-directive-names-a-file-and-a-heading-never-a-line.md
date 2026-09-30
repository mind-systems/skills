# Plan: 65.1 — the phase-note directive names a file and a heading, never a line

## Context
`src/skills/roadmap-outline-deep/SKILL.md` § "Step 1: Write the phase note" hands `note` a **Verbosity directive** that asks for "a `file:line` where a claim needs one". `docs/reference-by-name.md` calls that form a defect ("A `file:line` reference is a defect report against its target"). This task rewrites that one bullet so a claim resting on a file names the file and the heading, symbol or quoted fragment that holds it, never a line number. Task spec: `.ai-factory/specs/trickster77777/180-the-phase-note-directive-names-a-file-and-a-heading-never-a-line.md`; governing spec: `docs/reference-by-name.md` (not edited).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the directive

- [x] **Replace the Verbosity directive bullet in Step 1**
  Files: `src/skills/roadmap-outline-deep/SKILL.md`
  In § "Step 1: Write the phase note", the bullet list of `note`'s caller hooks ends with the bullet led by `- **Verbosity directive** —`. It currently reads (three wrapped lines):
  ```
  - **Verbosity directive** — short: a few sentences more than the preamble, grounded
    in the docs and code read at Step 0, a `file:line` where a claim needs one, never a
    transcript of the conversation.
  ```
  Replace the whole bullet with exactly this text (the sentence is pinned verbatim by the spec; the bold lead-in and the dash after it stay as written; continuation lines are indented two spaces like the sibling bullets; wrapped at the file's own column, which is 85 characters in this section):
  ```
  - **Verbosity directive** — short: a few sentences more than the preamble, grounded
    in the docs and code read at Step 0 — a claim that rests on a file names the file
    and the heading, symbol or quoted fragment that holds it, never a line number — and
    never a transcript of the conversation.
  ```
  Nothing else in the file changes. The **Destination directory** and **Template** bullets stay as they are. The re-run rule further down in Step 1 ("the template and verbosity directive above") refers to the directive by name, so it picks up the new sentence without an edit. Do not touch `src/skills/note/SKILL.md`: `note` reads the directive as free text.

### Confirm the blast radius

- [x] **Re-run the spec's sweep** (depends on the task above)
  Files: none (read-only check)
  Run:
  ```
  grep -rn "file:line" src/ docs/ CLAUDE.md
  grep -rn "erbosity directive" src/ docs/
  ```
  Expected: `src/skills/roadmap-outline-deep/SKILL.md` no longer appears in the first search. The remaining hits are the ones the spec's **Finding** lists as out of scope or intended. These are the `command-pin-gaps` walk paragraph and the `roadmap-prune` handoff item, which tasks 65.4 and 65.3 own; the `command-pin-gaps` scan-line form `[file:line|spec-location]`; the global CLAUDE.md reference rule; `docs/reference-by-name.md`; `docs/counts-go-stale.md`; and the root `CLAUDE.md` index row. The second search shows the new bullet, the re-run rule's by-name reference, `note`'s hook definition, and the separate directives in `command-handoff` and `task-rescue`. None of these needs an edit. A hit outside this list means the sweep has changed since the spec was written: report it and do not edit it.
