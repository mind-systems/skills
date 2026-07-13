# skill-description-field altitude — the "roadmap cleanup" flow

Phase 14, task 14.2. Same method and governing spec as [task 14.1](67-descfield-altitude-new-work-flow.md): read the flow's `description:` fields as one sub-document and level altitude/register — but to the **field reference** 14.1 records, not to a grain invented here.

**Preconditions.** Runs after phases 9–13 (altitude read off final descriptions) **and** after 14.1 (the reference grain). Also depends on phase 11: `task-rescue` / `task-rescue-audit` are the renamed skills — this task reads them under their new names. **Re-verify before running.**

## Group (the "roadmap cleanup" flow)

`roadmap-test-coverage`, `roadmap-prune`, `task-rescue`, `task-rescue-audit`.

## Provisional observation (against the current field — re-check after 9–13)

This flow holds the **exhaustive pole** of the manifest: the rescue/audit and test-coverage/prune descriptions are dense, multi-clause, near-mini-manual. The likely levelling direction is **down** toward 14.1's reference — compressing the enumerations to concept-plus-route grain — not up. Confirm against the final descriptions; the pole may have shifted after conformance.

## Guards

- Triggers/routing untouched; no vocabulary (9–13 owns it); **no topology** (never wire the flow into a description); no behavior/information loss a caller needs to route.
- Level **to 14.1's recorded reference**, not to a fresh grain — the whole field must converge on one altitude, not two even-but-different flows.
- **"No change" is legal** — the flow may already sit at the reference.
- Re-verify before running.

## Verification

- The four descriptions read at 14.1's reference altitude and register, in sequence, with no jump to a neighbor from the "new work" flow.
- Every trigger/keyword phrase byte-identical; each skill still routes.
- No enumerated detail dropped that a caller needs to decide when to invoke (compression, not amputation).
