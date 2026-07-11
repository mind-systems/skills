# roadmap-prune: default-pair sweep never deletes stem subdirectories

Source observation: `reviews/94-4-7-roadmap-prune-sweep-and-gate-…-review-1.md:23`, re-verified live 2026-07-12 — Step 5's default branch still `rm -rf`s the three flat dirs whole, and no guard forbids a default-pair prune while `.ai-factory/roadmaps/` exists. Deliberately amends spec 49 §Guards' byte-stable mandate: the byte-stable choice is exactly what leaves the hazard reachable.

## Current state

Step 5, default-pair branch: "`rm -rf` the three flat dirs directly under `<target repo root>/.ai-factory/`: `plans/`, `plan-reviews/`, `reviews/`" (+ flat `test-runs/` in tests mode). Those dirs are the parents of the per-roadmap stem subdirectories (`plan-reviews/<stem>/…`, per `orchestrator-artifacts` §1), so a default-pair prune on a repo that also holds `.ai-factory/roadmaps/` recursively deletes every developer's artifact queue — the exact cross-developer deletion 4.7 closed on the named side, still reachable from the default side.

## Change

Scope the default-pair sweep by the presence of `.ai-factory/roadmaps/` under the target repo root:

- `roadmaps/` absent (solo repo) → today's whole-dir `rm -rf`, byte-stable.
- `roadmaps/` present → delete only regular files directly under each swept dir (`find <dir> -maxdepth 1 -type f -delete` or equivalent), preserving stem subdirectories; the same rule applies to flat `test-runs/` in tests mode.

The named-roadmap branch is untouched — it already sweeps only its own stem's subdirectories.

## Files & types

- edit `src/skills/roadmap-prune/SKILL.md` only (Step 5; Step-8 report wording follows if it enumerates the swept dirs).

## Guards

- Gate, specs sweep, ledger, commit policy untouched.
- "Never a sibling stem's subdirectory" — unchanged invariant, now protected from both sides.
- Solo repos see today's behavior exactly.

## Verification

- Dry-read both branches: with `roadmaps/` present, a default prune leaves every `plan-reviews/<stem>/` intact; without it, behavior identical to today.
