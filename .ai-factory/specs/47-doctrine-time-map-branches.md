# Doctrine: the time map branches — global CLAUDE.md sentence + context-tree paragraph

Governing spec: `docs/multiuser-roadmaps.md` § «Ось времени». The 1.16 pattern: additions only, existing text byte-identical.

## Current state

- `src/global/CLAUDE.md` § "Grounding claims" defines the single time map: "When the project has `.ai-factory/ROADMAP.md`, it is the entry map of **time**: the seam between `[x]` and `[ ]` is where the project lives now…". A session entering a multiuser project has no loaded rule for what `.ai-factory/roadmaps/` is or where the present lives when the map branches.
- `docs/context-tree.md` mirrors the doctrine narratively (карта времени — `ROADMAP.md`); no time-branching layer exists there either.

## Change

1. **One sentence appended** to the roadmap passage of § "Grounding claims" in `src/global/CLAUDE.md` (target wording; final text pinned at implementation against the ТЗ): named roadmaps under `.ai-factory/roadmaps/` are branches of the time map — per-developer working buffers with an `> Owner:` first line; the project's present is the **union of their `[x]`/`[ ]` seams**, and entry into a multiuser project starts by enumerating that directory.
2. **One paragraph appended** to `docs/context-tree.md`'s карта-времени passage (Russian, matching the doc): ветки времени / ствол-Features / прун на интеграционной ветке как мерж времени — linking `docs/multiuser-roadmaps.md` as the governing spec.

## Files & types

- edit `src/global/CLAUDE.md`, `docs/context-tree.md`.

## Guards

- Additions only — every existing sentence in both files byte-identical (the 1.16 contract).
- One home per fact: the normative rule lands in the global CLAUDE.md; context-tree carries the narrative and the link, никогда copy.
- No skill edits here; the mechanism lives in specs 43–46.

## Verification

- `git diff` on both files shows pure insertions.
- The global sentence names: `roadmaps/`, the owner line, the seam union, directory enumeration as entry — all four, in one sentence.
