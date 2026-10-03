## Code Review Summary

**Files Reviewed:** 1 (`src/skills/task-rescue/SKILL.md`; the other staged files are pipeline artifacts: the plan, its sidecar, and plan-review-1)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture:** OK. The edit stays inside one lens skill body. The new sentence points back to Step 1's locator, which in turn defers to `orchestrator-artifacts` § 1. No engine content is inlined.
- **Rules:** WARN (non-blocking). The repo has no `.ai-factory/RULES.md`.
- **Roadmap:** OK. The change matches contract line 51.1 in `.ai-factory/roadmaps/trickster77777.md`, its task spec `0203-…`, and phase note 145. The phase note says no document governs this work.
- **Skill context:** none (`.ai-factory/skill-context/aif-review/SKILL.md` is absent).

### Verification against the task spec
- **New sentence:** both write sites now open with the sentence from the spec's "What must be true after", word for word. The sites are "Depth: spec + plan" step 4 and "Depth: plan ratified, implementation absent" step 3. The sentence is: "Locate the sidecar where Step 1 does — `.ai-factory/plans/{seq}-{slug}.json` for the default roadmap pair, `.ai-factory/plans/<stem>/{seq}-{slug}.json` for a named roadmap, `<stem>` being the stem of `$TARGET_FILE`."
- **Rest of each step:** unchanged in wording. Only the line breaks moved, and the rewrapped lines respect the file's 3-space continuation indent and roughly 88-column width. Three lines in this region are longer than 88 columns, but they were already that long and the diff did not touch them.
- **Third depth:** "Depth: spec + plan + code" step 5 still reads "same read/update/write procedure as the spec+plan depth above". It therefore picks up the new locator, as the spec intends.
- **`$TARGET_FILE`:** it is set in Step 4 before Step 5 runs, so `<stem>` can be resolved at both sites.
- **Orchestrator side:** the orchestrator reads a named roadmap's sidecar under `plans/<artifact_subdir>/`, and the new sentence points there.
- **Default pair:** a repo on the default `ROADMAP.md` still resolves to the same flat file as before.
- **Leftovers:** `grep -rn "seq}-{slug}.json" src/ docs/ CLAUDE.md` finds no remaining flat-only locator sentence.

### Critical Issues
None.

### Positive Notes
- The edit is minimal: one sentence replaced at each site, and nothing else changed.
- The new sentence names Step 1 as the authority instead of copying the layout rule, so the read path and the write paths cannot drift apart again.

## Deferred observations
- Affects: Phase 51 phase note `.ai-factory/specs/trickster77777/145-task-rescue-and-the-artifact-protocol.md`. The "Valid sidecar `step` states" table in `src/skills/task-rescue/SKILL.md` lists flat artifact paths: `plan-reviews/{seq}-{slug}-plan-review-N.md`, `reviews/{seq}-{slug}-review-N.md`, and `test-runs/{seq}-{slug}-test-N.txt`. On a named roadmap these paths gain a `<stem>/` segment. The task spec pins the table as unchanged, and the table describes what the orchestrator validates; it is not a write path for the agent. Still, the phase owner may want to decide whether the table should cite the layout the same way Step 1 does.

REVIEW_PASS
