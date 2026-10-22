> Owner: trickster77777@gmail.com

# Skills Roadmap

> Generic AI Factory skills — reusable slash-command packages for Claude Code.

## The lenses are missing from the skill description field

### Phase 79 — the lenses carry their descriptions in the field and the hand can load one

Governing spec: `docs/skill-description-field.md`

The planning lenses carry `disable-model-invocation: true`, so the skill description field lacks them and no agent can load them. The flag goes; `agent-architect`, `roadmap-test-coverage`, `roadmap-prune` and `task-rescue` stay out, since what each does is reviewed only before it happens. Phase note: [the lenses carry their descriptions in the field and the hand can load one](.ai-factory/specs/trickster77777/0221-the-lenses-carry-their-descriptions-in-the-field-and-the-hand-can-load-one.md)

- [x] **79.1 — the field's doc says which skills stand outside it, and why** — `docs/skill-description-field.md` describes the field as "the `description:` of every skill in the family", yet skills whose work is reviewed only before it happens carry `disable-model-invocation: true` and are not in it, the planning lenses' additive writes being reviewed after, and `docs/always-loaded-discipline.md` repeats "every skill's `description:`". Change: where the doc says what the field holds it states that a skill whose work is reviewed only before it happens, with the user present, and never after, is called by the user alone and stays out; the discipline doc's phrase takes the same words, "each skill the agent may call on its own"; the after-texts are pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0228-the-fields-doc-says-which-skills-stand-outside-it-and-why.md`. [2m 43s]
- [x] **79.2 — the planning lenses enter the skill description field** — `roadmap-outline`, `roadmap-outline-deep`, `roadmap-decompose` and `roadmap-decompose-skeleton` carry `disable-model-invocation: true`, so their descriptions are absent from the field `docs/skill-description-field.md` leans on, and no agent, the hand included, can load them through the `Skill` tool. Change: the flag reads `false` in each frontmatter, the way the engines carry it; the descriptions join every session's field, the orchestrator's agents' too. Spec: `.ai-factory/specs/trickster77777/0229-the-planning-lenses-enter-the-skill-description-field.md`. [2m 52s]

## The user's placeholder is `<user-slug>`

### Phase 82 — the user's placeholder is `<user-slug>`

Governing spec: `docs/philosophy/multiuser-roadmaps.md`

The skills write the user's slug as `<slug>`, the placeholder their file names use for a title, so one name carries two meanings; `paired-loop`, the registry and the `CLAUDE.md` rows already write it `<user-slug>`. Every user placeholder in the skills' text becomes `<user-slug>`: `roadmap-engine`'s named-roadmap path, `specs/<slug>/` and the test sibling, `roadmap-decompose`, `roadmap-outline-deep`, `orchestrator-artifacts`, `task-rescue`. The targeting hints of `roadmap-outline-deep` and `roadmap-decompose-skeleton` offer a slug neither defines; it goes, and they take a phase.

