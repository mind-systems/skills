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

- [x] **53.1 — three skill sentences agree with the shape they describe** — `roadmap-decompose` hook (d) "Decompose existing" asks for a spec with "how to verify", a check `roadmap-engine`'s "What a task spec holds" excludes; `command-pin-gaps` says in "The shape it repairs toward" and "What the pass never writes" that it "enumerates" a blast radius or breakage, where its own repair records what the sweep reaches now; and `roadmap-decompose-skeleton` § "Load-once / dependencies" lists two loaded skills of the three its `loads:` field names. Change: "how to verify" leaves the parenthesis, with "guards" kept by the user's word; the two sentences say "recording" and "records"; the list gains `polymorphism-philosophy`; the after-texts are pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0205-three-skill-sentences-agree-with-the-shape-they-describe.md`. [3m 26s]

## A skill nobody invokes is paid for in every session

### Phase 74 — task-rescue-audit is retired

The user has not invoked `task-rescue-audit` for months. Its outside view of a looped task is carried by the rescue report's own narrative, by peer architects holding memory across repositories and by names in the architecture maps, while its description is paid for in the always-loaded field of every session. The skill goes, and every live statement of it with it.

- [x] **74.1 — task-rescue-audit is deleted and every live statement of it follows** — `src/skills/task-rescue-audit/` and its `active/skills/` symlink exist, and live text names the skill: `task-rescue` Step 3's sentence that its narrative register "is shared with `task-rescue-audit`'s output", the section and a scheme line of `docs/sakshi-harness/skill-cycle.md`, and four places in this repository's `CLAUDE.md`. Change: the directory and the symlink go; the sentence is deleted with its pair; the section, the scheme line and the four places drop the name; each after-text is pinned verbatim in the spec, which also records the registry entry that names "audit", the orchestrator sentence its own head changes, and the records left untouched. Spec: `.ai-factory/specs/trickster77777/0207-task-rescue-audit-is-deleted-and-every-live-statement-of-it-follows.md`. [5m 33s]

## `aif-architecture` writes folder layout and misses where a system varies

### Phase 73 — aif-architecture describes the built design first and asks where the system varies

`aif-architecture` offers only packaging patterns and reads only folder layout; its option 2 writes a target to migrate toward. It never asks where the system varies, by mode, environment or provider, so a hand-built Ports and Adapters design came out a Modular Monolith target. Phase note: [aif-architecture describes the built design first and asks where the system varies](.ai-factory/specs/trickster77777/0206-aif-architecture-describes-folders-and-misses-where-the-system-varies.md)

- [x] **73.1 — the reference knows where variation lives** — `src/skills/aif-architecture/references/architecture.md` scores the packaging patterns in "Decision Matrix" and "Quick Decision Guide" by team size, domain complexity and scale, and teaches ports only as interfaces to external systems (the principle "Port Abstraction for External Dependencies"); nothing says a port can have an adapter per mode or provider, chosen at a composition root, and a low score reads as a system with nothing to vary. Change: a note after the matrix says it scores packaging fit only, a section "Where the System Varies — Ports and Adapters" defines the axis, the port, an adapter per value and the composition root, with the rule that a difference is a new adapter and never a branch at the junction, and one line under the guide says it picks packaging only; the three texts are pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0208-the-reference-knows-where-variation-lives.md`. [6m 9s]
- [x] **73.2 — the dependency rule holds at every scale** — `references/architecture.md` states the dependency rule once, in the Explicit Architecture ("Dependencies point INWARD"), the Structured Modules disclaim "rigid hexagonal ports", and no text names a pattern for the inside of a feature module or of presentation, where the user builds with a loose VIPER-like split and MVVM. Change: after the section 73.1 adds, a section "The Dependency Rule at Every Scale" names three scales, the system's edge, a feature module and the inside of presentation, as one rule, details depending on abstractions the core owns, with where variations live and which way dependencies point as the two things to look for at each; the section is pinned verbatim in the spec. Sequenced after 73.1. Spec: `.ai-factory/specs/trickster77777/0209-the-dependency-rule-holds-at-every-scale.md`. [3m 8s]
- [x] **73.3 — the template writes the built design** — `references/architecture-template.md` writes the packaging: folder structure and dependency rules, pasted code blocks as examples, and several bans with no reason; it has no place for what varies or the composition root. Change: the template gains "What varies", "Composition root", "The rule" and "Invariants" (links to the governing documents) ahead of the packaging sections, drops "Code Examples" for "Living Examples" named by path and symbol, writes a migration target only on the user's explicit choice, and its rules for generation carry the reason for each ban and forbid counts and thresholds; `## Decision Rationale` and its `Tech stack` line stay byte-identical, as `roadmap-test-coverage` reads them, and the `aif` sentence naming "code examples" is repinned; all texts are pinned verbatim in the spec. Sequenced after 73.1 and 73.2. Spec: `.ai-factory/specs/trickster77777/0210-the-template-writes-the-built-design.md`. [5m 17s]
- [x] **73.4 — the skill reads the built design before it offers a menu** — `src/skills/aif-architecture/SKILL.md` scans the codebase "to infer project size and complexity", never reads which interfaces have several implementations or where one is chosen, never asks a new project where it will vary, Step 1.5 offers the strict migration target beside "document reality" as an equal, and the `CLAUDE.md` pointer Step 3 writes says only "module boundaries, folder structure, and dependency rules". Change: Step 0 reads the built design, Step 1 names it before the packaging menu and asks a new project its variation axes first, Step 1.5 compares packaging only and offers the migration target only on the user's explicit choice, and the Step 3 pointer names what varies and the composition root before packaging; the after-texts are pinned verbatim in the spec. Sequenced after 73.3. Spec: `.ai-factory/specs/trickster77777/0211-the-skill-reads-the-built-design-before-it-offers-a-menu.md`. [5m 56s]

