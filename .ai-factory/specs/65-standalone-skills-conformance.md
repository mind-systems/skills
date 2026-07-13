# Standalone skills: grep-audit and conform to the reserved-words contract

Phase 12 of the Language-integration direction. Governing spec: [reserved-words](../../docs/reserved-words.md). Vocabulary-only; the loners sit mostly outside the roadmap vocabulary, so this is a grep-audit — "no change" is a legal outcome per skill.

## Current state — per-file audit (grep, 2026-07-13)

**`detangle` (123 lines)** — `milestone` (33, "in-progress or planned roadmap milestone?") → **`task`** (the roadmap unit under discussion for impact analysis). **Leave** "field" (15 "a field — exists at a specific level of the tree", 42 "file, function, class, field, endpoint" — both generic code-elements, not `skill-description-field`).

**`temporal-tree` (172 lines)** — `named roadmap` / `Named roadmap` (73, 87, 89) → **`named-roadmap`**.

**`aif` (249 lines)** — no reserved-word tokens. **Audit-clean → no change.**

**`aif-architecture` (169 lines)** — no reserved-word tokens. **Audit-clean → no change.**

**`observe-logs` (174 lines)** — only "fields" (24) — generic (log fields). **No change.**

**`command-handoff` (122 lines)** — only "field" (81, "field Z lives on the entity, not in params" — a generic data-field example). **No change.**

**`command-commit-roadmap-update` (17 lines)** — no reserved-word tokens. **Audit-clean → no change.**

**`aif-skill-generator` — EXCLUDED.** `active/skills/aif-skill-generator` is a symlink into `upstream/ai-factory/aif-skill-generator` — an upstream-pristine mirror we never hand-edit (editing it breaks the conflict-free sync split). Not in scope; leave it exactly as upstream ships it.

## Change

Only two files are touched: rename `roadmap milestone` → `task` in `detangle` and `named roadmap` → `named-roadmap` in `temporal-tree`. Behavior byte-identical. Every other skill in the phase is certified clean, no edit.

## Files & types

`src/skills/detangle/SKILL.md`, `src/skills/temporal-tree/SKILL.md`. Frontmatter `loads:` untouched (temporal-tree keeps `loads: roadmap-engine`).

## Guards

- **`aif-skill-generator` is upstream — never edited.** It is the one upstream original in the active set; conformance stops at our own `src/`.
- **Generic `field`/`fields` left** — every occurrence above (detangle 15/42, observe-logs 24, command-handoff 81) is a code/data-field, not the `skill-description-field` reserved word.
- **"No change" is a legal per-skill outcome** — five of the eight land no edit; the audit certifies them, it does not manufacture work.
- `loads:` edges + reverse-graph markers byte-identical; `` Spec: `` / `Governing spec:` tags legacy; behavior byte-identical.

## Verification

- `grep -inE '[^-]milestones?|named roadmap' src/skills/detangle/SKILL.md src/skills/temporal-tree/SKILL.md` → zero.
- `grep -inE 'spec note|contract line|milestone|named roadmap|governing spec' src/skills/{aif,aif-architecture,observe-logs}/SKILL.md src/commands/{command-handoff,command-commit-roadmap-update}.md` → zero (audit-clean, no edit made).
- `git status` shows no change under `upstream/` — `aif-skill-generator` untouched.