- [x] **82.1 — every user placeholder in the skills becomes `<user-slug>`** — the skills write the user's slug as `<slug>`, the placeholder their file names use for a title, in `roadmap-engine` (the roadmap path, `specs/<slug>/` and the test sibling, in its two-tier text and § "Named roadmaps"), `roadmap-decompose`, `roadmap-outline-deep`, `orchestrator-artifacts` and `task-rescue`. Change: each of those sites reads `<user-slug>`, the after-texts pinned per site in the spec. Spec: `.ai-factory/specs/trickster77777/0236-every-user-placeholder-in-the-skills-becomes-user-slug.md`. [4m 48s]
- [x] **82.2 — the targeting argument names a phase, not a slug** — `roadmap-outline-deep`'s `argument-hint: "[phase or slug]"` and its targeting text "a phase or slug", and `roadmap-decompose-skeleton`'s `"[phase/slug or task description]"` and "a phase, slug, or single task description", carry a slug that neither skill defines. Change: the slug goes from both hints and both targeting sentences — `roadmap-outline-deep` takes a phase, the skeleton pass a phase or a task description; the after-texts are pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0237-the-targeting-argument-names-a-phase-not-a-slug.md`. [2m 36s]

## Every agent derives the user's slug for itself

### Phase 83 — the session is given the user's slug, and no agent derives it

Governing spec: `docs/sakshi-harness/sakshi-harness.md`

Every agent that works with a user's things carries `roadmap-engine`'s derivation of the user's slug (§ "Named roadmaps", "Slug derivation") and computes it each time it resolves "my roadmap"; phase 76 puts a head's folder under the slug, so founding a head computes it again. The slug is a fact of the machine's git identity, not something to reason out. A script in `roadmap-engine/scripts/` derives it, a `SessionStart` hook registered at setup gives every session the line, and a session without it runs the script. The skills say only "the user's slug", and the derivation leaves the engine's text, which every roadmap session loads. Phase 76 rests on the slug as given.

- [x] **83.1 — the user's slug is derived by a script** — the derivation of the user's slug lives only in prose, `roadmap-engine`'s "Slug derivation", for each agent to carry out, while the orchestrator's running code derives it its own way. Change: a script `src/skills/roadmap-engine/scripts/user-slug.sh` prints the bare slug on one line, derived as that code does — the local-part of `git config user.email`, lowercased, each non-alphanumeric run collapsed to one hyphen, edge hyphens trimmed, the slugified `user.name` when the email is unset or its slug comes out empty — from the identity of the repository it runs in, exiting `2` when no slug is derivable; the skills' text states the derivation nowhere else. Spec: `.ai-factory/specs/trickster77777/0233-the-users-slug-is-derived-by-a-script.md`. [6m 25s]
- [x] **83.2 — the engine says the slug is given, not how to derive it** — `roadmap-engine` § "Named roadmaps", "Slug derivation", carries the rule into every session that loads the engine. Change: the paragraph says the user's slug is given at session start as the line `The user's slug: <user-slug>`, and a session holding no such line runs `scripts/user-slug.sh` and takes its output as the slug; the rule's text, the example and the fallback leave the engine; the after-text is pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0234-the-engine-says-the-slug-is-given-not-how-to-derive-it.md`. [2m 55s]
- [x] **83.3 — setup registers the session hook** — `README.md` § "Setup — activating the package" walks the user through the `~/.claude` surfaces, all of them symlinks, so no session starts holding the slug. Change: a further surface, a `SessionStart` hook in `~/.claude/settings.json` whose command prints `The user's slug: ` before the output of `~/.claude/skills/roadmap-engine/scripts/user-slug.sh` and prints nothing, exiting zero, where the script yields no slug, walked through with the user like the others and merged into the settings they keep, never written silently; the paragraph and the hook entry are pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0235-setup-registers-the-session-hook.md`. [4m 55s]
- [x] **83.4 — the slug script's header names no caller** — the header comment of `roadmap-engine`'s `scripts/user-slug.sh` says it "Derives the slug the way the pipeline does", yet the orchestrator now runs this script and derives nothing itself, so the comment points back at the script. Change: the header drops the caller phrase and reads "Derives the slug: the lowercased, hyphen-collapsed local-part of git user.email, falling back to git user.name", wrapped as the file wraps; the body of the script is unchanged; the after-text is pinned in the spec. Spec: `.ai-factory/specs/trickster77777/0245-the-slug-scripts-header-names-no-caller.md`. [2m 26s]

## Architects are per user, and their folders are not

### Phase 76 — a head's folder lives under its user's slug

Governing spec: `docs/paired-loop.md`

Architects are per user, as named roadmaps are, but the skills still found a head at a flat `.ai-factory/architects/<NN>/` and find a peer by number alone. The engine's path and numbering, the peer and team passages and the seed's `## Team` take the user's `<user-slug>` folder. Phase note: [a head's folder lives under its user's slug](.ai-factory/specs/trickster77777/0213-a-heads-folder-lives-under-its-users-slug.md)

