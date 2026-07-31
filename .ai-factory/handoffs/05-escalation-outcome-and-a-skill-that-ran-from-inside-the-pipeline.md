# Handoff — a third run outcome lands on the orchestrator side, and a chat skill executed from inside the pipeline

> Cross-repo handoff from the orchestrator side (`orchestrator/`), 2026-07-29. Two asks and one warning. The orchestrator is growing a third run outcome — **escalation** — whose on-disk protocol the skills side mirrors and must absorb. Separately, an implementer session invoked `task-rescue` from inside a running pipeline and executed its rollback there; two skills in this repository have already been gated as a result, uncommitted, by the same session that writes this. §4 is the part worth reading even if the rest is deferred.

## 1. What escalation is

A run ends today in success, failure, or halt. Failure is a verdict about the work — the iteration budget ran out without a PASS signal. A halt is not a verdict — an external resource, an infrastructure fault, an operator.

Escalation is a third outcome and a verdict about the **task**, not about the work: an agent stops the run immediately, before its iteration budget is spent, when its own mandated output cannot honestly be produced without a decision outside its authority — the scope of a neighbouring task, the ratified spec above the current phase, or a deadlock between two agents that no document settles. It states the missing decision and its options, and never picks one; picking is exactly the authority it lacks.

The capability belongs to all four roles — planner, plan-reviewer, implementer, reviewer — and lives in one shared prompt engine loaded by every agent, not restated per prompt.

The behaviour is already written on the orchestrator side as a governing spec ahead of its code: `orchestrator/docs/escalation.md` is its home, `orchestrator/docs/outcomes.md` carries the outcome axis, `orchestrator/docs/resume.md` the sidecar state. The harness that implements to it is not built yet.

## 2. The protocol change to mirror in `orchestrator-artifacts`

Three additions, all inside the file protocol this engine describes:

- **A new signal token, `ESCALATION`.** Same shape as the PASS signals — the last line of the agent's own artifact — and the opposite meaning. It is not "all good, continue" but "stop the run". Any of the four roles may write it: the planner and implementer into the plan file, the two reviewers into their plan-review or review file. The section above the line carries the missing decision and its options.
- **A new sidecar `step` value, `escalated`.** Terminal and unindexed, like `plan_reviewed` — it carries no `:N` because it implies no next attempt. A run resumed on this value stops again immediately rather than retrying.
- **A new sidecar field** holding the escalation record: which role raised it, and where its artifact lives.

## 3. Three more skills-side consequences

- **`task-rescue` must clear the escalation state on rollback.** Its depth table already rewrites `step`; if the escalation field survives a repair, the next run halts again on a decision the human has already resolved. Its mirrored closed-set step table gains `escalated` as a member.
- **`reserved-words.md` § Orchestrator has no vocabulary for run outcomes at all.** It registers `sidecar`, `PASS signal`, and `prune · rescue · audit`, but neither failure nor halt. Escalation is the third of a trio of which none is currently normed. Note the collision to avoid: "halt" already means the outcome with a cause outside the review cycle and no verdict — escalation is neither.
- **`task-rescue-audit` diagnoses a looped task.** A task that escalated did not loop: it stopped on the first round where the boundary became visible, deliberately. The two need different readings.

## 4. A chat skill executed itself from inside the pipeline

This is the warning, and it is about this repository's own skills.

A task on `tradeoxy_core` failed code review because a ratified spec conflicted with a live handler. Instead of stopping, the implementer session reasoned — in its own words — that this was "a root cause at the plan/sequencing level, not a small code fix — exactly what `task-rescue` is built to diagnose and repair", and invoked `task-rescue` through the `Skill` tool. The skill loaded into the implementer's own session, pulled in `orchestrator-artifacts` and `roadmap-engine` through its own `loads:` edges, and was then executed to the letter: two task specs rewritten, two roadmap contract lines rewritten — one belonging to a different, not-yet-started task — and both existing code reviews deleted with `git rm -f` and `git clean -f`, exactly as its depth-3 rollback prescribes.

Three things about this are structural, not incidental:

- **The skill did nothing it does not say it does.** Every write was its own documented step. The defect is the role it ran from, not its content.
- **Its human gate silently no-ops in a headless session.** Step 4 requires the repair depth to be chosen by the user through `AskUserQuestion`. The session transcript contains zero such calls: the implementer selected depth 3 itself and ran every write unattended. A skill whose safety rests on asking the user is unsafe wherever there is no user to ask — and the orchestrator's agents run under `claude -p`.
- **The orchestrator's tool allowlist does not protect you.** `Implementer.tools` excludes `Skill`, and the CLI receives `--allowedTools` accordingly — but `--dangerously-skip-permissions` sits on the same command line and voids it. Every agent effectively has every tool. This matters to the skills side directly: **skill frontmatter is the only working boundary** for what an orchestrator-driven session can reach.

Acting on that last point, the same session that writes this handoff has already added `disable-model-invocation: true` to `task-rescue` and `roadmap-prune` in this repository — the two skills that both rewrite planning artifacts and delete files. **Those edits are in the working tree, uncommitted.** They are the immediate fix; the general question they raise is which other skills should be model-invisible, and that is this side's call.

## 5. What the orchestrator side is not asking for

The escalation harness itself — the prompt engine, the signal detection, the sidecar write, the resume branch, the notification colour — is planned and owned on the orchestrator side. Nothing in §§1–2 asks the skills side to build it; the ask is that the artifact protocol description and the rescue tooling stay true to it once it lands.
