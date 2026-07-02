## Code Review Summary

**Files Reviewed:** 1 plan (`23-milestone-rescue-audit-narrative-output-register...md`) against target `src/skills/milestone-rescue-audit/SKILL.md`, spec note `34-milestone-rescue-audit-narrative-output.md`, sibling `milestone-rescue/SKILL.md`, and ROADMAP.md entry.
**Risk Level:** 🟢 Low

This is a prose-only reframe of a single `SKILL.md` — no code, no migrations, no API surface, no dependents. Verification confirms the plan is accurate and complete.

### Context Gates
- **Architecture** (`.ai-factory/ARCHITECTURE.md` present): No boundary/dependency impact. The change touches only the skill's *output register*, not its composition — no mechanism is extracted or factored, so the mechanism-vs-policy rule does not apply. `grep` confirms `milestone-rescue-audit` has **no consumers** (only self-references), so reframing its output has zero ripple. **PASS.**
- **Rules** (`.ai-factory/RULES.md`): not present → **WARN (optional file absent)**, non-blocking.
- **Roadmap** (`.ai-factory/ROADMAP.md`): Plan is directly linked to the open milestone at line 57 ("milestone-rescue-audit: narrative output register") and its spec note `34-...`. Milestone linkage is present. **PASS.**
- **Skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): not present → no project overrides to apply.

### Critical Issues
None.

### Verification Notes (all confirmed accurate)

- **Line references are exact**, not approximate:
  - Task 1 → Step 1 is lines 35–46 ✓ (table at 40–41, round-count/severity/outcome notes at 43–44)
  - Task 2 → Step 6 is lines 137–159 ✓
  - Task 3 → Step 5 is lines 118–133 ✓; the "Evidence: 2–3 bullet points" item is at 128–129 ✓
  - Task 4 → band-aid/mixed numbered items 3–6 at 146–156, cost note at 158–159 ✓
  - Task 5 → "What NOT to do" is lines 163–172 ✓
- **Assumption about milestone-rescue's Diagnosis Report is correct.** `milestone-rescue/SKILL.md:115–125` defines exactly the target register the plan mirrors — "chronological narrative in plain prose," "one short paragraph per review round," "length scales with the number of rounds — never compress," "No tables, no fragment-style bullet lists." The plan's wording in Tasks 2–5 faithfully matches this precedent.
- **Plan maps 1:1 to spec note `34`'s five edits.** Task 1↔edit 1, Task 2↔edit 2, Task 3↔edit 3, Task 4↔edit 4, Task 5↔edit 5 + guard verification. No spec requirement is dropped.
- **Behavior-preservation guard is explicit and correct.** Task 5 requires the analysis logic (Step 3 one-sentence-test decisive, Step 4 discriminators corroborative-only, "Default is NOT band-aid," healthy-convergence early exit), frontmatter, chat-only contract, and ≤500-line budget to remain unchanged — matching spec Constraints. Since the current file is 173 lines and this is a reframe (not an expansion), the 500-line ceiling is comfortably safe.
- **Full Step 6 coverage across tasks.** The existing Step 6 "Always include / When band-aid / Always end with" numbered structure is fully re-homed: base narrative (Task 2), verdict-at-end (Task 3), band-aid extras 3–6 (Task 4), and the closing cost note (Task 4). Nothing in Step 6 is left unaddressed.

### Minor Observation (non-blocking — WARN)

There is a mild wording tension the implementer should reconcile, inherited directly from the spec note:
- Task 3 states the narrative **"ends with the verdict."**
- Task 4 states the band-aid/mixed extras (root-cause block quote → reframe paragraph → upstream recommendation → cost note) **follow the verdict**.

So for a band-aid/mixed verdict, the verdict is not literally the last line. The intended reading is clear — the verdict is the *culmination of the narrative proper*, and the band-aid payoff material is an appendix that follows it. This matches the sibling skill's shape and the spec note (edit 3 + edit 4). Recommend the implementer phrase Step 6 so the two are obviously compatible (e.g. "the narrative culminates in the verdict; when band-aid/mixed, the root-cause payoff and recommendation follow"), to avoid a future reader seeing a contradiction.

### Positive Notes
- Task dependencies are correctly ordered (2 depends on 1; 3 and 4 depend on 2; 5 depends on 1–4).
- Each task pins concrete line ranges and states precisely what must *not* change — well-scoped, low-ambiguity, implementation-ready.
- Settings (Testing: no, Docs: no) are appropriate for a prose-only skill edit with no runtime surface and no doc-generation obligation.
- The plan repeatedly and explicitly guards the analysis pipeline as word-for-word invariant, which is the single highest-risk failure mode for this kind of reframe — and it is handled well.

PLAN_REVIEW_PASS
