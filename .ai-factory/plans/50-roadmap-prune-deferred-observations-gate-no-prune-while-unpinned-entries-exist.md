# Plan: roadmap-prune: deferred-observations gate — no prune while unpinned entries exist

## Context
Give `roadmap-prune` a read-only gate at the very top that refuses to run when any `## Deferred observations` entry in `plan-reviews/` or `reviews/` is unpinned, so the sweep never destroys observations before `milestone-rescue-audit prune` has processed them.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Wire the engine and gate

- [x] **Task 1: Add engine dependency and scan tools to frontmatter**
  Files: `src/skills/roadmap-prune/SKILL.md`
  In the YAML frontmatter add `loads: orchestrator-artifacts` (mirror the placement used in `src/skills/milestone-rescue/SKILL.md:14`). Extend `allowed-tools` (currently `Read Write Edit Bash(git *) Bash(rm *)`) with `Glob Grep` — the gate and the summary-report addition need read-only file scanning across the review dirs. Do not add any other tools; the sweep/commit tool grants stay as-is.

- [x] **Task 2: Add the deferred-observations gate above Step 1** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  Insert a new section as the **very first** step of the skill body, above `## Before you start`. Two parts, instructions only (no rationale prose — house rule):
  - A load-once line matching `milestone-rescue`'s wording (`src/skills/milestone-rescue/SKILL.md:34-36`): ensure `orchestrator-artifacts` is loaded once this chat (via the Skill tool, only if not already loaded) — it defines the `## Deferred observations` section format and the status-marker grammar / **pinned** definition referenced below. Reference the engine for the grammar and the pinned definition; never restate them here.
  - The gate procedure:
    1. Derive the target repo root from the skill argument (parent of the `.ai-factory/` holding the target ROADMAP.md) — same anchoring rule Step 5 already uses.
    2. Scan every `.md` file under `<target repo root>/.ai-factory/plan-reviews/` and `<target repo root>/.ai-factory/reviews/` for a `## Deferred observations` section. A file with no such section contributes nothing.
    3. Collect every entry line (`- Affects: <target> — <observation>`) that is **not pinned** per the engine's grammar (pinned = the entry line carries ≥1 bracketed status marker — do not redefine, cite the engine).
    4. If any unpinned entry exists → **stop the skill entirely**: print one line per unpinned entry as `<file>:<line> — <entry text>`, state that pruning is blocked until every entry is pinned, and name the resolution — run `milestone-rescue-audit` in prune mode (`milestone-rescue-audit prune`) first. Make **no** edits, no sweep, no ARCHITECTURE/ROADMAP changes, no partial prune.
    5. If none are unpinned → proceed to `## Before you start` and the normal flow, unchanged.
  Note the `ROADMAP_TESTS.md` parity explicitly: the gate scans the shared `plan-reviews/`/`reviews/` dirs identically in both modes; `test-runs/` files carry no review sections and are not scanned. Prune never promotes, evaluates, or marks entries — this gate is read-and-refuse only.

- [x] **Task 3: Extend Step 8 summary report with pre-standardization marker-phrase hits** (depends on Task 2)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In `## Step 8 — Summary report`, add a **report-only** clause: for files that have **no** `## Deferred observations` section but contain any pre-standardization marker phrase — `latent`, `forward risk`, `no action needed`, `out of scope for this milestone`, `flagging so Phase`, `Surface this to the orchestrator` — quote the matching paragraph(s) under a "possible unharvested margins" heading. State clearly this is report-only: free-form prose has no entry line to pin and **never gates**. Do not let this scan affect the gate in Task 2.

## Constraints (apply to all tasks)
- The sweep (Step 5), spec deletion, ROADMAP/ARCHITECTURE edits, and commit policy are untouched — this milestone adds only a read-only scan, an abort path, and a report clause.
- Do not rewrite, delete, or mark any entry text, `Affects:` value, or existing marker anywhere — pinning is `milestone-rescue-audit`'s job.
- Grammar and the pinned definition live in `orchestrator-artifacts` — reference, never redefine.
- Instructions only in the skill body; no rationale prose.
