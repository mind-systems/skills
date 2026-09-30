> Owner: trickster77777@gmail.com

# Skills Roadmap

> Generic AI Factory skills — reusable slash-command packages for Claude Code.

## The sweep survives; the tally it wrote does not

### Phase 56 — the blast-radius repair names the rule and the sweep that finds the set, never the tally of what it found

Governing spec: `docs/counts-go-stale.md`

`command-pin-gaps`'s Blast-radius holes clause orders exactly the census `docs/counts-go-stale.md` rules out: an enumeration in a task spec, true when swept and false once a sibling task lands. The same file's Value holes clause already refuses this for a line number, stating the reason a few lines above it — an argument that never reached the clause below. `roadmap-engine`'s own paragraph feeds the same instruction to every caller. Phase note: [the blast-radius repair clause orders the census its own file forbids](.ai-factory/specs/trickster77777/150-the-blast-radius-clause-orders-the-census-the-value-clause-forbids.md)

- [x] **56.1 — the blast-radius repair clause stops ordering the census it forbids** — `command-pin-gaps.md`'s Blast-radius holes `Repair:` sentence orders a `Grep`/`rg` enumeration into the task spec, and its `default:` line repeats it as "sweep enumeration" — both write the census `docs/counts-go-stale.md` forbids. Rewrite both to the rule/sweep/invariant form together (splitting leaves the file self-contradictory); the clause's definition sentence, its blocker sentence, its correct-as-written tail, and Value holes stay untouched. Spec: `.ai-factory/specs/trickster77777/154-the-repair-clause-writes-the-rule-and-the-sweep-not-the-tally.md`. [17m 38s]
- [x] **56.2 — the task-spec-shape root stops feeding the census instruction downstream** — `roadmap-engine/SKILL.md`'s "What a task spec holds" paragraph states *what breaks on contact* as "enumerated rather than hedged", the wording `command-pin-gaps` names as its own clause's derivation source, still read unchanged by eight callers. Reword the third clause to "pinned rather than hedged"; the heading text, first two clauses, and surrounding paragraphs stay byte-identical — `command-pin-gaps` cites the heading by name and it must keep resolving. Spec: `.ai-factory/specs/trickster77777/155-the-root-forbids-the-hedge-without-ordering-the-tally.md`. [9m 29s]

## Nothing in the chain asks whether a kind is carried by a type or a field

### Phase 57 — something in the chain asks what shape a distinction takes, at the moment the second member of a kind arrives

The family selects behaviour by policy injected from the caller — `note`'s hooks, `roadmap-engine`'s four, `test-philosophy`'s one discriminator — yet no skill body requires anything about the shape a distinction takes, and the naming vocabulary describes our own architecture, never the code it plans. The repair is additive, not corrective: put the question where a kind's second member arrives, and the family honours it as faithfully as everything already written. Phase note: [the family requires nothing about the shape a distinction takes, and is built entirely on that shape](.ai-factory/specs/trickster77777/151-the-family-requires-nothing-about-the-shape-a-distinction-takes.md)

- [x] **57.2 — the philosophy unit is built in test-philosophy's shape** — no skill for this exists; the unit's content (question, trigger, exemption, vocabulary) is settled in phase 57's own note and not re-derived here. Change: a new directory `src/skills/polymorphism-philosophy/` holding one SKILL.md — user-invocable, no I/O, load-once — plus a matching symlink into `active/skills/`. Deploys alone; directly invocable per the user's own standing ruling. Spec: `.ai-factory/specs/trickster77777/157-the-philosophy-unit-is-built-in-test-philosophys-shape.md`. [21m 38s]
- [x] **57.3 — the skeleton takes the bead** — `roadmap-decompose-skeleton/SKILL.md`'s Lens 1 justifies a skeleton by testability alone, and its `loads:` line reads `roadmap-engine test-philosophy`. Change: Lens 1 fires on the polymorphism unit's own event — a kind gaining a second member — instead of judging testability; `loads:` gains `polymorphism-philosophy`. Lens 2, Lens 3, and the file's restraint rules stay untouched. Sequenced last — it loads a file 57.2 must create first. Spec: `.ai-factory/specs/trickster77777/158-the-skeleton-takes-the-bead.md`. [16m 54s]

