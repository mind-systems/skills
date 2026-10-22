---
name: task-rescue
description: >-
  Reads failed orchestrator artifacts (plans, plan-reviews, code reviews),
  diagnoses how deep the root cause reaches and repairs to that depth, then rolls
  the task's state back so the orchestrator re-validates from there. Also checks
  downstream tasks for the same gaps. Use when the pipeline stops with "PLAN_REVIEW_PASS never achieved" or
  "REVIEW_PASS never achieved" — trigger phrases: "rescue", "milestone failed",
  "pipeline stopped".
argument-hint: "[path/to/ROADMAP.md | ROADMAP_TESTS.md]"
allowed-tools: Read Write Edit Glob Grep Bash(git *) Bash(mkdir *) AskUserQuestion Skill
loads: orchestrator-artifacts roadmap-engine note
disable-model-invocation: false
---

# Task Rescue

The orchestrator exhausting its iteration limit and stopping is the tripwire — how the
failure was noticed, not what failed. The subject of this skill is the defect in the
task's specification (task spec + contract line) and its implementation: it reads the
artifacts left uncommitted on disk, diagnoses how deep that defect reaches
(specification gap? bad plan? broken implementation?), and repairs to exactly that
depth — then rolls the sidecar and the artifact set back to the matching repaired state
so the orchestrator re-validates from there rather than starting blind.

The roadmap contract line (in `$TARGET_FILE`) is the roadmap half of the two-tier spec
pair (alongside the task spec the task's `Spec:` tag names) and is edited when the
spec tier is repaired. The repair is depth-keyed, not a single ROADMAP edit: task spec +
contract line, plan `.md`, or working-tree code, depending on how deep the root cause
runs. The user picks the depth; an explicit "fix Y / delete X" overrides.

Ensure `orchestrator-artifacts` is loaded once this chat (via the Skill tool, only if
not already loaded) — it defines the artifact layout, naming, signals, sidecar
fields, and marker grammar referenced below.

Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not
already loaded) — it defines the named-roadmap resolution referenced below.

---

## Step 1 — Discover artifacts

Run `git status --short -- .ai-factory/` to find all uncommitted files under `.ai-factory/`.

Filter results to the artifact directories (`plans/`, `plan-reviews/`, `reviews/`) —
layout and naming conventions are described in `orchestrator-artifacts`.

Ignore any uncommitted files outside these directories — the task spec itself
lives wherever the task's `Spec:` tag points, not in a fixed directory.

If no uncommitted files are found in any of the artifact directories, stop and tell
the user: there is nothing to rescue.

**Identify the task slug.** Extract the `<seq>-<slug>` shared by the artifact
filenames (see `orchestrator-artifacts` for the naming convention). If files from
multiple slugs are present, ask the user which task to rescue before proceeding.

**Read the phase's governing spec and phase note.** Determine `$TARGET_FILE` (the same
resolution Step 4 determines), read it, and locate the phase section the
task belongs to. Check the phase header and its intro lines for `Governing spec:`
documents or a `Phase note:`. If present, read every named document in full before
proceeding to Step 2 — this is unconditional, not suspicion-based. If the task is
under no phase, or neither pointer is named, proceed as today. This read is
additive to Step 4's own `$TARGET_FILE` resolution and contract-line locate — it does
not replace it. A named file that does not exist is told to the user here, and
carried into Step 3's Diagnosis Report as a finding — never skipped silently.

**Capture the report facts.** Record these facts now, at discovery, before anything is
deleted, and hold them for the report Step 5.7 writes — Step 5 deletes or rewrites the
sidecar at some repair depths and a re-run overwrites its keys, so `step`, `elapsed` and
the session ids are unrecoverable once that happens.

- **Project** — the last path segment of `git rev-parse --show-toplevel` run in the
  project being rescued. This fact fills the report's `**Project:**` line only; it is
  not the destination path, which Step 5.7 resolves for itself at write time.
- **Date** — today's date, ISO form (`YYYY-MM-DD`).
- **`step` and `elapsed`** — read from the task's sidecar, per `orchestrator-artifacts`
  § 3.
- **The session ids** — every session id the sidecar holds, each under its key as the
  sidecar spells it. They are the sessions whose artifacts this rescue reads, and the
  report names them so that one can be resumed and asked to quote what it saw. The
  sidecar is the live state of the attempt and is overwritten; the report is the record
  of this attempt and its diagnosis.
