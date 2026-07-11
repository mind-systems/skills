## Plan Review Summary

**Plan:** `.ai-factory/plans/84-1-15-detangle-pyramid-revision.md` (milestone 1.15 — detangle pyramid revision), revision 2
**Governing spec:** `.ai-factory/specs/35-detangle-pyramid-revision.md`
**Files Reviewed:** 1 plan + spec 35 + `src/skills/detangle/SKILL.md` (125 lines) + the four standards (`docs/context-tree.md`, `docs/skill-pyramid.md`, `docs/skill-composition-model.md`, global § "Grounding claims") + prior review `…-plan-review-1.md` + siblings `temporal-tree` / `roadmap-decompose-skeleton`
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap linkage** — OK: the plan's `# Plan: detangle — pyramid revision` heading resolves to `ROADMAP.md` line 187 (`- [ ] 1.15 — detangle: pyramid revision`), whose `Spec:` tag points at `specs/35-detangle-pyramid-revision.md`. Plan intent (audit-first, "no change" legal, protect the multi-tree raise, slim-in-place over links) matches the spec's Change/Guards. Aligned.
- **ARCHITECTURE.md** — no boundary/dependency issue: change is skill-body-internal, no module boundary crossed, no `loads:` edge introduced (a doc reference is not a Skill-tool load — correctly not added).
- **RULES.md** — n/a; CLAUDE.md conventions (one-home-per-fact, walkable-edge links) are honored, in fact they are the load-bearing rationale of the plan's shipped-skill constraint.
- **Spec fidelity** — the spec's literal "replace with a link" is correctly reconciled, not violated: for a globally-shipped skill the only always-available owner is the global rule, so "point at the owner" is satisfied by a by-name reference to global § "Grounding claims" or by slimming-in-place. Both honor the spec's one-home-per-fact intent; the plan's Context documents this reconciliation explicitly rather than silently diverging.

### Round-1 findings — all resolved
- **Finding 1 (dangling `docs/…` relink target).** Fully incorporated: the new **Shipped-skill constraint** block in Context, plus Task 1 lens 1 and Task 2's "No `docs/…` path link in the shipped body" guard, forbid a repo-doc path in the body and route any pointer to global § "Grounding claims" **by name**, preferring slim-in-place. Ground truth confirms the practice — `grep` over `src/skills/*/SKILL.md src/commands/*.md` for `context-tree|skill-pyramid|Grounding claims|global CLAUDE` returns **zero** hits, and both revised siblings carry no repo-doc link.
- **Finding 2 (imperative-safety).** Incorporated verbatim as Task 2's "Imperative-safety condition" guard — a restated imperative may be delinked/slimmed only if the always-loaded global rule already issues the same executor command (it does), else slim without removing the imperative.
- **Finding 3 (depth block over-pointing).** Incorporated as Task 1's "Caution on the depth block" lens — lines 116/117/118 are named as protected (own climb discipline, forest content, the deliberately-dropped "however much it takes" nuance), the block defaults to protection, and a line is flagged only on a clear one-to-one restatement.

### Critical Issues
None.

### Verification against current SKILL.md
- Line references are all accurate against the 125-line file: fractal model 14–24, "Before you start" 28–37, Step 2 climb 47–66, Step 3 forest 68–80, synthesis/ASCII-map 84–103, intent split 105–108, depth rules / what-not-to-do 113–126, protected lines 116/117/118. No stale offsets.
- Frontmatter assumption verified: `name` / `description` / `argument-hint` only — no `loads:` / `allowed-tools`. Task 2's "none added" guard is correct.
- Task 3's baseline analogue is sound: no proto/DTO exists in this meta-repo, so an engine consumed by multiple callers (`note`, reached via `grep -l "note" src/skills/*/SKILL.md src/commands/*.md`) is a legitimate in-repo stand-in for a cross-project forest raise; the grep syntax matches the CLAUDE.md reverse-graph convention.

### Positive Notes
- **Genre structure is correct:** read-only audit (Task 1) → conditional apply (Task 2, skipped on conformance) → conditional live baseline (Task 3, only if the body changed) maps cleanly onto spec 35's "revision, not a mandated rewrite" and "'no change' + a one-paragraph audit report is a legal, complete outcome."
- **Spec hard guard honored:** the multi-tree shared-contract raise (Step 3 + line 117) and the leaf→trunk climb are protected as detangle's own content, "never reduced to a doc link," verbatim to spec 35's Guards.
- **The plan constrains without expanding:** Task 2's final guard forbids adding content or inventing a `references/` split — a revision only removes / relinks / re-registers, matching the spec's behavior-identical mandate.

## Deferred observations
- Affects: the pyramid direction's hard rule ("skills link to them, never restate them") vs. globally-shipped skills — This tension is broader than milestone 1.15 and is now well-managed *within* the plan (route to the global rule; slim in place). What remains outside this milestone's file boundary is the direction text itself, which still literally says "link to them" while every shipped top-level skill (detangle, temporal-tree, the roadmap family) provably cannot host a walkable `docs/*.md` edge. Aligning the direction's wording with the observed practice ("audit against the docs" ≠ "link into the body") is a direction-level edit for a future pass, not a defect in this plan.

PLAN_REVIEW_PASS
