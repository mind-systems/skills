# orchestrator-artifacts: engine — the orchestrator's file protocol in one durable home

**Date:** 2026-07-04
**Source:** conversation context (deferred-observations channel design; audit two-mode redesign)

## Key Findings

- Three skills read the orchestrator's on-disk artifacts and each holds (or points at) its own description of the layout: `milestone-rescue` describes dirs/naming/rounds inline in its procedure; `milestone-rescue-audit`'s Inputs block says "for the artifact layout see `milestone-rescue`" — a cold audit run loads a ~440-line repair philosophy to extract ~15 lines of layout, the worst possible perception-tree edge; and the pending prune-gate task needs the `## Deferred observations` section format. Shared content with ≥2 callers → engine.
- A second, more urgent homelessness: the **status-marker grammar** currently lives in spec `03-prune-harvest-deferred-observations.md` — and specs die at prune by our own design. Without a durable home it would land in prune's skill body with audit referencing prune: the same skill-as-documentation smell. The engine is that home.
- What does **not** move: `milestone-rescue`'s sidecar `step`-states table — one consumer (only rescue writes `step`), stays in rescue.

## Details

### Edit 1 — new engine skill `src/skills/orchestrator-artifacts/SKILL.md`

Frontmatter: `name: orchestrator-artifacts`, `user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`. Body opens with the load-once statement and the standard reverse-graph marker (declarative, per the engine convention in CLAUDE.md). Content — pure protocol description, no procedure:

1. **Layout.** Artifacts live under the target repo's `.ai-factory/`: `plans/` (`<seq>-<slug>.md` plan + `<seq>-<slug>.json` sidecar), `plan-reviews/` (`<seq>-<slug>-plan-review-N.md`), `reviews/` (`<seq>-<slug>-review-N.md`), `patches/` (test mode bridges reviewer output here; empty in implement mode). Test mode adds `test-runs/` (`<seq>-<slug>-test-N.txt`) and roots at `ROADMAP_TESTS.md`. `<seq>` is assigned by the orchestrator at plan time and is not recoverable from a roadmap line; `N` is the round number — files in round order are the finding→fix history.
2. **Signals.** A review passes when its file ends with `PLAN_REVIEW_PASS` / `REVIEW_PASS` (`TEST_PASS` for test runs) on its own last line; no signal on the last round = the stage did not pass.
3. **Sidecar fields.** `planner`, `implementer` (resumable session ids), `step` (resume point — the closed set and its artifact requirements live in `milestone-rescue`, the only writer), `elapsed` (seconds, cumulative).
4. **Committed ⇔ completed.** The orchestrator commits a milestone's artifacts together with the milestone; tracked artifacts belong to completed tasks, uncommitted ones to failed/in-flight work.
5. **`## Deferred observations` section** (in both review genres): entry `- Affects: <phase / spec-note path / "unknown"> — <observation>`; section may be absent; entries are non-findings (a review with only them still passes); the reviewer never writes or imitates status markers — the field after the observation text is reserved for downstream tools (orchestrator spec `03-deferred-observations-section.md`).
6. **Status-marker grammar** (moved here from skills spec 03, verbatim in substance): append-only space-separated bracketed suffix at the end of the entry line; markers `[promoted → <path>]`, `[unrouted-reported]`, `[audit-corroborated]`, `[audit-dismissed]`; entry text and `Affects:` never rewritten, markers only accumulate; **pinned** = ≥1 marker; dedup rule — whoever pins an entry pins every occurrence across that milestone's review files (dedup by `Affects:` target + gist); all four markers are written by `milestone-rescue-audit` only.
7. **Mirrors-the-orchestrator invariant** (declared coupling): this file mirrors the orchestrator's file protocol (`orchestrator/main.py`, `agents.py`, `prompts/reviewer.md`) — if the protocol changes there, update this file; do not let them diverge.

### Edit 2 — rewire `milestone-rescue`

Add `loads: orchestrator-artifacts` to frontmatter (ensure loaded once per chat, same idiom as the roadmap family). Slim Step 1/Step 2: keep the **procedure** verbatim (git-status discovery of uncommitted files, slug identification, read-all-rounds discipline, governing-spec read) but drop prose that re-describes dirs/naming/rounds/signals now covered by the engine — reference it instead. The sidecar `step` table, all rollback procedures, and the Diagnosis Report register stay byte-identical. Behavior-identical overall.

### Edit 3 — activation and registration

Create the `active/skills/orchestrator-artifacts` symlink → `src/skills/orchestrator-artifacts`; add the skill to the active-set list in `CLAUDE.md`. The engine gets its reverse-graph marker from day one (it is born with three `loads:` edges).

### Constraints

- No procedure in the engine — it describes files, names, and semantics; discovery/repair/audit choreography stays with the callers.
- The callers' `loads:` edges for `milestone-rescue-audit` and `roadmap-prune` are added by their own tasks (specs 04 and 03) — this task wires only `milestone-rescue`.
- ≤ ~60 lines body; every line loads for three callers, keep it lean.

## What NOT to do

- Do not move the sidecar `step`-states table into the engine — single consumer, stays in `milestone-rescue`.
- Do not put gate, harvest, or audit behavior here — the engine holds no policy.
- Do not paraphrase the marker grammar differently from spec 03's wording when moving it — substance verbatim; spec 03 then references this engine as the grammar's home.
- Do not add a caller list — the reverse-graph marker with the inline grep is the whole reverse edge.
