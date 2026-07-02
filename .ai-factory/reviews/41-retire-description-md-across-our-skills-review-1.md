# Code Review: Retire DESCRIPTION.md across our skills

**Scope:** `git diff HEAD` — 10 modified source files (skill bodies + one config template + one Node script) plus planning artifacts.
**Risk Level:** 🟢 Low — pure deletion of read instructions and one dead config key; no runtime logic added.

## What changed

Content-only deletions of "Read `.ai-factory/DESCRIPTION.md`" instructions and mentions across our `src/` skills, plus removal of the now-dead `paths.description` config key from the `aif` config machinery. `upstream/ai-factory/` untouched. No `read CLAUDE.md` replacements added (correct — CLAUDE.md is auto-loaded).

## Verification performed

- **Full-tree sweep** — `grep -rn DESCRIPTION` over `.md`/`.yaml`/`.mjs`, excluding `upstream/` and historical `.ai-factory/{notes,plans,plan-reviews,reviews}`: **zero hits**. Every live reference in the plan's edit set is gone; nothing was missed.
- **`update-config.mjs` (read in full)** — the script is entirely data-driven by `SECTION_KEYS`. `ALLOWED_PATHS` (33–35), `parseTemplate` (382–417), `parseSection` (297–352), and `applyUpdates` (587–609) all derive their key set from `SECTION_KEYS` by iteration; there is **no** hard-coded `'description'` anywhere else in the file. Removing `'description'` from `SECTION_KEYS.paths` (line 8) is therefore internally consistent:
  - `parseTemplate` no longer requires a `paths.description` block in the template — matching the deletion from `config-template.yaml`. The `fail(3, "Template is missing managed key…")` path the plan-reviews flagged is now avoided, not triggered.
  - `ALLOWED_PATHS` no longer contains `paths.description`, so a stray `--payload` carrying it would be rejected — but grep confirms no such payload exists in `src/`, and the `aif` SKILL.md `description` hits are all the *project-description argument* concept, not the config key.
- **Atomic coupling honored** — the three coupled edits (`config-template.yaml` key, `update-config.mjs` `SECTION_KEYS` entry, and aif-docs `paths.description` resolution) are all present in the same diff, exactly as the plan's Commit 2 required. The schema and both consumers stay in sync.
- **Merge-mode safety** — against an older project `config.yaml` that still carries `paths.description`, `parseSection` (308) simply `continue`s past the now-unmanaged key; it is left in place untouched, no crash. Correct and out of this task's `src/`-only scope.

## Per-file check

- **roadmap-engine** — Step 0 DESCRIPTION block removed, ARCHITECTURE block now leads; Update-mode sentence reads cleanly ("`$TARGET_FILE` and a brief codebase check…"). No dangling reference.
- **roadmap-outline** — vision line now "sourced from user input"; surrounding optional-note guidance intact. Prose wraps mid-paragraph but renders as one paragraph — cosmetic only.
- **roadmap-decompose-skeleton / roadmap-test-coverage** — DESCRIPTION list item and conditional removed; stack inference from package-manager files is now unconditional. `$STACK` still sourced (ARCHITECTURE + package files).
- **aif-docs** — all five points cleaned (config-resolution bullet, defaults list, THEN read block, Artifact-Ownership Config-use and Read-only-context lines); ARCHITECTURE handling preserved.
- **detangle** — DESCRIPTION paragraph gone, ARCHITECTURE/ROADMAP paragraphs kept.
- **aif-plan** (SKILL.md + EXAMPLES.md) — Step 0 now leads with ARCHITECTURE ("FIRST:"), skip-line rephrased generically, example line updated.
- **aif config machinery** — template block and `SECTION_KEYS` entry removed together.

## Findings

None. The change is complete, consistent, and free of runtime breakage — the one non-obvious failure mode (template/`SECTION_KEYS` desync hard-failing the next `/aif` run) was correctly avoided by editing both sides atomically.

REVIEW_PASS
