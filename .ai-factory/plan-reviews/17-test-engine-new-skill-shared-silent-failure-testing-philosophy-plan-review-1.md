# Plan Review: test-engine — new skill — shared silent-failure testing philosophy

**Plan:** `.ai-factory/plans/17-test-engine-new-skill-shared-silent-failure-testing-philosophy.md`
**Files Reviewed:** plan + 5 codebase files (source skill, spec note, roadmap-engine, CLAUDE.md, ARCHITECTURE.md, ROADMAP.md)
**Risk Level:** 🟢 Low

## Context Gates

- **Architecture (`ARCHITECTURE.md` → "Composition: mechanism vs policy"):** WARN (informational).
  The plan aligns with the load-once, caller-in-control, pure-content pattern the doc prescribes.
  One vocabulary friction: ARCHITECTURE distinguishes **engine = mechanism** from **philosophy = policy**.
  The silent-failure discriminator is *policy* (a gate/lens that decides), yet the skill is named
  `test-engine` and the plan instructs it to follow the `roadmap-engine` (mechanism) framing. This is a
  pre-decided, roadmap-locked name (ROADMAP.md:43) — not something the plan should relitigate — but the
  framing paragraph should describe it as a shared *philosophy/discriminator* unit, not an "engine," to
  avoid mislabeling policy as mechanism. The plan text already says "philosophy unit," so this is minor.
- **Rules (`RULES.md`):** WARN — file absent (optional). No explicit convention violations detectable.
- **Roadmap (`ROADMAP.md`):** PASS. Work is linked to milestone at ROADMAP.md:43, and the sequencing is
  explicitly tracked (see below). Milestone alignment is clean.

## Verification of Plan Claims

All line references in the plan were checked against the live source and are **accurate**:

- Core question — `roadmap-test-coverage/SKILL.md:64-68` ✓ (blockquote at 66–68).
- Loud/silent table — `SKILL.md:70-76` ✓.
- Class A/B corollary — `SKILL.md:244-250` ✓.
- Registration target: custom-skills list at `CLAUDE.md:115` ✓; tree entry near `roadmap-engine/` at `CLAUDE.md:30` ✓.
- Frontmatter (`name: test-engine`, `user-invocable: false`, `disable-model-invocation: false`,
  `allowed-tools: Read`) matches spec note `29-test-engine-skill.md` §Frontmatter and ROADMAP.md:43 ✓.
- Intentional deviations from verbatim copy are correctly called out: generalize "TypeScript" → compile
  error (stack-agnostic), and keep the table header as "→ test" rather than the source's "→ keep." ✓

## Critical Issues

None. No blocking defects, missing migrations, wrong paths, or security concerns. This is a
content-only skill with `allowed-tools: Read` and no I/O — no runtime/security surface.

## Observations (non-blocking)

1. **The extraction is deliberately staged — and that is correct, not a gap.** This plan authors and
   registers `test-engine` but does NOT rewire the existing consumer. Read in isolation that would create
   duplication (content living in both `test-engine` and `roadmap-test-coverage`) with zero wired
   consumers. However, ROADMAP.md resolves this: line 49 (`roadmap-test-coverage: source silent-failure
   rule from test-engine`, spec note 31) is a separate tracked milestone that refactors the source to load
   the new skill, and line 47 (`roadmap-decompose-skeleton`, depends on engine + test-engine) is the second
   consumer. This mirrors exactly how `roadmap-engine` was landed (ROADMAP.md:41, already `[x]`) — skill
   first, consumers wired in follow-up milestones. The `≥2 callers` composition gate is satisfied by the
   roadmap trajectory (test-coverage + skeleton), not by this plan alone. No action needed; noting so the
   implementer does NOT attempt to edit `roadmap-test-coverage` in this plan — that is milestone 49's job
   and doing it here would collide.

2. **CLAUDE.md tree placement.** The plan says to add the tree entry "near `roadmap-engine/`." The tree is
   loosely ordered; `test-engine/` would sit most naturally between `roadmap-prune/` and `temporal-tree/`.
   Cosmetic only — the plan's instruction is acceptable.

3. **`roadmap-decompose-skeleton` does not yet exist** on disk (confirmed). The plan's Context references it
   as a "about to be duplicated" future caller, which is accurate given ROADMAP.md:47. No impact on this
   plan's tasks.

## Positive Notes

- Line-precise sourcing with an explicit "authoritative text is the source skill, the spec note is only a
  pointer" instruction — eliminates drift risk during the copy.
- Correctly forbids dragging any pipeline/agent-orchestration/`$RESEARCH_AREAS`/stack-specific logic into
  the pure-content skill, preserving the mechanism/policy boundary.
- Registration step protects the new skill from upstream sync (`CLAUDE.md:115`) — a real, easy-to-forget
  requirement handled explicitly.
- Single-commit scope is appropriate for new-skill + registration.

The plan is solid, accurate, and well-sequenced within the roadmap.

PLAN_REVIEW_PASS
