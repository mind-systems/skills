# Plan: orchestrator-artifacts: engine — the orchestrator's file protocol in one durable home

## Context
Extract the orchestrator's on-disk artifact protocol (layout, PASS signals, sidecar fields, `## Deferred observations` format, status-marker grammar) into a single durable `orchestrator-artifacts` engine skill, then rewire `milestone-rescue` to load it instead of re-describing the layout inline.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Create the engine

- [x] **Task 1: Create the `orchestrator-artifacts` engine skill**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  New skill, body ≤ ~60 lines, protocol description only — **no procedure, no policy** (discovery/repair/audit choreography stays with callers). Follow spec `.ai-factory/specs/05-orchestrator-artifacts-engine.md` Edit 1 exactly.
  Frontmatter: `name: orchestrator-artifacts`, `description` (what it is + when loaded), `user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`.
  Body opens with the load-once statement + the standard **reverse-graph marker** — one declarative sentence in the same idiom as `src/skills/note/SKILL.md` (lines 21–23) and the other engines, with the inline grep `` grep -l "orchestrator-artifacts" src/skills/*/SKILL.md src/commands/*.md `` (never a caller list). Then the seven content items:
  1. **Layout** — artifacts under the target repo's `.ai-factory/`: `plans/` (`<seq>-<slug>.md` plan + `<seq>-<slug>.json` sidecar), `plan-reviews/` (`<seq>-<slug>-plan-review-N.md`), `reviews/` (`<seq>-<slug>-review-N.md`), `patches/` (test mode bridges reviewer output here; empty in implement mode). Test mode adds `test-runs/` (`<seq>-<slug>-test-N.txt`) and roots at `ROADMAP_TESTS.md`. `<seq>` assigned by the orchestrator at plan time, not recoverable from a roadmap line; `N` = round number; files in round order are the finding→fix history.
  2. **Signals** — a review passes when its file ends with `PLAN_REVIEW_PASS` / `REVIEW_PASS` (`TEST_PASS` for test runs) on its own last line; no signal on the last round = the stage did not pass.
  3. **Sidecar fields** — `planner`, `implementer` (resumable session ids), `step` (resume point — note the closed set + artifact requirements live in `milestone-rescue`, its only writer), `elapsed` (seconds, cumulative).
  4. **Committed ⇔ completed** — the orchestrator commits a milestone's artifacts with the milestone; tracked artifacts belong to completed tasks, uncommitted to failed/in-flight work.
  5. **`## Deferred observations` section** (both review genres) — entry `- Affects: <phase / spec-note path / "unknown"> — <observation>`; section may be absent; entries are non-findings (a review with only them still passes); the reviewer never writes/imitates status markers — the field after the observation text is reserved for downstream tools.
  6. **Status-marker grammar** (moved from spec `03`, **substance verbatim** — do not paraphrase differently from spec 03's wording): append-only space-separated bracketed suffix at the end of the entry line; markers `[promoted → <path>]`, `[unrouted-reported]`, `[audit-corroborated]`, `[audit-dismissed]`; entry text and `Affects:` never rewritten, markers only accumulate; **pinned** = ≥1 marker; dedup rule — whoever pins an entry pins every occurrence across that milestone's review files (dedup by `Affects:` target + gist); all four markers written by `milestone-rescue-audit` only.
  7. **Mirrors-the-orchestrator invariant** (declared coupling) — this file mirrors the orchestrator's file protocol (`orchestrator/main.py`, `agents.py`, `prompts/reviewer.md`); if the protocol changes there, update this file, do not let them diverge.

### Phase 2: Rewire the first caller

- [x] **Task 2: Rewire `milestone-rescue` onto the engine** (depends on Task 1)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Per spec Edit 2. Add `loads: orchestrator-artifacts` to frontmatter (ensure loaded once per chat, same idiom as the roadmap family). Slim Step 1 / Step 2: **keep the procedure verbatim** — git-status discovery of uncommitted files, slug identification, read-all-rounds discipline, governing-spec read — but drop prose that re-describes dirs/naming/rounds/signals now covered by the engine, referencing the engine instead.
  **Byte-identical, do not touch:** the sidecar `step`-states table (`### Valid sidecar step states`, single consumer — stays), all Step 5 rollback procedures, and the Step 3 Diagnosis Report register. Overall behavior-identical.

### Phase 3: Activate and register

- [x] **Task 3: Symlink into the active set and register in CLAUDE.md** (depends on Task 1)
  Files: `active/skills/orchestrator-artifacts` (symlink), `CLAUDE.md`
  Per spec Edit 3. Create the symlink: `ln -sfn ../../src/skills/orchestrator-artifacts active/skills/orchestrator-artifacts` (match the relative-target form of the sibling symlinks under `active/skills/`; verify with `ls -l`).
  In `CLAUDE.md`, add `orchestrator-artifacts` to **The active set** paragraph (line 62) — the "our skills" list before the "plus one upstream original" clause.
