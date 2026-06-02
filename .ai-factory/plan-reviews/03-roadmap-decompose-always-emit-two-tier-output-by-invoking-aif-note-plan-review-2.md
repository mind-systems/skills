# Plan Review 2: roadmap-decompose — always emit two-tier output by invoking aif-note

**Plan:** `.ai-factory/plans/03-roadmap-decompose-always-emit-two-tier-output-by-invoking-aif-note.md`
**Risk Level:** 🔴 High (one load-bearing blocker still open from review 1)
**Verdict:** NOT READY. The plan is well-grounded and surgically scoped, but the single critical issue raised in review 1 — `Skill` missing from `roadmap-decompose`'s `allowed-tools` — is still absent from all four tasks. As written, the plan's central mechanism (invoke aif-note via the Skill tool) may not fire, which is the exact flakiness the feature exists to eliminate. A second, deeper concern about how aif-note scopes its output per task is also worth resolving before implementation.

## Context Gates

- **Architecture** (`.ai-factory/ARCHITECTURE.md` present): WARN — non-blocking. The dependency model section explicitly says "Skills invoke other skills by name … invocations are runtime text instructions." This plan introduces a *programmatic* skill-to-skill invocation via the Skill tool, which is consistent with the `aif` precedent but is the first domain-skill→aif-skill orchestration. No boundary violated; the change stays inside one skill file. No `## Features` anchor references either skill, so no anchor conflict.
- **Rules** (`.ai-factory/RULES.md`): not present — gate skipped (WARN, non-blocking).
- **Roadmap** (`.ai-factory/ROADMAP.md` present): PASS — work is explicitly linked. ROADMAP.md milestone "roadmap-decompose: always emit two-tier output by invoking aif-note" carries `Spec: .ai-factory/notes/13-task-decompose-two-tier-via-aif-note.md`. Plan, spec note 13, concept note 09, and the roadmap entry are mutually consistent.
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present — no project-specific review overrides to apply.

## Critical Issues

### 1. `Skill` is still missing from `roadmap-decompose`'s `allowed-tools` — no task adds it (UNRESOLVED from review 1)

Review 1 flagged this as the one blocker. The plan has **not** changed: target frontmatter is still

```
allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion
```

`Skill` is not in the list, and none of Tasks 1–4 mention the frontmatter at all. Yet Task 1 step 3 and Tasks 2–3 all hinge on "**invoke the `aif-note` skill via the Skill tool**." The in-repo precedent confirms the requirement: the only other skill that orchestrates a sub-skill — `aif` — declares `Skill` (and `WebFetch`, `AskUserQuestion`, etc.) in its `allowed-tools` (`.claude/skills/aif/SKILL.md`). Without `Skill` in the allowlist, the invocation is liable to be blocked or to surface a permission prompt mid-run — defeating the determinism the plan is chasing ("make the agent do it reliably every run", "the flakiness from manual chaining is gone").

**Fix:** add `Skill` to `roadmap-decompose`'s `allowed-tools` (fold into Task 1). One line, but it is the load-bearing change for the entire feature. It must be an explicit task step, not left implicit.

## Other Findings (non-blocking, but address before/during implementation)

### 2. aif-note's "summarize the whole conversation" workflow may not cleanly scope to one task (design risk — WARN)

This is the deeper concern review 1 did not surface. aif-note is built to **mine the current conversation context** — its Step 1 is literally "Review the full conversation to identify what was researched," and it derives its own slug and `<NN>`. The plan instructs decompose to invoke aif-note per atomic task with only the instruction "the content is a task spec," explicitly forbidding any template/behavior override.

The tension: in a single decompose run that produces N tasks, decompose drafts each task's full spec, then invokes aif-note N times. Each invocation re-reads the *entire* conversation — which by then contains every task's draft spec plus all surrounding decompose chatter. Nothing in aif-note's contract guarantees it will isolate "task K's spec" rather than blend tasks, mis-title, or pick a slug that doesn't match the task name. The plan's mitigation (capture the path aif-note reports back) keeps the `Spec:` tag *accurate*, but does not guarantee the note's *content* is correctly scoped to one task.

