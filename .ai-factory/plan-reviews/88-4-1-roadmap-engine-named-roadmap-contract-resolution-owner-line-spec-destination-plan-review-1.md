## Code Review Summary

**Files Reviewed:** 1 plan (`plans/88-4-1-…md`) against its reference chain — spec `43-engine-named-roadmap-contract.md`, ratified design `docs/multiuser-roadmaps.md`, target `src/skills/roadmap-engine/SKILL.md`, `note/SKILL.md`, ROADMAP Phase 4 intro, `ARCHITECTURE.md` composition rule.
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** (`ARCHITECTURE.md` → "Composition: mechanism vs policy"): PASS. The named-roadmap resolution is shared mechanism used by ≥2 callers (Phase 4.2/4.3), correctly placed in the engine and kept caller-agnostic — exactly the engine role. No boundary violation.
- **Rules** (`.ai-factory/RULES.md`): absent — WARN (optional file, nothing to enforce).
- **Roadmap** (`ROADMAP.md` line 207, milestone 4.1 under "Phase 4 — Named roadmaps across the skill family"): PASS. The plan matches the contract line and the phase intro; scope boundary ("owner line written at creation… `note` untouched… defaults byte-stable") is honored. This skills repo itself has no `.ai-factory/roadmaps/` dir, so the byte-stability guard's default case is the live state — a clean regression baseline for Task 3.
- **Governing chain** (spec 43 → `docs/multiuser-roadmaps.md`): PASS. All five section items in Task 1 are verbatim-faithful to spec 43's five-item Change list; the slug worked example, owner-line semantics, test-sibling derivation, and per-subdir spec destination all match the ratified doc.

### Critical Issues
None. The plan is implementable as written:
- Section placement is correct — `## The two-tier artifact` (SKILL.md:25) and `## Roadmap File Format` (SKILL.md:46) exist and bracket the insertion point, so "target-file resolution reads before the format that renders into it" is achievable.
- Task 2's quoted anchor text is accurate: both `.ai-factory/specs/` mentions in the two-tier section (the `<NN>`-scan at SKILL.md:28–29 and the `note` destination at SKILL.md:36–37) are named, so no anchor is missed.
- The `note`-untouched assumption is verified against ground truth: `note/SKILL.md:31` and `:52–57` already scope `mkdir -p`, the `[0-9][0-9]-*.md` numbering scan, and the final path to the destination-directory hook, with numbering explicitly per-directory. `.ai-factory/specs/<slug>/` is a plain hook value — no `note` change needed, exactly as the plan claims.
- Guards are correctly propagated: no caller names in the new section (Task 1 guard + Task 3.c), defaults byte-stable (Task 3.a), no orchestrator-path wording (Task 3.e).
- `allowed-tools: Read Skill` needs no change — the engine *describes* the git-identity resolution the calling agent runs; the maintenance flow already narrates `git log …` commands without granting Bash, so the new section is consistent with that convention.

### Low — clarity gap worth closing in Task 1 item 5
The engine's contract-line tag template (SKILL.md:32) reads `` Spec: `.ai-factory/specs/<NN>-<slug>.md`. `` and, per spec 43's byte-stability guard, must stay byte-identical — Task 2 correctly leaves it untouched. But for a named roadmap the spec note lands in `.ai-factory/specs/<slug>/<NN>-<slug>.md`, so the contract line's `Spec:` tag must carry the `<slug>/` subdirectory too — the ratified doc stresses readers resolve a spec "через `Spec:`-тег … с точным путём" (exact path). In practice the caller writes the tag from `note`'s returned path, so behavior is correct; the risk is only that an implementer reading item 5 ("specs land in `.ai-factory/specs/<slug>/`") alongside the unchanged flat template at :32 could copy the flat form and drop the subdirectory. This is fixable inside the plan's own constraints — the fix belongs in the *new* section (item 5), which is unconstrained by the byte-stability guard, not in :32. Recommend Task 1 item 5 add one clause: for a named roadmap the contract line's `Spec:` tag reflects the same `<slug>/` subdirectory path `note` returns. Non-blocking.

### Positive Notes
- The plan reads the byte-stability guard precisely: it isolates the single sentence that may change (Task 2) and makes byte-stability an explicit verification step (Task 3.a) with a concrete dry-read acceptance test rather than a hand-wave.
- Dependency ordering (Task 1 → 2 → 3) is correct and each task names its file and scope tightly; Task 3 folds guard-verification into the same file with no phantom report artifact.
- Scope discipline is strong: the plan resists widening into the callers (explicitly deferred to 4.2/4.3 in the Notes block) and into `note`, matching the phase decomposition.

## Deferred observations
- Affects: Phase 4 (engine coherence, beyond 4.1's byte-stable boundary) — the new `## Named roadmaps` section and the maintenance-flow hook (c) "Target-file routing" (SKILL.md:105–106, :124–126) will both describe target-file routing while sitting in separate sections with no cross-link. They are compatible layers (hook (c): the caller routes `$TARGET_FILE`; the new section: the resolution order the caller applies), and the byte-stability guard forbids editing hook (c) here, so there is nothing to do within 4.1. Whoever revisits engine coherence after the direction lands may want a one-clause pointer from hook (c) to the resolution order — out of this milestone's scope.

_One low-severity in-scope finding recorded above (contract-line `Spec:` tag path for named roadmaps); resolve it in Task 1 item 5 before implementation. The plan is otherwise solid and ready._
