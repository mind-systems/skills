# Plan: 6.2 — roadmap-prune: warn-only plan-layer citation scan at the number-reuse moment

## Context
Add a report-only grep scan to `roadmap-prune` that surfaces durable code/test comments citing the fluid plan layer (phase/note numbers, `.ai-factory/specs|notes` paths, `ROADMAP`/`Plan N`) at the moment prune frees a number — echoed in the Step 8 summary, never gating, editing, or blocking.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Add the report-only citation scan

- [x] **Task 1: Add the plan-layer citation scan sub-step**
  Files: `src/skills/roadmap-prune/SKILL.md`
  Add a new **report-only** sub-step that mirrors the existing Step 0.6 margin-capture → Step 8 echo pattern (a capture-now, echo-in-Step-8 structure). The sub-step must:
  - Anchor at the **target repo root** — the parent of the `.ai-factory/` holding the target ROADMAP.md, the same anchor Step 5 derives (reference that existing derivation, do not re-invent the wording).
  - Scope: the repo tree under that root, **excluding `.ai-factory/` and `.git/`**.
  - Grep (read-only) for the citation patterns — this pattern set is the contract and must match task 6.1's rule: `Phase [0-9]`, `note [0-9]{2}`, `\.ai-factory/(specs|notes)`, `ROADMAP`, `Plan [0-9]`. Include the illustrative invocation from the spec as guidance, stating explicitly it is guidance not contract (flags may be adjusted per platform as long as it stays read-only, repo-root-anchored, with the two excludes):
    ```bash
    grep -rInE "Phase [0-9]|note [0-9]{2}|\.ai-factory/(specs|notes)|ROADMAP|Plan [0-9]" \
      <target repo root> --exclude-dir=.ai-factory --exclude-dir=.git
    ```
  - Capture each hit for the Step 8 echo (Task 2).
  - State plainly, in the instructions-only voice the skill body mandates (no rationale prose — the *why* stays in the spec): warn-only, never gates, never edits, never blocks, never touches the roadmap/specs/`## Features`; false positives acceptable; distinct from the Step 0 deferred-observations gate.
  - **Removable-later marker:** add a note mirroring 4.2a's *Legacy-removable:* wording — once every consuming repo reads clean this scan can be deleted, or kept as a cheap standing regression net; the decision is deliberately deferred. Use the literal token `removable` so the spec's `grep -n "removable"` verification passes.
  - Placement: because the scan reads only code outside `.ai-factory/` (never deleted by the sweep), its timing is not sweep-critical; place it as its own report-only sub-step feeding Step 8, and make clear it is NOT part of the Step 0 gate and never affects whether the prune proceeds. Do not alter the Step 0 gate's block/refuse behavior or any other step — this change is strictly additive.

- [x] **Task 2: Echo captured hits in the Step 8 summary** (depends on Task 1)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In Step 8, add a report-only echo under a `possible plan-layer citations` heading, one `<file>:<line> — <matched text>` line per captured hit — modeled on the adjacent "possible unharvested margins" report-only block. If zero hits, omit the heading (mirroring the existing "if Step 0 captured nothing, omit the heading" rule). This echo never gates and never affects the Step 0 gate. Leave every other line of Step 8 byte-identical.

## Verification
- Every other step (Step 0 gate, sweep, `## Features` write, commit policy) reads byte-identical — the change is purely additive.
- `grep -n "removable" src/skills/roadmap-prune/SKILL.md` finds the removable-later marker.
- The Step 8 summary gains a `possible plan-layer citations` heading emitted only when hits exist.
