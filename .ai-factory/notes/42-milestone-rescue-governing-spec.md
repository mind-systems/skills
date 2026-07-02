# milestone-rescue: read the phase's governing spec before diagnosing

**Date:** 2026-07-02
**Source:** conversation context (live incident, tradeoxy Phase 7 rescue)

## Key Findings

- Live incident: three code-review rounds plus the rescue editor — four readers in a row — never opened the governing spec named in the roadmap phase's section header (`Governing spec:` line). The ratified spec tier did not participate in the review or the rescue at all; semantic blockers were issued without it.
- `src/skills/milestone-rescue/SKILL.md` never instructs reading phase-level spec documents: Step 1 discovers artifacts by slug, Step 4 reads `$TARGET_FILE` only to locate the milestone line. A phase's `Governing spec:` documents are invisible to the whole flow.
- Rule to add: if the milestone belongs to a phase whose header (or intro lines under it) carries `Governing spec:` naming one or more documents — read every named document before issuing any semantic diagnosis or repair.

## Details

### Edit 1 — Step 1 (Discover artifacts)

After identifying the milestone slug, read `$TARGET_FILE` (moving this read up from Step 4 is fine — Step 4 keeps its own locate logic), find the phase section the milestone belongs to, and check the phase header and its intro lines for a `Governing spec:` reference. If present, read every named document in full before proceeding to Step 2. If the milestone is not under any phase, or no `Governing spec:` is named, proceed as today.

### Edit 2 — Step 3 (Extract root cause)

When a governing spec was read, judge the recurring findings against it: a candidate "specification gap" may actually be a violation of an already-ratified contract the spec note failed to restate — the root cause and the repair target differ (amend the spec note to carry the governing constraint vs. invent a new decision). The Diagnosis Report must say whether the failure violates the governing spec, quoting the relevant clause.

### Edit 3 — "What NOT to do"

Add: "Do not issue a semantic diagnosis, blocker, or spec repair without having read the phase's `Governing spec:` documents when the phase names them — otherwise the ratified spec tier does not participate in the rescue at all."

### Constraints

- Behavior-identical elsewhere: artifact discovery filters, depth routing, rollback, sidecar table, git commands untouched.
- Body ≤ 500 lines; frontmatter unchanged.

## What NOT to do

- Do not make the governing-spec read conditional on suspicion — it is unconditional when the phase names one.
- Do not copy governing-spec content into the spec note wholesale — quote/restate only the clauses implicated by the findings.