## The state survives the compact; the reasons behind it do not

### Phase 58 — the snapshot carries the stretch's own history, and the series stays readable as one

Governing spec: `docs/paired-loop.md`

The architect's memory snapshot, followed to the letter, still loses what a successor needs most: why one option was taken over another, which premise proved false and how. The rule that a newer snapshot supersedes the last stays correct but unscoped — it should retire the next action, never the record. The file the rule produces is delegable today, and delegation fails: the reasoning lives only in the conversation the architect held, never in what gets handed off. Phase note: [the architect's memory snapshot is a history, not a telegram](.ai-factory/specs/trickster77777/152-the-architects-memory-snapshot-is-a-history-not-a-telegram.md)

- [x] **58.1 — the snapshot carries reasoning, not just residue, and is thick by default** — `src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter": "What a snapshot carries is only the volatile residue..." permits a bare inventory with no reasoning, and the adjoining sentence "Each new snapshot supersedes the last by name..." reads unscoped once the first requires a record to persist. Change: require the stretch's reasoning, state the thickness default — thick by default, thin only when asked or meant as a pointer list — and scope the supersession sentence: only the next action goes stale, the record stands. Per `docs/paired-loop.md`. Touch only these two sentences; 58.2 and 58.4 own the rest. Spec: `.ai-factory/specs/trickster77777/159-the-snapshot-carries-reasoning-and-is-thick-by-default.md`. [15m 30s]
- [x] **58.2 — the snapshot itself, not only its digest, is never delegated to the editor** — `src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter", the sentence ending "the digest is your own recovery note and is never sent to the editor" forbids delegating only the digest, leaving the snapshot file itself unaddressed. Change: append a clause forbidding delegating the snapshot itself to the editor, on the ground already stated for the digest — the conversation is the surface, only the head that held it writes about it — per `docs/paired-loop.md`'s who-writes-it claim; § "Relay on the marker..." states elsewhere what an `APPLY-EDIT` carries with no such exclusion, so it gains one too, or the file argues with itself. Touch only these two sentences. Spec: `.ai-factory/specs/trickster77777/160-the-snapshot-itself-is-never-delegated.md`. [28m 13s]
- [x] **58.4 — a request phrased as a handoff routes correctly on both sides, or on neither** — `src/skills/agent-architect/SKILL.md`'s two-occasions sentence and `src/commands/command-handoff.md`'s opening paragraph together leave "continue this same architect past a break" reachable by the wrong artifact — the boundary exists on neither side alone. Change: append a routing sentence to the two-occasions sentence, and insert one paragraph in `command-handoff.md` after its opening paragraph, before the first `---`, naming the sibling genre as not its own; both cite `docs/paired-loop.md` § "How the memory begins, and how it survives" rather than restating reader, subject, lifetime. `command-handoff.md`'s Steps 1–3 and "Holding a handoff" stay untouched, no thickness policy added; `agent-architect` touches only its own sentence. Spec: `.ai-factory/specs/trickster77777/162-a-handoff-phrased-request-can-mean-the-snapshot.md`. [10m 50s]

## A buffer with no seed reinvents its own shape at every founding

### Phase 59 — a buffer is founded from a seeded template rather than reinvented

Governing spec: `docs/paired-loop.md`

The memory is one thing — the head its only writer, the hand its reader — but nothing states what a newly founded buffer contains, so the pair reinvents the same shape at every founding, by memory rather than from a seeded file that travels with the skill. Phase note: [the buffer is born with a shape](.ai-factory/specs/trickster77777/153-the-buffer-is-born-with-a-shape.md)

