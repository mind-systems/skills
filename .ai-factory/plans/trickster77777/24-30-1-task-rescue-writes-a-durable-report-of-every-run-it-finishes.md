# Plan: 30.1 — task-rescue writes a durable report of every run it finishes

## Context
`src/skills/task-rescue/SKILL.md` prints its Diagnosis Report to chat and then deletes the artifacts it was drawn from, so a failed attempt leaves nothing behind. This task makes the rescue write one durable report per run — into the skills repo, under `.ai-factory/rescue-reports/<project>/` — through the `note` engine, at the end, once the repair is done.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Frontmatter

- [x] **Add the `note` edge and the one grant it needs**
  Files: `src/skills/task-rescue/SKILL.md`
  Two single-line edits in the frontmatter, nothing else in it moves.
  - `loads:` (`:12`) becomes exactly `loads: orchestrator-artifacts roadmap-engine note` — the two existing entries kept in place, `note` appended.
  - `allowed-tools:` (`:11`) gains exactly one entry, `Bash(mkdir *)`, and nothing else: `Read Write Edit Glob Grep Bash(git *) Bash(mkdir *) AskUserQuestion Skill`. Every word already on that line (`Read`, `Write`, `Edit`, `Glob`, `Grep`, `Bash(git *)`, `AskUserQuestion`, `Skill`) must still be there afterwards; compare against `git show HEAD:src/skills/task-rescue/SKILL.md` before finishing. The grant exists because `note` issues `mkdir -p <destination>` unconditionally on every invocation (`src/skills/note/SKILL.md:60-63`), so a caller delegating the write must carry it — `src/commands/command-handoff.md:9` carries it for exactly the same delegation. No `Bash(ls *)` is added: `note`'s `[0-9][0-9]-*.md` numbering scan is served by the `Glob` this skill already grants.
  - Do **not** touch `description:`, `argument-hint:`, `name:` or `disable-model-invocation:`. A durable side effect does not change the moment the skill is invoked, so the description says nothing about the report.
  - The body's "Ensure `orchestrator-artifacts` is loaded…" / "Ensure `roadmap-engine` is loaded…" paragraphs (`:32-38`) are the file's own load protocol; the `note` invocation is written at its point of use in Step 5.7 (below), not as a third paragraph here — `note` is called once, at the end, not loaded at entry.

### Step 1 — the four facts

- [x] **Capture project, date, `step` and `elapsed` at discovery, before anything is deleted** (depends on the frontmatter edit)
  Files: `src/skills/task-rescue/SKILL.md`
  Add one bolded sub-block to `## Step 1 — Discover artifacts`, in the register the surrounding sub-blocks use (`**Identify the task slug.**`, `**Read the phase's governing spec and phase note.**`). Place it **after `**Read the phase's governing spec and phase note.**`** and before `**Read every artifact file found**`. That placement is load-bearing, not cosmetic: the sidecar path needs both the slug (resolved by `**Identify the task slug.**`) and `$TARGET_FILE`, and `$TARGET_FILE` is first determined by the governing-spec sub-block (`:58-59`) — nothing earlier in Step 1 touches it. The new sub-block therefore reads `$TARGET_FILE`; it never resolves it itself, since the file already performs that resolution here and again in Step 4. Do not shorten or reflow any existing sentence to make room.
  Content, all of it explicit:
  - State plainly that these four facts are recorded **at discovery, before anything is deleted**, and held for the report Step 5.7 writes. That ordering is the whole point of capturing them here: Step 5 deletes the sidecar at spec depth (`:373`) and its `step`/`elapsed` are unrecoverable afterwards.
  - **Project** — the last path segment of `git rev-parse --show-toplevel` run in the project being rescued. This fact fills the report's `**Project:**` line; it is not the destination path, which Step 5.7 resolves for itself at write time.
  - **Date** — today's date, ISO form (`YYYY-MM-DD`).
  - **`step` and `elapsed`** — read from the task's sidecar; the two fields worth keeping per `orchestrator-artifacts` § 3.
  - **Where the sidecar lives** — name `orchestrator-artifacts` § 1 as the locator, and state the consequence explicitly: the flat `plans/<seq>-<slug>.json` layout holds for the default `ROADMAP.md`/`ROADMAP_TESTS.md` pair only, while a named roadmap's sidecar sits under a subdirectory keyed by its roadmap file stem (`roadmaps/john-doe.md` → `plans/john-doe/<seq>-<slug>.json`). `$TARGET_FILE` is already resolved in this step, so the stem is known here. Say why it is pinned: a sidecar missed by reading the wrong path records exactly the same thing as an absent one — both numbers lost, with no signal.
  - **No sidecar on disk** → record both fields as **absent**; never guess, never reconstruct a number from anything else. Step 5.7 renders absence as absence.
  - Leave the two flat `.ai-factory/plans/{seq}-{slug}.json` paths at `:387` and `:424` exactly as they are — they are outside this task's edit set.
  - Do not use `readlink` anywhere in this file; the git resolution above is the only path resolution used.

### Step 5.7 — the durable report

