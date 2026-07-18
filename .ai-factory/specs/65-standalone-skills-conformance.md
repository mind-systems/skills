# Standalone skills: grep-audit and conform to one dictionary

Task 17.4 of the One-dictionary direction. Governing spec: [reserved-words](../../docs/reserved-words.md). Naming-only; the loners sit mostly outside the roadmap vocabulary, so this is a grep-audit — "no change" is a legal outcome per skill.

## Current state — per-file audit (line numbers from the 2026-07-13 grep; re-verify by grep before editing)

**`detangle` (123 lines)** — `milestone` (33, "in-progress or planned roadmap milestone?") → **`task`** (the roadmap unit under discussion for impact analysis). **Leave** "field" (15 "a field — exists at a specific level of the tree", 42 "file, function, class, field, endpoint" — both generic code-elements).

**`temporal-tree` (172 lines)** — **audit-clean under the plain-form contract**: its `named roadmap` spellings (73, 87, 89) and attributive `named-roadmap resolution` (24, 71) are ordinary English; re-audit, expect no change.

**`aif` (249 lines)** — no synonym tokens. **Audit-clean → no change.**

**`aif-architecture` (169 lines)** — no synonym tokens. **Audit-clean → no change.**

**`observe-logs` (174 lines)** — only "fields" (24) — generic (log fields). **No change.**

**`command-handoff` (122 lines)** — only "field" (81, generic data-field example). **No change.**

**`command-commit-roadmap-update` (17 lines)** — no synonym tokens. **Audit-clean → no change.**

**`aif-skill-generator` — EXCLUDED.** `active/skills/aif-skill-generator` is a symlink into `upstream/ai-factory/aif-skill-generator` — an upstream-pristine mirror we never hand-edit (editing it breaks the conflict-free sync split). Not in scope; leave it exactly as upstream ships it.

## Change

Expected single edit: `roadmap milestone` → `task` in `detangle`. Behavior byte-identical. Every other skill in the task is certified clean, no edit.

## Files & types

`src/skills/detangle/SKILL.md` (the one expected edit); the rest audited only. Frontmatter `loads:` untouched (temporal-tree keeps `loads: roadmap-engine`).

## Guards

- **`aif-skill-generator` is upstream — never edited.** It is the one upstream original in the active set; conformance stops at our own `src/`.
- **Spelling is ordinary English.** Attributive hyphens and sentence-position capitals stay; only synonyms conform.
- **Generic `field`/`fields` left** — every occurrence above is a code/data-field, not the skill description field.
- **"No change" is a legal per-skill outcome** — the audit certifies, it does not manufacture work.
- `loads:` edges + reverse-graph markers byte-identical; `` Spec: `` / `Governing spec:` tags legacy; behavior byte-identical.

## Verification

- `grep -inE '[^-]milestones?' src/skills/detangle/SKILL.md` → zero.
- `grep -inE 'spec note|[^-]milestones?' src/skills/{temporal-tree,aif,aif-architecture,observe-logs}/SKILL.md src/commands/{command-handoff,command-commit-roadmap-update}.md` → zero (audit-clean, no edit made).
- `git status` shows no change under `upstream/` — `aif-skill-generator` untouched.
