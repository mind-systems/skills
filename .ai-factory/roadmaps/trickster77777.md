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

## The time entry's evidence exists only once a change has landed

### Phase 72 — the time entry's evidence is the change, a diff where it has landed and the task where it has not

`polymorphism-philosophy`'s time entry says its evidence is the diff, but its consumer, the skeleton's Lens 1, runs over open tasks before any diff exists, while a direct call on closed tasks or a code area has one. The evidence is the change: the diff where it has landed, the task that describes it where it has not. Phase note: [what a rule's moment cannot supply](.ai-factory/specs/trickster77777/0196-a-rule-asks-for-what-its-moment-cannot-supply.md)

- [x] **72.1 — the time entry's evidence is the change, not only the diff** — `src/skills/polymorphism-philosophy/SKILL.md` § "The two entries" says the time entry's "evidence is the diff", though the unit is read two ways: invoked directly on a code area or on closed tasks it has a diff, and `roadmap-decompose-skeleton` Lens 1 runs over open tasks before any diff exists, with the task text and the current code as its evidence. Change: the sentence names the change as the evidence, the diff where it has landed and the task that describes it where it has not, keeping both readers; pinned verbatim in the spec. Lens 1 states no evidence of its own and reads the new clause at run time. Spec: `.ai-factory/specs/trickster77777/0200-the-time-entrys-evidence-is-the-change-not-only-the-diff.md`. [2m 59s]

## A resumed head that runs the probe's two steps as one founds a second folder

### Phase 69 — the session probe prints its nonce in one command and searches for it in the next

`agent-architect`'s session probe has the head run "a command that prints a random nonce" and then search the transcripts for it. One command doing both finds nothing, as its output is not in the transcript until it returns, and a resumed head that does so founds a second folder silently. The nonce is printed by one command and searched by the next. Phase note: [the start's two open outcomes](.ai-factory/specs/trickster77777/0193-the-architects-start-leaves-two-failure-edges-open.md)

- [x] **69.1 — the session probe prints its nonce in one command and searches for it in the next** — `src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" has the head read its session id by "running a command that prints a random nonce, then searching the project's transcripts", without saying the two are separate commands; one command that both prints and searches finds nothing, since its output reaches the transcript only when it returns, and a resumed head that does so founds a second folder and leaves its memory in the first, silently. Change: the probe's sentence names two commands, the first printing the nonce and ending, the next searching for it; pinned verbatim in the spec. The zero-match policy stays: never ask, never stop. Spec: `.ai-factory/specs/trickster77777/0201-the-session-probe-prints-its-nonce-in-one-command-and-searches-in-the-next.md`. [17m 16s]

## A founded buffer opens as a seed

### Phase 70 — a founded buffer opens under its own title, not the seed's

A buffer founded from the seed opens with the seed's title and its paragraph about being a seed, because the step copies it "whole": the buffer misnames itself, though its opening must still say its standing entries come from the seed. It should open under its own title by folder number, the seed's description of itself staying in the seed. Phase note: [what a buffer holds and how it is copied](.ai-factory/specs/trickster77777/0194-the-engine-and-the-seed-do-not-say-what-a-buffer-holds.md)

- [x] **70.1 — a founded buffer opens under its own title** — `src/skills/agent-architect/templates/buffer-seed.md` opens with the title "# Buffer seed — the architect's memory at founding" and a paragraph about being a seed, and the founding passage of `agent-architect` has the seed "copied whole", so a founded buffer opens with both and misnames itself; the paragraph also defines "standing entry" for the head that reads it. Change: the seed carries its own title and description, then a `# Architect buffer — <this folder's number>` heading with an opening that speaks of this buffer and its standing entries; the founding passage copies from that heading down, the folder's number filling the title; pinned verbatim in the spec. Founded buffers keep their opening; the refresh matches bold lead-ins and is unaffected. Spec: `.ai-factory/specs/trickster77777/0202-a-founded-buffer-opens-under-its-own-title.md`. [6m 25s]

## The docs describe skills that have since moved

### Phase 50 — the documentation catches up with what the skills now do

Docs lag the skills: `skill-graph.md` names one direct caller of `note`; `skill-cycle.md` omits phase notes from what prune deletes and says the gap pass "closes", as does `skill-description-field.md`; `multiuser-roadmaps.md` knows one way into the specs directory; two CLAUDE.md lists omit `roadmap-outline-deep` and `orchestrator-artifacts`. Phase note: [the documentation catches up with what the skills now do](.ai-factory/specs/trickster77777/144-the-docs-catch-up-with-the-skills.md)

