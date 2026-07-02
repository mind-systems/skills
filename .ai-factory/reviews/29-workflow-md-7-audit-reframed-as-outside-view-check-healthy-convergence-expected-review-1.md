# Review: workflow.md §7 audit reframe

## Scope
Documentation-only change to `docs/workflow.md` §7 (the `milestone-rescue-audit` bullet, the ordering sentence, and the ASCII scheme annotation). No code, no config, no runtime surface — nothing to break at runtime.

## Verification against plan and spec (`.ai-factory/notes/39-workflow-audit-reframe.md`)

**Task 1 — audit bullet rewrite (line 42):** Correct.
- Trigger is now "любую веху, которая зациклилась (2–3 раунда...) или заняла аномально много времени, — даже если в итоге она прошла" — the "видно, что оркестратор... обходит" precondition is gone, so the verdict is no longer pre-judged. ✓
- Keeps the outside-view framing ("взгляд «снаружи»") and the understanding-vs-attrition distinction, with attrition defined as "заплатки вокруг одного неназванного структурного или спекового пробела". ✓
- Healthy convergence stated as the expected default; band-aid framed as the exception ("По умолчанию ожидается здоровая сходимость — заплатка это исключение... а не презумпция") — faithful to the skill's "Default is NOT band-aid". ✓
- Chat-only, one upstream recommendation, no file writes ("диагноз плюс одну рекомендацию наверх — только в чат, ничего не правит"). ✓
- Behavior-level only; no skill internals leaked. Single bullet; `milestone-rescue` bullet untouched. ✓

**Task 2 — ordering sentence (line 44):** Correct. Preserves "сперва rescue, следом audit по тёплым артефактам" and drops the "если... чувствуется «обход»" conditional gating. ✓

**Task 3 — ASCII scheme (line 69):** Correct. Annotation changed to "взгляд снаружи на зациклившуюся/аномальную веху"; column alignment and the `milestone-rescue` line preserved. ✓

## Observations (non-blocking, out of scope)
- The §7 intro (line 39) still opens with "Оркестратор упирается в лимит итераций и останавливается", which frames both tools around a halt — slightly in tension with the audit now running on milestones that passed. The bullet self-corrects ("даже если в итоге она прошла"), the plan explicitly scoped this to one bullet, and the note forbids restructuring other sentences. Not a defect; noted only for awareness.

No correctness, security, or consistency issues found.

REVIEW_PASS
