## Code Review Summary

**Files Reviewed:** 1 plan (`49-orchestrator-artifacts-engine…md`) against spec `05-orchestrator-artifacts-engine.md`, `milestone-rescue/SKILL.md`, `note/SKILL.md`, `roadmap-engine/SKILL.md`, `CLAUDE.md`, `ROADMAP.md`, `active/skills/`, and sibling specs `03`/`04`.
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy"):** PASS. The plan creates a pure **engine** (mechanism/protocol only, no procedure/policy) with ≥2 eventual callers — exactly the extraction criterion. The reverse-graph marker (declarative, inline grep, no caller list) and one-way `loads:` edge match the ratified convention. No violation.
- **Rules / CLAUDE.md:** PASS. Frontmatter shape (`user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`, no `loads:` on a leaf engine) matches `roadmap-engine`. Adding the skill name to the *inventory* line 62 is not name-based routing (the "no skill names in project files" rule targets routing sections, not the active-set inventory). Symlink relative-target form (`../../src/skills/orchestrator-artifacts`) matches every sibling under `active/skills/`. The "no upstream counterpart → never synced" placement is correct; the plan rightly touches no reconcile list.
- **Roadmap:** PASS. Plan heading matches ROADMAP.md line 109; the milestone sits in a flat `- [ ]` list with **no phase header and no `Governing spec:`**, so that gate is inapplicable. Downstream ordering is sound: the prune-gate (line 111) and audit two-mode (line 113) milestones both depend on this engine and follow it.

### Verification of codebase assumptions
All concrete claims in the plan check out against the tree:
- CLAUDE.md active-set paragraph **is** line 62, and the "plus one upstream original" clause exists to insert before. ✓
- `note/SKILL.md` lines 21–23 **do** carry the load-once + reverse-graph-marker idiom the plan cites as the template. ✓
- Sibling `active/skills/*` symlinks all use `../../src/skills/<name>`; `ln -sfn` form is correct. ✓
- `milestone-rescue/SKILL.md` has no `loads:` field today (clean add) and its `### Valid sidecar step states` table + Step 5 rollbacks + Step 3 Diagnosis Report register are the byte-identical-preserve targets the plan names. ✓
- The four artifact dirs, `<seq>-<slug>` naming, `test-runs/`, sidecar fields (`planner`/`implementer`/`step`/`elapsed`), and PASS signals in the engine spec all match what `milestone-rescue` currently encodes inline. ✓

### Task decomposition
The three tasks map 1:1 to spec Edits 1–3, with correct dependencies: Task 2 (rewire) and Task 3 (activate/register) both depend on Task 1 (engine exists) and are independent of each other. No missing step, no missing migration (this is a pure skills-repo change; there is no data/schema migration surface). The "keep procedure verbatim, drop descriptive prose" boundary in Task 2 is inherently a judgment call for the implementer, but it is scoped identically to spec Edit 2 and bounded by the explicit byte-identical-preserve list — acceptable.

### Critical Issues
None.

### Positive Notes
- Clean engine/policy split honored: the plan explicitly keeps discovery/repair/audit choreography with callers and the sidecar `step` table (single consumer) in `milestone-rescue` — no accidental policy leak into the engine.
- The reverse-graph marker is specified correctly as inline-grep-only (never a caller list), and the "born with edges but only one wired here" nuance is handled — the grep will simply resolve the single `milestone-rescue` edge until specs 03/04 land their own.
- The mirrors-the-orchestrator coupling (item 7) is declared as a two-sided invariant, matching the house rule for cross-file contracts grep can't derive.

## Deferred observations
- Affects: `.ai-factory/specs/05-orchestrator-artifacts-engine.md` (and the roadmap line 109) — The provenance clause "moved from spec `03`, substance verbatim — do not paraphrase differently from spec 03's wording" (Task 1 item 6, transcribed faithfully from spec 05 item 6 / its "What NOT to do") points at a source that no longer holds the text: spec `03-prune-harvest-deferred-observations.md` was already reduced to a *reference* ("the marker grammar … live in the orchestrator-artifacts engine (spec 05)", line 10). The authoritative grammar wording now lives only in spec 05 item 6 (and spec 04). This does not impede implementation — the plan inlines the full grammar verbatim and instructs "Follow spec 05 Edit 1 exactly," so the produced engine text is unambiguous — but the dangling "match spec 03's wording" pointer should be retargeted to spec 05 as the grammar's home. The plan faithfully implements a ratified spec; the imprecision originates in spec 05, which this milestone has no authority to rewrite.
- Affects: milestone `milestone-rescue-audit: two modes` (spec `.ai-factory/specs/04-audit-reads-deferred-observations.md`) — This milestone slims `milestone-rescue`'s inline layout description into an engine reference, while `milestone-rescue-audit`'s Inputs still says "see `milestone-rescue` for layout." That pointer is repointed onto the engine by spec 04's own task (roadmap line 113), which is outside this milestone's file boundary (it touches only the engine, `milestone-rescue`, `active/`, and `CLAUDE.md`). In the interim window the audit's pointer resolves to a `milestone-rescue` that references the engine rather than holding the layout inline — the information stays reachable one hop further, so nothing is stranded. Flagged only so the spec-04 milestone confirms the repoint and does not assume the inline layout still exists.
- Affects: `.ai-factory/specs/05-orchestrator-artifacts-engine.md` item 3 — The engine describes `step` with "the only writer" = `milestone-rescue`. Strictly, the orchestrator (`orchestrator/main.py`) also writes `step` (`plan_review_failed:N`, `review_failed:N`), as `milestone-rescue`'s own table note records; `milestone-rescue` is the only *skill-side* writer. The phrasing is inherited verbatim from the ratified spec and is harmless in context (the engine mirrors the orchestrator as an external system), but a one-word tightening ("the only skill that writes it") would prevent a future reader misreading it as sole authority.

PLAN_REVIEW_PASS
