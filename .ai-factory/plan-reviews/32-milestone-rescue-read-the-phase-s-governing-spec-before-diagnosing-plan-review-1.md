## Code Review Summary

**Files Reviewed:** 1 plan (`.ai-factory/plans/32-…-governing-spec-before-diagnosing.md`), cross-checked against the target skill `src/skills/milestone-rescue/SKILL.md`, the governing spec note `.ai-factory/notes/42-milestone-rescue-governing-spec.md`, and `ROADMAP.md`.
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap linkage — OK.** The plan's `# Plan:` title matches the open milestone on `ROADMAP.md` line 75 ("milestone-rescue: read the phase's `Governing spec:` before diagnosing"), which names `Spec: .ai-factory/notes/42-milestone-rescue-governing-spec.md`. The plan's three tasks map 1:1 onto the note's Edit 1 / Edit 2 / Edit 3 plus its "What NOT to do" constraints. Milestone is `feat`-shaped and correctly traced.
- **Architecture / composition — OK.** This is a single-skill body edit that adds mechanism to `milestone-rescue`; it introduces no new skill, no `loads:` dependency, and no cross-skill inlining. Nothing in `.ai-factory/ARCHITECTURE.md`'s composition boundary is crossed.
- **Rules — N/A.** No `.ai-factory/RULES.md` present (WARN: optional file absent, not blocking).

### Critical Issues

None. The plan is faithful to the ratified spec note and to the current skill structure.

### Verification notes (non-blocking)

1. **`$TARGET_FILE` resolution at Step 1 is sound.** Task 1 reuses Step 4's resolution logic (argument-named file / test-keyword → `ROADMAP_TESTS.md` / else `ROADMAP.md`). All three inputs that logic needs — the argument, the slug, and the artifact set — are already available at Step 1 (slug is extracted in the "Identify the milestone slug" block, lines 50–52), so the early resolution cannot fail for lack of information. Placement ("after the 'Identify the milestone slug' block") is correct.

2. **Deliberate duplication is spec-sanctioned.** The plan keeps Step 4's own `$TARGET_FILE` resolution and milestone-line locate logic intact and makes the Step 1 read purely additive. This duplicates the resolution rule in two places (a mild drift risk if the test-keyword heuristic ever changes), but note 42 Edit 1 explicitly permits this ("moving this read up from Step 4 is fine — Step 4 keeps its own locate logic"). Acceptable as specified; if a future edit touches the resolution rule, both sites must move together.

3. **Shared narrative register is protected.** Task 2 adds a *content* requirement to the Diagnosis Report (state whether the failure violates the governing spec; quote the clause) without touching the prose/no-tables register that SKILL.md line 122–123 declares "shared with `milestone-rescue-audit`". The plan is explicit about not altering the narrative-register / shared-with-audit constraints, so no mirrored edit in `milestone-rescue-audit` is triggered. Correct scoping.

4. **Line budget safe.** Current body is 356 lines; the three additions (~15–25 lines) stay well under the ≤500-line cap. Frontmatter is left unchanged, as required.

5. **"What NOT to do" folding is well-placed.** Task 3 correctly routes the second note-42 constraint ("do not copy governing-spec content into the spec note wholesale — quote/restate only implicated clauses") near the spec-note repair guidance (Step 5, Depth: spec, lines 227–237) rather than dumping it as an isolated bullet — matches "wherever they read most naturally."

### Positive Notes

- Every task carries an accurate `Files:` field and dependency ordering (Task 2 → Task 1, Task 3 → Task 2) that matches the actual data flow (the governing-spec read must exist before Step 3 can judge against it, before "What NOT to do" can forbid skipping it).
- The plan preserves all guarded invariants named in the milestone line and spec note: artifact discovery filters, the git-status command, the multi-slug prompt, depth routing, rollback, and the sidecar `step` table are all explicitly left untouched.
- Single-commit plan with a clear, prefix-free imperative message — consistent with repo commit conventions.

### Out-of-scope observation (not a plan defect)

The live incident cited by note 42 names "three code-reviews plus the rescue editor" as readers that skipped the governing spec. This plan correctly fixes only `milestone-rescue` (the note's stated scope). The sibling `milestone-rescue-audit` has the same phase-level blind spot but is deliberately not in scope here; if desired, that would be a separate roadmap milestone, not a change to this plan.

PLAN_REVIEW_PASS
