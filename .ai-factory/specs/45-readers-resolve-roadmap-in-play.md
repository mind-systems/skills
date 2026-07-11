# Readers resolve the roadmap in play: rescue, pin-gaps, test-coverage, temporal-tree

Governing spec: `docs/multiuser-roadmaps.md`. Depends on spec 43 (the engine section this task points at).

## Current state

The reading/operating skills each know only the default pair:

- `src/skills/milestone-rescue/SKILL.md:177-179` — "Determine `$TARGET_FILE`": test-keyword slugs → `.ai-factory/ROADMAP_TESTS.md`, else the default roadmap; an argument-named file wins. A milestone from a named roadmap resolves to the wrong file.
- `src/commands/command-pin-gaps.md:13` — final fallback: open `- [ ]` tasks above `---STOP---` in the literal `.ai-factory/ROADMAP.md`.
- `src/skills/roadmap-test-coverage/SKILL.md:29` — "`ROADMAP.md` (or `$ARGUMENTS` if provided)".
- `src/skills/temporal-tree/SKILL.md` — literal `.ai-factory/ROADMAP.md` mentions (grep at execution time; the file is in flux).

## Change

One rule, four sites — each names the engine's resolution (argument → my → default) instead of its bare literal:

- **rescue:** `$TARGET_FILE` resolution gains the named tier; the test-keyword branch maps a named roadmap to `.ai-factory/roadmaps/<slug>-tests.md`, the default to `.ai-factory/ROADMAP_TESTS.md` as today.
- **pin-gaps:** the fallback becomes "open tasks of the roadmap in play per the engine's resolution".
- **test-coverage:** the Layer-1 input line names the resolution.
- **temporal-tree:** literal path mentions widened to "the roadmap in play"; reconstruction commands take the resolved path.

## Files & types

- edit `src/skills/milestone-rescue/SKILL.md`, `src/commands/command-pin-gaps.md`, `src/skills/roadmap-test-coverage/SKILL.md`, `src/skills/temporal-tree/SKILL.md`.

## Guards

- Procedures byte-identical otherwise: rescue's depth menu, rollback variants, sidecar `step` table and artifact discovery; coverage's 8 layers and Class A/B table; pin-gaps' hole taxonomy and `## Blocking decisions`; temporal-tree's walk order.
- Resolution referenced, never restated (one home: spec 43's engine section).
- Behavior without `roadmaps/` identical to today at all four sites.

## Verification

- Each file's diff touches only target-resolution wording.
- Rescue dry-run on a default-roadmap milestone resolves `$TARGET_FILE` exactly as today.
