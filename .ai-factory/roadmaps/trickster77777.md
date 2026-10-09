> Owner: trickster77777@gmail.com

# Skills Roadmap

> Generic AI Factory skills — reusable slash-command packages for Claude Code.

## The lenses are missing from the skill description field

### Phase 79 — the lenses carry their descriptions in the field and the hand can load one

Governing spec: `docs/skill-description-field.md`

The planning lenses carry `disable-model-invocation: true`, so the skill description field lacks them and no agent can load them. The flag goes; `agent-architect`, `roadmap-test-coverage`, `roadmap-prune` and `task-rescue` stay out, since what each does is reviewed only before it happens. Phase note: [the lenses carry their descriptions in the field and the hand can load one](.ai-factory/specs/trickster77777/0221-the-lenses-carry-their-descriptions-in-the-field-and-the-hand-can-load-one.md)

- [ ] **79.1 — the field's doc says which skills stand outside it, and why** — `docs/skill-description-field.md` describes the field as "the `description:` of every skill in the family", yet skills whose work is reviewed only before it happens carry `disable-model-invocation: true` and are not in it, the planning lenses' additive writes being reviewed after, and `docs/always-loaded-discipline.md` repeats "every skill's `description:`". Change: where the doc says what the field holds it states that a skill whose work is reviewed only before it happens, with the user present, and never after, is called by the user alone and stays out; the discipline doc's phrase takes the same words, "each skill the agent may call on its own"; the after-texts are pinned verbatim in the spec. Spec: `.ai-factory/specs/trickster77777/0228-the-fields-doc-says-which-skills-stand-outside-it-and-why.md`.
- [ ] **79.2 — the planning lenses enter the skill description field** — `roadmap-outline`, `roadmap-outline-deep`, `roadmap-decompose` and `roadmap-decompose-skeleton` carry `disable-model-invocation: true`, so their descriptions are absent from the field `docs/skill-description-field.md` leans on, and no agent, the hand included, can load them through the `Skill` tool. Change: the flag reads `false` in each frontmatter, the way the engines carry it; the descriptions join every session's field, the orchestrator's agents' too. Spec: `.ai-factory/specs/trickster77777/0229-the-planning-lenses-enter-the-skill-description-field.md`.

## Architects are per user, and their folders are not

### Phase 76 — a head's folder lives under its user's slug

Governing spec: `docs/paired-loop.md`

Architects are per user, as named roadmaps are, but the skills still found a head at a flat `.ai-factory/architects/<NN>/` and find a peer by number alone. The engine's path and numbering, the probe, the peer and team passages and the seed's `## Team` take the user's `<slug>` folder. Phase note: [a head's folder lives under its user's slug](.ai-factory/specs/trickster77777/0213-a-heads-folder-lives-under-its-users-slug.md)

## A long-lived editor loses its working knowledge at a moment nobody chooses

### Phase 78 — the hand writes its own snapshot and a new hand carries on from it

Governing spec: `docs/paired-loop.md`

An editor loses its working context at a moment nobody chooses: the snapshot is the head's alone, and a fresh hand follows only a dead one. The hand writes its own in `editor/`, beside the head's `architect/`, and a new hand starts from it. Decomposed after 76 and the first field trial, run once 77 is decomposed. Phase note: [the hand writes its own snapshot and a new hand carries on from it](.ai-factory/specs/trickster77777/0215-the-hand-writes-its-own-snapshot-and-a-new-hand-carries-on.md)

## A rescue can only repair by adding

### Phase 80 — a rescue makes the task reflect what the system needs

Governing spec: `docs/what-a-task-carries.md`

Every rescue root cause is phrased as a constraint to add, every standard depth edits the spec, and propagation offers the same clause to open tasks, so a rescue only adds. A rescue should make the task reflect what the system needs, whatever that takes. Phase note: [a rescue makes the task reflect what the system needs](.ai-factory/specs/trickster77777/0226-a-rescue-repairs-to-the-root-and-the-root-may-be-something-to-remove.md)

## A find from the conversation enters a spec as if the system had asked for it

### Phase 81 — a task carries its source, and a find without one goes to the user

Governing spec: `docs/what-a-task-carries.md`

`note`'s default template carries `**Source:** conversation context`, the projects fill the slot with a skill's name, and `roadmap-decompose` asks no source, so a find from the conversation enters a spec unasked. A task answers to something the system asked for; the skills ask it where a task is written. Phase note: [a task carries its source, and a find without one goes to the user](.ai-factory/specs/trickster77777/0227-a-task-carries-its-source-and-a-find-without-one-goes-to-the-user.md)

---STOP---
