# Rescue analysis — checkpoints

Dated entries, newest first. Each says what was asked, how far the record was read in each repository, what the record showed in words, and what stayed silent. Conclusions carry no tallies: a measurement of the record goes stale, so a re-run of the method in `method.md` (scripts in `drafts/`) gives the numbers again. Hashes, file names and timestamps are coverage anchors, not findings.

Clocks: transcript times are UTC (`Z`); commit times are the commit's own +06; a rescue report's `**Date:**` is a calendar date.

## 2026-10-08 — do the planner sessions that survived a rescue notice that their spec and plan were changed under them?

**Question.** Where a rescue repaired a task at the specification-and-plan depth, the planner session was kept. Does that session notice that its spec and plan were changed under it, and what in a spec helps or burdens it?

**Selection.** Rescue reports whose repair went to the specification-and-plan depth, with the sidecar kept and the `planner` session id kept: `0026`, `0027` and `0029` in `.ai-factory/rescue-reports/tradeoxy_core/` print the rewritten sidecar with the id. Transcripts are at `~/.claude/projects/-Users-max-projects-tradeoxy-tradeoxy-core/<id>.jsonl`.

**Coverage.**
- `tradeoxy_core`
  - Newest rescue report: `0029-79-4-a-census-line-that-contradicted-its-own-latch.md` (date 2026-10-07).
  - Newest commit when this entry was written: `7038dc8`, 2026-10-08 11:12 (+06). The commit at the time of the interview was not recorded.
  - Interviewed: core 79.3.2, session `0bd50cc0-2cae-4034-94b3-0dc9f2ba3260`, which survived more than one such rescue. Transcript from 2026-10-07T03:13:39Z to 2026-10-08T05:52:54Z (UTC). The last time is probably the interview's own turns, because a resumed session appends to its file; this was not verified.
  - Not interviewed: core 79.4, session `83f8d8fb-1332-453e-a9cd-431f781d5cf2` (a single rescue after a full reset; transcript from 2026-10-07T09:25:57Z to 2026-10-07T10:52:10Z), and core 55.7 (four rescues). The planner id of 55.7 is not printed in its reports; it would be found by the plan path inside transcripts.
- `tradeoxy_broker`, skills repository: not part of this question.

**What the record showed.** The planner session met the changes: the harness's "changed on disk" note, lines in its plan it had not written, paragraphs added to the spec, review files gone or rewritten. Each time it took the file as the truth in silence and built on what the rescue had written as if it were its own work. It did not ask who had written what.

The one finding that came from the spec's own text was a sweep pinned verbatim into the spec, and the plan review then faulted the plan for leaving it out. The other findings came first from the code and were copied into the spec afterwards by the rescue, so the spec absorbed findings and did not produce them.

What helped the planner were decisions with their reasons that the code does not show: a run policy and why its timeout matches an existing wait; an empty registry and why it never grows; a fixed holder name and why uniqueness is not needed.

**Silent or uncovered.** Whether the surviving session misled any later round. Whether the other sessions behave as the interviewed one did. The interview answers were taken about what the conversation shows, never about the planner's reasoning (see `method.md`).

## 2026-10-07 — did the gap pass run on the tasks that escalated; how pin-gaps changed and why; why tasks started passing

Several questions were asked in one day from the same record. They share the method in `method.md`.

**Questions.**
1. Was `command-pin-gaps` run on the tasks that escalated in the rescue reports before they ran: core 52.1, 53.1, 55.8, 63.1, 64.3, and broker 43.3 and the broker test task about a snapshot seam?
2. Reconstruct the history of `command-pin-gaps` and, through it, how and why the project and its other skills changed.
3. Test the user's theory: (A) in the skills repository tasks started passing first time because specs pin the wording and tasks are atomic; (B) in `tradeoxy_core` simple bug-fix tasks ran clean and rescues began with engine work because the blast radius there is abnormally large.

**Coverage.**
- Skills repository (`/Users/max/projects/sakshi/skills`)
  - Newest rescue report: `09-58-2-an-invariant-that-counted-lines-across-its-own-rewrap.md` (2026-09-24).
  - Newest commit: `3a312d2`, 2026-10-07 18:05 (+06), a "Roadmap update". Newest task commit with orchestrator artifacts: `69d8826` (75.1), 2026-10-06 12:24. `579e0c2` (77.2, done in chat, no artifacts), 2026-10-07 12:50.
  - Newest transcript: the skills folder's latest invocation of the command at 2026-10-07T10:11Z, without arguments; the latest with arguments 2026-09-30T13:40Z.
- `tradeoxy_core`
  - Newest rescue report: `0029-79-4-a-census-line-that-contradicted-its-own-latch.md` (2026-10-07).
  - Newest task commit read: `1da3570` (79.7.2), 2026-10-07 18:11 (+06).
  - Newest transcripts: long architect sessions ending 2026-10-07T09:49Z; newest invocation of the command 2026-10-03T06:07Z.
  - Handoffs and snapshots scanned from commits through 2026-10-07.
