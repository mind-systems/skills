# Rescue analysis — method

The algorithm used to read the pipeline's record: rescue reports, task commits with their plans and reviews, session transcripts, architect handoffs and snapshots. The scripts are in `drafts/`, each marked DRAFT. Dated results are in `checkpoints.md`.

The method answers questions of the form "what happened to these tasks, and why". It never reads a buffer. It reads the record and says where the record is silent.

## Sources, and what each can and cannot show

| Source | Where | Shows | Cannot show |
|---|---|---|---|
| Rescue reports | `.ai-factory/rescue-reports/<project>/` in the skills repository | Why a run stopped, how deep the repair went, what was deleted | Runs before the reports began (the skills repository's folder starts at 2026-09-08) |
| Task commits | the project repository; subject `N.M — title` | The plan, plan-reviews and reviews of the run that landed, files changed outside `.ai-factory` | A failed run: a rescue deletes its plan, reviews and sidecar |
| Roadmap diff of a landing commit | `.ai-factory/ROADMAP.md` or `.ai-factory/roadmaps/<slug>.md` | The contract line, its `Spec:` tag, the `[x]` line with its run duration (skills repository) | A line reworded after landing |
| Spec history | `git log --follow -- <spec>` | When a spec was created and changed, by author date and commit date | Who changed it (a rescue or the architect), except by matching the date to the rescue |
| Session transcripts | `~/.claude/projects/<folder>/<session-id>.jsonl` | What was said and run, with times; every use of a command | An editor sub-agent's own work (a separate file); anything not retained |
| Handoffs and snapshots | `.ai-factory/handoffs/`, `.ai-factory/architects/*/NN-*.md` | What the architect wrote about the work at a time | The date it was written (only the date it landed in git) |

The transcript folder is the working directory's path with every non-alphanumeric character turned into a hyphen.

## Clocks

Every date in a result names its clock.

| Clock | Where it appears | Note |
|---|---|---|
| UTC (`Z`) | Transcript timestamps | The only clock that orders events across sessions |
| Commit's own zone (+06 for this machine) | `git log --date=format:…`, `%ad` and `%cd` | Commit time is the end of an amend chain; author time is its start |
| Calendar date | `**Date:**` in a rescue report | The day the report was written; checked against transcripts within a day |
| Duration | `[5m 33s]` on a done roadmap line | A length, not a time of day; covers the run that landed |

A "Roadmap update" commit is amended by the commit command until pushed, so its author date can be days older than its commit date. Use the commit date for when something landed in git and a transcript for when it was authored; print both when the difference could matter.

## Algorithm, by question

### 1. Did a gap pass run on a task before its run?

1. From the rescue report, take the task number and the date.
2. Find the contract line, even if pruned: `git log --all -S"**N.M —" -- <roadmap>`; read the first version and take the `Spec:` tag (`drafts/01`, `drafts/07`).
3. Get the spec's history with author and commit dates and match the commits to events (creation, a pass, the rescue) (`drafts/07`).
4. Search the architects' transcripts for every use of the command and its arguments (`drafts/02`, `drafts/03`), then for the editor's scan reports that name the task and spec (`drafts/05`), then for the task's id on the days around the pass (`drafts/04`).
5. Cross-check against handoffs and snapshots of the weeks around the writing and the run (`drafts/06`).
6. Verdict per task: ran, did not run, or unknown, with the transcript time or commit hash as evidence. Where nothing is found, say so and say which sessions were searched; absence in the retained sessions is not proof.

### 2. How and why did a skill change?

1. List the commits of the file with `git log --follow`; read each diff for meaning (which holes it was told to close, how, what it was forbidden to do) (`drafts/01`).
2. For each commit, find its task: the subject, then the roadmap line (`drafts/01 line`), then the spec (`drafts/15`), then rescue reports and handoffs of the same days.
3. Record what else moved in the same commit and in the neighbouring commits of the same days.
4. Group the commits into eras: stretches in which one kind of hole dominated. For each: what specs looked like, what the pipeline kept failing on, what the command was asked to do, what the change caused next.
5. Mark where a cure became the next disease, and where the user's own words turned the direction; quote the words as the files hold them and name the file.
6. Bring it to today, including what is still open; state premises of the question that the record did not bear out.

### 3. Does a theory about why tasks pass hold?

1. Fix the windows from the question. Choose cut dates that fall in gaps where no task landed, and say they are a judgment.
2. For every task commit in the window, read: plan-review rounds and code-review rounds as the files added in the landing commit; files changed outside `.ai-factory`; the spec's shape (template, length, how much of the after-section is quoted text, a Verification/Guards/Acceptance heading); the run duration from the roadmap diff; a rescue flag (`drafts/08`, `09`, `10`, `11`, `12`).
3. Attach rescues from the reports. Read the set from the report file names programmatically if you can; the original hand-typed it and missed one.
4. Compare groups: windows, then within a window by pinned or not, by files changed, by the presence of a checking section (`drafts/13`, `drafts/14`). A task with no artifacts (done in chat) drops out.
5. Sample: read the first plan-review of tasks that took several rounds and say what the round was about (spec apparatus, plan error, reach).
6. Give a verdict per part of the theory: holds, partly holds, does not hold, with counter-examples; list what the record cannot show.

### 4. Do surviving planner sessions notice a rescue's changes? (the interview)

1. Select rescue reports whose repair went to the specification-and-plan depth. Their rewritten sidecar prints the `planner` session id.
2. Locate the transcript `~/.claude/projects/<folder>/<id>.jsonl` and note its first and last times; remember a resumed session appends to its own file.
3. Resume the session read-only with the planner's own model and effort:

   ```
   claude -p --resume <id> --model opus --effort high --tools "Read,Grep,Glob" < prompt.txt
   ```

   Put the prompt on stdin. A variadic flag such as `--disallowedTools` swallows a trailing prompt argument. `drafts/16-interview.sh` wraps this.
4. Ask about the record, never about inner reasoning. A question of the form "does this conversation show…; quote the places" passes. Questions such as "what you made of…", "how you treated what you remembered", "go through the findings and judge" are stopped by a safety classifier as reasoning extraction, sometimes in the middle of an answer.
5. A stopped answer stays in the transcript. Read it back from the session's `.jsonl`: the visible text blocks of the latest turns (`drafts/17-read-session-text.py`).
6. Report what the conversation shows, with quotes, and say which sessions were not interviewed.

## Coverage discipline

Every run of the method records, per repository, the newest rescue report by file name, the newest commit by hash and time, and the newest transcript by time with its clock. The first checkpoint failed to record the broker's newest commit; record it at the time of the run. A result cannot be re-run, extended or compared without the boundary it stopped at.

## Traps

- **Pass flags.** A test that the token `PLAN_REVIEW_PASS` or `REVIEW_PASS` occurs in the last review file is not an outcome; it came out true for every task. Read the verdict section itself, or the sidecar, if the outcome matters.
- **Hand-typed rescue sets.** Build them from the report file names; the first set missed a report.
- **Failed runs are invisible.** Round counts describe the landed run. A task rescued several times looks like one run.
- **`git log -S`** finds the first and last appearance of a string, not every version.
- **Subjects.** Only commits titled `N.M — title` are tasks. Earlier tasks, and tasks done in chat, are absent or show no rounds.
- **Files outside `.ai-factory`** includes tests and docs; a mirror deletion or a purge is a very large number.
- **The pinned threshold** is a judgment. Sample specs by hand before trusting a total. An early version counted quotes of the current text.
- **A task's spec is read before its landing commit**, so a spec the landing commit itself changed shows its old text.
- **Transcripts** repeat the same message several times; dedupe by time. A session that only mentions a command can contain its marker without a use. An editor's sub-agent transcript is a different file.
- **Shell limits.** A command running over two minutes is moved to the background and its output is not the final one; a notification of a finished background task is not a message from anyone. In zsh, `echo "====="` fails and a glob with no match is an error; `sleep` is blocked, so wait with an `until` loop.
- **Scratch files** in `/tmp` do not survive a session. Rebuild from `drafts/`.

## Drafts

| File | Does |
|---|---|
| `01-pin-gaps-history.sh` | History of one file: commits, diffs, what moved with them, contract lines, neighbours, phase fate |
| `02-pin-gaps-invocations.py` | Invocations of a command per session in chosen transcript folders |
| `03-invocations-all-projects.py` | Last use of a command across all projects; user's arguments |
| `04-transcript-query.py` | Where a string occurs in one session between two times |
| `05-editor-scan-reports.py` | Which tasks an editor reported a gap pass on |
| `06-handoff-snapshot-scan.sh` | Handoffs and snapshots that mention a pass or a task |
| `07-spec-and-rescue-history.sh` | A spec's history, a task's artifacts, a contract line's spec |
| `08-task-rounds.py` | Rounds and files per task commit (the core measurement) |
| `09-spec-shape.py` | Spec template and pinned text per task |
| `10-spec-only.py`, `11-check-only.py` | Spec lookup for a cut-short run; checking-section flag |
| `12-time-suffix.py` | Run duration from the roadmap |
| `13-window-stats-skills.py`, `14-window-stats-core.py` | Group comparisons |
| `15-show-pruned-spec.sh` | First lines of a spec that has been pruned |
| `16-interview.sh` | The interview command |
| `17-read-session-text.py` | Visible text of a session's latest turns |
| `18-verbatim-count.py` | An abandoned measure; kept as part of the record |