- [x] **76.1 — the engine puts a head's folder in its user's folder** — `architect-editor-engine` § "The architect's buffer" places the head's folder at `.ai-factory/architects/<NN>/` and numbers a new one above the highest folder under `.ai-factory/architects/`, so every user's heads share one number space. Change: the folder is `.ai-factory/architects/<user-slug>/<NN>/`, `<user-slug>` the user's slug, taken from the line the session holds, `The user's slug: <user-slug>`, else from `roadmap-engine`'s `scripts/user-slug.sh`, and the number is counted within the user's folder; the after-text is pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0230-the-engine-puts-a-heads-folder-in-its-users-folder.md`. [2m 43s]
- [x] **76.2 — the architect reaches a peer in its owner's folder** — `agent-architect` § "Working with another architect" names a peer by folder number alone and reaches it at `.ai-factory/architects/<NN>/address.md`, a path that no longer holds once folders sit under their users. Change: a peer is named by folder number, with the owner's slug when it is another user's, and reached at `.ai-factory/architects/<user-slug>/<NN>/address.md`, `<user-slug>` the peer owner's slug; the after-text is pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0231-the-architect-finds-itself-and-its-peers-in-the-users-folder.md`. [2m 49s]
- [x] **76.3 — the seed's team links carry the owner's slug** — `src/skills/agent-architect/templates/buffer-seed.md`, in its `## Team` placeholder, tells a new head to name those it leads below "each by repository and folder number", which no longer names a head once folders sit under their users. Change: the clause reads "each by repository, owner's slug and folder number, never by session name", the form `docs/paired-loop.md` § "The team" already holds. Spec: `.ai-factory/specs/trickster77777/0232-the-seeds-team-links-carry-the-owners-slug.md`. [1m 54s]

## A long-lived editor loses its working knowledge at a moment nobody chooses

### Phase 78 — a snapshot keeps how its knowledge was got, the hand writes its own, and a new hand carries on from it

Governing spec: `docs/paired-loop.md`

The doc states the snapshot rule: a snapshot keeps how its knowledge was got, each half writes its own, the head replaces its hand before a compact. The skills hold none of it — the engine's folder has no `editor/`, `agent-architect` leaves the snapshot to the head, `editor.md` starts a hand from the buffer alone. Phase note: [the hand writes its own snapshot and a new hand carries on from it](.ai-factory/specs/trickster77777/0215-the-hand-writes-its-own-snapshot-and-a-new-hand-carries-on.md)

- [x] **78.1 — what a snapshot carries lives in the engine** — `agent-architect` § "Spawn once, message thereafter" holds the snapshot's genre — the volatile residue and the reasoning, "thick by default", "supersedes the last by name" — while `architect-editor-engine` § "The architect's buffer" holds only where snapshots live, and `docs/paired-loop.md` adds how the knowledge was got. Change: the engine takes the genre as one paragraph with the doc's additions in it — the method or where it is kept, the shape of what was studied when its source is out of reach, pointers to the detail; in place of "thick by default", the measure that what lies in no file is kept and what lies in a file becomes a pointer; `agent-architect` keeps its occasions and the conversation as the head's subject and points to the engine for the rest; the after-texts are pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0238-what-a-snapshot-carries-lives-in-the-engine.md`. [3m 30s]
- [x] **78.2 — the folder holds the hand's snapshots** — `architect-editor-engine` defines the folder as `buffer.md`, `address.md` and "the head's own snapshots", numbered inside the folder, with no place for the hand's, and says in its description and body that the head is the only writer and the hand never writes. Change: the folder also holds `editor/`, the hand's snapshots, named and numbered the same way and on their own; each opens with the line ``Writer: `<handle>`, relieved <date>.``; `editor/` is the history of hands and nothing else lists them; the head is the buffer's only writer, as it is of its own snapshots, and `editor/` is the hand's to write, in the description and the body alike; the after-texts are pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0239-the-folder-holds-the-hands-snapshots.md`. [2m 53s]
- [x] **78.3 — the head replaces its hand** — `agent-architect` § "Spawn once, message thereafter" has a fresh hand only after a dead one, "a digest of what the editor has accumulated", and a snapshot "never delegated to the editor to compose", "forbidden to the editor outright" in § "Relay on the marker; author the apply work-order and your own legwork". Change: the head replaces its hand before it compacts, in the user's window — half its context a firm floor, four fifths a soft mark, the seam its pick — as a quiet act, named in a line; the greenlight scopes to a work-order on a shared artifact, so the hand's snapshot, asked in an `APPLY-EDIT` message, needs none; the digest becomes a pointer to the hand's latest snapshot in `editor/`; the prohibition reads of "your own memory snapshot"; the spec pins the after-texts. Spec: `.ai-factory/specs/trickster77777/0240-the-head-replaces-its-hand.md`. [6m 56s]
- [x] **78.4 — the hand rehydrates from the buffer and its predecessor's snapshot** — `src/agents/editor.md` has the editor born fresh at every spawn, its spawn prompt giving the buffer's own path, and names no snapshot, so a hand starts from the buffer alone. Change: at spawn, once the engine is loaded, the hand reads the buffer whole and the latest snapshot in the `editor/` beside it, where one exists, before its first round, and takes that snapshot as its own memory, after a replacement and after a death alike, the head naming nothing beyond the buffer's path; the after-text is pinned in the spec. Spec: `.ai-factory/specs/trickster77777/0241-the-hand-rehydrates-from-the-buffer-and-its-predecessors-snapshot.md`. [2m 39s]
- [x] **78.5 — the replacement point is named in plain words** — "seam" is a reserved word, the `[x]`/`[ ]` boundary of a roadmap, yet `agent-architect` § "Spawn once, message thereafter" says "between the two you pick the seam" and `docs/paired-loop.md` § "How the memory begins, and how it survives" says "the head picks the seam", and a head read it as any point in the window and replaced its hand in the middle of a unit of work. Change: both clauses name the point as a break in the work, the end of a unit of work, and nothing else in either file changes; the after-texts are pinned in the spec. Spec: `.ai-factory/specs/trickster77777/0249-the-replacement-point-is-named-in-plain-words.md`.

