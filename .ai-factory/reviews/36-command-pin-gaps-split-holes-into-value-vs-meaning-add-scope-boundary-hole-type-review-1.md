# Code Review: command-pin-gaps — split holes into value vs meaning

**Scope:** `src/commands/command-pin-gaps.md` (only code change). Plan/JSON/plan-review artifacts under `.ai-factory/` are process files, not code.

## What changed
The single "find every place the agent would guess" taxonomy + single value-pinning repair move were split into two labeled classes:
- **Value holes** — unpinned symbols, magic numbers; repair by pinning the exact value with `file:line`.
- **Meaning holes** (new) — edge behavior, open forks, unnamed invariants/interaction contracts, undrawn scope boundaries, unstated ordering; repair by writing a spec clause from observed code behavior, citing source where one exists, else escalate to `## Blocking decisions`.

Scan-mode line format extended to `[file:line|spec-location] → value|meaning → what's missing → fix`; default mode gains "or spec clause" and "optionally split the count by class"; frontmatter description rewritten to describe both repair moves.

## Correctness verification against spec note 46
- Value-hole content preserved verbatim (enum names **and** values, error codes, strings, versions, paths, field **types**, magic numbers); `file:line` requirement retained — matches "do not drop the file:line citation for value holes." ✓
- Edge cases (error/timeout/reconnect/cancel/empty/race) and unstated ordering correctly **moved** from the value list into meaning holes. ✓
- Scope boundary added as the new meaning-hole type. ✓
- Meaning-hole grounding is conditional — "citing the code that grounds it where a concrete source exists" — so no `file:line` is forced on sourceless holes, matching the note's explicit "do not require a file:line for a meaning hole that has no single source." ✓
- Product-decision escape hatch to `## Blocking decisions` preserved for both classes; "never fabricate" retained. ✓
- Note 37's target logic (line 13 target-priority paragraph) and the "space to fantasize" framing (line 15) are untouched. ✓
- Scan/default format changes match the note; default report string `N closed from source · M blocking` unchanged, with the note-sanctioned optional class split. ✓

## Runtime / structural checks
- **Frontmatter YAML valid:** `description` is a `>-` folded block scalar; the inline colon on line 3 (`…close each one now: pin…`) is literal block content, not a stray mapping key. `argument-hint` stays quoted (`"[path | scan]"`), `allowed-tools` unchanged. No parse break for the harness's command loader.
- **Size:** 22 lines — within the "~20 lines, rewording not a new pipeline" constraint.
- **Tools:** no new capabilities needed; `allowed-tools` correctly left as-is.
- **No `upstream/ai-factory/` touched.**

This is a prose command definition (an agent prompt) — no executable code, migrations, types, or concurrency surface to break. The change is a faithful, internally consistent restructure of the spec.

No findings.

REVIEW_PASS
