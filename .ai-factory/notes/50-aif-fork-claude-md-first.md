# aif: fork into src/ — targeted edits only; CLAUDE.md becomes the first artifact

**Date:** 2026-07-02
**Source:** conversation context (aif/aif-architecture review)

## Key Findings

- The skill works well overall — this is **not a rework**. Fork it (copy `upstream/ai-factory/aif` → `src/skills/aif`, repoint `active/skills/aif` → `../../src/skills/aif`) and make **targeted edits only**; the logic, mode flow, and section structure stay untouched, so a diff against upstream shows exactly what was cut and added, nothing reshaped.
- Today the user hand-writes CLAUDE.md first and only then runs `/aif` for the rest — the skill should produce CLAUDE.md itself, as the first artifact.

## Details

### Untouched (the bulk of the skill)

Three-mode skeleton and detection, skills.sh acquisition + security scanning, Python detection, MCP configuration, `rules/base.md`, language resolution logic, **config.yaml machinery verbatim** (`update-config.mjs` + template + payload protocol — the user keeps this file), the final `/aif-architecture` invocation, "CRITICAL: Do NOT Implement".

### Edit 1 — CLAUDE.md as the first artifact

In every mode, before the other artifacts: generate the project's `CLAUDE.md` following the user's conventions — `## Purpose`, `## Commands` (from the detected package manager / Makefile), stack facts, a `## Documentation` index section (empty if no docs yet); `## Status` when the project has a real built/target gap worth stating. Content sources, in order of availability: the chat context when the conversation already carries the project intent (the common case, not a requirement), `$ARGUMENTS`, the stack scan, user answers from the mode's existing dialogs. If CLAUDE.md already exists — update only missing sections, never clobber.

### Edit 2 — drop DESCRIPTION.md generation

Remove the DESCRIPTION.md creation steps from all modes (the artifact is retired, note 52). Where later steps reference DESCRIPTION.md as input (e.g. `/aif-architecture` hand-off), the reference point becomes the generated CLAUDE.md.

### Edit 3 — AGENTS.md stays, but as the one-line pointer

Keep the AGENTS.md generation step, replace the multi-section template (Project Overview / Tech Stack / directory tree / Documentation table / AI Context Files) with the standing convention:

```markdown
See [CLAUDE.md](CLAUDE.md) as the single source of truth for this project.
```

### Edit 4 — drop the dead machinery block

Remove the `skill-context`/aif-evolve block (same cut already applied to `aif-docs`, note 49 — the machinery exists in no project).

### Repo bookkeeping

- `ln -sfn ../../src/skills/aif active/skills/aif`.
- Update skills-repo `CLAUDE.md`: `aif` moves from "upstream originals used as-is" to the reworked-from-upstream reconcile-by-diff list (alongside `aif-docs`); upstream mirror stays pristine.

## What NOT to do

- Do not restructure modes, flows, or dialogs — logic unchanged; the four edits above are the whole task.
- Do not touch `upstream/ai-factory/aif`.
- Do not remove config.yaml, the language-resolution logic, or the marketplace/scanning sections.
- Do not bake in an assumption that a rich chat context is always present — it is the common case, not a precondition.