- [x] **59.1 — the zone split comes out of the skill files** — `src/skills/architect-editor-engine/SKILL.md` § "The architect's buffer" (frontmatter and body), `src/skills/agent-architect/SKILL.md` (§ "Spawn once, message thereafter" and § "Your buffer is shared; you alone write it"), and `src/agents/editor.md`'s opening paragraph still define or reference the buffer's settled/live split. Change: remove the split from all three, per the user's ruling and `docs/paired-loop.md` § "What the memory holds, and who holds it"; state the two rules that survive — the head is the memory's only writer, the hand reads it in full and never writes to it. `.ai-factory/notes/07-architect-buffer.md` is out of scope. Spec: `.ai-factory/specs/trickster77777/164-the-zone-split-comes-out-of-the-skill-files.md`. [25m 48s]
- [x] **59.2 — the buffer is seeded from a template at founding** — `src/skills/agent-architect/` has no `templates/` directory, and its SKILL.md's buffer-creation paragraph seeds no starting content, so the pair reinvents the same shape at every founding. Change: add `templates/buffer-seed.md` holding the memory's seven rubrics (per this phase's corrected note) plus the counts-rule standing entry in its own words, never a pointer to `docs/counts-go-stale.md`; append one sentence at the paragraph's end naming it read once at founding. Touch only the paragraph's end — 59.1 owns its mid-paragraph clause. Spec: `.ai-factory/specs/trickster77777/165-the-buffer-is-seeded-from-a-template-at-founding.md`. [4m 52s]

## A dead hand stops the skill; permission was never the question

### Phase 60 — a dead hand is remade, not asked about

Governing spec: `docs/paired-loop.md`

The skill treats a dead hand as a stop — reported first, never auto-replayed, respawn waiting on the user — but the ruling makes the hand the head's own: reported in passing, the next message is the new spawn, standing permission. What survives is the cost: a fresh hand holds no round history, so what it is given carries its own ground. Phase note: [a dead hand is remade, not asked about](.ai-factory/specs/trickster77777/166-a-dead-hand-is-remade-without-a-pause.md)

- [x] **60.1 — a dead hand stops being a stop** — `src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" holds a dead editor as a stop: report before anything is sent, a payload never auto-replayed, the respawn waiting on the user. Change: per the ruling and `docs/paired-loop.md`, replace the passage — the death is reported in passing, the next message is the new spawn, standing permission, never asked for; a fresh hand holds no round history, so the next order stays self-contained. `src/agents/editor.md` is untouched — no matching stop. Spec: `.ai-factory/specs/trickster77777/167-a-dead-hand-stops-being-a-stop.md`. [4m 55s]

## The rule that would have prevented it was held by the architect while the architect broke it

### Phase 61 — a spec states what to hold, never a check or a line

Governing spec: `docs/what-a-task-carries.md`

Two of the user's rulings — a task is not an instruction for reviewing itself, and a spec states what to hold, never where to write it — sat in the buffer as debts for weeks; 58.2's rescue paid the cost, three rounds failing inside the verification tasks it produced, the change itself never faulted. Phase note: [a spec states what to hold, never a check or a line](.ai-factory/specs/trickster77777/169-a-spec-states-what-to-hold-never-a-check-or-a-line.md)

- [x] **61.1 — the repair is a mood, not a mechanism** — `command-pin-gaps.md`'s Blast-radius holes Repair sentence orders the invariant as something "every match must satisfy after the change" — an instruction to a later run, exactly what *What the pass never writes* forbids; 58.2's rescue failed three rounds inside the verification tasks this produced, never the change itself. Change: the invariant becomes a recorded finding — what the sweep, run now, reaches — never a check for later; note `138-…`'s Q4 paragraph, quoting the sentence live, updates in the same stroke. Spec: `.ai-factory/specs/trickster77777/168-the-repair-is-a-mood-not-a-mechanism.md`. [3m 43s]
- [x] **61.2 — the three parts exclude a check, a line, and a fence** — `roadmap-engine/SKILL.md`'s **What a task spec holds** paragraph says "three parts and nothing else" but never states what a fourth is not; `docs/what-a-task-carries.md` now states it. Add one sentence: no clause checks that the instruction was carried out, none is a position in the file, and none fences off a neighbour — scope is stated positively, as what the task changes. The heading and its three clauses stay byte-identical; many callers reach it, `command-pin-gaps` among them by name. Spec: `.ai-factory/specs/trickster77777/170-the-three-parts-are-the-whole-and-none-is-a-check-or-a-line.md`. [2m 53s]

## An architect's memory is scattered across folders and found only when handed over

### Phase 62 — each architect lives in a folder of its own

Governing spec: `docs/paired-loop.md`

`architect-editor-engine` places the buffer at `.ai-factory/notes/<NN>-architect-buffer.md`, among every note there; snapshots go to `.ai-factory/handoffs/`, beside project handoffs. The doc gives each head a folder under `.ai-factory/architects/` with its buffer, snapshots, and one address file (session id and name) a peer reads instead of the buffer. Phase note: [each architect lives in a folder of its own](.ai-factory/specs/trickster77777/171-each-architect-lives-in-a-folder-of-its-own.md)

- [x] **62.1 — the engine names the architect's folder as the memory's home** — `architect-editor-engine/SKILL.md` § "The architect's buffer" defines the buffer as a file at `.ai-factory/notes/<NN>-architect-buffer.md`, numbered among the other notes. Define instead the folder `.ai-factory/architects/<NN>/` holding `buffer.md`, `address.md` (two lines, `session-id:` and `session-name:`, read by a peer instead of the buffer) and the head's own `<NN>-<slug>.md` snapshots, the highest number the latest; a new folder takes the highest number plus one. The frontmatter description follows, and so do `CLAUDE.md`'s `.ai-factory/` tree line and its `handoffs/` sentence, which come to name the architects' folders. Spec: `.ai-factory/specs/trickster77777/174-the-engine-names-the-architects-folder-as-the-memorys-home.md`. [4m 4s]
- [x] **62.2 — the architect lives in its folder** — `agent-architect/SKILL.md` has a new head create its buffer at the engine's path, keeps no address, and names no destination for a snapshot. After: § "Spawn once, message thereafter" has a new head found its folder per the engine, seed `buffer.md` from `templates/buffer-seed.md` and write `address.md`; the head reads its session id by a nonce probe of the project's transcripts and its session name from the first line `ListAgents` returns (which joins the skill's `allowed-tools`), and rewrites `address.md` on every start and rehydration; a snapshot is written into its own folder; the recovery passage and § "Your buffer is shared; you alone write it" speak of the folder. Sequenced after 62.1. Spec: `.ai-factory/specs/trickster77777/175-the-architect-lives-in-its-folder.md`. [7m 47s]

### Phase 63 — the architect comes back on a bare invocation

Governing spec: `docs/paired-loop.md`

Rehydration today resumes whichever chat receives a pasted snapshot naming the buffer; the doc keys a folder to the session id, which holds across a compact and a reopened chat and which the head reads itself with no hook, and a chat no folder claims founds its own. Blocked on phase 62. Phase note: [the architect comes back on a bare invocation](.ai-factory/specs/trickster77777/172-the-architect-comes-back-on-a-bare-invocation.md)

- [x] **63.1 — the architect comes back on a bare invocation** — `agent-architect/SKILL.md` decides a start by what the user hands it: a snapshot naming a buffer resumes it, and every snapshot carries the buffer's path. After: § "Spawn once, message thereafter" has the head read its session id (62.2's probe), find the folder under `.ai-factory/architects/` whose `address.md` carries it and work in that folder's `buffer.md` and its latest snapshot when it holds one; with no such folder, found a new head, never asking which; the snapshot stops carrying the buffer's path; the handle-recovery block (the `meta.json` fallback, re-pointing the editor, the two-live-buffers paragraph) goes, the liveness probe and dead-editor rule staying; § "Your buffer is shared; you alone write it" and § "On every invocation" agree. Sequenced after 62.2. Spec: `.ai-factory/specs/trickster77777/176-the-architect-comes-back-on-a-bare-invocation.md`. [6m 7s]

## Two architects negotiate roles nobody uses

### Phase 64 — architects talk without roles

Governing spec: `docs/paired-loop.md`

`architect-pairing-engine` splits two architects into deciding and applying halves, the user as courier. Two heads worked by talking directly, each in its zone — the user ruled it pointless. The phase retires the skill, its symlink, every pairing mention in `agent-architect`; drops it from `CLAUDE.md`'s two lists; gives `agent-architect` the doc's peer account. Blocked on phase 62. Phase note: [architects talk without roles](.ai-factory/specs/trickster77777/173-architects-talk-without-roles.md)

- [x] **64.1 — `agent-architect` drops the roles and gains the peer account** — `agent-architect/SKILL.md` still speaks of a pairing role, a deciding or applying half and a paired architect, and says nothing of working with a peer. After: every such place goes or speaks of the editor alone — the `loads:` line, the role-recording passage in § "Spawn once, message thereafter", § "Nothing closes a round before the report on it exists", § "Verify the report by fact", § "Your buffer is shared; you alone write it" — and a short section, "Working with another architect", holds the peer account: `SendMessage` at the session name `address.md` holds, approval in each chat, hold then reconcile, verify by the files, ask rather than read, no roles. Sequenced after 63.1. Spec: `.ai-factory/specs/trickster77777/177-agent-architect-drops-the-roles-and-gains-the-peer-account.md`. [6m 6s]
- [x] **64.2 — the pairing engine is retired** — after 64.1 nothing loads `architect-pairing-engine`, yet `src/skills/architect-pairing-engine/`, the symlink `active/skills/architect-pairing-engine`, and the skill's name in `CLAUDE.md`'s active set and in its "Everything else in `src/skills/` is ours" list under § "Upstream Sync" remain. Remove the directory and the symlink, and the name from both lists; the lists stay, each without it. A sweep of `src/`, `docs/`, `active/` and `.ai-factory/ARCHITECTURE.md` finds no other live claim, and the one Features row there records a past build. Sequenced after 64.1. Spec: `.ai-factory/specs/trickster77777/178-the-pairing-engine-is-retired.md`. [3m 8s]

## The last clean-up of counts and positions left skills still asking for them

### Phase 65 — a skill asks for a name and a decision, never a line or a measurement

Governing spec: `docs/counts-go-stale.md`, `docs/reference-by-name.md`, `docs/what-a-task-carries.md`

Docs address by name (`reference-by-name`), write what produces a measurement, not the measurement (`counts-go-stale`), keep a check out of a spec (`what-a-task-carries`). Skills ask otherwise: a phase-note directive wants a `file:line`, the seed a dated measurement and no spec rule, the prune handoff a line, the gap pass a line or a count. Phase note: [the skills still ask for a line and a measurement](.ai-factory/specs/trickster77777/179-the-skills-still-ask-for-a-line-and-a-measurement.md)

- [ ] **65.1 — the phase-note directive names a file and a heading, never a line** — `src/skills/roadmap-outline-deep/SKILL.md` § "Step 1: Write the phase note" passes `note` a **Verbosity directive** asking for "a `file:line` where a claim needs one"; a phase note written under it grounds a claim by a line number, which `docs/reference-by-name.md` calls a defect report against its target. Change: the clause becomes a request that a claim resting on a file name that file and the heading, symbol or quoted fragment that holds it, never a line number; the sentence pinned verbatim in the spec. `note` reads the directive as free text, so no caller follows its wording. Spec: `.ai-factory/specs/trickster77777/180-the-phase-note-directive-names-a-file-and-a-heading-never-a-line.md`.
- [ ] **65.2 — the buffer seed states the counts rule as a decision and a producer** — `src/skills/agent-architect/templates/buffer-seed.md`, `## Method`, holds the standing entry "the counts rule" in the words "Keep a contract, delete a census" and "Date a measurement instead of asserting it as permanent" — the account `docs/counts-go-stale.md` has left: a decision stays, a measurement of the current tree goes, dated or not, and what produces it is written. Change: the entry says that in its own words, pinned verbatim in the spec, with no pointer to the doc; the contract and census vocabulary and the dating sentence go, and the entry adds why a spec least of all carries such a number: the specs queued behind a running task age before the orchestrator reaches them. A buffer founded from the old seed holds a copy of the old entry, a record. Spec: `.ai-factory/specs/trickster77777/181-the-seed-states-the-counts-rule-as-a-decision-and-a-producer.md`.
- [ ] **65.3 — the prune handoff names the review file, not the entry's line** — `src/skills/roadmap-prune/SKILL.md` § "Step 0 — Deferred-observations gate": the item that stops on an unpinned entry names the resolution, whose first part has the handoff carry the "`file:line` of the entry" — a line that points elsewhere once the review file changes before the handoff is read. Change: the handoff carries the review file the entry sits in, which with the entry's original reviewer text finds it; the pinned sentence is in the spec. The chat line the item prints just before, `<file>:<line> — <entry text>`, stays as it is. No other file reads a line from the handoff. Spec: `.ai-factory/specs/trickster77777/182-the-prune-handoff-names-the-review-file-not-the-entrys-line.md`.
- [ ] **65.4 — the gap pass stops suggesting a line or a count** — `src/commands/command-pin-gaps.md` suggests a position or a tally in three sentences, against its own **Value holes** repair ("never a line number") and `docs/counts-go-stale.md`: the walk paragraph ends each behavior "at a `file:line` landing in the code"; the **Meaning holes** repair asks for "citing the code that grounds it"; the **Blast-radius holes** repair has a too-large sweep report "the search and its count". Change: the landing and the grounding code are each named as a file and the named thing inside it, and the too-large sweep is reported as its search, with no number; the three sentences are pinned verbatim in the spec. The scan line `[file:line|spec-location]` is chat output, and the rule, sweep and finding form stands. Spec: `.ai-factory/specs/trickster77777/183-the-walk-lands-on-a-file-and-a-named-thing.md`.
- [ ] **65.5 — the seed carries what a spec holds** — `src/skills/agent-architect/templates/buffer-seed.md`, `## Method`, holds one standing entry, the counts rule, and nothing on what a spec holds, though the head re-reads its buffer all session and a skill is read once and fades. The rule lives in `roadmap-engine`'s **What a task spec holds** and in `docs/what-a-task-carries.md`; an architect whose session held the engine's new text still wrote guard and acceptance sections into specs, from a habit in its buffer. Change: `## Method` gains a second standing entry after the counts rule, in the same shape, pinned verbatim in the spec: a spec states what is true now, what must be true after and what breaks on contact, and nothing else — no check, no position, no fence — with no pointer to a doc or a skill. Sequenced after 65.2, since both edit `## Method`. Spec: `.ai-factory/specs/trickster77777/185-the-seed-carries-what-a-spec-holds.md`.

## The behaviour an architect must keep holding lives in a file it reads once

### Phase 66 — the skill gives birth to the architect, the buffer is its ROM

Governing spec: `docs/paired-loop.md`

The skill is read once and forgotten a few messages on; the buffer is read, edited and re-read all session, so the behaviour an architect must keep holding lives there, and the seed carries it into every new buffer. The seed holds the buffer's shape and one entry. Decomposition waits until every task above has landed. Phase note: [the skill gives birth, the buffer is the ROM](.ai-factory/specs/trickster77777/184-the-skill-gives-birth-to-the-architect-the-buffer-is-its-rom.md)

---STOP---

## A number written into a folder that never used one

### Phase 41 — the width `note` writes follows the folder it writes into

`note` writes a fixed four-digit width into every destination regardless of what it already holds, and every destination on disk today is narrower and unpadded. This is the gate for phase 47: `roadmap-outline-deep`'s "Invoke `note` only for a phase that has no pointer yet" cannot be followed for a first note without corrupting the folder it lands in. Phase note: [the width is fixed where the folders are not](.ai-factory/specs/trickster77777/135-note-width-against-its-destinations.md)

## A wrong number reads exactly like a right one

### Phase 42 — the always-loaded rule names a section number as a position address

Governing spec: `docs/reference-by-name.md`

A session cited a governing document's section by number, consistently and wrongly — the rule it pointed at lived one section over — and the mis-citation propagated into contract lines, task specs, a handoff, and a shared buffer before a fresh read against the document caught it. Nothing had been renumbered; the number simply resolved to the wrong place. Phase note: [the number resolves, and resolves wrongly](.ai-factory/specs/trickster77777/136-a-number-is-not-the-name-beside-it.md)

## The pass answers for one task and is pointed at a roadmap

### Phase 43 — the gap pass runs on one task, and finding nothing is an outcome

`command-pin-gaps` walks one task at a time — its deciding question asks whether the run, holding this task and nothing else, would have to invent — yet its own targeting permits a phase or the whole open roadmap as one invocation, with nothing saying whether the walk repeats per task or runs once over all of them. A hole one task's context closes goes unseen when several are read together, and the file never says so. Phase note: [the unit is fixed for the walk and open for the call](.ai-factory/specs/trickster77777/137-the-unit-is-fixed-for-the-walk-and-open-for-the-call.md)

## Four questions the pass does not ask

### Phase 44 — the walk asks the four questions the run found it was not asking

Four questions the gap pass never asks share one shape: a verification signal — a green suite, a satisfied-looking requirement, a confirmed quote, a passing build — is trusted as proof exactly where it is compatible with the defect standing. They part at the layer the witness sits on, landing in three homes: `test-philosophy`'s own discriminator, `command-pin-gaps`' walk, and its blast-radius sweep. Phase note: [four witnesses, each trusted where it is blind](.ai-factory/specs/trickster77777/138-four-witnesses-each-trusted-where-it-is-blind.md)

## Every question in the chain looks for what is missing

### Phase 46 — something asks whether a task claims more than its defect requires

This phase is blocked on two rulings, not one: whether a task claiming more than its defect needs a new rule at all, and whose it is; and where a spec's re-decided, already-ratified answer gets caught, given that no independent reader between drafting and the orchestrator is guaranteed to hold the governing document. If the two answers name different homes, this is two phases. Phase note: [two subtractions that arrived together](.ai-factory/specs/trickster77777/140-two-subtractions-that-arrived-together.md)

## A note written after the tasks takes their shape

### Phase 47 — the phase note describes the diverging ground, never the task set

A phase note describes the area of code that diverges and names the documentary surface where one exists; task keys never appear in it, because the contract line is a task's only home. The failure this phase names — one entry per task — is not reproducible on this repository's own two notes, both of which already hold that shape; the evidence is foreign, from elsewhere. The template presupposes a document to measure against, with an escape hatch for when none exists. Phase note: [what the note describes, and what the skill presupposes](.ai-factory/specs/trickster77777/141-what-the-note-describes-and-what-the-skill-presupposes.md)

## The rule discourages the most productive round in the loop

### Phase 48 — an echo is about the verdict, not about whose question it was

Governing spec: `docs/paired-loop.md`

The variable that decides an echo is whether a second, independently produced reading exists — not who asked. § "The user's marker" keys on origin alone; § "Where the split falls" keys on independence and leakage. `agent-architect` inherits the doc's imprecision word for word; the spec never states the round-closing rule it names as its own section. Phase note: [whether a second reading exists at all](.ai-factory/specs/trickster77777/142-two-readings-or-one.md)

## The buffer's definition describes a use it outgrew

### Phase 49 — the shared memory says what it is actually for

Governing spec: `docs/paired-loop.md`

The buffer's file is numbered per architect, one per session; the memory it holds is project-wide discipline, rulings and method. Nothing bridges the two when a head ends with no snapshot. This phase decides which gives way: a staging area the drain rule covers, or durable shared context the file cannot yet hold. Phase note: [the container is per head, and the content is not](.ai-factory/specs/trickster77777/143-the-container-is-per-head-and-the-content-is-not.md)

## The docs describe skills that have since moved

### Phase 50 — the documentation catches up with what the skills now do

Nine deferred observations across phases 26–30 describe skills that have moved since the doc was written: `skill-graph.md`'s caller count, four separate gaps in `skill-cycle.md`, `multiuser-roadmaps.md`'s spec-dir description, and two omissions in the global CLAUDE.md. Direction runs docs → roadmap → code; here the code moved first and nothing carried the docs forward with it. Phase note: [the documentation catches up with what the skills now do](.ai-factory/specs/trickster77777/144-the-docs-catch-up-with-the-skills.md)

## The rescue path carries its own unrepaired defects

### Phase 51 — task-rescue and the artifact protocol close their own gaps

Six deferred observations against `task-rescue` and the artifact protocol survived their own tasks' guarded boundaries: a sidecar write site still using the wrong path for a named roadmap, a body over the line bound, two small gaps in the marker grammar's writer attribution, a stale path shorthand, and an unstated ban on hand-composing. None blocked its own task; none closed itself either. Phase note: [task-rescue and the artifact protocol close their own gaps](.ai-factory/specs/trickster77777/145-task-rescue-and-the-artifact-protocol.md)

## The coverage pass has leftovers no phase claimed

### Phase 52 — roadmap-test-coverage's remaining observations

Governing spec: `docs/test-coverage-pass.md`

`roadmap-test-coverage` leaves observations no later phase claimed: a spec's now-pruned overstatement of what `aif` mandates for `$TEST_CMD`, checked fresh against the skill it described; and two residues in the test-plan template — a note titled by the area it was called before research, and a template that spawns its sole writer as a possibly read-only agent. Phase note: [roadmap-test-coverage's remaining observations](.ai-factory/specs/trickster77777/146-roadmap-test-coverage-leftovers.md)

