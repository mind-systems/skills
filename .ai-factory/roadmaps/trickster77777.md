> Owner: trickster77777@gmail.com

# Skills Roadmap

> Generic AI Factory skills — reusable slash-command packages for Claude Code.

## A wrong number reads exactly like a right one

### Phase 42 — the always-loaded rule names a section number as a position address

Governing spec: `docs/reference-by-name.md`

A session cited a governing document's section by number, consistently and wrongly — the rule it pointed at lived one section over — and the mis-citation propagated into contract lines, task specs, a handoff, and a shared buffer before a fresh read against the document caught it. Nothing had been renumbered; the number simply resolved to the wrong place. Phase note: [the number resolves, and resolves wrongly](.ai-factory/specs/trickster77777/136-a-number-is-not-the-name-beside-it.md)

- [x] **42.1 — the always-loaded rule separates a number assigned once from a heading's ordinal** — `src/global/CLAUDE.md` § "Grounding claims" says "A heading, a bolded rule, a symbol, a numbered item survives every insertion above it", with nothing to tell a number assigned once and split, like a task's `N.M` or a skill's step, from a heading's ordinal, which shifts like a line number, though `docs/reference-by-name.md` § "Granularity, not size" now draws the line. The global file reaches every session of every project through the link chain from `~/.claude/CLAUDE.md`. Change: the sentence names a number assigned once and split rather than shifted among what survives, and says a document's section is cited by its heading's text; pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0197-the-always-loaded-rule-separates-a-number-from-a-heading-ordinal.md`. [3m 17s]

## A skill cites a doc, though a skill is its own documentation

### Phase 71 — a skill carries what it needs from a doc in its own text

A skill is its own documentation; docs describe the skills, never the reverse, and what a skill needs from a doc is part of its own text. Three carriers cite `docs/paired-loop.md` instead: `agent-architect`'s snapshot paragraph, `command-handoff`, and the seed's `## Team` placeholder. No doc states the rule; it lives in the architect's buffer. Phase note: [a path that exists in one repository](.ai-factory/specs/trickster77777/0195-a-skill-cites-a-path-that-exists-in-one-repository.md)

- [x] **71.1 — a skill carries what it needs from a doc, and cites none** — `agent-architect`'s snapshot paragraph, `src/commands/command-handoff.md` and the `## Team` placeholder in `templates/buffer-seed.md` each cite `docs/paired-loop.md`, though a skill is its own documentation. In the first two the sentence before the citation already draws the line by who reads and what it is about; the placeholder cites the doc for a model it does not state, and uses "liaison", which no skill defines. Change: the citations leave; the placeholder carries its own links, the liaison's meaning and the compact in its own words; each file's after-text is pinned verbatim in the spec. Heads already founded keep their own `## Team` text. Spec: `.ai-factory/specs/trickster77777/0198-a-skill-carries-what-it-needs-from-a-doc-and-cites-none.md`. [4m 35s]

## The user restates the gap pass's unit every time he runs it

### Phase 43 — the gap pass walks every task alone and reports once at the end

The user asks the gap pass over every open task one at a time, without stopping, report at the end, each time by hand. Its targeting accepts a task, a phase or every open task and leaves the unit unsaid; it comes to walk each task alone, holding that task and nothing else, finish it before the next, and report once, blockers gathered. Phase note: [the unit is fixed for the walk and open for the call](.ai-factory/specs/trickster77777/137-the-unit-is-fixed-for-the-walk-and-open-for-the-call.md)

- [x] **43.1 — the gap pass has one mode: every task walked alone, one report at the end** — `src/commands/command-pin-gaps.md` fixes the unit of its walk in one task, "holding this task and nothing else", while its targeting accepts a task, a phase or all open tasks above the stop as one invocation and says nothing of the unit between them; it keeps a scan mode beside the default one, and its default edits "the file" and ends on one report line with no place for many tasks' blockers. The user wants one mode, the range he names. Change: the targeting says each task is walked alone, in order, finished before the next, without stopping; one paragraph gives the per-task work and the single report, blockers gathered, owners named; the scan mode, its trigger words, list format and argument hint, and "a plan" in the description leave; texts pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0199-the-gap-pass-walks-every-task-alone-and-reports-once.md`. [3m 57s]

---STOP---

## A rule asks for what its moment cannot supply

### Phase 72 — a rule is stated in terms of what is available when it runs

