# Plan: 25.1 — task-rescue gains an escalation branch; orchestrator-artifacts, reserved-words.md, and task-rescue-audit absorb the rest

## Context
The orchestrator now emits a third run outcome — escalation (an agent stops on a decision outside its authority). This task mirrors that on-disk protocol into the skills-side surfaces that predate it: `orchestrator-artifacts` (protocol description), `task-rescue` (only skill-side reader/writer of the affected sidecar state — gains recognition, a short-form report, and a clear-and-reset path reusing the existing spec-depth reset), `reserved-words.md` § Orchestrator (run-outcome vocabulary), plus one unrelated one-word audit-wording fix in `task-rescue-audit`.

## Settings
- Testing: no
- Logging: none
- Docs: no

## Tasks

### Phase 1: Protocol reference and vocabulary (the shared tokens the other edits cite)

- [x] **Task 1: `orchestrator-artifacts` — name escalation in §2, §3, §7**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  Three targeted insertions in the file's terse protocol-reference register; §§1, 4, 5, 6 stay untouched.
  - §2 "Signals" (`:34-38`): add a sentence naming `ESCALATION` as a third signal shape, opposite in meaning to the PASS signals (it *stops* the run rather than continuing it), written by any of the four roles onto the last line of the artifact it already owns — the plan file for the planner/implementer, the plan-review/review file for the two reviewers.
  - §3 "Sidecar fields" (`:40-44`): add `escalation` to the field list (the escalation record: the role that raised it, the artifact path, a one-line excerpt of the missing decision); note that `step`'s closed set — still delegated to `task-rescue` — now includes `escalated`.
  - §7 "Mirrors-the-orchestrator invariant" (`:79-83`): add the orchestrator's escalation prompt engine and its resume-detection module to the enumerated mirrored files, named by the orchestrator's own file layout, matching §7's existing bare-filename style (no line numbers). Ground the names against `orchestrator/docs/features/escalation.md` and `orchestrator/docs/features/resume.md` (per the task spec's home pointers) at edit time — read them to name the actual files.

- [x] **Task 2: `reserved-words.md` § Orchestrator — three run-outcome entries + Home pointer**
  Files: `docs/reserved-words.md`
  In § Orchestrator (`:67-75`), change only the `Home` line and append three bullets after the five existing ones; the five pre-existing entries stay byte-identical.
  - `Home` line: add the third pointer `orchestrator/docs/concepts/outcomes.md` so it reads `Home — `orchestrator-artifacts`, [skill-cycle](sakshi-harness/skill-cycle.md), `orchestrator/docs/concepts/outcomes.md`.`
  - Append `failure`, `halt`, `escalation` exactly as worded in the task spec (§3), keeping halt and escalation distinguishable by cause: halt = external (resource/infra/operator), escalation = the agent's own recognized authority boundary. Glossary-entry register only; the registry indexes the names, it does not re-home the definitions.

### Phase 2: task-rescue escalation branch (depends on Task 1)

- [x] **Task 3: `task-rescue` Step 2 — add the Escalated classification ahead of the failure conditions**
  Files: `src/skills/task-rescue/SKILL.md`
  Insert a new classification **before** Plan-phase failure (`:82`) and Implement-phase failure (`:86`) — ahead of all four existing classifications, whose text and relative order stay byte-identical.
  - Condition: the sidecar's `step` reads `"escalated"`, OR (sidecar absent/stale) the plan file or the most recent plan-review/review file ends with the exact line `ESCALATION`.
  - Label per the task spec (§2, Step 2 bullet): "Escalated (terminal, human decision pending) — not a specification, plan, or code defect; [role] stopped because its output could not be produced honestly without a decision outside its authority. Repair depth does not apply in the usual sense — see Step 4's own escalation branch."
  - This check must fire first so an escalating planner/implementer (which writes `ESCALATION` into the plan file with no plan-review file on disk) is not misclassified as Plan-phase failure.

- [x] **Task 4: `task-rescue` Step 3 — add the escalation short-form report branch** (depends on Task 3)
  Files: `src/skills/task-rescue/SKILL.md`
  Add a short-form branch parallel to the stale-implementer-session form (`:156-159`), per the task spec (§2, Step 3 bullet): for an escalation classification there is no defect chain to narrate — state plainly that [role] stopped on a decision outside its authority, then restate (verbatim or lightly paraphrased) the missing decision and its options from the artifact's `## Escalation` section. End with that decision set off as a block quote, in place of the root-cause sentence (there is no root cause, only a decision to make). The full-narrative form for Plan-phase/Implement-phase failures and the existing stale-implementer-session short form stay byte-identical. Preserve the discipline that the report names substantive/domain content only — never the `ESCALATION` marker, the `escalation` field, or `step: "escalated"` in what the user reads (per the untouched "What NOT to do" line `:473-476`).

