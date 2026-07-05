---
name: milestone-rescue
description: >-
  Reads failed orchestrator artifacts (plans, plan-reviews, code reviews, patches),
  diagnoses how deep the root cause reaches, repairs to that depth (spec / spec+plan /
  spec+plan+code / plan-ratified-implementation-absent), and rolls the sidecar +
  artifacts back to exactly the repaired state so the orchestrator re-validates from
  there. Also checks downstream milestones for
  the same gaps. Use when the pipeline stops with "PLAN_REVIEW_PASS never achieved" or
  "REVIEW_PASS never achieved" — trigger phrases: "rescue", "milestone failed",
  "pipeline stopped".
argument-hint: "[path/to/ROADMAP.md | ROADMAP_TESTS.md]"
allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion
loads: orchestrator-artifacts
---

# Milestone Rescue

The orchestrator exhausting its iteration limit and stopping is the tripwire — how the
failure was noticed, not what failed. The subject of this skill is the defect in the
task's specification (spec note + contract line) and its implementation: it reads the
artifacts left uncommitted on disk, diagnoses how deep that defect reaches
(specification gap? bad plan? broken implementation?), and repairs to exactly that
depth — then rolls the sidecar and the artifact set back to the matching repaired state
so the orchestrator re-validates from there rather than starting blind.

The roadmap contract line (in `$TARGET_FILE`) is the roadmap half of the two-tier spec
pair (alongside the spec note the milestone's `Spec:` tag names). It IS edited when the spec
tier is repaired. The output is not a single ROADMAP edit — it is a depth-keyed
repair: spec note + contract line, plan `.md`, or working-tree code, depending on how
deep the root cause runs. The user picks the depth; an explicit "fix Y / delete X"
overrides.

Ensure `orchestrator-artifacts` is loaded once this chat (via the Skill tool, only if
not already loaded) — it defines the artifact layout, naming, signals, sidecar
fields, and marker grammar referenced below.

---

## Step 1 — Discover artifacts

Run `git status --short -- .ai-factory/` to find all uncommitted files under `.ai-factory/`.

Filter results to the artifact directories (`plans/`, `plan-reviews/`, `reviews/`,
`patches/`) — layout and naming conventions are described in `orchestrator-artifacts`.

Ignore any uncommitted files outside these directories — the spec note itself
lives wherever the milestone's `Spec:` tag points, not in a fixed directory.

If no uncommitted files are found in any of the artifact directories, stop and tell
the user: there is nothing to rescue.

**Identify the milestone slug.** Extract the `<seq>-<slug>` shared by the artifact
filenames (see `orchestrator-artifacts` for the naming convention). If files from
multiple slugs are present, ask the user which milestone to rescue before proceeding.

**Read the phase's governing spec.** Determine `$TARGET_FILE` (the same resolution
Step 4 uses: argument-named file if given, else `.ai-factory/ROADMAP_TESTS.md` for test
slugs, else `.ai-factory/ROADMAP.md`), read it, and locate the phase section the
milestone belongs to. Check the phase header and its intro lines for a
`Governing spec:` reference. If present, read every named document in full before
proceeding to Step 2 — this is unconditional, not suspicion-based. If the milestone is
under no phase, or no `Governing spec:` is named, proceed as today. This read is
additive to Step 4's own `$TARGET_FILE` resolution and milestone-line locate — it does
not replace it.

**Read every artifact file found** — all rounds, not just the latest. The pattern of
failures across rounds matters as much as the final round. A plan-review from round 1
reveals what the planner missed first; a patch from round 2 shows whether the
implementer addressed it. Read them all before drawing any conclusions.

---

## Step 2 — Diagnose root cause and depth

Determine which phase failed and how deep the root cause runs. This classification is
an **internal routing signal** that feeds the depth choice in Step 4 — it is not itself
the diagnosis the user receives; the substantive diagnosis is Step 3's Diagnosis Report.
Signal semantics (`PLAN_REVIEW_PASS`, `REVIEW_PASS`, last-line requirement) are defined
in `orchestrator-artifacts`; the classification below only applies them.

**Plan-phase failure** — no plan-review file contains `PLAN_REVIEW_PASS` on its own
line. Root cause is likely a specification gap or scope overload; repair depth starts
at spec.

