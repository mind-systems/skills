# task-rescue writes a durable report of every run it finishes

## Current state (grounded, read fresh)

`src/skills/task-rescue/SKILL.md:162` makes the Diagnosis Report "a mandatory, first-class deliverable printed before the Step 4 depth menu, without the user asking for it" — a chronological narrative, one paragraph per review round, ending in a standalone root-cause sentence. It is printed and nothing writes it anywhere.

Step 5 deletes the artifacts that carry the failure at every depth: plan-reviews and reviews always, the plan and the sidecar at spec depth. `:373` states that the loss of `planner`, `implementer` and `elapsed` is intentional and `:375` emits `Sidecar deleted (full reset).` `orchestrator-artifacts` § 3 names the two fields worth keeping: `step`, the resume point, and `elapsed`, cumulative seconds.

A task can also be redone, dropped or re-decomposed later, by a decision this skill never sees, and its history goes with it. Neither loss is recoverable, so a failure repeated across a month cannot be shown to anyone.

`src/skills/note/SKILL.md:31-33` exposes the three caller hooks this needs: a destination directory, which drives its `mkdir -p`, its `[0-9][0-9]-*.md` numbering scan and the final path; a template the caller passes verbatim; and a verbosity directive that replaces the two default rules. `command-handoff` already drives it exactly this way.

`task-rescue`'s frontmatter grants `Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill` (`:11`) and loads `orchestrator-artifacts roadmap-engine` (`:12`). `git -C ~/.claude/skills/task-rescue rev-parse --show-toplevel` prints the skills repo root and falls inside the existing `Bash(git *)` grant; `~/.claude/skills` is the personal-scope symlink every session already depends on to load any skill at all. `.ai-factory/rescue-reports/` does not exist yet.

## The change

1. The frontmatter `loads:` line gains `note`, keeping the two entries it already has.

2. Step 1, at discovery and before anything is deleted, records four facts and holds them for the report: the project the rescue runs in, named by the last segment of `git rev-parse --show-toplevel` run in that project; today's date; and the sidecar's `step` and `elapsed`. The sidecar is located per `orchestrator-artifacts` § 1, which this skill already loads: a named roadmap's artifacts sit under a subdirectory keyed by its roadmap file stem, never flat under `plans/`. Where no sidecar is on disk, both fields are recorded as absent rather than guessed — and since a sidecar missed by reading the wrong path records exactly the same thing, losing the numbers with no signal, the locator is named here rather than left to the two flat paths already written at `src/skills/task-rescue/SKILL.md:387` and `:424`.

3. A new final step, `## Step 5.7`, placed after `## Step 5.6` and before `## What NOT to do`, writes the report once, at the end, when the repair is done and the task is ready for a new run. `note` is invoked once with all three hooks supplied. The destination is `<skills repo root>/.ai-factory/rescue-reports/<project>/`, where the root comes from `git -C ~/.claude/skills/task-rescue rev-parse --show-toplevel` and `<project>` from the last segment of `git rev-parse --show-toplevel` in the project being rescued, both run at this moment and neither stored or cached. The template is caller-supplied and verbatim, in the shape the folder already holds: a title line `# <task number> — <short phrase naming what stopped the run>`, then `**Project:**`, `**Date:**` in ISO form, `**Stopped at:**` and `**Elapsed before the rescue:**` from the four facts of item 2, then the diagnosis as Step 3 wrote it, then what the repair did — the depth chosen, or the escalation option, or the non-convergence choice, and what was deleted or kept. Where Step 3 produced no root-cause sentence and no category, as it does for an escalation, the report carries what Step 3 actually emitted; the template never demands a part that branch does not produce. The verbosity directive keeps the diagnosis's own register and length.

4. Where the report cannot be written — the skills root does not resolve, or the run has not been given that repository as a writable directory — say so plainly and complete the rescue anyway. Never invent a fallback path, never fall back to a directory inside the project, and never invoke `note` a second time. There is no second write and nothing is reopened later: a run that ends before this step leaves no report, which is the accepted cost of writing once.

