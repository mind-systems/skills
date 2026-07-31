## Code Review Summary

**Scope:** documentation / skill-authoring task. The changed surfaces are Claude-executed
skill instructions and a glossary, not runtime code — "correctness" here is textual
fidelity to the on-disk orchestrator protocol and internal consistency of the
instructions an agent will follow.

**Files changed (4, as scoped):**
- `docs/reserved-words.md` — § Orchestrator: Home pointer + 3 entries (`failure`, `halt`, `escalation`).
- `src/skills/orchestrator-artifacts/SKILL.md` — §2, §3, §7.
- `src/skills/task-rescue/SKILL.md` — Step 2, Step 3, Step 4, three Step-5 rollbacks, closed-set table, "What NOT to do".
- `src/skills/task-rescue-audit/SKILL.md` — one word on line 32.

**Risk Level:** 🟢 Low. No blocking findings.

### Verified against ground truth
- **Protocol tokens mirror the orchestrator byte-for-byte** (per the phase-25 spec and the
  passing plan-review, grounded in the orchestrator sibling repo): `ESCALATION` last-line
  marker, `## Escalation` section, `step: "escalated"` (terminal, unindexed, always-valid),
  `escalation` sidecar field (role · path · one-line excerpt). §7's new mirror entries
  `prompts/escalation.md` and `resume.py` match the orchestrator's own file layout and the
  section's existing bare-filename style.
- **Escalation-first ordering (Step 2)** is correct and load-bearing: an escalating
  planner/implementer writes `ESCALATION` into the *plan* file with no plan-review on disk,
  which matches Plan-phase failure's condition verbatim — the new classification is inserted
  ahead of all four existing ones and the "check this first" instruction is explicit, so the
  misclassification the task set out to fix is closed. The four existing classifications and
  their relative order are byte-identical.
- **Clear-and-reset reuses the existing spec-depth reset**, no new rollback procedure and no
  fifth depth-menu entry — the guard holds. Step 5's three key-preserving rollbacks gain only
  the one-clause defensive `escalation`-key drop; deletion/JSON mechanics are otherwise
  unchanged. The spec-depth rollback correctly gets no clause (its wholesale sidecar delete
  already clears the key).
- **Closed-set table** gains the sixth row and the "five"→"six" count is updated; the
  reference-only framing (`task-rescue` never writes `escalated`, only clears it) matches the
  treatment of `plan_review_failed:N`/`review_failed:N`. The closing note is updated to say so.
- **Diagnosis-Report discipline preserved**: the new Step 3 branch restates only the
  `## Escalation` section's domain content and sets the decision off as a block quote; it names
  no marker, field, or `step` value in user-facing text, consistent with the untouched "What
  NOT to do" mechanics line.
- **`task-rescue-audit`**: exactly one word changed ("cold rescue" → "cold audit") on line 32;
  `grep -c escalat` → 0, so the audit gained no escalation logic — the guard holds.
- **`reserved-words.md`**: the five pre-existing § Orchestrator entries are byte-identical; only
  the Home line and three appended bullets changed. `halt` and `escalation` are kept
  distinguishable by cause (halt = external; escalation = the agent's own authority boundary),
  addressing the precision risk the spec flagged.

Acceptance greps all pass: `escalat` hits confined to Step 2/3/4, the three rollbacks, the
table, and "What NOT to do" — zero in Step 1, Step 5.5, Step 5.6, or the spec-depth rollback's
own text. `git diff --stat` shows exactly the four scoped files.

## Deferred observations
- Affects: `src/skills/task-rescue/SKILL.md:235-238` (Step 4 escalation branch, option 2) — the
  summary sentence "Options 1 and 2 both **reuse the existing spec-depth full reset verbatim**
  (Step 5's 'Depth: spec' procedure)" points at the whole `Depth: spec` procedure, whose steps 1–2
  *edit the task spec + contract line* — which option 2 explicitly forbids ("Do not edit this
  task's spec"). The option-2 body already self-scopes the reset correctly ("perform the
  spec-depth full reset on THIS escalated task's transient state"), so a careful agent reconciles
  it to the deletion steps (3–4) only; the residual is that the shared "verbatim … procedure"
  pointer slightly over-claims for option 2. The plan-review pre-flagged this and suggested
  stating plainly that option 2 invokes only the deletion portion of the spec-depth procedure.
  Non-blocking clarity nit, not a functional defect — left for whoever next touches this branch. [routed → .ai-factory/specs/trickster77777/89-task-rescue-escalation-branch-polish.md]
- Affects: `docs/reserved-words.md:76` (spec-mandated wording, not the implementer's choice) — the
  new bare `failure` entry shares the stem "failure" with the pre-existing qualified test terms
  `silent failure` / `loud failure` (`:64-65`). They are disambiguated by qualifier and by
  section (Tests vs Orchestrator) and the entry is added verbatim per the task spec, so this is
  conformant; noted only so a future reader does not read it as an accidental stem collision. [dismissed]

REVIEW_PASS
</content>
