# Handoff — before running Phase 14, re-verify the altitude tasks against the final description-field

> Pre-flight blocker for Phase 14 (skill-description-field: even abstraction-level). Its tasks (14.1–14.3, specs 67–69) were **decomposed before phases 9–13 landed**. Altitude must be read off the *final* descriptions, not the pre-conformance ones — so the drafted tasks are provisional and must be re-verified before the orchestrator runs them.

## Why this is a blocker

A skill's altitude (how much detail its `description:` packs) is assessed by reading all descriptions as one manifest. Phases 9–13 rewrite tokens *inside* those descriptions (`milestone`→phase/task, `spec note`→`task-spec`, the flagship in `roadmap-outline`/`roadmap-decompose`, the rescue rename). Vocabulary conformance is roughly altitude-neutral, but "roughly" is not "certainly": the provisional poles named in the specs (the **exhaustive pole** = the cleanup flow's rescue/audit/test-coverage/prune; the **terse pole** = `aif`/`note`) were observed against the *current* field and may shift.

## Re-verify before running — checklist

1. **Phases 9–13 have landed.** Every skill description is vocabulary-conformed. Altitude read off a stale description is wrong.
2. **The Phase 11 rename is in place** — `task-rescue` / `task-rescue-audit` exist under the new names; 14.2 reads them by those names.
3. **Re-read all descriptions as one manifest** (the order the harness loads them) and re-confirm the two poles and the outliers each spec names — 67/68/69 pin them provisionally, against the pre-conformance field.
4. **Set the reference altitude (14.1) against the final descriptions**, not the drafted-now assumptions; 14.2/14.3 converge on that reference.
5. **"No change" stays legal.** If the field already reads even after 9–13, the plan says so and the implementer edits nothing — a valid outcome, not a failure.

## One-line

Phase 14's altitude tasks are drafted against the pre-conformance field; re-read the final descriptions, re-confirm the poles and the reference, and only then run — the plan may legitimately conclude the field already reads as one document.