- **Where the sidecar lives** — located per `orchestrator-artifacts` § 1: the flat
  `plans/<seq>-<slug>.json` layout holds for the default `ROADMAP.md`/`ROADMAP_TESTS.md`
  pair only, while a named roadmap's sidecar sits under a subdirectory keyed by its
  roadmap file stem (`roadmaps/john-doe.md` → `plans/john-doe/<seq>-<slug>.json`).
  `$TARGET_FILE` is already resolved above, so the stem is known here. This is pinned
  because a sidecar missed by reading the wrong path records exactly the same thing as
  an absent one — everything it holds lost, with no signal.
- **No sidecar on disk** → record `step`, `elapsed` and the session ids as **absent**;
  never guess, never reconstruct a number from anything else. Step 5.7 renders absence
  as absence.

**Read every artifact file found** — all rounds, not just the latest. The pattern of
failures across rounds matters as much as the final round. A plan-review from round 1
reveals what the planner missed first; a review from round 2 shows whether the
implementer addressed it. Read them all before drawing any conclusions.

---

## Step 2 — Diagnose root cause and depth

Determine which phase failed and how deep the root cause runs. This classification is
an **internal routing signal** for Step 4's depth choice, not itself the diagnosis the
user receives — that's Step 3's Diagnosis Report. Signal semantics (`PLAN_REVIEW_PASS`,
`REVIEW_PASS`, last-line requirement) are defined in `orchestrator-artifacts`; the
classification below only applies them.

**Escalated (terminal, human decision pending)** — the sidecar's `step` reads
`"escalated"`, OR (sidecar absent/stale) the plan file or the most recent
plan-review/review file ends with the exact line `ESCALATION`. Not a specification,
plan, or code defect; [role] stopped because its output could not be produced
honestly without a decision outside its authority. Repair depth does not apply in the
usual sense — see Step 4's own escalation branch. Check this condition first, ahead
of every classification below — an escalating planner/implementer writes `ESCALATION`
into the plan file itself with no plan-review file on disk, which otherwise matches
Plan-phase failure's condition verbatim.

**Plan-phase failure** — no plan-review file contains `PLAN_REVIEW_PASS` on its own
line. Root cause is likely a specification gap or scope overload; repair depth starts
at spec.

**Implement-phase failure** — at least one plan-review file contains `PLAN_REVIEW_PASS`,
but no review file contains `REVIEW_PASS`. Root cause is a defect in the code or plan;
repair depth is at least spec+plan.

