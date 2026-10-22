# 80.2 — Step 5 is mechanics

## What is true now

The skill is as 80.1 leaves it; none of that task touches the sections below.

`src/skills/task-rescue/SKILL.md`, § "Step 5 — Apply repair and roll back artifacts", opens with the deletion rule: uncommitted files are removed with git-native commands only (`git clean -f -- <path>` for an untracked file, `git rm -f -- <path>` for a staged one), committed files are never deleted, the spec file is never touched except by the deliberate repair of the task spec, and another slug's files are never deleted. It then carries a paragraph for each option Step 4 offers — "Non-convergence (terminal — no rollback)" and "Escalated" options 1, 2 and 3 — and four procedures headed "Depth:": spec, spec + plan, spec + plan + code, and plan ratified with implementation absent. Each procedure lists its repair steps, its deletions, an `Emit:` line, and, in the three that keep the sidecar, the sidecar write: locate the file by the roadmap's stem (flat under `plans/` for the default pair, under `plans/<stem>/` for a named roadmap), read it or start from `{}`, set `step`, drop `implementer` where the implementation is discarded, drop `escalation`, keep every other key, write two-space JSON. The spec + plan procedure holds the write in full, the plan-ratified one repeats it, and the spec + plan + code one refers back to "the spec+plan depth above". The full reset deletes the sidecar.

§ "Valid sidecar `step` states", under Step 5, holds the table of the orchestrator's closed set and the paragraphs that follow it: the rescue always writes attempt 1 "since both depths delete every plan-review/review file"; the bare `"planned"` and `"implemented"` forms are retired; the silent failure mode of a `step` whose artifact is missing; the test-mode replacement; a paragraph on the always-valid states with the two conditions for writing `"planned:1"` and `"implemented:1"`; a long note on which values the skill writes and that it never writes `"escalated"`, only clears it; and a closing paragraph that restates the Diagnosis Report's conclusion and confirms the rescue is complete. `orchestrator-artifacts`, § "Sidecar fields", names this skill the home of the closed set and its artifact requirements.

§ "Step 5.6 — Pin disposed observations" lists two disposal branches with their markers, a spec path and dismissed, and its scope paragraph names the depths that delete review files. `orchestrator-artifacts`, § "Status-marker grammar", holds more than the two: the fixed marker and the route onto a phase.

§ "Step 4 — Choose repair depth" offers four numbered options labelled by depth, each with a "Rollback:" line that states the rollback in full, option 2 adding "(keeping passing plan-reviews intact if wanted)", although the spec + plan procedure deletes every plan-review. The escalation options describe their rollback as the "spec-depth full reset", and a paragraph after them routes each option to a labeled procedure of Step 5.

## What must be true after

Step 5 states once how files are deleted: git-native, committed files never deleted, another slug's files never deleted. The sentence that the spec file is never touched except by the deliberate repair goes. It states once how the sidecar is written: located by the roadmap's stem as `orchestrator-artifacts` § "Layout" lays out, read or started from `{}`, `step` set, `planner`, `elapsed` and every key not named left as they are, `escalation` dropped wherever the sidecar is rewritten, two-space JSON.

It states four rollback states, each with what stays on disk and what it requires:
- **Full reset.** The plan, every plan-review, every review and the sidecar are deleted; nothing of the attempt remains. Requires nothing.
- **`planned:1`.** The plan stays; every plan-review and every review is deleted; `step` is `"planned:1"` and `implementer` is dropped. Requires the plan `.md` on disk.
- **`implemented:1`.** The plan, the passing plan-reviews and the working-tree diff stay; every review is deleted; `step` is `"implemented:1"` and `implementer` stays. Requires the plan on disk and a non-empty working diff.
- **`plan_reviewed`.** The plan and every plan-review stay; every review is deleted; `step` is `"plan_reviewed"` and `implementer` is dropped. Requires a plan-review ending with `PLAN_REVIEW_PASS` on disk for the slug.

The table of valid states stays as it stands, with the silent failure mode and the test mode beside it.

The four "Depth:" procedures go with their repair steps and their `Emit:` lines. The paragraphs keyed to Step 4's options stay and name the state they run: non-convergence changes no state; escalation option 1 repairs the task spec and contract line with the decision, then the full reset; option 2 is the full reset with the spec and contract line untouched; option 3 changes no state. The paragraph on the always-valid states, the note on which values the skill writes, the paragraph that holds the attempt-1 sentence and the retired bare forms, and the closing restatement of the Diagnosis Report go; the requirement of each state lives with the state.

§ 5.6 says a rescue pins what it disposes of this session, at the moment it does, in `orchestrator-artifacts`' status-marker grammar and by that pointer; it names no marker. The scope paragraph keeps its sentences except the parenthetical that names the depths, which goes. The closing paragraph, that a rescue disposes only of what it evaluated and leaves the rest unmarked for the resolution session, stays.

Step 4's menu stays. Its four options keep their labels, and each "Rollback:" line names its state — full reset, `planned:1`, `implemented:1`, `plan_reviewed` — with the detail only in Step 5. The parenthetical on keeping passing plan-reviews goes from option 2. The escalation options say "the full reset" where they said "spec-depth full reset", and the paragraph that routes the options to Step 5 names the states in place of the procedures.

## What breaks on contact

**Rule:** a text breaks on this change if it points at a "Depth:" procedure that no longer exists, or restates a rollback's contents outside Step 5's states.

**Sweep:**
```
grep -n -E "Depth:|spec-depth|depth above|both depths|Emit:|bare|Always-valid" src/skills/task-rescue/SKILL.md
```

**Finding.** The search returns the headings of the four procedures and their `Emit:` lines; the escalation options, the routing paragraph and the closing of Step 4; the escalation paragraphs of Step 5; the sentences after the table of states; and § 5.6's scope paragraph. Each is a target above. The "Rollback:" lines of the menu and the offering condition of option 4 stay and still point at a state that exists. `orchestrator-artifacts` § "Sidecar fields" and the table's own note that it mirrors the orchestrator's accepted set stay true; the orchestrator's docs describe a rescue by its concept and need no change.
