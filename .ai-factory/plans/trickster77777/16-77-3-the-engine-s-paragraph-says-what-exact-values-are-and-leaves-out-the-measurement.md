# Plan: 77.3 — the engine's paragraph says what exact values are and leaves out the measurement

## Context
Rewrite the "What a task spec holds" paragraph in `src/skills/roadmap-engine/SKILL.md` so that "exact values" is defined as the code's own values (a literal, a symbol, a type, a path), the reader who does not re-derive is the planner rather than the implementer, and the "Nothing else means" list gains a measurement-of-the-tree clause with its reason. The task spec (`.ai-factory/specs/trickster77777/0217-a-spec-names-its-sets-and-does-not-measure-the-tree.md`, § "What must be true after") pins the full paragraph verbatim and is the authority; this brings the engine into agreement with `docs/what-a-task-carries.md` § "What a spec holds", already changed by 77.2.

Ground truth at planning time: the paragraph is the bold lead-in `**What a task spec holds:**` in `src/skills/roadmap-engine/SKILL.md`, hard-wrapped at roughly 88 columns, with `Nothing else means, concretely:` starting on its own line directly after `*what breaks on contact*, pinned rather than hedged.` (no blank line between them), followed by a blank line and `**Never write a full spec inline in the roadmap**`. Its current text matches the spec's § "What is true now" quote word for word.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the paragraph

- [x] **Replace the "What a task spec holds" paragraph with the pinned text**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Replace the whole paragraph — from `**What a task spec holds:**` through `never as a prohibition standing in for it.` — with the text quoted in the spec's § "What must be true after", word for word and punctuation for punctuation (em dashes are literal `—`, italics `*what is true now*`, `*what must be true after*`, `*what breaks on contact*` kept). The three changes it carries, for orientation only — copy from the spec, not from this list:
  - after "read from the code with exact values" comes "— the code's own values, a literal, a symbol, a type, a path —";
  - "so the implementer does not re-derive it" becomes "so the planner does not re-derive it";
  - in the "Nothing else means" list, between the position clause and the fence clause, comes "no clause is a measurement of the tree — a count is false before the task is reached;", inserted before the existing "and" that opens the fence clause (i.e. "…never where to write it; no clause is a measurement of the tree — a count is false before the task is reached; and no clause fences off a neighbour by name — …").
  Keep the file's layout: hard-wrap the prose at the same width as the surrounding lines (~88 columns), start `Nothing else means, concretely:` on its own line directly after the line ending `pinned rather than hedged.` with no blank line between, and keep the single blank lines before `**What a task spec holds:**` and before `**Never write a full spec inline in the roadmap**`. Change nothing else in the file — no other paragraph, no frontmatter.

### Blast radius

- [x] **Run the spec's sweep and confirm nothing else restates the paragraph** (depends on Replace the "What a task spec holds" paragraph with the pinned text)
  Files: none edited
  Run the two searches from the spec's § "What breaks on contact":
  ```
  grep -l "roadmap-engine" src/skills/*/SKILL.md src/commands/*.md
  grep -rn "What a task spec holds\|exact values\|Nothing else means" src docs --include="*.md"
  ```
  Expected reach, per the spec's finding: the engine's callers depend on it only for format and flow and none restates the paragraph; the second search reaches the rewritten paragraph itself, `src/commands/command-pin-gaps.md` (points at the paragraph by name, "not restated here" — stays unchanged), and `docs/what-a-task-carries.md` § "What a spec holds" (already carries the same exact-values and measurement wording from 77.2 — stays unchanged). If a match outside this set restates what a task spec holds with another meaning of "exact values" or asks a spec to hold a measurement, stop and report it rather than editing it.
