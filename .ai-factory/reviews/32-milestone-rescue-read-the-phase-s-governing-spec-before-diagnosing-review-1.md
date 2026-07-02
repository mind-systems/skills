# Code Review — milestone-rescue: read the phase's `Governing spec:` before diagnosing

**Scope reviewed:** `git diff HEAD` / `git status`. The only source change is
`src/skills/milestone-rescue/SKILL.md` (skill instruction text). The staged plan,
plan-review, and sidecar JSON under `.ai-factory/` are planning artifacts, not product
code.

This skill is executable-behavior prose, not compiled code — so "correctness" here means
internal consistency, faithful realization of the governing spec note
(`.ai-factory/notes/42-milestone-rescue-governing-spec.md`), and no contradiction with
surrounding rules. There is no runtime surface, no migration, no type/race concern.

## What the diff does

Three additions, matching the three planned tasks:

1. **Step 1 (Discover artifacts), lines 54-62** — new "Read the phase's governing spec"
   paragraph: resolve `$TARGET_FILE`, locate the milestone's phase, read every
   `Governing spec:` document in full before Step 2, unconditionally.
2. **Step 3 (Extract root cause), lines 118-123** — new paragraph: judge recurring
   findings against the governing spec; a "specification gap" may be a ratified-contract
   violation; Diagnosis Report must state whether it violates and quote the clause.
3. **Depth: spec, lines 247-248 + What NOT to do, lines 364-367** — don't copy the
   governing spec wholesale (quote only implicated clauses); no semantic
   diagnosis/blocker/repair without the read; read is unconditional, never
   suspicion-gated.

## Verification against the spec note and constraints

- **Edit 1 / Edit 2 / Edit 3** from the spec note — all present and faithful.
- **`$TARGET_FILE` resolution parity** — Step 1's summary ("argument-named file, else
  ROADMAP_TESTS.md for test slugs, else ROADMAP.md") correctly mirrors Step 4's
  three-way rule at lines 161-163. No drift.
- **Additive, not a replacement** — the diff explicitly states the Step 1 read does not
  replace Step 4's own resolution/locate (line 60-62). Step 4 is untouched, so no
  double-edit or lost logic.
- **Unconditional, not suspicion-based** — stated in Step 1 (line 59) and reinforced in
  What NOT to do (lines 366-367). Consistent, no contradiction.
- **Behavior-identical elsewhere** — depth routing, rollback procedures, the sidecar
  `step` table, and all `git` commands are untouched by the diff. Confirmed against the
  full file.
- **Shared narrative register** — the Step 3 addition adds *content* requirements
  (state violation, quote clause) but does not alter the prose-narrative register that is
  coupled to `milestone-rescue-audit` ("change it in both files or neither", line 139).
  The coupling invariant is not triggered — no matching edit is required there.
- **No orchestrator-vocabulary conflict** — quoting a governing-spec clause is domain
  content, compatible with Step 3's "domain language only / zero orchestrator
  vocabulary" rule (line 145-147).
- **Body ≤ 500 lines** — file is 378 lines. Frontmatter unchanged (lines 1-13).

## Findings

None. The change is a clean, faithful realization of the spec note with no internal
contradictions, no constraint violations, and no collateral edits to the untouched
subsystems.

REVIEW_PASS