- [x] **Task 5: `task-rescue` Step 4 — add the escalation clear-and-reset branch with its `AskUserQuestion`** (depends on Task 3)
  Files: `src/skills/task-rescue/SKILL.md`
  Add an escalation branch to Step 4 (`:176-254`). On an Escalated classification: skip the standard four-depth menu (nothing is broken to repair at plan/code level), present the missing decision surfaced in Step 3, then present the three-option `AskUserQuestion` block quoted verbatim in the task spec (§2, Step 4):
  1. Decision recorded in this task's spec — apply the resolved decision to spec + contract line (the normal spec repair), then perform the **existing spec-depth full reset** (`:280-292` — delete plan, all plan-reviews, all reviews, and the sidecar), which clears `step:"escalated"` and the `escalation` field for free.
  2. Decision belongs elsewhere (neighboring task / governing spec) — do NOT edit this task's spec; report where the decision belongs (the same flag-and-point pattern used for scope overload, `:216-219`); still perform the spec-depth full reset on THIS task's transient state.
  3. Not resolved yet — report only, no reset, no file changes; the escalated sidecar stays as the orchestrator left it.
  - Pin explicitly in the body: options 1 and 2 reuse the existing spec-depth cleanup procedure verbatim — do NOT introduce a new rollback procedure or a fifth depth-menu entry. The only new thing is the routing decision (which option) and, for option 2, the pointer report instead of an in-place spec edit.

- [x] **Task 6: `task-rescue` Step 5 — defensive `escalation`-key drop at the three key-preserving rollbacks** (depends on Task 3)
  Files: `src/skills/task-rescue/SKILL.md`
  At each of the three key-preserving rollback procedures — spec+plan (`:296-311`), spec+plan+code (`:315-327`), plan-ratified (`:331-348`) — add a one-clause defensive "also delete the `escalation` key if present" instruction (belt-and-suspenders for a stray `escalation` field reached by a non-escalation rescue on the same sidecar). Their file-deletion and JSON read/update/write mechanics stay byte-identical otherwise. The spec-depth rollback (`:280-292`) needs no clause — its wholesale sidecar delete already clears any `escalation`/`step:"escalated"` state.

- [x] **Task 7: `task-rescue` closed-set table + "What NOT to do" — add the `escalated` row and two guards** (depends on Task 3)
  Files: `src/skills/task-rescue/SKILL.md`
  - Closed-set table (`:352-381`): add a sixth row `| "escalated" | re-halts immediately, no retry (until cleared) | none — always valid |`, marked reference-only exactly like `"plan_review_failed:N"`/`"review_failed:N"` — `task-rescue` never *writes* this value (only the orchestrator writes it, at detection, before any rescue runs); it only *clears* it via the spec-depth full reset or the defensive key-drop. Update the table's closing note (`:376-381`) to state this explicitly. The four existing rows and the surrounding guard/note prose not naming `escalated` stay byte-identical apart from the one new row and the note addition. (Note: the "five values" wording at `:354` becomes six — update that count.)
  - "What NOT to do" (`:449-481`): add one line — do not let the Plan-phase/Implement-phase conditions fire before checking for escalation (an escalating planner/implementer writes `ESCALATION` into the plan file with no plan-review file, otherwise matching Plan-phase failure's condition and reporting a defect chain that never existed). Add a second line — do not invent a new rollback procedure or a fifth depth-menu entry for escalation; options 1 and 2 reuse the existing spec-depth full reset verbatim.

### Phase 3: Unrelated one-word audit fix

- [x] **Task 8: `task-rescue-audit:32` — "cold rescue" → "cold audit"**
  Files: `src/skills/task-rescue-audit/SKILL.md`
  On line `:32`, change the single word "rescue" to "audit" in "cold rescue takes an optional slug…" so the sentence names this skill's own cold-invocation mode, matching the already-correct self-referential phrasing on line `:31`. No other word on the line changes; no escalation-awareness, no exclusion clause, no new section — the file gains nothing else.

## Verification (from the task spec)
- `grep -n "ESCALATION\|escalat" src/skills/orchestrator-artifacts/SKILL.md` → hits in §2, §3, §7 only.
- `grep -n "escalat" src/skills/task-rescue/SKILL.md` → hits in Step 2, Step 3, Step 4 (incl. the new `AskUserQuestion` block), the three rollback procedures, the closed-set table, and "What NOT to do"; zero hits in Step 1, Step 5.5, Step 5.6, or the spec-depth rollback's own text.
- Manual read: Step 4's escalation branch presents three `AskUserQuestion` options (resolve-and-reset / point-elsewhere-and-reset / not-yet-report-only), not a bare report-and-stop; options 1 and 2 invoke the existing spec-depth full reset by reference — no new deletion/JSON-write procedure anywhere in the diff.
- `grep -n "cold rescue" src/skills/task-rescue-audit/SKILL.md` → 0; `grep -n "cold audit" …` → 1; `grep -c "escalat" src/skills/task-rescue-audit/SKILL.md` → 0.
- `grep -n "failure\|halt\|escalation" docs/reserved-words.md` → three new § Orchestrator entries with the `Home` line carrying three pointers; none elsewhere.
- `git diff --stat` shows exactly four files: `src/skills/orchestrator-artifacts/SKILL.md`, `src/skills/task-rescue/SKILL.md`, `docs/reserved-words.md`, `src/skills/task-rescue-audit/SKILL.md`.
</content>
</invoke>
