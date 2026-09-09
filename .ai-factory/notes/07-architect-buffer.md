# Architect buffer — 07

Two zones. **Live** is the architect's own and is not read by the editor: a hand that already holds the head's conclusion returns an echo where an independent reading was wanted. **Settled** is the editor's to hold as its own working context, re-read when it changes. The governing account of this file is [paired-loop](../../docs/paired-loop.md).

---

# Live — the architect's own

## Editor

- Handle: `ad6a88c15b45ee4f5`, agent type `editor`, spawned on the first authored apply work-order.
- It has read `docs/paired-loop.md` as instructions addressed to itself, and holds this file's Settled zone as its own working context. It does not read this Live zone.
- Accumulated: every apply round of specs 106–115, the roadmap through phases 36–37, `docs/paired-loop.md`, the two phase notes; one `REPORT-ONLY` relay of the user's `/task-rescue ::`; two delegated sweeps — the open tasks against the documentation, and the four paired-loop artifacts against the spec.
- It has consumed well over 400k tokens this session, past any window, so it has silently lost early history. Treat its accumulated context as partial, never as a record: a round it handled hours ago may be gone from it while the file it produced is not.

## Pairing role

None assigned; `architect-pairing-engine` not loaded. A second architect works this repository concurrently, reached only through the user — its buffers are `05-` and `06-`, never edited from here.

## Where the work stands

Every task through 35.1 has landed. Seven open tasks: `36.1`–`36.5`, `37.1` and `37.2`, specs `116`–`120`, `122` and `123`, phase notes `114` and `115`, all against the governing spec `docs/paired-loop.md`. `37.3` was withdrawn by the user and its spec deleted; the gap in the numbering stays.

`docs/paired-loop.md` now carries § "How the memory begins, and how it survives" — the buffer's lifecycle, and the only place the recovery trigger is stated. The whole phase is free of position addresses; every task addresses its target by heading, by task number, or by a quotation verified unique against the file.

`36.1` has run once and failed at planning; it is repaired and its plan is held at `planned:1` with the reviews deleted, ready to re-run. The other seven have not been through a readiness pass.

Next in the cycle: `command-pin-gaps` over the eight, then the orchestrator. `roadmap-prune` is optional before either — 35 closed tasks would fold into Features and leave the two phases on a clean map.

## Open deferrals

**Resolved — the buffer's lifecycle is ruled, and three artifacts are behind it.** The ruling is in the Settled zone. What it leaves open is work, not a question: `docs/paired-loop.md` states none of the four moments and is the phase's governing spec, so it moves first; 36.2 is directionally right but unconditional where the ruling is conditional — a continuing architect adopts the buffer the handoff names, only a new one creates — and needs rewriting, not correcting; and two moments belong to no task at all: the editor learning the buffer's path at its spawn, and the handoff as the editor's own recovery carrier after its context ends. The second contradicts `agent-architect`, which today says the digest is never sent to the editor.

**Unresolved design question under Phase 36.** The settled zone holds project-scoped, durable content — discipline, rulings, method — inside a file named and numbered per session. If it is a staging area on the way into the skills, the drain rule covers it and orphaning is tolerable. If it is the pair's durable shared context, which is what telling the editor to hold it implies, it does not belong in a per-session file at all. The two answers lead to different tasks; nothing in 36.1–36.3 settles it.

