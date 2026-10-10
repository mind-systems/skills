# Architect 05 — buffer

The pair's shared memory for architect 05. The head writes it; the hand reads it whole and never writes to it. Shape and standing entries follow `src/skills/agent-architect/templates/buffer-seed.md`.

## Where things stand

**No open work and no live round.** Everything this head planned in `skills` is committed and pruned. What is open is read off the seam of `.ai-factory/roadmaps/trickster77777.md`, and none of it is this head's. What waits on the user is in the ledger.

## Team

Each node holds its own links, not the whole network. A folder number resolves to a live address through that folder's `address.md`.

**Above:** `skills`, folder 07 — the liaison. Reach it by `SendMessage` at the name in `.ai-factory/architects/07/address.md`; never read its buffer. The placement is 07's report; the user has not confirmed it here.

**Below:** none.

## Rulings in force

Only rulings not yet held by an artifact. Each is a debt; it leaves when an artifact states it.

**No path into a sibling repository inside a shipped skill.** The user: «скилы работают вне нашего сакши контекста и они конечно могут рассуждать об оркестраторе, кто выполняет таски, но как об абстрактной личности-скрипте, но не ссылаться на его сорсы». Two shipped skills still break it — see the ledger entry on orchestrator sources.

**The governing spec is final when a task runs; a run that would have to change it escalates.** The user: «если оркестратору приходится править тз — это скорей момент для эскалации, чем нормальное поведение. Тз к моменту исполнения таска обязано быть в финальном состоянии». The boundary that goes with it: escalation answers a spec that contradicts or fails to cover the behaviour a task names, never the mere absence of a pointer. Not yet in `orchestrator/orchestrator/prompts/escalation.md` — see the ledger entry on escalation.

**A task's "what is true now" is the code as every open task above it leaves it.** The user, through 07: «да не только в фазе! роадмап в принципе так устроен. У меня в голове не укладывается, что это надо объяснять!» What a predecessor rewrites is never quoted into a later task. Drains into the seed as a standing entry when phase 77's task "a task's now" lands; `docs/what-a-task-carries.md` § "What a spec holds" already says it.

**The hand is replaced quietly, inside a window.** The user, through 07: the window runs from half the hand's context, a firm floor, to four fifths, a soft mark, and the head picks the seam between them, «без фанатизма»; the replacement is named in one line in passing, never with token counts, forecasts or a question — «архитектор начнёт ебать мне мозги компактом редактора» is what to avoid. The hand writes its own snapshot and a new hand starts from the buffer plus that snapshot. In force now, before any skill states it. At the seam, the head asks the live hand for its snapshot, which goes into `.ai-factory/architects/05/editor/`. The head then spawns a new hand, giving it the buffer's path and that snapshot's path. Composing the head's own snapshot stays forbidden to the hand. Drains when phase 78 (note `.ai-factory/specs/trickster77777/0215-…`) lands in the skills; `docs/paired-loop.md` does not state it yet either.

**The head's and the hand's snapshots live apart.** The user, through 07: separate folders `architect/` and `editor/` inside the head's folder, «что б память не смешивалась». Not yet the engine's layout — `architect-editor-engine` still keeps snapshots at the folder's root — so this folder's snapshot stays where it is until phase 78 lands.

**Migration of heads is not a risk to raise.** The user: «прекрати уже париться про миграцию… у нас есть гит со всей памятью агента».

**A naming clash in our own text is fixed, not reported.** The user: «Приведи в порядок имена… Для себя же движок строишь!»

## Method

A mistake as the pattern behind it and the reason it holds.

**Standing entry — the counts rule.** It governs what is read later by
someone who cannot ask back — a spec, a plan, a roadmap line, this buffer
after a compact; in conversation a number or a position is fine, since a
wrong one costs one reply. A number someone decided is written: it stays
true however the tree grows. A measurement of the current tree is not
written, dated or not — write what produces it, the rule or the search that
gives it fresh each time. A spec least of all carries a number measuring the
tree: tasks run one after another, and each one changes the tree the next
was written against, so such a number in a queued spec is false before the
orchestrator reaches it, and the orchestrator cannot execute a spec whose
facts no longer hold. A number met in a spec, a plan or a report is read as
an order of magnitude; one that has gone stale is not a defect to correct,
count again or stop on. Two counts that disagree are not reconciled against
each other; ask which member is missing.

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

**A hand that has compacted holds the order only in substance.** It knows it was compacted — its turn opens "This session is being continued from a previous conversation that ran out of context" — and files it had read survive verbatim, but the order survives only as the summary's gloss, so a text pinned verbatim in the order is lost and the hand composes its own in its place; and it trusts the summary's claim that it re-read the buffer. So after a hand's compact, re-send what the order pinned verbatim and verify the result on the file, never on the report. Observed on a peer's editor; the record is phase 78's note.

## Orientation

**This folder's path lags its governing spec on purpose.** `docs/paired-loop.md` puts a head's folder at `.ai-factory/architects/<slug>/<NN>/`; `architect-editor-engine` still defines the flat `.ai-factory/architects/<NN>/` until phase 76 lands, and the engine is what this head runs on.

**The phase note is the architect's, not the orchestrator's — by design.** `Phase note:` is emitted by `roadmap-outline-deep`, read by `roadmap-decompose` and `task-rescue`, and captured by `roadmap-prune`; no orchestrator prompt reads it. Per 07, the user ruled that a task is complete and self-sufficient and the phase note is for the architect; a spec that names the note gets it read through the planner's walk.

## Ledger

**Orchestrator sources cited from shipped skills, by paths that open nothing.** What: `src/skills/task-rescue/SKILL.md`, in the sentence after the closed set of `step` values, cites `orchestrator/resume.py` and two functions in it; `src/skills/orchestrator-artifacts/SKILL.md` § "Mirrors-the-orchestrator invariant" cites `orchestrator/main.py`, `agents.py`, `prompts/reviewer.md`, `prompts/escalation.md`, `resume.py`. Both load into every project. The fix keeps each invariant in behavioural terms and drops the paths. Why deferred: paused by the user. Trigger: the user's go.

**Escalation does not name a spec that fails to cover the target.** What: `orchestrator/orchestrator/prompts/escalation.md` names "the ratified spec above the current task" as a cause, which covers a fork the spec leaves open but not a spec silent on the behaviour a task names; the ruling under § "Rulings in force" needs it, with the boundary that absence of a pointer is never a cause. Why deferred: left to the orchestrator-side head. Trigger: a run escalating on a missing pointer, or the user's go.

**Pipeline skill descriptions carry neither the docs nor the direction.** What: the `description:` of `roadmap-outline`, `roadmap-decompose`, `task-rescue` and `roadmap-prune` never mention documentation. Why deferred: the user considers the descriptions well written. Trigger: the docs-are-the-ТЗ argument recurring with an agent.

## Candidates — not tasks

**A contract line is still asked for "guards".** Hook (d) no longer asks for them; it now points at the engine's definition. But `roadmap-decompose`'s `description:` says a contract line names "the key files, types, and guards", and `roadmap-engine`'s contract-line template says "key files/types/guards involved". A guard is a fence: the seed's "what a spec holds" excludes it, and `docs/names-and-reasons-not-laws.md` names it as a failure. Since phase 79 the description sits in every session's field. Promoted only on the user's word.

## Current thread

**Pair work with 07**, at the user's word «зови 05 на помощь, дальше работай с ним в паре». 07 decomposes; I read independently and adversarially, report by fact, and hold my reading until 07's exists. The verdict and the order are 07's.
