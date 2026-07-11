# roadmap-prune: sweep and gate learn the per-roadmap artifact subdirectories

Governing spec: `docs/multiuser-roadmaps.md` § «Разрешение целевого файла» (amended — per-roadmap artifact subdirs); layout description: `orchestrator-artifacts` §1 as updated by spec 48. Runs after 4.4 (same file; serial within the loop) and after 4.6/spec 48 (the layout section this references).

## Current state

`src/skills/roadmap-prune/SKILL.md` sweeps and scans a flat-only layout:

- Step 5 sweep: "`rm -rf` the four artifact dirs, directly under `<target repo root>/.ai-factory/`: `plans/`, `plan-reviews/`, `reviews/`, `patches/`" — includes the retired `patches/`, and on a multiuser repo would delete **every developer's** artifacts, not the pruned roadmap's.
- Step 0 gate: "Scan every `.md` file under `plan-reviews/` and `reviews/`" — written for flat dirs; with stem-keyed subdirectories the scan must cover nested files.
- `ROADMAP_TESTS.md` parity sentence and the Step-8 report reference the same flat dirs.

## Change

1. **Sweep scoped to the pruned roadmap** (Step 5): pruning the default pair sweeps the flat dirs exactly as today (byte-stable); pruning a named roadmap sweeps only its own stem's subdirectories — `plans/<stem>/`, `plan-reviews/<stem>/`, `reviews/<stem>/` (+ `test-runs/<stem>/` in tests mode) — never the flat dirs, never a sibling stem's subdirectories (another developer's completed artifacts are not this prune's to delete).
2. **`patches/` leaves the sweep list** — the dir is retired; the list is three dirs (+ `test-runs/` in tests mode).
3. **Gate scan covers nesting** (Step 0): the `plan-reviews/`/`reviews/` scan explicitly includes subdirectory files ("every `.md` file under, at any depth"); the deferred-observations gate thereby sees all developers' unpinned entries — the gate stays repo-wide by design (prune is an integration-branch act; unresolved observations block it regardless of author).
4. Step-8 report wording follows the same layout reference; specs sweep unchanged (`Spec:` tags carry exact paths — subdir-agnostic by construction).

## Files & types

- edit `src/skills/roadmap-prune/SKILL.md` only.

## Guards

- Layout is referenced from `orchestrator-artifacts` §1, never restated in detail (the `loads:` edge already exists).
- 3.1's landed text (versioned header, self-heal, ledger semantics) and 4.4's two policy sentences untouched.
- Default-pair prune byte-stable: a solo repo sees today's behavior exactly.
- Instructions only, no rationale prose (the skill's own mandate); commit policy untouched.

## Verification

- `grep -n "patches" src/skills/roadmap-prune/SKILL.md` → zero hits.
- Dry-read both branches: default prune → flat three-dir sweep; named prune → only `<stem>/` subdirs named, sibling stems explicitly excluded.