- [x] **Add `## Step 5.7` — one report per run, written once through `note`** (depends on the Step 1 capture)
  Files: `src/skills/task-rescue/SKILL.md`
  Insert a new step titled `## Step 5.7 — Write the durable report`, placed after `## Step 5.6 — Pin disposed observations` and before `## What NOT to do`, separated by the same `---` rule the neighboring steps use. Write it in full, in the prose register of Steps 5.5/5.6. The `≤ 500-line` body constraint in `CLAUDE.md` § "Key constraints" does not apply to this file and its length is never a defect here: do not compress existing text, do not move anything into `references/`, do not propose a split.
  The step must state, each explicitly:
  - **When.** The report is written **once, at the end, when the repair is done and the task is ready for a new run** — `note` is invoked **exactly once per run**, and the file is never reopened, by this run or a later one. There is no second write and nothing is completed later; a run that ends before this step leaves no report, which is the accepted cost of writing once.
  - **Which runs.** Every terminating branch that reaches this step writes a report — every repair depth (spec, spec+plan, spec+plan+code, plan-ratified), **escalation** (all three options of Step 4's escalation branch, including option 3, which runs no Step 5 procedure and arrives here via Step 5.5) and **non-convergence** (all three options) included. Name the **scope-overload exit** as the one terminating branch that does not reach this step: Step 4 flags it, points to `/roadmap-decompose` and skips the depth menu, so no repair runs and no report is written.
  - **Destination, both halves resolved at write time.** `<skills repo root>/.ai-factory/rescue-reports/<project>/`, built from two commands run **at this moment**, here in Step 5.7: `git -C ~/.claude/skills/task-rescue rev-parse --show-toplevel` gives the skills repo root (inside the existing `Bash(git *)` grant; `~/.claude/skills` is the personal-scope symlink every session already relies on to load any skill), and `git rev-parse --show-toplevel` run in the project being rescued gives, in its last path segment, `<project>`. State that **neither half is stored nor cached** — the address is never carried from an earlier step. The Step 1 project fact is not this address: it fills the report's `**Project:**` line, and the path is re-resolved here regardless. The destination lies outside the project being rescued — the skills repo has to be a writable directory in the session (via `--add-dir` or the project's own settings), a one-time setup act per project.
  - **All three of `note`'s hooks are supplied** (`src/skills/note/SKILL.md:31-33`), named as such:
    - *destination directory* — the path above; it drives `note`'s `mkdir -p`, its per-directory `[0-9][0-9]-*.md` numbering scan and the final path.
    - *template* — the caller-supplied skeleton below, passed verbatim.
    - *verbosity directive* — the diagnosis keeps its own register and length; the report is not re-condensed. (This replaces `note`'s default Rules 1 and 2 for the run.)
    Also pass the topic slug `note` takes as `$1`: the task number with dots as hyphens, followed by the same short phrase used in the title line (e.g. `30-1-<phrase>`), matching the files already in the folder.
    Do not restate `note`'s mechanics — numbering, `mkdir -p`, folder style stay in `note` and are reached through the hooks.
  - **The template**, given literally in a fenced block, in the shape the folder already holds (`.ai-factory/rescue-reports/skills/01…03`):
    - title line `# <task number> — <short phrase naming what stopped the run>` — a phrase, never a root-cause claim, so branches that produce no root cause still have a title;
    - the four facts as `**Project:**`, `**Date:**` (ISO), `**Stopped at:**`, `**Elapsed before the rescue:**`, each rendered as **absent** where Step 1 recorded absence;
    - the diagnosis as Step 3 wrote it;
    - what the repair did — the depth chosen, or the escalation option taken, or the non-convergence choice — and what was deleted or kept.
    State that where Step 3 produced no root-cause sentence and no category (the escalation branch, which ends in the restated decision instead), the report carries **what Step 3 actually emitted**: the template never demands a part that branch does not produce, and no section is invented to fill it.
  - **When the write cannot happen.** Name both ways it fails — the skills repo root does not resolve, or the run has not been given that repository as a writable directory — and require the step to **say so plainly to the user and complete the rescue anyway**. Never invent a fallback path, never fall back to any directory inside the project being rescued, never invoke `note` a second time, and never defer the write to a later run. State this at this spot rather than relying on a ban written elsewhere.
  - **The chat printout is unchanged.** The Diagnosis Report is still printed exactly as Step 3 mandates; the file is additional, and no step of this skill ever reads it back.
  Do not touch Step 5.6 or the marker grammar — the report has no part in pinning. Do not touch `src/skills/task-rescue-audit/SKILL.md`.

### Verification

- [x] **Check the edit against the task spec's verification list** (depends on the Step 5.7 addition)
  Files: `src/skills/task-rescue/SKILL.md`
  Take every count on a whitespace-normalized read of the file, never a line-oriented `grep` — a requirement wrapped across two lines must still count. Confirm: the `loads:` line reads `orchestrator-artifacts roadmap-engine note`; the `allowed-tools` line differs from `git show HEAD:…` by exactly the one added entry; `readlink` appears zero times and `rev-parse --show-toplevel` at least twice — Step 5.7 alone must carry two, the project's own name and the skills repo root, alongside Step 1's capture of the project fact; `.ai-factory/rescue-reports/` appears; Step 1 states the capture happens before anything is deleted, sits after the sub-block that determines `$TARGET_FILE`, and names `orchestrator-artifacts` § 1 as the sidecar locator; Step 5.7 names all three `note` hooks, states write-once/invoked-once/never-reopened, states that both halves of the destination are resolved at write time and neither is stored or cached, states that every terminating branch including escalation and non-convergence writes a report, names the scope-overload exit as the one that does not, and states both failure modes with the rescue completing anyway. Finally, `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` must list exactly `src/skills/task-rescue/SKILL.md` and nothing else.
