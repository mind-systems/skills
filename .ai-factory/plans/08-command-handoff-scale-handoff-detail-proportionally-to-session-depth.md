# Plan: command-handoff — scale handoff detail proportionally to session depth

## Context
Make `/command-handoff` produce output whose granularity tracks how much the session actually did — deep sessions get migration-guide depth, trivial sessions stay short — by layering depth instructions, two new trigger-based skeleton sections, a concrete error-log requirement, and a richness self-check onto the existing command.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Layer depth instructions onto Step 2

All edits target `src/commands/command-handoff.md` (symlinked to `~/.claude/commands/command-handoff.md`). The changes are **additive** — the existing 9-section skeleton, its section names/order, the `note`/`ноут` trigger behavior, and the note-persistence path (Step 3) all stay unchanged.

- [x] **Task 1: Add the proportional-depth mandate**
  Files: `src/commands/command-handoff.md`
  In Step 2 ("Compose the handoff prompt"), after the paragraph that introduces the skeleton (line ~41) and before the skeleton code-fence, add a short mandate block stating: **output length and granularity must track how much was actually done.** A session that touched many work-units (phases, modules, files, tasks) must **enumerate each one individually** with its specific state and the specific thing to re-check — never collapse a whole subsystem to summary bullets. A small session still yields a short handoff. Add the explicit guard: **proportional, not maximal** — a trivial session padded to migration-guide length is itself a failure. Keep it tight (a few lines), matching the command's dense imperative tone.

- [x] **Task 2: Add two new first-class skeleton sections** (depends on Task 1)
  Files: `src/commands/command-handoff.md`
  Append two new named slots to the skeleton inside the `~~~` fence, after section 9 (Hard rules), as sections **10** and **11**. These are first-class slots, not afterthoughts, but trigger-based — included only when the session covered many work-units or recurring cross-cutting concerns (mirror the existing "only if the session produced these" phrasing used by sections 7–9):
  - `## 10. Cross-cutting contracts / invariants checklist` — the concrete names, types, signatures, and rules that recur across the work and must stay identical everywhere (e.g. "type X stays `Foo[]`, never `Bar[]`"; "method renamed `a()`→`b()`"; "field Z lives on the entity, not in params"). Note inline that this is the densest, highest-leverage section for consistency-heavy efforts.
  - `## 11. Per-unit map with watch-points` — for each work-unit touched: one line of *what it became* + one line of *the non-obvious thing to verify* (where the work was tricky or a mistake nearly happened). Call out that it is distinct from the flat "Current state" list.
  Also update the prose that gates optional sections: the line at ~line 41 referencing "Optional sections (7–9)" must now read 7–11 (or equivalent), so the trigger rule covers the two new sections.

- [x] **Task 3: Strengthen the error-log section requirement** (depends on Task 2)
  Files: `src/commands/command-handoff.md`
  Tighten section 6 (Error log) in the skeleton so it demands **actual mistakes + their exact corrections, each named with the specific symbol / file / decision** — explicitly not "some issues were fixed." Reinforce that this is the first thing thin handoffs drop and the cheapest repeat-failure to prevent. Keep "Empty → omit section" intact.

- [x] **Task 4: Add the richness self-check gate** (depends on Task 3)
  Files: `src/commands/command-handoff.md`
  At the end of Step 2, after "Populate every field…" (line ~90) and before Step 3, add a self-check the agent applies to its own draft before emitting: *Could a fresh agent, with only this note, (a) execute the next step, (b) avoid every mistake in the error log, and (c) for each subsystem touched, know what it became and what to re-check? If a whole subsystem collapsed to one bullet, or the recurring contracts aren't listed — expand before emitting.* Restate the proportionality guard so the gate does not push trivial sessions toward bloat. This gate applies to both chat mode and note mode (it runs before the Step 3 split).
