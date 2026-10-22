# Plan: 80.2 — Step 5 is mechanics

## Context
In `src/skills/task-rescue/SKILL.md`, § "Step 5 — Apply repair and roll back artifacts" repeats the same facts in many places. Four "Depth:" procedures each restate the deletion rule, the repair steps and an `Emit:` line, and three of them restate the sidecar write. This task rewrites Step 5 so that it states three things once: the deletion rule, the sidecar write, and four rollback states. The four states are full reset, `planned:1`, `implemented:1` and `plan_reviewed`. Each state says what stays on disk and what it requires.

The task also makes these changes:
- The table of valid states stays. The notes after it go.
- § 5.6 points to `orchestrator-artifacts` and names no marker of its own.
- In Step 4's menu, each option names its state instead of spelling out the rollback.

The task spec `.ai-factory/specs/trickster77777/0254-step-5-is-mechanics.md` is authoritative. Its § "What must be true after" states the required behaviour, but it pins no texts word for word. The after-texts below are drafts. Write them in the skill's existing register and keep the file's hard wrap at about 86 columns. The phase's governing spec is `docs/names-and-reasons-not-laws.md`.

Assumptions:
- The spec gives a breakage rule: a text breaks if it points at a "Depth:" procedure that no longer exists, or if it restates a rollback's contents outside Step 5's states. Three places outside the spec's listed targets fail that rule:
  - Step 2's stale-implementer paragraph ("the plan-ratified rollback (Step 5)").
  - Two bullets in § "What NOT to do": the sidecar-keys bullet and the `"planned:1"`/`"implemented:1"` bullet.
  - The last bullet of § "What NOT to do", which says "spec-depth full reset". The spec's own sweep grep returns this one.

  This plan repairs these with the smallest change that satisfies the rule: retarget one line, delete two bullets, and rename one term. Task 80.3 later rewrites Step 2 and removes § "What NOT to do" entirely. No other file in `skills/` or `orchestrator/` names these procedures (checked by grep).
- Step 4's option labels, its scope-overload and stale-implementer flags, its non-convergence menu, and the closing line "proceed to Step 5 with the chosen depth" stay. The options are still labelled by depth. Step 4's flags and menus are 80.3's work.
- The pointers to `orchestrator-artifacts` sections are written by heading text: `§ "1. Layout"` and `§ "6. Status-marker grammar"`. This matches the `§ "3. Sidecar fields"` pointer that 80.1 wrote in § 5.7.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit `src/skills/task-rescue/SKILL.md`

- [x] **Rewrite Step 5's body as rules and states**
  Files: `src/skills/task-rescue/SKILL.md`
  In § "Step 5 — Apply repair and roll back artifacts", replace everything from the heading down to the `### Valid sidecar \`step\` states` subheading. Keep the heading itself. Remove the following:
  - The opening paragraph and its deletion bullets.
  - The "Never touch the spec file … except the deliberate task-spec repair below" sentence.
  - The four escalation and non-convergence paragraphs.
  - All four `**Depth: …**` procedures, with their numbered steps and `Emit:` lines.

  The new body, in this order:
  1. **Opening:** one sentence saying that Step 5 applies the repair Step 4's choice names, then rolls the task back to the state that choice names.
  2. **Deleting files.** Use `git status --short -- .ai-factory/` to find uncommitted files. Delete them with git-native commands only: an untracked file (`??`) with `git clean -f -- <path>`, a staged one (`A `) with `git rm -f -- <path>`. Never delete a committed file, and never delete a file belonging to another task slug.
  3. **Writing the sidecar.** Locate the sidecar by the roadmap's stem, as `orchestrator-artifacts` § "1. Layout" lays it out, `<stem>` being the stem of `$TARGET_FILE`. Read it if present, or start from `{}` if absent. Set `step`. Leave `planner`, `elapsed` and every key the state does not name as they are. Drop `escalation` wherever the sidecar is rewritten. Write the sidecar back as JSON with two-space indentation.
  4. **Rollback states:** a short lead-in, then four bullets. Each bullet states what is deleted, what stays, the `step` and `implementer` handling, and what the state requires. All deletions are for this slug.
     - **Full reset.** The plan `.md`, every plan-review, every review and the sidecar are deleted, so nothing of the attempt remains. Requires nothing.
     - **`planned:1`.** The plan stays. Every plan-review and every review is deleted. `step` is `"planned:1"` and `implementer` is dropped. Requires the plan `.md` on disk.
     - **`implemented:1`.** The plan, the passing plan-reviews and the working-tree diff stay. Every review is deleted. `step` is `"implemented:1"` and `implementer` stays. Requires the plan on disk and a non-empty working diff.
     - **`plan_reviewed`.** The plan and every plan-review stay. Every review is deleted. `step` is `"plan_reviewed"` and `implementer` is dropped. Requires a plan-review ending with `PLAN_REVIEW_PASS` on disk for the slug.
  5. **Paragraphs keyed to Step 4's other branches.** Keep the bold labels and `---` separators in the file's current style. Each paragraph names the state it runs:
     - **Non-convergence:** no state changes for any of the three options. Every artifact and the sidecar stay as they are. Proceed to Step 5.5.
     - **Escalated, option 1:** repair the task spec and contract line with the decision, then run the full reset.
     - **Escalated, option 2:** run the full reset with the task spec and contract line untouched, because the decision belongs elsewhere.
     - **Escalated, option 3:** no state changes. Every artifact stays as the orchestrator left it. Proceed to Step 5.5.

  The repair guidance inside the old procedures goes with them, as the spec requires. That guidance covered quoting only the implicated clauses of a governing spec, and the contract-line clause style.

