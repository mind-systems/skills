# Plan: 73.3 — the template writes the built design

## Context
`src/skills/aif-architecture/references/architecture-template.md` writes only the packaging. It has no place for what varies or for the composition root. This task replaces the whole file with the text pinned in the task spec `.ai-factory/specs/trickster77777/0210-the-template-writes-the-built-design.md` § "What must be true after". It also repins one sentence in `src/skills/aif/SKILL.md` that still promises "code examples". Tasks 73.1 (`b09ed48`) and 73.2 (`e09e147`) are committed, and the working tree is clean. The phase note says no document governs this skill, so no doc changes. This repository has no `.ai-factory/RULES.md`.

I re-ran the spec's three blast-radius sweeps while planning:
- `grep -rn "Decision Rationale\|Tech stack:\*\*" src docs CLAUDE.md` finds the template and `src/skills/roadmap-test-coverage/SKILL.md` (Stack resolution, "Primary"). That skill reads `## Decision Rationale` → `- **Tech stack:** ...` verbatim. It keeps working only if the heading and its three bullets stay byte-identical. They move, but their text must not change, and `roadmap-test-coverage` is not edited. The hits in `aif-architecture/SKILL.md` ("Tech stack (language, framework, …)") are question prompts, not reads of the generated file, so they stay.
- `grep -rn -i "code examples\|code example" src docs CLAUDE.md --include="*.md"` finds:
  - the template, which is replaced
  - the `aif` sentence under "**Final step: Generate Architecture Document**", which is repinned
  - `aif-docs` (`SKILL.md`, `references/REVIEW-CHECKLISTS.md`, `references/generate-state-a.md`), which talks about documentation in general, so it stays
  - `aif-architecture/references/architecture.md` § "Code Examples (Language-Agnostic Pseudo-Code)", which is the reference's own teaching material and not the generated file's shape, so it stays
- `grep -rn "Legacy vs New\|Code Organization Note\|Option 1\|Option 2" src docs CLAUDE.md --include="*.md"` finds only the template.

`aif-architecture/SKILL.md` refers to the template by its path, and to the trailing empty `## Features` section ("MUST end with an empty `## Features` section"). The new template still ends with that section, so `SKILL.md` is not touched here. Its Step 0, Step 1, Step 1.5 and Step 3 are rewritten in 73.4.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the template

- [x] **Replace `architecture-template.md` with the pinned text**
  Files: `src/skills/aif-architecture/references/architecture-template.md`
  Overwrite the whole file with the text between the outer `~~~~` fences in the spec's § "What must be true after". The `~~~~` fence lines are not part of the file. The first line of the file is `Output template for the generated `ARCHITECTURE.md`. …`, and the last line is the final rule bullet, `- Base the generated folder structure on the user's decision in Step 1.5 … without user consent.`. End the file with one trailing newline, as it does today.
  Copy every character from the spec:
  - Keep the backslash-escaped inner fences `\`\`\`` around the Folder Structure block exactly as written. The current file uses them too. Do not turn them into real backticks.
  - Keep the outer ```` ```markdown ```` / ```` ``` ```` fence around the template body.
  - Keep the ✅/❌ glyphs, the em dashes, the straight apostrophes, and the `**…**` bold markers.
  - Keep the bracketed guidance lines, including `[Only if the user explicitly asked for a migration target in Step 1.5, add the following section:]` and `[For existing code, unless a migration target was asked for, add the following lighter section:]`.
  - Keep the `<!-- roadmap-prune anchors … Leave empty. -->` comment under `## Features`.
  Do not hard-wrap, reword, or add anything.
  The sections now run in this order: `# Architecture: [Pattern Name]`, `## Overview`, `## What varies`, `## Composition root`, `## The rule`, `## Invariants`, `## Decision Rationale`, `## Folder Structure`, `## Dependency Rules`, `## Layer/Module Communication`, `## Key Principles`, `## Legacy vs New Code Policy`, `## Code Organization Note`, `## Living Examples`, `## Anti-Patterns`, `## Features`. After them comes **Rules for generation:** with nine bullets, starting with "Read the variation from the code before writing…".
  Check: `git diff` must show the `## Decision Rationale` heading and these three bullet lines unchanged, with no `-`/`+` pair on any of them:
  - `- **Project type:** [from CLAUDE.md / codebase]`
  - `- **Tech stack:** [language, framework]`
  - `- **Key factor:** [primary reason for this choice]`
  They only move, now sitting after `## Invariants`. Also check that `grep -n "Code Examples\|Option 1\|Option 2\|Adapt ALL examples" src/skills/aif-architecture/references/architecture-template.md` returns nothing.

### Repin the `aif` sentence

- [x] **Replace the "code examples" sentence in `aif`** (independent of the template task)
  Files: `src/skills/aif/SKILL.md`
  The paragraph under "**Final step: Generate Architecture Document**" today reads: "Invoke `/aif-architecture` to define project architecture. This creates `.ai-factory/ARCHITECTURE.md` with architecture pattern, folder structure, dependency rules, and code examples tailored to the project."
  Replace that whole line with the spec's pinned text, exactly: "Invoke `/aif-architecture` to define project architecture. This creates `.ai-factory/ARCHITECTURE.md` with the architecture pattern, what varies and where it is chosen, folder structure, dependency rules, and links to the documents that govern the invariants, tailored to the project."
  Write it as one physical line. Keep the backticks, but leave out the spec's outer quotes. Nothing else in the file changes.
  Check: `grep -rn -i "code examples" src/skills/aif/SKILL.md` returns nothing.
