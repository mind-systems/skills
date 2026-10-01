# Plan: 68.1 — a route target may be a phase, and a phase counts its touches

## Context
`src/skills/orchestrator-artifacts/SKILL.md` § "6. Status-marker grammar" admits only an open task's spec as the target of `[routed → <path>]`. This task widens the routed bullet to admit a phase (`[routed → <roadmap path> § Phase N]`) and adds one paragraph defining a phase's `**Touches:** N` count. Both texts are pinned verbatim in the task spec `.ai-factory/specs/trickster77777/191-a-route-target-may-be-a-phase-and-a-phase-counts-its-touches.md` § "What must be true after". Only this one file changes. Per the spec's § "What breaks on contact", `task-rescue` cites § 6 without restating the target, `roadmap-prune` reads only that a bracketed marker is present (its own sentence is task 68.2, not this one), and the orchestrator never parses markers. None of them changes here.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Grammar edit

- [x] **Replace the routed bullet in § "6. Status-marker grammar"**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Replace the two-line bullet that begins `` - `[routed → <path>]` — routed into an **open** task's spec; `` (and its continuation line `an editable surface (the task spec of an open task), never a completed or frozen one`) with the spec's pinned text, word for word:
  "- `[routed → <path>]` — routed into an **open** task's spec, or onto a phase as `[routed → <roadmap path> § Phase N]`, `<roadmap path>` being the roadmap file's repo-root-relative path — `.ai-factory/ROADMAP.md`, or `.ai-factory/roadmaps/<slug>.md` for a named roadmap; the target must resolve to an editable surface (the task spec of an open task, or a phase still in the roadmap), never a completed or frozen one"
  Wrap the bullet the way the file already wraps: the existing column width (about 85 chars) and a two-space continuation indent under the `- `. Only line breaks may differ from the pinned text. Never break a line inside a backtick span, so `` `[routed → <roadmap path> § Phase N]` `` stays on one line. Leave the `[fixed]` and `[dismissed]` bullets and the intro paragraph above them byte-identical.

- [x] **Add the touch-count paragraph after the dedup rule** (depends on the routed-bullet edit)
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Insert a new paragraph right after the paragraph that ends `review files (dedup by `Affects:` target + gist).` and before the `**Legacy markers**` paragraph. Separate it from both with one blank line. Use the spec's pinned text word for word:
  "A phase is a route target too. Routing a distinct finding onto a phase adds one to that phase's touch count, a `**Touches:** N` line kept in the phase note, or in the phase's preamble while the phase has no note; a count of one is not written, so the line first appears at two. The count is one per distinct finding, not per occurrence the dedup rule pins. It is a hint for sorting the roadmap and never a rule; a missed count costs nothing."
  Wrap it at the file's column width, as above; `` `**Touches:** N` `` must not split across lines. Leave the frontmatter, all section headings, the "Pinned"/dedup paragraph, the Legacy markers paragraph and § 7 untouched. Afterwards, confirm with `git diff` that only these two hunks changed and that, once line breaks are collapsed, the new texts match the spec's quotes character for character, including the `→` and `§` characters and the em dashes.
