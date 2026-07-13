# Plan: 5.8 — wording tightenings from the observation pass

## Context
Three one-clause wording fixes flagged by the observation pass, bundled into one task by explicit user decision: point `roadmap-engine`'s hook (c) at the resolution order, replace two literal `ROADMAP.md` back-references in `roadmap-decompose-skeleton` with "the source roadmap", and correct `orchestrator-artifacts`'s "only writer" to "only skill-side writer". Zero behavior change — every other sentence in the three files stays byte-identical.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Wording fixes

- [x] **Task 1: Point roadmap-engine hook (c) at the resolution order**
  Files: `src/skills/roadmap-engine/SKILL.md`
  On line 137, hook (c) reads: `The engine never infers this; the caller resolves it before Step 0 runs.` Append one clause pointing at the `## Named roadmaps` section (line 49) that defines the resolution order — e.g. `…the caller resolves it before Step 0 runs (per the `## Named roadmaps` resolution order).` Body-only edit; the frontmatter is owned by 5.5 and must not be touched. Change only this sentence — every other line byte-identical. Verify: `grep -n "Named roadmaps" src/skills/roadmap-engine/SKILL.md` shows hook (c) now references the section.

- [x] **Task 2: Replace the two literal `ROADMAP.md` back-references in roadmap-decompose-skeleton** DEVIATION: plan's verify command / the render-target replacement wraps "same" (line 113) and "source roadmap" (line 114) across lines just like the original `ROADMAP.md` text did, so plain `grep -n 'same source roadmap'` reads 0 hits too — confirmed correct instead via multiline grep (`same\nsource roadmap` matches lines 113-114) and direct file read; both phrases render as intended.
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Two literals name the default file where they mean the Step-0-resolved source roadmap; both become "the source roadmap", keeping each sentence's bold-emphasis structure.
  - Line 113–114 (Step 4 render target): `render into the **same ` + "`ROADMAP.md`**` the source tasks live in` → keep the emphasis but name the resolved roadmap, e.g. `render into the **same source roadmap** the source tasks live in`.
  - Line 125–126 (disposition insert): `**Insert** … immediately **before** it in ` + "`ROADMAP.md`." → `… immediately **before** it in the source roadmap.`
  Change only these two phrases; the surrounding sentences stay byte-identical. Verify: `grep -n 'same source roadmap' src/skills/roadmap-decompose-skeleton/SKILL.md` → exactly 1 hit after the edit (the render-target line). Do **not** use `grep 'same .ROADMAP'` — the target text wraps across lines 113–114, so `same` and `ROADMAP` never share a line and that pattern reads zero both before and after, a false pass.

- [x] **Task 3: Correct "only writer" to "only skill-side writer" in orchestrator-artifacts**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  On line 44 the `step` field description reads `… live in `milestone-rescue`, its only writer),`. The orchestrator also writes `step` (`plan_review_failed:N`, `review_failed:N`), so rescue is only the skill-side writer. Change `its only writer` → `its only skill-side writer`. Nothing else on the line changes. Verify: `grep -n "only skill-side writer" src/skills/orchestrator-artifacts/SKILL.md` → exactly 1 hit after the edit. Do **not** verify with `grep "only writer"` — after the edit the phrase is `only skill-side writer`, which has no contiguous `only writer` substring, so that pattern reads zero and would falsely signal a missing edit.
