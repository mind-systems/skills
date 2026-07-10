# Review: 1.2 — global CLAUDE.md: drop the nav / See-Also bans

## Scope
Code changes in `src/global/CLAUDE.md` and `docs/context-tree.md` (per `git diff HEAD`). The other staged files are planning artifacts (ROADMAP, plan, plan-review, plan JSON) — not code under review.

## Findings

Both edits match the plan and the spec (`.ai-factory/specs/23-global-drop-nav-see-also-bans.md`) exactly.

- **Task 1 — `src/global/CLAUDE.md`:** The two prohibition bullets (`No prev/next navigation links`, `No "See Also" sections`) are removed. The remaining § "Documentation style" bullets are byte-identical and correctly ordered: the task-22 walkable-tree bullet plus the five untouched bullets (`Describe behavior, not code`, `No file/directory trees`, `Match the language of existing docs`, `No README documentation table`, `Describe current state only`). No replacement prohibition was introduced.

- **Task 2 — `docs/context-tree.md`:** The sentence in § "Ссылки — рёбра, по которым ходят" drops both named forms ("навигационные шапки", "«See Also»") while preserving the load-bearing-edges reasoning verbatim ("рёбра без нагрузки, которые засоряют граф, ничего в нём не соединяя"). The rewrite still contrasts a load-bearing link placement against ceremonial link sections ("собранных ради самого жеста ссылки") without naming a displaced form. Russian register and surrounding sentences untouched; only the one sentence changed.

## Verification
- `grep -rn -i "see also\|prev/next\|← Previous\|nav" src/global/CLAUDE.md docs/context-tree.md` → zero matches (exit 1). Cyrillic "навигационной" does not match the Latin `nav` pattern.
- § "Documentation style" retains the walkable-tree bullet and the five untouched bullets.
- `docs/context-tree.md` still explains load-bearing-only edges with no banned form named.
- Cross-reference integrity: § "Где что нормировано" (line 29) still cites § "Documentation style" as the home of link-form rules — the retained walkable-tree bullet keeps that pointer valid.

No correctness, security, or runtime concerns — this is a documentation/instruction text change with no executable surface.

REVIEW_PASS
