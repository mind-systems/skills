# Plan: 61.2 — the three parts exclude a check, a line, and a fence

## Context
In `src/skills/roadmap-engine/SKILL.md`, the **What a task spec holds** paragraph says "three parts and nothing else". It never says what a fourth part would be. This task adds one sentence that says it: no clause is a check that the instruction was carried out, none is a position in the file, and none fences off a neighbour. The task spec is `.ai-factory/specs/trickster77777/170-the-three-parts-are-the-whole-and-none-is-a-check-or-a-line.md`, and its § "What must be true after" pins the exact wording. The governing spec is `docs/what-a-task-carries.md`.

Ground truth checked before planning:
- The paragraph starts with `**What a task spec holds:** three parts and nothing else — *what is true now*, read`. It is hard-wrapped over four lines, each at most 85 characters.
- The paragraph ends with the line `*what breaks on contact*, pinned rather than hedged.` A blank line follows, then the `**Never write a full spec inline in the roadmap**` paragraph.
- Nearby paragraphs in the file wrap at about 84–90 characters and use no `> ` prefix.
- `src/commands/command-pin-gaps.md` cites the paragraph only by its heading text, `roadmap-engine`'s "What a task spec holds" paragraph. It does not quote the body.

Assumption: the new sentence goes into the file's own form. It is appended to the existing paragraph and hard-wrapped to the paragraph's width of about 85 characters. The spec's quote wrapping is not reproduced. The words, punctuation, em-dashes, and semicolons stay exactly as the spec pins them.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### State what a fourth part is not

- [x] **Append the exclusion sentence to the What a task spec holds paragraph**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Right after `pinned rather than hedged.` in the **What a task spec holds** paragraph, still inside that paragraph with no blank line, append this exact sentence. It is separated from the preceding text by one space or a line break:
  ```
  Nothing else means, concretely: no clause is a check that the instruction was carried out, which belongs to the review the orchestrator already runs; no clause is a position in the file — each states what the artifact must hold, never where to write it; and no clause fences off a neighbour by name — scope is stated positively, as what the task changes, never as a prohibition standing in for it.
  ```
  Hard-wrap the appended text to the paragraph's existing width, with lines of about 85 characters or fewer. Line breaks may fall only between words. The words themselves must not change.
  Leave all of these byte-identical: the bold heading text `**What a task spec holds:**` (`command-pin-gaps` cites it by name), the three existing clauses and their current line breaks, the **Why two tiers** paragraph above, the **Never write a full spec inline in the roadmap** paragraph below, the blank lines around the paragraph, the frontmatter (including `loads: note`), the reverse-graph marker line, and every other section of the file.
