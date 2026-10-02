# Plan: 70.1 — a founded buffer opens under its own title

## Context
A buffer founded from `src/skills/agent-architect/templates/buffer-seed.md` is "copied whole" today, so it opens with the seed's title and the seed's paragraph about being a seed, and misnames itself. After this task the seed carries two `#` headings: first its own title with a paragraph about the seed, then a `# Architect buffer — <this folder's number>` heading whose opening speaks of this buffer and its standing entries. The founding passage in `src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" copies from that second heading down, with the folder's number filling the title. All new text is pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0202-a-founded-buffer-opens-under-its-own-title.md` § "What must be true after". Copy it exactly.

Blast radius, from the spec's sweep (re-run while planning, same result):
- `copied whole` / `copies it whole` match only the seed's opening paragraph and the founding passage. This task rewrites both.
- `Buffer seed` matches only the seed's own title, which stays.
- `buffer-seed` matches the founding passage, the refresh sentence in the skill (it reads the standing entries "of `templates/buffer-seed.md` against the buffer's, matching an entry by its bold lead-in"), and the seed itself.

The refresh sentence reads only the standing entries, so it stays unchanged. These also stay unchanged:
- the seed's sections from `## Team` down, including the guidance lines and standing entries;
- the existing buffers under `.ai-factory/architects/`, which per the spec keep their opening;
- `docs/paired-loop.md`, `architect-editor-engine` and `CLAUDE.md`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit the seed and the founding passage

- [x] **Give the seed two openings**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  Replace the file's lines from the title `# Buffer seed — the architect's memory at founding` through the end of its opening paragraph (the paragraph ending "The headings below are filled over the session, not left as placeholder prose."). That is everything above `## Team`. Replace it with this text, verbatim from the spec:

  ```
  # Buffer seed — the architect's memory at founding

  This is the starting shape of a newly founded architect's buffer. The step "Spawn once, message thereafter" in `agent-architect/SKILL.md` copies it into a new buffer file from the `# Architect buffer` heading down, and at every start that finds an existing folder reads the standing entries under `## Method` again, to bring the buffer's entries to the seed's text.

  # Architect buffer — <this folder's number>

  The standing entries of this buffer — the bold-led entries under `## Method` whose lead-in begins "Standing entry —" — come from the seed, `agent-architect`'s `templates/buffer-seed.md`, and are brought to its text at every start that finds this folder. The headings below are filled over the session, not left as placeholder prose.
  ```

  Wrap both paragraphs at the file's existing column (about 74 characters, like the current opening paragraph). Do not break a backticked span across lines. Keep the em dashes (—) and straight quotes exactly as given. Leave one blank line between the buffer's opening paragraph and `## Team`. Do not change anything from `## Team` down.

- [x] **Make the founding passage copy from the buffer heading down** (independent of the seed edit)
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", the first paragraph ends with this founding clause, wrapped across lines:
  "…create `buffer.md` in it, seeded in full from `templates/buffer-seed.md` at the moment of its founding, copied whole, and write `address.md`."
  Replace that clause with this text, verbatim:
  "…create `buffer.md` in it, seeded from `templates/buffer-seed.md` at the moment of its founding — copied from its `# Architect buffer` heading down, the folder's number filling that title — and write `address.md`."
  The paragraph's next sentence, "Either way the buffer exists before any editor does.", stays. The earlier refresh sentence ("you also read the standing entries of `templates/buffer-seed.md` against the buffer's, matching an entry by its bold lead-in, …") stays word for word. Re-wrap only the lines the edit touches, at the paragraph's existing column (about 72 characters).

### Verify

- [x] **Run the sweep again** (depends on both edits)
  Files: none (read-only)
  The searches run on the source, so check any match that a line break splits by reading the paragraph.
  - `grep -rn "copied whole\|copies it whole\|seeded in full" src/ docs/ CLAUDE.md` must return nothing.
  - `grep -n "^# " src/skills/agent-architect/templates/buffer-seed.md` must list exactly two headings, `# Buffer seed — the architect's memory at founding` and `# Architect buffer — <this folder's number>`, in that order.
  - `grep -n "Architect buffer" src/skills/agent-architect/SKILL.md` must return the founding passage.
  - `git diff` must show that nothing changed in the seed from `## Team` down or in the skill outside the founding clause.
