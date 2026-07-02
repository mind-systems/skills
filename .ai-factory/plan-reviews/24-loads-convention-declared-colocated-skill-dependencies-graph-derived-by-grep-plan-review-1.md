# Plan Review: `loads:` convention — declared, colocated skill dependencies

**Plan:** `24-loads-convention-declared-colocated-skill-dependencies-graph-derived-by-grep.md`
**Files Reviewed:** 8 (5 depending skills, milestone-rescue, milestone-rescue-audit, CLAUDE.md) + edge-completeness sweep across all `src/skills` / `src/commands`
**Risk Level:** 🟢 Low

## Context Gates

- **Architecture (`.ai-factory/ARCHITECTURE.md`):** The plan is a direct expression of the "Composition: mechanism vs policy" model — engines hold mechanism, philosophies hold policy and stay in control. Declaring one-way `loads:` edges (engines never list callers) is fully aligned with caller-agnosticism. No boundary violation. **PASS.**
- **Rules:** Edits are confined to `src/` (authored layer) and `CLAUDE.md`; `upstream/ai-factory/` is explicitly untouched — matches the three-way-split invariant in project CLAUDE.md. Space-separated `loads:` value mirrors the existing `allowed-tools:` convention. **PASS.**
- **Roadmap:** This is meta/skill infrastructure work on the skills repo itself; no application-milestone linkage expected. **WARN (informational only)** — no ROADMAP entry referenced, which is fine for a convention change of this scope.

## Verification of the Plan's Codebase Assumptions

Every factual claim in the plan was checked against the actual files:

- **Edge set is complete and accurate.** The four skills carrying `Skill` in `allowed-tools` are exactly `roadmap-outline`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-test-coverage`. Their real load targets match the plan verbatim:
  - `roadmap-outline` → `roadmap-engine` (SKILL.md:75, :146) ✓
  - `roadmap-decompose` → `roadmap-engine` (:136, :187, :208) ✓
  - `roadmap-decompose-skeleton` → `roadmap-engine` + `test-philosophy` (:31, :42–43, :83) ✓
  - `roadmap-test-coverage` → `test-philosophy` (:64) ✓
  - `roadmap-engine` → `note` (content-level load instruction at :29) ✓
- **Correctly excludes non-edges.** `roadmap-test-coverage → roadmap-decompose` is a user handoff, not a load ("Do not run `/roadmap-decompose` automatically", :281) — the plan rightly omits it. The description's "deep-research agents" (:6) are `Agent`-spawned research workers, not a `Skill`-load of a `deep-research` skill; no body reference exists, so no edge — correctly omitted.
- **`test-philosophy` and `note` load nothing** — no `loads:` field for them, as the plan states.
- **Task 3 line references are accurate.** `milestone-rescue/SKILL.md:115` is "Form: a chronological narrative in plain prose"; `milestone-rescue-audit/SKILL.md:145–146` already says "the same register as `milestone-rescue`'s Diagnosis Report". The both-ends declaration is genuinely one-sided today and the plan patches the correct (rescue) end.
- **Task 4 CLAUDE.md anchor exists** — `## Skill Authoring` → `### Composition — mechanism vs policy` is present; adding a sibling `###` subsection is structurally sound.
- **Frontmatter safety assumption holds.** Extra keys (`disable-model-invocation`, `user-invocable`) already coexist in these files, confirming the harness ignores unknown fields — `loads:` is safe.

## Observations (non-blocking, informational)

1. **Task 2 verifier should lean on the body-instruction grep, not just `Skill` in `allowed-tools`.** `roadmap-engine` legitimately declares `loads: note` yet has `allowed-tools: Read` (no `Skill`) — because the *caller* executes the load. The "Skill in allowed-tools" half of the heuristic would not surface `roadmap-engine`; only the "Skill-tool load instructions" grep (which catches its body line :29) does. The plan lists both greps, so it is internally consistent — but whoever runs Task 2 should treat the body-instruction grep as the authoritative one for content-level engines, or `roadmap-engine→note` could be missed. Worth stating explicitly in the task so the verifier doesn't rely on the frontmatter signal alone.

2. **Reverse-graph grep in Task 4 is intentionally broad.** `grep -l "<name>" src/skills/*/SKILL.md src/commands/*.md` matches *any* mention — the engine's own `name:` line, prose references, and load edges alike — not purely `loads:` edges. For the stated purpose ("find an engine's callers before touching it") the broad form is arguably safer (it also catches prose coupling), so this is defensible; just note in the doc that the result is "mentions," and that `grep -l "loads:.*<name>"` narrows it to true load edges if a clean reverse-edge list is wanted. No change required — just be precise in the wording so a reader doesn't over-trust the raw match set.

## Positive Notes

- The plan respects the repo's core invariant (edit `src/`, never `upstream/`) and the caller-agnosticism rule, and it explicitly rejects the cache-without-invalidation design (no static map, no `loaded-by:`) — the reasoning is sound and consistent with the existing `roadmap-decompose-skeleton` "Call graph" section, which it correctly leaves in place as colocated.
- Line-number targeting, edge inventory, and the false-positive exclusions (`ui-ux-pro-max`'s "How to Use This Skill" heading; the `roadmap-decompose` handoff) are all accurate — this plan was written against the real files, not from memory.
- Phasing (declare → verify → both-ends invariant → doc) with explicit dependencies is clean and the behavior-identical constraints on Task 3 are correctly scoped.

The two observations are refinements to the *wording* of Tasks 2 and 4, not defects — the implementation as specified will produce correct, consistent results. No missing steps, no wrong assumptions, no bad paths, no migrations owed.

PLAN_REVIEW_PASS
