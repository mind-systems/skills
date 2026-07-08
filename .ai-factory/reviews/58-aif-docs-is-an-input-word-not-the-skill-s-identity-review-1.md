# Review: aif-docs: ТЗ is an input word, not the skill's identity

## Scope
Behavior-identical rename/reframe pass over `src/skills/aif-docs/SKILL.md`. Reviewed the full `git diff HEAD`, the complete SKILL.md, the spec (`.ai-factory/specs/12-aif-docs-tz-input-not-identity.md`), and the plan.

## Verification against spec

- **`:3` frontmatter `description`** — matches the pinned string byte-for-byte: "living ТЗ —" lead dropped, governing-spec gloss kept, trigger list extended with `"напиши ТЗ"` and `"техническое задание"`. ✅
- **`:13` H1 title** — now `# Documentation Generator`, exactly as pinned. ✅
- **`:15` identity paragraph** — both ТЗ occurrences replaced; reads with `**governing spec**` and "exception to that genre". Matches pinned string. ✅
- **`:19` Core Principles opener** — both ТЗ occurrences replaced with "governing-spec genre" / "exempt from that genre". Matches pinned string. ✅

## Guards

- **ТЗ containment** — `grep -rin "ТЗ" src/skills/aif-docs/SKILL.md src/skills/aif-docs/references/` returns exactly one hit: the `:3` description trigger list. Zero in H1, identity paragraph, Core Principles, body, or `references/`. ✅
- **Referent-conditional dual-write logic untouched** — the diff is confined to lines 1–3 and 13–19; Step 1 (`:70`), Step 2.1 staleness (`:318`), Step 4 Technical Accuracy checks (`:369-374`) never appear in the diff. The ahead-of-code / shipped-behavior capability is intact. ✅
- **`references/` untouched** — `git diff --stat` shows only `SKILL.md` changed (4 insertions / 4 deletions). ✅
- **No new mode / lead-lag meta / fork / size / state-machine / `--web` / checklist changes.** Reframe-only. ✅
- **Upstream mirror untouched** — no change under `upstream/ai-factory/`. ✅

## Correctness / runtime concerns
No code, no runtime surface — this is skill instruction text. Frontmatter YAML remains valid: the `description` is a single unquoted scalar with no YAML-breaking characters introduced (em dashes and quoted trigger phrases were already present in the prior version). `argument-hint` still quoted. No structural or parsing regressions.

## Findings
None.

REVIEW_PASS
