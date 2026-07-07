## Plan Review 2 — aif-docs: write the ТЗ, stop refusing docs-ahead-of-code

**Plan:** `.ai-factory/plans/56-aif-docs-write-the-stop-refusing-docs-ahead-of-code.md`
**Spec:** `.ai-factory/specs/10-aif-docs-rewrite-tz.md`
**Target files:** `src/skills/aif-docs/SKILL.md`, `references/REVIEW-CHECKLISTS.md`, `references/topic-guides.md`
**Files Reviewed:** 4 (plan + 3 targets, plus spec + roadmap)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`, present): no aif-docs-specific boundary or composition rule; the plan touches no `loads:` edge and no engine contract. **PASS.**
- **Rules** (`.ai-factory/RULES.md`): absent. **WARN** (optional file missing) — no convention source to check against.
- **Roadmap** (`.ai-factory/ROADMAP.md:123`): the milestone line "aif-docs: write the ТЗ — stop refusing docs-ahead-of-code" (`Spec: .ai-factory/specs/10-aif-docs-rewrite-tz.md`) exists, is unchecked; the plan's `# Plan:` heading matches it; the spec note resolves. **PASS.**
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present — no project override to apply.

### Round-1 findings — all resolved
This revision was written against plan-review-1's three findings; each is now landed:
1. **Residual "mode" vocabulary.** Task 1 now drops Principle 6's dangling clause (`:24` "every run, **every mode**, no exceptions" → "every run, no exceptions"); Task 3 sweeps the "No-motivation pass (mandatory, **all modes**)" heading (`:391`) to "(mandatory)" and removes the `MODE = normal` label; Task 6 adds a `grep -rin "all modes\|every mode\|MODE = normal"` sweep with the sensible "bare `mode` inside `model` is fine" caveat. **Closed.**
2. **Coordination-trio staleness (spec Change item 4).** Task 3 now carries an explicit "Coordination-trio staleness" sub-block wiring the on-each-run README / CLAUDE.md-index / ARCHITECTURE.md check into the State C audit, with the "check-don't-clobber, ARCHITECTURE.md stays read-only" stance stated. **Closed.**
3. **Frontmatter `description` scope.** Task 1 now declares the frontmatter `description` (`:3`) **in scope** as router-facing skill identity, and pins the invocation trigger phrases ("create docs", "write documentation", "update docs", "generate readme", "document project") as must-keep-intact. **Closed.**

### Verification performed
- Re-ran all spec greps against `src/skills/aif-docs/`. Every `3d`/`3д`/`MODE = 3D`/`Document-Driven` hit (SKILL.md:4, 64, 68-70, 72, 74, 76, 83, 95, 345, 395, 400; REVIEW-CHECKLISTS.md:11, 12, 15), every nav-residue hit (REVIEW-CHECKLISTS.md:43, topic-guides.md:8), and every orphaned-mode hit (SKILL.md:24, 97, 391) is enumerated by a task. No un-cited occurrence exists; `consolidation.md`/`html-generation.md` are clean. Task 2/3/4/5 coverage is complete.
- Confirmed line citations (`:3`, `:4`, `:13-15`, `:24`, `:64`, `:67-70`, `:72-92`, `:93-97`, `:345`, `:391`, `:395-400`; REVIEW-CHECKLISTS `:11/:12/:15/:43/:44`; topic-guides `:8`) all point at exactly the text described.
- Task 2 removing the `**If MODE = 3D:**` branch (`:95`) plus Task 3's Step 1 rewrite (`:93-97`) together remove both the `3D` and the `MODE = normal` (`:97`) branch labels — the single-mode collapse is fully covered.
- Dependency chain (1→2→3→4→5→6) and the two-commit split are coherent; commit subjects are imperative, sentence-case, no type prefix, no trailing period — consistent with repo git conventions.
- Spec Guards all honored: no lead/lag meta-commentary (repeated in Tasks 1, 3, 6); no fork (Step 2 State A / A-B-C machine / `--web` / checklists all kept); Principle 6 cited by name; `upstream/` and `aif-architecture` untouched; body shrinks (stays ≤500).

### Critical Issues
None.

### Findings

**1. (LOW) Task 4's ARCHITECTURE.md tree-link criterion isn't reconciled with Task 3's read-only stance.**
Task 4 replaces the linear-nav items in `REVIEW-CHECKLISTS.md` with the feature-cross-link tree model, carrying the spec's phrasing "*in ARCHITECTURE.md, module/subsystem mentions link to their topic docs*" into a review checklist. As a **check**, its failure state ("ARCHITECTURE.md module mentions don't link to topic docs") has no aif-docs-owned remediation — Task 3, Step 0, and Artifact Ownership all hold ARCHITECTURE.md read-only ("check for staleness, don't clobber… no aif-architecture edit"). An implementer wiring this checklist item without the colocated guard could produce a criterion that drives edits into a read-only file, contradicting Task 3. The plan already resolves this tension in Task 3 (prominent read-only stance), so the risk is small — but the reconciliation lives in a different task than the checklist wording. Recommend Task 4 add a half-sentence that the ARCHITECTURE.md tree-link line is **check-only** for aif-docs (verify presence; the links themselves are aif-architecture's / a human's to author), mirroring Task 3. This is in-scope (references/REVIEW-CHECKLISTS.md is a target file) and inherited from spec items 3+4, whose own item-4 guard is the reconciliation to cite.

### Positive Notes
- The revision is a precise, targeted response to plan-review-1 — each of the three findings is closed at the exact task and line it was raised against, with no over-correction and no scope creep.
- Task 1 pins Principle 6 **by name** (anticipating numbering drift) and now also explicitly protects the frontmatter trigger phrases so auto-selection can't regress — a subtle failure mode caught.
- The "no lead/lag meta-commentary" guard is repeated at every task that could reintroduce it (Tasks 1, 3, 6), preserving the exact insight (spelling out the duality is what spawned `3d`) that is the spec's strongest guard.
- Task 6's grep sweep was widened to catch orphaned bare-`mode` vocabulary that the token greps alone would miss, with a correct false-positive caveat.
- Line citations are exact and independently reproduced by grep — zero drift between plan and code.
