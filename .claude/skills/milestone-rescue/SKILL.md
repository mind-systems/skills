---
name: milestone-rescue
description: >-
  Reads failed orchestrator artifacts (plans, plan-reviews, code reviews, patches),
  classifies the failure mode, extracts recurring issues, and proposes a concrete
  milestone description update in ROADMAP.md so the next orchestrator run starts with
  a better-specified task. Use when the pipeline stops with "PLAN_REVIEW_PASS never
  achieved" or "REVIEW_PASS never achieved" — trigger phrases: "rescue", "milestone
  failed", "pipeline stopped".
argument-hint: "[path/to/ROADMAP.md]"
allowed-tools: Read Edit Glob Grep Bash(git *) AskUserQuestion
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

Read `.ai-factory/ROADMAP.md` (or the path provided as argument) and locate the
milestone line matching the slug identified in Step 1.

Determine the **dominant root cause** from the issue list in Step 3 — the category
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

Apply the confirmed change to ROADMAP.md, then delete the stale artifacts.

**If update:** use Edit to modify the milestone line in ROADMAP.md. Keep the
description concise — each constraint is one semicolon-separated clause. Match the
style of surrounding milestone lines.

**If decompose:** use Edit to replace the single milestone line with the new milestone
lines. Order them by dependency. Verify each new line reads coherently in context.

**Clean up artifacts.** After ROADMAP.md is updated, delete all uncommitted files
from `plans/`, `plan-reviews/`, `reviews/`, and `patches/` that belong to this
milestone's slug. Use `git status --short -- .ai-factory/` to identify them, then
delete using git-native commands only:

- Files marked `??` (untracked) → `git clean -f -- <path>`
- Files marked `A ` (staged/added) → `git rm -f -- <path>`

Do NOT delete committed files. Do NOT touch `.ai-factory/notes/`. Do NOT delete files
belonging to other milestone slugs.

Show the user the list of deleted files and confirm the rescue is complete.

---

## Step 5.5 — Propagate findings to open milestones

After ROADMAP.md is updated, scan the remaining `- [ ]` milestones for the same gaps.

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