## A rescue leaves no way back to the sessions it read

### Phase 84 — a rescue report leads back to the sessions whose artifacts it read

`task-rescue` captures `step` and `elapsed` from the sidecar before a repair deletes it, and no session id, so once a depth resets the sidecar or a re-run overwrites its keys, nobody can resume the planner or the implementer to ask what it saw. The report should name the sessions whose artifacts the rescue read. Phase note: [a rescue report leads back to the sessions whose artifacts it read](.ai-factory/specs/trickster77777/0242-a-rescue-report-leads-back-to-the-sessions-it-read.md)

- [x] **84.1 — the capture records the session ids and the report names them** — `task-rescue` § "Step 1 — Discover artifacts" captures `step` and `elapsed` from the sidecar before a repair deletes it, and no session id, and § "Step 5.7 — Write the durable report" renders `Stopped at` and `Elapsed before the rescue` alone, so after a spec-depth reset or a re-run the planner and the implementer cannot be resumed to quote what they saw. Change: the capture records every session id the sidecar holds, each under its key, and the report names them in a `Sessions` line, `absent` where there is no sidecar; the capture's "four facts" loses its count; the after-texts are pinned in the spec. Spec: `.ai-factory/specs/trickster77777/0243-the-capture-records-the-session-ids-and-the-report-names-them.md`. [2m 58s]
- [x] **84.2 — the engine names the plan-reviewer session keys** — `orchestrator-artifacts` § "3. Sidecar fields" names `planner` and `implementer` as resumable session ids, while the orchestrator now writes `plan-reviewer-<N>` into the sidecar on each plan-review attempt, right after the reviewer returns and even when it wrote no review, and never reads it. Change: § 3 names the family: one plan reviewer's session id per attempt, `<N>` the round its `plan-review-<N>` file carries, for reading only and never resumed by the run; the after-text is pinned in the spec. Spec: `.ai-factory/specs/trickster77777/0246-the-engine-names-the-plan-reviewer-session-keys.md`. [2m 41s]

## The skills cite the orchestrator's source

### Phase 86 — the skills speak of the orchestrator's protocol and never cite its source

The orchestrator moved its modules, so two skills cite files and a function that no longer hold what they are cited for. The skills run outside this repository's context: they speak of the orchestrator as an executor and state a mirrored protocol as behaviour, never by file or function. Phase note: [the skills speak of the orchestrator's protocol and never cite its source](.ai-factory/specs/trickster77777/0247-the-skills-speak-of-the-orchestrators-protocol-not-of-its-source.md)

