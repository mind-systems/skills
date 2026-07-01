# Code Review: roadmap-engine — shared two-tier artifact-output engine

**Plan:** `.ai-factory/plans/16-roadmap-engine-new-skill-shared-two-tier-artifact-output-engine.md`
**Changes reviewed:** `git diff HEAD` + `git status`
**Files in scope for this milestone:**
- `src/skills/roadmap-engine/SKILL.md` (new)
- `CLAUDE.md` (modified — registration)

(`.ai-factory/ROADMAP.md`, `plans/*`, `plan-reviews/*` are orchestrator bookkeeping, not code under review.)

---

## Nature of the change

This is a **content/instruction-only change** — a new Agent Skill (agent runtime instructions) plus two registration edits. There is no executable application code, no schema/migration, no types, and no I/O logic that runs outside the agent. "Runtime" correctness here means: valid frontmatter, non-contradictory instructions, accurate cross-references, and fidelity to the source text that was lifted.

---

## Verification performed

- **Frontmatter is valid and the skill actually loads.** `name: roadmap-engine` matches the directory name. `user-invocable: false` + `disable-model-invocation: false` is a valid combination (matches `aif-note`/`roadmap-test-coverage` convention) — it makes the engine a non-slash-command that callers invoke via the Skill tool. Confirmed live: the harness now lists `roadmap-engine` as an available skill, proving the YAML parses and the skill is discoverable. ✅
- **`allowed-tools: Read Write Edit Glob Grep Skill` is sufficient and needs no `Bash`.** Note-number scanning uses `Glob`; note + roadmap writes use `Write`/`Edit`; the aif-note load uses `Skill`. The `Write` tool auto-creates parent directories, so the `mkdir -p .ai-factory/notes` step embedded in aif-note's template is not needed by the engine and its absence causes no failure (and `.ai-factory/notes/` already exists). ✅
- **Content is a faithful, verbatim lift of the source.** The Per-Task Render Procedure reproduces `roadmap-decompose/SKILL.md` "Two-Tier Output" steps 3–5 (aif-note load-once → write note → write contract line), correctly renumbered and re-targeted to "the target roadmap file the caller named." The "Roadmap File Format" section (skeleton + "Rules for writing a contract line") is copied byte-faithfully from decompose lines 302–323. ✅
- **Policy/mechanism boundary is correct.** The excluded items (mode determination, exploration, `AskUserQuestion`, Atomicity Gate, skeleton lenses, silent-failure rule, main-vs-test target selection) exactly match spec note 28's exclusion list and the plan. The render procedure correctly begins *after* draft-spec + gate — those stay in the caller. No policy leaked into the engine. ✅
- **Input-contract scope note is present and accurate.** The SKILL.md explicitly states note *creation only* and defers in-place note update (decompose Mode 2.5) to spec note 30 — matching the plan's Task 1 item 2 revision. ✅
- **"Copy, don't delete" guard was respected.** `roadmap-decompose/SKILL.md` is **not** in the change set (`git diff --name-only` → 0 hits) and still contains its "Roadmap File Format" section (`grep` → 1 hit). The intentional temporary duplication exists exactly as the plan prescribed; decompose is not broken. ✅
- **CLAUDE.md registration is correct and complete (both required edits).** `roadmap-engine/` added to the Repository Structure tree with a descriptive comment; `roadmap-engine` added to the "Custom skills — never overwrite from upstream" list (line 115). The alphabetical-ish insertion position (after `roadmap-decompose`) is sensible. No unrelated lists touched. ✅
- **Body length well within the ≤500-line limit** (107 lines). All paths are relative. All content in English. ✅

---

## Findings

No bugs, security issues, or correctness problems.

### Informational (non-blocking, cosmetic — no action required)

1. **Redundant sentence in render step 2.** `SKILL.md:49–53` says "determine `<NN>` by scanning existing files in `.ai-factory/notes/`" and then, one clause later, repeats "Determine `<NN>` by scanning so it never collides." The second sentence is redundant with the first. This is pure editorial duplication in agent instructions — it produces no incorrect behavior (both say the same thing: scan for the next free number). Optional tidy-up on a future touch; not worth a re-implementation cycle.

2. **Description advertises consumers not yet wired up.** The `description` names `roadmap-decompose-skeleton` and `aif-roadmap` as invokers, though neither routes through the engine yet (future milestones 30/32; skeleton doesn't exist yet). This is intentional and acceptable for an incrementally-built family — the plan-review already accepted it. No change needed.

---

## Conclusion

The implementation matches the plan exactly: a content-only engine that owns render mechanism, holds no policy, correctly registers in both CLAUDE.md locations, and leaves `roadmap-decompose` untouched (intentional temporary duplication). Frontmatter parses and the skill loads live. The only observations are cosmetic and non-blocking. No bug, security, or correctness issues found.

REVIEW_PASS
