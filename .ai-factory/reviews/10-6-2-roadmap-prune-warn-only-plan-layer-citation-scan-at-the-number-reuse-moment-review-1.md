# Code review — 6.2 roadmap-prune warn-only plan-layer citation scan

Scope of change (per `git diff HEAD` / `git status`): a single code artifact, `src/skills/roadmap-prune/SKILL.md`. The other staged files are planning artifacts (plan `.md`/`.json`, plan-review) and were not treated as code. The diff is purely additive — two insertions, no deletions or edits to existing lines.

## What the change does
- Adds `## Step 7.5 — Plan-layer citation scan (report-only)` between Step 7 and Step 8.
- Adds a second report-only echo block in Step 8 for the captured hits.

## Verification against the spec (`.ai-factory/specs/59-prune-warn-plan-layer-citation-scan.md`)
- **Report-only / never gates** — stated in the Step 7.5 header and both echo blocks; the outcome explicitly never affects whether the prune proceeds. ✓
- **Anchor** — target repo root, "the same anchor Step 5 derives", not re-invented. ✓ (matches Step 5 line 273.)
- **Scope / excludes** — repo tree under root, excluding `.ai-factory/` and `.git/`. ✓
- **Pattern set (the contract)** — `Phase [0-9]`, `note [0-9]{2}`, `\.ai-factory/(specs|notes)`, `ROADMAP`, `Plan [0-9]` — matches the spec's contract exactly (`{2}` is ERE-equivalent to the roadmap line's `[0-9][0-9]`). ✓
- **Guidance-not-contract** — the `grep` invocation is explicitly labeled illustrative; flags adjustable as long as read-only, root-anchored, two excludes. ✓
- **Capture format** — `<file>:<line> — <matched text>`, consistent between Step 7.5 and the Step 8 echo. ✓
- **Removable-later marker** — present, mirrors 4.2a's `*Legacy-removable:*` wording; `grep -n "removable"` matches line 386 (spec verification satisfied). ✓
- **Step 8 omit-when-empty** — "If Step 7.5 captured nothing, omit the heading", mirroring the existing "possible unharvested margins" block. ✓
- **Distinct from Step 0 gate** — called out in the header ("distinct from the Step 0 gate, which does"). ✓
- **Every other step byte-identical** — confirmed by the diff: only two additive hunks, no existing line touched. ✓

## Correctness / runtime considerations
- No renumbering: Step 8 remains Step 8; the new step slots in as 7.5, so no cross-reference to a step number is invalidated. The `## Features` header prefix-matching, ledger, gate, sweep, and commit policy are all untouched.
- The scan reads only code *outside* `.ai-factory/`, which the prune never modifies, so placing it after the roadmap edit (Step 7.5) has no ordering hazard — nothing it reads has been mutated by Steps 4–6. Placement is safe.
- No shell/quoting hazard introduced: the `grep` block is documentation, explicitly non-binding, and the agent can equally satisfy it with the `Grep` tool. This is consistent with the skill's pre-existing reliance on bash `grep` (Step 3 pipes `git log -p | grep`), so no new tool-permission expectation is introduced by this change.
- Expected false positives (e.g. the skill's own `ROADMAP` mentions when dry-run on this repo) are acknowledged by the spec as acceptable; the scan is a heads-up, not a proof.

## Notes (non-blocking, not defects)
- Placement as a full top-level `Step 7.5` rather than a Step 0 sub-step is a reasonable reading of the spec: it satisfies "not part of the Step 0 gate", "feeds Step 8", and keeps the capture near its echo. No behavioral consequence.

No bugs, security issues, or correctness problems found. The change faithfully implements the spec and is strictly additive.

REVIEW_PASS
