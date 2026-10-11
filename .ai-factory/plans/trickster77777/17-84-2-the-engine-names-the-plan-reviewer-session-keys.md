# Plan: 84.2 — the engine names the plan-reviewer session keys

## Context
`orchestrator-artifacts` § "3. Sidecar fields" names only `planner` and `implementer` as session ids. The orchestrator also writes `plan-reviewer-<N>` into the sidecar on every plan-review attempt (`PlanReviewer.review_plan` in `orchestrator/orchestrator/agents.py` calls `_write_session(plan_path, f"plan-reviewer-{attempt}", sid)` as soon as the agent returns, before it checks the review file), and the run never reads that key. This task makes § 3 name that key family, so the engine mirrors the orchestrator's protocol, as § "7. Mirrors-the-orchestrator invariant" requires. The after-text is pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0246-the-engine-names-the-plan-reviewer-session-keys.md`, § "What must be true after". Copy it exactly and do not paraphrase it.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit `orchestrator-artifacts`

- [x] **Rewrite the § 3 sidecar-fields paragraph**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  In § "3. Sidecar fields", replace the single paragraph (it opens "`planner`, `implementer` (resumable session ids), `step` …" and ends "… a one-line excerpt of the missing decision).") with the spec's pinned text:
  "`planner`, `implementer` (resumable session ids), `plan-reviewer-<N>` (one plan reviewer's session id per attempt, kept even when that reviewer wrote no review; `<N>` is the round number its `plan-review-<N>` file carries; for reading only, never resumed by the run), `step` (resume point — the closed set and its artifact requirements live in `task-rescue`, its only skill-side writer; the closed set now includes `escalated`), `elapsed` (seconds, cumulative), `escalation` (the escalation record: the role that raised it, the artifact path, and a one-line excerpt of the missing decision)."
  The only change is the new `plan-reviewer-<N>` clause, inserted between `(resumable session ids),` and `` `step` ``. Keep every other word byte-identical. Re-wrap the paragraph to the file's existing hard wrap of about 84 columns, matching the surrounding lines. Leave the heading, the frontmatter (its description already says "sidecar fields" in general terms and stays true), and every other section unchanged.

### Verify the blast radius

- [x] **Run the spec's sweep and confirm nothing else breaks** (depends on Rewrite the § 3 sidecar-fields paragraph)
  Files: none changed. This is a read-only check.
  From the repo root, run the sweep from the spec's § "What breaks on contact": `grep -rn` for `resumable session`, `Sidecar fields`, `any others`, `every other key` and `plan-reviewer` over `src docs CLAUDE.md`. Expected results:
  - `resumable session` and `Sidecar fields` return only the edited § 3 in `src/skills/orchestrator-artifacts/SKILL.md`.
  - `any others` and `every other key` return only the two sidecar-rewrite steps in `src/skills/task-rescue/SKILL.md` ("Preserve every other key — `planner`, `elapsed`, and any others — untouched"). Those steps stay true, because the new key family falls under "every other key".
  - `plan-reviewer` returns the new § 3 clause and the role list in § "2. Signals". Both stay true.
  - Nothing under `docs/` or in `CLAUDE.md` appears.
  Edit no other file. That includes `task-rescue`: its valid-states table and its session-id capture stay as they are.
