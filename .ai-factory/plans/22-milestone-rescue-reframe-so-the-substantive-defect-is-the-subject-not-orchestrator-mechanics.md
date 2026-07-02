# Plan: milestone-rescue: reframe so the substantive defect is the subject, not orchestrator mechanics

## Context
Reframe `src/skills/milestone-rescue/SKILL.md` so the first-class subject becomes the defect in the task's spec/contract and its implementation — with orchestrator mechanics (iteration limit, PASS markers) demoted to internal routing signals. Artifact discovery, depth routing, rollback, and sidecar logic stay behavior-identical.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

All tasks edit the single file `src/skills/milestone-rescue/SKILL.md`. They are surgical edits from the spec note `.ai-factory/notes/33-milestone-rescue-reframe-substantive-defect.md` — a reframe, not a rewrite. Hard guards for every task: body stays ≤ 500 lines; frontmatter (lines 1–13) unchanged; the sidecar `step` closed-set table + contract text (lines 240–259) and all `git` commands untouched; the classification logic and PASS-marker detection stay identical (only their labeling changes). Do edits in file order to avoid anchor drift.

### Phase 1: Reframe the entrypoint and routing

- [x] **Task 1: Reframe the opening paragraph**
  Files: `src/skills/milestone-rescue/SKILL.md`
  Rework the opening prose (~lines 17–21, under `# Milestone Rescue`). State in one sentence that the exhausted iteration limit is the **tripwire** — *how* the failure was noticed — then move on. Make the subject explicit: this skill diagnoses and repairs the defect in the task's specification (spec note + contract line) and its implementation. Do not dwell on the pipeline stop. Keep the existing "how deep the root cause reaches / repairs to that depth / rolls sidecar back" content that follows intact.

- [x] **Task 2: Relabel Step 2 signals as internal routing; reorder the diagnosis statement** (depends on Task 1)
  Files: `src/skills/milestone-rescue/SKILL.md`
  In Step 2 (~lines 59–83), keep the plan-phase / implement-phase / non-convergence classification logic and the PASS-marker signal detection **exactly as is**, but add explicit framing that these are an **internal routing signal** feeding the Step 4 depth choice — not the diagnosis the user receives. Rewrite the closing "State the diagnosis explicitly" line (~line 82) to lead with the substantive root cause first and place the failure phase last, as routing context only.

### Phase 2: Promote the Diagnosis Report to the centerpiece

- [x] **Task 3: Add the mandatory Diagnosis Report to Step 3** (depends on Task 2)
  Files: `src/skills/milestone-rescue/SKILL.md`
  In Step 3 (~lines 87–105), add a mandatory **Diagnosis Report** as a first-class deliverable, printed to the user *before* the Step 4 depth menu without the user asking. Specify its form precisely per the spec note:
  - **Chronological narrative in plain prose** — the story of the implementation attempt as a sequence of events: what the implementation did, what defect the review found, what the fix changed, what new defect that fix introduced — round by round, in complete sentences. One short paragraph per review round; a single-round failure may be one paragraph. Length scales with the number of rounds — never compress a multi-round chain to fit a sentence budget.
  - Weave reviewer findings from recurring rounds (2+) into the narrative as quotes/paraphrases, as evidence.
  - **No tables, no fragment-style bullet lists** inside the Diagnosis Report.
  - **Domain language only** — what the spec note / contract line stated wrongly or left ambiguous and how plan/code went wrong as a consequence. Zero orchestrator vocabulary (no iteration counts, no PASS markers, no phase names, no sidecar).
  - **Ending — a standalone root-cause sentence**: one sentence stating the missing/wrong constraint in the spec/contract, phrased so that had it been present the failure chain would not have occurred; placed last, visually set off (e.g. a block quote).
  Keep the existing root-cause categories (spec gap / scope overload / mechanical error) and recurring-issue signal, but attach them to the report as a classification rather than replacing it.

- [x] **Task 4: Rewrite the Step 4 non-convergence template to lead with substance** (depends on Task 3)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Rewrite the canned non-convergence prose in the Step 4 `AskUserQuestion` block (~lines 120–133) so it leads with substance ("the deliverable is complete and correct; remaining findings are cosmetic: <one-line summary of what they are>") and mentions the PASS mechanics in at most one clause of context. Keep the three options and Option-3 spec-note behavior functionally unchanged.

### Phase 3: Restate substance at close and add the guardrail

- [x] **Task 5: Restate the diagnosis in Step 5 before file bookkeeping** (depends on Task 4)
  Files: `src/skills/milestone-rescue/SKILL.md`
  At the Step 5 closing output (~line 261, before the deleted-files list / "Show the user the list of deleted files"), add one paragraph restating the Diagnosis Report's conclusion — what was wrong, what was repaired, at which depth — so the substantive summary comes first and file bookkeeping second. Do not alter the git-native deletion commands or the sidecar `step` table above.

- [x] **Task 6: Add the "What NOT to do" mechanics-as-problem ban** (depends on Task 5)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Append a bullet to the "What NOT to do" section (~lines 299–314): never present orchestrator mechanics — iteration limits, missing PASS markers, phase names, sidecar states — as "the problem"; they are how the failure surfaced, not what failed. Clarify this constrains *output and reporting*, not analysis — pipeline signals are still read internally to route repair depth. After this edit, verify total file line count is ≤ 500.

## Commit Plan
- **Commit 1** (after tasks 1-6): "Reframe milestone-rescue around the substantive defect instead of orchestrator mechanics"
