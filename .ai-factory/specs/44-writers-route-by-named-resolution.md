# Writers route by the engine's named-roadmap resolution: outline, decompose, skeleton

Governing spec: `docs/multiuser-roadmaps.md`. Depends on spec 43 (the engine section this task points at).

## Current state

The three roadmap writers each hardcode their target short of the named tier:

- `src/skills/roadmap-outline/SKILL.md:51` — hook (c): "Always `.ai-factory/ROADMAP.md` — trivial policy, no keyword/argument branching."
- `src/skills/roadmap-decompose/SKILL.md` hook (c) — Default → `.ai-factory/ROADMAP.md`; explicit filename wins; test keywords → `.ai-factory/ROADMAP_TESTS.md`. No "my roadmap" step; the test branch cannot map a named roadmap to its sibling.
- `src/skills/roadmap-decompose-skeleton/SKILL.md:58` — "Read the target roadmap (`ROADMAP.md`, or the file named by the arg/context)".

## Change

One rule, three sites — each hook (c) routes through the engine's named-roadmap resolution instead of its bare literal:

- **outline:** target policy becomes the engine's resolution order (argument → my → default); still no keyword branching at the strategic tier.
- **decompose:** insert "my roadmap" between explicit-argument and default; the test-keyword branch derives the sibling of the roadmap in play — default → `.ai-factory/ROADMAP_TESTS.md` as today, named → `.ai-factory/roadmaps/<slug>-tests.md`.
- **skeleton:** the parenthetical names the engine's resolution instead of the bare `ROADMAP.md` default.

## Files & types

- edit `src/skills/roadmap-outline/SKILL.md`, `src/skills/roadmap-decompose/SKILL.md`, `src/skills/roadmap-decompose-skeleton/SKILL.md`.

## Guards

- Philosophy untouched: outline's phase grammar and 5–15 rule, decompose's Atomicity Gate and hooks (a)/(b)/(d), skeleton's three lenses — byte-identical.
- Resolution is referenced, never restated — the mechanism has one home in the engine (spec 43).
- Behavior without `roadmaps/` identical to today at all three sites.

## Verification

- `grep -n "roadmaps/" ` over the three files hits only resolution references, no restated derivation/owner mechanics.
- Dry run of each skill's routing with no multiuser context resolves exactly as today.