- **A phase has an internal blast radius and no pass counts it.** Where several tasks of one phase edit the same files, the first to land invalidates the citations the others were grounded in. `command-pin-gaps` reads a task against the code; nothing reads a task against its siblings' pending edits. Found by hand on Phase 36 after the same defect surfaced five times: a spec's grounded section cited a heading, a sentence and a span that an earlier task of its own phase removes. Belongs beside 34.2 as a `command-pin-gaps` concern.
- **A sentence is not a unit of claim.** `agent-architect:235-237` is one sentence carrying three claims whose fates diverge — two close the buffer to the editor and go, one names the architect as its only writer and survives with a new reason. A spec that disposes of "the sentence" disposes of three different things in one word, and the rescue order, the spec and the plan each read it differently. The same error one level up is naming one occurrence of a claim a file states in several places. Both are the same habit: treating a textual unit as if it carried one meaning.
- **No recovery path for the buffer itself — now ruled, still unbuilt.** The skill recovers the *editor's handle* from `meta.json` when no handoff reached the architect, and nothing recovers the *buffer's path*; an auto-compact before any handoff is written orphans it, and a fresh architect cannot tell `07` from `01`–`06`. The ruling settles what happens — no pointer in the handoff means a new architect creating a new buffer, so an orphan is a cost paid once and never a wrong state — and it belongs in the same rewrite 36.2 takes.
- **The processed mark comes back out of `command-handoff`.** Task 31.1 put it in this morning — the mark line in both emitted shapes, the Template-hook exemption that carries it verbatim, and the `## Holding a handoff` body rule built on it. The user has since retired the idea on evidence: agents do not flip it. Removing it is a task against the same file, and the reasoning that put it there is in spec 106 for whoever writes the reversal. *Trigger:* the user says to write it.
- **`note`'s numbering glob cannot see a three-digit file.** Its scan is `[0-9][0-9]-*.md`; in `.ai-factory/specs/trickster77777/` that matches 19 files with a maximum of `99`, while the directory's real maximum is `121`. Followed literally the next number collides with a file already there. Silent — no error, two files sharing a prefix, every later scan compounding it — and `note` is loaded by eight callers, so every destination folder is exposed.
- **`$HANDOFF_LIST` in `roadmap-test-coverage`.** The word carries a second concept there — items handed to `roadmap-decompose`, nothing to do with `.ai-factory/handoffs/`. Not a registry violation: `handoff` is absent from `docs/reserved-words.md`, and that document declares itself final. Task 34.4 set the precedent for removing exactly this collision without breaking that finality. *Trigger:* the user rules on whether the registry admits the genre.
- **One finding still owed to `aif-docs`.** The two handoff genres — continuing the same architect across a compact against handing to a different agent or repository — are named by no document, so neither can become a task until the spec states it. The other finding, the editor's own context ending short of death, is no longer owed: the user has ruled the recovery, and it goes into `docs/paired-loop.md` with the rest of the lifecycle.

---

# Settled — the editor's to hold

## Working discipline

**Standing rule about this section: whenever the user gives feedback on how the architect works, record it here immediately, as settled behaviour — not as an episode.** A ruling that stays in the chat dies with the chat, and the next session repeats the correction.

Keep the chat on substance. Investigation legwork goes to the editor as one `REPORT-ONLY` batch rather than a run of greps in the chat; file writes, scripts included, go as `APPLY-EDIT`. Verification of what landed stays with the architect — that is the layer that caught every discrepancy, including a silent bug in the architect's own analysis script. **The architect** never pastes its raw output into the chat: it states the conclusion in a line. The editor's own reports are the opposite — they carry the raw output to the architect, which is how a wrong expectation is caught, and `editor.md` requires it. A single decisive check is cheaper run directly than relayed.

Until the shared engine holds this file, the editor has no way to notice a change here on its own. The architect names it when the settled zone moves; an unannounced edit reaches nobody.

**The marker and delegation are different axes.** `::` governs whose message crosses the channel: it forwards the *user's* payload for an independent read, and an unmarked user message is never forwarded. Delegating the architect's *own* legwork needs no marker and no permission. When the user's payload is relayed, the editor's agreement is signal and gets reconciled; when the architect's legwork is relayed, there is no second opinion in it — it is a hand, and treating its agreement as corroboration mistakes an echo for evidence.

**The architect writes handoffs, the buffer and rescue reports itself — because it holds the context, not because a rule forbids the hand.** A handoff is the architect's own context, and having something that does not hold it retell it produces an unpredictable result; the same goes for anything the architect authors from its own reading. This is a practice, not a boundary to enforce: the user has ruled that outside the buffer it does not matter whose hand wrote a thing, and a task naming the class was withdrawn on exactly that ground. Everything else goes to the editor by default.

