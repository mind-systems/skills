## Plan Review Summary

**Plan:** 34 — roadmap-decompose: slim to philosophy-only over the engine's flow
**Files Reviewed:** plan + `src/skills/roadmap-decompose/SKILL.md` (281 lines, current), `src/skills/roadmap-engine/SKILL.md` (247 lines), notes 36/38/43/44, ROADMAP.md line 79, plan-review-1
**Risk Level:** 🟢 Low

This is the second-round plan. Both non-blocking findings from plan-review-1 have been explicitly folded into the plan text, and the plan still maps accurately to the codebase. No blocking issues. Recommend PASS.

### Context Gates

- **Roadmap linkage** — ✅ Plan traces to ROADMAP.md line 79 (`roadmap-decompose: slim to philosophy-only over the engine's flow`), whose `Spec:` tag points at note 44 (`44-roadmap-decompose-philosophy-slim.md`), which exists and the plan Context names. Milestone → spec → plan chain intact. The plan is a faithful transcription of note 44's "what stays / what goes" split.
- **Governing dependency (note 43)** — ✅ Plan presumes note 43 landed (engine gained the maintenance flow). Confirmed: `roadmap-engine/SKILL.md` carries the "Roadmap maintenance flow" section (Step 0, mode determination, create/update/check modes, mechanism-tier critical rules, hook points a/b/c/d at lines 71–81). The plan's lead-in "run its **Roadmap maintenance flow**" matches the engine's section title (engine line 63).
- **Predecessor notes 36/38** — ✅ Plan correctly forbids reintroducing what note 36 (stale `/aif-plan`·`/aif-implement`·`/decompose` refs) and note 38 (inline roadmap-format block) removed. Task 3 greps for these leftovers.
- **ARCHITECTURE / composition rule** — ✅ `.ai-factory/ARCHITECTURE.md` present; plan honors mechanism-vs-policy (philosophy skill loads the engine, does not restate its mechanism; "Do not restate the engine's flow, dialogs, format, or mechanism-tier critical rules"). No `RULES.md`, no `skill-context/aif-review/SKILL.md`, no `ROADMAP_TESTS.md` (Testing: no) — gates skipped correctly.

### Round-1 Findings — both resolved

1. **"Mark already-completed milestones as `[x]`" on first run (was homeless).** ✅ Now explicitly allocated: Task 1 hook (a), parity carry-over (i), citing current line 97. Task 3 re-confirms it "survived … neither silently dropped." Line reference verified (decompose line 97).
2. **Engine create-mode gather-input placeholder (was unallocated phrasing).** ✅ Now explicitly allocated: Task 1 hook (a), parity carry-over (ii) — decompose supplies the wording "What tasks should I decompose into the roadmap?" (current line 63) to fill the engine's `AskUserQuestion: <caller phrases this…>` placeholder (engine line 109). Task 3 re-confirms the placeholder "is actually filled." Both line references verified (decompose line 63; engine line 109).

### Hook Coverage Cross-Check

The engine declares four caller-supplied hooks (engine lines 71–81): (a) Granularity, (b) Per-entry gate (optional), (c) Target-file routing, (d) Extra update-mode actions. The plan's four hooks map one-to-one:

- **(a) Granularity** — matches engine hook (a); plus the two parity carry-overs correctly parked here (see above).
- **(b) Atomicity Gate stated once** — matches engine hook (b), applied by the engine in both create-draft and update-add. Registering the single gate as hook (b) reproduces today's dual placement (current 1.3.1 + 2.4.1) without restating it twice.
- **(c) Target-file routing** — default `ROADMAP.md`, explicit filename wins, test keywords → `ROADMAP_TESTS.md`; faithful to current lines 34–38.
- **(d) "Decompose existing"** — matches engine hook (d); note-handling rule (existing `Spec:` tag → `Write` in place, tag unchanged; legacy inline → new note + add tag; offer split on 2+ concerns; no bulk migration) is a faithful transcription of current 2.5 (lines 198–202).

**Deletion scope is accurate:** the plan deletes Step 0, Step 1 mode boilerplate, Mode 1 (1.1–1.4 incl. 1.3.1 gate), Mode 2 sub-actions 2.1/2.2/2.3/2.4+2.4.1/2.6/2.7, and all of Mode 3 — and correctly **retains** 2.5 by re-registering it as hook (d). The 5-option Mode-2 menu is reproduced as engine's 4-option menu + hook (d).

**Critical-rules split (Task 2) is clean:** decompose's mechanism rules #2 (source-of-truth read-before-modify) / #3 (never-remove-silently) / #4 (`[x]`-stays-until-prune) already live in the engine's "Critical rules (mechanism)" (engine lines 240–243) and are dropped; philosophy rules #1 (atomic/specific) / #5 (NO implementation, post-note-36 wording) / #6 (two-tier) stay. Matches the file exactly.

### Non-blocking Observations (not defects; no action required)

1. **"entries" vs "tasks" dialog wording.** Delegating to the engine's caller-agnostic flow means user-facing dialogs now say "entries" where decompose historically said "tasks" (e.g. confirm-menu "Add more entries"). This is a cosmetic divergence from a strict reading of "behavior-identical," but it is a pre-accepted consequence of note 43's deliberate caller-agnostic engine design — not introduced by this plan, and unavoidable without violating the composition rule. No change warranted.
2. **Merged update-menu ordering.** Today "Decompose existing" sits as option 3 (between Add and Reprioritize); via engine-menu + hook (d) its position is unspecified. Trivial; the set of actions is preserved, which is what parity requires. Worth no more than the implementing agent's discretion.

### Positive Notes

- Round-1 findings were addressed by amending the plan text (explicit carry-overs + explicit Task-3 confirmations), not by hand-waving — the parity contract is now self-checking.
- Frontmatter claims are exact: `loads: roadmap-engine` (line 11), `allowed-tools` (line 10), `disable-model-invocation: true` (line 12) all present; "keep as-is" is correct.
- Task 3 bakes in a grep-for-leftovers pass (residual Mode 1/2/3 machinery, duplicated dialogs/format, stale `/aif-plan`·`/aif-implement`·`/decompose`) plus a line-count check — appropriate self-verification for a "behavior-identical" refactor, which per repo rules stays unverified until the live output is compared to the pre-refactor baseline.
- Target ~60–100 lines from a 281-line source is realistic given how much of the source is pure delegation.
- Load-once discipline is explicitly preserved (Task 1: "Preserve the load-once discipline sentence").

The plan is well-scoped, accurately mapped, and resolves the prior round's findings. Safe to implement.

PLAN_REVIEW_PASS
