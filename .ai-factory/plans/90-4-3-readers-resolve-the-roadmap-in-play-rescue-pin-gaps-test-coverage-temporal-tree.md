# Plan: 4.3 — readers resolve the roadmap in play: rescue, pin-gaps, test-coverage, temporal-tree

## Context
Widen the four reading/operating skills from bare-literal roadmap paths to the engine's named-roadmap resolution (argument → my → default), so a milestone from a named roadmap under `.ai-factory/roadmaps/` resolves correctly. Resolution is referenced, never restated — its one home is roadmap-engine's "Named roadmaps" section (spec 43).

### Dependency wiring (applies to every task — this is not a pure wording change)
Each reader newly *depends on* roadmap-engine's "Named roadmaps" content (slug derivation → local-part → lowercase → non-alnum runs to a single hyphen; the `> Owner:` verification and hard-stop on mismatch). A pointer alone dangles — the agent must be able to reach the content at runtime. The ratified pattern is the sibling 4.2 writers (`roadmap-decompose`, `roadmap-outline`), which each: (a) declare `loads: roadmap-engine` in frontmatter; (b) carry a body line "Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not already loaded)"; (c) reference "per `roadmap-engine`'s named-roadmap resolution order". Every reader task below does all three, not only (c).

Tool-access split, verified against each file's `allowed-tools`:
- **rescue** — has `Skill`; `loads: orchestrator-artifacts`. Append `roadmap-engine` to `loads:` and add the load-once line (it already carries the identical line for `orchestrator-artifacts`).
- **test-coverage** — has `Skill`; `loads: test-philosophy`. Append `roadmap-engine` to `loads:` and add the load-once line.
- **command-pin-gaps** — `allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git grep *)`, **no `Skill`**, no `loads:`. Add `Skill` to `allowed-tools` (the milestone-1.17 precedent: `Skill` joins `allowed-tools` wherever the body loads via the Skill tool), add `loads: roadmap-engine`, and the load-once line.
- **temporal-tree** — `allowed-tools: Read Bash(git *) Glob Grep`, **no `Skill`**, no `loads:`. Same treatment: add `Skill`, add `loads: roadmap-engine`, and the load-once line.

roadmap-engine already carries its reverse-graph marker (it is loaded by decompose/outline), so no engine-side edit is needed; the coupling is declared one-way on the caller side, as the skill-graph rule requires.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

Each task is an independent single-site edit — no cross-task dependencies. Per spec 45, every non-target-resolution procedure stays byte-identical, and behavior without a `roadmaps/` directory must be identical to today (the engine "never infers multiuser mode" — "my" activates only on explicit user request, so the default path stays `ROADMAP.md`).

### Phase 1: Widen the four readers to the engine's resolution

- [x] **Task 1: rescue — `$TARGET_FILE` resolution gains the named tier (+ reconcile the Step-1 restatement)**
  Files: `src/skills/milestone-rescue/SKILL.md`
  - **Frontmatter:** append `roadmap-engine` to the `loads:` field → `loads: orchestrator-artifacts roadmap-engine`. (`Skill` is already in `allowed-tools`.)
  - **Load-once line:** add a body sentence mirroring the existing `orchestrator-artifacts` load-once line (`:33-35`) — "Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not already loaded) — it defines the named-roadmap resolution referenced below." Place it alongside the existing load-once instruction.
  - **Step 4 resolution (`:177-180`):** replace the three-branch literal list (argument → test-keyword → default) with the engine's resolution order argument → my → default. Keep the explicit-argument branch first. The test-keyword branch (keywords: test, tests, spec) maps **the roadmap in play**, not a fixed literal: a named roadmap → its `.ai-factory/roadmaps/<slug>-tests.md` sibling, the default → `.ai-factory/ROADMAP_TESTS.md` as today. Reference `roadmap-engine`'s "Named roadmaps" resolution (slug/owner mechanics) rather than restating it.
  - **Step 1 reconciliation (`:56-58`):** the parenthetical "(the same resolution Step 4 uses: argument-named file if given, else `.ai-factory/ROADMAP_TESTS.md` for test slugs, else `.ai-factory/ROADMAP.md`)" restates the old three literal branches and would contradict the widened Step 4. Collapse it to a **pure pointer** — "(the same resolution Step 4 determines)" — so the resolution lives in exactly one place (Step 4, ultimately the engine). Leave the sentence at `:62-64` ("additive to Step 4's own `$TARGET_FILE` resolution") unchanged — it stays correct.
  - **Guards:** on a default-roadmap milestone with no `roadmaps/`, `$TARGET_FILE` resolves exactly as today. Depth menu, rollback variants, sidecar `step` table, and artifact discovery stay byte-identical.

