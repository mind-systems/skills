# 84.2 — the engine names the plan-reviewer session keys

## What is true now

`src/skills/orchestrator-artifacts/SKILL.md`, § "3. Sidecar fields", reads: "`planner`, `implementer` (resumable session ids), `step` (resume point — the closed set and its artifact requirements live in `task-rescue`, its only skill-side writer; the closed set now includes `escalated`), `elapsed` (seconds, cumulative), `escalation` (the escalation record: the role that raised it, the artifact path, and a one-line excerpt of the missing decision)." It names no key for a plan reviewer.

The orchestrator writes one. `PlanReviewer.review_plan` in `orchestrator/orchestrator/agents.py` takes the attempt number and, right after the agent returns and before it checks that the review file exists, calls `_write_session(plan_path, f"plan-reviewer-{attempt}", sid)`; the key is there even when the reviewer wrote no review or escalated. `_write_session` sets the key in the sidecar's JSON, so a re-run of an attempt replaces its own key and leaves the others. `process_task` in `orchestrator/orchestrator/main.py` builds the plan-review path `…-plan-review-{attempt}.md` and passes the same `attempt`. The run reads the sidecar by named keys only (`step`, `elapsed`, `planner`, `implementer`, `escalation`) and never reads this one. The orchestrator's `docs/features/resume.md` states the key the same way. The orchestrator's review of the task that added it raised the missing mirror as a deferred observation (`orchestrator/.ai-factory/reviews/trickster77777/26-30-1-a-plan-reviewer-s-session-id-is-kept-in-the-sidecar-review-1.md`).

§ "7. Mirrors-the-orchestrator invariant" has the file mirror the orchestrator's protocol and be updated when it changes there.

## What must be true after

In § "3. Sidecar fields", the paragraph reads:

"`planner`, `implementer` (resumable session ids), `plan-reviewer-<N>` (one plan reviewer's session id per attempt, kept even when that reviewer wrote no review; `<N>` is the round number its `plan-review-<N>` file carries; for reading only, never resumed by the run), `step` (resume point — the closed set and its artifact requirements live in `task-rescue`, its only skill-side writer; the closed set now includes `escalated`), `elapsed` (seconds, cumulative), `escalation` (the escalation record: the role that raised it, the artifact path, and a one-line excerpt of the missing decision)."

## What breaks on contact

**Rule:** a text breaks on this change if it lists the sidecar's keys as a closed set without the plan-reviewer family, or treats every session id in the sidecar as one the run resumes.

**Sweep:**
```
grep -rn "resumable session" src docs CLAUDE.md
grep -rn "Sidecar fields" src docs CLAUDE.md
grep -rn "any others" src docs CLAUDE.md
grep -rn "every other key" src docs CLAUDE.md
grep -rn "plan-reviewer" src docs CLAUDE.md
```

**Finding.** The search for `resumable session` returns § "3. Sidecar fields", the target. The search for `Sidecar fields` returns that heading and the skill's frontmatter description, "sidecar fields", which lists none and stays true. The searches for `any others` and `every other key` return `task-rescue`'s two rollback procedures that rewrite the sidecar and "Preserve every other key — `planner`, `elapsed`, and any others — untouched"; the family falls under "every other key", so the procedures keep it, and a kept key harms no resume, since the run never reads it; each stays true. The search for `plan-reviewer` returns the signals paragraph of § "2. Signals", which names the plan reviewer as a role and stays true. `task-rescue`'s valid-states table mirrors the orchestrator's `step` values and the family adds no `step` write, so it stays true; its capture of "every session id the sidecar holds, each under its key" takes the family in once § 3 names it. No doc or `CLAUDE.md` text appears in any output.
