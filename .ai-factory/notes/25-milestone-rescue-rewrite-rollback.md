# milestone-rescue: Refactor — Repair by Depth, Roll Back to the Repaired State

**Date:** 2026-06-26
**Source:** conversation context + reading `~/projects/orchestrator`

## Key Findings

- This is a **refactor**, not a rewrite or a gutting. The skill keeps every real capability — diagnose the failure, repair the real cause, roll the state back, check downstream tasks, flag a malformed task — and gets leaner by **compressing and de-duplicating** (merging the propose/apply overlap, the near-duplicate AskUserQuestion templates, and the overlapping sidecar prose), not by deleting features. Behavior improves slightly.
- **Repair model = depth.** When rescuing, the fix extends from the spec tier downward as far as the cause requires, in three nested variants:
  1. **spec note + contract line** — the requirement itself was wrong.
  2. **spec note + plan** — spec fixed and the plan corrected to match.
  3. **spec note + plan + code** — fixed all the way down, by hand.
- **Rollback goes to exactly the repaired state** ("откат до починенного состояния"): keep everything up to and including what was repaired, discard everything after, set the sidecar so the orchestrator re-validates from there.
- The **contract line IS edited** — it is the roadmap half of the two-tier spec pair (with the spec note). Fixing the spec means fixing both tiers. (My earlier "no ROADMAP edit" was wrong.)
- **Downstream propagation stays** (after a rescue, check whether the orchestrator's findings affect the *following* milestones) and **scope-overload stays as a flag** (skill recognizes a genuinely malformed task and tells the user to run `roadmap-decompose` — it does not decompose itself; rare but real).

## Details

### Orchestrator mechanics (ground truth from `~/projects/orchestrator`)

Pipeline per milestone: plan → plan-review (loop to `max_iterations`) → implement → review (loop) → commit. Agents talk only through files in `.ai-factory/`: `plans/` (plan `.md` + `{NN}-{slug}.json` sidecar), `plan-reviews/`, `reviews/`, `patches/`. PlanReviewer writes `PLAN_REVIEW_PASS`; Reviewer writes `REVIEW_PASS`. No pass within the limit → orchestrator stops, everything uncommitted — that is when rescue runs. The planner reads the **spec note**: `roadmap.py` passes the contract line verbatim to the planner (`agents.py:268`) and the line ends with `` Spec: `.ai-factory/notes/<NN>-<slug>.md` ``.

**Sidecar `step` (closed set, mirrors `_validate_sidecar_step` / `_detect_milestone_step`, `main.py:108/157`).** Only ever change `step`; preserve `planner`/`implementer`/`elapsed`. Resume mapping:

| `step` | Resumes at |
|---|---|
| `"planned"` | plan-review, attempt 1 |
| `"plan_review_failed:N"` | plan, attempt N+1 |
| `"plan_reviewed"` | implement, iter 1 |
| `"implemented"` | review, iter 1 |
| `"review_failed:N"` | implement, iter N+1 |
| *(plan `.md` absent)* | plan, attempt 1 (re-plan) |

A `step` whose artifact is missing is silently cleared → orchestrator falls back to a disk heuristic. Keep the table as the source-of-truth reference; orchestrator owns it, don't diverge.

### The three repair depths → rollback states

The agent diagnoses how deep the cause goes, repairs to that depth, then rolls back to exactly that state. The **user picks** the depth (their explicit "fix Y / delete X" overrides). Each row: repair → keep → delete → sidecar.

1. **spec (note + contract line).** The requirement was wrong. Repair the spec note `.ai-factory/notes/<NN>-<slug>.md` **and** its contract line in `ROADMAP.md`. The plan is built on a stale spec → regenerate it. Delete plan `.md`, plan-reviews, reviews, patches, **and** the sidecar (plan gone → sidecar gone). Orchestrator re-plans from the fixed spec (plan absent → plan attempt 1).
2. **spec + plan.** Repair spec (note + contract line) and the plan `.md`. Keep plan + sidecar. Delete plan-reviews (reviewed the old plan), reviews, patches. Sidecar `step` → `"planned"` → re-runs plan-review on the fixed plan.
3. **spec + plan + code.** Repair spec, plan, and the code by hand in the working tree. Keep plan + passing plan-reviews + the hand-fixed diff + sidecar. Delete reviews, patches ("откатив ревьюшки"). Sidecar `step` → `"implemented"` → re-runs review on the fixed code.

(In practice the spec may already be fine and only the plan/code need touching — the depth is "how far down the cause reaches," and the spec tier is just the top of that range, edited only when the requirement itself was the problem.)

Deletions git-native: untracked (`??`) → `git clean -f -- <path>`; staged (`A `) → `git rm -f -- <path>`. Never delete committed files or files of other slugs.

### Downstream propagation (keep — it is the point of rescuing)

After the milestone is rescued, scan the following `- [ ]` milestones: did the orchestrator's findings (recurring issues, the corrected spec) affect them? If a later task touches the same files/APIs/pattern or shares the corrected assumption, surface it and offer to apply the same fix to its spec note + contract line. This is what makes a rescue more than a local patch.

### Scope-overload (keep as a flag, not a decomposition)

If diagnosis shows the task is genuinely malformed (too many concerns, wrong framing) rather than just under-specified, the skill does **not** rewrite or decompose it. It flags this to the user and points them to `roadmap-decompose` — the user decides whether to remove the current task and replace it with new ones, or rewrite it from scratch. Rare, but it happens, and it must not be silently swallowed.

### What gets compressed (compression, not feature removal)

- **Non-convergence** — collapse the multi-step special-case machinery (`:68-90, :138-161, :225-236`) into one diagnosis outcome: all rounds non-blocking + deliverable present → recommend committing instead of re-running. One short clause, not its own sub-procedure.
- **Issue extraction** — drop the 4-attribute numbered-list formatting and the verbose dedup-across-rounds prose (`:95-125`); keep "read all rounds, the recurring root cause across rounds is the signal, it decides the repair depth."
- **AskUserQuestion templates** — replace the three large milestone-update/decompose code blocks (`:169-219`) with one compact depth choice.
- **Sidecar prose** — fold silent-failure-mode / always-valid-guard / test-mode paragraphs (`:289-302`) into the table + one line.
- **Step 4 / Step 5 overlap** — the proposal step and the apply step repeat the cleanup logic; merge into one apply section keyed by the three depths.

### Frontmatter

- `description` — rewrite around diagnose → repair (spec / spec+plan / spec+plan+code) → roll back to the repaired state → check downstream. Keep trigger phrases "rescue", "milestone failed", "pipeline stopped".
- `allowed-tools` — keep `Read Write Edit Glob Grep Bash(git *) AskUserQuestion` (Edit now repairs the contract line, spec note, plan, and code).
- `argument-hint` — keep the optional `ROADMAP.md | ROADMAP_TESTS.md` arg (contract-line edits still target it).

### Guards

- One file: `src/skills/milestone-rescue/SKILL.md`. No Python, no orchestrator changes.
- Leaner via compression — do **not** drop diagnose, repair, rollback, downstream propagation, or scope-overload flagging.
- **Precision floor (keep word-for-word, never compress away):** the exact deleted-file set per variant (which dirs, `git clean` vs `git rm`); the exact `step` value per variant + the closed-set table; the "only touch `step`, preserve `planner`/`implementer`/`elapsed`" rule; the Step-1 artifact-discovery block.
- Keep Step-1 artifact discovery intact — `milestone-rescue-audit` points at it (note 22).
- `name: milestone-rescue` unchanged; keep it in CLAUDE.md "Custom skills — never overwrite from upstream".

## Decisions

- **Presentation order: by repair variant** — `spec` → `spec+plan` → `spec+plan+code`. The `AskUserQuestion` lists the three in this order (shallowest spec edit first, deepest hand-fixed code last), naming the resulting rollback state for each. Resolved by user.
