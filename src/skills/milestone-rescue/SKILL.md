---
name: milestone-rescue
description: >-
  Reads failed orchestrator artifacts (plans, plan-reviews, code reviews, patches),
  classifies the failure mode, extracts recurring issues, and proposes a concrete
  milestone description update in ROADMAP.md so the next orchestrator run starts with
  a better-specified task. Use when the pipeline stops with "PLAN_REVIEW_PASS never
  achieved" or "REVIEW_PASS never achieved" — trigger phrases: "rescue", "milestone
  failed", "pipeline stopped".
argument-hint: "[path/to/ROADMAP.md | ROADMAP_TESTS.md]"
allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion
---

# Milestone Rescue

Translates failed pipeline artifacts into a concrete ROADMAP.md improvement. When the
orchestrator exhausts its iteration limit, it leaves uncommitted plans, plan-reviews,
code reviews, and patches on disk — this skill reads them all, finds the root cause,
and proposes a precise update (or decomposition) to the milestone description so the
next run starts from a stronger specification.

Use this skill after the orchestrator stops — not to rewrite the plan or implement
anything, but to fix the upstream description that caused the failure. The output is
exactly one ROADMAP.md edit.

---

## Step 1 — Discover artifacts

Run `git status --short -- .ai-factory/` to find all uncommitted files under `.ai-factory/`.

Filter results to the four artifact directories only:

- `plans/`
- `plan-reviews/`
- `reviews/`
- `patches/`

Ignore any uncommitted files outside these directories (e.g. `notes/`).

If no uncommitted files are found in any of the four directories, stop and tell the
user: there is nothing to rescue.

**Identify the milestone slug.** Artifact filenames share a common `<NN>-<slug>` prefix
(e.g. `03-milestone-rescue`). Extract the slug from the filenames. If files from
multiple slugs are present, ask the user which milestone to rescue before proceeding.

**Read every artifact file found** — all rounds, not just the latest. The pattern of
failures across rounds matters as much as the final round. A plan-review from round 1
reveals what the planner missed first; a patch from round 2 shows whether the
implementer addressed it. Read them all before drawing any conclusions.

---

## Step 2 — Classify failure mode

Determine which phase of the pipeline failed by inspecting the artifact files:

**Plan-phase failure** — no plan-review file for this slug contains `PLAN_REVIEW_PASS`
on its own line. The planner could not produce a plan the reviewer accepted within the
iteration limit.

**Implement-phase failure** — at least one plan-review file contains `PLAN_REVIEW_PASS`
on its own line, but no review file contains `REVIEW_PASS` on its own line. The plan
was approved but the implementation repeatedly failed review.

**Non-convergence (done-but-unrecognized)** — when the implement-phase condition holds
(PLAN_REVIEW_PASS present, no REVIEW_PASS), check all three of the following before
declaring an implement-phase defect:

1. No review file contains `REVIEW_PASS` on its own line.
2. Every review file contains only Low or Informational findings — no Blocking or
   Critical severity.
3. The plan's deliverables show evidence of being produced or modified on disk. For
   `modify`-type deliverables (where the target file pre-existed), look for patches
   or reviews that confirm the change landed — do not treat file existence alone as
   sufficient.

When all three hold, classify as **non-convergence** — the implementation is likely
complete and correct; the reviewer kept generating cosmetic nits without clearing the
bar. If any review contains a Blocking or Critical finding, or any deliverable is
absent or unproduced, use the standard implement-phase failure classification instead.

