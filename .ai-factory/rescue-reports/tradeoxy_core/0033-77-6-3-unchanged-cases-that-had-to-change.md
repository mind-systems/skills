# 77.6.3 — unchanged cases that had to change

**Project:** tradeoxy_core
**Date:** 2026-10-11
**Stopped at:** planned:3
**Elapsed before the rescue:** 528

The task wires both start doors to the landed, tested run starter. Its reviews converged — medium with four findings, then low with one, then low with one — and the plan was a modest sixteen thousand characters. The first review found suites whose cases the spec called unchanged failing at runtime, because they passed the old rendezvous mock into the slot the starter now takes; an eslint gate the project's rules exclude; an exhaustive default copied from a string-union precedent that would print «[object Object]» for this object union; and leftover registry wording. The second found two more leftover comments of the same kind. The third found the starter's result redeclaring the `outcome` binding the doors already hold for the ownership probe. Read with core 123, two of the first round's findings were seeded by the spec's own text — «unchanged» cases and a precedent wrong for the outcome's shape — and no reviewer saw that the gRPC door's suite pinned only three of seven outcomes, where a wrong code fails silently against the analyst's status contract.

> The spec called cases unchanged that had to drop their rendezvous mock, pointed at a string-union precedent for an object-union default, and did not require the gRPC door's suite to pin every outcome the way the REST suite does.

Category: specification gap. Recurring: leftover rendezvous wording in the suites (rounds 1 and 2), the planner's to find.

## What was done

Repaired at the specification-and-plan depth. Spec `.ai-factory/specs/0292-both-start-doors-open-the-run.md` was corrected in three places: the REST suite's cases that were called unchanged now keep their assertions and drop the rendezvous mock, with registry-naming titles saying the starter; the renderers' exhaustive default stringifies the outcome with `JSON.stringify`; and the gRPC door's suite pins every non-`started` outcome to its status. Spec `.ai-factory/specs/73-pat-tier-start-serve.md` was given its clause that `toReplayStartRpcError` takes only the non-`started` outcomes, so the PAT door answers `started` itself. The plan `.ai-factory/plans/165-77-6-3-both-start-doors-open-the-run-through-the-starter.md` was kept, with round three's rename of the starter's result binding and a seven-row gRPC status table in the tier-suite task. The three plan reviews were deleted, and the sidecar was set back to `planned:1` with the reviewers' session ids kept.