## Other people's repositories ride in our tree

### Phase 75 — upstream holds the sources we follow, not a mirror of them

A mirror of `lee-to/ai-factory` and its `aif-skill-generator` ride in our tree and so in every task commit, though other people's repositories are sources we compare against, not code we commit. The user does not need the mirror in commits and writes his own skills, so the generator has no use. The tracked mirror and the generator's symlink go; each source is a file in `upstream/` with its git-ignored clone beside it, and the sync script becomes a comparison that reads them and fetches.

- [x] **75.1 — the tracked mirror goes and the sync script becomes a fetching comparison** — `upstream/ai-factory/` is a tracked mirror that `scripts/sync-upstream.sh` overwrites with `rsync -a --delete`, `active/skills/aif-skill-generator` links into it, and `upstream/` already holds one tracked file per source, with the docs describing the end state. Change, in this order: `git rm -r upstream/ai-factory` and the symlink go; `.gitignore` gains `upstream/*/`; the script is renamed `scripts/compare-sources.sh`, reads each `upstream/*.md` for its URL, counterpart skills and newest `Last seen:` commit, keeps the clone beside it, cloned on first use and fetched after, prints the head and the commit subjects since that commit, diffs our counterparts against the clone, and writes nothing tracked; its text is pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0212-upstream-is-a-list-of-sources-and-the-mirror-and-the-generator-go.md`. [4m 34s]

## The counts reach the specs through the steps that write them

### Phase 77 — a spec holds no measurement of the tree

Governing spec: `docs/counts-go-stale.md`

Specs written by `roadmap-decompose` carry count words beside the members they name — "these seven logic models", "exactly the two sites". Count words reach them because the steps that write a spec pull toward a count and do not carry the counts rule. Phase note: [a spec holds no measurement of the tree](.ai-factory/specs/trickster77777/0214-a-spec-names-the-members-and-does-not-count-them.md)

- [ ] **77.2 — the doc that governs a spec's shape says what exact values are and leaves out the measurement** — `docs/what-a-task-carries.md` § "What a spec holds" says what is true now is read from the code "with exact values" and that none of the parts is a check, but not what a value is or that a measurement of the tree is not held either. Change: "exact values" is said to mean the code's own values (a literal, a symbol, a type, a path), and the measurement joins what a spec does not hold, with its reason: tasks run one after another, so a count of the tree is false before the task is reached; the paragraph is pinned verbatim in the spec, in agreement with the engine's. Spec: `.ai-factory/specs/trickster77777/0220-the-doc-that-governs-a-specs-shape-names-its-sets-and-leaves-out-the-measurement.md`.
- [ ] **77.3 — a spec's exact values are the code's own and it does not measure the tree** — `roadmap-engine` § "What a task spec holds" asks for what is true now "with exact values" without saying what a value is, and its "Nothing else means" list holds checks, positions and fences but no measurement, so a writer follows the paragraph into a count. Change: "exact values" is said to mean the code's own values (a literal, a symbol, a type, a path), and the list gains the measurement with its reason in a clause: a tasks queue runs one after another, so a count of the tree is false before the task is reached; the paragraph is pinned verbatim in the spec. Sequenced after 77.2. Spec: `.ai-factory/specs/trickster77777/0217-a-spec-names-its-sets-and-does-not-measure-the-tree.md`.
- [ ] **77.4 — the blast-radius invariant asks for no size** — `command-pin-gaps` paragraph "Blast-radius holes" has the invariant "a recorded finding of what the sweep, run now, reaches … so a reader can tell a genuinely narrow set from a broken pattern", whose purpose clause judges size and so draws a count into the spec, while `docs/counts-go-stale.md` names "how many files a sweep reaches" as a measurement. Change: the purpose clause reads "so a reader can tell a working pattern from a broken one"; "A sweep too large to enumerate is itself a finding" stays, being a judgement about a task's shape and not a count written into a spec; the changed sentence is pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0218-the-blast-radius-invariant-asks-for-no-size.md`.
- [ ] **77.5 — the seed's counts entry says a work-order is not conversation** — the counts standing entry in `agent-architect/templates/buffer-seed.md` says "in conversation a number or a position is fine", and a work-order sits on that side by its wording, though it is thrown away once applied and the spec is composed from it, so its counts reach the spec. Change: after that clause the entry says a work-order is not conversation in this sense, because the spec is composed from it, and a count in an order becomes a count in the spec; the entry is refreshed into every buffer from this text, so the addition stays short; the sentence is pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0219-the-seeds-counts-entry-says-a-work-order-is-not-conversation.md`.

