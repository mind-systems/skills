# Plan: 59.2 — the buffer is seeded from a template at founding

## Context
A newly founded architect's buffer currently starts empty, so the pair rebuilds the same shape from memory each time. This task adds a skill-local seed template to `agent-architect` and one sentence in its SKILL.md that says to read the template once, when a new buffer is created. The content is pinned in the task spec `.ai-factory/specs/trickster77777/165-the-buffer-is-seeded-from-a-template-at-founding.md` (§ "What must be true after"). The rationale is in the phase note `153-the-buffer-is-born-with-a-shape.md`: seven rubrics with no zones and no *rescues* rubric, the counts rule written out in its own words, and the template kept out of `architect-editor-engine`. The governing spec is `docs/paired-loop.md` § "How the memory begins, and how it survives".

Ground truth checked before planning:
- `src/skills/agent-architect/` contains only `SKILL.md`. There is no `templates/` directory yet.
- `active/skills/agent-architect` is a directory-level symlink to `../../src/skills/agent-architect`. A new `templates/` subdirectory shows up in `active/` automatically, so no symlink work is needed.
- 59.1 has landed (commit `6391145`). The buffer-creation paragraph in § "Spawn once, message thereafter" is the first paragraph under that heading (it opens "Your own start comes before any editor exists"). It already carries 59.1's mid-paragraph clause "it is where your buffer's path and rules are defined". It ends with the sentence "Either way the buffer exists before any editor does.", which is split across two wrapped lines.
- The same section has a later sentence about the memory snapshot: "no command is invoked and no template is consulted". It is about the snapshot, not the buffer, so it does not conflict with this task and stays untouched.
- Precedent for a skill-local, read-once template: `src/skills/aif-docs/templates/html-template.html`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Seed template and its founding-time pointer

- [x] **Create the buffer seed template**
  Files: `src/skills/agent-architect/templates/buffer-seed.md` (new; creates the `templates/` directory)
  Write the file with the markdown block from the task spec § "What must be true after", byte for byte. Keep its title line, its read-once preamble, and exactly seven `##` rubrics in this order: Where things stand, Rulings in force, Method, Orientation, Ledger, Candidates — not tasks, Current thread. Each rubric keeps its angle-bracket guidance line. The **Standing entry — the counts rule** paragraph goes under `## Method`, in its own words. Do not add any of the following:
  - a zone or a settled/live split
  - an eighth rubric, including a *live* heading or a *rescues* heading
  - a handle or pairing-role slot, since `architect-editor-engine` already covers those
  - any link or path to `docs/counts-go-stale.md` or to anything under `.ai-factory/`. The template travels to other projects where those files do not exist.
  Copy the spec's hard line wraps inside the angle-bracket lines and the counts paragraph exactly as written.

- [x] **Append the founding sentence to the buffer-creation paragraph** (depends on Create the buffer seed template)
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", find the first paragraph (the one ending "Either way the buffer exists before any editor does."). Add this sentence right after that final sentence, verbatim from the spec:
  "A newly created buffer is seeded in full from `templates/buffer-seed.md` at the moment of its founding — read once, copied whole, never reread for a buffer that is merely resumed."
  Continue the paragraph's existing hard wrap of about 72–76 columns. Only the paragraph's last line may change, and only by gaining trailing text; the new sentence then continues on new wrapped lines before the blank line. Leave every earlier line of the paragraph byte-identical. That includes 59.1's clause "it is where your buffer's path and rules are defined" and the "no such pointer means you are a new architect and create your own buffer first…" sentence. Do not touch the frontmatter (`loads:` stays `architect-editor-engine architect-pairing-engine`, since the template is a file and not a skill), any other paragraph, or the snapshot paragraph's "no template is consulted" sentence.

### Blast-radius confirmation

- [x] **Run the spec's sweep and confirm path references** (depends on both tasks above)
  Files: none edited (read-only)
  Run `grep -rln "agent-architect/templates\|buffer-seed" src/ docs/ .ai-factory/`. The spec's rule applies:
  - Path references to the new file should appear only in this task's own artifacts (the roadmap contract line in `.ai-factory/roadmaps/trickster77777.md` and spec `165-…`), plus the new template and the SKILL.md sentence this task writes.
  - Phase note `153-the-buffer-is-born-with-a-shape.md` matches only on the prose phrase "a once-only buffer-seed template". That is not a path reference, so no edit.
  - Plan and review files under `.ai-factory/plans/` and `.ai-factory/reviews/` for this task are working artifacts, not claims on the path.
  If any other file names the path, report it instead of editing it. Nothing under `docs/` is written.