**Stale implementer session (plan ratified, implementation absent)** — the implement-phase
condition holds, AND every review round reports the product file(s) byte-identical to
HEAD — no round ever produced a real diff, not merely a defective one. This is a
pipeline-state defect (the implementer session's memory has gone stale), not a spec,
plan, or code defect — the plan itself needs no repair. Repair depth is Step 4's
plan-ratified option, rolling back to `plan_reviewed` (Step 5), not
spec/spec+plan/spec+plan+code.

**Non-convergence (terminal, commit-as-is)** — the implement-phase condition holds AND
every review contains only Low or Informational findings AND the plan's deliverables
are present/produced on disk (for `modify`-type deliverables, confirm via reviews
that the change landed — file existence alone is not sufficient). When all
three hold, the work is likely done; recommend committing instead of re-running. No
rollback, no artifact cleanup.

Keep this severity pass lightweight — blocking/non-blocking only; full issue extraction
is Step 3's job. State the diagnosis explicitly before proceeding, in this order:
root-cause category, then likely repair depth, with the failure phase mentioned last as
routing context only.

---

## Step 3 — Extract root cause

Scan all artifact files for problems and improvement requests. Formats are
inconsistent — `### Issues`, `## Critical Issues`, `## Suggestions`, `### Task 1:`,
inline numbered lists — so don't hardcode heading names.

Read all rounds (Step 1's mandate). **Recurring issues** (present in 2+ rounds) are
the primary signal — the implementer could not fix them across rounds, so the
description is the only reliable enforcement, and they determine the repair depth.

Root-cause categories (context for depth + scope-overload flag):

- **Specification gap** — ambiguous or missing constraint / edge case / scope boundary
- **Scope overload** — too many concerns; planner or implementer loses coherence
- **Mechanical error** — recurring execution mistakes independent of the task spec
- **Stale implementer session** — every review round found the product file(s)
  byte-identical to HEAD; the plan was ratified but no attempt ever produced a diff for
  it to describe

Escalation is not in this list — it carries no root cause; see its own short-form
branch below and skip the "Attach the root-cause category" step for it.

When a governing spec or phase note was read in Step 1, judge the recurring findings
against them: a candidate "specification gap" may actually be a violation of an
already-ratified contract that the task spec failed to restate — the root cause and
the repair target differ (amend the task spec to carry the governing constraint vs.
invent a new decision). The phase note stands beside the governing spec as a second
baseline a finding is judged against: the governing spec states how the phase must
become, the note what diverges now. Where a governing spec was read, the Diagnosis
Report must state whether the failure violates it and quote the relevant clause;
where a finding instead matches a divergence the phase note already records, the
report says so and names it as already-recorded divergence. Such a finding is not by
itself a "specification gap" — the divergence is known and ratified at the phase
tier — so it does not on its own drive Step 4's depth choice toward inventing a new
decision; the repair target is the task spec failing to carry what the note already
stated, mirroring the root-cause/repair-target distinction above.

Identify the dominant root cause and whether any issue is recurring — both carry into
Step 4, driving the depth choice and the scope-overload flag.

**Write the Diagnosis Report** — a mandatory, first-class deliverable printed before the
Step 4 depth menu, without the user asking for it.

Form: a chronological narrative in plain prose. Tell the story of the implementation
attempt as a sequence of events — what the implementation did, what defect the review
found, what the fix changed, and what new defect that fix introduced — round by round,
in complete sentences. One short paragraph per review round is the natural shape; a
single-round failure may be a single paragraph. Length scales with the number of
rounds — never compress a multi-round chain to fit a sentence budget. Weave reviewer
findings from the recurring rounds (2+) into the narrative as quotes or paraphrases, as
evidence.

No tables, no fragment-style bullet lists inside the Diagnosis Report — the causal
story is read top to bottom, not reconstructed from a grid.

For a stale-implementer-session classification, the narrative has no defect chain to
tell: state plainly that the plan was ratified, that every round left the product
file(s) unchanged from HEAD, and that the gap is in the pipeline's record of the
attempt rather than in the spec, plan, or code.

For an escalation classification, the narrative has no defect chain to tell either:
state plainly that [role] stopped on a decision outside its authority, then restate —
verbatim or lightly paraphrased — the missing decision and its options from the
artifact's `## Escalation` section. End with that decision restated as a block
quote, in place of the root-cause sentence — there is no root cause here, only a
decision still to make.

Describe what the task spec / contract line stated wrongly or left ambiguous, and how
the plan or code went wrong as a consequence. The narrative may name a round and the
reviewer whose finding it tells.

End with a standalone root-cause sentence, visually set off (e.g. a block quote): one
sentence stating the missing or wrong constraint in the spec/contract, phrased so that,
had it been present, the failure chain would not have occurred.

Attach the root-cause category (specification gap / scope overload / mechanical error /
stale implementer session — not applicable to an escalation classification, which has
none) and the recurring-issue signal to the report as a classification, not as a
substitute for the narrative — they carry into Step 4 to drive the depth choice.

**Write the durable report.** Step 3 ends with the first write of the durable report.
The write is made per § "Step 5.7 — Write the durable report", through `note`, with the
destination, the three hooks and the topic slug that section gives. Keep the path `note`
returns: every later section of the durable report is appended to that file.

---

## Step 4 — Choose repair depth

**Determine `$TARGET_FILE`** per `roadmap-engine`'s named-roadmap resolution order:
explicit argument wins, then "my roadmap", then the default `.ai-factory/ROADMAP.md`
— see the engine's "Named roadmaps" section for the slug/owner mechanics.
- If argument names a file → use `.ai-factory/<that file>`
- If the task slug or artifacts suggest test tasks (keywords: test, tests, spec)
  → the test sibling of the roadmap in play: a named roadmap resolves to
  `.ai-factory/roadmaps/<user-slug>-tests.md`, the default to
  `.ai-factory/ROADMAP_TESTS.md` as today
- Otherwise → `$TARGET_FILE` = the roadmap in play (per the resolution order above)

Read `$TARGET_FILE` and locate the contract line matching the slug identified in Step 1.

**When classification is Escalated** — skip the standard four-depth menu entirely;
nothing is broken to repair at plan or code level. Present the missing decision
surfaced in Step 3, then present via `AskUserQuestion`:

```
This task escalated — <one-line restatement of the missing decision>.

Escalation is not a defect at any repair depth; it stops here because a decision
outside any agent's authority is required before this task can proceed.

Options:
1. Decision recorded in this task's spec — reset and re-plan
   Apply the resolved decision to this task's spec + contract line (the normal
   spec repair), then perform the full reset — this clears
   step:"escalated" and the escalation field for free, and the orchestrator
   re-plans clean.
2. Decision belongs elsewhere (a neighboring task / the governing spec) —
   point there and reset
   Do not edit this task's spec. Report where the decision belongs (the same
   flag-and-point pattern already used for scope overload). Still perform the
   full reset on THIS escalated task's transient state, so it
   re-plans fresh once the owning artifact is resolved.
3. Not resolved yet — report only, leave the escalated state
   No reset. The escalated sidecar stays exactly as the orchestrator left it;
   the user re-runs this rescue after the decision is made.
```

Each option runs a rollback state of Step 5 — no new rollback state, no fifth
depth-menu entry: option 1 repairs the task spec and contract line with the decision,
then runs the full reset; option 2 runs the full reset with the spec and contract line
untouched; option 3 changes no state. Proceed to Step 5.

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
3. Fold recurring spec-traceable nits into the task spec before committing
```

Option 3: scan findings for nits that reference a gap in the task spec the `Spec:` tag
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

Otherwise, present the repair depth via `AskUserQuestion` — each option states what gets
repaired and the rollback state; the user's explicit "fix Y / delete X" overrides this
menu.

```
Root cause: <spec-gap | mechanical-error | scope-overload | stale-implementer-session>
Dominant recurring issue: <one line>

Choose repair depth:

1. spec — repair task spec + contract line in $TARGET_FILE
   Rollback: full reset

2. spec + plan — repair spec + plan .md
   Rollback: planned:1

3. spec + plan + code — repair spec + plan + code by hand in the working tree
   Rollback: implemented:1

4. plan ratified, implementation absent — keep the plan and its passing plan-review(s);
   the implementer session never produced a diff
   Rollback: plan_reviewed
```

Offer option 4 only when a passing plan-review is on disk for this slug — the plan was
ratified but the product diff is empty (see the diagnosis signal in Step 2–3). After the
user confirms, proceed to Step 5 with the chosen depth.

---

## Step 5 — Apply repair and roll back artifacts

Step 5 applies the repair Step 4's choice names, then rolls the task back to the state
that choice names.

**Deleting files.** Use `git status --short -- .ai-factory/` to identify uncommitted
files, then delete using git-native commands only:

- Files marked `??` (untracked) → `git clean -f -- <path>`
- Files marked `A ` (staged/added) → `git rm -f -- <path>`

Never delete committed files. Never delete files belonging to other task slugs.

**Writing the sidecar.** Locate the sidecar by the roadmap's stem, as
`orchestrator-artifacts` § "1. Layout" lays it out, `<stem>` being the stem of
`$TARGET_FILE`. Read it if present; start from `{}` if absent. Set `step`. Leave
`planner`, `elapsed` and every key the state does not name as they are. Drop
`escalation` wherever the sidecar is rewritten. Write it back as JSON with two-space
indentation.

**Rollback states.** Every deletion is for this slug.

- **Full reset.** The plan `.md`, every plan-review, every review and the sidecar are
  deleted — nothing of the attempt remains. Requires nothing.
- **`planned:1`.** The plan stays. Every plan-review and every review is deleted.
  `step` is `"planned:1"` and `implementer` is dropped. Requires the plan `.md` on disk.
- **`implemented:1`.** The plan, the passing plan-reviews and the working-tree diff
  stay. Every review is deleted. `step` is `"implemented:1"` and `implementer` stays.
  Requires the plan on disk and a non-empty working diff.
- **`plan_reviewed`.** The plan and every plan-review stay. Every review is deleted.
  `step` is `"plan_reviewed"` and `implementer` is dropped. Requires a plan-review
  ending with `PLAN_REVIEW_PASS` on disk for the slug.

---

**Non-convergence:** no state changes for any of the three options. Every artifact and
the sidecar stay as they are. Proceed directly to Step 5.5.

---

**Escalated — option 1 (decision recorded here):** repair the task spec and contract
line with the decision, then run the full reset.

---

**Escalated — option 2 (decision belongs elsewhere):** run the full reset with the
task spec and contract line untouched — the decision belongs elsewhere, not here.

---

**Escalated — option 3 (not resolved yet):** no state changes. Every artifact stays as
the orchestrator left it. Proceed directly to Step 5.5.

---

### Valid sidecar `step` states

This is a **closed set** — Step 5 picks one of the six values below, never invents
one. This table mirrors the orchestrator's accepted set of sidecar `step` values — if
it changes, update this table; do not let them diverge.
The artifact paths here and in the test-mode line below are the default pair's flat
layout; for a named roadmap they gain its `<stem>/` segment, per `orchestrator-artifacts`
§ 1, the way Step 1 locates the sidecar.

| `step` value | Resumes at | Required on disk to validate |
|---|---|---|
| `"planned:N"` | plan-review, attempt N | none — always valid |
| `"plan_review_failed:N"` | plan, attempt N+1 | `plan-reviews/{seq}-{slug}-plan-review-N.md` |
| `"plan_reviewed"` | implement, iter 1 | a plan-review file ending with `PLAN_REVIEW_PASS` |
| `"implemented:N"` | review, iter N | none — always valid |
| `"review_failed:N"` | implement, iter N+1 | `reviews/{seq}-{slug}-review-N.md` |
| `"escalated"` | re-halts immediately, no retry (until cleared) | none — always valid |

**Silent failure mode:** the orchestrator clears any `step` value whose required artifact is missing and falls through to the disk heuristic — writing a wrong value silently loses the resume point.
**Test mode:** `review_failed:N` is replaced by `test_run_failed:N` (artifact: `test-runs/{seq}-{slug}-test-N.txt`).

---

## Step 5.5 — Propagate findings to open tasks

For a non-convergence classification, propagation is a no-op — every round was
non-blocking, so there are no real defects to propagate. Do not surface cosmetic nits
to unrelated tasks.

After completing the repair (if any), scan the remaining `- [ ]` tasks in
`$TARGET_FILE` for the same gaps.

**Which issues to propagate** (priority order): recurring issues first (appeared in 2+
rounds — propagate to any open task touching the same files, APIs, or patterns);
then mechanical errors (same pattern type); then specification gaps (same domain only).

**How to identify matches:** same file paths or module names; same API, class, method,
or operator family; same structural pattern (e.g. "bridge", "repository", "hook").

**If matches found**, present a single question:

```
These open tasks may have the same gaps. Apply the same fix?

→ TaskA: + <proposed clause>
→ TaskB: + <proposed clause>

Options:
1. Apply all
2. Review each individually
3. Skip
```

If no matches found, or all issues are domain-specific to the failed task, skip silently.

---

## Step 5.6 — Pin disposed observations

A rescue pins each deferred-observation entry it disposes of this session at the moment
it disposes of it, together with every sibling occurrence across that task's review
files. The pin follows the grammar and dedup rule of `orchestrator-artifacts`
§ "6. Status-marker grammar" — by that pointer, never redefined here.

Scope the pin to review files still present on disk at pin time — Step 5 may already
have deleted the rescued slug's review files, and a deleted file has nothing to pin
and nothing left for `roadmap-prune`'s gate to flag. Pin at the moment of the judgment
— routing or dismissal — not at session end.

Rescue disposes only of what it evaluates this session — it does not corroborate a
finding against a root-cause chain or sweep every unrouted entry across the review
corpus. Entries rescue does not evaluate or dispose of this session stay unmarked,
left for the resolution session (`orchestrator-artifacts` §6) to pin later.

---

## Step 5.7 — Write the durable report

The durable report is written through `note` (loaded via `loads: note` above), so a
failed attempt leaves a record even after Step 5 deletes the artifacts it was drawn
from. The first write happens at the end of Step 3; this section defines it.

**Extending the file.** The file is extended while the rescue is hot. Each addition is
a section headed by its date (`## <YYYY-MM-DD>`) and appended directly to the path the
first write returned, with Edit/Write and not through `note`. The lines already in the
file stay as written. The first appended section is made here, once the repair is done:
it records what the repair did — the depth chosen, the escalation option taken, or the
non-convergence choice made — and what was deleted or kept. When the first write
returned no path, because it failed per "When the write cannot happen", nothing is
appended and Write creates no file.

**Destination, both halves resolved at write time.** The report's destination is
`<skills repo root>/.ai-factory/rescue-reports/<project>/`, built from two commands
run at the moment of the first write, at the end of Step 3, not carried from any
earlier step:

- `git -C ~/.claude/skills/task-rescue rev-parse --show-toplevel` gives the skills
  repo root — inside the existing `Bash(git *)` grant; `~/.claude/skills` is the
  personal-scope symlink every session already relies on to load any skill.
- `git rev-parse --show-toplevel` run in the project being rescued gives, in its last
  path segment, `<project>`.

Neither half is stored nor cached — both are re-resolved at the first write regardless
of anything computed earlier. The Step 1 project fact is not this address: it fills the
report's `**Project:**` line only, and the destination path is resolved fresh at the
first write independently of it.

The destination lies outside the project being rescued, so the skills repo has to be
a writable directory in the session running this rescue — via `--add-dir` or the
project's own settings. This is a one-time setup act per project.

**All three of `note`'s hooks are supplied** (`note`'s own Step "Hooks (caller
inputs)"), named as such:

- *destination directory* — the path resolved above; it drives `note`'s `mkdir -p`,
  its per-directory numbering scan, and the final path.
- *template* — the caller-supplied skeleton below, passed verbatim.
- *verbosity directive* — the diagnosis keeps its own register and length; the report
  is not re-condensed. This replaces `note`'s default Rules 1 and 2 for this run.

Also pass the topic slug `note` takes as `$1`: the task number with dots turned into
hyphens, followed by the same short phrase used in the report's title line (e.g.
`30-1-<phrase>`), matching the files already in the folder. `note`'s own mechanics —
numbering, `mkdir -p`, folder style — are not restated here; they are reached through
these hooks.

