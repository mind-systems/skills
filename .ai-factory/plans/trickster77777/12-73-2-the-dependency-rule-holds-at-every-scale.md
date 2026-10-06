# Plan: 73.2 — the dependency rule holds at every scale

## Context
`src/skills/aif-architecture/references/architecture.md` states the dependency rule only for the Explicit Architecture. Nothing in it names a pattern for the inside of a feature module or of presentation. This task adds one section, "The Dependency Rule at Every Scale". It goes between the section 73.1 added, "## Where the System Varies — Ports and Adapters", and "## Terminology". The section text is copied verbatim from the task spec `.ai-factory/specs/trickster77777/0209-the-dependency-rule-holds-at-every-scale.md` § "What must be true after". Task 73.1 is done (commit `b09ed48`), and its section sits right before `## Terminology` now. The phase note says no document governs this skill, so no doc is edited. There is no `.ai-factory/RULES.md`.

Blast radius: I re-ran the spec's two sweeps while planning.
- `grep -n -i "dependency rule\|point inward\|hexagonal\|strict downward\|viper\|mvvm" src/skills/aif-architecture/references/architecture.md` finds these, all of which stay:
  - the Explicit Architecture's "**Dependency rule:**" line and the "**Ports and Adapters (Hexagonal):**" principle, which are the system-edge case of the new section
  - 73.1's "also called hexagonal architecture" sentence
  - the Structured Modules' "**Separation from DDD:**" principle, which disclaims "rigid hexagonal ports". The new section describes a loose split, not a rigid one.
  - the Layered pattern's "**Strict Downward Dependencies:**", which the matrix's "Domain purity" row already scores
  - the Structured Modules' "**Strict Downward Flow:**" line (`Controllers → Services → Repositories`). The spec's finding does not name this one, but it falls under the same rule. It points presentation → deciding layer → data, which is the direction the new section states, so the section does not reverse it and the line stays.
- `grep -rn -i "viper\|mvvm" src docs CLAUDE.md --include="*.md"` finds nothing today. After the change, the only hits are in the new section.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Add the pinned section to the reference

- [x] **Insert "The Dependency Rule at Every Scale" before "Terminology"**
  Files: `src/skills/aif-architecture/references/architecture.md`
  This file does not hard-wrap. Each paragraph and each list item is one physical line, and blocks are separated by one blank line. Put the new section right after the last paragraph of "## Where the System Varies — Ports and Adapters", which ends with `and packaging is named second.`, and before the `## Terminology` heading. Keep one blank line between blocks.
  The section starts with the heading `## The Dependency Rule at Every Scale` and has, in this order:
  1. The paragraph "One rule — details depend on abstractions the core owns, never the reverse — holds at each scale … The scales nest; the rule does not change."
  2. A bullet list of three items, each on one line, with no blank lines between them. The items start with `- **The system's edge** — Ports and Adapters.`, `- **A feature module** — three responsibilities, …` and `- **The inside of presentation** — MVVM.`.
  3. The paragraph "This is Clean Architecture's dependency rule seen at each scale … the folders that follow from them are packaging, named second."
  Copy every character from the spec, including the `**…**` bold markers, the em dashes, the straight apostrophes in "system's", "Clean Architecture's" and "matrix's", and the inner double quotes around "Domain purity". The spec wraps the section in one pair of outer double quotes, the opening one before `## The Dependency Rule at Every Scale` and the closing one after `named second.`. Those quotes mark where the text starts and ends; they are not part of it, so leave them out. Do not add anything to the text, do not reword it, and do not hard-wrap it.

Nothing else in the file changes. The 73.1 section, the "Dependency rule" line, the "Ports and Adapters (Hexagonal)" and "Separation from DDD" principles, "Strict Downward Flow", "Strict Downward Dependencies" and the Decision Matrix all stay as they are. `git diff` must show only added lines.