Keep the severity inspection here lightweight — a blocking/non-blocking check, not a
full issue extraction (that is Step 3's job).

State the classification explicitly before proceeding. The failure mode determines what
kind of constraints to add to the milestone description — plan-phase failures usually
indicate specification gaps; implement-phase failures often reveal scope overload or
mechanical execution patterns.

---

## Step 3 — Extract issues

For each artifact file, extract all items that describe problems or improvement
requests. Real artifacts in this repo use inconsistent formats — do not hardcode
heading names. Scan for any section whose content lists problems, improvements, or
feedback regardless of exact heading level or wording. Common patterns include:
`### Issues`, `## Critical issues`, `## Critical Issues`, `## Suggestions`,
task-based headings like `### Task 1:`, or inline numbered lists.

**Deduplicate across rounds.** The same issue appearing in round 1 and round 2 is one
issue — but mark it as **recurring**. A suggestion that appears in 2+ rounds is
effectively a critical: the implementer failed to address it twice, which means the
milestone description needs to mandate it explicitly.

**Categorize each issue by root cause:**

- **Specification gap** — the milestone description was ambiguous or missing a
  constraint, edge case, or scope boundary. Fix: add a clause to the description.
- **Scope overload** — too many concerns in one milestone; the planner or implementer
  loses coherence between sub-tasks. Fix: decompose into smaller milestones.
- **Mechanical error** — recurring execution mistakes independent of the task
  specification (wrong line numbers, dropped content during replacement, missing
  guards, lost convention notes). Fix: add an explicit constraint that prevents the
  pattern.

Produce a numbered list of issues, each with:

1. A short description of the issue
2. Its root cause category
3. A proposed fix clause (one sentence, written at the *what* level — not *how*)
4. Whether it is recurring (appeared in 2+ rounds)

---

## Step 4 — Propose milestone update

**Determine `$TARGET_FILE`:**
- If argument names a file → use `.ai-factory/<that file>`
- If the milestone slug or artifacts suggest test tasks (keywords: test, tests, spec) → `$TARGET_FILE = .ai-factory/ROADMAP_TESTS.md`
- Otherwise → `$TARGET_FILE = .ai-factory/ROADMAP.md`

Read `$TARGET_FILE` and locate the milestone line matching the slug identified in Step 1.

**When classification is non-convergence** — do not propose a milestone-description
change. Instead, present via `AskUserQuestion`:

```
The implementation appears complete and correct.

Every review round was non-blocking (N rounds, all findings Low/Informational).
Deliverables are present on disk. The pipeline only failed to emit REVIEW_PASS
because the reviewer kept generating cosmetic nits without clearing the bar.

Recommended: commit the deliverable rather than re-running — another run would
likely loop again for the same cosmetic reasons.

Options:
1. Commit the deliverable (after any remaining trivial nits)
2. Re-run the pipeline anyway
3. Fold recurring spec-traceable nits into the spec note before committing
```

If the user chooses option 3, scan the review findings for nits that reference a gap
in the spec note file (`.ai-factory/notes/<NN>-….md` for this milestone — not the
ROADMAP milestone line), propose the minimal clause addition, apply it to the spec
note file, then proceed as option 1.

Proceed to Step 5 with the user's choice recorded.

---

For real defect classifications (plan-phase failure or implement-phase failure),
determine the **dominant root cause** from the issue list in Step 3 — the category
with the most issues (or most recurring issues if counts are equal).

Present the proposal via `AskUserQuestion` using the appropriate template:

---

**When dominant root cause is spec-gap or mechanical-error** — propose clause update
as primary:

```
Proposed update to milestone "<title>":

  + <one clause per issue — concise, imperative>
  + <next clause>

Options:
1. Apply the update
2. Decompose into smaller milestones instead
3. Let me edit the proposal first
```

Compose the proposed line by taking the existing milestone line and appending each
clause as a semicolon-separated addition, matching the existing ROADMAP style (see
root ROADMAP.md for examples of inline numbered sub-steps and inline constraints).

---

**When dominant root cause is scope-overload** — propose decomposition as primary:

```
Proposed decomposition of milestone "<title>":

  → <milestone 1 title>: <description>
  → <milestone 2 title>: <description>
  [→ <milestone 3 title>: <description>]

Options:
1. Apply the decomposition
2. Add clauses to the existing milestone instead
3. Let me edit the proposal first
```

Replace the original milestone with 2–3 smaller ones, ordered by dependency. Each
new milestone inherits the constraints relevant to its scope from the analysis.

---

If the user chooses **option 2** in either variant, compose and present the
alternative proposal using the other template variant, then confirm before
proceeding to Step 5.

If the user chooses **option 3** in either variant, ask them for their edits and
incorporate them before applying.

---

## Step 5 — Apply and clean up

**Non-convergence + options 1 or 3 (commit accepted):** if the classification from
Step 2 is non-convergence and the user chose option 1 or 3 in Step 4, skip the
artifact cleanup and the sidecar update entirely. Leave plans, plan-reviews, reviews,
patches, and the sidecar in place — they describe completed, correct work pending a
commit. Proceed directly to Step 5.5.

**Non-convergence + option 2 (re-run):** if the classification is non-convergence
and the user chose option 2 in Step 4, skip the `$TARGET_FILE` edit (no description
change was proposed) and follow the **implement-phase (re-implement)** cleanup path:
keep the plan `.md` and passing plan-reviews, delete reviews and patches for this
slug, and update the sidecar `step` to `"plan_reviewed"`. Then proceed to Step 5.5.
The reviewer will start fresh from the existing approved plan.

Apply the confirmed change to `$TARGET_FILE`, then delete the stale artifacts.

**If update:** use Edit to modify the milestone line in ROADMAP.md. Keep the
description concise — each constraint is one semicolon-separated clause. Match the
style of surrounding milestone lines.

**If decompose:** use Edit to replace the single milestone line with the new milestone
lines. Order them by dependency. Verify each new line reads coherently in context.

**Clean up artifacts.** After `$TARGET_FILE` is updated, delete stale uncommitted
files for this slug. Use `git status --short -- .ai-factory/` to identify them, then
delete using git-native commands only:

- Files marked `??` (untracked) → `git clean -f -- <path>`
- Files marked `A ` (staged/added) → `git rm -f -- <path>`

The set of files to delete depends on the failure mode from Step 2:

**Plan-phase failure (full reset)** — delete all four artifact types: the plan `.md`
file, all plan-review files, all review files, and all patch files for this slug.
Nothing of the discarded plan attempt should remain.

**Re-plan-review (plan corrected in place)** — the plan `.md` has been edited to fold
in reviewer findings and is kept. Delete all plan-review files for this slug (they
reviewed the old plan). Delete all review and patch files for this slug. Keep the
`.json` sidecar. Set `step` to `"planned"`.

**Implement-phase failure (re-implement)** — keep the plan `.md` and any plan-review
files that contain `PLAN_REVIEW_PASS` (they describe a valid plan). Delete only the
review files and patch files for this slug.

Do NOT delete `.json` sidecar files from `plans/` except on a full reset, where the
sidecar is deleted alongside the plan — the sub-step below handles all three cases. Do NOT
delete committed files. Do NOT touch `.ai-factory/notes/`. Do NOT delete files
belonging to other milestone slugs.

### Valid sidecar `step` states

This is a **closed set** — Step 5 picks one of the five values below, never invents
one. This table mirrors `_validate_sidecar_step()` / `_detect_milestone_step()` in
`orchestrator/main.py` — if the orchestrator's accepted set changes, update this table;
do not let them diverge.

| `step` value | Resumes at | Required on disk to validate |
|---|---|---|
| `"planned"` | plan-review, attempt 1 | none — always valid |
| `"plan_review_failed:N"` | plan, attempt N+1 | `plan-reviews/{seq}-{slug}-plan-review-N.md` |
| `"plan_reviewed"` | implement, iter 1 | a plan-review file ending with `PLAN_REVIEW_PASS` |
| `"implemented"` | review, iter 1 | none — always valid |
| `"review_failed:N"` | implement, iter N+1 | `reviews/{seq}-{slug}-review-N.md` |

**Silent failure mode.** The orchestrator clears any `step` value whose required
artifact is missing and falls through to the disk heuristic — writing a wrong value
silently loses the intended resume point and can re-run the planner from scratch.

**Test mode.** In test mode, `review_failed:N` is replaced by `test_run_failed:N`
(artifact: `test-runs/{seq}-{slug}-test-N.txt`).

**Always-valid guard.** `"planned"` and `"implemented"` carry no artifact reference
and always validate — the orchestrator accepts them unconditionally. They are therefore
only safe to write when the corresponding earlier-phase artifacts actually exist on
disk: write `"planned"` only when the plan `.md` is present; write `"implemented"`
only when the plan `.md` is present and a non-empty working diff exists. Never write
`"planned"` after deleting the plan `.md` — the orchestrator would accept the value
and then fail to find the plan it expects to review.

**Update or delete the sidecar.** The sidecar's lifetime tracks the plan's — plan
gone → sidecar gone; plan kept → sidecar updated. Locate the JSON sidecar at
`.ai-factory/plans/{seq}-{slug}.json` — the same `<NN>-<slug>` prefix identified in
Step 1.

**Full reset (plan `.md` deleted above):** delete the `.json` sidecar using
git-native commands — `git rm -f -- <path>` if tracked or staged, `git clean -f --
<path>` if untracked. The loss of `planner`, `implementer`, and `elapsed` is
intentional — this sidecar described a discarded attempt.

Emit: `Sidecar deleted (full reset).`

**Plan `.md` kept (re-implement or re-plan-review):** check the working tree for the
sidecar (attempt to read it or list with `Glob`).

- If the file exists, read it and parse it as JSON.
- If it does not exist, start from an empty JSON object.

Inspect which plan-review and review files for this slug remain on disk **after** the
cleanup deletions above, then determine the correct `step` value:

| Situation after cleanup | Write `step` |
|---|---|
| Plan `.md` corrected in place; plan-reviews, reviews deleted | `"planned"` (create sidecar if absent) |
| Plan-reviews exist and pass, reviews deleted | `"plan_reviewed"` (create sidecar if absent) |

If both plan-reviews and reviews pass on disk, the orchestrator finished — surface
this to the user and skip the sidecar update.

Update **only** the `step` key in the JSON object. Preserve every other key already
present — `planner`, `implementer`, `elapsed`, and any others — untouched. Do not
overwrite `planner`, `implementer`, or `elapsed`. Serialize the result back as JSON
with 2-space indentation and write it to the sidecar path using `Write`.

Emit: `Sidecar updated: step set to "<value>".` (where `<value>` is whichever step was written)

Show the user the list of deleted files and confirm the rescue is complete.

---

## Step 5.5 — Propagate findings to open milestones

For a non-convergence classification there are no real defects to propagate — every
round was non-blocking, so propagation is a no-op. Do not surface cosmetic nits to
unrelated milestones.

After `$TARGET_FILE` is updated, scan the remaining `- [ ]` milestones in `$TARGET_FILE` for the same gaps.

**Which issues to propagate** (in priority order):

- **Recurring issues** (appeared in 2+ rounds) → highest priority; the implementer couldn't fix it even with a patch, so the description is the only reliable enforcement. Propagate to any open milestone that touches the same files, APIs, or patterns.
- **Mechanical errors** → propagate to milestones with the same pattern type (same bridge, same threading model, same API family).
- **Specification gaps** → propagate only if the open milestone is in the same domain.

**How to identify matches:**

For each issue selected for propagation, scan open milestone descriptions for:
- The same file paths or module names
- The same API, class, method, or operator family
- The same structural pattern (e.g. "bridge", "repository", "hook", "middleware")

**If matches found**, present a single question:

```
These open milestones may have the same gaps. Apply the same fix?

→ MilestoneA: + <proposed clause>
→ MilestoneB: + <proposed clause>

Options:
1. Apply all
2. Review each individually
3. Skip
```

If no matches found, or if all issues were domain-specific to the failed milestone, skip silently.

---

## What NOT to do

- Do not rewrite the plan — that is the orchestrator's job on the next run
- Do not implement the fix — same reason
- Do not keep stale artifacts — they describe a failed attempt at the old specification
  and will confuse the next planner agent
- Do not add implementation details to the milestone — keep constraints at the *what*
  level, not the *how* level
- Do not delete committed files or files belonging to other milestones
- Do not skip reading earlier rounds — the pattern of failures across rounds is the
  primary signal, not just the final round
- Do not overwrite `planner`, `implementer`, or `elapsed` in the sidecar — on a
  re-implement rescue the sidecar is updated (only `step` changes); on a full reset
  the sidecar is deleted entirely alongside the plan
- Do not write `"planned"` or `"implemented"` when the corresponding artifact is
  absent — both are always-valid states the orchestrator accepts without artifact
  checks, so writing one after deleting the plan `.md` (or before any working diff
  exists) silently sends the orchestrator into the wrong phase
