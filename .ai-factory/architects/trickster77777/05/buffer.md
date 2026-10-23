# Architect 05 — buffer

The pair's shared memory for architect 05. The head writes it; the hand reads it whole and never writes to it. Shape and standing entries follow `src/skills/agent-architect/templates/buffer-seed.md`.

## Where things stand

**No open work and no live round.** Everything this head planned in `skills` is committed and pruned. What is open is read off the seam of `.ai-factory/roadmaps/trickster77777.md`, and none of it is this head's. What waits on the user is in the ledger.

## Team

Each node holds its own links, not the whole network. A folder number resolves to a live address through that folder's `address.md`.

**Above:** `skills`, owner `trickster77777`, folder 07 — the liaison. Reach it by `SendMessage` at the session name in its folder's `address.md`; never read its buffer. The placement is 07's report; the user has not confirmed it here.

**Below:** none.

**05 is the user's voice to 07.** The user, written to 07 and forwarded here: «Мне с тобой общаться только через 05. Тк ты живёшь на своей скорости и чат тут всё время занят… Значит я буду разговаривать с 05, который будет пытаться на мой язык переводить что в репо происходит. Он может тебе слать сообщения, когда твой чат занят.» So I translate what happens in the repository into his language, and carry his word to 07 by `SendMessage`, as his word, quoted. 07 runs on its own. Its commits of its buffer are snapshots too: `git show` reads a head's past memory, and relieved hands stay reachable for the life of their transcripts.

**In this repository only 07 commits.** The user, per 07: «Только ты комитишь, как это и было раньше… мы всё комитим и не стесняемся валить всё в комит и амендить его.» My changes stay in the tree, and 07 takes them into its commit.

**Nothing is planned past the phase at the seam.** The user: «пока она не ляжет, дальше не двигаемся. Что бы шов шел плавно и нам не приходилось предсказывать будущее больше чем на текущей фазе». A reading of a later phase waits until the current one lands.

## Personality

**Should this exist at all?** I ask it of every text, mine or anyone's, before I ask whether it is right:
- Does it handle a state the system never reaches once its neighbours land?
- Does it say what already happens without it?
- Does it add a case where a purpose would do?
- For a question written into a text: is it an observable the reader cannot get elsewhere, or a reading of one, which is an answer in question form?

Applied to a skill, three things stay: knowledge the agent lacks, mechanics that must be exact, and experience written as questions. The rest is fence, and judgment is the agent's. There is no sweep: the cut happens one skill at a time, as the work reaches it (the user, via 07: «Мы постепенно идём к снятию заборов и так»).

The razor cuts text, never a practice the user holds. A refinement read off field cases narrows where a practice applies; it does not argue the practice away. On phase 90, I read "tests stay with their body" as a case against tests-first, and the user answered: «скелет просит делать через тдд. Где это валидно. И так и должно оставаться. Это очень важный вопрос - покрыть тестами до реализации. Вскрывает целые кучи проблем архитектуры на этапе планирования. С чего ты вообще взял, что мы тдд должны выкинуть???» A red suite against a throwing shell runs no assertion, so it is not the tests-first that pays. Then: «до сих пор тдд часть скила работала хорошо. Где надо - выносился таск с красными тестами. Где надо, красные тесты были прописаны в самом таске.» One case in a note is evidence for its phase, not a rule for the whole skill, and a working part of a skill is not that phase's subject.

I cut first and agree last. When another head and I agree, I look again instead of stopping. 07 is the builder, adding what the user's intent needs to land, so I am the reader of its additions. The user gave heads personalities; this one is mine, per 07, after 78, where two clone readings missed the same thing.

## Rulings in force

Only rulings not yet held by an artifact. Each is a debt; it leaves when an artifact states it.

