## Code Review Summary

**Files Reviewed:** 1 plan + `src/skills/aif-docs/SKILL.md` + `references/REVIEW-CHECKLISTS.md` + spec note 48 + ROADMAP milestone (line 85) + repo AGENTS.md/CLAUDE.md
**Risk Level:** 🟢 Low

This is the second-round review. Plan v2 was revised against plan-review-1; the check below focuses on whether every review-1 finding is now closed and whether the expanded scope (two files) is complete and line-accurate.

### Context Gates

- **Roadmap:** Plan title matches ROADMAP.md line 85; governing spec is `.ai-factory/notes/48-aif-docs-index-in-claude-md.md`. Linkage OK.
- **Architecture:** `.ai-factory/ARCHITECTURE.md` carries no boundary/dependency rule on README/CLAUDE.md doc-index placement. No conflict.
- **Rules:** No `.ai-factory/RULES.md`. Skipped.
- **Spec deviation handling:** Plan explicitly documents the spec-note 48 internal contradiction (line 25 "review checklists unchanged" vs. line 14 "every place the README table is audited is retargeted") in its "Deviation from spec note 48" section and resolves it in-scope (Task 8), citing unambiguous intent and correctly declining a `milestone-rescue` escalation. This is the right call — the checklist file is where the enforced audit lives, so leaving it untouched would self-revert the feature. **Review-1 Critical Issue 1 resolved.**

### Review-1 findings — closure check

- **Critical Issue 1** (REVIEW-CHECKLISTS.md still mandates + auto-restores the README table) → **Closed** by Phase 3 / Task 8, retargeting lines 8, 44, 57. The self-reverting Standards-Compliance auto-fix (line 57) is retired and replaced with a CLAUDE.md-section check plus a legacy-README-table detector.
- **Issue 2** (dangling ordering reference at SKILL.md line 549) → **Closed** by Task 7(b), retargeting it to the CLAUDE.md `## Documentation` section.
- **Issue 3** (dual index home AGENTS.md + CLAUDE.md) → **Resolved** by the "Scope & invariants" carve-out and Task 7: the AGENTS.md `## Documentation` table is preserved as pre-existing behavior per spec item 6, only the redirect case defers to CLAUDE.md. Verified against this repo: AGENTS.md is a one-line redirect to CLAUDE.md, and CLAUDE.md already carries a `## Documentation` section — Task 7's carve-out applies cleanly here.
- **Issue 4** (CLAUDE.md not in ownership declarations) → **Closed** by Task 8b (Artifact Ownership + Important Rule #7), scoped to the section, not the whole file.
- **Issue 5** (Task 6 SKILL.md retarget was vacuous) → **Resolved**: Task 6 is now correctly framed as only the surface legacy-flag, with the substantive audit retarget explicitly delegated to Task 8 in the checklist file.

### Line-number & coverage verification

Every "documentation table" touchpoint in both files maps to a task with an accurate line reference:

| Touchpoint | Line | Task |
|-----------|------|------|
| SKILL.md Principle 3 | 21 | Task 1 |
| SKILL.md 2.2 template `## Documentation` | 291–298 | Task 2 |
| SKILL.md README rule | 311 | Task 2 |
| SKILL.md Step 1.1 consolidation link | 208 | Task 4 |
| SKILL.md State B stays-in-README | 374 | Task 5 |
| SKILL.md State B proposal example | 395 | Task 5 |
| SKILL.md State B execute split | 410 | Task 5 |
| SKILL.md Step 5 ordering ref | 549 | Task 7(b) |
| SKILL.md Artifact Ownership | 562 | Task 8b |
| SKILL.md Important Rule #7 | 574 | Task 8b |
| REVIEW-CHECKLISTS.md Technical | 8 | Task 8 |
| REVIEW-CHECKLISTS.md Readability | 44 | Task 8 |
| REVIEW-CHECKLISTS.md Standards auto-fix | 57 | Task 8 |

A fresh grep of both files for `documentation table` / `Documentation links` / `README Documentation` returns exactly these lines — no straggler is left uncovered. The AGENTS.md `## Documentation` template (SKILL.md 533/535/538) is deliberately and correctly excluded per spec item 6.

### Critical Issues

None.

### Positive Notes

- All 13 touchpoints across both files are accounted for with exact line numbers — the implementer can navigate directly, and the grep in the Verification section will confirm zero stragglers.
- The two-file scope is now correct and internally justified; the spec blind spot is documented rather than silently inherited.
- Task 7(b) additionally fixes the dangling ordering reference — an in-scope SKILL.md edit review-1 flagged as uncovered.
- Ownership is scoped to the CLAUDE.md `## Documentation` section only, not the whole file — right boundary, avoids over-claiming a file the skill doesn't own.
- Target format (`| Doc | What it covers |`) matches this repo's own CLAUDE.md convention (line 20) — grounded, not invented.
- Body-growth restraint (reword over add) respects the known >500-line constraint and correctly leaves the diet to the follow-on milestone (ROADMAP line 87 / note 49).
- Commit split (1: Tasks 1–3; 2: Tasks 4–7, 8b; 3: Task 8) is logically ordered and the messages follow the repo's no-prefix / sentence-case convention. The 8b-before-8 numbering is unusual but is explained by grouping the SKILL.md ownership edit with Phase 2 and isolating the checklist file as Commit 3 — intentional, not an error.
- Readability line 44 retargets to a CLAUDE.md section that a browsing "new user" won't read, but the ordering *intent* (getting-started → workflow → details) is preserved verbatim, so the check remains meaningful; no action needed.

### Verdict

Plan v2 closes all five review-1 findings, extends scope to the enforced checklist file with accurate line references, and documents its one spec deviation with sound reasoning. No blocking issues remain.

PLAN_REVIEW_PASS