- [x] **86.1 — the skills mirror the orchestrator's protocol without citing its source** — `orchestrator-artifacts` § "7. Mirrors-the-orchestrator invariant" names the orchestrator's source files as the ones it mirrors, and `task-rescue` § "Valid sidecar `step` states" names a source file and two functions, one of which no longer exists. Change: the invariant stays, stated as behaviour — a change to the orchestrator's file protocol on its side is a change here, in lockstep; the `task-rescue` table mirrors the orchestrator's accepted set of sidecar `step` values; neither names a file, path or function; the after-texts are pinned in the spec. Spec: `.ai-factory/specs/trickster77777/0248-the-skills-mirror-the-orchestrators-protocol-without-citing-its-source.md`. [2m 44s]

## A rescue can only repair by adding

### Phase 80 — the rescue skill keeps the knowledge and the mechanics, and the repair is the agent's

Governing spec: `docs/names-and-reasons-not-laws.md`

`task-rescue` keeps what the agent lacks (artifacts, rollback states, how runs fail) as questions that decide nothing, and has grown answers: a depth per class, a menu. The repair is the agent's; a rescue writes its report and waits, paused, for the user to read it: the report is the interface, not a question. Phase note: [a rescue makes the task reflect what the system needs](.ai-factory/specs/trickster77777/0226-a-rescue-repairs-to-the-root-and-the-root-may-be-something-to-remove.md)

## A red suite written against a throwing shell has no floor

### Phase 90 — a contract-task pays only for the unit where the lifecycle hazard lives

Governing spec: none written yet.

The concurrency lens of `roadmap-decompose-skeleton` splits a contract-task off a heavy task touching two hazards; in the field it covered a whole mixed surface. A red suite against a throwing shell runs no assertion, so its coverage is judged by imagining wrong implementations, and imagination has no floor. Phase note: [a contract-task pays only for the unit that holds the hazard](.ai-factory/specs/trickster77777/0250-a-contract-task-pays-only-for-the-unit-that-holds-the-hazard.md)

## Nobody asks whether the code is ready for the tasks we wrote

### Phase 91 — the deepening asks whether the code is ready for the phase, and a preparatory phase comes first when it is not

Governing spec: `docs/philosophy/principles-at-their-moment.md`

No skill asks what shape the code needs for a phase to land as one change, nor whether it has it; when it has not, the run stops and the user inserts a preparatory phase by hand. The deepening already reads the code, so the question is asked there, and a preparatory phase comes first. Phase note: [the deepening asks whether the code is ready for the phase](.ai-factory/specs/trickster77777/0251-the-deepening-asks-whether-the-code-is-ready-for-the-phase.md)

## A find from the conversation enters a spec as if the system had asked for it

### Phase 81 — a task carries its source, and a find without one goes to the user

Governing spec: `docs/what-a-task-carries.md`

`note`'s default template carries `**Source:** conversation context`, the projects fill the slot with a skill's name, and `roadmap-decompose` asks no source, so a find from the conversation enters a spec unasked. A task answers to something the system asked for; the skills ask it where a task is written. Phase note: [a task carries its source, and a find without one goes to the user](.ai-factory/specs/trickster77777/0227-a-task-carries-its-source-and-a-find-without-one-goes-to-the-user.md)

## Two heads of one character are clones

### Phase 85 — each head has a personality of its own, a question it brings to every reading

Governing spec: `docs/paired-loop.md`

The doc states that each head has a personality of its own, a question it brings to every reading, so that two heads are not clones. The seed has no place for it and `agent-architect` does not speak of it; it is practised in the field. Phase note: [each head has a personality of its own](.ai-factory/specs/trickster77777/0244-each-head-has-a-personality-of-its-own.md)

## The active set holds what the cycle no longer uses

### Phase 94 — the active set holds only what the cycle uses

Governing spec: none written yet.

The user no longer calls `roadmap-test-coverage` or `aif-docs` («дока пишется грамотно»), and both stay in the active set. Whether each leaves `active/` or is cut down to its one question is the user's to rule.

## The cycle the doc describes is not the cycle the user runs

### Phase 95 — `skill-cycle.md` describes the cycle the user runs

