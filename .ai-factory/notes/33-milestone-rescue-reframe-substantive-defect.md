# milestone-rescue: make the substantive defect first-class; demote orchestrator mechanics to routing signals

**Date:** 2026-07-02
**Source:** conversation context

## Key Findings

- `src/skills/milestone-rescue/SKILL.md` is built around the **operational event** (the orchestrator hit its iteration limit; no `PLAN_REVIEW_PASS`/`REVIEW_PASS` emitted) as its load-bearing axis. The **substantive root cause** — what the spec note / contract line stated wrongly or left underspecified, and how that failed to materialize in code — exists only instrumentally, to pick a rollback depth.
- Effect: after the skill runs, the agent's context is saturated with pipeline vocabulary. Asked "what was the problem," the agent answers in orchestrator terms (iteration limits, PASS markers). The orchestrator's mechanics are the **trigger**, never the answer — the user wrote the orchestrator and knows how it works.
- Fix is a **reframe, not a rewrite**: the artifact-discovery, depth-routing, rollback, and sidecar logic are correct and must stay behavior-identical. Only the framing and the user-facing output change — the substantive defect becomes the first-class subject; pipeline signals become internal routing inputs.

## Details

Six targeted edits to `src/skills/milestone-rescue/SKILL.md` (line anchors approximate — locate by content):

1. **Opening paragraph (~lines 17–21).** Reframe: the pipeline stop is *how the failure was noticed*, not *the failure*. The subject of this skill is the defect in the task's specification (spec note + contract line) and its implementation. State in one sentence that the iteration limit is the tripwire, then move on — do not dwell on it.

2. **Step 2.** Keep the classification logic (plan-phase / implement-phase / non-convergence via PASS-marker signals) exactly as is, but explicitly label it an **internal routing signal** that feeds the depth choice — not the diagnosis. Reorder the "state the diagnosis" instruction (~line 82): substantive root cause first, failure phase last (as routing context only).

3. **Step 3 — promote to the skill's centerpiece.** Add a mandatory **Diagnosis Report** as a first-class deliverable, printed to the user *before* the Step 4 depth menu, without the user having to ask.

   **Form — chronological narrative in plain prose.** The report tells the story of the implementation attempt as a sequence of events: what the implementation did, what defect the review found, what the fix changed, and what new defect that fix introduced — round by round, in complete sentences. One short paragraph per review round is the natural shape; a single-round failure may be one paragraph total. **Length scales with the number of rounds — never compress a multi-round chain to fit a sentence budget** (that is what pushes the report into table form). Reviewer findings from the recurring rounds (2+) are woven into the narrative as quotes or paraphrases, as evidence.

   **No tables, no fragment-style bullet lists** in the Diagnosis Report — the causal story is read top to bottom, not reconstructed from a grid. (Tables remain fine elsewhere in the skill where they already exist, e.g. the sidecar `step` contract table.)

   **Language — the domain of the task.** What the spec note / contract line stated wrongly or left ambiguous, and how the plan or code went wrong as a consequence. **Zero orchestrator vocabulary** (no iteration counts, no PASS markers, no phase names, no sidecar).

   **Ending — the root-cause sentence.** The narrative ends with one standalone sentence stating the missing or wrong constraint in the spec/contract, phrased so that, had it been in the spec, the failure chain would not have occurred. This is the payoff line — placed last, visually set off (e.g. a block quote).

   The existing root-cause categories (spec gap / scope overload / mechanical error) stay, but as a classification *attached to* the report, not a substitute for it.

4. **Step 4 non-convergence template (~lines 121–133).** Rewrite the canned prose to lead with substance ("the deliverable is complete and correct; remaining findings are cosmetic: <one-line summary of what they are>") and mention the PASS mechanics in at most one clause of context. Currently the template puts orchestrator-register prose directly into the agent's mouth.

5. **Step 5 closing output (~line 261).** Before the deleted-files list, restate the Diagnosis Report's conclusion in one paragraph (what was wrong, what was repaired, at which depth). File bookkeeping comes second.

6. **"What NOT to do".** Add: "Never present orchestrator mechanics — iteration limits, missing PASS markers, phase names, sidecar states — as 'the problem'. They are how the failure surfaced, not what failed. This constrains your *output and reporting*, not your analysis: pipeline signals are still read internally to route the repair depth."

## Constraints

- **Behavior-identical** for artifact discovery, depth routing, rollback, and the sidecar. This is a framing/output reframe, not a logic change.
- Body stays **≤ 500 lines**; keep the file's existing English, tone, and formatting conventions.
- **Do not touch** the sidecar `step` closed-set table, the closed-set contract text, or any git commands.
- Frontmatter unchanged.

## What NOT to do

- Do not rewrite the skill or restructure its steps — the six edits are surgical.
- Do not change the classification logic or the PASS-marker signal detection — only relabel it as internal routing.
- Do not remove the root-cause categories — attach them to the Diagnosis Report, don't replace it with them.
- Do not let the Diagnosis Report use any orchestrator vocabulary — it is stated purely in the task's domain terms.
- Do not present the failure chain as a table or as compressed fragments — the Diagnosis Report is a story the user reads once, top to bottom, not a data structure.
