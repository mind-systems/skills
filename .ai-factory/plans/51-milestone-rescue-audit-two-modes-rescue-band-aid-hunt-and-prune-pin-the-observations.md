# Plan: milestone-rescue-audit: two modes — `rescue` (band-aid hunt) and `prune` (pin the observations)

## Context
Give `milestone-rescue-audit` a run-mode argument (`rescue|prune`, default `rescue`), wire it to the `orchestrator-artifacts` engine, teach rescue mode to read `## Deferred observations` as corroborating evidence (never findings), and add a prune mode that pins every unpinned deferred observation across both review dirs. All edits land in the single file `src/skills/milestone-rescue-audit/SKILL.md`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Frontmatter and Inputs

- [x] **Task 1: Frontmatter — mode arg, engine edge, write grant**
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  In the YAML frontmatter: change `argument-hint` to `"[rescue|prune]"`; add a `loads: orchestrator-artifacts` line (match the exact placement/format used in `src/skills/milestone-rescue/SKILL.md:14` and `src/skills/roadmap-prune/SKILL.md:11`); add `Edit` to `allowed-tools`. The current line 13 is `Read Glob Grep Bash(git *)`; the only correct target string is `Read Edit Glob Grep Bash(git *)`. Do **not** add `Write` — spec 04 Edit 4 scopes writes to append-only suffixes and promotion appends into existing files, both expressible via `Edit`.

- [x] **Task 2: Mode dispatch + rewritten Inputs block** (depends on Task 1)
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  Introduce the run-mode argument near the top (after the intro / before `## Inputs`): `$1` ∈ `rescue | prune`; absent → `rescue` (historic behavior). State that `rescue` runs on one failed task's warm-or-cold artifacts (band-aid hunt); `prune` runs when `roadmap-prune`'s gate refused, to pin unmarked deferred observations. Rewrite `## Inputs` so each mode's inputs are stated **directly**: rescue → one task's artifacts (warm from `milestone-rescue`, or located cold before Step 1); prune → the target repo's `.ai-factory/plan-reviews/` and `.ai-factory/reviews/` in full. **Delete** the sentence "for the artifact layout and directory structure see `milestone-rescue`" and instead point to the loaded `orchestrator-artifacts` engine for layout/naming/rounds/signals. Ensure the engine is loaded once per chat.
  **Cold-rescue target identification** (addresses review issue 1 — `$1` is now the mode, so the slug no longer arrives as the first argument): in the Inputs rewrite, state that cold rescue takes an **optional trailing slug** (`$2`) naming the task; when absent, it identifies the target from the user's prose plus a `Glob` over `plan-reviews/`/`reviews/` for the matching `<seq>-<slug>-*` artifacts. This keeps `$1` as the mode (no spec-Edit-1 contradiction) while preserving the "or cold on any looped/outlier task" affordance the description advertises. Do not touch the `description` field's "or cold" wording — pruning that affordance is a spec-tier decision, not this milestone's (see the review's deferred observation).

### Phase 2: Rescue mode — deferred observations as evidence

- [x] **Task 3: Step 1 captures deferred observations separately** (depends on Task 2)
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  In `## Step 1 — Reconstruct the finding→fix chain`, add that entries under `## Deferred observations` are **excluded** from the finding→fix chain, the round count of findings, and the severity trend. Capture them separately as working material: round, `Affects:` target, one-line gist. Entries already carrying an `audit-*` marker (per the engine's grammar) are skipped as already-evaluated — their existing verdict may still be cited. Reference the engine for the section format and marker grammar; do not redefine either.

- [x] **Task 4: Verdict corroboration + marking** (depends on Task 3)
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  In the verdict path (Step 3 root-cause test and/or Step 6 narrative — place where the band-aid case is argued): when a captured observation describes the same gap the finding→fix chain circles around, the narrative names it — quoting the observation and its round — as corroboration on the band-aid side (gap visible early, routed around). State explicitly it is **corroborative only**, never replacing the one-sentence root-cause test; absence of a match carries no weight either way. Add the marking rule: observations the audit **actually evaluated** against the chain/code get `[audit-corroborated]` or `[audit-dismissed]` appended (per the engine's append-only grammar); merely-captured ones stay unmarked. Note this is an `Edit` write on the review file's entry line.

### Phase 3: Prune mode and contracts

- [x] **Task 5: Prune mode section — pin everything** (depends on Task 2)
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  Add a prune-mode section (a clearly mode-gated block; keep the existing Steps 1–6 as the rescue pipeline). For every unpinned entry across both review dirs (dedup by `Affects:` target + gist per the engine's rule): (1) **evaluate** the observation against current code and roadmap — still holds, or resolved/obsoleted by later work; (2) **pin** per the engine's markers — stale/wrong/already-resolved → `[audit-dismissed]`; real and `Affects:` resolves to an existing file under the target repo root → append the entry verbatim (+ source `<seq>-<slug>` slug) under a `## Deferred observations` heading in that file (create the heading at end if absent), then mark `[promoted → <path>]`; real but unroutable (phase name, `unknown`, unresolvable path) → report verbatim in the mode's output and mark `[unrouted-reported]`. Mark **every** sibling occurrence across the milestone's review files. Exit criterion: zero unpinned entries; end with a summary — counts per marker + the unrouted list for the user to route by hand. No route-guessing (no phase-name resolution, no fuzzy matching); only an existing-file `Affects:` path promotes.

- [x] **Task 6: Write contract + What NOT to do** (depends on Tasks 4, 5)
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  Update the chat-only contract to carve out exactly the permitted writes: (a) append-only status suffixes on deferred-observation entry lines in review files, and (b) prune-mode promotion appends under a `## Deferred observations` heading in `Affects:`-target files — never content edits, never any other file. In `## What NOT to do`, add: do not count deferred observations as findings (round counts, severity trends, whack-a-mole discriminator); do not let a matching observation replace the one-sentence test in rescue mode; do not guess routes in prune mode; do not redefine the marker grammar, rewrite entry text/`Affects:` values/existing markers, or mark observations not actually evaluated; do not sweep, delete, or touch the roadmap in either mode. Confirm the rescue pipeline, one-sentence test, discriminators, and "default is NOT band-aid" wording remain unchanged.

## Commit Plan
- **Commit 1** (after tasks 1-6): "Add rescue and prune modes to milestone-rescue-audit"
