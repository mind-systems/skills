# Task — roadmap-outline emits phase headers; decompose/skeleton emit numbered tasks

**Date:** 2026-07-05
**Source:** tradeoxy planning session (GUI Limit Order Intents direction) — the format below was converged on live, against real broker + GUI roadmaps.

## 1. Frame

The roadmap family (`roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`) currently shares one output shape: all three write checkbox task bullets. The tradeoxy session settled a two-level roadmap grammar where **outline owns phase headers and the numbering spine, decompose/skeleton own the tasks under them** — the skills must split accordingly.

## 2. Read-first map

### Must-read now

- `tradeoxy_broker/.ai-factory/ROADMAP.md` — the reference implementation of the grammar (section below `---STOP---`: `## Limit Order Intents` → `### Phase 1 - Intent Store` → `- [ ] **1.1 ...**` tasks).
- `tradeoxy_gui/.ai-factory/ROADMAP.md` — second example, and the one that exercised the cross-section numbering rule (`## Limit Order Intents — GUI surfaces` → `### Phase 9` … `### Phase 12`, continuing after an earlier section's Phase 8).
- `src/skills/roadmap-outline/SKILL.md` — hook (a) currently says "each entry is a high-level goal" rendered as a contract line; this is what changes to phase-header emission.
- `src/skills/roadmap-decompose/SKILL.md` + `src/skills/roadmap-decompose-skeleton/SKILL.md` — gain the task-numbering rule (`N.M` under their phase).

### Read on demand

- `src/skills/roadmap-engine/SKILL.md` — the shared file-format section still shows a flat milestone list; decide whether the phase-header grammar lives there or in outline's hooks (see Open question).

## 3. The settled grammar

```markdown
## <Direction name>                          ← direction section (## header)

<direction preamble: source handoff/spec links, hard rules, gating>

### Phase N — <Phase title>                  ← outline writes THESE

<phase intro as prose, no checkbox: gate ("blocked on X"), the problem today,
key contracts / pinned decisions the phase rests on>

- [ ] **N.1 — <Task name>** — <contract line per roadmap-engine two-tier
  format>. Spec: `.ai-factory/specs/<NN>-<slug>.md`.   ← decompose/skeleton write THESE
- [ ] **N.2 — <Task name>** — … Spec: …
```

Division of labor:

- **`roadmap-outline`** emits `### Phase N — Title` subheadings with a prose intro paragraph — **never checkbox bullets**. A phase is not a task; it has no `[ ]`, no `Spec:` tag of its own. The intro paragraph absorbs what used to be the milestone contract line (gate, problem, key contracts).
- **Phase numbers are globally sequential integers across the whole roadmap file** — a new direction section continues from the highest existing phase number in ANY section, never restarts at 1. (tradeoxy_gui precedent: "Core Integration" ends at Phase 8, so the intents section starts at Phase 9 — the user first asked for "8.." and it collided with the existing Phase 8; uniqueness across the file is the point, so the orchestrator can address a phase without naming its section.)
- **`roadmap-decompose` and `roadmap-decompose-skeleton`** emit tasks as flat checkbox bullets directly under the phase header, numbered `**N.M — Name**` where `N` is the parent phase number and `M` is a 1-based ordinal within the phase. Everything else about a task is unchanged: two-tier per `roadmap-engine` (contract line + spec note + `Spec:` tag), atomicity gate, dependency ordering.

## 4. Error log (from the live session — the cases the split must prevent)

- The GUI session's first rendering made phases themselves checkbox milestone bullets and nested the task under one with indentation (`  - [ ] **9.1 …**`). Corrected by the user against the broker roadmap: phases became `###` headers, tasks became flat top-level bullets. The current outline skill's "entry = contract line" hook reproduces exactly this mistake.
- Phase numbering restarted at 1 inside the new section (Phase 1–4), colliding with the existing "Core Integration" Phase 1–8 in the same file. Renumbered to 9–12. Cross-references inside contract lines had to be chased manually ("blocked on Phases 9 and 10", "Replaces Phase 11's REST seeding") — numbering rules belong in the skill so this is done once, correctly.

## 5. Next step

Update the three skills: `roadmap-outline` hook (a) rewritten to phase-header emission + global sequential numbering + prose intro; `roadmap-decompose` and `roadmap-decompose-skeleton` granularity hooks gain the `N.M` numbering rule (N from the parent phase header they decompose). Keep `roadmap-engine` caller-agnostic per the established engine-caller boundary (note 38).

## 6. Open question

Where does the phase-header grammar live — in `roadmap-engine`'s "Roadmap File Format" section (shared rendering, callers reference it) or entirely in `roadmap-outline`'s hooks (engine stays a flat-list format, outline layers headers on top)? The engine currently shows a flat `## Milestones` list that no longer matches either tradeoxy roadmap below `---STOP---`.
