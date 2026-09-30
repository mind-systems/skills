# Plan: 66.3 — the drain names its second destination

## Context
`src/skills/architect-editor-engine/SKILL.md` gives the buffer's drain one destination, in both its § "The architect's buffer" and its frontmatter description. `docs/paired-loop.md` § "Where the pair's behaviour lives" gives it two: a project or skill ruling goes to its artifact, and the pair's base behaviour goes to the seed and stays as a standing entry. The doc also says that what was said twice or failed twice is a debt to drain. This task makes the engine's drain paragraph and its description clause match the doc. The spec `.ai-factory/specs/trickster77777/188-the-drain-names-its-second-destination.md` pins both texts verbatim.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Engine text

- [x] **Replace the drain paragraph in § "The architect's buffer"**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  In § "The architect's buffer", find the paragraph that begins "A ruling recorded in the buffer is a debt against the skill, not a record of one." It sits between the channel-message paragraph and the "Two architects are two heads" paragraph. It currently reads in full: "A ruling recorded in the buffer is a debt against the skill, not a record of one. It leaves the buffer when it reaches the artifact that should hold it; without that drain the buffer accumulates decisions everyone follows and no artifact states." Replace the whole paragraph with exactly this text (from the spec § "What must be true after"). Keep it as one line, like the other paragraphs in that section:

  > A ruling recorded in the buffer is a debt against the skill, not a record of one, and it drains to one of two places. A ruling about the project or its skills leaves the buffer when it reaches the artifact that should hold it; without that drain the buffer accumulates decisions everyone follows and no artifact states. The base behaviour of the pair drains to the seed the buffer is founded from and stays in the buffer as its standing entry, which both halves re-read all session. Something the user had to say twice, or that failed twice, is a debt to drain; said once, it is not.

  Do not change any other paragraph in the section.

- [x] **Replace the drain clause in the frontmatter description**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  The `description: >-` folded scalar contains the clause "the drain rule that a ruling leaves the buffer once it reaches the artifact that should hold it,". It currently wraps across two lines, starting at "memory on change, and the drain rule that a ruling leaves the buffer once it". Replace that clause with exactly:
  "the drain rule — a project or skill ruling leaves the buffer once it reaches the artifact that should hold it, the pair's base behaviour goes to the seed and stays as a standing entry, and what was said or failed twice is a debt to drain —"
  Leave the text around it untouched: "…the editor's re-read of the memory on change, and " stays before the clause, and " and the rule that no architect reads another's buffer…" stays after it. Re-wrap only the affected lines of the folded scalar. Use two-space indentation and keep lines at roughly the current width (about 80 columns). Do not change any other frontmatter field.
  Length check: after the change, the folded description (lines joined with single spaces) must be at most 1024 code points. With the pinned clause it comes to 1010 code points; today it is 867. To verify, join the indented lines under `description:` with single spaces and count them with `python3 -c` using `len()` on the str, which counts code points. Confirm the result is ≤ 1024.

### Blast radius

- [x] **Confirm no other text needs to change** (depends on both tasks above)
  Files: none (verification only)
  Run the sweep from the spec: `grep -rn -i "drain" src/ docs/ CLAUDE.md`. Expected hits:
  - The engine's own paragraph and description, which are the target of this task.
  - `src/skills/agent-architect/SKILL.md`, the sentence in § "Your buffer is shared; you alone write it" that lists "the drain rule" as `architect-editor-engine`'s without restating it. It stays unchanged.
  - `src/skills/roadmap-decompose-skeleton/SKILL.md`, a heap-drain example. It is unrelated and stays unchanged.
  - `docs/paired-loop.md`, which already states both destinations and the threshold. It stays unchanged.
  - `CLAUDE.md`, the Paired loop row of the documentation index ("…its drain going to an artifact or, for base behaviour, to the seed, what was said or failed twice a debt…"). It already names both destinations and the threshold, so it stays unchanged.

  If the sweep finds any other text that states the drain with a single destination, stop and report it. Do not edit files outside `src/skills/architect-editor-engine/SKILL.md`.
