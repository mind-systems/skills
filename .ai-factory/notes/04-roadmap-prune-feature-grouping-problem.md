# roadmap-prune and roadmap-test-coverage — Feature Grouping Problem

**Date:** 2026-05-13
**Source:** conversation context (tradeoxy_core second roadmap prune)

## Key Findings

- `roadmap-prune` Step 2 produces inconsistent feature groupings because its grouping criteria are abstract and subjective ("coherent unit of capability") — the agent defaults to copying phase names instead of identifying real system capabilities.
- `roadmap-test-coverage` solves the same structural problem (grouping roadmap tasks into meaningful areas) more reliably because it uses a concrete checklist and grounds decisions in actual source files — not just task names.
- The fix for `roadmap-prune` is two additions: (1) a concrete classify-first checklist before grouping, and (2) a step that looks at which `src/` files the tasks touched before deciding whether to create a new feature row or add a hash to an existing one.

## Details

### The Problem in Practice

During tradeoxy_core's second prune, the agent produced 13 proposed features from ~50 completed tasks. Problems found:

1. **Phase ≠ Feature** — `Phase 15 — Symbol Search Multi-Exchange` became a feature called "Symbol search multi-exchange". Phase headers are organizational containers, not capability names.

2. **Refactors became features** — Phase 20 (CandleGateway decomposition, circular dep fix, indicator protocol unification) was labeled "Architecture cleanup" — a row in Features. Refactors don't add capabilities and shouldn't create new rows.

3. **Iterations of the same feature were split** — Phases 10, 11, 13, 14, 19 all touched candle storage. The agent proposed 5–6 separate rows instead of one "Candle storage" row with accumulated hashes.

4. **No link to existing features** — ARCHITECTURE.md already had rows for "Exchange execution" and "gRPC signal delivery". Phase 21 (evict stale ccxt) and Phase 20.4 (indicator protocol) were extensions of those, but the agent proposed new rows instead of appending hashes.

### Root Cause: Abstract Criteria vs. Concrete Checklist

```
roadmap-test-coverage               roadmap-prune (current)
───────────────────────             ─────────────────────────
Criteria:                           Criteria:
  - non-trivial logic?              - "coherent unit of capability"
  - high blast radius?              - "delivered together"
  - hard-to-spot bugs?
  - OR: pure wiring? → skip

Concrete, checkable.                Abstract, interpreted freely.
```

`roadmap-test-coverage` also grounds decisions in reality by sending agents to **read source files**. `roadmap-prune` only reads ROADMAP.md — so phase names become the dominant signal.

### Structural Gap: roadmap-test-coverage goes to code, roadmap-prune doesn't

```
roadmap-test-coverage flow:         roadmap-prune flow (current):
  ROADMAP.md                          ROADMAP.md
      ↓ Step 2                            ↓ Step 2
  "testable areas"                    "features"
      ↓ Step 3                            ↓ (nothing)
  reads src/ files                    ─────────────
  classifies by real content              ↓ Step 3
      ↓                               finds git hashes
  concrete decisions
```

If `roadmap-prune` checked which `src/` directories the tasks touched, it would immediately see that Phases 10/11/13/14/19 all map to `src/candles/` — one module, one feature row.

### Proposed Fix for roadmap-prune Step 2

**Addition 1: Classify before grouping**

Before naming any feature, apply this filter to every task group:

> "What can the system do AFTER these tasks that it couldn't do BEFORE?"
> - Can answer in one sentence from operator's perspective → feature (new or extended)
> - Improvement to existing capability → append hash to existing row, don't create new
> - Internal restructuring with no new operator-visible capability → skip (no row)

**Addition 2: Map tasks to src/ modules before deciding new vs. existing**

Before creating a new feature row, check:
- Which `src/` files did these tasks change?
- Does any existing ARCHITECTURE.md feature row cover that module area?
- If yes → this is an extension, add hash to existing row.

**Addition 3: Explicit "Phase ≠ Feature" rule**

Add to Step 2's rules:
> Never copy a phase header as a feature name. Phase headers are work organization — feature names describe system capabilities from the operator's perspective.

### Parallel Between the Two Skills

Both skills read a list of tasks and group them into meaningful areas. The difference:

| Aspect | roadmap-test-coverage | roadmap-prune |
|--------|----------------------|---------------|
| Output | testable components | architectural features |
| Criteria | concrete checklist | abstract description |
| Grounds in code | yes (Step 3 reads src/) | no |
| Handles "existing" | n/a | poorly — no concrete check |
| Phase = area? | naturally avoids it | defaults to it |

The two skills could share a common "grouping" pattern — classify first with a checklist, then verify against real files, then name.

## Open Questions

- Should `roadmap-prune` Step 2 actually spawn an Explore agent per candidate feature to check which src/ files are involved — similar to how `roadmap-test-coverage` spawns agents per area?
- Or is a simpler heuristic enough: "grep the task description for `src/` paths, map to module"?
- Should the classify-first filter be added to `roadmap-test-coverage` too (it currently has the checklist but no explicit "refactor → skip" path)?
