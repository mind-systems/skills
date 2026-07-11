# Plan: 4.2 — writers route by the engine's resolution: outline, decompose, skeleton

## Context
Point the three roadmap writers (outline, decompose, skeleton) at `roadmap-engine`'s named-roadmap resolution (spec 43) instead of their hardcoded bare `ROADMAP.md` literal, so each routes through the shared resolution order (argument → my → default) while their philosophy stays byte-identical.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Route the three writers through the engine's resolution

- [x] **Task 1: outline hook (c) becomes the resolution order**
  Files: `src/skills/roadmap-outline/SKILL.md`
  Rewrite the `### (c) Target-file routing` body (`:51`, currently `Always .ai-factory/ROADMAP.md — trivial policy, no keyword/argument branching.`) so the target policy is the engine's named-roadmap resolution order (explicit argument → "my roadmap" → default `.ai-factory/ROADMAP.md`), reference it as living in `roadmap-engine` — do not restate the slug/owner mechanics. Keep the strategic-tier restraint: still **no keyword branching** at this tier (unlike decompose). Per the spec, outline routes through the resolution but adds no test-keyword branch. `roadmap-engine` is already declared in `loads:` (`:6`) and referenced throughout, so no frontmatter change. Everything else in the file (phase grammar, 5–15 rule, hooks (a)/(b)/(d), check mode) stays byte-identical.

- [x] **Task 2: decompose hook (c) inserts "my roadmap" and derives the test sibling**
  Files: `src/skills/roadmap-decompose/SKILL.md`
  Edit the `### (c) Target-file routing` list (`:61-65`). Insert the "my roadmap" step between the explicit-argument rule and the default so the order reads: explicit filename argument wins → "my roadmap" (per `roadmap-engine`'s resolution) → default `.ai-factory/ROADMAP.md`. Change the test-context-keyword branch so the test roadmap is derived as the **sibling of the roadmap in play**, not a bare literal: default roadmap → `.ai-factory/ROADMAP_TESTS.md` (as today), a named roadmap → `.ai-factory/roadmaps/<slug>-tests.md` (per the engine's "Test sibling" rule). Reference the engine's resolution; do not restate slug derivation or owner-line mechanics. Keep hooks (a)/(b)/(d), the Atomicity Gate, and all other body text byte-identical. `roadmap-engine` already in `loads:` (`:11`).

- [x] **Task 3: skeleton Step 0 names the engine's resolution**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  In Step 0 (`:58`), change the parenthetical `Read the target roadmap (ROADMAP.md, or the file named by the arg/context)` so it names the engine's named-roadmap resolution (argument → my → default) instead of the bare `ROADMAP.md` default — a reference, not a restatement. Leave the rest of the sentence (collect open `- [ ]` tasks, never touch `- [x]`) and the three lenses' decision contracts byte-identical. `roadmap-engine` already in `loads:` (`:15`).

## Notes for the implementer
- The resolution mechanism has exactly one home — `roadmap-engine`'s "Named roadmaps" section (spec 43). All three edits **reference** it; none restate the slug/owner/derivation mechanics. Verification: `grep -n "roadmaps/" ` over the three files should hit only resolution references, never restated derivation or owner mechanics.
- Behavior without a `roadmaps/` directory must be identical to today at all three sites (lazy migration).
