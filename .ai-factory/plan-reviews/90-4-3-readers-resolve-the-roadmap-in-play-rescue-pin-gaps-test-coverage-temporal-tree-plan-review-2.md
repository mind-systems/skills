## Code Review Summary

**Files Reviewed:** 1 plan (targets 4 skill/command files) — revision 2
**Risk Level:** 🟢 Low

Plan under review: `4.3 — readers resolve the roadmap in play`. Root recovered: `ROADMAP.md:211` (Phase 4), governing spec `.ai-factory/specs/45-readers-resolve-roadmap-in-play.md` → its own governing spec `docs/multiuser-roadmaps.md`; the resolution's one home is roadmap-engine's "Named roadmaps" section (spec 43, `roadmap-engine/SKILL.md:49`). Sibling `[x]` milestone 4.2 (spec 44 — the writers `roadmap-decompose`/`roadmap-outline`) is the ratified wiring precedent and was read as the baseline. Plan-review-1 raised three blocking findings; this pass verifies whether revision 2 resolves them.

All four edit sites re-verified against the live files: rescue `SKILL.md:177-180` (Step 4 three-branch list) + `:56-58` (Step 1 restatement) + `:33-35` (orchestrator-artifacts load-once line); pin-gaps `:13`; test-coverage `:29` (feeding `$ROADMAP_PATH` at `:31-32`); temporal-tree `:67`/`:70`. Every literal the plan names is present at the cited line.

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy") — **PASS.** Revision 2 establishes the engine-load edge (frontmatter `loads:` + a load-once body line) for all four readers, so the newly-declared dependency on roadmap-engine's resolution content is actually reachable at runtime rather than a dangling pointer.
- **Rules** (global CLAUDE.md → "Dependencies and the skill graph") — **PASS.** Every reader now declares `loads: roadmap-engine` in its own frontmatter, matching how sibling 4.2 wired the identical dependency. Commands are included in the reverse-graph grep (`src/commands/*.md`), so pin-gaps' `loads:` line is discoverable. No engine-side edit needed — roadmap-engine already carries its reverse-graph marker (loaded by decompose/outline), and adding callers does not require re-marking.
- **Roadmap** — aligned. Scope (four sites, resolution referenced-not-restated, defaults byte-stable) matches the contract line and spec 45's Change/Guards.

### Resolution of plan-review-1 findings

**Issue 1 (rescue Step 1 restatement would contradict widened Step 4) — RESOLVED.** Task 1 now carries an explicit "Step 1 reconciliation (`:56-58`)" bullet: collapse the parenthetical "(the same resolution Step 4 uses: … three literals …)" to the pure pointer "(the same resolution Step 4 determines)", and correctly leaves the `:62-64` "additive to Step 4's own resolution" sentence unchanged. Verified against ground truth: `:56-58` is exactly the restatement, `:62-64` is exactly the additive sentence — both citations accurate.

**Issue 2 (engine-load edge unaddressed; two readers cannot load the engine) — RESOLVED.** Revision 2 adds a "Dependency wiring" preamble and a per-task tool-access split:
- rescue + test-coverage already have `Skill` in `allowed-tools` (verified: rescue `:13`, test-coverage `:13`) → append `roadmap-engine` to `loads:` + load-once line.
- pin-gaps + temporal-tree have **no `Skill`** (verified: pin-gaps `:10`, temporal-tree `:10`) → add `Skill` to `allowed-tools`, add `loads: roadmap-engine`, add load-once line. The plan grounds this in the ratified milestone-1.17 precedent ("`Skill` joins `allowed-tools` wherever the body loads via the Skill tool") — verified as a real `[x]` line at `ROADMAP.md:191`, correct class match.
- The load-once wording ("Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not already loaded)…") reuses the ratified writers' core phrasing (decompose `:21-22`, outline `:16-17`) and correctly adapts the trailing clause — readers reference the resolution rather than running the maintenance flow.

**Issue 3 (temporal-tree's "my" tier questionable for repo-wide historic reconstruction) — RESOLVED in-plan, spec-faithfully.** Task 4's "Semantic caveat" bullet closes the deferred question without reopening spec 45: it honors the spec-dictated argument → my → default tier, notes the engine never infers "my" (default path stays `ROADMAP.md`, identical to today), and documents that an explicitly-named roadmap reconstructed at a historic hash may not exist there — the user's explicit choice, not a silent default. This is the correct resolution: the tier is spec-mandated, so the plan documents the semantic rather than diverging from spec 45.

### Correctness spot-checks
- **Two-dimensional rescue resolution handled correctly.** rescue's Step 4 currently composes two orthogonal axes — which-roadmap (argument/default) × test-sibling (test keyword). Task 1 widens the which-roadmap axis to argument → my → default while keeping the test-keyword axis as a composing dimension (named → `roadmaps/<slug>-tests.md`, default → `ROADMAP_TESTS.md`). This matches spec 45's rescue Change bullet exactly and the `-tests` sibling naming matches engine `:66` and the contract line.
- **temporal-tree literals.** `:70` is the full-path command `git show <first-hash>:.ai-factory/ROADMAP.md`; `:67` is the prose "read ROADMAP.md …". Task 4 covers both (command takes the resolved path, "narrative follows suit") and instructs grep-at-execution-time since the file is in flux — appropriate.
- **Referenced-never-restated guard honored.** The Dependency-wiring preamble describes slug/owner mechanics for the *planner's* context; every task instruction says "reference the engine; do not restate slug/owner mechanics" — consistent with spec 45's guard.

### Positive Notes
- All line citations are accurate against the live files, including the `:33-35`, `:56-58`, `:62-64` triangulation inside rescue.
- The tool-access split is verified per-file against actual `allowed-tools`, not assumed — and each grant is justified by a ratified precedent.
- Byte-identical guards are enumerated per file and match spec 45's guard list (rescue depth/rollback/sidecar table, coverage's 8 layers + Class A/B, pin-gaps' hole taxonomy + `## Blocking decisions`, temporal-tree's walk order + Features prefix-match).
- The "no `roadmaps/` → identical to today" invariant is stated in the task preamble and holds at all four sites, consistent with the engine's "never infers multiuser mode".
- Not touching each file's `argument-hint` is the spec-faithful choice — spec 45's Verification pins the diff to "only target-resolution wording", so leaving the illustrative hints is correct, not an omission.

All three plan-review-1 findings are resolved; the wiring the prior pass demanded is now present and precedent-grounded, and no new defect was found. The plan is implementation-ready.

PLAN_REVIEW_PASS
