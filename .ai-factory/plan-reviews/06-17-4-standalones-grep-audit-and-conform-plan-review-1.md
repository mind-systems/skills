# Plan Review: 17.4 — Standalones: grep-audit and conform

## Code Review Summary

**Files Reviewed:** plan + governing spec (`.ai-factory/specs/65-standalone-skills-conformance.md`) + contract line (ROADMAP 17.4) + `src/skills/detangle/SKILL.md` + the six certified-clean files (by grep)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md` present; a one-word prose substitution inside a skill body crosses no module boundary and touches no `loads:` edge. No misalignment. PASS.
- **Rules** — `.ai-factory/RULES.md` absent. WARN (optional file, not a defect).
- **Roadmap** — ROADMAP 17.4 is present and `[ ]`, at the seam. The plan's scope matches the contract line item-for-item: `detangle` the one real token, six certified clean, `aif-skill-generator` excluded. Linkage is explicit. PASS.
- **Reference walk** — contract line → `Spec: .ai-factory/specs/65-standalone-skills-conformance.md` → `Governing spec: docs/reserved-words.md`. All three read; the plan conforms to each.

### Verified against ground truth

Every factual claim in the plan re-derived against the working tree:

- `rg -U -in 'milestones?' src/skills/detangle/SKILL.md` → exactly one hit, **line 33**, text matching the plan verbatim. ✅
- `rg -U -in 'spec\s+notes?|milestones?'` over the six files → exit 1, zero hits. ✅
- `rg -in 'spec-note'` over the six → exit 1, zero hits. ✅
- `rg -U -in 'spec\s+notes?|spec-note' src/skills/detangle/SKILL.md` → exit 1. The plan's single-edit claim holds for the *other* synonym family too, which the plan does not assert but which is now confirmed.
- `detangle` frontmatter is `name` / `description` / `argument-hint` only — no `loads:` field, as the plan states. ✅
- The two certify-don't-edit `field` sites are at lines 15 and 42, both generic code elements, exactly as described. ✅

The linguistic call is also right: collapsing `roadmap milestone` → `task` rather than `roadmap task` follows reserved-words' qualifier rule, and `task` (not `phase`) is the correct registry word for the `N.M` unit whose in-progress state moves an impact analysis. The resulting sentence reads grammatically — the article `an` binds to `in-progress`, not to the substituted noun.

### Critical Issues

None.

### Findings

**1. The `git status --short` gate as written is already false, before any edit** — plan line 87.

The gate says: *"`git status --short` → **exactly one modified file**, `src/skills/detangle/SKILL.md`. Nothing under `upstream/`, nothing under `active/`, **no new files**."*

At plan time `git status --short` already returns:

```
?? .ai-factory/plans/06-17-4-standalones-grep-audit-and-conform.json
?? .ai-factory/plans/06-17-4-standalones-grep-audit-and-conform.md
```

These are the orchestrator's own artifacts for this very task, and more will land during the run (this plan-review file, the review file, the sidecar). An implementer reading the gate literally sees new files that the gate forbids, and has no stated basis for distinguishing "my edit strayed" from "the pipeline wrote its own bookkeeping." The likely outcomes are both bad: either a phantom reconciliation loop, or the implementer learns to wave the gate through — which costs the gate its real function of catching a stray edit under `upstream/` or `active/`.

The fix is to scope the gate to the source tree rather than the whole worktree, e.g. `git status --short -- src/ active/ upstream/` → exactly one line, `M src/skills/detangle/SKILL.md`. This preserves the gate's actual intent (nothing strayed into the pristine mirror or the symlink layer) while being true at run time. The companion `git diff --stat` gate on line 88 is unaffected — untracked files do not appear in it — so only the one line needs restating.

**2. "two lines above" is off by one** — plan line 47.

The justification for dropping the `roadmap` qualifier reads *"the enclosing paragraph names `.ai-factory/ROADMAP.md` two lines above."* `ROADMAP.md` appears on line 30; the edit site is line 33 — three lines above. The reasoning is sound and the conclusion is correct (the roadmap context *is* established within the paragraph, so the qualifier does no disambiguating work); only the count is wrong. Worth correcting because this plan's whole discipline is that stated line facts are re-derivable — a reader who checks this one and finds it off has less reason to trust the ones that matter.

### Positive Notes

- **The anti-manufacture guard is the plan's best feature.** Stating up front that one changed line across seven files is success, and naming a discretionary improvement in the clean six as *a review finding*, directly counters the failure mode this task is most exposed to. It is repeated at the point of action in Task 2 rather than left in the preamble.
- **Both grep strengthenings are recorded rather than silently applied,** with the concrete reason (the `[^-]` anchor cannot match a line-initial occurrence; the `\s` form is blind to `spec-note`) and the evidence (17.3 hit both blind spots in its own files). This is exactly the right handling of a plan that improves on its spec — the deviation is auditable, and both strengthenings are strictly-stronger on files expected to return zero, so they cannot mask a regression.
- **The certified no-change sites are listed with their reasons** — `field` at 15 and 42, `temporal-tree`'s `named roadmap` and `named-roadmap`, `observe-logs`' and `command-handoff`'s generic `field`. Certification therefore does not depend on the implementer rediscovering why each is legal, which is what turns a certification into a rewrite.
- **Stop-and-report on an unexpected hit** (line 76) is the correct escalation: a hit in the certified six means the spec's inventory is wrong, and amending the spec must precede touching the file. The plan does not authorize improvising an edit.
- **The Task 4 deviation is honest and well-argued.** `detangle` emits free-form analytical prose that is not byte-comparable between runs, and no pre-conformance baseline exists; a live run would be an unanchored smoke test. The substituted static check is specific rather than hand-wavy — it names the `Step 4` pointer as a live internal reference that must survive, which is the one thing on that line that could actually break something.
- **`aif-skill-generator`'s exclusion is given its mechanism, not just its verdict** — the `active/` → `upstream/` symlink and the conflict-free-sync split it protects. An implementer who understands *why* will not "just check" it.

## Deferred observations

None.