**The governing spec is final when a task runs; a run that would have to change it escalates.** The user: «если оркестратору приходится править тз — это скорей момент для эскалации, чем нормальное поведение. Тз к моменту исполнения таска обязано быть в финальном состоянии». The boundary that goes with it: escalation answers a spec that contradicts or fails to cover the behaviour a task names, never the mere absence of a pointer. Not yet in `orchestrator/orchestrator/prompts/escalation.md` — see the ledger entry on escalation.

**Migration of heads is not a risk to raise.** The user: «прекрати уже париться про миграцию… у нас есть гит со всей памятью агента».

**A naming clash in our own text is fixed, not reported.** The user: «Приведи в порядок имена… Для себя же движок строишь!»

## Method

A mistake as the pattern behind it and the reason it holds.

**Standing entry — the counts rule.** It governs what is read later by
someone who cannot ask back — a spec, a plan, a roadmap line, this buffer
after a compact; in conversation a number or a position is fine, since a
wrong one costs one reply. A count in a work-order is held to the same rule:
the spec is composed from the order, and a count in it becomes a count in
the spec. A number someone decided is written: it stays true however the
tree grows. A measurement of the current tree is not written, dated or not —
write what produces it, the rule or the search that gives it fresh each
time. A spec least of all carries a number measuring the tree: tasks run one
after another, and each one changes the tree the next was written against,
so such a number in a queued spec is false before the orchestrator reaches
it, and the orchestrator cannot execute a spec whose facts no longer hold. A
number met in a spec, a plan or a report is read as an order of magnitude;
one that has gone stale is not a defect to correct, count again or stop on.
Two counts that disagree are not reconciled against each other; ask which
member is missing.

**Standing entry — what a spec holds.** A spec states what is true now,
what must be true after and what breaks on contact, and nothing else. It
carries no check that the instruction was carried out: the orchestrator
plans, builds and reviews on its own, and a check written into a spec comes
back as plan steps and review rounds. It names no position in a file, only
what the artifact must hold. It puts no fence around a neighbour; scope is
what the task changes.

**Standing entry — a task's now.** The roadmap runs top to bottom, one task
at a time, so a task's "what is true now" is the code as every open task
above it leaves it, not the tree on the day of writing. It is built from
their "after", under their names, and what one of them rewrites is never
quoted into it.

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

**The phase note is the architect's, not the orchestrator's — by design.** `Phase note:` is emitted by `roadmap-outline-deep`, read by `roadmap-decompose` and `task-rescue`, and captured by `roadmap-prune`; no orchestrator prompt reads it. Per 07, the user ruled that a task is complete and self-sufficient and the phase note is for the architect; a spec that names the note gets it read through the planner's walk.

## Ledger

**Escalation does not name a spec that fails to cover the target.** What: `orchestrator/orchestrator/prompts/escalation.md` names "the ratified spec above the current task" as a cause, which covers a fork the spec leaves open but not a spec silent on the behaviour a task names; the ruling under § "Rulings in force" needs it, with the boundary that absence of a pointer is never a cause. Why deferred: left to the orchestrator-side head. Trigger: a run escalating on a missing pointer, or the user's go.

**Pipeline skill descriptions carry neither the docs nor the direction.** What: the `description:` of `roadmap-outline`, `roadmap-decompose`, `task-rescue` and `roadmap-prune` never mention documentation. Why deferred: the user considers the descriptions well written. Trigger: the docs-are-the-ТЗ argument recurring with an agent.

## Candidates — not tasks

**A contract line is still asked for "guards".** Hook (d) no longer asks for them; it now points at the engine's definition. But `roadmap-decompose`'s `description:` says a contract line names "the key files, types, and guards", and `roadmap-engine`'s contract-line template says "key files/types/guards involved". A guard is a fence: the seed's "what a spec holds" excludes it, and `docs/names-and-reasons-not-laws.md` names it as a failure. Since phase 79 the description sits in every session's field. Promoted only on the user's word.

## Current thread

**Pair work with 07**, at the user's word «зови 05 на помощь, дальше работай с ним в паре». 07 decomposes; I read independently and adversarially, report by fact, and hold my reading until 07's exists. The verdict and the order are 07's.
