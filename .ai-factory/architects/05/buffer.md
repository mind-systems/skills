# Architect 05 — buffer

The pair's shared memory for architect 05. The head writes it; the hand reads it whole and never writes to it. Shape and standing entries follow `src/skills/agent-architect/templates/buffer-seed.md`.

## Where things stand

*2026-10-01 — rewritten at the migration into this folder.*

**This head was idle from 2026-09-09 to 2026-10-01** and holds no live round. It was woken by the user to move its memory into `.ai-factory/architects/05/` and bring the buffer current.

**The migration, done by hand and not committed:** the buffer moved from `.ai-factory/notes/05-architect-buffer.md` to this file; the one memory snapshot this head wrote, `12-phase-note-and-the-transformation-walk.md`, moved in beside it, its pointer to the buffer repointed here; `address.md` written — `session-id: e0bf20a8-9c9c-4e92-bd30-aa6568e01ab9`, `session-name: skills-eb`, the id read by probe (exactly one transcript matched). Handoffs 09, 10, 11, 13 also name the old buffer path but stayed in `.ai-factory/handoffs/`: 09, 10 and 13 were written by other heads and mention it only from outside; 11 was written by this head but is a project handoff for a reviewer, not a memory snapshot.

**`skills`** — everything this head planned is committed and pruned from the roadmap: 28.1 `e264805`, 28.2 `01ec355`, 29.1 `0762ab8`, 35.1 `5db3995`. What is open now is read off the seam of `.ai-factory/roadmaps/trickster77777.md`, not from here; none of it is this head's.

**`orchestrator`** — the phase-note task this head wrote there never landed: no prompt reads `Phase note:`, its spec is gone, and its task numbers there now belong to other work. See the ledger.

## Team

Each node holds its own links, not the whole network. A folder number resolves to a live address through that folder's `address.md`.

**Above:** `skills`, folder 07 — the liaison. Reach it by `SendMessage` at the name in `.ai-factory/architects/07/address.md`; never read its buffer. This placement reached me through 07's message of 2026-10-01, which said the user put me in its team; the user has not said so in this chat yet.

**Below:** none.

## Rulings in force

Only rulings not yet held by an artifact. Each is a debt; it leaves when an artifact states it.

**No path into a sibling repository inside a shipped skill.** The user: «скилы работают вне нашего сакши контекста и они конечно могут рассуждать об оркестраторе, кто выполняет таски, но как об абстрактной личности-скрипте, но не ссылаться на его сорсы». Two shipped skills still break it — see the ledger entry on orchestrator sources.

**The governing spec is final when a task runs; a run that would have to change it escalates.** The user: «если оркестратору приходится править тз — это скорей момент для эскалации, чем нормальное поведение. Тз к моменту исполнения таска обязано быть в финальном состоянии». The boundary that goes with it: escalation answers a spec that contradicts or fails to cover the behaviour a task names, never the mere absence of a pointer. Not yet in `orchestrator/orchestrator/prompts/escalation.md` — see the ledger entry on escalation.

## Method

A mistake as the pattern behind it and the reason it holds.

**Standing entry — the counts rule.** A number someone decided is written:
it stays true however the tree grows. A measurement of the current tree is
not written, dated or not — write what produces it, the rule or the search
that gives it fresh each time. A spec least of all carries a number
measuring the tree: tasks run one after another, and each one changes the
tree the next was written against, so such a number in a queued spec is
false before the orchestrator reaches it, and the orchestrator cannot
execute a spec whose facts no longer hold. A number met in a spec, a plan or
a report is read as an order of magnitude; one that has gone stale is not a
defect to correct, count again or stop on. Two counts that disagree are not
reconciled against each other; ask which member is missing.

**Standing entry — what a spec holds.** A spec states what is true now,
what must be true after and what breaks on contact, and nothing else. It
carries no check that the instruction was carried out: the orchestrator
plans, builds and reviews on its own, and a check written into a spec comes
back as plan steps and review rounds. It names no position in a file, only
what the artifact must hold. It puts no fence around a neighbour; scope is
what the task changes.

**Standing entry — state the behaviour and stop.** A rule says what happens
and ends there: no sentence for each case it excludes, no guard against its
own misuse. A rule or a fix that needs guards against its own machinery is
the wrong one.

**Standing entry — a task is not retold in the code.** A spec's reasons are
for whoever plans, and the code keeps none of them. A task says what must be
true and what to delete or link; it never asks for a comment carrying its
reasoning, a skeleton's contract or its scope. A comment in code says only
what a reader would get wrong from the code alone, where the reader meets
it, in a line or three.