## The lenses are missing from the skill description field

### Phase 79 — the lenses carry their descriptions in the field and the hand can load one

Governing spec: `docs/skill-description-field.md`, `docs/paired-loop.md`

The lenses carry `disable-model-invocation: true`, so the skill description field lacks them. The flag goes from every lens but `roadmap-prune` and `task-rescue`, and `architect-editor-engine` says a skill the work needs is loaded once by whoever does the work, then held. Docs first. Phase note: [the lenses carry their descriptions in the field and the hand can load one](.ai-factory/specs/trickster77777/0221-the-lenses-carry-their-descriptions-in-the-field-and-the-hand-can-load-one.md)

## Architects are per user, and their folders are not

### Phase 76 — a head's folder lives under its user's slug

Governing spec: `docs/paired-loop.md`

Architects are per user, as named roadmaps are, but the skills still found a head at a flat `.ai-factory/architects/<NN>/` and find a peer by number alone. The engine's path and numbering, the probe, the peer and team passages and the seed's `## Team` take the user's `<slug>` folder. Phase note: [a head's folder lives under its user's slug](.ai-factory/specs/trickster77777/0213-a-heads-folder-lives-under-its-users-slug.md)

## A long-lived editor loses its working knowledge at a moment nobody chooses

### Phase 78 — the hand writes its own snapshot and a new hand carries on from it

Governing spec: `docs/paired-loop.md`

An editor loses its working context at a moment nobody chooses: the snapshot is the head's alone, and a fresh hand follows only a dead one. The hand writes its own in `editor/`, beside the head's `architect/`, and a new hand starts from it. Decomposed after 76 and the first field trial, run once 77 is decomposed. Phase note: [the hand writes its own snapshot and a new hand carries on from it](.ai-factory/specs/trickster77777/0215-the-hand-writes-its-own-snapshot-and-a-new-hand-carries-on.md)

---STOP---