**Taking a memory snapshot on request is a capability of the architect, not a property of any skill.** The user asks for a snapshot and one is written — no command invoked, no template consulted. It is a snapshot precisely because everything durable already lives outside the conversation: the roadmap holds time, the specs hold decisions, this buffer holds the practice. The snapshot carries only the volatile residue — where the work stands, what the hand knows, what will slip first, and what must not be resolved by inference. Written that way it stays short; written as an inventory of the session it is neither short nor a snapshot. Each new one supersedes the last by name, so a reader never follows a stale next action. *This debt is assigned: 36.5 carries it into `agent-architect`, folded in rather than given a task of its own because the sentence it lands in is already rewritten by two tasks of the same phase. Erase this paragraph when 36.5 lands; do not write a second task for it.*

**The pairing is a brush and its fingers, not a specification and its auditor.** The architect supplies meaning, constraint and place; the editor writes the artifact. Pin what a sentence must say and where it goes — not its characters — because a writer with the file open never restates what already stands beside it, and an architect composing replacement text blind does exactly that. What stays is mechanism, not ceremony: anchor by a unique string rather than a position, so two sessions editing one file do not collide; and read the landed result — not to audit the editor, which over a full session never once silently deviated, but to see what the decision looks like once it is real. Every defect that reading caught was the architect's own.

**Fingers explore a surface before anything is written about it, and whoever touched it writes.** A grounded section — what is true now, read from the code with exact values — belongs to the hand that had the file open, not to an architect who compressed a sweep into a claim and passed the claim on. The claim is where the detail dies: a grep showing six hits became "the shape occurs twice" in a spec when the file holds it once, because the output was read and the lines were not. The architect keeps the decision — what must change and why.

The split that governs it: a **factual** question (what does this line say, how many times does this word occur) is best answered by one careful reader who touches and writes, since two summarisers are worse than one; a question of **judgment** (is this task right, does it contradict a doc) needs two independent readings reconciled, and there the independence is the whole point.

**A ruling recorded here is a debt against the skill, not a record of one.** It is erased when it reaches the artifact that should hold it. A buffer that works well as shared context makes it more comfortable to leave rulings in it, so the drain tightens rather than relaxes.

## Rulings, in the user's own terms

- **A handoff is `note` under a lens, nothing more.** "Это просто надстройка над ноутом, как дистиллятором смысла! Мы же не пронизываем все скилы ноутами!" Already the governing position in `docs/sakshi-harness/skill-graph.md`; the skills drifted from the doc.
- **Provenance is not reference.** A document written after reading a handoff is fine; citing it is not.
- **A skill is its own documentation.** `docs/` describes the system; a single skill's behaviour belongs in the skill. Behaviour spanning several artifacts — the paired loop — belongs in `docs/`.
- **A task spec holds three things and nothing else** — what is true now, read from code with exact values; what must be true after, in the code's own terms; what breaks on contact, enumerated.
- **A handoff is a snapshot of memory, and the processed mark is retired.** Where you are, what is in flight, what the durable artifacts do not hold — never an inventory of the session. The mark shipped in the morning and failed by evening: agents refuse to flip it or forget, and handoff 19 sat spent and superseded still reading `[ ]`, unmarked by the architect who superseded it. A rule nobody follows is not a rule. Do not mark, do not expect a mark, read no meaning into the marks already on disk.
- **A task is not an instruction for reviewing itself.** The orchestrator has a department for that. Guards against what nobody would do, and counts that restate the instruction, belong to neither tier.
- **The buffer's life is keyed to the handoff, and the editor is told which buffer is ours.** "Если скилл архитектора спавнится вместе с хэндофом, снапшотом памяти — это значит, буфер уже есть и он прописан в хэндофе. Если в хэндофе нет ссылки на буфер — это новый спавн архитектора и он обязан себе создать сначала новый буфер. Потом создать редактора и записать его имя или айди в буфер. Во время спавна редактору должны сказать — какой буфер наш. Если редактор компактнул свой чат, ему надо снова скормить последний хэндоф-снапшот памяти архитектора." Four consequences: a handoff naming a buffer means adopt, never create; no pointer means create first, before the editor exists; the editor learns the buffer's path at spawn; and the handoff is the editor's recovery carrier too, not the architect's alone.
- **A task explains what an artifact must hold, never where to type it.** "Мы должны объяснять 'в таком-то классе нужны методы такого плана', не надо объяснять на какой строке что написать." The register, not just the addressing: name the artifact and what must be true of it. A line range is the visible form of the same error, and a heading substituted for a line range is only half the repair.

