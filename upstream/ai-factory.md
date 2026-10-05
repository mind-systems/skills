# ai-factory

URL: https://github.com/lee-to/ai-factory
Counterparts: aif, aif-architecture, aif-docs, aif-plan

Why we follow it: another model of agent behaviour, read to check the directions we take against theirs. Ours are authoritative; changes worth taking are ported by hand.

## 2026-10-05

Last seen: `ac92beb` (2026-09-29, v2.19.0)

Heading:
- an opt-in "ultra" lane where a strong model plans and a small one executes: plans with Implementation Steps, Acceptance Criteria and a Required Detail Gate;
- machine-readable markers and JSON gate blocks for future orchestrators;
- review hardened for literal models: report everything, confidence markers, auto-validation, and a gate that fails on an unresolved marker;
- session and memory continuity: `aif-warmup`, `aif-transfer`, QA agent memory;
- config-driven command defaults.

Converges with us: a requirements reconciliation gate (a roadmap item is a scope indicator, each rule recorded with its source); a fresh-context coherence check before research is saved; the user's original request kept verbatim.

Diverges: they build gates and recipes, a regulator; we cut specs to behaviour and keep observations non-blocking, a sensor.

`aif-architecture`: unchanged upstream since 2026-06-23, with no variation axis; our phase 73 is ahead.

Taken: nothing. Worth remembering: `aif-transfer`, lessons carried between projects.
