# orchestrator-artifacts: mirror the per-roadmap artifact layout; retire the `patches/` bridge

Governing spec: `docs/multiuser-roadmaps.md` § «Разрешение целевого файла» (as amended — per-roadmap artifact subdirectories). Layout source of truth: the orchestrator's own change, `~/projects/orchestrator/.ai-factory/specs/13-artifact-subdirs.md`. This is the §7 mirrors-the-orchestrator invariant firing: the protocol changed there, the mirror updates here.

## Current state

`src/skills/orchestrator-artifacts/SKILL.md` describes a flat-only layout and a retired mechanism:

- `:25` — §1 Layout names `patches/` with "test mode bridges reviewer output here; empty in implement mode" — the bridge was retired by orchestrator task 02 (pre-existing drift, found while mirroring).
- `:9` — the frontmatter description enumerates "plans, plan-reviews, reviews, patches, or sidecars".
- §1 knows nothing of per-roadmap subdirectories: a named roadmap's artifacts land under a subdirectory keyed by the roadmap file stem, and the flat description would misroute every reader of a multiuser repo.

## Change

1. **§1 Layout gains the per-roadmap rule:** artifacts of the default pair (`ROADMAP.md`/`ROADMAP_TESTS.md`) live flat, byte-identical to today; a named roadmap's artifacts live under a subdirectory keyed by its file stem — `roadmaps/kg-wmservice.md` → `plans/kg-wmservice/…`, same segment under `plan-reviews/`, `reviews/`, `test-runs/`; `<seq>` numbering is per-directory (each subdirectory has its own axis — the very point of the split).
2. **`patches/` vanishes** from §1 and from the frontmatter description; nothing replaces it.
3. §4's sentence — "tracked artifacts belong to completed tasks, uncommitted ones to failed/in-flight" — is now load-bearing for the orchestrator's resume-adoption gate (its spec 14): the sentence's meaning must survive any rewording, best left verbatim.

## Files & types

- edit `src/skills/orchestrator-artifacts/SKILL.md` only.

## Guards

- This engine is loaded by `milestone-rescue`, `milestone-rescue-audit`, `roadmap-prune` (reverse graph via `grep -l "orchestrator-artifacts"`) — their procedures read layout from here; the mirror update must stay descriptive protocol, no procedure added.
- §5/§6 (deferred observations, marker grammar) untouched.
- ≤ the engine's lean size — this is a few lines of layout, not a section.

## Verification

- `grep -n "patches" src/skills/orchestrator-artifacts/SKILL.md` → zero hits.
- §1 names both layouts (flat default pair, stem-keyed subdirectories) and per-directory numbering; §4 sentence intact.
