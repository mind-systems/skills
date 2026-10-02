# Plan: 71.1 — a skill carries what it needs from a doc, and cites none

## Context
Three skill-side files cite `docs/paired-loop.md`: the snapshot paragraph in `agent-architect`, a paragraph in `command-handoff`, and the `## Team` placeholder in the buffer seed. A skill is its own documentation, so this task removes all three citations. The two prose citations are simply deleted, because the sentence before each one already draws the line. The placeholder is rewritten so it states the model itself, including what "liaison" means. The after-text of each file is pinned verbatim in the task spec, `.ai-factory/specs/trickster77777/0198-a-skill-carries-what-it-needs-from-a-doc-and-cites-none.md` § "What must be true after". The phase note is `.ai-factory/specs/trickster77777/0195-a-skill-cites-a-path-that-exists-in-one-repository.md`.

Ground-truth notes (checked against the files while planning):
- `src/commands/command-handoff.md` puts each paragraph on one physical line, so its edit stays on one line.
- `src/skills/agent-architect/SKILL.md` hard-wraps prose at 72 columns or less.
- `src/skills/agent-architect/templates/buffer-seed.md` hard-wraps at 76 columns or less.
- The two wrapped files keep their wrapping. Only words change; the extra whitespace changes are just the line breaks around each edit.
- `docs/paired-loop.md` is not touched. Its heading "How the memory begins, and how it survives" stays.
- Existing buffers under `.ai-factory/architects/` are not touched. A head that is already founded keeps its own `## Team` text.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Remove the citations

- [x] **Drop the parenthetical citation from the agent-architect snapshot paragraph**
  Files: `src/skills/agent-architect/SKILL.md`
  The edit is in § "Spawn once, message thereafter", in the paragraph that opens "The memory snapshot continuing this same architect has two occasions:".

  Delete this exact text: ` (`docs/paired-loop.md` § "How the memory begins, and how it survives" draws the line by reader, subject, and lifetime)`. Include its leading space. Today it is wrapped across the lines that begin "not reach here (" and "it survives\" draws".

  After the deletion, the sentence reads exactly as the spec pins it: "…a request meant for whoever comes next, on the project rather than on this conversation, is the different genre `command-handoff` writes, and does not reach here. The on-request one is the architect's own capability, reached by a request rather than a command: no command is invoked and no template is consulted."

  Keep the reflow local. Replace the five physical lines that run from "not reach here (`docs/paired-loop.md` …" through "consulted. Either occasion writes the snapshot into your own folder —" with these four lines:
  ```
  not reach here. The on-request one is the architect's own capability,
  reached by a request rather than a command: no command is invoked and
  no template is consulted. Either occasion writes the snapshot into your
  own folder —
  ```
  The next existing line, "numbered as `architect-editor-engine` defines — with a digest of what", follows unchanged. Leave every other word of the paragraph as it is, and leave the paragraph's other lines alone.

- [x] **Drop the trailing citation clause from command-handoff**
  Files: `src/commands/command-handoff.md`
  Find the single-line paragraph that opens "A request meant to continue the same architect's own memory across a break is a different genre". Replace the ending `; `docs/paired-loop.md` § "How the memory begins, and how it survives" draws that line by reader, subject, and lifetime.` with a period.

  The whole line then reads verbatim: "A request meant to continue the same architect's own memory across a break is a different genre — the architect's own on-request snapshot, not this command — and never reaches here, however it is phrased."

  Keep it on one physical line, and keep the em dashes.

### Rewrite the seed placeholder

- [x] **Replace the `## Team` placeholder in the buffer seed**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  Under the `## Team` heading, replace the whole four-line placeholder, from "<Where this head sits in a team, as `docs/paired-loop.md` § \"The team\" has" through "session name.>". Use the spec's pinned text, wrapped at 76 columns or less:
  ```
  <Where this head sits in a team, by its own links and not the whole
  network's: the goal it serves, linked to where it is written; its liaison
  above, the head that another repository's work reaches through; and those it
  leads below — each by repository and folder number, never by session name.
  After a compact this is how the head knows its place.>
  ```
  Words and punctuation must match the spec's sentence exactly, including the em dash and the angle brackets that open and close it. Leave the `## Team` heading, the blank lines around it, and all other sections and standing entries unchanged.

### Confirm the sweep

- [x] **Run the spec's blast-radius sweep** (depends on all three edits above)
  Files: none modified
  Run these from the repository root:
  `grep -rn "paired-loop" src/`, `grep -rn "How the memory begins" src/ docs/ CLAUDE.md`, `grep -rn "## Team" src/ docs/ CLAUDE.md`.

  Expected results:
  - `paired-loop` returns no hits under `src/`.
  - "How the memory begins" returns only the heading in `docs/paired-loop.md`.
  - `## Team` returns only the seed's heading.

  If any other text under `src/` cites a file under `docs/`, stop and report it rather than editing it. The same goes for anything that reads the old sentences or the old placeholder wording. Mentions of `docs/` as a working folder in `aif-docs` and `roadmap-outline-deep` are not citations, so leave them alone.
