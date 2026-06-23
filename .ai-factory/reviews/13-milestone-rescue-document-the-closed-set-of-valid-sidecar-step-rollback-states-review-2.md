# Review 2 — milestone-rescue: document the closed set of valid sidecar `step` rollback states

## Scope
Doc-only change to `src/skills/milestone-rescue/SKILL.md` Step 5. No code, migrations, or runtime surface. Verified against the authoritative spec note (`.ai-factory/notes/23-task-milestone-rescue-document-rollback-states.md`); the orchestrator (`orchestrator/main.py`) is in another repo and not present here.

## Changes since review 1
All three findings from review 1 were addressed:

1. **Low (decision-table conflict) — resolved.** The standalone `Sidecar doesn't exist → create with "plan_reviewed"` row that conflicted with the new `"planned"` row was removed. The create-if-absent behavior is now folded into each real situation row: `Plan .md corrected in place → "planned" (create sidecar if absent)` and `Plan-reviews exist and pass → "plan_reviewed" (create sidecar if absent)`. No two rows can match with conflicting values anymore.
2. **Informational (heading) — resolved.** The sidecar-update sub-section heading is now `Plan `.md` kept (re-implement or re-plan-review):`, so the re-plan-review path is explicitly covered by the only procedure describing how to read/update the sidecar.
3. **Informational ("both cases") — resolved.** Updated to "all three cases", consistent with the three cleanup outcomes listed directly above.

## Verification
- The five-value `step` table reproduces the spec note exactly — values, resume phases, and required artifacts all match. No transcription errors.
- Test-mode swap, silent-failure-mode prose, and source-of-truth caveat match the note.
- The always-valid guard correctly states the preconditions for `"planned"` (plan `.md` present) and `"implemented"` (plan present + non-empty working diff), and names the failure mode it prevents.
- Decision table is internally consistent with the always-valid guard (the `"planned"` row requires the corrected plan `.md` on disk) and with the cleanup-outcome narrative.
- The non-convergence + option 2 path (SKILL.md:231–236) specifies its sidecar value (`"plan_reviewed"`) inline and does not depend on the renamed heading — still coherent.
- The decision table correctly writes only the two values a rescue legitimately produces (`"planned"`, `"plan_reviewed"`); `"implemented"` / `"review_failed:N"` are orchestrator-internal states and correctly appear in the reference table but not the rescue write-table.
- All three plan tasks satisfied; change stays doc-only and does not rewrite the existing cleanup flow.

No findings.

REVIEW_PASS