Governing spec: `docs/sakshi-harness/skill-cycle.md`

The cycle the user runs has reasoning between the steps and not only at its start: reasoning, outline, reasoning, deep, docs, reasoning, decompose, a walk over each task (why it is there and whether the code is ready), skeleton per phase, orchestrator. Docs are corrected at the deepening, in the genre, with no call to `aif-docs` and no closing `aif-docs` reconciliation. A prune comes when the done tasks fill about the first 150 lines of the roadmap, read as where a done phase ends near there, 145 or 170 alike, and not at the end of each cycle. After each phase the user asks whether there are deferred observations; that habit lives in phase 89. The doc still lists the test-coverage pass as a step, runs the skeleton for heavy tasks only and not per phase, and closes every cycle with a prune and an `aif-docs` reconciliation. By the user's ruling, docs are edited at the deepening.

## A head knows the cycle only from the user's words

### Phase 96 — `agent-architect` carries the cycle and says when each partner is called

Governing spec: none written yet.

A head knows the cycle its project lives in only from the user's words, and in another team's repository the global CLAUDE.md does not travel while the architect skill does: one skill is easier to ask a team to use than a root CLAUDE.md. So `agent-architect` carries the cycle: reasoning, outline, reasoning, deepening, docs, reasoning, decomposition, a walk over each task (why it is there, whether the code is ready), skeleton per phase, orchestrator, rescue. A head that finds a phase past a skipped step mentions it in a line and goes on; a deepening may come after decomposition. The skeleton leaves no mark: the session remembers it, and the user places a compact after it. The skill also says when each partner is called, the razor after each step to look at the update, the third view after the deepening, after decomposition and at a rescue («архитектор забывает напарника позвать… фэйбла ему надо объяснить, когда его звать»); phase 85 brings the personalities into the skill, and this phase says when each is called. The user: «Скилл архитектора превращается в то, что глобальный клодмд делает для нас. Если команде не удастся навязать наш рутовый клодмд, единственный способ транслировать наше поведение - через скилл архитектора.»

## A head cannot take a rescue or a prune itself

### Phase 92 — rescue and prune are open to the agent's own call

The head that launches the orchestrator answers for the run, so it takes a rescue on a stop and a prune after it itself. With `disable-model-invocation: true` on `task-rescue` and `roadmap-prune`, only the user's slash command could call them.

- [x] **92.1 — rescue and prune are called by the agent as the other skills are** — `task-rescue` and `roadmap-prune` carry `disable-model-invocation: true` in their frontmatter, so only the user's slash command invokes them, while the head that launches the orchestrator answers for the run and must take a rescue on a stop and a prune after it itself. Change: in both `src/skills/task-rescue/SKILL.md` and `src/skills/roadmap-prune/SKILL.md` the value reads `disable-model-invocation: false`, the form the other skills use, and nothing else in either file changes; the after-texts are pinned in the spec. Spec: `.ai-factory/specs/trickster77777/0252-rescue-and-prune-are-called-by-the-agent-as-the-other-skills-are.md`.

---STOP---

## A deferred observation met again is met as if it were new

### Phase 89 — a phase carries a mark that an observation was met again, and the prune gate becomes a safety check

Governing spec: none written yet.

An observation met once is a fact and met twice is a debt, so a deferred observation worth fixing later becomes a phase through the ordinary outline, and where a phase for it already exists it gets a mark on that phase that the observation was met again. Observations are pinned as they appear, so the prune gate stops being where a pile of unpinned ones is dealt with and becomes a safety check. The user's own habit sits at the same place: after each landed phase he asks «есть отложенные наблюдения?», and it is there that the work digs deeper: «вот тут кроется самый страшный способ зарываться». The observations have surfaced real defects and have spawned work no goal needed. The mark answers it: an observation met once is pinned and parked, and one acts on it now only if it blocks the path to the user's goal or has been met again. On this side the phase would touch the roadmap format in `roadmap-engine` and the gate in `roadmap-prune`. The meaning lies in [the futures document](docs/futures/the-run-reaches-the-team-or-a-person-starts-it.md) for now. The work is wanted and not scheduled: the governing doc is written at the deepening.
