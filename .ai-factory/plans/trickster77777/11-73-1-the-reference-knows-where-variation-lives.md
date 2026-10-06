# Plan: 73.1 — the reference knows where variation lives

## Context
`src/skills/aif-architecture/references/architecture.md` scores packaging patterns and teaches ports only as interfaces to external systems. It does not say where a system varies. This task adds three texts, a note after the matrix, a new section on variation axes and ports, and one line under the Quick Decision Guide. All three are copied verbatim from the task spec `.ai-factory/specs/trickster77777/0208-the-reference-knows-where-variation-lives.md` § "What must be true after". The phase note `.ai-factory/specs/trickster77777/0206-aif-architecture-describes-folders-and-misses-where-the-system-varies.md` says no document governs this skill, so no doc is edited. There is no `.ai-factory/RULES.md`.

Blast radius: I re-ran the spec's two sweeps while planning, and they match the spec's finding.
- `grep -n -i "simpl\|external" src/skills/aif-architecture/references/architecture.md` finds these, all of which stay:
  - the two guide lines "New project, small team, simple domain? → Layered" and "Simple CRUD app? → Layered Architecture"
  - the Layered section's "This is the simplest architectural pattern" and its "For small teams and simple CRUD applications" sentence, both statements about packaging
  - the "Port Abstraction for External Dependencies" principle, which stays true because external systems are one case of a port
  - folder-tree comments about external adapters
- `grep -rn -i "decision matrix" src docs CLAUDE.md` finds only the reference's own heading and two lines in `src/skills/aif-architecture/SKILL.md` Step 1. Task 73.4, which runs after this one, rewrites the first of those lines. The second, "Evaluate the project against the decision matrix", stays true. `SKILL.md` is not touched here.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Add the three pinned texts to the reference

- [x] **Insert the matrix note and the "Where the System Varies — Ports and Adapters" section**
  Files: `src/skills/aif-architecture/references/architecture.md`
  This file does not hard-wrap. Each paragraph is one physical line, and paragraphs are separated by one blank line. Put the new text right after the paragraph that opens with `**Note on subvariants:**` and before the `## Terminology` heading. Keep one blank line between blocks. The two texts go in this order:
  1. The note, as one paragraph. It starts with `**Note on what the matrix measures:**` and ends with `answered in "Where the System Varies — Ports and Adapters" below.` The inner double quotes around the section name are part of the text.
  2. The section. It starts with the heading `## Where the System Varies — Ports and Adapters` (with an em dash) and has seven paragraphs: "Ports and Adapters, also called hexagonal architecture…", "Packaging patterns answer…", "A **variation axis** is…", "A port is therefore not only…", "The rule that follows…", "A port that exists only so a test…", and "Variation is an axis of its own…". The section ends with `and packaging is named second.`
  Copy both texts character for character from the spec, including the `**…**` bold markers on **variation axis**, **port**, **adapter** and **composition root**, and the em dashes. The spec wraps each text in outer double quotes. Those quotes mark where a text starts and ends; they are not part of the text, so leave them out. Do not add anything to the text, do not reword it, and do not hard-wrap it.

- [x] **Add the packaging-only line under "Quick Decision Guide"** (depends on the previous task only for its position in the file)
  Files: `src/skills/aif-architecture/references/architecture.md`
  Between the `## Quick Decision Guide` heading and the `` ```text `` code block, add this paragraph, with one blank line before it and one after:
  ```
  Each line below picks packaging only; none says anything about where the system varies.
  ```
  Do not change the code block's lines.

Nothing else in the file changes. The Decision Matrix table, the "Port Abstraction for External Dependencies" principle, the "Port and Adapter (Dependency Inversion)" example and the Layered section all stay as they are. `git diff` must show only added lines.
