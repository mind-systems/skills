# Phase 50 — the documentation catches up with what the skills now do

What still diverges, by file and heading:

- **`docs/sakshi-harness/skill-graph.md`, § "Воронка в один дистиллятор".** It names `command-handoff` as the one direct caller of `note`: "`command-handoff` зовёт `note` напрямую". `roadmap-outline-deep` also passes its own destination, template and verbosity hooks to `note` without going through `roadmap-engine`.
- **`docs/sakshi-harness/skill-cycle.md`, § "Уборка и сверка — `roadmap-prune` → `aif-docs`".** It states what prune deletes as "вместе с отработавшими артефактами и их task-spec", and prune also deletes the phase notes its preambles point at.
- **The gap pass's zone, in two places.** The diagram line "закрыть места угадывания" in `skill-cycle.md`, § "Схема", and "(close the places an implementer would guess at)" in `docs/skill-description-field.md` say "close", while the command also routes what it may not close to a named owner and raises fundamental conflicts as blockers. Neither is a specification of the command, so nothing breaks on the facts; the zone wants stating as close-or-route.
- **`docs/philosophy/multiuser-roadmaps.md`, § "Разрешение целевого файла в семье скиллов".** It says a task spec is always resolved through the contract line's `Spec:` tag. The same directory also holds phase notes, resolved through a `Phase note:` pointer and sharing the directory's `<NN>` counter, so the section names one resolution path where two exist.
- **The global CLAUDE.md, § "Planning workflow".** Its planning chain reads "`/roadmap-outline` → `/roadmap-decompose` (plus `/roadmap-decompose-skeleton` on heavy tasks)" and omits `roadmap-outline-deep`, the step between them; this is the always-loaded surface, where `skill-cycle.md` is not loaded.
- **This repository's CLAUDE.md, § "Upstream Sync".** Its "Everything else in `src/skills/` is ours" list omits `orchestrator-artifacts`, which lives in `src/skills/`, has no upstream counterpart and is linked into the active set.

What no longer diverges. The claim that `skill-cycle.md` pairs `roadmap-outline-deep` with the gap pass as a code-tier symmetry the skill did not hold is settled: Step 0 of `roadmap-outline-deep` now reads the code the phase is about, down to the leaf. The claim that the document names the orchestrator's planner and reviewer as readers of a phase note is settled: the sentence was corrected, and they reach a note only through a spec that names it. The order the earlier text gave for `roadmap-outline-deep` against `aif-docs` is settled: `skill-cycle.md` now puts the deep pass before the documents are written.

Nothing under `docs/` is written by this phase's own note.