This does not require altering aif-note. It only requires the invocation prompt to be specific: pass aif-note the task name (as its `$1` slug arg — that is aif-note's documented input, not a behavior override) and clearly delimit *which* drafted spec is the subject. Recommend Task 1 spell out that the aif-note invocation names the specific task and its spec text, so aif-note has an unambiguous subject. Worth one sentence; otherwise the per-task notes may be the next source of flakiness.

### 3. Frontmatter `description` will go stale (WARN — repeat of review 1 finding 2)

The skill `description` still advertises "each entry is a fully specified task: what exists today, what needs to change, which files and methods to touch, and explicit guard conditions." After this change the roadmap *entry* is a ~600-char contract line and the full spec lives in the note. No task updates the frontmatter description. This is user-facing skill-discovery text — recommend a small wording update folded into Task 1 or Task 4.

### 4. Sequential note numbering not stated (WARN — repeat of review 1 finding 3)

aif-note allocates `<NN>` by scanning `.ai-factory/notes/` for the highest `[0-9][0-9]-*.md` and incrementing. This is collision-free **only if** decompose invokes aif-note strictly sequentially (each note written to disk before the next invocation). The per-task procedure is inherently sequential, so it holds in practice, but a gate split producing "two invocations" should explicitly run them one-after-another, not batched. Note 09 called this out ("allocate numbers sequentially … so two tasks never collide"). One sentence in the Task 1 procedure block prevents a future parallel-invocation regression.

## Verified — assumptions that hold

- **aif-note is model-invocable.** `.claude/skills/aif-note/SKILL.md` has `disable-model-invocation: false` and `user-invocable: true`. The plan's premise holds in the current tree.
- **aif-note writes `<NN>-<slug>.md`, no `task-` prefix.** The plan's tag form `Spec: .ai-factory/notes/<NN>-<slug>.md` matches aif-note's actual naming (notes 09/13 used a `task-` prefix, but aif-note owns naming, so dropping it is correct and consistent with "do not alter aif-note").
- **aif-note reports the saved path** (Step 4: `Note saved: .ai-factory/notes/<NN>-<slug>.md`), so "capture the path aif-note reports back" is achievable.
- **All touchpoints are accurate.** Step 1.3, Steps 2.4/2.5, the "Roadmap File Format" section, and "Critical Rules" all exist and currently carry the inline-spec instructions the plan replaces. Atomicity Gates 1.3.1/2.4.1 exist; the plan correctly leaves their logic intact and runs the gate on the full spec before notes/contract lines.
- **File path correct.** `.claude/skills/roadmap-decompose/SKILL.md` exists; all four tasks target it.
- **Editing this skill is allowed.** `roadmap-decompose` is on CLAUDE.md's custom / never-overwrite-from-upstream list.
- **Mode 3 (`check`) correctly left untouched** — it only flips `[ ]`→`[x]`; unaffected by the two-tier shape.
- **No migration.** Plan and spec note 13 both correctly say *do not* bulk-migrate pre-existing legacy inline tasks — avoiding roadmap diff churn.

## Positive Notes

- Tightly scoped, surgical change with correct dependency ordering (Tasks 2–4 depend on Task 1's shared procedure block) — the right way to avoid four drifting copies of the procedure.
- Strong provenance discipline: reconciles note 09's concept against its superseded inline-template mechanism, and inherits note 13's char-budget numbers consistently.
- Char budget framed as guidance not a hard clamp — sensible, avoids brittle output rules.

## Recommended Action

1. **Blocking:** add `Skill` to `roadmap-decompose`'s `allowed-tools` as an explicit step in Task 1 (Critical Issue 1).
2. **Strongly recommended:** make the aif-note invocation prompt name the specific task + its spec text and pass the task slug as aif-note's `$1` (Finding 2), and state that invocations run sequentially (Finding 4).
3. **Cheap:** refresh the frontmatter `description` to the contract-line + spec-note shape (Finding 3).

With item 1 addressed (and ideally 2), the plan is ready to implement.
