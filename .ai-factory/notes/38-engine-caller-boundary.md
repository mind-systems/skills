# roadmap-engine: drop caller knowledge; roadmap-decompose stops duplicating the engine's format inline

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- `src/skills/roadmap-engine/SKILL.md` names its callers twice — description: "Currently loaded by roadmap-decompose; retained as forward-looking shared-format infra…", body: "The calling philosophy skill (currently `roadmap-decompose`) stays in control…". Both are stale (outline, decompose, and skeleton all load it now) and wrong by design: an engine is caller-agnostic and must not track who loads it (user: "он не знает о своих наследниках, да ему и без разницы").
- `src/skills/roadmap-decompose/SKILL.md` Mode 1.3 embeds a copy of the roadmap file format (the `# Project Roadmap / > vision / ## Milestones / - [ ] **Task Name** — …` fenced block) — duplicated engine content, violating the repo's own composition rule ("do not copy the engine's machinery — load it and let it stay in control of its own content").

## Details

### roadmap-engine edits

- **Description:** remove the "Currently loaded by roadmap-decompose; retained as forward-looking shared-format infra for the rest of the roadmap family" sentence — describe only what the engine holds (the two-tier format) and that it is load-once, caller-agnostic.
- **Body:** "The calling philosophy skill (currently `roadmap-decompose`) stays in control" → "The calling philosophy skill stays in control" (no caller named).

### roadmap-decompose edit

- **Mode 1.3:** replace the fenced roadmap-format block with a short instruction: draft in memory per `roadmap-engine`'s roadmap file format (contract lines with `` Spec: `<note pending>`. `` placeholders) — the engine is loaded at 1.3 anyway for drafting; do not restate its format. Keep the milestone rules list (atomic, gate, ordering, `[x]` marking) — that is decompose's own philosophy, not engine content.
- Verify no other inline restatement of the engine's format remains in decompose (Mode 2.4 / 2.5 reference the engine by name — those are correct as-is).

## What NOT to do

- Do not move any decomposition philosophy (atomicity gate, ordering, split rules) into the engine — it holds format only.
- Do not add a caller registry or "used by" list anywhere in the engine.
- Do not change the two-tier format itself — this is a boundary cleanup, not a format change.
