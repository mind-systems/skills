# Plan Review: 17.4 — Standalones: grep-audit and conform (round 2)

## Code Review Summary

**Files Reviewed:** plan + governing spec (`.ai-factory/specs/65-standalone-skills-conformance.md`) + contract line (ROADMAP 17.4) + `src/skills/detangle/SKILL.md` + the six certified-clean files (by grep) + prior plan-review round 1
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md` present; a one-word prose substitution inside a skill body crosses no module boundary, touches no `loads:` edge, and adds no skill-graph node. No misalignment. PASS.
- **Rules** — `.ai-factory/RULES.md` absent. WARN (optional file, not a defect).
- **Roadmap** — ROADMAP 17.4 present and `[ ]`, at the seam (17.1–17.3 are `[x]`, 17.5 is `[ ]` and explicitly ordered after 17.1, which has landed). The plan's scope matches the contract line item-for-item: `detangle` the one real token, `temporal-tree`'s `named roadmap` re-audited to no change, five more certified clean, `aif-skill-generator` excluded as upstream-pristine. Linkage explicit. PASS.
- **Reference walk** — contract line → `Spec: .ai-factory/specs/65-standalone-skills-conformance.md` → `Governing spec: docs/reserved-words.md`. All three read; the plan conforms to each, and its two documented strengthenings of the spec's gate expression are additive, not contradictory.

### Round-1 findings — both resolved

- **Finding 1 (the `git status` gate was false before any edit)** — fixed at plan line 87. The gate now reads `git status --short -- src/ active/ upstream/` → exactly one line, `M src/skills/detangle/SKILL.md`. Re-derived just now: that scoped command returns **empty** on the current tree, so after the single edit it returns exactly the one expected line. The plan also added a paragraph explaining *why* the path scope is load-bearing (unscoped output carries the pipeline's own untracked artifacts), which preserves the gate's function instead of teaching the implementer to wave it through. Correctly fixed.
- **Finding 2 ("two lines above" off by one)** — fixed at plan line 47, now "three lines above". Verified: `.ai-factory/ROADMAP.md` is named on `detangle:30`, the edit site is line 33.

### Verified against ground truth

Every factual claim in the plan re-derived against the working tree in this session:

- `rg -U -in 'milestones?' src/skills/detangle/SKILL.md` → exactly one hit, **line 33**, reading `in-progress or planned roadmap milestone? That changes the impact analysis in Step 4.` — matching the plan verbatim, including the wrap (line 32 ends `part of an`). ✅
- `rg -U -in 'spec\s+notes?|milestones?'` over the six certified files → exit 1, zero hits. The plan's bare-form strengthening returns zero exactly as the spec's `[^-]`-anchored form does. ✅
- `rg -in 'spec-note'` over the six → exit 1, zero hits. ✅
- `detangle` frontmatter is `name` / `description` / `argument-hint` only — no `loads:` field, so the byte-stability guard is vacuous here as the plan states. ✅
- The two certify-don't-edit `field` sites are at lines 15 and 42, both generic code elements. ✅
- `### Step 4 — Synthesize` exists at line 80 — the trailing step pointer the plan names as a live internal reference is real and resolvable. ✅
- The edit site sits inside `## Before you start — load project context` (line 28), the section Task 4 requires re-reading whole. ✅

The linguistic call remains right: collapsing `roadmap milestone` → `task` rather than `roadmap task` follows the reserved-words qualifier rule (the roadmap context is established three lines above), and `task` rather than `phase` is the correct registry word for the `N.M` unit whose in-progress state moves an impact analysis. The article `an` binds to `in-progress`, not to the substituted noun, so the sentence stays grammatical.

### Critical Issues

None.

### Findings

None.

### Positive Notes

- **The anti-manufacture guard survived the revision intact** and is still stated twice — once in Context, once at the point of action in Task 2 — naming a discretionary edit in the clean six as *a review finding*. For a task whose success condition is one changed line across seven files, this is the single most load-bearing sentence in the plan.
- **The round-1 fix improved on what was asked.** The finding only required the gate be made true; the plan additionally recorded why the path scope exists, so a future reader cannot "simplify" it back to an unscoped `git status` without noticing what that costs.
- **Both grep strengthenings stay recorded rather than silently applied,** each with its mechanism (the `[^-]` anchor cannot match a line-initial occurrence; the `\s` form is structurally blind to `spec-note`) and its evidence (17.3 hit both blind spots). Both are strictly stronger on files expected to return zero, so neither can mask a regression.
- **Certified no-change sites carry their reasons** — `field` at 15 and 42, `temporal-tree`'s `named roadmap` and attributive `named-roadmap`, `observe-logs`' and `command-handoff`'s generic `field`, `temporal-tree`'s `loads: roadmap-engine`. Certification does not depend on the implementer rediscovering why each is legal, which is what would turn a certification back into a rewrite.
- **Stop-and-report on an unexpected hit** is the correct escalation: a hit in the certified six means the spec's inventory is wrong, and amending the spec precedes touching the file. No improvised edit is authorized.
- **The Task 4 deviation is honest and well-argued** — `detangle` emits free-form analytical prose that is not byte-comparable across runs and no pre-conformance baseline exists, so the substituted static read is the stronger feasible check. It names the `Step 4` pointer specifically, which is the one thing on that line that could actually break something.
- **`aif-skill-generator`'s exclusion is given its mechanism** — the `active/` → `upstream/` symlink and the conflict-free-sync split it protects — plus an explicit "do not open it to check", which forecloses the curiosity path.

PLAN_REVIEW_PASS
