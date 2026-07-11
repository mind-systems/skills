# Plan: doctrine: the time map branches — global CLAUDE.md sentence + context-tree paragraph

## Context
Teach the loaded doctrine that named roadmaps under `.ai-factory/roadmaps/` branch the time map: one normative sentence in the global CLAUDE.md and one mirroring narrative paragraph in `docs/context-tree.md`, additions only per the 1.16 pattern.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Doctrine edits

- [x] **Task 1: Append the time-branches sentence to the global CLAUDE.md**
  Files: `src/global/CLAUDE.md`
  In § "Grounding claims", at the end of the roadmap/time paragraph (currently ending "…the two maps together orient a cold session before any skill is invoked.", the paragraph beginning "When the project has `.ai-factory/ROADMAP.md`, it is the entry map of **time**…"), append **one new sentence** to that same paragraph. The sentence must name all four elements the spec's Verification requires, in one sentence: named roadmaps under `.ai-factory/roadmaps/` are branches of the time map (per-developer working buffers, each with an `> Owner:` first line); the project's present is the **union of their `[x]`/`[ ]` seams**; and entry into a multiuser project starts by enumerating that directory. This is the normative home of the rule (one home per fact) — no link needed here. **Additions only:** every existing sentence in the file stays byte-identical; `git diff` must show a pure insertion.

- [x] **Task 2: Append the time-branches paragraph to context-tree.md**
  Files: `docs/context-tree.md`
  In § «Две карты входа — время и пространство», immediately after the existing карта-времени paragraph (the one ending "…так что история остаётся проходимой, не загромождая карту.", line 17), insert **one new Russian paragraph** mirroring the doctrine narratively — not a copy of the normative rule. It covers: ветки времени (именованные роадмапы под `.ai-factory/roadmaps/`), ствол-Features (единая уплотнённая история), and прун на интеграционной ветке как мерж времени; state that the project's present is the объединение швов `[x]`/`[ ]` всех живых роадмапов. Carry the narrative + link only (one home per fact): link `docs/multiuser-roadmaps.md` as the governing spec via an inline Markdown link at the load-bearing point, matching the doc's existing link style (e.g. `[Мультиюзерность — именованные роадмапы](multiuser-roadmaps.md)`). Match the file's Russian and prose register; do not add a directory tree or a fields/methods list. **Additions only:** existing text byte-identical; `git diff` shows a pure insertion.

## Notes
- Ground the wording against the governing spec `docs/multiuser-roadmaps.md` § «Ось времени» — do not paraphrase it from memory when implementing.
- No skill edits in this milestone (the mechanism lives in specs 43–46); scope is exactly these two files.
