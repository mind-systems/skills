# Code Review: roadmap-decompose slim to philosophy-only

**Milestone:** 34 — roadmap-decompose: slim to philosophy-only over the engine's flow
**Change reviewed:** `src/skills/roadmap-decompose/SKILL.md` (281 → 81 lines)
**Governing spec:** `.ai-factory/notes/44-roadmap-decompose-philosophy-slim.md`
**Also read in full:** `src/skills/roadmap-engine/SKILL.md` (the delegated flow), the plan, plan-review-1.

The only product change is `SKILL.md`; the other staged files are planning artifacts (plan, plan-reviews, plan `.json`). This is a prose-instruction refactor — the "runtime" is an agent executing the skill, so the failure modes are dropped behaviors and instructions that contradict or fail to wire into the engine's flow. I checked for both.

## Verification performed

**Frontmatter unchanged (as required).** `loads: roadmap-engine`, `allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill`, and `disable-model-invocation: true` are all intact. ✅

**Load-once discipline preserved.** Line 21–22: "Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not already loaded) and run its **Roadmap maintenance flow** with the hooks below." Section title matches the engine's actual heading (engine line 63). ✅

**Hook-to-engine wiring is one-to-one.** The engine declares four caller-supplied hooks (engine lines 71–81): (a) Granularity, (b) Per-entry gate optional, (c) Target-file routing, (d) Extra update-mode actions. Decompose supplies exactly `(a)/(b)/(c)/(d)` under matching labels, so each engine hook point is filled by the correspondingly-lettered section. No orphaned hook, no unfilled placeholder. ✅

**Behavior parity, mode by mode:**
- *Create mode* — engine holds gather-input (3-option dialog + priorities follow-up), explore, draft-in-memory with `<note pending>` placeholder, per-entry gate, confirm dialog, save. The two behaviors the engine's create flow does *not* itself carry — "mark already-completed milestones as `[x]`" and the gather-input question phrasing that fills the engine's `<caller phrases this…>` placeholder — are both explicitly re-supplied in hook (a) (lines 33–37). This closes the two parity gaps raised in plan-review-1. ✅
- *Update mode* — engine's 4-option menu (Review / Add / Reprioritize / Rewrite) plus hook (d) "Decompose existing" reconstitutes today's 5-option menu with no duplicate and no lost option. The Add action's atomicity gate is covered by the engine applying the per-entry gate hook. ✅
- *Check mode* — fully owned by the engine; decompose correctly states nothing. ✅

**Dropped critical rules are not lost — they moved to the engine.** Old decompose rules #2 (source of truth), #3 (never remove silently), #4 (`[x]` stays until prune) are mechanism-tier and are present verbatim in the engine's "Critical rules (mechanism)" (engine lines 240–243, grep-confirmed). Decompose correctly keeps only the three philosophy-tier rules (atomic/specific, two-tier always, no-implementation). ✅

**Hook (d) matches the governing spec exactly.** Note 44 enumerates what "Decompose existing" must retain: expand a vague milestone into a full spec + note-handling rule (existing `Spec:` tag → update in place; legacy inline → new note + tag; offer split on 2+ concerns; no bulk migration). Lines 60–72 transcribe all four faithfully. The old 2.5's "list open milestones / ask which to expand" procedural sub-steps are absent, but note 44 did not enumerate them among what stays — the spec's essence is "expand a vague milestone into a full spec," which is preserved — so this is within spec, not a regression. ✅

**No stale references reintroduced (notes 36/38).** Grep for `aif-plan`, `aif-implement`, `/decompose`, `note pending`, `Mode [123]`, and an inline `ROADMAP.md Format` block returns nothing. The no-implementation rule uses the post-note-36 wording ("the orchestrator implements in a separate run"). ✅

**Size.** 81 lines, inside the note's ~60–100 target. ✅

## Findings

None. The refactor is a faithful, behavior-preserving delegation: every deleted line is either mechanism now owned by the engine or a dialog the engine reproduces, and the two carry-over behaviors the engine does not hold are explicitly re-supplied through hook (a). No contradictions, no unwired hooks, no dropped user-facing behavior beyond what the governing spec authorized.

Note for the record: behavior-identical skill refactors remain formally unverified until a live `/roadmap-decompose` run (create + update + check) is compared against the pre-refactor baseline, per the repo's composition rules. That is an execution-time check outside this static review's scope and is not a defect in the change.

REVIEW_PASS
