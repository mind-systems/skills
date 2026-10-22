## Code Review Summary

**Files Reviewed:** 1 (`src/skills/task-rescue/SKILL.md`; the staged plan, plan-review and sidecar are pipeline artifacts)
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture — OK.** The edit stays inside one skill. `task-rescue` still loads `orchestrator-artifacts` and now points at it by heading text: `§ "1. Layout"` for locating the sidecar, and `§ "6. Status-marker grammar"` for pinning. It does not restate the engine's grammar, so the boundary between the engine and its caller is tighter than before. The `orchestrator-artifacts` § "3. Sidecar fields" claim, that `task-rescue` is home to the closed set and its artifact requirements, still holds: the table stays, and each requirement now sits with its state.
- **Rules — OK.** There is no `.ai-factory/RULES.md`. The edit follows the global rules:
  - Sections are cited by name, not by position.
  - Comments do not cite the plan layer.
  - It is written in present tense, with no change history.
- **Roadmap — OK.** The edit matches task 80.2 in `.ai-factory/roadmaps/trickster77777.md` (Phase 80, governing spec `docs/names-and-reasons-not-laws.md`). It also matches the task spec `.ai-factory/specs/trickster77777/0254-step-5-is-mechanics.md` § "What must be true after". Each item in that section was checked against the result:
  - **Deletion rule:** stated once. It is git-native, never deletes a committed file, and never deletes a file of another slug. The "never touch the spec file" sentence is gone.
  - **Sidecar write:** stated once. It locates the sidecar by stem via `§ "1. Layout"`, reads it or starts from `{}`, and sets `step`. It leaves `planner`, `elapsed` and every key the state does not name, drops `escalation` wherever the sidecar is rewritten, and writes two-space JSON.
  - **Four rollback states:** each one's on-disk effect, `step`/`implementer` handling and requirement match the spec's bullets word for word in substance.
  - **Valid-states section:** the table, the silent failure mode line and the test mode line stay. The N = 1 / bare-forms paragraph, the always-valid guard, the "Note:" paragraph and the closing Diagnosis-Report restatement are gone.
  - **Option paragraphs:** the four "Depth:" procedures and every `Emit:` line are gone. The non-convergence paragraph and the escalation option paragraphs each name their state, as the spec dictates.
  - **§ 5.6:** names no marker and points at the engine. The scope paragraph lost only its depth parenthetical. The closing paragraph is unchanged.
  - **Step 4:** labels are kept. Each `Rollback:` line names its state, and option 2's plan-review parenthetical is gone. The escalation options say "the full reset", and the routing paragraph names states.
- **Plan conformance — OK.** The plan has no `DEVIATION` annotations, and the diff carries out each plan task as written. That includes the three extra repairs the plan's Assumptions justify under the spec's own breakage rule:
  - the Step 2 stale-implementer pointer;
  - the two deleted § "What NOT to do" bullets;
  - "the full reset" in the last bullet of § "What NOT to do".
- **Sweep.** `grep -n -E "Depth:|spec-depth|depth above|both depths|Emit:|bare|Always-valid|\[routed|\[dismissed" src/skills/task-rescue/SKILL.md` returns nothing. Grep finds no other file in `skills/` or `orchestrator/` that names the removed procedures.

### Critical Issues

None.

These dependents of the rewritten text were checked and still read correctly:
- Step 1's "Step 5 deletes or rewrites the sidecar at some repair depths".
- § 5.7's "the depth chosen, the escalation option taken, or the non-convergence choice made".
- The table intro's "Step 5 picks one of the six values".
- The escalation menu's "this clears step:"escalated" … for free". The full reset deletes the sidecar, so this remains accurate.

Keeping `plan-reviewer-<N>` keys on the `planned:1` state follows the spec's "every key not named left as they are". It causes no harm, because the orchestrator rewrites `plan-reviewer-1` at the next attempt.

### Positive Notes

- Step 5 is now a single statement of mechanics, with three rules and four states. The duplicated sidecar procedure appeared in three copies with slightly different wording, and that source of drift is gone.
- Each state's requirement sits with the state itself. Before, it sat in a separate "always-valid guard" and a "Note:" paragraph that disagreed in scope ("both depths" against four rollbacks).
- § 5.6 cites the engine by heading text and stops copying two of its markers. The copy had already fallen behind the engine's grammar, which also has `[fixed]` and phase routing.
- The wrap width and register match the surrounding file.

## Deferred observations

- Affects: `.ai-factory/specs/trickster77777/0255-the-answers-become-questions-and-the-rescue-pauses-on-the-report.md` — § "What is true now" of the 80.3 spec still lists two § "What NOT to do" bullets that this task removed: the bullet on the `planner`/`elapsed`/`implementer` sidecar keys, and the guards on writing `planned:1`/`implemented:1`. 80.3 removes the whole section, so its outcome is unaffected. Its description of the present, though, is now two bullets out of date for whoever plans it.

REVIEW_PASS
