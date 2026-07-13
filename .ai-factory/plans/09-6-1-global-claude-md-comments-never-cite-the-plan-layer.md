# Plan: 6.1 — global CLAUDE.md: comments never cite the plan layer

## Context
Land the single authoritative rule forbidding durable code/test comments from citing the fluid plan layer (phase/note numbers, `ROADMAP`/`Plan` references, `.ai-factory/` paths) into the global instructions, so a pruned-and-reused number can never turn a stamped citation into a confident false pointer.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Append the prohibition bullet

- [x] **Task 1: Add the "Comments never cite the plan layer" bullet to § "Documentation style"**
  Files: `src/global/CLAUDE.md`
  In § "Documentation style", insert exactly one new bullet immediately **after** the "Describe behavior, not code." bullet (the first bullet, currently line 15), before "No file/directory trees.". The bullet text is verbatim from the spec, no additions:
  ```markdown
  - **Comments never cite the plan layer.** No code or test comment carries a phase/note number, a `ROADMAP`/`Plan` reference, or an `.ai-factory/` path.
  ```
  Constraints (per spec `.ai-factory/specs/58-global-comments-never-cite-plan-layer.md`):
  - **Pure prohibition only** — no positive/"link `docs/` instead" limb, no second sentence, no provenance sentence. A positive limb would provoke doc-citation flooding; the operational "instead" lives in the orchestrator's implementer prompt (spec 18), never here.
  - **Additions only** — every existing line in the file must stay byte-identical; the edit adds exactly one line.
  - Do not touch any other section, skill, or doc.
  - Verify after the edit: `grep -n "Comments never cite the plan layer" src/global/CLAUDE.md` → one hit inside § "Documentation style"; `git diff src/global/CLAUDE.md` → exactly one bullet added, no other line changed.
