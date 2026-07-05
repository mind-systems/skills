# roadmap-engine: shape-condition the checkbox flows and soften the two-tier opener

**Date:** 2026-07-05
**Source:** deferred observations from milestone 52's plan-review-2/-3 and review-1 (two-level phase grammar), evaluated in chat

## Problem today

Milestone 52 made the engine's note/placeholder mandates shape-conditional at all three
sites (create-mode draft `src/skills/roadmap-engine/SKILL.md:154-160`, finalize
`:174-180`, update-mode Add `:204-208`), but the **checkbox-marking** flows and the
section opener still assume every entry is a checkbox'd two-tier milestone:

1. **Update-mode "Review progress"** (`:201-203`) — "for each unchecked entry …
   propose marking the confirmed-done entries `[x]`". A phase entry (outline's hook (a)
   shape) has no checkbox to mark; the action's wording gives an agent no answer for
   phase headers coexisting in the same file as `N.M` tasks.
2. **Check mode** (`:225-264`) — scans "every open `- [ ]` entry" and marks `[x]`.
   Same gap, plus: mode determination (`:116`) routes a literal `check` argument to
   Check mode for **any** caller. Outline dropped `check` from its `argument-hint` in
   milestone 52, but a user typing `/roadmap-outline check` still lands in the engine's
   Check mode with nothing valid to scan at the phase tier.
3. **"The two-tier artifact" opener** (`:27`) — "Each milestone is a two-tier entry:
   a contract line … plus a full spec note" is categorically false for phase entries,
   which milestone 52 legalized (no contract line, no note, no tag). Review-1 judged it
   "an overbroad description in a context section, not an instruction that produces a
   wrong artifact" — but it is the last remaining universal-two-tier claim in the file.

## Pinned decision — derive, don't mark

Phase-tier progress is a **derivative of the phase's child tasks**: a phase reads
complete when every `N.M` task under its header is `[x]`. There is no phase-level
checkbox, so the engine's flows never *mark* anything at the phase tier — they may
*report* derived phase progress, nothing more. Check mode remains a checkbox-tier
feature: a caller whose hook (a) shape carries no checkboxes has nothing for Check
mode to scan, and the engine says so instead of leaving the routing silent.

## The change (one file: `src/skills/roadmap-engine/SKILL.md`)

1. **Review progress** (`:201-203`): add shape-conditioning — the marking applies to
   checkbox entries only; entries whose shape has no checkbox (e.g. a phase header)
   are never marked; where such entries coexist with `N.M` tasks in the same file,
   phase progress may be reported as derived from its child tasks (all `[x]` → phase
   reads complete), report-only.
2. **Check mode** (`:225-264`): one added sentence at the top — Check mode operates on
   checkbox entries only; when the caller's entry shape (hook a) carries no checkbox,
   there is nothing to scan and the caller registers no check mode (its argument
   routing should not advertise one). No change to the scan/evidence/report mechanics
   for checkbox callers.
3. **Opener** (`:27`): soften the categorical claim — the two-tier entry is the shape
   of the *task tier*; a caller's hook (a) may define entries with no contract line
   (e.g. phase headers), and the note/tag machinery of this section applies only where
   a contract line exists. One–two sentences, no restructuring.

## Guards

- **Caller-agnostic** — no skill names anywhere in the engine (note 38's rule);
  "e.g. a phase header" is the same register the draft/finalize/Add loosening already
  uses.
- **Do not touch** the already-loosened draft/finalize/Add wording, the Roadmap File
  Format section, the numbering rules, or the contract-line rules — this task covers
  only the three spots above.
- Exactly three callers load the engine (outline, decompose, skeleton) — their hooks
  must stay coherent; decompose/skeleton (genuinely checkbox-tier) must be unaffected
  by all three edits.
- ≤500 lines (file is 274 today).

## How to verify

1. `grep -n "Each milestone is a two-tier entry" src/skills/roadmap-engine/SKILL.md`
   → no categorical match (softened wording in place).
2. Review progress and Check mode both carry a shape-condition sentence; draft,
   finalize, and Add sections byte-identical to HEAD.
3. `grep -n "roadmap-outline\|roadmap-decompose\|skeleton" src/skills/roadmap-engine/SKILL.md`
   → zero matches (still caller-agnostic).
