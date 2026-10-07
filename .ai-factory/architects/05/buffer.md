# Architect 05 — buffer

The pair's shared memory for architect 05. The head writes it; the hand reads it whole and never writes to it. Shape and standing entries follow `src/skills/agent-architect/templates/buffer-seed.md`.

## Where things stand

*2026-10-01 — rewritten at the migration into this folder.*

*2026-10-07, after a compact:* rehydrated from this buffer and snapshot 13. The probe matched one transcript, so `address.md` is unchanged. The counts standing entry was refreshed from the seed's text.

*2026-10-07:* at 07's request, this head gave an independent review of phase 77 and reported to 07 without writing anything; see § "Current thread".

**This head was idle from 2026-09-09 to 2026-10-01** and holds no live round. It was woken by the user to move its memory into `.ai-factory/architects/05/` and bring the buffer current.

**The migration, done by hand and committed by the user in `7b375e1`:** the buffer moved from `.ai-factory/notes/05-architect-buffer.md` to this file; the one memory snapshot this head wrote, `12-phase-note-and-the-transformation-walk.md`, moved in beside it, its pointer to the buffer repointed here; `address.md` written — `session-id: e0bf20a8-9c9c-4e92-bd30-aa6568e01ab9`, `session-name: skills-eb`, the id read by probe (exactly one transcript matched). Handoffs 09, 10, 11, 13 also name the old buffer path but stayed in `.ai-factory/handoffs/`: 09, 10 and 13 were written by other heads and mention it only from outside; 11 was written by this head but is a project handoff for a reviewer, not a memory snapshot.

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

**A task's "what is true now" is the code as every open task above it leaves it.** The user, through 07: «да не только в фазе! роадмап в принципе так устроен. У меня в голове не укладывается, что это надо объяснять!» What a predecessor rewrites is never quoted into a later task. Drains into the seed as a standing entry when phase 77's task "a task's now" lands; `docs/what-a-task-carries.md` § "What a spec holds" already says it.

**The hand is replaced quietly, inside a window.** The user, through 07: the window runs from half the hand's context, a firm floor, to four fifths, a soft mark, and the head picks the seam between them, «без фанатизма»; the replacement is named in one line in passing, never with token counts, forecasts or a question — «архитектор начнёт ебать мне мозги компактом редактора» is what to avoid. The hand writes its own snapshot and a new hand starts from the buffer plus that snapshot. Drains when phase 78 (note `.ai-factory/specs/trickster77777/0215-…`) lands in the skills.

**The head's and the hand's snapshots live apart.** The user, through 07: separate folders `architect/` and `editor/` inside the head's folder, «что б память не смешивалась». Not yet the engine's layout — `architect-editor-engine` still keeps snapshots at the folder's root — so this folder's snapshot stays where it is until phase 78 lands.

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

**This buffer's history before the folder** is not here; it is `git show 96ffb4c:.ai-factory/notes/05-architect-buffer.md` — the round-by-round record of 2026-09-04 to 09-09. Two heads wrote into that file under the same number: the session that founded it, and a later continuation that rehydrated from it. The pairing roles both of them recorded are gone: `architect-pairing-engine` no longer exists in `src/` or `active/`, and `docs/paired-loop.md` § "Working with another architect" states there are no roles.

**Editor.** No editor is live for this head now. The old record names two handles, `ab8b2f1a1b98a601b` and `aa73188f9b856545e`; the next channel-message is the only liveness probe, and whichever hand receives it must be told this buffer's new path, `.ai-factory/architects/05/buffer.md`, in that same message.

**This folder's path lags its governing spec on purpose.** `docs/paired-loop.md` already puts a head's folder at `.ai-factory/architects/<slug>/<NN>/`; `architect-editor-engine` still defines the flat `.ai-factory/architects/<NN>/` until phase 76 lands. The engine is what this head runs on, so the folder stays flat until then. The phase's note says the user moves existing heads by hand, as with the first migration; a head never moves its own folder on its own initiative.

**The phase note is the architect's, not the orchestrator's — by design.** In `skills` the `Phase note:` pointer is emitted by `roadmap-outline-deep`, read by `roadmap-decompose` and `task-rescue`, and captured by `roadmap-prune`. No orchestrator prompt reads the pointer on a phase header, and that is intended: per 07, the user ruled on 2026-09-24 that a task is complete and self-sufficient and the phase note is for the architect; a spec that names the note gets it read through the planner's walk along named edges. A reader who assumes the run sees the header pointer is wrong.

## Ledger

**Orchestrator sources cited from shipped skills, by paths that open nothing.** What: `src/skills/task-rescue/SKILL.md`, in the sentence after the closed set of `step` values, cites `orchestrator/resume.py` and two functions in it; `src/skills/orchestrator-artifacts/SKILL.md` § "Mirrors-the-orchestrator invariant" cites `orchestrator/main.py`, `agents.py`, `prompts/reviewer.md`, `prompts/escalation.md`, `resume.py`. Both load into every project. The fix keeps each invariant in behavioural terms and drops the paths — the invariant is real, only the pointer is wrong. Why deferred: paused by the user while pin-gaps work was in flight. Trigger: the user's go; the pin-gaps work it waited on is long done. Confirmed on the files by 07 as well.

**Escalation does not name a spec that fails to cover the target.** What: `orchestrator/orchestrator/prompts/escalation.md` names "the ratified spec above the current task" as a cause, which covers a fork the spec leaves open but not a spec silent on the behaviour a task names; the user's ruling under § "Rulings in force" needs it, with the boundary that absence of a pointer is never a cause. Why deferred: left to the orchestrator-side head in a handoff there. Trigger: a run escalating on a missing pointer, or the user's go.

**Pipeline skill descriptions carry neither the docs nor the direction.** What: the `description:` of `roadmap-outline`, `roadmap-decompose`, `task-rescue` and `roadmap-prune` never mention documentation. Why deferred: the user considers the descriptions well written. Trigger: the docs-are-the-ТЗ argument recurring with an agent.

*Closed:* both deferrals against `docs/reserved-words.md` — the file is declared final; the reference-by-name handoff into `tradeoxy_core` — its `RULES.md` carries no position rule now; the orchestrator not reading `Phase note:` — by design, the user's ruling of 2026-09-24 as 07 reports it; copy-or-link for a task spec — drained: `src/commands/command-pin-gaps.md` itself says a task spec repeating a paragraph from a document is not a finding, and the global "never a copy" sits under § "Documentation style", governing docs.

## Candidates — not tasks

**`roadmap-decompose` hook (d) asks a spec for "guards".** Its list — what exists, the exact change, files/types/methods to touch, guards — asks for a fence the seed's "what a spec holds" excludes and that `docs/names-and-reasons-not-laws.md` names as a failure. Outside phase 77's sources by agreement with 07. Promoted only on the user's word.

## Current thread

**Phase 77, reviewed as 07's second reader — reconciled, verdict carried by 07.** 07 conceded the sweep "run now" (put to the user as his ruling, since its repair reaches every spec's Finding paragraph), the work-order sentence's overreach, both chain breaks, the phase stating half its sources, and "Sequenced after". I conceded that "…pinned verbatim in the spec" has a job: it tells the planner the text is contract text. Left to the user: the engine's "implementer" against the doc's "planner". Raised late and agreed: in pin-gaps the value-hole repair should lean on the walk sentence rather than restate the now-clause with an unanchored "it". If the user's ruling changes what the blast-radius task does, the pin-gaps walk task's now is rebuilt from the new after, not patched. Nothing of mine to apply; the order is 07's.
