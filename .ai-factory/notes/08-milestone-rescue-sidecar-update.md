# milestone-rescue: Update JSON Sidecar After Cleanup

## Problem

After `milestone-rescue` deletes artifacts (plan-reviews, reviews) and cleans up, the orchestrator's JSON sidecar (`plans/{slug}.json`) retains the old `step` value referencing files that no longer exist.

Example: sidecar has `step: plan_review_failed:2`, rescue deletes plan-review-2.md → next orchestrator run tries to pass that file to the planner → reads a non-existent path.

The orchestrator has its own validation fix (notes/08 in the orchestrator project), but the rescue skill should also proactively write the correct `step` after cleanup — defense in depth, and makes the next run's behavior obvious without relying on the orchestrator's fallback.

## What step value to write after cleanup

After deleting artifacts, determine the correct `step` based on what remains on disk:

| Situation after cleanup | Write `step` |
|---|---|
| Plan-reviews deleted (or none pass) | `"planned"` |
| Plan-reviews exist and pass, reviews deleted | `"plan_reviewed"` |
| Plan-reviews pass, reviews exist but none pass | `"plan_reviewed"` (re-implement) |
| Sidecar doesn't exist | create it with correct `step` |

## Where in the skill to add this

**Step 5 — Apply and clean up** — after deleting artifact files, add:

1. Locate the sidecar: `plans/{seq}-{slug}.json` (same slug used for artifact deletion).
2. Read it if it exists (plain `json.load`), or start with `{}`.
3. Determine the correct `step` value from the table above by checking what plan-review and review files remain on disk after cleanup.
4. Write `step` back to the sidecar (`json.dump` with `indent=2`).
5. Tell the user: `Sidecar updated: step set to "{value}"`.

## What NOT to touch in the sidecar

- `planner` session ID — keep (planner can resume its session)
- `implementer` session ID — keep
- `elapsed` — keep

Only `step` is updated.

## Skill file location

`~/projects/skills/milestone-rescue/SKILL.md` — add the sidecar update as the last sub-step of **Step 5**, before the "show deleted files" summary.

**Include the mapping table verbatim** in SKILL.md — do not paraphrase or summarize it. The agent running the skill must see the exact table to make the correct decision without guessing. Copy the table from this note as-is into the skill body.