- `tradeoxy_broker`
  - Newest rescue report: `0005-13-2-3-cancellation-heard-only-through-the-request-stream.md` (2026-10-06), read for its date only; the report of the snapshot-seam test task is `01-the-snapshot-seam-the-spec-promised-on-a-path-that-has-none.md`.
  - Newest commit: not recorded at the time; at writing it is `ee844ee`, 2026-10-06 13:37 (+06).
  - Newest transcript: `3a1202f9-…` ending 2026-10-06T06:44:51Z; newest invocation of the command 2026-10-02T06:21Z.
  - Handoffs and snapshots scanned from commits between 2026-09-17 and 2026-10-02.
  - No per-task round table was built for broker.
- `tradeoxy_gui`, the orchestrator: invocations of the command and their arguments only (GUI latest 2026-10-03T06:23Z; orchestrator latest 2026-09-28T12:14Z). Their commits, rescues and prompts were not read.

**Corrections to the 2026-10-07 report.** Flaws that change how its tables read:
- The pass flags in the round-count script (`ppass`, `rpass`) test only that the token occurs somewhere in the last review file. They came out true for every task, which means the token also occurs in text that is not a pass. "Ended on a pass" is unproven; do not use those flags.
- The rescue sets used to mark tasks as rescued were typed by hand from file names, in both repositories. The core set left out core 77.1 (report `0024-77-1-a-seam-whose-write-was-left-to-be-invented.md`). The tables are unaffected because core has no 77.x row in the data, but the sets are not a list of every rescue.

**What the record showed, question 1.** The gap pass ran before the run on every escalated core task and on broker 43.3, each shown by a transcript that names the task and its spec, and in most cases by the editor's scan report. It did not run on the broker test task: that spec was written by the test-coverage pass and marked ready, and the later gap pass covered only its gated neighbours (specs `0008` and `0010`), the next day. What stopped each run was something the pass did not see or had introduced: a catch-all translation, a deferred step, an opaque key core does not own, a type correction by the pass itself that cost a tick, guards added around a restart design that should have been revived in place, a work item that carried a copy of its order. The passes found other holes in the same specs and closed them.

**What the record showed, question 2.** The command began as a pin of unpinned values with a cited line, split meaning holes from value holes after a failure on an unspecified contract, then became a walk from the task into the code with a third class for blast radius. Each repair of a failure became the next failure: telling it to enumerate what a change breaks led specs to carry a census of call sites; the repair to rule, sweep and invariant said "every match must satisfy after the change", an instruction to a later run; that became a recorded finding. A pass over a task whose replacement text is pinned finds nothing in the content, so its holes lie in the checking apparatus, and it closes them by enlarging it. The user's rulings turned the direction several times: one task at a time and one mode; a task is a ticket, not a plan; a single field instance is not a phase. The evidence is `git log --follow` on `src/commands/command-pin-gaps.md`: `9814b65`, `62ae16a`, `cb30cb7`, `cd0853a`, `5348761`, `0762ab8`, `497510b`, `02ff899`, `2051e54`, `d219456`, `59cf80f`, `98f08b6`. Premises of the brief that did not hold: the command was still used after 2026-09-30 in the tradeoxy repositories (and, without arguments, in this one on 2026-10-07), and rescues continued in core and broker after that date; only the skills repository has had none since 2026-09-24.

**What the record showed, question 3.**
- (A) holds in part. Rounds fell and run time fell after 2026-09-30, and code review now almost always passes first time. New skills and fundamental rework did cost rounds. But pinned wording did not by itself make runs clean: the batch of 2026-09-24 pinned heavily and ran no faster than before. Atomic tasks did not discriminate either: multi-file tasks pass first time in the later window, and single-file tasks took extra rounds in the earlier one. The extra rounds were about the plan's and spec's own checking apparatus (a verification step that collided with its wording, an anchor on a wrapped line, a wrong governing spec named, a census over a list), not about reach.
- (B) holds in part. Blast radius correlates with rounds across core, and the wide retyping tasks and the shared-pool and backtest-engine stretches rescued most. But the simple door fixes of 2026-09-18 also escalated, on a design or premise error, and the stretch after the review-debt fixes began with hygiene tasks of very wide reach, not engine work. Core's first-round plan-review rate stays roughly flat over time, including the clean stretch. No report attributes a failure to branching threads in the code; the "radius the compiler could not see" reports describe comments, test doubles and titles.

**Silent or uncovered.**
- The timestamps of the escalated runs themselves; I bounded them by the rescue dates.
- The first run's artifacts for any rescued task (a rescue deletes them).
- Rescue reports before 2026-09-08 in the skills repository's folder.
- The reasons for deleting phases 44 and 46 to 48 beyond the buffer's ruling.
- The user's exact words on 29.1 and on keeping "guards".
- The creation conversation of 2026-06-22.
- Whether the orchestrator's prompts changed between windows.
- Whether the gap pass ran on every task in every window; only the escalated tasks were checked.
- Editor sub-agent transcripts were not read.
- Broker per-task rounds, the GUI and orchestrator repositories, `tradeoxy_analyst`, `mind`.