5. The chat printout stays exactly as it is. The file is additional, and no step of the skill ever reads it back.

## Files & types

- edit: `src/skills/task-rescue/SKILL.md` — the `loads:` line, Step 1, and one new step at the end of Step 5

## Guards

- The grant gains exactly one entry, `Bash(mkdir *)`, and nothing else. `note` issues `mkdir -p <destination>` unconditionally before saving (`src/skills/note/SKILL.md:60-63`), on every invocation and whether or not the directory exists, so a caller that delegates the write must carry it: `src/commands/command-handoff.md:9` grants it for exactly this delegation. The per-directory numbering scan needs no `Bash(ls *)` — this skill already grants `Glob`. Nothing else in the frontmatter moves, and where a step seems to need `readlink`, the git resolution is used instead.
- The destination lies outside the project the rescue runs in. Where the run cannot write there, the step says so plainly and the rescue still completes — it never skips the report silently and never falls back to a directory inside the project. Setting that up is a one-time act per project: the skills repo has to be an allowed directory in the session the rescue runs in, through `--add-dir` or that project's own settings.
- `task-rescue-audit` is not touched. Its own text forbids writing files, and whether it gains this capability is a separate decision.
- Step 5.6 and the marker grammar stay exactly as they are; the report has no part in pinning.
- `note`'s mechanics are not restated here — numbering, `mkdir -p` and folder style stay in `note`, reached through its hooks.
- The ≤ 500-line body constraint in `CLAUDE.md` § "Key constraints" is deliberately not applied to this file, and its length is never a finding here. The skill's own instruction core — read the artifacts, name the root cause, propose the repair — is about 164 lines; the remaining bulk is the rollback state machine that mirrors the orchestrator's resume contract, where length is fidelity, not bloat. Write what this task needs in full, in the register the surrounding steps already use: do not compress an existing sentence to make room, do not move anything into `references/`, do not shorten the new steps to save lines, and do not propose a split. The file is 581 lines today and is expected to grow.
- One report file per run, written once. `note` is invoked exactly once and the file is never reopened, by this run or a later one.

## Verification

Counts against a whitespace-normalized read of the named file, never a line-oriented `grep`.

- the `loads:` line reads `orchestrator-artifacts roadmap-engine note` → 1
- the `allowed-tools` line equals the same line in `git show HEAD:src/skills/task-rescue/SKILL.md` with exactly one entry added, `Bash(mkdir *)` → the words `Write`, `Edit`, `Glob`, `Grep`, `Bash(git *)`, `AskUserQuestion` and `Skill` each still appear on it, and no other entry is new
- the word `readlink` → 0, and `rev-parse --show-toplevel` → ≥ 1
- `.ai-factory/rescue-reports/` → ≥ 1
- Step 1 states that the four facts are captured before anything is deleted → ≥ 1
- the new step names all three of `note`'s hooks → each ≥ 1
- the file states that the report is written on every terminating branch, escalation and non-convergence included → ≥ 1
- the file states that the resolved path is never stored or cached → ≥ 1
- the file states that the report is written once, at the end, when the repair is done and the task is ready for a new run → ≥ 1, and that `note` is invoked once per run → ≥ 1
- the file states both ways the write can fail and that the rescue completes anyway → ≥ 1, and the words `reopen` and `fallback path` do not appear as permitted behavior → the file never instructs a second write
- `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly `src/skills/task-rescue/SKILL.md` and nothing else
- the file names `orchestrator-artifacts` § 1 as the locator of the sidecar → ≥ 1, and pins `git rev-parse --show-toplevel` for the project's own name as well as for the skills repo root → ≥ 2 together
- the file names the scope-overload exit as the one terminating branch that does not reach the closing step → ≥ 1
- No count above is trusted as evidence until it was taken by the normalized method named at the head of this section