**The template**, given literally below, in the shape the folder already holds:

```markdown
# <task number> — <short phrase naming what stopped the run>

**Project:** <the Step 1 project fact, or "absent">
**Date:** <the Step 1 date fact, ISO form>
**Stopped at:** <the Step 1 `step` fact, or "absent"> — <what stopped the run: the review cycle spent at its round R, or the role that escalated>
**Elapsed before the rescue:** <the Step 1 `elapsed` fact, or "absent">
**Sessions:** <every session id the Step 1 capture holds, each as `<key>: <id>`, or "absent">

<the diagnosis, exactly as Step 3 wrote it>

## Who found what

**Root cause found by:** <who>, <when>

- <the finding> — <who>, <when>
```

The diagnosis keeps its prose form; the finders live only in this section, outside it.
*Who* is one of: the user; head N, by its number; the editor; the plan-reviewer or the
reviewer at round R; the implementer or the planner; the rescue itself. *When* is one
of: before the run; in the run; in the rescue; after the rescue, for a defect in the
repair itself. The role and round come from the sidecar's session keys (per
`orchestrator-artifacts` § "3. Sidecar fields") and from the number each plan-review and
review file carries; the user and the heads come from the conversation. A finder that no
artifact and no conversation states is written as "not stated". The section holds one
bullet per finding the diagnosis names.

