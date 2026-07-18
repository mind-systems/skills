# Code Review: 14.1 — Compress the mini-manual descriptions to the routing contract

**Files Reviewed:** `git diff HEAD` in full — 11 changed description blocks (`src/skills/*`, `src/agents/editor.md`), spec 74, the plan, plus each edited skill's body read in full to check the description against what the skill actually does. Independent recount of all 12 baseline rows and an independent sweep of the loaded field (`active/skills/`, `active/commands/`, `active/agents/`).
**Risk Level:** 🟡 Medium — two compressions changed what the always-loaded layer *claims*, one of them into a statement the body explicitly contradicts.

## Scope note

`git diff HEAD` also carries unrelated pre-existing working-tree changes: `.ai-factory/specs/24-…` and `39-…` (path corrections `~/projects/skills` → `~/projects/sakshi/skills`, and the Phase-13 present-tense doctrine rewording). Neither belongs to 14.1; both are outside this review. Spec 74's disposition-list addition is the spec-tier reconciliation the plan's guards anticipate, and is consistent with the plan.

## Verified against ground truth

Mechanically checked, not eyeballed:

- **All 12 post-edit character counts in the plan's table are exact**, and the total is exactly 4578 against a 5781 baseline — a 20.8% drop in the always-loaded layer. I recomputed every row with the same whitespace-normalized method; no row is off by even one character.
- **Every guarded byte-identical string survives**: `task-rescue`'s two PASS literals and three trigger phrases, `task-rescue-audit`'s five trigger phrases, `roadmap-test-coverage`'s unhyphenated opening sentence and its `Use when…`, `roadmap-decompose-skeleton`'s `Use when…`/`Trigger:` line, `orchestrator-artifacts`' `Pure protocol reference, no procedure.` and `Use when reading or writing…`, `test-philosophy`'s opening and full silent/loud rule sentence, `temporal-tree`'s `Invoke after detangle…`, `agent-architect`'s `Use when…`. 13/13 pass.
- **Frontmatter beyond `description:` is untouched everywhere.** The diff contains no change to `name:`, `loads:`, `allowed-tools`, `argument-hint`, `tools:`, `model:`, `effort:`, `user-invocable`, `disable-model-invocation`.
- **The closure claim now holds.** Sweeping every description in the loaded field for sibling-skill mentions returns exactly six residuals, and all six are on the disposition list: `editor`→`agent-architect` (keep), `aif-architecture`→`aif`, `task-rescue-audit`→`task-rescue`, `temporal-tree`→`detangle` (three when-anchor keeps), `command-handoff`/`command-pin-gaps`→`note` (non-matches). No unaccounted wiring clause remains — the defect that looped the plan through three review rounds is genuinely closed.
- **Both reverse-graph markers survive**, so the two caller-list cuts moved a fact rather than destroyed it (`orchestrator-artifacts`, `test-philosophy` bodies both retain their `grep -l …` marker).
- **`test-philosophy`'s capitalization repair is punctuation-only** (`; holds` → `Holds`), as authorized — no word changed.
- **`command-pin-gaps` is correctly untouched**, matching its recorded no-change verdict.

## Findings

### 1. `roadmap-decompose-skeleton` — the compression narrowed the skill's stated applicability, and now contradicts its own `Use when` (`src/skills/roadmap-decompose-skeleton/SKILL.md:6-8`)

The rewrite moved a qualifier's scope. Before, the async-I/O condition attached to the **last** extraction kind only:

> Extracts interface/abstract skeleton tasks, tests-first tasks …, and no-prod-code contract-tasks **for heavy tasks mixing async I/O + stateful buffer + lifecycle**.

After, the same trailing phrase governs **all three**:

> Extracts skeleton, tests-first, and no-prod-code contract tasks — tests-first filtered by the silent-failure rule — **for heavy tasks mixing async I/O + stateful buffer + lifecycle**.

The description now says this skill extracts skeleton and tests-first tasks *for async-I/O-plus-buffer-plus-lifecycle work* — which is false. The body scopes the skill to "heavy or hazardous tasks and shared type surfaces only" (`SKILL.md:23-24`), and the async/buffer/lifecycle triple is the **concurrency lens's** trigger, not a precondition on the skeleton or TDD lenses. The very next sentence — kept byte-identical, correctly — contradicts the new claim: `Use when a task is heavy/hazardous **or shares a type surface**…`.

Runtime effect: a reader routing on the what-clause skips this skill for a shared type surface with no concurrency, which is one of its two headline cases. This is the "compression, not amputation" guard failing — and it is a *new* false statement in the always-loaded layer, i.e. exactly the drift the task exists to remove.

Fix is small and stays inside the plan's Task 4 intent: re-attach the qualifier to the contract-task kind, e.g. `Extracts skeleton, tests-first (filtered by the silent-failure rule), and no-prod-code contract tasks for surfaces mixing async I/O + stateful buffer + lifecycle.` No trigger phrase moves; the character count stays in the same range.

### 2. `roadmap-test-coverage` — "drafting a test plan" asserts work the body explicitly forbids this skill from doing (`src/skills/roadmap-test-coverage/SKILL.md:4-6`)

Cutting `then hands off to /roadmap-decompose` was right — it is topology. But the replacement clause claims the drafting for this skill:

> Filters areas by silent-failure risk **before researching and drafting a test plan**.

The body says the opposite in two places: Layer 8 is titled **Hand Off** and prints `Next step: /roadmap-decompose` with a paste-ready handoff list (`SKILL.md:320-343`), and the hard rules state **"Never write ROADMAP_TESTS.md — that is `/roadmap-decompose`'s job"** (`SKILL.md:372`). The skill researches, classifies, and writes task specs; it does not draft the plan.

So where the old description was verbose-but-true, the new one is concise-and-false. The pre-existing `Use when you want a complete test plan…` is fine — it describes the user's goal, not the skill's action — but the what-clause should stop at what the skill produces. Suggested: `Filters areas by silent-failure risk, then researches each and writes up the findings.` (or similar) — no claim of drafting, same length class.

## Nit (non-blocking)

- `roadmap-engine` now reads `…contract line plus a full task spec — plus the shared create/update/check…` — two `plus`es in close succession where `written via note` used to separate them. Meaning is intact and the cut was correct; only the cadence suffered.

## Assessment

The mechanical discipline here is genuinely strong: exact counts, every guarded literal preserved, frontmatter clean, and the field sweep now closed — the wiring goal of the task is achieved. Both findings are the same class of defect, and it is the one this task was most at risk of: in compressing a true-but-verbose sentence, the rewrite produced a shorter sentence that says something the body does not support. Neither is caught by any of the plan's checks, because every check is about *what was removed* (topology, triggers, size) and neither is about *whether what remains is still true*. Worth adding that as a verification line for the rest of Phase 14: after each cut, re-read the surviving description against the body it summarizes.

Both fixes are single-sentence edits inside the already-opened `description:` blocks.
