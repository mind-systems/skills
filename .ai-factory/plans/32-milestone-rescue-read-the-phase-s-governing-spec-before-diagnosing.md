# Plan: milestone-rescue: read the phase's `Governing spec:` before diagnosing

## Context
Make the ratified spec tier participate in every rescue: `milestone-rescue` must read a milestone phase's `Governing spec:` documents before any semantic diagnosis or repair, and judge recurring findings against them.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Edit milestone-rescue SKILL.md

- [x] **Task 1: Step 1 — read the phase's governing spec after identifying the slug**
  Files: `src/skills/milestone-rescue/SKILL.md`
  In Step 1 ("Discover artifacts"), after the "Identify the milestone slug" block, add an instruction: determine `$TARGET_FILE` (the same resolution logic already stated in Step 4 — argument-named file / ROADMAP_TESTS.md for test slugs / ROADMAP.md otherwise), read it, locate the phase section the milestone belongs to, and check the phase header and its intro lines for a `Governing spec:` reference. If present, read **every** named document in full before proceeding to Step 2 — unconditional, not suspicion-based. If the milestone is under no phase, or no `Governing spec:` is named, proceed as today. Keep it explicit that Step 4 retains its own `$TARGET_FILE` resolution and milestone-line locate logic (this read is additive, does not remove Step 4's read). Do not touch artifact discovery filters, the git-status command, or the multi-slug prompt.

- [x] **Task 2: Step 3 — judge recurring findings against the governing spec** (depends on Task 1)
  Files: `src/skills/milestone-rescue/SKILL.md`
  In Step 3 ("Extract root cause"), add a paragraph: when a governing spec was read in Step 1, judge the recurring findings against it. A candidate "specification gap" may actually be a violation of an already-ratified contract that the spec note failed to restate — the root cause and repair target differ (amend the spec note to carry the governing constraint vs. invent a new decision). The Diagnosis Report must state whether the failure violates the governing spec and quote the relevant clause. Keep this consistent with the existing root-cause-category and Diagnosis Report instructions; do not alter the narrative-register / shared-with-audit constraints.

- [x] **Task 3: "What NOT to do" — no semantic diagnosis without the governing-spec read** (depends on Task 2)
  Files: `src/skills/milestone-rescue/SKILL.md`
  In the "What NOT to do" section, add a bullet: do not issue a semantic diagnosis, blocker, or spec repair without having read the phase's `Governing spec:` documents when the phase names them — otherwise the ratified spec tier does not participate in the rescue at all. Also (per the spec note's "What NOT to do"): keep the governing-spec read unconditional (not suspicion-gated) and do not copy governing-spec content into the spec note wholesale — quote/restate only the clauses implicated by the findings. Fold these two constraints in wherever they read most naturally (the second belongs near the spec-note repair guidance). Leave depth routing, rollback, sidecar table, and git commands untouched; keep body ≤ 500 lines and frontmatter unchanged.

## Commit Plan
- **Commit 1** (after tasks 1-3): "Make milestone-rescue read the phase governing spec before diagnosing"
