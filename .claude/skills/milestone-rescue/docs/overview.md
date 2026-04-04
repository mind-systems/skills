# milestone-rescue — Overview

## What it solves

The orchestrator runs a plan → implement → review pipeline for each milestone. When
it hits the iteration limit without `PLAN_REVIEW_PASS` or `REVIEW_PASS`, it stops and
leaves artifacts on disk: uncommitted plans, plan reviews, code reviews, patches.

These artifacts contain the exact reasons the milestone failed — but they are written
for the next agent in the pipeline, not for the human. The human is left with a wall
of text and no clear action.

`milestone-rescue` reads those artifacts, extracts what the reviewer agents didn't
like, and translates it into a concrete proposal: update the milestone description in
ROADMAP.md so the next orchestrator run starts with a better-specified task. Or, if
the task is too broad, decompose it.

---

## When to invoke

After the orchestrator stops with:
```
STOPPED — Plan failed review after N attempt(s).
```
or
```
STOPPED — Implementation failed review after N attempt(s).
```

There are uncommitted files in `.ai-factory/plans/`, `.ai-factory/plan-reviews/`,
and/or `.ai-factory/reviews/`.

---

## What the orchestrator leaves behind

| Path | Written by | Contains |
|------|-----------|----------|
| `.ai-factory/plans/<n>-<slug>.md` | Planner | Latest plan attempt |
| `.ai-factory/plan-reviews/<n>-<slug>-plan-review-<r>.md` | PlanReviewer | Issues with the plan, round by round |
| `.ai-factory/reviews/<n>-<slug>-review-<r>.md` | Reviewer | Issues with the implementation |
| `.ai-factory/patches/<n>-<slug>-patch-<r>.md` | Reviewer | Fix instructions for the implementer |

All of these are uncommitted. The orchestrator only commits on success.

---

## Workflow

### Step 1 — Read all artifacts

Find all uncommitted files in `.ai-factory/`:

```bash
git status --short -- .ai-factory/
```

Read every file found: plans, plan-reviews, reviews, patches. Do not skip any — the
pattern of failures across rounds is as important as the final round.

### Step 2 — Identify the failure mode

Classify what stopped the pipeline:

**Plan-phase failure** — `PLAN_REVIEW_PASS` never appeared in any plan-review file.
The planner could not write a plan the reviewer accepted within the iteration limit.

**Implement-phase failure** — plan was approved, but `REVIEW_PASS` never appeared in
any review file. The implementer could not produce code the reviewer accepted.

### Step 3 — Extract reviewer complaints

For each review file, extract:
- **Critical issues** — things that blocked passing (the reviewer explicitly says
  "critical", "must fix", or the issue type that caused the plan/code to fail)
- **Suggestions** — non-blocking but repeated across rounds (a suggestion that
  appears in round 1 and round 2 is effectively a soft critical)
- **Patterns** — mechanical errors that recur (off-by-one line numbers, missing
  guards, lost convention notes when replacing blocks)

Distinguish between:
- **Task specification problems** — the milestone description was ambiguous, missing
  a constraint, or missing an edge case. Fix: enrich the task description.
- **Scope problems** — the milestone covers too much ground; the planner/implementer
  gets lost between the sub-tasks. Fix: decompose into smaller milestones.
- **Mechanical problems** — the task was fine but the plan had recurring execution
  errors (wrong line numbers, missing guards). Fix: add explicit constraints to the
  task description.

### Step 4 — Propose action

The proposal format depends on the dominant root cause from Step 3.

**When root cause is spec-gap or mechanical-error** — propose clause update as primary:

```
Proposed update to milestone "roadmap-prune skill":

  + replace Step 5 with simplified version, do not delete it
  + ARCHITECTURE.md read in Step 2 needs "if it exists" guard
  + when replacing a block, explicitly preserve any convention notes inside it

Options:
1. Apply the update
2. Decompose into smaller milestones instead
3. Let me edit the proposal first
```

**When root cause is scope-overload** — propose decomposition as primary:

```
Proposed decomposition of milestone "roadmap-prune skill":

  → roadmap-prune core: group tasks, find hashes, update ARCHITECTURE.md
  → roadmap-prune cleanup: delete pruned lines from ROADMAP.md, verify

Options:
1. Apply the decomposition
2. Add clauses to the existing milestone instead
3. Let me edit the proposal first
```

If the user picks option 2 in either variant, compose and present the alternative
proposal (clauses ↔ decomposition) before proceeding. If the user picks option 3,
incorporate their edits first.

### Step 5 — Apply and clean up

Apply the confirmed change to ROADMAP.md, then delete the stale artifacts.

**If update:** add the missing constraints inline as semicolon-separated clauses,
matching the style of surrounding milestone lines.

**If decompose:** replace the single milestone line with the new milestone lines,
ordered by dependency.

**Clean up** — delete all uncommitted files from `plans/`, `plan-reviews/`,
`reviews/`, and `patches/` that belong to this milestone's slug:

- Files marked `??` (untracked) → `git clean -f -- <path>`
- Files marked `A ` (staged) → `git rm -f -- <path>`

Do NOT delete committed files. Do NOT touch `.ai-factory/notes/`. Do NOT delete
files belonging to other milestone slugs.

---

## What NOT to do

- Do not rewrite the plan yourself — that is the orchestrator's job on the next run
- Do not implement the fix — same reason
- Do not keep the stale artifacts — they will confuse the next planner agent
- Do not add implementation details to the milestone description — keep it a
  milestone, not a plan. The constraints you add should be *what* to do, not *how*