- [x] **Trim § "Valid sidecar `step` states" to the table** (depends on Rewrite Step 5's body as rules and states)
  Files: `src/skills/task-rescue/SKILL.md`
  Keep these unchanged: the closed-set intro paragraph (including its mirrors-the-orchestrator sentence and the named-roadmap layout sentence), the six-row table, the `**Silent failure mode:**` line and the `**Test mode:**` line.

  Delete these:
  - The paragraph "The rescue always writes **N = 1** — both depths delete …", including the sentence on the retired bare `"planned"` / `"implemented"` forms.
  - The `**Always-valid guard:**` line.
  - The whole "Note: `"plan_reviewed"` **is** written by this skill …" paragraph.
  - The closing paragraph "Restate the Diagnosis Report's conclusion … confirm the rescue is complete."

  The `---` before § "Step 5.5" stays.

- [x] **§ 5.6 pins by pointer**
  Files: `src/skills/task-rescue/SKILL.md`
  In § "Step 5.6 — Pin disposed observations":
  1. Replace the opening paragraph and both disposal bullets (`**Routed**` … `[routed → <spec path>]`, and `**Evaluated and found moot …**` … `[dismissed]`) with one paragraph. It says that a rescue pins each deferred-observation entry it disposes of this session at the moment it disposes of it, together with every sibling occurrence across that task's review files. The pin follows the grammar and dedup rule of `orchestrator-artifacts` § "6. Status-marker grammar", by that pointer. The paragraph names no marker, no bracketed literal, and no disposal branch.
  2. In the scope paragraph, delete only the parenthetical "(spec / spec+plan depth delete both genres; spec+plan+code and plan-ratified depth delete reviews, keep plan-reviews)". The sentence then reads "… Step 5 may already have deleted the rescued slug's review files, and a deleted file has nothing to pin …". Keep the "Pin at the moment of the judgment …" sentence.
  3. Leave the closing paragraph ("Rescue disposes only of what it evaluates …") unchanged.

- [x] **Step 4 names the states**
  Files: `src/skills/task-rescue/SKILL.md`
  In § "Step 4 — Choose repair depth":
  1. In the escalation menu code block, option 1: replace "then perform the existing spec-depth full reset (delete the plan, all plan-reviews, all reviews, and the sidecar) — this clears …" with "then perform the full reset — this clears …". Keep the rest of the text. The deletion list goes because it restates the state.
  2. In option 2 of the same menu: "Still perform the spec-depth full reset on THIS escalated task's …" becomes "Still perform the full reset on THIS escalated task's …".
  3. Rewrite the routing paragraph ("Each option routes to its own labeled procedure under Step 5 …") so that it names states, not procedures:
     - Each option runs a rollback state of Step 5, with no new rollback state and no fifth depth-menu entry.
     - Option 1 repairs the task spec and contract line with the decision, then runs the full reset.
     - Option 2 runs the full reset with the spec and contract line untouched.
     - Option 3 changes no state.

     The paragraph ends with "Proceed to Step 5."
  4. In the depth menu code block, keep every option's label line. Option 4 keeps its two-line label ("plan ratified, implementation absent — keep the plan and its passing plan-review(s); / the implementer session never produced a diff"). Make two changes:
     - Remove the parenthetical " (keeping passing plan-reviews intact if wanted)" from option 2's label.
     - Replace each `Rollback:` line with the state name only: `Rollback: full reset`, `Rollback: planned:1`, `Rollback: implemented:1`, `Rollback: plan_reviewed`. Option 4's rollback detail (implementer dropped, resumes at implement iteration 1 with a fresh session) goes, because it lives in Step 5.
  5. Leave the following unchanged: the paragraph after the menu ("Offer option 4 only when …"), the non-convergence branch, the scope-overload flag and the stale-implementer flag.

- [x] **Repair the remaining pointers to the removed procedures** (depends on Rewrite Step 5's body as rules and states)
  Files: `src/skills/task-rescue/SKILL.md`
  1. In § "Step 2 — Diagnose root cause and depth", in the "Stale implementer session" paragraph, replace "Repair depth is the plan-ratified rollback (Step 5), not spec/spec+plan/spec+plan+code." with "Repair depth is Step 4's plan-ratified option, rolling back to `plan_reviewed` (Step 5), not spec/spec+plan/spec+plan+code." Change nothing else in Step 2.
  2. In § "What NOT to do", make three changes:
     - Delete the bullet that opens "Do not overwrite `planner` or `elapsed` in the sidecar". Step 5's sidecar write and states now hold this.
     - Delete the bullet that opens "Do not write `"planned:1"` or `"implemented:1"` when the corresponding artifact is absent". Each state's requirement now holds this.
     - In the last bullet, replace "reuse the existing spec-depth full reset verbatim" with "reuse the full reset".

     Leave the other bullets unchanged.
  3. Verify with the spec's sweep:
     `grep -n -E "Depth:|spec-depth|depth above|both depths|Emit:|bare|Always-valid" src/skills/task-rescue/SKILL.md`
     It must return no lines. Then check that `grep -n -E "\[routed|\[dismissed" src/skills/task-rescue/SKILL.md` returns nothing from § 5.6.
