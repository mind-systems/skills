## Code Review Summary

**Files Reviewed:** 1 plan (`plans/88-4-1-…md`) against its reference chain — spec `43-engine-named-roadmap-contract.md`, ratified design `docs/multiuser-roadmaps.md`, target `src/skills/roadmap-engine/SKILL.md`, `note/SKILL.md`, ROADMAP line 207 (Phase 4), and prior review `…-plan-review-1.md`.
**Risk Level:** 🟡 Medium

### Context Gates
- **Architecture** (`ARCHITECTURE.md` → "Composition: mechanism vs policy"): PASS. Named-roadmap resolution is shared mechanism (≥2 callers in 4.2/4.3), correctly placed in the engine and kept caller-agnostic. No boundary violation.
- **Rules** (`.ai-factory/RULES.md`): absent — WARN (optional file, nothing to enforce).
- **Roadmap** (`ROADMAP.md` line 207, milestone 4.1 under "Phase 4 — Named roadmaps across the skill family"): PASS. Plan matches the contract line and phase intent; scope boundary (owner line at creation, `note` untouched, defaults byte-stable) honored. This repo has no `.ai-factory/roadmaps/`, so the byte-stable default is the live regression baseline for Task 3.
- **Governing chain** (spec 43 → `docs/multiuser-roadmaps.md`): PASS. All five Task 1 items are verbatim-faithful to spec 43's five-item Change list; slug worked example, owner-line semantics, test-sibling derivation, and per-subdir spec destination match the ratified doc.

**Review-1 finding resolved:** The prior low finding (contract-line `Spec:` tag must carry `<slug>/` for named roadmaps) is now closed — Task 1 item 5 adds the explicit clause (tag reflects `.ai-factory/specs/<slug>/<NN>-<slug>.md`, lives only in the new section, flat template at line 32 left byte-identical). Correct fix, placed exactly where the byte-stability guard leaves room.

### Critical Issues
None that block correctness. One in-scope clarity finding below should be tightened before implementation, since it touches the byte-stability-sensitive edit that is the crux of this milestone.

### Findings

**1. Task 2 describes two physically separate edit sites as "this sentence" (singular) and prescribes one merged sentence — the file cannot hold it as one.**
`src/skills/roadmap-engine/SKILL.md` carries the two `.ai-factory/specs/` references Task 2 must vary in **different paragraphs** of `## The two-tier artifact`:
- the `<NN>`-scan clause at lines 28–29 (`` `<NN>` scanned against `.ai-factory/specs/` so it never collides ``), and
- the `note`-destination clause at lines 36–37 (`pass destination `.ai-factory/specs/` via `note`'s destination hook; per-directory numbering happens there`).

Task 2 quotes both fragments (good) but then says "so it **reads**: the destination is `.ai-factory/specs/` … or `.ai-factory/specs/<slug>/` … and `<NN>` is scanned against whichever destination is in play" and "Keep the change minimal — only **this sentence** gains the named-destination variant." The two fragments are eight lines and two paragraphs apart; they cannot become one sentence without restructuring surrounding prose — which would itself break the byte-stability guard. An implementer following "only this sentence" literally risks editing one site and leaving the other pinned to the flat `.ai-factory/specs/`.

Why it matters for correctness, not just style: if line 36–37 stays unconditional ("pass destination `.ai-factory/specs/`"), it contradicts Task 1 item 5 (named → `<slug>/`) and would route a named roadmap's specs to the flat dir. Both sites genuinely must gain the variant.

Fix (inside the plan): reword Task 2 to state there are **two independent edit sites** in `## The two-tier artifact` — the `<NN>`-scan clause (28–29) and the `note`-destination clause (36–37) — each gaining the named-destination variant **in place**, not merged. This also aligns the plan with the spec guard's wording ("the `<NN>`-scan sentence gaining the named-destination variant"), which names only one sentence; the plan should note that correctness requires the destination clause to gain the same variant, since both hardcode `.ai-factory/specs/`.

### Positive Notes
- The `note`-untouched assumption is verified against ground truth: `note/SKILL.md:31`, `:52–57`, `:117` scope the `mkdir -p`, `[0-9][0-9]-*.md` scan, and final path to the destination hook, with numbering explicitly per-directory. `.ai-factory/specs/<slug>/` is a plain hook value — no `note` change, exactly as the plan claims.
- Section placement is achievable and correct: `## The two-tier artifact` (line 25) and `## Roadmap File Format` (line 46) bracket the insertion point, so "resolution reads before the format that renders into it" holds.
- Guards are propagated precisely: caller-agnostic new section (Task 1 guard + Task 3.c), no orchestrator wording (Task 3.e), `grep -n "Owner:"` contract check (Task 3.d), and a concrete behavioral dry-read acceptance test for byte-stability (Task 3.a) rather than a hand-wave.
- Scope discipline is strong: the plan resists widening into the callers (deferred to 4.2/4.3 in Notes) and into `note`, and the item-5 tag clause is confined to the unconstrained new section.
- The engine/policy split is preserved: item 1 keeps "the engine never infers multiuser mode," so the new resolution recipe stays consistent with maintenance-flow hook (c) ("the caller resolves `$TARGET_FILE`").

## Deferred observations
- Affects: Phase 4 (engine coherence, beyond 4.1's byte-stable boundary) — the new `## Named roadmaps` section and maintenance-flow hook (c) "Target-file routing" (SKILL.md:105–106, 124–126) both describe target-file routing in separate sections with no cross-link. They are compatible layers (hook (c): the caller routes `$TARGET_FILE`; new section: the resolution order the caller applies), and the byte-stability guard forbids editing hook (c) here. Whoever revisits engine coherence after the direction lands may want a one-clause pointer from hook (c) to the resolution order — out of this milestone's scope. [routed → .ai-factory/specs/57-wording-tightenings-observation-pass.md]
