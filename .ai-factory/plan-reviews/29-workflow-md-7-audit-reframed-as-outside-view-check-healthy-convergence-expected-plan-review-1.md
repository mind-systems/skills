## Code Review Summary

**Files Reviewed:** 1 plan (targets `docs/workflow.md`)
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap (linkage):** PASS. Plan heading matches `.ai-factory/ROADMAP.md` line 69 — the pending `[ ] workflow.md §7: audit reframed as outside-view check…` milestone. The line names `Spec: .ai-factory/notes/39-workflow-audit-reframe.md`.
- **Governing spec (`notes/39-workflow-audit-reframe.md`):** PASS. All three tasks trace directly to the spec:
  - Task 1 ↔ "Rewrite the `milestone-rescue-audit` bullet … behavior-level only, Russian, no internals."
  - Task 2 ↔ "Keep the 'сперва rescue, следом audit по тёплым артефактам' sentence … but decouple it from the 'видно, что обходит' precondition."
  - Task 3 ↔ "and the corresponding line in the ASCII scheme if needed."
  Spec's "What NOT to do" (don't touch the `milestone-rescue` bullet, don't restructure, no skill internals) is honored explicitly in Tasks 1–3.
- **Architecture (`.ai-factory/ARCHITECTURE.md`):** PASS (N/A). Docs-only edit, no module/dependency boundaries touched.
- **Rules (`.ai-factory/RULES.md`):** WARN — file not present; no explicit convention gate to apply. Global doc-style rules ("describe behavior not code", "match the language of neighboring docs") are already baked into the plan.

### Critical Issues
None.

### Verification of codebase assumptions
- **Line references are accurate.** `docs/workflow.md` currently has: line 42 = the `**milestone-rescue-audit**` bullet, line 44 = the "Обычный порядок: сперва rescue…" closing sentence, line 69 = the scheme annotation `milestone-rescue-audit   ← оркестратор обходит проблему (архитектурный сигнал)`. All match the plan's stated locations.
- **The reframe matches the real skill.** Every claim the plan wants the doc to make is grounded in `src/skills/milestone-rescue-audit/SKILL.md`:
  - Trigger = any looped (2–3 rounds at plan/implement review) or wall-clock-outlier milestone, even a passed one → skill frontmatter + Step-1/Step-5.
  - Outside-view, understanding-vs-attrition distinction → skill header ("Convergence by Understanding, or by Attrition?").
  - Healthy convergence is the expected default → Step 3 "Default is NOT band-aid" and "What NOT to do" final line ("healthy convergence is the expected result; band-aid accretion is the exception worth naming").
  - Chat-only diagnosis + one upstream recommendation, no file writes → Step 6 + `allowed-tools: Read`.
  So removing the "оркестратор … **обходит**" precondition genuinely corrects a doc that over-narrows the trigger relative to the skill.

### Minor observations (non-blocking)
- **Task 3 wording — keep it accurate, not verbose.** The old annotation is a single tight line inside an ASCII box (`← оркестратор обходит проблему (архитектурный сигнал)`). The scheme column is width-constrained; the replacement should stay a short annotation (e.g. "проверка сходимости на зациклившихся/выбивающихся вехах") rather than a full sentence, or it will break the box's visual alignment. The plan already says "Keep the scheme's layout" — just flagging that brevity is the operative constraint here.
- **Settings `Docs: no` is correct.** The artifact being edited *is* documentation, so there is no separate doc-update obligation; no missing step.
- **No migrations, no security surface, no API usage** — pure prose edit to a Russian-language doc; global rule "match the language of existing docs" is satisfied since all edits stay in Russian.

### Positive Notes
- Tightly scoped: three surgical edits, each pinned to an exact line, with explicit "don't touch the `milestone-rescue` bullet / don't restructure §7" guards that mirror the spec's negative constraints.
- Task dependencies are correct: Tasks 2 and 3 depend on Task 1's reframe landing first, since both must align to the new framing.
- Behavior-level fidelity: the plan deliberately forbids leaking skill internals (steps/discriminators) into the doc, matching both the spec and the repo's "describe behavior, not code" doc rule.

PLAN_REVIEW_PASS
