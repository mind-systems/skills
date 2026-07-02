## Plan Review Summary

**Plan:** 34 — roadmap-decompose: slim to philosophy-only over the engine's flow
**Files Reviewed:** plan + `src/skills/roadmap-decompose/SKILL.md` (281 lines, current), `src/skills/roadmap-engine/SKILL.md`, notes 36/38/43/44, ROADMAP.md line 79
**Risk Level:** 🟢 Low

The plan is well-scoped and accurately mapped to the codebase. File paths, note references, frontmatter claims, and the hook-to-engine mapping all check out. Two minor behavior-parity gaps are worth closing inside Task 1/Task 3 before implementing; neither is blocking.

### Context Gates

- **Roadmap linkage** — ✅ Plan traces to ROADMAP.md line 79 (`roadmap-decompose: slim to philosophy-only…`), whose `Spec:` tag points at note 44, which the plan Context paragraph names. Milestone → spec → plan chain is intact.
- **Governing dependency (note 43)** — ✅ The plan presumes note 43 landed (engine gained the maintenance flow). Confirmed: `roadmap-engine/SKILL.md` already contains the "Roadmap maintenance flow" section (Step 0, mode determination, create/update/check modes, mechanism-tier critical rules, and the caller-supplied hook points a/b/c/d). The plan's lead-in text "run its **Roadmap maintenance flow**" matches the engine's actual section title (line 63). No missing dependency.
- **Predecessor notes 36/38** — ✅ Plan correctly instructs not to reintroduce what note 36 (stale `/aif-plan`·`/aif-implement`·`/decompose` refs) and note 38 (inline roadmap-format block) removed.
- **ARCHITECTURE / RULES** — `.ai-factory/ARCHITECTURE.md` present; the plan honors the mechanism-vs-policy composition rule (philosophy skill loads the engine, does not restate its mechanism). No `RULES.md` (skip). No `skill-context/aif-review/SKILL.md` (skip). No `ROADMAP_TESTS.md` — irrelevant here since Testing: no.

### Hook Coverage Cross-Check (Task 3's core claim)

The engine declares four caller-supplied hook points (engine lines 71–81): (a) Granularity, (b) Per-entry gate optional, (c) Target-file routing, (d) Extra update-mode actions. The plan's four hooks (a/b/c/d in Task 1) map one-to-one and correctly. Deletion scope is accurate: the plan deletes Step 0, Step 1 mode boilerplate, Mode 1 (1.1–1.4 incl. 1.3.1 gate), Mode 2 sub-actions 2.1/2.2/2.3/2.4+2.4.1/2.6/2.7, and all of Mode 3 — and correctly **retains** 2.5 (Decompose existing) by re-registering it as hook (d). Critical-rules split (Task 2) is clean: mechanism rules #2/#3/#4 already live in the engine's "Critical rules (mechanism)"; philosophy rules #1/#5/#6 stay. Matches the file exactly.

### Findings (non-blocking — fold into Task 1/Task 3)

1. **Create-mode "mark already-completed milestones as `[x]`" has no home.** Current decompose Mode 1.3 (line 97) instructs "Mark already-completed milestones as `[x]`." The engine's Create-mode flow (engine lines 133–137) does **not** carry this behavior, and none of hooks a/b/c/d covers it. If Task 1 deletes Mode 1 verbatim and adds only the four hooks, this first-run behavior is silently dropped — contradicting the "behavior-identical in every mode" contract. **Recommendation:** either keep it as one line of decompose's granularity philosophy (hook a), or have Task 3 explicitly confirm the drop is acceptable rather than assume parity.

2. **Engine's create-mode gather-input dialog expects caller-supplied phrasing that the plan doesn't allocate.** The engine's Create-mode dialog is a fill-in placeholder: `AskUserQuestion: <caller phrases this for its own granularity>` (engine line 109). Today decompose asks "What tasks should I decompose into the roadmap?" (line 63). Hook (a) as written in the plan supplies granularity *philosophy*, not the question *text*. For strict behavior-parity, Task 1 should explicitly note that decompose supplies the create-mode question phrasing (via hook a), so the engine's placeholder is actually filled. Cheap to add; worth naming so the implementing agent doesn't leave the placeholder unfilled.

### Positive Notes

- Frontmatter claim is exact: `loads: roadmap-engine` (line 11), `allowed-tools` (line 10), and `disable-model-invocation: true` (line 12) are all present as the plan states — "keep as-is" is correct, nothing to change.
- The merged update menu is correctly reasoned: engine's 4-option menu + hook (d) "Decompose existing" reproduces today's 5-option menu (Review / Add / Decompose existing / Reprioritize / Rewrite). No option lost.
- Hook (d)'s note-handling rule (existing `Spec:` tag → `Write` in place, tag unchanged; legacy inline → new note + add tag; offer split on 2+ concerns; no bulk migration) is a faithful transcription of current 2.5 (lines 198–202).
- Task 3 bakes in a grep-for-leftovers pass (residual Mode 1/2/3, duplicated dialogs/format, stale `/aif-plan`·`/aif-implement`·`/decompose`) and a line-count check — good self-verification for a "behavior-identical" refactor, which per repo rules stays unverified until output is compared to baseline.
- Target ~60–100 lines from a 281-line source is realistic given how much is pure delegation.

The two findings are refinements to the parity check, not defects in the plan's structure. Address them within the existing Task 1/Task 3 wording before implementing.