**Implement-phase failure** — at least one plan-review file contains `PLAN_REVIEW_PASS`,
but no review file contains `REVIEW_PASS`. Root cause is a defect in the code or plan;
repair depth is at least spec+plan.

**Stale implementer session (plan ratified, implementation absent)** — implement-phase
condition holds (a `PLAN_REVIEW_PASS` plan-review is present, no `REVIEW_PASS`), AND
every review round reports the product file(s) byte-identical to HEAD — i.e. no round
ever produced a real diff, not merely a defective one. This is a pipeline-state defect
(the implementer session's memory has gone stale), not a spec, plan, or code defect —
the plan itself needs no repair. Repair depth is the plan-ratified rollback (Step 5),
not spec/spec+plan/spec+plan+code.

**Non-convergence (terminal, commit-as-is)** — implement-phase condition holds (PLAN_REVIEW_PASS
present, no REVIEW_PASS) AND every review contains only Low or Informational findings
AND the plan's deliverables are present/produced on disk (for `modify`-type deliverables,
confirm via patches or reviews that the change landed — file existence alone is not
sufficient). When all three hold, the work is likely done; recommend committing instead
of re-running. This is a distinct outcome: no rollback, no artifact cleanup.

Keep the severity inspection here lightweight — blocking/non-blocking only, not a full
issue extraction (that is Step 3's job).

State the diagnosis explicitly before proceeding, in this order: root-cause category
first, then likely repair depth, with the failure phase mentioned last as routing
context only.

---

## Step 3 — Extract root cause

Scan all artifact files for problems and improvement requests. Real artifacts use
inconsistent formats — do not hardcode heading names. Common patterns: `### Issues`,
`## Critical Issues`, `## Suggestions`, `### Task 1:`, inline numbered lists.

Read all rounds, not just the latest. **Recurring issues** (present in 2+ rounds) are
the primary signal — the implementer could not fix them even with a patch, so the
description is the only reliable enforcement. The recurring root cause determines the
repair depth.

Root-cause categories (context for depth + scope-overload flag):

- **Specification gap** — ambiguous or missing constraint / edge case / scope boundary
- **Scope overload** — too many concerns; planner or implementer loses coherence
- **Mechanical error** — recurring execution mistakes independent of the task spec
- **Stale implementer session** — every review round found the product file(s)
  byte-identical to HEAD; the plan was ratified but no attempt ever produced a diff for
  it to describe

When a governing spec was read in Step 1, judge the recurring findings against it: a
candidate "specification gap" may actually be a violation of an already-ratified
contract that the spec note failed to restate — the root cause and the repair target
differ (amend the spec note to carry the governing constraint vs. invent a new
decision). The Diagnosis Report must state whether the failure violates the governing
spec and quote the relevant clause.

Identify the dominant root cause and whether any issue is recurring. Carry both into
Step 4 — they drive the depth choice and the scope-overload flag.

**Write the Diagnosis Report.** Before presenting the Step 4 depth menu, print a
mandatory Diagnosis Report to the user — a first-class deliverable, produced without
the user asking for it.

Form: a chronological narrative in plain prose. Tell the story of the implementation
attempt as a sequence of events — what the implementation did, what defect the review
found, what the fix changed, and what new defect that fix introduced — round by round,
in complete sentences. One short paragraph per review round is the natural shape; a
single-round failure may be a single paragraph. Length scales with the number of
rounds — never compress a multi-round chain to fit a sentence budget. Weave reviewer
findings from the recurring rounds (2+) into the narrative as quotes or paraphrases, as
evidence. This narrative register is shared with `milestone-rescue-audit`'s output —
change it in both files or neither.

No tables, no fragment-style bullet lists inside the Diagnosis Report — the causal
story is read top to bottom, not reconstructed from a grid.

For a stale-implementer-session classification, the narrative has no defect chain to
tell: state plainly that the plan was ratified, that every round left the product
file(s) unchanged from HEAD, and that the gap is in the pipeline's record of the
attempt rather than in the spec, plan, or code.

Domain language only: describe what the spec note / contract line stated wrongly or
left ambiguous, and how the plan or code went wrong as a consequence. Zero orchestrator
vocabulary — no iteration counts, no PASS markers, no phase names, no sidecar.

End with a standalone root-cause sentence, visually set off (e.g. a block quote): one
sentence stating the missing or wrong constraint in the spec/contract, phrased so that,
had it been present, the failure chain would not have occurred.

Attach the root-cause category (specification gap / scope overload / mechanical error /
stale implementer session) and the recurring-issue signal to the report as a
classification, not as a substitute for the narrative — they carry into Step 4 to drive
the depth choice.

---

## Step 4 — Choose repair depth

**Determine `$TARGET_FILE`:**
- If argument names a file → use `.ai-factory/<that file>`
- If the milestone slug or artifacts suggest test tasks (keywords: test, tests, spec) → `$TARGET_FILE = .ai-factory/ROADMAP_TESTS.md`
- Otherwise → `$TARGET_FILE = .ai-factory/ROADMAP.md`

Read `$TARGET_FILE` and locate the milestone line matching the slug identified in Step 1.

**When classification is non-convergence** — present via `AskUserQuestion`:

```
The deliverable is complete and correct; remaining findings are cosmetic:
<one-line summary of what they are>.

Deliverables are present on disk and every review round raised only Low/Informational
nits — the pipeline never emitted REVIEW_PASS because the reviewer kept generating
those nits, not because of a real defect.

Recommended: commit the deliverable — another run would likely loop again.

Options:
1. Commit the deliverable (after any remaining trivial nits)
2. Re-run the pipeline anyway
3. Fold recurring spec-traceable nits into the spec note before committing
```

Option 3: scan findings for nits that reference a gap in the spec note the `Spec:` tag
points at, propose the minimal clause addition, apply it, then
proceed as option 1. Proceed to Step 5 with the user's choice for all three options.

---

**For real defects (plan-phase or implement-phase failure, or a stale implementer session):**

**Scope-overload flag:** if the dominant root cause is scope overload — the task has
too many unrelated concerns or is fundamentally mis-framed — do NOT decompose here.
Flag this to the user and point to `/roadmap-decompose`. The user decides whether to
remove/replace or rewrite. Skip the depth menu in this case.

**Stale-implementer-session flag:** if Step 2 classified the failure as a stale
implementer session (plan ratified, implementation absent), do not present the standard
three depths (spec / spec+plan / spec+plan+code) — the plan needs no repair, so none of
them apply. Present only option 4 below as the recommended rollback; the user's
explicit "fix Y / delete X" still overrides.

Otherwise, present the repair depth via `AskUserQuestion`. Each option states what gets
repaired and what the rollback state is. The user's explicit "fix Y / delete X" overrides
this menu.

```
Root cause: <spec-gap | mechanical-error | scope-overload | stale-implementer-session>
Dominant recurring issue: <one line>

Choose repair depth:

1. spec — repair spec note + contract line in $TARGET_FILE
   Rollback: plan, plan-reviews, reviews, patches, and sidecar deleted; orchestrator re-plans

2. spec + plan — repair spec + plan .md (keeping passing plan-reviews intact if wanted)
   Rollback: plan-reviews, reviews, patches deleted; sidecar step → "planned"

3. spec + plan + code — repair spec + plan + code by hand in the working tree
   Rollback: reviews, patches deleted; sidecar step → "implemented"

4. plan ratified, implementation absent — keep the plan and its passing plan-review(s);
   the implementer session never produced a diff
   Rollback: reviews, patches deleted; sidecar step → "plan_reviewed"; `implementer`
   session dropped; orchestrator resumes at implement, iteration 1, with a fresh session
```

Offer option 4 only when a passing plan-review is on disk for this slug — the plan was
ratified but the product diff is empty (see the diagnosis signal in Step 2–3). After the
user confirms, proceed to Step 5 with the chosen depth.

---

## Step 5 — Apply repair and roll back artifacts

Execute the repair and artifact cleanup for the depth chosen in Step 4. Use
`git status --short -- .ai-factory/` to identify uncommitted files, then delete
using git-native commands only:

- Files marked `??` (untracked) → `git clean -f -- <path>`
- Files marked `A ` (staged/added) → `git rm -f -- <path>`

Never delete committed files. Never touch the spec file (wherever its `Spec:` tag
points) except the deliberate spec-note repair below. Never delete files belonging to
other milestone slugs.

---

**Non-convergence (terminal — no rollback):** the user chose to commit or re-run in Step 4
(options 1, 2, or 3). Leave all artifacts in place — plans, plan-reviews, reviews,
patches, and sidecar all describe completed, correct work. Do NOT delete any artifact.
Do NOT touch the sidecar. Proceed directly to Step 5.5.

---

**Depth: spec** — repair spec note + contract line; full reset.

1. Edit the spec note (the file the contract line's `Spec:` tag points at) to address
   the root cause. If a governing spec was read in Step 1, do not copy its content into the spec note
   wholesale — quote/restate only the clauses implicated by the findings.
2. Edit the contract line in `$TARGET_FILE` to match (keep it concise;
   each constraint is one semicolon-separated clause matching surrounding style).
3. Delete: plan `.md`, all plan-review files, all review files, all patch files for
   this slug — nothing of the discarded attempt should remain.
4. Delete the `.json` sidecar (tracked/staged → `git rm -f`; untracked → `git clean -f`).
   The loss of `planner`, `implementer`, and `elapsed` is intentional.

Emit: `Sidecar deleted (full reset).`

---

**Depth: spec + plan** — repair spec + plan; roll back to `"planned"`.

1. If the requirement itself was implicated, edit the spec note + contract line in
   `$TARGET_FILE` (same as spec depth above). If the spec is already correct, this
   step is a no-op — repair only the plan below.
2. Edit the plan `.md` to fold in the root-cause fix.
3. Delete: all plan-review files, all review files, all patch files for this slug.
   Keep the plan `.md` and sidecar.
4. Locate the sidecar at `.ai-factory/plans/{seq}-{slug}.json`. Read it if present;
   start from `{}` if absent. Set the `step` key to `"planned"` and **delete** the
   `implementer` key — it names the session whose implementation was just discarded, so
   its memory no longer describes anything on disk. Preserve every other key —
   `planner`, `elapsed`, and any others — untouched. Write back as JSON with 2-space
   indentation.

Emit: `Sidecar updated: step set to "planned"; implementer session dropped.`

---

**Depth: spec + plan + code** — repair spec + plan + code; roll back to `"implemented"`.

1. If the requirement itself was implicated, edit the spec note + contract line in
   `$TARGET_FILE`. If the spec is already correct, this step is a no-op — repair only
   the plan/code below.
2. Edit the plan `.md` if needed (keep passing plan-reviews intact).
3. Apply the hand-fix directly in the working tree (the diff IS the repair).
4. Delete: all review files, all patch files for this slug. Keep the plan `.md`,
   passing plan-review files, hand-fixed diff, and sidecar.
5. Update the sidecar `step` to `"implemented"` — same read/update/write procedure
   as the spec+plan depth above.

Emit: `Sidecar updated: step set to "implemented".`

---

**Depth: plan ratified, implementation absent** — the plan and its passing
plan-review(s) stand; only the (missing) implementation is discarded; roll back to
`"plan_reviewed"`.

1. Keep the plan `.md` and every plan-review file for this slug untouched — the plan
   was ratified and needs no repair.
2. Delete: all review files and all patch files for this slug — there is no
   implementation for them to describe.
3. Locate the sidecar at `.ai-factory/plans/{seq}-{slug}.json`. Read it if present;
   start from `{}` if absent. Set the `step` key to `"plan_reviewed"` and **delete** the
   `implementer` key — the session it names never produced the implementation, so its
   memory would only mislead the next implement attempt. Preserve every other key —
   `planner`, `elapsed`, and any others — untouched. Write back as JSON with 2-space
   indentation.
4. Validation contract: only write `"plan_reviewed"` when a plan-review file ending
   with `PLAN_REVIEW_PASS` is present on disk for this slug — never write it otherwise.

Emit: `Sidecar updated: step set to "plan_reviewed"; implementer session dropped.`

---

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

**Silent failure mode:** the orchestrator clears any `step` value whose required artifact is missing and falls through to the disk heuristic — writing a wrong value silently loses the resume point.
**Test mode:** `review_failed:N` is replaced by `test_run_failed:N` (artifact: `test-runs/{seq}-{slug}-test-N.txt`).
**Always-valid guard:** `"planned"` and `"implemented"` carry no artifact reference and always validate — write `"planned"` only when the plan `.md` is present; write `"implemented"` only when the plan `.md` is present and a non-empty working diff exists. Never write `"planned"` after deleting the plan `.md`.

Note: `"plan_reviewed"` **is** written by this skill — exactly by the plan-ratified
rollback (Step 5), and only when a plan-review file ending with `PLAN_REVIEW_PASS` is
present on disk for the slug. Otherwise the flow writes only `"planned"` (spec+plan
depth), `"implemented"` (spec+plan+code depth), or deletes the sidecar (spec depth).
`"plan_review_failed:N"` and `"review_failed:N"` remain not written — reference-only
values from the orchestrator contract.

Restate the Diagnosis Report's conclusion in one paragraph — what was wrong, what was
repaired, and at which depth — before the file bookkeeping below.

Show the user the list of deleted files and confirm the rescue is complete.

---

## Step 5.5 — Propagate findings to open milestones

For a non-convergence classification, propagation is a no-op — every round was
non-blocking, so there are no real defects to propagate. Do not surface cosmetic nits
to unrelated milestones.

After completing the repair (if any), scan the remaining `- [ ]` milestones in
`$TARGET_FILE` for the same gaps.

**Which issues to propagate** (priority order): recurring issues first (appeared in 2+
rounds — propagate to any open milestone touching the same files, APIs, or patterns);
then mechanical errors (same pattern type); then specification gaps (same domain only).

**How to identify matches:** same file paths or module names; same API, class, method,
or operator family; same structural pattern (e.g. "bridge", "repository", "hook").

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

If no matches found, or all issues are domain-specific to the failed milestone, skip silently.

---

## Step 5.6 — Pin disposed observations

When deferred-observation entries encountered in the artifacts read this session are
routed into roadmap tasks — a new task + spec written (e.g. via `/roadmap-decompose`
in the same chat) or folded into a spec repaired at Step 5 — append
`[promoted → <spec path>]` to the entry and to every sibling occurrence across that
milestone's review files, per the engine's dedup rule (`orchestrator-artifacts` §6;
do not redefine the grammar, the pinned definition, or the dedup rule). Scope the pin
to review files still present on disk at pin time — Step 5 may already have deleted
the rescued slug's review files (spec / spec+plan depth delete both genres;
spec+plan+code and plan-ratified depth delete reviews, keep plan-reviews), and a
deleted file has nothing to pin and nothing left for `roadmap-prune`'s gate to flag.
Pin at the moment the task/spec lands, not at session end. Entries not disposed
in-session stay unmarked, left for `milestone-rescue-audit` prune mode.

---

## What NOT to do

- Do not keep stale artifacts at the chosen rollback depth — they describe a failed
  attempt and will confuse the next planner or implementer
- Do not add implementation details to the milestone or spec note — keep constraints
  at the *what* level, not the *how* level
- Do not delete committed files or files belonging to other milestone slugs
- Do not skip reading earlier rounds — the pattern of failures across rounds is the
  primary signal, not just the final round
- Do not issue a semantic diagnosis, blocker, or spec repair without having read the
  phase's `Governing spec:` documents when the phase names them — otherwise the
  ratified spec tier does not participate in the rescue at all. This read is
  unconditional whenever the phase names a governing spec, never suspicion-gated.
- Do not overwrite `planner` or `elapsed` in the sidecar — these persist untouched at
  every depth. `implementer` is the one exception: delete it whenever the repair
  discards the implementation the session produced (spec+plan depth, and the
  plan-ratified rollback depth), since the key would otherwise name a session whose
  memory describes a discarded attempt. Do not keep `implementer` around "for the
  elapsed stats" — those stats live in `elapsed`, which is retained regardless. On a
  full reset (spec depth) the sidecar is deleted entirely alongside the plan
- Do not write `"planned"` or `"implemented"` when the corresponding artifact is
  absent — both are always-valid states the orchestrator accepts without artifact
  checks, so writing one after deleting the plan `.md` (or before any working diff
  exists) silently sends the orchestrator into the wrong phase
- Never present orchestrator mechanics — iteration limits, missing PASS markers, phase
  names, sidecar states — as "the problem". They are how the failure surfaced, not what
  failed. This constrains your *output and reporting*, not your analysis: pipeline
  signals are still read internally to route the repair depth
- Do not write `[audit-corroborated]`, `[audit-dismissed]`, or `[unrouted-reported]` —
  and do not dismiss an observation by marker. Rescue's only marker is
  `[promoted → <path>]`, written only for observations actually routed into a task or
  spec this session; evaluating, dismissing, and sweeping stay
  `milestone-rescue-audit`'s
