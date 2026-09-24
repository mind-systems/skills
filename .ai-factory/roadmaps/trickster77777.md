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
- [ ] **58.4 — a request phrased as a handoff routes correctly on both sides, or on neither** — `src/skills/agent-architect/SKILL.md`'s two-occasions sentence and `src/commands/command-handoff.md`'s opening paragraph together leave "continue this same architect past a break" reachable by the wrong artifact — the boundary exists on neither side alone. Change: append a routing sentence to the two-occasions sentence, and insert one paragraph in `command-handoff.md` after its opening paragraph, before the first `---`, naming the sibling genre as not its own; both cite `docs/paired-loop.md` § "How the memory begins, and how it survives" rather than restating reader, subject, lifetime. `command-handoff.md`'s Steps 1–3 and "Holding a handoff" stay untouched, no thickness policy added; `agent-architect` touches only its own sentence. Spec: `.ai-factory/specs/trickster77777/162-a-handoff-phrased-request-can-mean-the-snapshot.md`.

## A buffer with no seed reinvents its own shape at every founding

### Phase 59 — a buffer is founded from a seeded template rather than reinvented

Governing spec: `docs/paired-loop.md`

The memory is one thing — the head its only writer, the hand its reader — but nothing states what a newly founded buffer contains, so the pair reinvents the same shape at every founding, by memory rather than from a seeded file that travels with the skill. Phase note: [the buffer is born with a shape](.ai-factory/specs/trickster77777/153-the-buffer-is-born-with-a-shape.md)

- [ ] **59.1 — the zone split comes out of the skill files** — `src/skills/architect-editor-engine/SKILL.md` § "The architect's buffer" (frontmatter and body), `src/skills/agent-architect/SKILL.md` (§ "Spawn once, message thereafter" and § "Your buffer is shared; you alone write it"), and `src/agents/editor.md`'s opening paragraph still define or reference the buffer's settled/live split. Change: remove the split from all three, per the user's ruling and `docs/paired-loop.md` § "What the memory holds, and who holds it"; state the two rules that survive — the head is the memory's only writer, the hand reads it in full and never writes to it. `.ai-factory/notes/07-architect-buffer.md` is out of scope. Spec: `.ai-factory/specs/trickster77777/164-the-zone-split-comes-out-of-the-skill-files.md`.
- [ ] **59.2 — the buffer is seeded from a template at founding** — `src/skills/agent-architect/` has no `templates/` directory, and its SKILL.md's buffer-creation paragraph seeds no starting content, so the pair reinvents the same shape at every founding. Change: add `templates/buffer-seed.md` holding the memory's seven rubrics (per this phase's corrected note) plus the counts-rule standing entry in its own words, never a pointer to `docs/counts-go-stale.md`; append one sentence at the paragraph's end naming it read once at founding. Touch only the paragraph's end — 59.1 owns its mid-paragraph clause. Spec: `.ai-factory/specs/trickster77777/165-the-buffer-is-seeded-from-a-template-at-founding.md`.

## A dead hand stops the skill; permission was never the question

### Phase 60 — a dead hand is remade, not asked about

Governing spec: `docs/paired-loop.md`

The skill treats a dead hand as a stop — reported first, never auto-replayed, respawn waiting on the user — but the ruling makes the hand the head's own: reported in passing, the next message is the new spawn, standing permission. What survives is the cost: a fresh hand holds no round history, so what it is given carries its own ground. Phase note: [a dead hand is remade, not asked about](.ai-factory/specs/trickster77777/166-a-dead-hand-is-remade-without-a-pause.md)

- [ ] **60.1 — a dead hand stops being a stop** — `src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" holds a dead editor as a stop: report before anything is sent, a payload never auto-replayed, the respawn waiting on the user. Change: per the ruling and `docs/paired-loop.md`, replace the passage — the death is reported in passing, the next message is the new spawn, standing permission, never asked for; a fresh hand holds no round history, so the next order stays self-contained. `src/agents/editor.md` is untouched — no matching stop. Spec: `.ai-factory/specs/trickster77777/167-a-dead-hand-stops-being-a-stop.md`.

## The rule that would have prevented it was held by the architect while the architect broke it

### Phase 61 — a spec states what to hold, never a check or a line

Two of the user's rulings — a task is not an instruction for reviewing itself, and a spec states what to hold, never where to write it — sat in the buffer as debts for weeks; 58.2's rescue paid the cost, three rounds failing inside the verification tasks it produced, the change itself never faulted. Phase note: [a spec states what to hold, never a check or a line](.ai-factory/specs/trickster77777/169-a-spec-states-what-to-hold-never-a-check-or-a-line.md)

- [ ] **61.1 — the repair is a mood, not a mechanism** — `command-pin-gaps.md`'s Blast-radius holes Repair sentence orders the invariant as something "every match must satisfy after the change" — an instruction to a later run, exactly what *What the pass never writes* forbids; 58.2's rescue failed three rounds inside the verification tasks this produced, never the change itself. Change: the invariant becomes a recorded finding — what the sweep, run now, reaches — never a check for later; note `138-…`'s Q4 paragraph, quoting the sentence live, updates in the same stroke. Spec: `.ai-factory/specs/trickster77777/168-the-repair-is-a-mood-not-a-mechanism.md`.
- [ ] **61.2 — the three parts are the whole, and none is a check or a line** — `roadmap-engine/SKILL.md`'s **What a task spec holds** paragraph says "three parts and nothing else" but never states what a fourth is not, and a checking instruction shipped as spec content without contradicting it. Add one sentence: none of the three checks that the instruction was carried out — that is the review the orchestrator already runs — and each states what the artifact must hold, never where to write it. The heading and its three clauses stay byte-identical; many callers reach it, `command-pin-gaps` among them by name. Spec: `.ai-factory/specs/trickster77777/170-the-three-parts-are-the-whole-and-none-is-a-check-or-a-line.md`.

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
