> Owner: trickster77777@gmail.com

# Skills Roadmap

> Generic AI Factory skills — reusable slash-command packages for Claude Code.

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
