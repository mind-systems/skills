# Plan: workflow.md §7: audit reframed as outside-view check, healthy convergence expected

## Context
Reframe the `milestone-rescue-audit` bullet in `docs/workflow.md` §7 so it reads as an outside-view check of any looped/outlier milestone (even a passed one) with healthy convergence as the expected outcome — not a band-aid-suspected trigger.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Reframe the audit bullet

- [x] **Task 1: Rewrite the `milestone-rescue-audit` bullet in §7**
  Files: `docs/workflow.md`
  Rewrite the second bullet under §7 (currently line 42, the one starting `**milestone-rescue-audit**`). In the doc's existing Russian style and at behavior level only (no skill internals — no steps/discriminators):
  - Trigger is **any** milestone that looped (2–3 раунда на ревью плана или имплементации) or took an outlier amount of wall-clock — even one that ultimately passed (зелёная галочка). Remove the current "когда по ходу разбора видно, что оркестратор проблему не решает, а **обходит**" precondition — it pre-judges the verdict.
  - It looks "снаружи" and distinguishes сходимость-через-понимание from сходимость-через-измор (band-aid accretion around one unnamed structural/spec gap).
  - Healthy convergence is the **expected** outcome; band-aid is the exception worth naming ("Default is NOT band-aid" reflected in the doc's own words).
  - Emits a diagnosis plus one upstream recommendation to chat only — ничего не правит, no file writes.
  Keep it to a single bullet; do not restructure §7 or touch the `milestone-rescue` bullet above it.

- [x] **Task 2: Decouple the ordering sentence from the "обход" precondition** (depends on Task 1)
  Files: `docs/workflow.md`
  Rework the closing sentence of §7 (currently line 44, "Обычный порядок: сперва rescue, а если по тёплым артефактам чувствуется «обход» — следом audit, пока контекст не остыл."). Preserve the correct ordering claim — сперва rescue, следом audit по тёплым артефактам — but drop the "если чувствуется «обход»" conditional so the audit is no longer gated on suspecting a band-aid.

- [x] **Task 3: Align the ASCII scheme line with the reframe** (depends on Task 1)
  Files: `docs/workflow.md`
  Update the scheme block (currently line 69: `milestone-rescue-audit   ← оркестратор обходит проблему (архитектурный сигнал)`) so its annotation matches the new framing — an outside-view convergence check on looped/outlier milestones rather than "оркестратор обходит проблему". Keep the scheme's layout and the `milestone-rescue` line untouched; edit only this one annotation.
