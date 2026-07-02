# Plan: roadmap-engine: drop caller knowledge; decompose stops inlining the engine's format

## Context
Make `roadmap-engine` truly caller-agnostic (remove both stale caller mentions) and stop `roadmap-decompose` Mode 1.3 from restating the engine's roadmap-format block — replace it with a pointer while keeping decompose's own milestone philosophy.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Engine boundary cleanup

- [x] **Task 1: Drop caller names from roadmap-engine frontmatter description**
  Files: `src/skills/roadmap-engine/SKILL.md`
  In the frontmatter `description` (lines 3–8), remove the sentence "Currently loaded by roadmap-decompose; retained as forward-looking shared-format infra for the rest of the roadmap family." Rewrite so the description states only what the engine holds: the canonical two-tier roadmap artifact format (~600-char contract line + full spec note via `note`), caller-agnostic, load-once, no decomposition philosophy of its own. Do not name any caller. Keep it under the 1024-char frontmatter limit.

- [x] **Task 2: Drop the caller name from the roadmap-engine body**
  Files: `src/skills/roadmap-engine/SKILL.md`
  In the intro paragraph (around lines 17–21), change "The calling philosophy skill (currently `roadmap-decompose`) stays in control" → "The calling philosophy skill stays in control" — remove the parenthetical caller name. Leave the rest of the paragraph (load-once rule, format-vs-philosophy boundary) unchanged. Do not add any "used by"/caller registry anywhere. The `## Roadmap File Format` section and the two-tier format itself stay byte-identical.

### Phase 2: Decompose stops inlining the engine's format

- [x] **Task 3: Replace the fenced roadmap-format block in decompose Mode 1.3 with a pointer to the engine**
  Files: `src/skills/roadmap-decompose/SKILL.md`
  In **1.3: Generate draft roadmap** (around lines 89–108), remove the fenced ```markdown``` block that duplicates the engine's roadmap file format (`# Project Roadmap` / `> vision` / `## Milestones` / `- [ ] **Task Name** — …`, lines 93–102). Replace with a short instruction: draft the roadmap in memory (do not write `$TARGET_FILE` yet) per `roadmap-engine`'s roadmap file format, using placeholder `` Spec: `<note pending>`. `` tags on the contract lines. `roadmap-engine` is already declared in `loads:` and referenced elsewhere in the file — do not restate its format. Keep the existing **Rules for milestones** list (atomic/one-concern, per-milestone spec draft → Atomicity Gate → draft contract line, ordering by dependencies, `[x]` marking) exactly as-is — that is decompose's own philosophy, not engine content. Do not touch Mode 1.3.1 (Atomicity Gate) or Steps 1.4 / 2.4 / 2.5.

- [x] **Task 4: Verify no other inline restatement of the engine's format remains in decompose**
  Files: `src/skills/roadmap-decompose/SKILL.md`
  Grep the file for any remaining copy of the engine's format block (`# Project Roadmap`, `## Milestones` fenced templates, contract-line rule lists). Confirm the only remaining references to the format are by-name pointers to `roadmap-engine` (Steps 1.4/2.4/2.5 and Critical Rule 6 are correct as-is). No format changes, no caller registry, no moved philosophy.

## Notes
- Guard (from spec note 38): do NOT change the two-tier format itself, do NOT move any decomposition philosophy (atomicity gate, ordering, split rules) into the engine, do NOT add a caller/"used by" list anywhere. Never touch `upstream/ai-factory/`.
- Single commit at the end: "Make roadmap-engine caller-agnostic and stop decompose inlining its format"
