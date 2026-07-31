# task-rescue gains an escalation clear-and-reset path; orchestrator-artifacts, reserved-words.md, and task-rescue-audit absorb the rest

Source handoff: `.ai-factory/handoffs/05-escalation-outcome-and-a-skill-that-ran-from-inside-the-pipeline.md`. The orchestrator now emits a third run outcome, escalation; three skills-side surfaces that describe or depend on its on-disk protocol read incomplete against it, and a fourth one-word residue rides along. This task closes all four: `orchestrator-artifacts` (the protocol description), `task-rescue` (the only skill-side reader/writer of the affected sidecar state), `reserved-words.md` § Orchestrator (no run-outcome vocabulary today), and `task-rescue-audit:32` (a terminology leftover unrelated to escalation).

**One atomic task**, not several: the first three edits are one fact — the orchestrator now emits a third outcome — reaching each surface, and none is useful alone (`task-rescue` citing a vocabulary `reserved-words.md` lacks is as broken as `orchestrator-artifacts` describing a protocol `task-rescue`'s table contradicts). The fourth (`task-rescue-audit:32`) is folded in by explicit instruction — one word, a file already open.

## The protocol to mirror (the on-disk contract)

Escalation is a third run outcome — not a failure (no verdict on the work) and not a halt (its cause is the agent's own authority boundary, not an external resource). Its home is the orchestrator's governing spec (`orchestrator/docs/concepts/outcomes.md`, `orchestrator/docs/features/escalation.md`, `orchestrator/docs/features/resume.md`). The skills side mirrors these on-disk tokens byte-for-byte:

- **`ESCALATION`** — an agent writes this exact word on the last line of the artifact it already produces (the plan file for the planner and implementer; the plan-review or review file for the two reviewers) to stop the run — the opposite of a PASS signal.
- **`## Escalation`** — the section immediately above the marker, stating the missing decision and its options in plain prose; the agent never picks one.
- **sidecar `step: "escalated"`** — terminal and unindexed (no `:N`); a resumed run stops again immediately rather than retrying, until the state is cleared.
- **sidecar field `escalation`** — the escalation record: the role that raised it, the artifact path, and a one-line excerpt of the missing decision.

**`src/skills/orchestrator-artifacts/SKILL.md`** — current text does not name escalation anywhere (`grep -c escalat` → 0):
- §2 "Signals" (`:34-38`) names only `PLAN_REVIEW_PASS`/`REVIEW_PASS`/`TEST_PASS`.
- §3 "Sidecar fields" (`:40-44`) lists `planner`, `implementer`, `step`, `elapsed` only; no `escalation` field.
- §7 "Mirrors-the-orchestrator invariant" (`:79-83`) enumerates a fixed set of orchestrator files this doc mirrors — the orchestrator's escalation prompt engine and its resume-detection module are now equally load-bearing sources for the content this task adds and are missing from that enumeration.

**`src/skills/task-rescue/SKILL.md`** — gaps, all verified against the live file (`grep -c escalat` → 0 before this task):
- **Step 2** (`:74-107`) is a closed set of four classifications — Plan-phase failure (`:82`, keyed on "no plan-review file contains `PLAN_REVIEW_PASS`"), Implement-phase failure (`:86`), Stale implementer session (`:90-95`), Non-convergence (`:97-102`) — none recognizes `ESCALATION`. A planner/implementer escalation writes `ESCALATION` into the **plan file itself**, with **no plan-review file on disk at all** — so such a task matches Plan-phase failure's condition verbatim today and would misclassify.
- **Step 3** (`:111-172`) offers only the full chronological Diagnosis Report narrative (`:143-151`) or, for stale-implementer-session, a short plain-statement form (`:156-159`). No branch exists for escalation.
- **Step 4** (`:176-254`) presents the four-option depth menu (`:231-250`) for every classification except non-convergence (its own `AskUserQuestion` block, `:190-210`) and scope-overload/stale-implementer-session, which explicitly skip it (`:216-219`, `:221-225`). No branch exists for escalation, and — critically — a bare "skip the menu and report" would leave the task **permanently wedged**: the run re-halts immediately on every resume of a `step:"escalated"` sidecar, and nothing clears that state automatically. Clearing it is this skill's job, the same way it already clears every other terminal sidecar state on repair.
- **Step 5**'s three key-preserving rollback depths — spec+plan (`:296-311`), spec+plan+code (`:315-327`), plan-ratified (`:331-348`) — each reads the existing sidecar and states which keys to preserve/drop (`planner`/`elapsed` preserved; `implementer` dropped at two of the three), with no mention of an `escalation` key (it didn't exist when these were written). The spec-depth rollback (`:280-292`) deletes the sidecar wholesale — this already clears any `escalation`/`step:"escalated"` state for free, which is exactly what the escalation clear-and-reset path (this task) reuses.
- The closed-set table (`:352-381`) mirrors the orchestrator's accepted `step` values and states so explicitly (`:354-357`, "if the orchestrator's accepted set changes, update this table") — it has 5 rows; the closed set the orchestrator accepts now includes `escalated`.

**`src/skills/task-rescue-audit/SKILL.md`** — zero mentions of escalation (`grep -c escalat` → 0); user-ruled out of scope for escalation-awareness — see Guards. Separately, and unrelated to escalation: line `:32` reads "If run cold, locate and read them before Step 1: cold rescue takes an optional slug naming the task as `$1`..." — this describes **this skill's own** cold-invocation mode (its `argument-hint: "[task-slug]"`), but names it "cold rescue," borrowing the sibling skill's name, a leftover from the era before rescue and audit were separated. The line immediately above it (`:31`, "If run cold...") already uses the correct self-referential phrasing.

**`docs/reserved-words.md` § Orchestrator** (`:67-75`) — five entries (`orchestrator`, `sidecar`, `PASS signal`, `deferred observations`, `prune · rescue · audit`); none of `failure`, `halt`, `escalation` exists. Confirmed: `grep -n "halt" docs/reserved-words.md docs/using-the-language.md src/skills/*/SKILL.md` → zero hits anywhere in the repo — there is no pre-existing registry entry either of the new terms could clash with. The precision risk is prospective, not remedial: `outcomes.md:9` and `escalation.md:9` both describe their outcome as carrying "no verdict about the work," so a careless pair of new entries could read as synonyms unless the entries state the distinguishing cause explicitly (halt: external; escalation: the agent's own recognized authority boundary).

## The change

**1. `src/skills/orchestrator-artifacts/SKILL.md`**
- §2 "Signals" (`:34-38`): add a sentence naming `ESCALATION` as a third signal shape, opposite in meaning to the PASS signals (stop the run, not continue it), written by any of the four roles into the artifact it already owns (plan file for planner/implementer; plan-review/review file for the two reviewers).
- §3 "Sidecar fields" (`:40-44`): add `escalation` (the escalation record: role, artifact path, one-line excerpt) to the field list; note that `step`'s closed set — still delegated to `task-rescue` — now includes `escalated`.
- §7 (`:79-83`): add the escalation prompt engine and the resume-detection module to the enumerated mirrored files (named by the orchestrator's own file layout at edit time — this doc's existing §7 already enumerates by bare filename, no line numbers).

**2. `src/skills/task-rescue/SKILL.md`**

- **Step 2**: add a new classification, ordered **before** Plan-phase failure and Implement-phase failure (not after, unlike the existing bottom-up reading order) — condition: the sidecar's `step` reads `"escalated"`, or (sidecar absent/stale) the plan file or the most recent plan-review/review file ends with the exact line `ESCALATION`. Label: "Escalated (terminal, human decision pending) — not a specification, plan, or code defect; [role] stopped because its output could not be produced honestly without a decision outside its authority. Repair depth does not apply in the usual sense — see Step 4's own escalation branch."

- **Step 3**: add a short-form branch, parallel to stale-implementer-session's (`:156-159`): "For an escalation classification, the narrative has no defect chain to tell: state plainly that [role] stopped on a decision outside its authority, then restate — verbatim or lightly paraphrased — the missing decision and its options from the artifact's `## Escalation` section (already domain language by construction). End with that decision sentence set off as a block quote, in place of the root-cause sentence — there is no root cause here, only a decision still to make."

- **Step 4 — the escalation branch (clear-and-reset, not report-only).** On an Escalated classification: skip the standard four-depth menu (nothing is broken to repair at plan/code level), present the missing decision surfaced in Step 3, then present via `AskUserQuestion`:

  ```
  This task escalated — <one-line restatement of the missing decision>.

  Escalation is not a defect at any repair depth; it stops here because a decision
  outside any agent's authority is required before this task can proceed.

  Options:
  1. Decision recorded in this task's spec — reset and re-plan
     Apply the resolved decision to this task's spec + contract line (the normal
     spec repair), then perform the existing spec-depth full reset (delete the
     plan, all plan-reviews, all reviews, and the sidecar) — this clears
     step:"escalated" and the escalation field for free, and the orchestrator
     re-plans clean.
  2. Decision belongs elsewhere (a neighboring task / the governing spec) —
     point there and reset
     Do not edit this task's spec. Report where the decision belongs (the same
     flag-and-point pattern already used for scope overload). Still perform the
     spec-depth full reset on THIS escalated task's transient state, so it
     re-plans fresh once the owning artifact is resolved.
  3. Not resolved yet — report only, leave the escalated state
     No reset. The escalated sidecar stays exactly as the orchestrator left it;
     the user re-runs this rescue after the decision is made.
  ```

  Pin explicitly, in the skill body: the full reset in options 1 and 2 **is** the existing spec-depth cleanup procedure (`:280-292`) — do not introduce a new rollback procedure or a fifth depth-menu entry; the only new thing is the routing decision (which of the three options) and, for option 2, the pointer report instead of an in-place spec edit. Option 3 performs no file changes at all.

- **Step 5**: keep the defensive "also delete the `escalation` key if present" clause at each of the three key-preserving rollback procedures (spec+plan `:296-311`, spec+plan+code `:315-327`, plan-ratified `:331-348`) — belt-and-suspenders for a stray `escalation` field reached by a **non**-escalation rescue on the same sidecar (e.g., a task that escalated once, was left at option 3, and is later rescued via a different classification entirely). The spec-depth rollback needs no separate clause — it is the same wholesale sidecar delete the escalation branch's options 1/2 already reuse.

- **Closed-set table** (`:352-381`): add a sixth row — `| "escalated" | re-halts immediately, no retry (until cleared) | none — always valid |` — marked reference-only, matching the existing treatment of `"plan_review_failed:N"`/`"review_failed:N"`: `task-rescue` never **writes** this value itself (only the orchestrator writes it, at the moment of detection, before any rescue ever runs); `task-rescue` only **clears** it, via the spec-depth full reset (options 1/2 above) or the defensive key-drop at the other three depths. Update the table's closing note to state this explicitly.

- **"What NOT to do"**: add one line: "Do not let the Plan-phase/Implement-phase conditions fire before checking for an escalation — an escalating planner/implementer writes `ESCALATION` into the plan file itself, with no plan-review file at all, which otherwise matches Plan-phase failure's condition and reports a defect chain that never existed." Add a second line: "Do not invent a new rollback procedure or a fifth depth-menu entry for escalation — options 1 and 2 of the escalation branch reuse the existing spec-depth full reset verbatim."

**3. `docs/reserved-words.md` § Orchestrator** (`:67-75`): add three entries, together, worded to keep halt and escalation distinguishable per the precision risk noted above, with a home pointer to the orchestrator's own governing spec so the registry indexes the names rather than re-homing their definitions:

```
Home — `orchestrator-artifacts`, [skill-cycle](sakshi-harness/skill-cycle.md), `orchestrator/docs/concepts/outcomes.md`.

- **orchestrator** — the CLI that executes a finished roadmap task by task; it plans nothing.
- **sidecar** — a task run's status file.
- **PASS signal** — `PLAN_REVIEW_PASS` / `REVIEW_PASS`, a stage's pass marker.
- **deferred observations** — review remarks left unresolved; unpinned ones block a prune. The heading a program scans, `## Deferred observations`, is a protocol token.
- **prune · rescue · audit** — operations: fold `[x]` tasks into Features; repair a task that did not converge to the depth of its root cause; an outside-view look at a task that looped.
- **failure** — a review cycle exhausted its attempt budget without a PASS signal; a verdict about the work.
- **halt** — the run stops for a cause outside the review cycle (a resource, an infrastructure fault, an operator); not a judgment about the work.
- **escalation** — an agent stops the run before its budget is spent because its mandated output cannot honestly be produced without a decision outside its authority; also carries no verdict about the work, but the cause is the agent's own recognized boundary, never an external one — the distinction from halt.
```

Only the `Home` line and the three new bullets change; the five existing bullets stay byte-identical.

**4. `src/skills/task-rescue-audit/SKILL.md:32`** — one-word terminology fix, unrelated to escalation: "cold rescue" → "cold audit," so the sentence describes this skill's own cold-invocation mode in its own name, matching line `:31`'s already-correct self-referential phrasing immediately above it. No other word on the line changes. No escalation-awareness, no exclusion clause, no new section — this file gains nothing else.

## Files & types

- edit: `src/skills/orchestrator-artifacts/SKILL.md` — §2, §3, §7 only.
- edit: `src/skills/task-rescue/SKILL.md` — Step 2, Step 3, Step 4 (new escalation branch with its `AskUserQuestion`), three of Step 5's four rollback procedures (defensive clause only, unchanged mechanics otherwise), the closed-set table, "What NOT to do."
- edit: `docs/reserved-words.md` — § Orchestrator only: the `Home` line and three new entries appended after the existing five.
- edit: `src/skills/task-rescue-audit/SKILL.md` — line `:32` only, one word ("rescue" → "audit" in "cold rescue").

## Guards

- **`task-rescue-audit/SKILL.md` gets exactly one word changed, nothing else.** No escalation-awareness, no exclusion clause, no new section. User ruling stands: the audit diagnoses convergence-by-attrition (spaghetti/band-aid patterns), not rescue outcomes; an escalated task did not loop, and the skill's own scope boundary against `task-rescue`'s rescue flow already excludes it structurally (it reads raw artifacts, never task-rescue's output, and works cold by design) — that boundary needs no restatement or reinforcement here.
- **No new repair-depth flow, no fifth depth-menu entry.** Escalation's clear-and-reset **is** the existing spec-depth full reset, invoked from a new routing decision inside Step 4's escalation branch — not a new Step 5 procedure. The three existing key-preserving rollback depths gain only the one-clause defensive `escalation`-key drop; their file-deletion and JSON read/write mechanics stay byte-identical otherwise.
- **Zero orchestrator vocabulary survives into the Diagnosis Report's own text** — the new Step 3 branch restates only the `## Escalation` section's content; it must never name the marker, the sidecar field, or `step: "escalated"` in what the user reads, per the existing "What NOT to do" line (`:473-476`), itself untouched.
- **Step 2's other four classifications, their conditions, and their relative order among themselves stay byte-identical** — only the new escalation check is inserted ahead of all of them.
- **Step 3's full narrative form for Plan-phase/Implement-phase failures, and the existing stale-implementer-session short form, stay byte-identical.**
- **The four existing table rows, and the guard/note prose below the table not naming `escalated`, stay byte-identical** apart from the one new row and the closing-note addition.
- **`orchestrator-artifacts` §§1, 4, 5, 6 stay untouched** — only §2, §3, §7 are in scope.
- **`reserved-words.md`'s five pre-existing § Orchestrator entries stay byte-identical** — only the `Home` line gains the third pointer and three new bullets are appended.
- **Preserve task-rescue's discipline that the Diagnosis Report names the substantive reason, never orchestrator mechanics — per its own "What NOT to do" section.** Preserve register in every other file too — targeted insertions in each skill's established voice (`orchestrator-artifacts`'s terse protocol-reference register; `reserved-words.md`'s glossary-entry form), not a rewrite of any file.

## Verification

- `grep -n "ESCALATION\|escalat" src/skills/orchestrator-artifacts/SKILL.md` → hits in §2, §3, §7 only.
- `grep -n "escalat" src/skills/task-rescue/SKILL.md` → hits in Step 2, Step 3, Step 4 (including the new `AskUserQuestion` block), the three rollback procedures, the closed-set table, and "What NOT to do"; zero hits in Step 1, Step 5.5, Step 5.6, or the spec-depth rollback procedure's own text beyond it being referenced (not duplicated) from Step 4.
- Manual read: Step 4's escalation branch presents three `AskUserQuestion` options (resolve-and-reset / point-elsewhere-and-reset / not-yet-report-only), not a bare report-and-stop.
- Manual read: options 1 and 2 both explicitly invoke the existing spec-depth full reset by reference — no new deletion/JSON-write procedure appears anywhere in the diff.
- `grep -n "cold rescue" src/skills/task-rescue-audit/SKILL.md` → zero hits; `grep -n "cold audit" src/skills/task-rescue-audit/SKILL.md` → one hit.
- `grep -c "escalat" src/skills/task-rescue-audit/SKILL.md` → `0` (still untouched beyond the one-word fix).
- `grep -n "failure\|halt\|escalation" docs/reserved-words.md` → three new entries present under § Orchestrator, with the `Home` line carrying three pointers; none elsewhere in the file.
- `git diff --stat` shows exactly four files changed: `src/skills/orchestrator-artifacts/SKILL.md`, `src/skills/task-rescue/SKILL.md`, `docs/reserved-words.md`, `src/skills/task-rescue-audit/SKILL.md`.
