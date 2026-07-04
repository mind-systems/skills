# milestone-rescue-audit: two modes — rescue (band-aid hunt) and prune (pin the deferred observations)

**Date:** 2026-07-04
**Source:** conversation context (deferred-observations channel design; artifact layout and marker grammar live in the `orchestrator-artifacts` engine — spec `05-orchestrator-artifacts-engine.md`; depends on that task landing first)

## Key Findings

- The skill gains an explicit **run mode argument**: `rescue` | `prune` (`argument-hint`), so the agent never guesses the angle — the user states it. `rescue` (default when the argument is absent — the historic behavior) runs after `milestone-rescue` on a failed task's warm artifacts, hunting band-aid convergence. `prune` runs when `roadmap-prune`'s gate refused to sweep: its job is to **pin every unmarked deferred observation** so prune can run.
- The two modes search connections at different angles. Rescue mode asks "did this milestone converge by understanding or attrition?" — one task, its chain of rounds. Prune mode asks, per observation, "what stands behind this — is it still real, and where does it land?" — the whole project's review dirs, entries as the unit, current code/roadmap as the reference.
- In both modes, `## Deferred observations` entries are **not findings** (a review with only them still passes — orchestrator contract): they never enter the finding→fix chain, round counts, or severity trends.

## Details

### Edit 1 — mode argument and the engine edge

`$1` ∈ `rescue` | `prune`; absent → `rescue`. Update `argument-hint` to `"[rescue|prune]"`. Add `loads: orchestrator-artifacts` to frontmatter (ensure loaded once per chat). Rewrite the Inputs block: each mode's inputs stated directly — rescue: one task's artifacts (warm from `milestone-rescue`, or located cold); prune: the target repo's `.ai-factory/plan-reviews/` and `.ai-factory/reviews/` in full — and the layout/naming/rounds/signals come from the engine: **delete the "for the artifact layout … see `milestone-rescue`" pointer** (a cold run must not load a 440-line repair philosophy as documentation).

### Edit 2 — rescue mode: deferred observations as evidence

1. **Step 1 (chain reconstruction):** entries under `## Deferred observations` are excluded from the finding→fix chain, the round count of findings, and the severity trend. Capture them separately (round, `Affects:` target, one-line gist). Entries already carrying an `audit-*` marker are skipped as evaluated (their existing verdict may still be cited).
2. **Verdict evidence:** when a captured observation describes the same gap the finding→fix chain circles around, the narrative names it — quoting the observation and its round — as corroboration on the band-aid side (the gap was visible early and routed around). Corroborative only; it never replaces the one-sentence root-cause test. Absence of a match carries no weight either way.
3. **Marking:** observations the audit actually **evaluated** against the chain/code get `[audit-corroborated]` or `[audit-dismissed]` appended per spec 03's grammar; merely-captured ones stay unmarked.

### Edit 3 — prune mode: pin everything

For every unpinned entry across both review dirs (dedup by `Affects:` target + gist across each milestone's review files, per spec 03's protocol):

1. **Evaluate** the observation against the current code and roadmap: does it still hold, or did later work resolve/obsolete it?
2. **Pin** with the grammar's markers:
   - stale/wrong/already-resolved → `[audit-dismissed]`;
   - real and `Affects:` resolves to an existing file under the target repo root → append the entry verbatim (+ source `<seq>-<slug>`) under a `## Deferred observations` heading in that file (create the heading at the end if absent), then mark `[promoted → <path>]`;
   - real but unroutable (phase name, `unknown`, unresolvable path) → report it to the user verbatim in the mode's output and mark `[unrouted-reported]`.
3. Mark **every** occurrence across the milestone's review files. The mode's exit criterion: zero unpinned entries remain; end with a summary — counts per marker and the unrouted list for the user to route by hand.

### Edit 4 — write contract

The chat-only contract gains exactly this carve-out, and `Edit` joins `allowed-tools`: the skill's only writes are (a) append-only status suffixes on deferred-observation entry lines in review files, and (b) prune-mode promotion appends under a `## Deferred observations` heading in `Affects:`-target files. Never content edits, never any other file. Review files are terminal artifacts — the append-only marker carries zero corruption risk; the alternative chain "audit advises, another skill applies" adds a forgettable step and is rejected.

### Constraints

- Rescue mode's analysis pipeline, one-sentence root-cause test, discriminators, "default is NOT band-aid", healthy-convergence early-exit — all unchanged.
- Marker grammar, pinned-definition, and dedup rule live in the `orchestrator-artifacts` engine — referenced, never redefined.
- Old reviews without the section: nothing to capture or pin, no fallback heuristics — the audit does not mine marker phrases (prune's report quotes them, report-only).

## What NOT to do

- Do not count deferred observations as findings anywhere — not in round counts, not in severity trends, not in the whack-a-mole discriminator.
- Do not make a matching observation decisive in rescue mode — it corroborates the one-sentence test, never replaces it.
- Do not guess routes in prune mode — no phase-name resolution, no fuzzy matching; only an `Affects:` path resolving to an existing file promotes; everything else is reported and marked `unrouted-reported`.
- Do not redefine the marker grammar; do not rewrite entry text, `Affects:` values, or existing markers; do not mark observations that were not actually evaluated (rescue mode).
- Do not sweep, delete, or touch the roadmap in either mode — prune's job stays prune's.
