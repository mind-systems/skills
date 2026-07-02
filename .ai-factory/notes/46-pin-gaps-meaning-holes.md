# command-pin-gaps: two hole classes — value holes and meaning holes — with two repair moves

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review + tradeoxy Phase 7 incident)

## Key Findings

- `src/commands/command-pin-gaps.md` lists a hole taxonomy dominated by **value-shaped holes** (enum names and values, error codes, exact strings, versions, paths, field types, magic numbers) and prescribes a **single repair move**: "go read the code/proto and pin the exact value with a `file:line` citation". Semantic holes (open forks, unspecified edge cases) are in the list but get funneled through the same value-pinning move, which does not fit them.
- The command's actual intent (user's): find the **logical** places in specs where the implementing agent would have to invent *meaning* — not just missing literals.
- Live evidence (tradeoxy Phase 7): the failure-causing holes were an unspecified interaction **contract** (release/re-acquire interleaving on a shared stream entry) and an undrawn **scope boundary** (`OrdersStreamService` out of the task's zone). Neither is a value; no `file:line` pin closes them — their repair is a missing constraint sentence in the spec. The current command would scan that spec note and find nothing.
- The `file:line` rigor has proven side value — forcing the agent to actually read files surfaces unexpected details — so it stays for value holes and as grounding evidence wherever a concrete source exists.

## Details

Restructure the hole search and repair into two classes:

- **Value holes** (unchanged): TODO/TBD/«решим по ходу», unpinned symbols — enum names **and values**, error codes, exact strings, versions, paths, field **types** — magic numbers. Repair: read the code/proto, pin the **exact** value with a `file:line` citation; never invent.
- **Meaning holes** (new, explicit): undefined behavior at the edges (error/timeout/reconnect/cancel/empty/race — currently listed, now routed here); open forks («либо…либо») with no decision; an unnamed invariant or interaction contract between components the task touches; an undrawn **scope boundary** — which files/services are *outside* the task's zone (new hole type); unstated task ordering. Repair: write the missing constraint as a **spec clause** derived from the *observed behavior of the actual code*, citing the code that grounds it where a concrete source exists; when the code cannot settle it (genuine product decision), raise it under `## Blocking decisions` — never fabricate.

Scan-mode line format extends to name the class: `[file:line|spec-location] → value|meaning → what's missing → fix`. Default mode unchanged: edit in place, report `N closed from source · M blocking` (optionally split by class).

Keep the command small — it is ~20 lines; this is a rewording and a reroute, not a new pipeline. Target-selection logic is note 37's territory — do not touch it here beyond merging cleanly if 37 landed first.

## What NOT to do

- Do not drop the `file:line` citation requirement for value holes — the forced deep read is deliberate.
- Do not require a `file:line` for a meaning hole that has no single source line — the grounding citation is "where one exists", the clause itself is the deliverable.
- Do not let meaning-hole repair invent product decisions — `## Blocking decisions` stays the escape hatch.
