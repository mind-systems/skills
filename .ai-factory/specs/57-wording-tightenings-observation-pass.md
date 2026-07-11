# Wording tightenings from the observation pass

Source observations, all re-verified live 2026-07-12: `plan-reviews/88-4-1-roadmap-engine-named-roadmap-contract-…-plan-review-1.md:29` (+ siblings in `-plan-review-2.md:38`, `-plan-review-3.md:33`), `plan-reviews/89-4-2-writers-route-…-plan-review-1.md:31`, `plan-reviews/49-orchestrator-artifacts-engine-…-plan-review-1.md:33`. Three one-clause fixes, one concern: reviewer-flagged wording that dangles or reads wrong but causes no wrong behavior. Bundled into one task by explicit user decision (2026-07-12) — three separate milestones would be pure ceremony.

## Current state

1. `src/skills/roadmap-engine/SKILL.md` — hook (c) "Target-file routing" says "The engine never infers this; the caller resolves it before Step 0 runs" with no pointer to the `## Named roadmaps` section that defines *how* the caller resolves it (the resolution order). Two sections describe the same routing, no cross-link.
2. `src/skills/roadmap-decompose-skeleton/SKILL.md` — two literal `ROADMAP.md` back-references survive 4.2's Step-0 resolution: Step 4 "render into the **same `ROADMAP.md`** the source tasks live in" (:114) and the disposition rule "**Insert** … immediately **before** it in `ROADMAP.md`" (:126). Unambiguous in context, but they name the default file where they mean the resolved one.
3. `src/skills/orchestrator-artifacts/SKILL.md` — the `step` field description calls `milestone-rescue` "its only writer" (:44); strictly the orchestrator also writes `step` (`plan_review_failed:N`, `review_failed:N`) — rescue is the only *skill-side* writer.

## Change

1. Hook (c) gains one clause pointing at the resolution order — e.g. "…the caller resolves it before Step 0 runs (per the `## Named roadmaps` resolution order)".
2. Both skeleton literals → "the source roadmap", keeping each sentence's emphasis structure.
3. "its only writer" → "its only skill-side writer".

## Files & types

- `src/skills/roadmap-engine/SKILL.md` (one clause; body only — runs serial with 5.5, which owns the frontmatter line), `src/skills/roadmap-decompose-skeleton/SKILL.md` (two phrases), `src/skills/orchestrator-artifacts/SKILL.md` (one word).

## Guards

- Wording only — zero behavior change; every other sentence in the three files byte-identical.
- All three files are engines with callers — their expectations are part of the contract; nothing here changes a contract, only names it more precisely.

## Verification

- `grep -n "Named roadmaps" src/skills/roadmap-engine/SKILL.md` → hook (c) now references the section.
- `grep -n 'same .ROADMAP' src/skills/roadmap-decompose-skeleton/SKILL.md` → zero.
- `grep -n "only writer" src/skills/orchestrator-artifacts/SKILL.md` → the phrase reads "only skill-side writer".
