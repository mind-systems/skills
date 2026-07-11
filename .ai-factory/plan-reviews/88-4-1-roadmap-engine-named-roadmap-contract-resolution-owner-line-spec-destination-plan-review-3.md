## Code Review Summary

**Files Reviewed:** 1 plan (`plans/88-4-1-…md`) against its full reference chain — spec `43-engine-named-roadmap-contract.md`, ratified design `docs/multiuser-roadmaps.md`, target `src/skills/roadmap-engine/SKILL.md`, `note/SKILL.md`, ROADMAP line 207 (Phase 4), and the two prior plan reviews.
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy"): PASS. Named-roadmap resolution is shared mechanism (≥2 callers land in 4.2/4.3), correctly placed in the engine and kept caller-agnostic — the engine role exactly. No boundary violation.
- **Rules** (`.ai-factory/RULES.md`): absent — WARN (optional file, nothing to enforce).
- **Skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): absent — WARN (no project-specific review overrides).
- **Roadmap** (`ROADMAP.md` line 207, milestone 4.1 under "Phase 4 — Named roadmaps across the skill family"): PASS. Plan matches the contract line word-for-word in scope: resolution order, slug derivation, owner-line + hard-stop, test sibling derived from the roadmap in play, per-subdir spec destination, `note` untouched, defaults byte-stable. This repo has no `.ai-factory/roadmaps/` dir (confirmed), so the byte-stable default is the live regression baseline Task 3.a checks against.
- **Governing chain** (spec 43 → `docs/multiuser-roadmaps.md`): PASS. All five Task 1 items are faithful to spec 43's five-item Change list; the slug worked example, owner-line semantics, test-sibling rule, and the per-subdirectory spec destination all match the ratified doc (`.ai-factory/roadmaps/<имя>-tests.md`, `.ai-factory/specs/<имя>/`, "точный путь" tag resolution).

### Prior findings — both resolved
- **Review-1 (low):** contract-line `Spec:` tag must carry `<slug>/` for named roadmaps. Closed — Task 1 item 5 now adds the explicit clause (tag reflects the exact `.ai-factory/specs/<slug>/<NN>-<slug>.md` path `note` returns, lives only in the new section, flat template at line 32 stays byte-identical). Correct fix, placed where the byte-stability guard leaves room.
- **Review-2 (medium):** Task 2 described two physically separate edit sites as "this sentence" (singular) and prescribed a merged sentence. Closed — Task 2 now states the flat destination is hardcoded in "**two physically separate clauses, in different paragraphs eight lines apart**," that "both must gain the named-destination variant **in place**," and that they "cannot be merged into one sentence without restructuring surrounding prose, which would itself break byte-stability." Each site is quoted with its own before/after. This matches ground truth exactly.

### Critical Issues
None. The plan is implementable as written. Verified against the target file:
- **Section placement** is achievable: `## The two-tier artifact` (SKILL.md:25) and `## Roadmap File Format` (SKILL.md:46) bracket the insertion point, so "resolution reads before the format that renders into it" holds.
- **Task 2 anchor 1** — the `<NN>`-scan clause is verbatim on SKILL.md:28–29 (`` `<NN>` scanned against `.ai-factory/specs/` so it never collides ``). The quoted fragment excludes the sibling note-path token `.ai-factory/specs/<NN>-<slug>.md` on the same line, so the edit stays surgical and leaves that flat template intact — consistent with item 5 documenting the named note path only in the new section.
- **Task 2 anchor 2** — the `note`-destination clause is verbatim on SKILL.md:35–37 (`pass destination `.ai-factory/specs/` via `note`'s destination hook; per-directory numbering happens there`). The "eight lines apart" claim is accurate (36 − 28 = 8).
- **Byte-stability boundary** is honored: the contract-line tag template at :32 stays byte-identical; the plan honestly surfaces that it edits one clause beyond what spec 43's guard literally names ("only the `<NN>`-scan sentence") and justifies it — the destination clause hardcodes `.ai-factory/specs/` too, so leaving it unconditional would route a named roadmap's specs to the flat dir and contradict item 5. Sound, disclosed deviation.
- **`note`-untouched** is verified against ground truth: `note`'s `mkdir -p`, the `[0-9][0-9]-*.md` scan, and the final path already resolve to the destination-directory hook with per-directory numbering. `.ai-factory/specs/<slug>/` is a plain hook value — no `note` change, exactly as Task 1 item 5 and Task 3.b claim.
- **Guards** propagate cleanly: caller-agnostic new section (Task 1 guard + Task 3.c), no orchestrator wording (Task 3.e), a concrete `grep -n "Owner:"` contract check (Task 3.d), and a behavioral dry-read acceptance test for byte-stability (Task 3.a) rather than a hand-wave.
- **No frontmatter change needed:** the new section adds no `loads:` edge (`note` already loaded), and the engine already carries its reverse-graph marker (SKILL.md:22–23).

### Positive Notes
- Scope discipline is strong: the plan resists widening into the callers (deferred to 4.2/4.3 in the Notes block) and into `note`, matching the phase decomposition; the item-5 tag clause is confined to the unconstrained new section.
- The engine/policy split is preserved: item 1 keeps "the engine never infers multiuser mode," so the resolution recipe stays consistent with maintenance-flow hook (c) ("the caller resolves `$TARGET_FILE`").
- Dependency ordering (Task 1 → 2 → 3) is correct; Task 3 folds guard-verification into the same file with no phantom report artifact.

## Deferred observations
- Affects: Phase 4 (engine coherence, beyond 4.1's byte-stable boundary) — the new `## Named roadmaps` section and maintenance-flow hook (c) "Target-file routing" (SKILL.md:105–106, 124–126) both describe target-file routing in separate sections with no cross-link. They are compatible layers (hook (c): the caller routes `$TARGET_FILE`; the new section: the resolution order the caller applies), and the byte-stability guard forbids editing hook (c)'s existing text here. Whoever revisits engine coherence after the direction lands may want a one-clause forward pointer from the new section to hook (c) — out of this milestone's scope.

PLAN_REVIEW_PASS
