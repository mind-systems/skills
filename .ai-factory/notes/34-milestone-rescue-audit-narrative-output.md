# milestone-rescue-audit: narrative output register (match milestone-rescue's Diagnosis Report form)

**Date:** 2026-07-02
**Source:** conversation context

## Key Findings

- `src/skills/milestone-rescue-audit/SKILL.md`'s **analysis pipeline is sound** and must stay behavior-identical: chain reconstruction → central question → one-sentence root-cause test → discriminators → verdict. The defect is purely the **output contract**: Step 1 *mandates* a `Round | Finding | Fix | …` table, Step 6 *requires* that table in the chat output as "the evidence base", Step 5 reduces evidence to "2–3 bullet points", and Step 6 is a numbered checklist. The user cannot read tables — the causal story (what was tried, what broke, what the fix spawned) has to be mentally reconstructed from a grid.
- The sibling skill `milestone-rescue` was already reframed to a **chronological prose narrative** (see `.ai-factory/notes/33-milestone-rescue-reframe-substantive-defect.md` for the adopted form). This task brings the audit skill's output to the same register. A live run of the reframed `milestone-rescue` confirmed the narrative form works well for exactly this material — multi-round whack-a-mole chains.
- This is an **output-register reframe, not a logic change**: analysis, thresholds, and defaults stay word-for-word; only the deliverable's form changes.

## Details

Five targeted edits to `src/skills/milestone-rescue-audit/SKILL.md`. Do not restructure the steps or change any analysis logic, thresholds, or defaults.

1. **Step 1 — demote the table to an internal working device.** Keep the round-by-round reconstruction, but the `Round | Finding | Fix | …` table becomes **scratch material, not the deliverable**: the agent may organize the chain however it likes while analyzing (the columns remain useful as a checklist of what to capture per round — finding + severity, fix applied, whether the fix introduced/revealed the next finding). State explicitly that the user-facing form is produced in Step 6.

2. **Step 6 — replace the output contract with a narrative.** The deliverable is a **chronological narrative in plain prose**, the same form as `milestone-rescue`'s Diagnosis Report: the story of the milestone told round by round in complete sentences — what the implementation did, what the review found, what the fix changed, and what that fix introduced or revealed next. One short paragraph per round is the natural shape; **length scales with the number of rounds — never compress a multi-round chain to fit a size budget**. Reviewer findings are woven in as quotes or paraphrases. **No tables, no fragment-style bullet lists** in the output — the story is read once, top to bottom. Round counts and severity trends are **legitimate vocabulary here** (convergence across rounds IS the audit's subject) — the ban is on tabular/fragment *form*, not on mentioning rounds.

3. **Verdict placement.** The narrative ends with the verdict: the spectrum position (independent fixes / mixed / band-aid accretion) + confidence, in one or two sentences whose supporting evidence the narrative has already told. Replace Step 5's "2–3 bullet points of evidence" with: **"the narrative is the evidence; the verdict sentence names the 1–2 strongest signals from it."**

4. **Band-aid / Mixed extras as prose.** When the verdict is band-aid accretion or mixed: the root-cause sentence from Step 3 is the payoff line — placed immediately after the verdict, visually set off (block quote). The structural reframe follows as a short prose paragraph (*what*-level only, as now). Item 5's "mapping: each band-aid fix → what the structural change replaces it with" must also be **prose** — one or two sentences per fix woven into the reframe paragraph, not a mapping table or arrow list. The upstream recommendation (amend spec / decompose / re-architect / accept) stays, stated plainly as the closing sentence. The cost note (round count, wall-clock) stays at the very end, one line.

5. **"What NOT to do".** Add: do not present the finding→fix chain as a table or as compressed fragments in the output — tables are permitted only as internal scratch during Step 1; the deliverable is a story the user reads once, top to bottom.

## Constraints

- **Analysis logic behavior-identical:** the one-sentence test remains decisive, the discriminators remain corroborative-only, "default is NOT band-aid" and the healthy-convergence early exit stay **word-for-word**.
- **Chat-only output contract unchanged** — no file writes, no ROADMAP edits.
- Frontmatter unchanged; body stays **≤ 500 lines**; keep the file's existing English, tone, and formatting conventions.

## What NOT to do

- Do not restructure the steps or touch any threshold, default, or discriminator.
- Do not turn the audit into a file-writing skill — it stays chat-only.
- Do not keep the table as the deliverable — it survives only as internal Step 1 scratch.
- Do not compress a multi-round chain to fit a size budget, and do not render it as a table or fragment list in the output.
