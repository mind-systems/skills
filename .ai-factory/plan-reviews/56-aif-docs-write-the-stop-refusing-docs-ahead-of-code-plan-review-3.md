## Plan Review 3 — aif-docs: write the ТЗ, stop refusing docs-ahead-of-code

**Plan:** `.ai-factory/plans/56-aif-docs-write-the-stop-refusing-docs-ahead-of-code.md`
**Spec:** `.ai-factory/specs/10-aif-docs-rewrite-tz.md`
**Target files:** `src/skills/aif-docs/SKILL.md`, `references/REVIEW-CHECKLISTS.md`, `references/topic-guides.md`
**Files Reviewed:** 4 (plan + 3 targets, plus spec + roadmap)
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md`, present): no aif-docs-specific boundary or composition rule; the plan touches no `loads:` edge and no engine contract, and it holds `ARCHITECTURE.md` read-only (check-don't-clobber) throughout. **PASS.**
- **Rules** (`.ai-factory/RULES.md`): absent. **WARN** (optional file missing) — no convention source to check against.
- **Roadmap** (`.ai-factory/ROADMAP.md:123`): the milestone line "aif-docs: write the ТЗ — stop refusing docs-ahead-of-code" (`Spec: .ai-factory/specs/10-aif-docs-rewrite-tz.md`) exists, is unchecked, and its `Spec:` tag resolves to the present spec note. The plan's `# Plan:` heading matches it. The ROADMAP diff (2 insertions) only adds this milestone line — no unrelated churn. **PASS.**
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present — no project override to apply.

### Verification performed
- Re-ran all three spec greps against the current `src/skills/aif-docs/`. **Every** hit is enumerated by an owning task:
  - `3d`/`Document-Driven`/`MODE = 3D`: SKILL.md:4, 64, 68–70, 72, 74, 76, 83, 95, 345, 395, 400 → Tasks 2/3; REVIEW-CHECKLISTS.md:11, 12, 15 → Task 4.
  - nav residue: REVIEW-CHECKLISTS.md:43 → Task 4; topic-guides.md:8 → Task 5.
  - orphaned mode vocab: SKILL.md:24 → Task 1; SKILL.md:69 (removed with the MODE-detection block) → Task 2; SKILL.md:97 (`**If MODE = normal:**`) → Task 3's Step 1 rewrite; SKILL.md:391 → Task 3; REVIEW-CHECKLISTS.md:15 → Task 4. No un-cited occurrence exists; `consolidation.md`/`html-generation.md` are clean.
- Confirmed every line citation (`:3`, `:4`, `:13-15`, `:24`, `:64`, `:67-70`, `:72-92`, `:93-97`, `:345`, `:391`, `:395-400`; REVIEW-CHECKLISTS `:11/:12/:15/:43/:44`; topic-guides `:8`) points at exactly the text described.
- The single-mode collapse is fully covered: Task 2 removes the `**If MODE = 3D:**` branch (`:95`) and Task 3 rewrites Step 1 (`:93-97`), together deleting both `MODE = 3D` and `MODE = normal` (`:97`) labels.
- Spec Change items all land: item 1 (delete 3d wholesale) → Tasks 2+4; item 2 (one mode writes ТЗ, referent-conditional accuracy, no lead/lag meta) → Tasks 3+4; item 3 (feature-cross-link tree, purge linear-nav) → Tasks 4+5; item 4 (reference the CLAUDE.md index, one-home-per-fact, coordination-trio staleness with ARCHITECTURE.md check-don't-clobber) → Task 1 plus Task 3's "Coordination-trio staleness" sub-block.
- Spec Guards honored: no lead/lag meta-commentary (repeated in Tasks 1, 3, 6); no fork (Step 2 State A / A-B-C machine / `--web` / checklists all kept); Principle 6 cited **by name** against numbering drift; `upstream/` and `aif-architecture` untouched; body only shrinks (stays ≤500).
- Dependency chain (1→2→3→4→5→6) is coherent; the two-commit split (1–3, then 4–6) is safe — Task 6 greps both SKILL.md and references after all edits land in commit 2. Commit subjects are imperative, sentence-case, no type prefix, no trailing period — consistent with repo git conventions.

### Round-2 finding — resolved
Plan-review-2's single LOW finding — Task 4's ARCHITECTURE.md tree-link criterion not reconciled with Task 3's read-only stance — is now landed. Task 4 explicitly marks the ARCHITECTURE.md tree-link line **check-only for aif-docs** ("verify the links' presence; authoring/repairing them is aif-architecture's or a human's job… mirror Task 3's check-don't-clobber stance so the checklist item never drives an edit into that file"). **Closed.**

### Critical Issues
None.

### Findings
None. This revision cleanly closes the last open finding without over-correction or scope creep, and independent grep reproduction shows zero drift between plan and code.

### Positive Notes
- Complete token coverage independently reproduced by grep — every `3d`/nav/orphaned-mode hit is owned by a task, with exact line numbers.
- The plan pins Principle 6 **by name** (anticipating numbering drift) and protects the frontmatter invocation trigger phrases so auto-selection can't regress while the descriptive clause is reframed ТЗ-first.
- The "no lead/lag meta-commentary" guard is repeated at every task that could reintroduce it (Tasks 1, 3, 6), preserving the spec's strongest insight (spelling out the duality is what spawned `3d`).
- Task 6's grep sweep is widened to catch orphaned bare-`mode` vocabulary that the token greps alone would miss, with a correct false-positive caveat ("`mode` inside `model` is fine").
- Scope discipline matches the spec's "no fork this pass" boundary precisely; ARCHITECTURE.md stays read-only across Task 3, Task 4, Step 0, and Artifact Ownership.

PLAN_REVIEW_PASS
