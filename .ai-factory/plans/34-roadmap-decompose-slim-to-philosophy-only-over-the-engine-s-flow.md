# Plan: roadmap-decompose: slim to philosophy-only over the engine's flow

## Context
After note 43 moved the shared roadmap-maintenance flow into `roadmap-engine`, this milestone strips the duplicated flow machinery from `roadmap-decompose/SKILL.md`, leaving only decompose's philosophy and wiring it to the engine's flow via explicit hooks — behavior-identical for the user in every mode.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Rewrite decompose to philosophy-only

- [x] **Task 1: Replace the flow machinery with a load-once + hook wiring, keeping only philosophy**
  Files: `src/skills/roadmap-decompose/SKILL.md`
  Rewrite the body (frontmatter unchanged — `loads: roadmap-engine` already present; keep `allowed-tools` and `disable-model-invocation: true` as-is). Delete the duplicated flow text now owned by `roadmap-engine`: **Step 0** (Load Project Context), **Step 1** mode/mode-determination boilerplate that the engine covers, **Mode 1** (Create) gather-input/explore/confirm dialogs and its embedded Atomicity Gate at 1.3.1, **Mode 2** sub-actions that duplicate the engine (2.1 read-state, 2.2 menu, 2.3 review progress, 2.4 add + its duplicated 2.4.1 gate, 2.6 reprioritize, 2.7 save/summary), and all of **Mode 3** (Check). Replace with a short lead-in: "Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not already loaded) and run its **Roadmap maintenance flow** with the hooks below." Then supply exactly the four engine hooks as decompose's philosophy content:
    - **(a) Granularity** — each entry is one atomic task: one file boundary, one concern, one reason to revert; two-tier discipline (a contract line in the roadmap plus a full spec note per the engine's format — never a full spec inline). Order by logical sequence (dependencies first). Two parity carry-overs from today's Mode 1 that the engine's create flow does not itself hold, so hook (a) must supply them: (i) on first run, mark already-completed milestones as `[x]` (current line 97); (ii) supply the create-mode gather-input **question phrasing** that fills the engine's `AskUserQuestion: <caller phrases this…>` placeholder (engine line 109) — today's wording "What tasks should I decompose into the roadmap?" (current line 63) — so the placeholder is not left unfilled.
    - **(b) Per-entry gate** — state the **Atomicity Gate once**: after drafting each entry's full spec, before its contract line — *"Can the first half be deployed without the second half and still make sense?"* If yes → split into two entries, apply the gate to each half recursively until no half passes; if no → the entry is atomic. "Make sense" = compiles, breaks nothing, delivers independently observable value. Register this as the flow's per-entry gate hook (hook b).
    - **(c) Target-file routing** — resolve `$TARGET_FILE` before the flow runs: default `.ai-factory/ROADMAP.md`; an explicit filename argument (e.g. `ROADMAP_TESTS.md`) wins; test-context keywords (test, tests, spec, testing, тест, тесты) → `.ai-factory/ROADMAP_TESTS.md`.
    - **(d) Extra update action "Decompose existing"** — register the added update-menu action: expand a vague milestone into a full spec (what exists today, the exact change, files/types/methods to touch, guards, how to verify), with the note-handling rule — existing `Spec:` tag → update the named note in place with `Write`, tag unchanged; legacy inline (no tag) → write a new note per the engine's format and add the `Spec:` tag; offer a split when the milestone bundles 2+ independent concerns (a split → two notes + two contract lines); never bulk-migrate untouched legacy tasks.
  Do **not** restate the engine's flow, dialogs, format, or mechanism-tier critical rules "for convenience." Do not reintroduce anything notes 36 (stale `/aif-plan`, `/aif-implement`, `/decompose` refs) or 38 (inline roadmap-format block) removed. Preserve the load-once discipline sentence. Target ~60–100 lines total.

- [x] **Task 2: Reduce Critical Rules to the philosophy tier**
  Files: `src/skills/roadmap-decompose/SKILL.md`
  Keep only philosophy-tier critical rules, dropping the mechanism-tier ones the engine now owns (source-of-truth read-before-modify, never-remove-silently, `[x]`-stays-until-prune — these live in the engine's "Critical rules (mechanism)"). Retain: milestones are atomic and specific (one concern, one reason to revert); every task is two-tier (contract line + spec note per `roadmap-engine`'s format, never a full spec inline); NO implementation — this skill only plans, the orchestrator implements in a separate run (post-note-36 wording, no `/aif-implement` reference).

- [x] **Task 3: Verify hook coverage and no behavior drift** (depends on Task 1, Task 2)
  Files: `src/skills/roadmap-decompose/SKILL.md`
  Cross-check against `src/skills/roadmap-engine/SKILL.md` "Hook points (caller-supplied)" list: confirm each hook decompose needs (a/b/c/d) is explicitly supplied and named, and that the engine's flow with these hooks reproduces today's create/update/check interaction for the user in every mode. Explicitly confirm the two create-mode parity carry-overs survived: (i) already-completed milestones still marked `[x]` on first run, and (ii) the create-mode gather-input question placeholder is actually filled with decompose's wording — neither silently dropped. Grep the final file for leftovers: no residual Mode 1/2/3 machinery, no duplicated dialogs/format blocks, no stale `/aif-plan`·`/aif-implement`·`/decompose` references. Confirm the H1, intro sentence, and frontmatter still read correctly and line count sits ~60–100.
