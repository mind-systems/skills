## Plan Review Summary

**Files Reviewed:** 1 plan (`54-roadmap-prune-step-6-speaks-the-direction-section-grammar.md`), target skill `src/skills/roadmap-prune/SKILL.md`, governing spec `.ai-factory/specs/08-prune-direction-section-vocabulary.md`, roadmap contract line (`.ai-factory/ROADMAP.md:119`), grammar source `src/skills/roadmap-engine/SKILL.md`
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture (`.ai-factory/ARCHITECTURE.md`):** OK. The change touches only `roadmap-prune`'s instruction body; no `loads:` edge, no engine/philosophy boundary, no composition contract is altered. Aligns with "Composition: mechanism vs policy" (§30) — prune stays a policy skill, no mechanism moves.
- **Rules (`.ai-factory/RULES.md`):** Not present — WARN (optional file absent, non-blocking).
- **Roadmap linkage:** OK. Contract line present at `ROADMAP.md:119` (`- [ ] **roadmap-prune: Step 6 speaks the direction-section grammar**`), tagged `Spec: .ai-factory/specs/08-prune-direction-section-vocabulary.md`. The plan's `# Plan:` heading matches the milestone title. Governing spec 08 traces back to a deferred observation carried through milestone 52's plan-reviews — the follow-through is real, not invented scope.

### Verification of plan claims against the codebase
- Line anchors are exact: `:218` = "Delete the pruned `[x]` tasks from `## Milestones`", `:222` = "Keep `## Milestones` with all remaining `[ ]` tasks", `:226`–`:231` = the emptied-phase sweep, `:101` = "Never copy a phase or section header as a feature name." All confirmed against the current file.
- The "new grammar" premise is real: `roadmap-engine/SKILL.md:53–65` defines `## <Direction name>` → `### Phase N` → `N.M` tasks, with globally-sequential phase numbers and legal gaps (`:76–80`). The emptied-direction sweep's no-renumber guard (Task 2 clause a) mirrors the same invariant the emptied-phase sweep already states (`:227–230`).
- The flat-shape claim holds: this repo's own `ROADMAP.md` uses `## Milestones` (single flat list), so the "flat behavior must remain exactly correct" constraint is load-bearing and correctly emphasized.
- Task decomposition maps 1:1 onto the spec: spec change #1 → Task 1 (vocabulary generalization); spec changes #2+#3 → Task 2 (emptied-direction sweep + retain-rule coexistence). The dependency (Task 2 depends on Task 1) is correct — the direction sweep sits "one level up" from wording Task 1 introduces.
- Task 2 correctly requires deleting both the `## <Direction name>` header **and its preamble prose**, matching the grammar where a direction carries preamble text directly under its header (`roadmap-engine:55`).
- Guards are complete and internally consistent: Step-6-only scope, no renumbering, ≤500 lines (306 today; +~2 sentences is safe), and the byte-identical protection of Steps 0–5/7/8, the commit policy, "What NOT to do", and the `:101` rule.

### Critical Issues
None. The plan is faithful to the governing spec, its codebase assumptions are accurate, file paths and line anchors are correct, and no migration or security surface is involved (instruction-only skill edit).

### Positive Notes
- Tight scoping: the plan repeats the spec's "Step 6 only" boundary in both task bodies and the Guards block, reducing the risk of an implementer drifting into adjacent steps.
- The plan preserves prune's instructions-only register explicitly ("no rationale prose"), matching the skill's established `What NOT to do` constraint (`:282`).
- The retain-rule interplay is stated as a guard clause (Task 2 clause b), not left implicit — this is exactly the "declare the coexistence" pattern the existing emptied-phase sweep already uses (`:230–231`).

## Deferred observations
- Affects: `.ai-factory/specs/08-...` future milestone / `roadmap-prune` Step 1 (`SKILL.md:68`) and Step 7 (`SKILL.md:246`) — Two further literal "Milestones" references survive outside Step 6: Step 1's "leave ~20 lines of active context in Milestones" and Step 7's "The Milestones section still reads coherently without the pruned tasks." For a two-level (direction-grammar) roadmap these name a section that doesn't exist, the same latent gap this milestone fixes in Step 6. The spec and plan deliberately guard Steps 1 and 7 as byte-identical, so correcting them here would contradict the plan's own scope boundary — hence a deferred observation for a follow-up milestone rather than a finding against this plan. The verify step (Step 7) in particular would benefit from the shape-covering wording once someone opens that scope.

PLAN_REVIEW_PASS
