# global CLAUDE.md: drop the nav / See-Also bans — the positive link rule displaces them

## Current state

`src/global/CLAUDE.md` § "Documentation style" carries two prohibition bullets — "**No prev/next navigation links.**" and "**No 'See Also' sections.**" — born as a counter-measure against the upstream `aif-docs`, which used to mandate both forms. That source is gone: `grep -rn -i "see also|prev/next|← Previous|nav header" src/` (excluding the global CLAUDE.md itself) returns zero — the skill family contains no trace of either form. The bans now cut the other way: a prohibition keeps the prohibited concept loaded — every session reads "no nav headers" and thereby receives the very idea of nav headers. Meanwhile task 22 adds the positive rule ("Docs form a walkable tree… inline links… at the moment they are load-bearing"), which entails both bans as a consequence: a ceremonial link section is a non-load-bearing edge.

## Change

- `src/global/CLAUDE.md` § "Documentation style": **delete the two bullets** — "No prev/next navigation links." and "No 'See Also' sections." — leaving the remaining bullets untouched and unrenumbered (they are unnumbered dashes).
- `docs/context-tree.md` § "Ссылки — рёбра, по которым ходят": rephrase the one sentence that names both banned forms — keep the reasoning ("рёбра без нагрузки засоряют граф, ничего не соединяя") but drop the named forms ("навигационные шапки", "«See Also»") so the doc carries the positive rule without seeding the patterns it displaced.

## Files & types

- edit `src/global/CLAUDE.md` (§ Documentation style, −2 bullets)
- edit `docs/context-tree.md` (one sentence rephrased in place)

## Guards

- **Depends on task 22** — the positive walkable-tree bullet must already be in § Documentation style before the bans are removed; the removal is a displacement, not a bare deletion.
- All other Documentation-style bullets byte-identical (behavior-not-code, no trees, language matching, no README table, current-state-only).
- No replacement prohibition is added anywhere — the point is that the named forms disappear from the loaded context entirely.

## Verification

- `grep -rn -i "see also\|prev/next\|← Previous\|nav" src/global/CLAUDE.md docs/context-tree.md` → zero matches.
- § Documentation style still contains the task-22 walkable-tree bullet and the five untouched bullets.
- `docs/context-tree.md` still explains load-bearing-only edges — with no banned form named.