- [x] **50.1 — the docs say what the skills now do** — The funnel names both direct callers of `note`, the domains section no longer counts trunks, the cycle doc describes the blast-radius repair as a rule, a sweep and a record of what the sweep reaches and prune as deleting the notes of emptied phases, the global planning chain names `roadmap-outline-deep`, and the skills list in `CLAUDE.md` includes `orchestrator-artifacts`.

## A rescue on a named roadmap rolls back a sidecar nobody reads

### Phase 51 — task-rescue writes the sidecar where the orchestrator reads it

`task-rescue` reads the sidecar by `orchestrator-artifacts`' layout, a named roadmap's under `plans/<stem>/`, but its two rollback writes in Step 5 use the flat path. On a named roadmap the rollback lands where the orchestrator does not read, and the run resumes from the old step, silently. Both write sites take the locator the read site uses. Phase note: [task-rescue and the artifact protocol close their own gaps](.ai-factory/specs/trickster77777/145-task-rescue-and-the-artifact-protocol.md)

- [x] **51.1 — task-rescue writes the sidecar where the orchestrator reads it** — `src/skills/task-rescue/SKILL.md` Step 1 locates the sidecar by `orchestrator-artifacts` § 1, a named roadmap's under `plans/<stem>/`, but its two rollback write sites in Step 5, "Depth: spec + plan" and "Depth: plan ratified, implementation absent", say "Locate the sidecar at `.ai-factory/plans/{seq}-{slug}.json`", the flat path, and the depth "spec + plan + code" takes the same procedure by reference; on a named roadmap the rollback lands where the orchestrator does not read, and the run resumes from the old step, silently. Change: both sites take the read site's locator, the flat path for the default pair and `plans/<stem>/` for a named roadmap; pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0203-task-rescue-writes-the-sidecar-where-the-orchestrator-reads-it.md`. [3m 18s]

## Research agents that cannot write are asked to write, and the note is titled before its research

### Phase 52 — the researcher can write, and the note's title is the name research chose

Governing spec: `docs/test-coverage-pass.md`

`roadmap-test-coverage` Layer 4 launches an `Explore` agent per area and has it "write the file yourself", though `Explore` is read-only and the user has watched researchers refuse to write. The note's title is the pre-research area name while its slug is chosen after research. The writer becomes an agent that can write, and the title takes the researched name. Phase note: [roadmap-test-coverage's remaining observations](.ai-factory/specs/trickster77777/146-roadmap-test-coverage-leftovers.md)

- [x] **52.1 — the coverage researcher can write, and the note takes the researched name** — `src/skills/roadmap-test-coverage/SKILL.md` § "Layer 4 — Deep Research (parallel agents)" launches "one `Explore` agent per area" and tells it to write the note itself, though `Explore` lacks `Edit`, `Write` and `NotebookEdit`; the user has seen researchers refuse to write while the main agent writes for them. Its template also opens `# <Area Name> — Test Plan` while the slug is chosen after research, "not for the Area label above". Change: the launch names a `general-purpose` agent, and the prompt and the template give the title the same researched name the slug takes; the three texts are pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0204-the-coverage-researcher-can-write-and-the-note-takes-the-researched-name.md`. [4m 29s]

## Sentences in the skills still describe what earlier phases retired

### Phase 53 — the skill bodies stop describing retired shapes

Three skill sentences outlived the shape they describe: "Decompose existing" still asks a spec for "how to verify", a check `roadmap-engine` excludes; `command-pin-gaps` still says it "enumerates" breakage where its own repair records what the sweep reaches; the skeleton's "Load-once / dependencies" omits `polymorphism-philosophy`. Phase note: [the skill bodies stop describing retired shapes](.ai-factory/specs/trickster77777/147-sentences-that-outlived-their-shape.md)

- [ ] **53.1 — three skill sentences agree with the shape they describe** — `roadmap-decompose` hook (d) "Decompose existing" asks for a spec with "how to verify", a check `roadmap-engine`'s "What a task spec holds" excludes; `command-pin-gaps` says in "The shape it repairs toward" and "What the pass never writes" that it "enumerates" a blast radius or breakage, where its own repair records what the sweep reaches now; and `roadmap-decompose-skeleton` § "Load-once / dependencies" lists two loaded skills of the three its `loads:` field names. Change: "how to verify" leaves the parenthesis, with "guards" kept by the user's word; the two sentences say "recording" and "records"; the list gains `polymorphism-philosophy`; the after-texts are pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0205-three-skill-sentences-agree-with-the-shape-they-describe.md`.

---STOP---
