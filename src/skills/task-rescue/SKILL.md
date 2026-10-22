---
name: task-rescue
description: >-
  Reads failed orchestrator artifacts (plans, plan-reviews, code reviews) and writes
  its report with the intended repair and rollback. It waits for the user's word, then
  repairs to the depth of the root cause and rolls the task's state back so the
  orchestrator re-validates from there. Also checks open tasks below for the same gap.
  Use when the pipeline stops with "PLAN_REVIEW_PASS never achieved" or
  "REVIEW_PASS never achieved" — trigger phrases: "rescue", "milestone failed",
  "pipeline stopped".
argument-hint: "[path/to/ROADMAP.md | ROADMAP_TESTS.md]"
allowed-tools: Read Write Edit Glob Grep Bash(git *) Bash(mkdir *) AskUserQuestion Skill
loads: orchestrator-artifacts roadmap-engine note
disable-model-invocation: false
---

# Task Rescue

The orchestrator stopping — exhausting its iteration limit, or escalating before its
budget is spent — is the tripwire: how the failure was noticed, not what failed. The
subject of this skill is what the stopped task needs, read from the artifacts it left
uncommitted on disk. It fixes neither the root's kind nor its place: the rescue answers
a few questions about the stalled task, writes its report with the repair and rollback
it intends, and waits for the user's word. The repair then reaches as deep as the root
cause, steered by that word, and the sidecar and the artifact set roll back to the
matching repaired state so the orchestrator re-validates from there rather than
starting blind.

The roadmap contract line (in `$TARGET_FILE`) is the roadmap half of the two-tier spec
pair (alongside the task spec the task's `Spec:` tag names) and is edited when the
spec tier is repaired. A repair may go above the task — putting a phase in front of it,
closing a phase, or deleting the task.

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

**Resolve `$TARGET_FILE` and locate the task.** If an explicit argument names a file,
use `.ai-factory/<that file>`. Otherwise use the roadmap in play, as `roadmap-engine`'s
"Named roadmaps" resolution gives it — the roadmap in play is the one whose contract
line carries the slug. Read it and locate the contract line that matches the slug.

**Read the governing spec and phase note.** The rescue locates the task's phase in
`$TARGET_FILE` and reads in full every document that the phase header or intro names as
`Governing spec:` or `Phase note:`.

**Capture the report facts.** Record these facts now, at discovery, before anything is
deleted, and hold them for the report Step 5.7 writes — Step 5 deletes or rewrites the
sidecar in some rollback states and a re-run overwrites its keys, so `step`, `elapsed` and
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

## Step 2 — What a stop can look like

Signal semantics (`PLAN_REVIEW_PASS`, `REVIEW_PASS`, last-line requirement) are defined
in `orchestrator-artifacts`.

Two facts are not in the artifacts' own words, so they are stated here.

**An escalation is read first.** An escalating agent — the planner, the implementer, or
either reviewer — writes `ESCALATION` on the last line of the artifact it owns. For a
planner or an implementer that artifact is the plan file, possibly with no plan-review
on disk. The sidecar reads `step: escalated`, and the missing decision lies in the
artifact's escalation section. Read this before anything else: otherwise a plan with no
plan-review reads as unfinished planning.

**A resumed implementer can return with no diff.** Every review then reports the product
file(s) identical to HEAD, although the plan was ratified. No spec, plan or code defect
exists; the gap is in the pipeline's record of the attempt.

---

## Step 3 — Ask the stalled task

Scan all artifact files for problems and improvement requests. Formats are
inconsistent — `### Issues`, `## Critical Issues`, `## Suggestions`, `### Task 1:`,
inline numbered lists — so don't hardcode heading names.

**The five questions.** They are put to the stalled task. The rescue answers them by
reading, and none of them routes to a repair:

1. Does the same finding recur, or is it a new one each round while severity falls?
2. Did the spec leave the planner something to decide or enumerate?
3. Is anything the spec says false of the code, or did its own text (a check or a fence)
   cause the findings?
4. Should the task exist as written, and is the system ready for it?
5. Do open tasks below carry the same gap?

**The diagnosis** — a mandatory, first-class deliverable, written without the user
asking for it.

Form: a chronological narrative in plain prose. Tell the story of the attempt as a
sequence of events — what each round did, what its review found, and what the next round
changed — round by round, in complete sentences. One short paragraph per round is the
natural shape; a single-round stop may be a single paragraph. Length scales with the
number of rounds — never compress a multi-round chain to fit a sentence budget. Weave
reviewer findings from every round the narrative tells into it as quotes or paraphrases,
as evidence. The narrative may name a round and the reviewer whose finding it tells.

No tables, no fragment-style bullet lists inside the diagnosis — the causal story is
read top to bottom, not reconstructed from a grid.

**The intended repair.** The rescue decides the repair and the rollback state it
intends. If the stop escalated, the report tells it as a decision for the user, with its
options.

**First write of the report.** Step 3 makes the first write of the durable report. The
write is made per § "Step 5.7 — Write the durable report", through `note`, with the
destination, the three hooks and the topic slug that section gives. Keep the path `note`
returns: every later section of the durable report is appended to that file. This first
write holds the diagnosis, the section on who found what, and the intended repair and
rollback.

**The stop.** The rescue then stops. In the conversation it says where the report lies
and that it waits for the user's word. The diagnosis lives in the report, not in the
chat.

---

## Step 5 — Apply repair and roll back artifacts

On the user's word, Step 5 applies the repair the report intends and rolls the task
back to the state it names, as that word steers them. Applying a clause to an open task
the report names under question five is part of what the word releases.

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

## Step 5.6 — Pin disposed observations

A rescue pins each deferred-observation entry it disposes of this session, together
with every sibling occurrence across that task's review files, when the repair is
applied, on the user's word, and not at the moment of a judgment made before it. The
pin follows the grammar and dedup rule of `orchestrator-artifacts`
§ "6. Status-marker grammar" — by that pointer, never redefined here.

Scope the pin to review files still present on disk at pin time — Step 5 may already
have deleted the rescued slug's review files, and a deleted file has nothing to pin
and nothing left for `roadmap-prune`'s gate to flag.

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
file stay as written. The section appended once the repair is done, on the user's word,
records what the repair did, the rollback state the task was left in, and what was
deleted or kept. When the first write returned no path, because it failed per "When the
write cannot happen", nothing is appended and Write creates no file.

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

## Intended repair

<the repair the rescue intends, and the rollback state it intends — one of Step 5's
four, or that the task's state is left as it is; for an escalation, the decision and
its options; the open tasks below that carry the same gap, each with what it would gain>
```

The diagnosis keeps its prose form; the finders live only in `## Who found what`,
outside it. *Who* is one of: the user; head N, by its number; the editor; the
plan-reviewer or the reviewer at round R; the implementer or the planner; the rescue
itself. *When* is one of: before the run; in the run; in the rescue; after the rescue,
for a defect in the repair itself. The role and round come from the sidecar's session
keys (per `orchestrator-artifacts` § "3. Sidecar fields") and from the number each
plan-review and review file carries; the user and the heads come from the conversation.
A finder that no artifact and no conversation states is written as "not stated".
`## Who found what` holds one bullet per finding the diagnosis names.

The title phrase names what stopped the run, never a root-cause claim.

**When the write cannot happen.** Two ways it fails: the skills repo root does not
resolve, or the run has not been given that repository as a writable directory.
Either way, **say so plainly to the user.** Never invent a fallback path, never fall
back to any directory inside the project being rescued, never invoke `note` a second
time, and never defer the write to a later run.
