# roadmap-test-coverage — Filter Redesign

**Date:** 2026-05-17
**Source:** conversation context

## Key Findings

- The current Step 2 filter in `roadmap-test-coverage` is too broad — it produces "test almost everything" because it only excludes trivially thin code, not code that fails loudly vs. silently.
- The missing filter is: *"If logic breaks here — will TypeScript / the runtime catch it immediately, or will the system continue running and produce wrong results silently?"* Only the latter class warrants unit tests.
- `roadmap-prune` already solves the analogous problem with one question: *"Could you write an e2e test for this that didn't exist before?"* The test-coverage skill needs the same kind of single decisive question.
- The two skills are structural mirrors: `roadmap-prune` compiles tasks → features (operator perspective); `roadmap-test-coverage` should compile tasks → test areas (reliability perspective). Both should be distillation, not enumeration.

## Details

### The Problem

`roadmap-test-coverage` reads the roadmap, sees implemented logic A/B/C, and classifies nearly all of it as "worth testing" because it asks "is there logic here?" — not "can this logic fail silently?".

When run on the mind_mobile project it produced a near-exhaustive list, which contradicts the philosophy the user holds: test what matters, not everything.

### The Philosophy (from `mind_mobile/docs/core/testing.md`)

The existing `testing.md` captures this well but is anchored to Flutter/Dart (Riverpod Notifiers, Fake* classes, StreamController injection). The principle is universal; the vocabulary is not:

- Test **black boxes** — contracts, not implementation details
- Do not test thin translation layers (mappers, pass-through services, orchestrators)
- Do not test infrastructure (gRPC, WebSocket, Redis wrappers)
- Do test: state machines, complex aggregators, pure functions with non-trivial formulas, anything with hard-to-spot boundary conditions

### The "Silent Failure" Filter

The right classification question for Step 2:

> *"If the logic here is wrong, does TypeScript / NestJS / the runtime produce an error, or does the system run normally and produce wrong output?"*

| Breaks loudly → skip | Fails silently → test |
|---|---|
| Mapper with wrong field type | BackfillService cursor off by one |
| Controller missing a route param | CandlePersistenceService flush dedup wrong key |
| DI wiring missing a provider | CandleCloseDetector OHLCV aggregation wrong |
| Thin adapter with no branches | IndicatorSnapshotService position state machine |

### Structural Parallel with roadmap-prune

`roadmap-prune` Step 2.1:
> "Could you write an e2e test for this that didn't exist before?"
→ If no: internal only, no feature row

`roadmap-test-coverage` Step 2 (proposed):
> "If the logic here breaks, will the system signal it immediately, or continue silently?"
→ If loudly: skip. If silently: include.

Both questions force the agent to reason about **observable consequences**, not about code structure.

### Tooling Divergence (secondary finding)

The `roadmap-test-coverage` skill is stack-agnostic and correctly so. However agent prompts in Step 6 contain no guidance on fakes vs. mocks — agents default to `jest.fn()` everywhere. The `testing.md` philosophy prefers hand-written `Fake*` classes. This is a secondary concern; the filter quality is the bigger problem.

## Open Questions

- Should the "silent failure" filter be encoded as a literal question the agent asks itself per area (like `roadmap-prune` Step 2.1), or as a revised skip/include criteria table?
- Should the skill load a project-level `testing.md` / testing philosophy doc (if present) and pass it to each Step 6 agent as additional context? This would let the mock strategy (fakes vs. jest.fn) flow from the project's own conventions.
