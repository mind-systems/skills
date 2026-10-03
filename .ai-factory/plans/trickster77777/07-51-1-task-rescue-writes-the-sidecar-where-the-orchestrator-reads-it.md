# Plan: 51.1 — task-rescue writes the sidecar where the orchestrator reads it

## Context
`src/skills/task-rescue/SKILL.md` Step 1 (bullet "Where the sidecar lives") already locates the sidecar per `orchestrator-artifacts` § 1 — flat `plans/<seq>-<slug>.json` for the default pair, `plans/<stem>/<seq>-<slug>.json` for a named roadmap. Two Step 5 rollback write sites still hard-code the flat path, so on a named roadmap the rollback lands where the orchestrator never reads it. This task replaces the first sentence of each write site with the read site's locator, pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0203-task-rescue-writes-the-sidecar-where-the-orchestrator-reads-it.md` § "What must be true after".

Blast radius (the spec's sweep, re-run while planning, same result):
- `grep -rn "seq}-{slug}.json" src/ docs/ CLAUDE.md` matches only the two write sites — in "Depth: spec + plan" step 4 and "Depth: plan ratified, implementation absent" step 3. Both change.
- "Depth: spec + plan + code" step 5 ("same read/update/write procedure as the spec+plan depth above") inherits the new locator by reference — leave it unchanged.
- These also stay unchanged: the Step 1 "Where the sidecar lives" bullet, the spec-depth deletion (it names no path), the escalation and no-repair branches, the "Valid sidecar `step` states" table, `orchestrator-artifacts`, and `docs/sakshi-harness/skill-cycle.md`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Point both rollback write sites at the read site's locator

- [x] **Rewrite the locator sentence at both Step 5 write sites**
  Files: `src/skills/task-rescue/SKILL.md`
  Under "**Depth: spec + plan**", step 4 currently opens: "Locate the sidecar at `.ai-factory/plans/{seq}-{slug}.json`." Under "**Depth: plan ratified, implementation absent**", step 3 opens with the same sentence. In both places, replace exactly that one sentence with this text, verbatim from the spec:

  ```
  Locate the sidecar where Step 1 does — `.ai-factory/plans/{seq}-{slug}.json` for the default roadmap pair, `.ai-factory/plans/<stem>/{seq}-{slug}.json` for a named roadmap, `<stem>` being the stem of `$TARGET_FILE`.
  ```

  Everything after that sentence in each step stays word-for-word as it is: "Read it if present; start from `{}` if absent. Set the `step` key to …", the `implementer` and `escalation` deletions, the preserve-every-other-key clause, and the 2-space-indentation clause. The file hard-wraps prose at a fixed column (lines are about 88 characters, with list continuation lines indented three spaces). Re-wrap only the edited paragraph to match. Do not change wording when re-wrapping, and do not touch neighbouring paragraphs.

  Verify: `grep -n "seq}-{slug}.json" src/skills/task-rescue/SKILL.md` shows the new sentence (both paths) at each of the two sites, and no remaining "Locate the sidecar at `.ai-factory/plans/{seq}-{slug}.json`". `git diff` touches only those two paragraphs.
