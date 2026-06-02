---
name: command-handoff — scale handoff detail to session depth (it under-mines deep sessions)
description: Field lesson refining the command-handoff command (see note 12). On a very deep session the command emitted an impoverished, fixed-size handoff — generic one-liners, no per-unit map, no contracts checklist, no per-unit watch-points. The fix: instruct it to scale detail to how much was done — enumerate every work-unit touched, extract the recurring contracts/invariants, and pull concrete watch-points + a named error log — so a 1M-token session yields a migration-guide-depth note, not three bullets.
type: project
---

# command-handoff — Scale Detail to Session Depth

**Date:** 2026-06-02
**Provenance:** observed live in a `tradeoxy_core` session (~1M tokens of context, a whole indicator-engine v2 roadmap reviewed phase by phase). Refines note `12-task-command-handoff.md` (the command's task spec) with a field failure + the correction the user demanded.

## What happened (the failure)

`/command-handoff note` ran on a very deep session and produced a **thin** handoff: the skeleton sections were present but each was filled with a sentence or two — generic "Done / In-flight" bullets, a one-line read map, an error log of one item. The user rejected it outright: *"we have almost a million tokens of context here, you have nothing to say?? I want it as detailed as note 92."* A hand-expanded rewrite — to the depth of a real migration guide — was accepted: it added a **per-unit map** (every phase + its note + what it became), a **cross-cutting contracts checklist** (the names/types/invariants that must stay consistent across units), **per-unit watch-points** (the specific thing to re-check in each), and a **concrete, named error log**. Same skeleton; ~5× the substance.

## Root cause

The command's output is effectively **fixed-size**. The skeleton (note 12 §6) lists section *names*, and the agent's default is to satisfy each with a line or two. Nothing tells it that **output depth must be proportional to session depth.** So a trivial bugfix session and a thousand-decision architecture session produce handoffs of roughly the same length — and the deep one is starved. The skeleton is good; the *mining instruction* is too shallow.

## The fix — what to add to the command

Add an explicit **proportional-depth mandate** + two richness mechanisms:

1. **Scale to the session.** State in the command: *the handoff's length and granularity must track how much was actually done.* A session that touched many work-units (phases, modules, files, tasks) must **enumerate each one** with its specific state and the specific thing to re-check — never collapse a whole subsystem into three summary bullets. A small session still gets a short note (this is *proportional*, not *always long*).

2. **Add two high-value sections for substantial sessions** (these are what turned the rejected note into the accepted one — make them first-class, not optional afterthoughts):
   - **Cross-cutting contracts / invariants checklist** — the concrete names, types, signatures, and rules that recur across the work and must stay identical everywhere (e.g. "type X stays `Foo[]`, never `Bar[]`"; "method renamed `a()`→`b()`"; "field Z lives on the entity not in params"). This is the single densest, highest-leverage section for a consistency-heavy effort and the default skeleton has no slot for it.
   - **Per-unit map with watch-points** — for each work-unit touched: one line of *what it became* + one line of *the non-obvious thing to verify* (the place the work was tricky or a mistake nearly happened). Distinct from the flat "current state" list.

3. **Error log must be concrete and named** — actual mistakes + their exact corrections, with the specific symbol/file/decision, not "some issues were fixed." These are the cheapest repeat-failures to prevent and the first thing thin handoffs drop.

4. **Richness self-check before emitting** — a gate the command applies to its own draft:
   > *Could a fresh agent, with only this note, (a) execute the next step, (b) avoid every mistake in the error log, and (c) for each subsystem touched, know what it became and what to re-check? If a whole subsystem collapsed to one bullet, or the contracts that recur aren't listed, expand before emitting.*

## Reference exemplar (good vs bad)

The same session produced both: the **rejected** thin version and the **accepted** rich version (`tradeoxy_core/.ai-factory/notes/98-roadmap-v2-guided-review-pass.md` — a per-phase map, a cross-cutting "contracts to verify" checklist, per-phase watch-points, a 5-item named error log) and its sibling `97-roadmap-v2-verification-pass.md`. Worth pasting a sanitized fragment into the command as a few-shot of the target depth, so "what good looks like" is anchored, not left to the agent's default brevity.

## Don't over-correct

The mandate is **proportional**, not maximal. A short session yields a short handoff; padding a trivial session to migration-guide length is its own failure. The trigger for the rich form is *the session actually produced a lot* — many units, recurring contracts, several corrections. Judge by what was done, not by a fixed template size.

## Relationship to existing notes

- Builds on note `12-task-command-handoff.md` (the command's task spec) — this is the depth-scaling refinement to its content-skeleton step.
- Same spirit as note `10-continuation-handoff-skill.md` (the original "rich handoff beats /compact" idea); this pins down *why the first cut still came out thin* and how to force the depth.