The title phrase names what stopped the run, never a root-cause claim — a branch
that produces no root cause still needs a title. Where Step 3 produced no
root-cause sentence and no category — the escalation branch, which ends in the
restated decision instead — the report carries **what Step 3 actually emitted**: the
template never demands a part that branch does not produce, and no section is
invented to fill it.

**When the write cannot happen.** Two ways it fails: the skills repo root does not
resolve, or the run has not been given that repository as a writable directory.
Either way, **say so plainly to the user and complete the rescue anyway.** Never
invent a fallback path, never fall back to any directory inside the project being
rescued, never invoke `note` a second time, and never defer the write to a later run.

---

## What NOT to do

- Do not keep stale artifacts at the chosen rollback depth — they describe a failed
  attempt and will confuse the next planner or implementer
- Do not add implementation details to the task or task spec — keep constraints
  at the *what* level, not the *how* level
- Do not delete committed files or files belonging to other task slugs
- Do not skip reading earlier rounds — the pattern of failures across rounds is the
  primary signal, not just the final round
- Do not issue a semantic diagnosis, blocker, or spec repair without having read the
  phase's `Governing spec:` documents or `Phase note:` when the phase names them —
  otherwise the ratified spec tier does not participate in the rescue at all, and
  without the note the rescue never sees what the phase already recorded as
  diverging. This read is unconditional whenever the phase names either pointer,
  never suspicion-gated.
- Do not mark any observation rescue did not actually evaluate this session. Rescue
  pins only what it disposed of this session, in `orchestrator-artifacts` §6's
  current form — an entry it did not evaluate stays unmarked, left for the
  resolution session to pin
- Do not let the Plan-phase/Implement-phase conditions fire before checking for an
  escalation — an escalating planner/implementer writes `ESCALATION` into the plan
  file itself, with no plan-review file at all, which otherwise matches Plan-phase
  failure's condition and reports a defect chain that never existed
- Do not invent a new rollback procedure or a fifth depth-menu entry for
  escalation — options 1 and 2 of the escalation branch reuse the full reset
