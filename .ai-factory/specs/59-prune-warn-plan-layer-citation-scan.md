# roadmap-prune: warn-only plan-layer citation scan at the number-reuse moment

Origin: [handoff 15](../handoffs/15-code-cites-fluid-plan-layer-false-resolution.md) § 5 candidate 4, promoted. Enforces the rule task 6.1 states in `src/global/CLAUDE.md`. Runs after 5.4 — 5.2/5.3/5.4 already edit `roadmap-prune/SKILL.md`; serial to avoid same-file churn.

## Current state

`roadmap-prune` frees phase/note numbers every run — Step 6 deletes the pruned `[x]` lines and the freed number (globally-sequential, holes legal) is later refilled by an unrelated direction. Nothing signals that a durable code comment cited the number prune just freed, so the false-resolution corruption (a `// Phase 8.1.2` comment now pointing at a live, unrelated `Phase 8`) is armed silently at exactly this moment. Prune has two reads of the repo already — the Step 0 deferred-observations **gate** (blocks) and the 4.2a legacy self-heal (`## Features` marker) — but neither looks at code.

## Change

Add a **report-only** scan to `src/skills/roadmap-prune/SKILL.md`, echoed in Step 8's summary. It never gates, never edits, never blocks — distinct from the Step 0 gate.

- **Where anchored:** the target repo root — the parent of the `.ai-factory/` holding the target ROADMAP.md, the same anchor Step 5 derives.
- **Scope:** the repo tree under that root, **excluding** `.ai-factory/` (the plan layer citing itself is legal) and `.git/`.
- **Patterns** (the citation shapes, matching task 6.1's rule and the orchestrator implementer prohibition): `Phase [0-9]`, `note [0-9][0-9]`, `\.ai-factory/(specs|notes)`, `ROADMAP`, `Plan [0-9]`. One grep, e.g.:

  ```bash
  grep -rInE "Phase [0-9]|note [0-9]{2}|\.ai-factory/(specs|notes)|ROADMAP|Plan [0-9]" \
    <target repo root> --exclude-dir=.ai-factory --exclude-dir=.git
  ```

- **Output:** under a `possible plan-layer citations` heading in the Step 8 report, one `<file>:<line> — <matched text>` per hit. If zero hits, omit the heading (mirrors Step 8's existing "possible unharvested margins" report-only heading).
- **Placement in the skill:** its own report-only sub-step feeding Step 8, alongside the Step 0.6 margin-capture → Step 8 echo pattern already in the file. It is not part of the Step 0 gate and never affects whether the prune proceeds.

Carry a **removable-later** marker mirroring 4.2a's *Legacy-removable* note: once every consuming repo reads clean, this scan can be deleted — or kept as a cheap standing regression net; the decision is deliberately deferred, and the marker records that.

## Files & types

- edit `src/skills/roadmap-prune/SKILL.md` only — a new report-only scan sub-step + its Step 8 echo + the removable-later marker.

## Guards

- **Warn-only, never gates.** Unlike Step 0's deferred-observations gate, this scan never stops the prune, never blocks, never demands resolution — it prints and proceeds. It never edits code and never touches the roadmap, specs, or `## Features`.
- **False positives are acceptable.** The scan is a heads-up at the arming moment, not a proof; the reader judges each hit. The `.ai-factory/`-exclude keeps the plan layer's own legitimate `Phase N` text out of the report; residual noise (e.g. a repo whose docs legitimately discuss phases) is tolerated, not engineered away.
- **`grep` shape is guidance, not contract.** The pattern set is the contract (it must match task 6.1's rule); the exact `grep` invocation is illustrative — an implementer may adjust flags for the platform as long as it stays read-only and repo-root-anchored with the two excludes.
- **Instructions-only.** Follow the skill's "no rationale prose in the body" mandate — the scan is described as steps, the *why* stays here in the spec.
- Every other step (gate, sweep, `## Features` write, commit policy) byte-identical; this is additive.

## Verification

- Dry-run the prune on this repo (no commit): the summary prints a `possible plan-layer citations` section listing real `file:line` hits from `src/` skill bodies, and the prune otherwise completes unchanged.
- Confirm the scan never blocks: on a repo with many hits, the prune still proceeds to Step 8.
- `grep -n "removable" src/skills/roadmap-prune/SKILL.md` → the removable-later marker present.
- The Step 0 gate's block/refuse behavior reads identically to before.
