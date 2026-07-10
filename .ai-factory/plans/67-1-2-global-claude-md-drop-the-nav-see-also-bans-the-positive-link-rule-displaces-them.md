# Plan: 1.2 — global CLAUDE.md: drop the nav / See-Also bans — the positive link rule displaces them

## Context
Task 22's positive walkable-tree rule ("inline links only at load-bearing moments") already entails both prohibitions, and the upstream `aif-docs` source they countered is gone — so the two ban bullets now only keep the prohibited concept loaded into every session. This milestone removes them, leaving no replacement prohibition.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Remove the displaced bans

- [x] **Task 1: Delete the two prohibition bullets from the global CLAUDE.md**
  Files: `src/global/CLAUDE.md`
  In § "Documentation style", delete exactly these two consecutive bullets (currently lines 22–23):
  - `- **No prev/next navigation links.** Never add ` `[← Previous](...)` ` / ` `[Next →](...)` ` header navigation to doc files — it's useless clutter.`
  - `- **No "See Also" sections.** Never add a "See Also" footer to doc files.`
  Leave every other bullet in the section byte-identical and in place — including the task-22 walkable-tree bullet (`**Docs form a walkable tree.**`) and the five untouched bullets (`Describe behavior, not code`, `No file/directory trees`, `Match the language of existing docs`, `No README documentation table`, `Describe current state only`). Add no replacement prohibition anywhere. The bullets are unnumbered dashes, so nothing needs renumbering.

- [x] **Task 2: Rephrase the one sentence in `docs/context-tree.md` that names both banned forms**
  Files: `docs/context-tree.md`
  In § "Ссылки — рёбра, по которым ходят" (the sentence at line 25 beginning "Инлайн-ссылка ставится в несущем месте…"), drop the two named patterns — "навигационные шапки" and "«See Also»" — while keeping the load-bearing-edges reasoning intact ("рёбра без нагрузки, которые засоряют граф, ничего в нём не соединяя"). The rewritten sentence must still contrast a link placed at a load-bearing moment against ceremonial link sections in general, without naming either displaced form. Keep the surrounding sentences and the Russian register untouched; edit only this sentence in place. Introduce no new prohibition wording.

## Verification (for the implementer)
- `grep -rn -i "see also\|prev/next\|← Previous\|nav" src/global/CLAUDE.md docs/context-tree.md` → zero matches.
- § "Documentation style" still contains the task-22 walkable-tree bullet plus the five untouched bullets.
- `docs/context-tree.md` still explains load-bearing-only edges, with no banned form named.