- [x] **Task 2: pin-gaps — final fallback names the roadmap in play**
  Files: `src/commands/command-pin-gaps.md`
  - **Frontmatter:** add `Skill` to `allowed-tools`; add a `loads: roadmap-engine` line.
  - **Load-once line:** add a body sentence — "Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not already loaded) — it defines the named-roadmap resolution referenced below."
  - **Fallback edit (`:13`):** change the last fallback from "all open `- [ ]` tasks above `---STOP---` in `.ai-factory/ROADMAP.md`" to the open tasks of the roadmap in play per `roadmap-engine`'s resolution (argument → my → default), still scanning each contract line and its `Spec:` note above `---STOP---`. Reference the engine; do not restate slug/owner mechanics.
  - **Guards:** the `$ARGUMENTS`-first and chat-scope tiers, the value/meaning hole taxonomy, `## Blocking decisions`, and scan/default modes stay byte-identical.

- [x] **Task 3: test-coverage — Layer-1 input names the resolution**
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  - **Frontmatter:** append `roadmap-engine` to the `loads:` field → `loads: test-philosophy roadmap-engine`. (`Skill` is already in `allowed-tools`.)
  - **Load-once line:** add the "Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not already loaded)" body sentence.
  - **Layer-1 edit (`:29`):** replace "`ROADMAP.md` (or `$ARGUMENTS` if provided)" with the engine's resolution order (argument → my → default) for the roadmap in play, feeding `$ROADMAP_PATH`. Reference `roadmap-engine`'s "Named roadmaps" section for the mechanics.
  - **Guards:** the 8 layers, the Class A/B table, and every other procedure stay byte-identical.

- [x] **Task 4: temporal-tree — literal path mentions widened to the roadmap in play**
  Files: `src/skills/temporal-tree/SKILL.md`
  - **Frontmatter:** add `Skill` to `allowed-tools`; add a `loads: roadmap-engine` line.
  - **Load-once line:** add the "Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not already loaded)" body sentence.
  - **Path edits:** replace the literal `.ai-factory/ROADMAP.md` mentions (`:67` and `:70`; grep at execution time since the file is in flux) with "the roadmap in play" resolved per `roadmap-engine`'s resolution (argument → my → default). The Step-3 reconstruction command `git show <first-hash>:.ai-factory/ROADMAP.md` takes the resolved roadmap path; the roadmap-snapshot narrative follows suit.
  - **Semantic caveat (resolves the review's Issue 3):** temporal-tree reconstructs the **integration-branch, repo-wide** pruned history — its entry point is the `## Features` table that `roadmap-prune` builds on the integration branch (per milestone 4.4 / spec 46 and `docs/multiuser-roadmaps.md`). Spec 45 dictates the argument → my → default tier here, and it is honored; but "my" is only ever activated on explicit user request (the engine never infers), so the default path stays `ROADMAP.md` — identical to today. Add one sentence documenting this: when a named roadmap is explicitly requested, `git show <hash>:<resolved path>` reconstructs whatever roadmap path the user named at that historic hash — a named roadmap may not exist at an old hash, which is the user's explicit choice, not a silent default. This closes the deferred question in-plan (spec-faithful) rather than reopening spec 45.
  - **Guards:** the walk order (Steps 1–6), the `## Features` prefix-match rule, ARCHITECTURE.md handling, synthesis output, and "What NOT to do" stay byte-identical.