**Standing entry — the orchestrator's commit takes the whole tree.** While
it runs a queue in a repository, leave nothing uncommitted there, or it
lands inside a task's commit.

**A check whose result does not depend on the truth it tests is worse than no check.** It came in four shapes, each believed: a line-oriented `grep` returns 0 for a phrase that wraps; an exact match fails on `**` inside a quoted span or on the same claim worded differently; `wc -m` returns bytes, not characters, because this shell's locale is not UTF-8; a predicate of my own tested the wrong terminator. So: compare against a whitespace- and emphasis-normalized read, count characters as code points, and when a check disagrees with a report, suspect the check before the report.

**A path is tested by opening it, never by reading it.** Paths that looked right dropped a package directory and opened nothing, in a spec, a contract line and two shipped skills; each was found only by extracting every path a file names and testing it for existence.

**Before changing anything's role in a file, find every place the file names it.** Replacing one item and leaving its references further down produced a self-contradicting spec three times in a row. Past a handful of edits to one file, replace the file whole — a batch of partial replacements once matched nothing and left withdrawn text standing.

**A value I produced, and a check I received ready-made, get no exemption from measurement.** Both errors trust a thing for where it came from instead of what it says.

## Orientation

**This buffer's history before the folder** is not here; it is `git show 96ffb4c:.ai-factory/notes/05-architect-buffer.md` — the round-by-round record of 2026-09-04 to 09-09. Two heads wrote into that file under the same number: the session that founded it, and a later continuation that rehydrated from it. The pairing roles both of them recorded are gone: `architect-pairing-engine` no longer exists in `src/` or `active/`, and `docs/paired-loop.md` § "Working with another architect" states there are no roles.

**Editor.** No editor is live for this head now. The old record names two handles, `ab8b2f1a1b98a601b` and `aa73188f9b856545e`; the next channel-message is the only liveness probe, and whichever hand receives it must be told this buffer's new path, `.ai-factory/architects/05/buffer.md`, in that same message.

**The phase note is the architect's, not the orchestrator's — by design.** In `skills` the `Phase note:` pointer is emitted by `roadmap-outline-deep`, read by `roadmap-decompose` and `task-rescue`, and captured by `roadmap-prune`. No orchestrator prompt reads the pointer on a phase header, and that is intended: per 07, the user ruled on 2026-09-24 that a task is complete and self-sufficient and the phase note is for the architect; a spec that names the note gets it read through the planner's walk along named edges. A reader who assumes the run sees the header pointer is wrong.

## Ledger

**Orchestrator sources cited from shipped skills, by paths that open nothing.** What: `src/skills/task-rescue/SKILL.md`, in the sentence after the closed set of `step` values, cites `orchestrator/resume.py` and two functions in it; `src/skills/orchestrator-artifacts/SKILL.md` § "Mirrors-the-orchestrator invariant" cites `orchestrator/main.py`, `agents.py`, `prompts/reviewer.md`, `prompts/escalation.md`, `resume.py`. Both load into every project. The fix keeps each invariant in behavioural terms and drops the paths — the invariant is real, only the pointer is wrong. Why deferred: paused by the user while pin-gaps work was in flight. Trigger: the user's go; the pin-gaps work it waited on is long done. Confirmed on the files by 07 as well.

**Escalation does not name a spec that fails to cover the target.** What: `orchestrator/orchestrator/prompts/escalation.md` names "the ratified spec above the current task" as a cause, which covers a fork the spec leaves open but not a spec silent on the behaviour a task names; the user's ruling under § "Rulings in force" needs it, with the boundary that absence of a pointer is never a cause. Why deferred: left to the orchestrator-side head in a handoff there. Trigger: a run escalating on a missing pointer, or the user's go.

**Pipeline skill descriptions carry neither the docs nor the direction.** What: the `description:` of `roadmap-outline`, `roadmap-decompose`, `task-rescue` and `roadmap-prune` never mention documentation. Why deferred: the user considers the descriptions well written. Trigger: the docs-are-the-ТЗ argument recurring with an agent.

*Closed:* both deferrals against `docs/reserved-words.md` — the file is declared final; the reference-by-name handoff into `tradeoxy_core` — its `RULES.md` carries no position rule now; the orchestrator not reading `Phase note:` — by design, the user's ruling of 2026-09-24 as 07 reports it; copy-or-link for a task spec — drained: `src/commands/command-pin-gaps.md` itself says a task spec repeating a paragraph from a document is not a finding, and the global "never a copy" sits under § "Documentation style", governing docs.

## Candidates — not tasks

None at the moment.

## Current thread

None. This head is between threads.
