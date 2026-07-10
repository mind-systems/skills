# aif-architecture: pyramid pass — matrix and templates behind pointers, alignment check intact

## Current state

`src/skills/aif-architecture/SKILL.md` (236 lines) carries its lens (Step 0 context from the project CLAUDE.md, Step 1 recommendation flow, Step 1.5 Codebase Alignment Check, Step 3 CLAUDE.md pointer line) together with inline mass: the full decision matrix and the ARCHITECTURE.md template with both policy branches. A `references/` dir already exists (`references/architecture.md` is a mandatory read).

## Change

One pyramid pass:

- **Body keeps:** the step flow, the Alignment Check, the CRITICAL `references/architecture.md` read, the `## Features` reserved-section rule, the CLAUDE.md pointer contract.
- **Move to `references/`:** the decision matrix and the full ARCHITECTURE.md template (both policy branches) — read at the step that uses them.
- **Verbatim-protected:** the Alignment Check procedure, the template's reserved `## Features` section, the recommendation flow's decision wording.
- Two-reader register.

## Guards

- **Behavior-identical** — same recommendation on the same codebase, same generated ARCHITECTURE.md; moved text byte-identical.
- Frontmatter unchanged.
- Live baseline before the next phase task: run on a real project pre/post; diff the recommendation and the generated file.

## Verification

- Body materially slimmer; matrix/template behind pointers; baseline diff of the generated ARCHITECTURE.md → empty.
