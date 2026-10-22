## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/19-80-1-the-report-is-the-chronicle.md`
**Target:** `src/skills/task-rescue/SKILL.md` (single file)
**Risk Level:** 🟢 Low. All four critical issues from plan-review 1 are fixed. One small
issue is left: the plan keeps a phrase that only made sense next to the rule it removes.

### Context Gates

- **Roadmap — OK.** `# Plan: 80.1 — The report is the chronicle` matches task 80.1 in
  `.ai-factory/roadmaps/trickster77777.md`, Phase 80 (governing spec
  `docs/names-and-reasons-not-laws.md`). I read the task spec
  `0253-the-report-is-the-chronicle.md` in full. The plan covers every clause of its
  § "What must be true after".
- **Scope — OK.** The plan leaves Step 4, § "Step 5", § 5.5, § 5.6 and the `description:`
  to 80.2 and 80.3, which matches those tasks' contract lines.
- **ARCHITECTURE / RULES — WARN (not present).** There is no `.ai-factory/RULES.md` and
  no skill-context file for `aif-review`, so neither applies.
- **Codebase assumptions re-checked against the current file:**
  - The sweep patterns (`reopened|exactly once|reads it back|Zero orch|orchestrator mech`
    and the plan's second grep) hit only the "When" paragraph, the "Which runs"
    paragraph, the printout paragraph, the Step 3 sentence, the "What NOT to do" bullet
    and the template's `## What was done`. The plan deletes every one of these. The
    plan no longer tells the implementer to mention "What was done", so it no longer
    makes its own sweep fail.
  - Item 4 now covers all three phrases in § 5.7 that place the moment of the write:
    "at this moment, here in Step 5.7", "re-resolved here" and "at this point".
  - Each branch still reaches § 5.7 without the "Which runs" paragraph. Step 5's
    non-convergence and escalation option-3 paths go "directly to Step 5.5", and
    §§ 5.5 → 5.6 → 5.7 run in order. Deleting "Which runs" therefore removes no
    routing.
  - `orchestrator-artifacts` § "3. Sidecar fields" holds `planner`, `implementer`,
    `plan-reviewer-<N>` and an `escalation` record that names the role that raised it.
    The roles and rounds in `Stopped at` and in `## Who found what` are therefore
    sourced correctly. The reviewer's round comes from the review file's number.
  - `allowed-tools` already grants `Write Edit` for the appends. `loads:` already holds
    `note`.
  - The dated `## 2026-10-21` heading exists in `rescue-reports/tradeoxy_core/0044-…`.
    This confirms the `## <YYYY-MM-DD>` assumption.

### Critical Issues

1. **The plan keeps "(already domain language by construction)", whose only job was to
   satisfy the rule this task deletes.** (Low severity, cosmetic.)
   In § "Step 3: drop the vocabulary rule and end with the first write", item 1, last
   bullet, the plan says to leave the escalation paragraph's "already domain language by
   construction" as it is. That parenthetical explains why restating the
   `## Escalation` section word for word is allowed under "Domain language only: … Zero
   orchestrator vocabulary". After this task removes that label and sentence, the
   phrase "domain language" appears nowhere else in the skill. The parenthetical then
   becomes a stale reason in a paragraph next to the edit. It also still suggests that
   the narrative is held to a domain-language rule. The new sentence says the opposite:
   the narrative may name a round and a reviewer. The spec's § "What breaks on contact"
   sets the rule: a text breaks if it implies that the narrative must avoid the
   pipeline's own words. This phrase sits next to that rule, and the fix is inside this
   task's single file.
   **Fix:** in that bullet, tell the implementer to delete the parenthetical
   "(already domain language by construction)" and leave the rest of the escalation
   paragraph unchanged.

### Positive Notes

- Each plan-review 1 finding is fixed precisely:
  - The new paragraph is headed "**Write the durable report.**" and says "the durable
    report" throughout, so it no longer collides with Step 3's "the report".
  - The ordering remark is marked as a note for the implementer, so it will not become
    skill text.
  - The append paragraph now says that a failed first write leaves nothing to append
    and that Write creates no file. This keeps the "never defer the write" rule intact.
- The template change keeps the stop and the root-cause finder on separate lines. It
  adds no second stop line, which is what the spec and phase note `0226` require.
- The plan correctly relies on the existing "title phrase" paragraph to cover the
  escalation branch's missing root cause under `Root cause found by`, without adding a
  special case.
- Every reference is by heading or quoted text. The plan cites no line numbers.

## Deferred observations

- Affects: `.ai-factory/specs/trickster77777/0255-the-answers-become-questions-and-the-rescue-pauses-on-the-report.md` — Once the first write moves to the end of Step 3, the scope-overload exit in Step 4 leaves a durable report on disk. That exit never reaches § 5.7, so no dated section records that the task was flagged and pointed to `/roadmap-decompose`. Step 4 is outside 80.1's scope. 80.3 removes that flag and has the rescue extend the report after the user's word, so that task should make sure every ending of a rescue appends its dated section. [dismissed]