## Sentences in the skills still describe what earlier phases retired

### Phase 53 — the skill bodies stop describing retired shapes

Seven sentences a landed task's own removal orphaned: `roadmap-outline-deep`'s justification for its pointer now paraphrases a narrowed grant more loosely than the grant reads; a coupling declared on one side only; `roadmap-decompose` and `roadmap-engine` disagreeing about a task spec's parts; and two skill bodies whose descriptions still assert what their own bodies no longer do. Phase note: [the skill bodies stop describing retired shapes](.ai-factory/specs/trickster77777/147-sentences-that-outlived-their-shape.md)

## The registry is final and meets words it does not hold

### Phase 54 — three concepts without a registry entry

Governing spec: `docs/reserved-words.md`

Blocked on the user's ruling whether a registry that declares itself final admits an entry. Three concepts recur in skill bodies with no home in `docs/reserved-words.md` § "Paired loop": the deciding and applying halves, named twice over; second reader, named once; work-order, defined only by implication inside another entry. Phase note: [three concepts without a registry entry](.ai-factory/specs/trickster77777/148-three-words-the-registry-does-not-hold.md)

## The pairing's second half was never fully wired

### Phase 55 — the pairing engine and the editor's licence

Governing spec: `docs/paired-loop.md`

Blocked on the user's ruling — the reviewer names handoff 08 as where the question was parked. `architect-pairing-engine`'s own text still carries a fourth carrier of the own-hands model it purged elsewhere, the correction licence's trigger for an outright-wrong order was cut along with its power, and the editor's gloss for `APPLY-EDIT` does not anticipate an order decided one architect upstream. Phase note: [the pairing engine and the editor's licence](.ai-factory/specs/trickster77777/149-the-pairing-engine-and-the-editors-licence.md)

---STOP---