## The discriminator that decides a check

`test-philosophy`, applied one tier up. **Silent failure → check it. Loud failure → do not.** A check that can only fail where the instruction was ignored describes a loud failure: the diff shows it on sight. Dropping a clause from a rationale is silent; not writing a pinned command is loud. A check that cannot fail on this repository at all — that an interpreter counts characters, that a file contains what was just written into it — is not a weak check but not a check.

## Standing method rule

**An expectation in a work-order is scoped to what the order changes — never to the whole file or the whole tree.** Seven violations in one session, three shapes:

- stale state ignored — `git status` pinned as "exactly N entries" while other files were already modified or untracked;
- a count contradicting the order's own guardrail — a phrase counted at zero while the same order preserved a sentence containing it;
- a count that cannot return its number by construction — a phrase the check must restate to check it; an unanchored grep catching the word in prose; plain arithmetic.

Count over the added text, anchor the pattern, or name the pre-existing occurrences in the expectation itself.

**Lifting a constraint means stating what it was protecting.** "Do not trim to stay under the ceiling" removed a number and left no criterion, and the line came back at 1511 code points doing the spec's job — obeyed exactly, and wrong. The number was never the point; the two-tier split was. The same shape appears in a guardrail drawn around a section instead of around a claim: a boundary named without its purpose is followed to somewhere neither of us wanted. Name the purpose and the hand steers by it; name only the edge and it optimizes for whatever is left.

**An edit to a governing spec reaches that phase's note in the same round.** The note states what diverges *now*, measured against the doc; move the doc and the note's measurements are taken from a line that no longer exists. The failure is not staleness but inversion — a note that said something was undocumented on both sides reports the opposite once one side documents it. Two skills read the note in full and unconditionally: decomposition before a phase's first task, and rescue when judging a failure against its second baseline. A rescue reading an inverted note diagnoses against a false baseline and prescribes the wrong repair, which is the most expensive mistake in the cycle. When scoping a round that touches a doc, the phase note is inside the boundary, never outside it.

## Measurements worth keeping

- **Where the pipeline fails:** across three months of run notifications, 91 of 94 failures happen before any code is written — 73 at plan review, 18 at review, 3 at implement. The run-event log seeded from that history is `orchestrator/metrics/runs.jsonl`.
- Rescue reports 02 and 03 diagnose **over**-specification; 04 and 05 diagnose **under**-verification and prescribe more of what 02/03 identified as the disease. Two architects reached the same wrong prescription independently — convergence here is a shared blind spot, not confirmation.
- **Seven tasks landed in a row with no rescue** after the specs were cut back to behaviour, against five rescues over the four tasks before. The sharpest point: a task that had burned six planning rounds and two rescues passed first time once its spec pinned a paragraph's text instead of describing its scope. The run does not separate the cut check lists from the three-part shape — one intervention through several channels.
- `tradeoxy_core`: 31 open tasks, **13** whose spec carries the counting register, 18 clean. In its eight most recent specs — Guards 17%, Tests 13%, Acceptance 5%. The cut is Guards + Acceptance, about 22%. **`## Tests` stays** — tests are a `test-philosophy` deliverable, not review instructions, and an unwary cleanup takes them first.

## Where the skills lag this practice — the drift register

Verified against the files, not assumed:

- **`agent-architect`: "You author your own prompt in exactly one case: the apply work-order"** — false, in the section heading and in the body. The architect also authors `REPORT-ONLY` prompts for its own legwork.
- **`agent-architect` says the editor is never told about the buffer**, and `architect-editor-engine` holds only the two message formats. Phases 36 and 37 close both, against `docs/paired-loop.md`.
- **`agent-architect` states the opposite of the governing spec on the editor's recovery.** Its pre-compact paragraph says the digest of what the editor accumulated is the architect's own note and is never sent to the editor; the governing spec says the snapshot carrying the head across a break carries the hand across its own, handed over whenever the architect rehydrates. This is the loudest lag in the register — not a gap but a contradiction, and until 36.5 lands the skill instructs against the spec it answers to.

## Buffer ownership

`.ai-factory/notes/` in this repository holds only architect buffers, one per session; `05-` and `06-` belong to the other architect and are never edited from here.
