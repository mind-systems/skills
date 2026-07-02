# Plan: milestone-rescue-audit — narrative output register (match milestone-rescue's Diagnosis Report)

## Context
Reframe `milestone-rescue-audit`'s deliverable from a `Round | Finding | Fix` table into a chronological prose narrative (matching `milestone-rescue`'s Diagnosis Report), leaving the entire analysis pipeline — thresholds, discriminators, defaults — behavior-identical.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Reframe output register

- [x] **Task 1: Demote Step 1 table to internal scratch**
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  In "Step 1 — Reconstruct the finding→fix chain" (lines ~35–46): keep the round-by-round reconstruction and the round-count / severity-trend / outcome notes, but reframe the `Round | Finding(s) + severity | Fix applied | …` table as **internal working material, not the deliverable**. State that the agent may organize the chain however it likes while analyzing, that the columns remain a useful checklist of what to capture per round (finding + severity, fix applied, whether the fix introduced/revealed the next finding), and that the **user-facing form is produced in Step 6**. Do not change what gets reconstructed — only its status (scratch vs deliverable).

- [x] **Task 2: Replace Step 6 output contract with a chronological prose narrative** (depends on Task 1)
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  Rewrite "Step 6 — Output (to chat only)" (lines ~137–159). The deliverable becomes a **chronological narrative in plain prose** — the same register as `milestone-rescue`'s Diagnosis Report: the milestone told round by round in complete sentences (what the implementation did, what the review found, what the fix changed, what that fix introduced or revealed next). One short paragraph per round is the natural shape; reviewer findings woven in as quotes/paraphrases. **No tables, no fragment-style bullet lists** in the output. State that **length scales with the number of rounds — never compress a multi-round chain to fit a size budget**. Explicitly allow round counts and severity trends as legitimate vocabulary (convergence across rounds is the audit's subject); the ban is on tabular/fragment *form*, not on mentioning rounds. Keep the chat-only / no-file-writes contract intact.

- [x] **Task 3: Place the verdict at the end of the narrative and update Step 5 evidence rule** (depends on Task 2)
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  In the rewritten Step 6: the narrative **ends with the verdict** — spectrum position (independent fixes / mixed / band-aid accretion) + confidence, in one or two sentences whose support the narrative has already told. In "Step 5 — Verdict" (lines ~118–133), replace the "**Evidence:** 2–3 bullet points…" item with: **"the narrative is the evidence; the verdict sentence names the 1–2 strongest signals from it."** Leave the spectrum, confidence levels, "Mixed" definition, and the "default to the left" rule unchanged.

- [x] **Task 4: Render band-aid / mixed extras as prose** (depends on Task 2)
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  In the rewritten Step 6, convert the band-aid/mixed extras (currently numbered items 3–6 + cost note) into prose that follows the verdict: the Step 3 root-cause sentence as the payoff line placed immediately after the verdict, visually **set off as a block quote**; the structural reframe as a short prose paragraph (*what*-level only, no *how*); the per-fix mapping (each band-aid fix → what the structural change replaces it with) woven into that reframe paragraph as **one or two sentences per fix — not a mapping table or arrow list**; the upstream recommendation (amend spec / decompose / re-architect / accept, with its existing conditions) stated plainly as the closing sentence; the cost note (round count, wall-clock if known) as a single line at the very end.

- [x] **Task 5: Add tabular/fragment ban to "What NOT to do"** (depends on Tasks 1–4)
  Files: `src/skills/milestone-rescue-audit/SKILL.md`
  Add a bullet to the "What NOT to do" section (lines ~163–172): do not present the finding→fix chain as a table or as compressed fragments in the output — tables are permitted only as internal scratch during Step 1; the deliverable is a story the user reads once, top to bottom. Then verify the whole file: analysis logic (Step 3 one-sentence test decisive, Step 4 discriminators corroborative-only, "Default is NOT band-aid", healthy-convergence early exit) is **word-for-word unchanged**; frontmatter unchanged; skill stays chat-only; body ≤ 500 lines.
