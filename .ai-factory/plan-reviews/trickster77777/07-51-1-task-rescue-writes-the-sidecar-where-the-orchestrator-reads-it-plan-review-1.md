## Code Review Summary

**Files Reviewed:** 1 plan (target: `src/skills/task-rescue/SKILL.md`; cross-checked against the task spec `.ai-factory/specs/trickster77777/0203-…`, the phase note `.ai-factory/specs/trickster77777/145-task-rescue-and-the-artifact-protocol.md`, `src/skills/orchestrator-artifacts/SKILL.md` § "1. Layout", and `orchestrator/orchestrator/main.py`)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** — OK. The change stays inside one lens skill body and repeats the locator that skill already uses in Step 1. It defers to the engine `orchestrator-artifacts` § 1 rather than copying its content.
- **Rules** — WARN (non-blocking): there is no `.ai-factory/RULES.md` in this repo.
- **Roadmap** — OK. The plan matches the contract line 51.1 in `.ai-factory/roadmaps/trickster77777.md` (Phase 51), its `Spec:` note (0203) and the phase note (145). The phase note says "No document governs this", so there is no governing spec to check against.

### Ground-truth verification
- `grep -rn "seq}-{slug}.json" src/ docs/ CLAUDE.md` matches exactly the two write sites the plan names. The first is under "Depth: spec + plan" step 4, and the second is under "Depth: plan ratified, implementation absent" step 3. Each begins with the quoted sentence word for word.
- "Depth: spec + plan + code" step 5 inherits the procedure by reference ("same read/update/write procedure as the spec+plan depth above"), so it correctly stays unchanged.
- The orchestrator puts a named roadmap's sidecar under `plans/<artifact_subdir>/`. It sets `plans_dir = plans_dir / mode.artifact_subdir` in `main.py`. This matches the new sentence and `orchestrator-artifacts` § "1. Layout".
- `$TARGET_FILE` is set before Step 5 (in Step 1's governing-spec read and in Step 4), so `<stem>` can be resolved at both write sites.
- The replacement text in the plan matches the spec's "What must be true after" exactly. The plan keeps the rest of each step word for word, as the spec requires.
- The plan's guidance on wrapping and indentation is correct for this file: prose wraps at about 88 characters and list continuation lines are indented 3 spaces. The verify step uses a line-based grep. It still works after re-wrapping, because each path is a single unbroken backticked token that contains `{seq}-{slug}.json`.

### Critical Issues
None.

### Positive Notes
- The plan re-ran the spec's blast-radius sweep and lists what stays unchanged, with a reason for each item. This stops the implementer from "fixing" the inherited third depth or the Step 1 bullet.
- The edit is limited to one sentence per site, and the plan says explicitly that re-wrapping must not change any wording. That respects the "word-for-word" contract the spec relies on.
- The verify step includes a negative check (the old sentence is gone) and a check that the diff touches only those two paragraphs.

## Deferred observations
- Affects: Phase 51 phase note `.ai-factory/specs/trickster77777/145-task-rescue-and-the-artifact-protocol.md` — The "Valid sidecar `step` states" table in `src/skills/task-rescue/SKILL.md` also uses flat artifact paths in its "Required on disk to validate" column: `plan-reviews/{seq}-{slug}-plan-review-N.md`, `reviews/{seq}-{slug}-review-N.md`, and in the Test-mode line `test-runs/{seq}-{slug}-test-N.txt`. On a named roadmap, `orchestrator-artifacts` § 1 puts these under the same `<stem>/` segment. The task spec deliberately keeps the table unchanged, and the table describes the orchestrator's validation rather than giving the agent a path to write. The validation contract that actually applies ("a plan-review file … for this slug") names no path. This is outside 51.1's pinned scope, but whoever owns the phase may want to decide whether the table should cite the layout the way Step 1 does.

PLAN_REVIEW_PASS
