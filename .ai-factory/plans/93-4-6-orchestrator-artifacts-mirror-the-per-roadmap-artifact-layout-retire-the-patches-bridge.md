# Plan: orchestrator-artifacts: mirror the per-roadmap artifact layout; retire the `patches/` bridge

## Context
The `orchestrator-artifacts` protocol engine still documents a flat-only artifact layout and the retired `patches/` bridge. This milestone teaches §1 the per-roadmap subdirectory rule and removes `patches/` from the engine, mirroring the orchestrator's spec 13 per the amended governing spec.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Mirror the layout, retire the bridge

- [x] **Task 1: Rewrite §1 Layout with the per-roadmap rule and drop `patches/`**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  In §1 Layout (`:21`–`:29`): remove the `patches/` clause ("test mode bridges reviewer output here; empty in implement mode") entirely — nothing replaces it. Add the per-roadmap rule per spec `.ai-factory/specs/48-orchestrator-artifacts-subdir-layout-mirror.md` change #1: artifacts of the default pair (`ROADMAP.md`/`ROADMAP_TESTS.md`) live flat, byte-identical to the current wording; a named roadmap's artifacts live under a subdirectory keyed by its roadmap file stem — `roadmaps/kg-wmservice.md` → `plans/kg-wmservice/…`, same stem segment under `plan-reviews/`, `reviews/`, `test-runs/`; state that `<seq>` numbering is per-directory (each subdirectory carries its own numbering axis). Keep the section lean — a few lines of layout, not a new section. Preserve the surrounding sentences (`<seq>` assigned at plan time / not recoverable from a roadmap line; `N` = round number) intact. Do NOT touch §4's sentence "tracked artifacts belong to completed tasks, uncommitted ones to failed/in-flight" — its meaning is load-bearing for the orchestrator's resume gate and must survive verbatim. §5/§6 untouched.

- [x] **Task 2: Remove `patches` from the frontmatter description** (depends on Task 1)
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  In the frontmatter `description` (`:9`), the "Use when reading or writing plans, plan-reviews, reviews, patches, or sidecars under `.ai-factory/`" enumeration drops `patches`, reading "plans, plan-reviews, reviews, or sidecars". Verification: `grep -n "patches" src/skills/orchestrator-artifacts/SKILL.md` returns zero hits.
