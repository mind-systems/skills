---
name: command-handoff — scale handoff detail proportionally to session depth
description: Task spec for adding a proportional-depth mandate + two new sections + richness self-check to command-handoff.md so deep sessions produce migration-guide-depth output, not three bullets.
type: project
---

# command-handoff — Scale Handoff Detail Proportionally to Session Depth

**Date:** 2026-06-03
**Source:** conversation context + field lesson in note `17-task-command-handoff-scale-detail-to-session.md`

## Key Findings

- `command-handoff.md` produces fixed-size output regardless of session depth — nothing instructs the agent to scale granularity to what was actually done.
- A 1M-token architecture session and a trivial bugfix produce handoffs of equal thinness because the skeleton sections default to 1–2 lines each.
- The fix is purely additive to the existing 9-section skeleton: add a proportional-depth mandate, two new first-class sections, a concrete error-log requirement, and a richness self-check gate.
- The mandate is proportional, not maximal — a short session must still yield a short note.

## Details

### File to modify

`src/commands/command-handoff.md` (symlinked to `~/.claude/commands/command-handoff.md`)

### What exists today

The command has a 9-section skeleton (frame → two-tier read-first map → current state → next step → working discipline → error log, + optional orientation / domain-spine / hard-rules). It covers the right *topics* but gives no instruction on *depth*: the agent fills each section with whatever seems sufficient, which defaults to brief. Nothing ties output size to session size.

### The exact change

Add four things to the content-generation step (after the skeleton is introduced, before the "emit" instruction):

**1. Proportional-depth mandate**
State explicitly: *output length and granularity must track how much was actually done.* A session that touched many work-units (phases, modules, files, tasks) must **enumerate each one individually** with its specific state and the specific thing to re-check — never collapse a whole subsystem to summary bullets. A small session still gets a short handoff (proportional, not always-long).

**2. Two new first-class sections for substantial sessions**
These are not optional afterthoughts — make them named slots in the skeleton, triggered when the session covered many units or recurring cross-cutting concerns:
- **Cross-cutting contracts / invariants checklist** — the concrete names, types, signatures, and rules that recur across the work and must stay identical everywhere (e.g. "type X stays `Foo[]`, never `Bar[]`"; "method renamed `a()`→`b()`"; "field Z lives on the entity not in params"). The densest, highest-leverage section for consistency-heavy efforts.
- **Per-unit map with watch-points** — for each work-unit touched: one line of *what it became* + one line of *the non-obvious thing to verify* (where the work was tricky or a mistake nearly happened). Distinct from the flat "current state" list.

**3. Concrete named error log**
The existing error-log section must be actual mistakes + their exact corrections, with the specific symbol / file / decision. Not "some issues were fixed." These are the cheapest repeat-failures to prevent and the first thing thin handoffs drop.

**4. Richness self-check gate (applied to the agent's own draft before emitting)**
> *Could a fresh agent, with only this note, (a) execute the next step, (b) avoid every mistake in the error log, and (c) for each subsystem touched, know what it became and what to re-check? If a whole subsystem collapsed to one bullet, or the contracts that recur across the work aren't listed, expand before emitting.*

### Guard conditions

- The 9-section skeleton structure stays unchanged — these are depth instructions layered on top, not a restructure.
- The `note`/`ноут` trigger behavior and note-persistence path are unchanged.
- Mandate is **proportional, not maximal** — explicitly state that a trivial session padding itself to migration-guide length is its own failure.

### Reference exemplars (in tradeoxy_core)

- Accepted rich version: `tradeoxy_core/.ai-factory/notes/98-roadmap-v2-guided-review-pass.md` (per-phase map, cross-cutting contracts checklist, per-phase watch-points, 5-item named error log)
- Sibling: `97-roadmap-v2-verification-pass.md`
- Worth extracting a sanitized fragment as a few-shot anchor in the command.

### How to verify

Run `/command-handoff note` at the end of a session that touched 3+ phases or modules. Output must: enumerate each unit individually, include a cross-cutting contracts section with named types/signatures, include per-unit watch-points, and have a named error log with specific symbols. Compare against a run after a trivial single-file fix — that one should still be short.

## Open Questions

- Whether to embed a sanitized few-shot fragment inline in the command or just describe the target depth — inline is higher-signal but adds length to an already-substantial command file.