A rule asks for what its moment cannot supply: `polymorphism-philosophy`'s time entry takes the diff as evidence where the skeleton runs before any diff, and `command-pin-gaps`' blast-radius floor cannot be met by a sweep for wording the task removes. Phase note: [what a rule's moment cannot supply](.ai-factory/specs/trickster77777/0196-a-rule-asks-for-what-its-moment-cannot-supply.md)

## Every question in the chain looks for what is missing

### Phase 46 — something asks whether a task claims more than its defect requires

This phase is blocked on two rulings, not one: whether a task claiming more than its defect needs a new rule at all, and whose it is; and where a spec's re-decided, already-ratified answer gets caught, given that no independent reader between drafting and the orchestrator is guaranteed to hold the governing document. If the two answers name different homes, this is two phases. Phase note: [two subtractions that arrived together](.ai-factory/specs/trickster77777/140-two-subtractions-that-arrived-together.md)

## The phase-note skill leaves its budget, grounding and engine use open

### Phase 47 — the phase-note skill decides what its budget counts, what grounds a note and how it uses the engine

`roadmap-outline-deep` leaves unsettled whether the pointer counts toward the preamble budget, whether a note can be grounded in the code alone when its verbosity directive asks for "docs and code", and whether it should run the engine's maintenance flow, given that it rewrites preambles with no confirmation step. Phase note: [what the note describes, and what the skill presupposes](.ai-factory/specs/trickster77777/141-what-the-note-describes-and-what-the-skill-presupposes.md)

## `agent-architect` keys the echo on who asked

### Phase 48 — an echo is about whether a second reading exists, not about who delegated

Governing spec: `docs/paired-loop.md`

`agent-architect` says a report on the head's own delegated legwork "carries no second opinion", however much of the ground the head walked itself. What decides an echo is whether a second, independently produced reading exists, and `docs/paired-loop.md` § "Where the split falls" already says so; only the skill's sentence remains. Phase note: [whether a second reading exists at all](.ai-factory/specs/trickster77777/142-two-readings-or-one.md)

## The architect's start leaves two failure edges open

### Phase 69 — a failed probe and a dead hand holding a relay have a defined outcome

A failed session probe at founding leaves a folder no later start finds, and a resumed head whose probe fails once founds a new folder and orphans its own; the dead-editor paragraph says nothing of a user's `::` payload the head holds unforwarded. Both need the user's ruling. Phase note: [the start's two open outcomes](.ai-factory/specs/trickster77777/0193-the-architects-start-leaves-two-failure-edges-open.md)

## The engine and the seed do not yet say what a buffer holds

### Phase 70 — the buffer's contents and its copying are stated where the buffer is defined

The engine's sentence on what the memory holds names no editor handle, though the skill writes one into the buffer and the seed has no place for it; the engine uses "seed" and "standing entry", which only the skill and the seed define; and the seed is "copied whole", title and guidance lines included. Phase note: [what a buffer holds and how it is copied](.ai-factory/specs/trickster77777/0194-the-engine-and-the-seed-do-not-say-what-a-buffer-holds.md)

## The docs describe skills that have since moved

### Phase 50 — the documentation catches up with what the skills now do

Docs lag the skills: `skill-graph.md` names one direct caller of `note`; `skill-cycle.md` omits phase notes from what prune deletes and says the gap pass "closes", as does `skill-description-field.md`; `multiuser-roadmaps.md` knows one way into the specs directory; two CLAUDE.md lists omit `roadmap-outline-deep` and `orchestrator-artifacts`. Phase note: [the documentation catches up with what the skills now do](.ai-factory/specs/trickster77777/144-the-docs-catch-up-with-the-skills.md)

## The rescue path carries its own unrepaired defects

### Phase 51 — task-rescue and the artifact protocol close their own gaps

`task-rescue` still writes its rollback to the flat sidecar path, wrong for a named roadmap, and its body is far over the line bound. The marker grammar names one writer where `task-rescue` is another, and Step 5.6 has no `[fixed]` branch; the mirror source has a short path, and the durable report lacks the ban on hand-composing. Phase note: [task-rescue and the artifact protocol close their own gaps](.ai-factory/specs/trickster77777/145-task-rescue-and-the-artifact-protocol.md)

## The coverage note's title and its writing agent were left as they were

### Phase 52 — the test-plan note's title follows its slug, and its writer can write

Governing spec: `docs/test-coverage-pass.md`

`roadmap-test-coverage`'s Layer 4 titles each test-plan note by the area's name before research, while the agent picks its slug after reading the source, and has an `Explore` agent write the file, an agent type that can be read-only. Phase note: [roadmap-test-coverage's remaining observations](.ai-factory/specs/trickster77777/146-roadmap-test-coverage-leftovers.md)

## Sentences in the skills still describe what earlier phases retired

### Phase 53 — the skill bodies stop describing retired shapes

Skill bodies still describe retired shapes: the link grant is paraphrased loosely and `roadmap-prune`'s safety reason leans on it with no matching sentence in `roadmap-outline`; "Decompose existing" asks for guards and how to verify against "nothing else"; `editor.md` still says "relayed"; the engine's description omits the ride-alongside bound. Phase note: [the skill bodies stop describing retired shapes](.ai-factory/specs/trickster77777/147-sentences-that-outlived-their-shape.md)

---STOP---
