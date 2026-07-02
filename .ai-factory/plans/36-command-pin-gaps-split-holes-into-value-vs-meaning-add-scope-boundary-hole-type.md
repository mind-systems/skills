# Plan: command-pin-gaps: split holes into value vs meaning; add scope-boundary hole type

## Context
Restructure `src/commands/command-pin-gaps.md` so its hole taxonomy splits into **value holes** (kept: exact-value + `file:line` pinning) and **meaning holes** (new: edge behavior, open forks, unnamed invariants/interaction contracts, undrawn scope boundaries, unstated ordering — repaired by writing a missing spec clause from observed code behavior). This lets the command catch semantic gaps like the tradeoxy Phase 7 interaction-contract and scope-boundary holes that the single value-pinning move could not close.

## Settings
- Testing: no
- Logging: none
- Docs: no

## Tasks

### Phase 1: Restructure the command

- [x] **Task 1: Split the hole-finding body into two explicit classes with two repair moves**
  Files: `src/commands/command-pin-gaps.md`
  Replace the single taxonomy paragraph (current line 14) and single repair paragraph (current line 16) with two classes. **Do not touch** the Target paragraph (line 10) or the "space to fantasize" framing (line 12) — that is note 37's target logic and must stay behavior-identical.
  - **Value holes** (unchanged content, now labeled): TODO/TBD/«решим по ходу», unpinned symbols — enum names **and values**, error codes, exact strings, versions, paths, field **types** — magic numbers. Repair: read the code/proto and pin the **exact** value with a `file:line` citation; never invent. Keep the forced-deep-read intent.
  - **Meaning holes** (new, explicit): undefined behavior at the edges (error/timeout/reconnect/cancel/empty/race — **move these here** out of the value list); open forks («либо…либо») with no decision; an unnamed invariant or interaction contract between components the task touches; an undrawn **scope boundary** — which files/services are *outside* the task's zone (new hole type); unstated task ordering. Repair: write the missing constraint as a **spec clause** derived from the *observed behavior of the actual code*, citing the code that grounds it **where a concrete source exists**; when the code cannot settle it (genuine product decision), raise it under `## Blocking decisions` at the top of the file — never fabricate.
  - Preserve the existing `## Blocking decisions` escape hatch for product decisions across both classes.
  Guardrails (from note "What NOT to do"): never drop the `file:line` requirement for value holes; never require a `file:line` for a meaning hole that has no single source line (the grounding citation is "where one exists"; the clause itself is the deliverable); never let meaning-hole repair invent a product decision.

- [x] **Task 2: Extend scan-mode format to name the class; keep default mode/report** (depends on Task 1)
  Files: `src/commands/command-pin-gaps.md`
  Update the **scan mode** line format (current line 18) to name the class: `[file:line|spec-location] → value|meaning → what's missing → fix` — note the location field now allows a `spec-location` for meaning holes that have no single source line. Leave **default mode** (current line 19) behavior-identical: edit the file in place, then report `N closed from source · M blocking` — optionally split the count by class. Keep the overall file at ~20 lines: this is a rewording and reroute, not a new pipeline, so no new sections beyond the two-class restructure.

- [x] **Task 3: Align the frontmatter description with the two-class model** (depends on Task 1)
  Files: `src/commands/command-pin-gaps.md`
  Update the frontmatter `description` (lines 2–5) so it reflects both repair moves — closing value holes with a concrete value from the code **and** closing meaning holes by writing the missing constraint as a spec clause — rather than only "close each one now with a concrete value read from the actual code/proto". Keep it concise; leave `argument-hint` and `allowed-tools` unchanged (no new tools are required).

## Notes
- Single small file (~20 lines); all changes are contained in `src/commands/command-pin-gaps.md`. Fewer than 5 tasks → single commit at the end, no commit-plan checkpoints needed.
- This command lives under `src/commands/` and is symlinked into the active set; do not touch `upstream/ai-factory/`.
