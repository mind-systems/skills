# Review: milestone-rescue-audit — narrative output register

**Scope reviewed:** `src/skills/milestone-rescue-audit/SKILL.md` (the only code change; the other staged files are planning artifacts).

## Method
- `git diff HEAD` and `git status` inspected.
- Full changed file read (194 lines).
- Analysis pipeline (Steps 2–4) diffed byte-for-byte against `HEAD` — confirmed **identical**.

## Verification against spec/plan

**Task 1 — Step 1 table demoted to scratch.** ✅ The mandated `Round | Finding | Fix | …` table is removed and replaced with a prose capture list plus an explicit statement that the reconstruction is "internal working material, not the deliverable" and that a scratch table is a fine internal device. Points forward to Step 6 for the user-facing form. What gets reconstructed (finding + severity, fix applied, whether it introduced/revealed the next finding, round count, severity trend, outcome) is preserved.

**Task 2 — Step 6 narrative.** ✅ Deliverable reframed to a chronological prose narrative, one paragraph per round, findings woven as quotes/paraphrases, explicit "No tables, no fragment-style bullet lists," length-scales-with-rounds clause present, round-counts/severity-trends explicitly permitted as vocabulary. Chat-only / no-file-writes contract retained (line 143).

**Task 3 — verdict placement + Step 5 evidence rule.** ✅ Narrative ends with the verdict (spectrum position + confidence). Step 5's old "2–3 bullet points" evidence item is replaced verbatim with the spec's wording: "the narrative is the evidence; the verdict sentence names the 1–2 strongest signals from it." Spectrum, confidence levels, "Mixed" definition, and "default to the left" rule left unchanged.

**Task 4 — band-aid/mixed extras as prose.** ✅ Root-cause sentence as block quote immediately after the verdict; structural reframe as a prose paragraph (*what*-only, "no *how*"); per-fix mapping woven into that paragraph as one-to-two sentences per fix, explicitly "not a mapping table or arrow list"; upstream recommendation as closing sentence; cost note as a single line at the end. The four recommendation options remain a decision-menu describing *when each applies* (agent guidance), not a mandated output shape — consistent with the spec's "plain upstream recommendation."

**Task 5 — "What NOT to do" ban.** ✅ New bullet forbids presenting the chain as a table or compressed fragments in the output, permitting tables only as Step 1 scratch.

## Constraint checks
- **Analysis logic behavior-identical:** confirmed — Steps 2–4 diff identical; "Default is NOT band-aid" (lines 84–86) and the healthy-convergence early-exit (lines 81–82) are word-for-word unchanged; discriminators corroborative-only unchanged; one-sentence test decisive unchanged.
- **Chat-only:** unchanged (no file-write instructions introduced; `allowed-tools: Read` only).
- **Frontmatter:** unchanged.
- **Body length:** 194 lines ≤ 500.
- **English/tone/formatting:** consistent with the rest of the file.

## Observations (non-blocking, no action required)
- Step 5's Evidence bullet now forward-references "the narrative," which is only produced in Step 6. This is a deliberate, spec-mandated forward reference and reads cleanly when the skill is taken as a whole; not a defect.
- Line 50 ("The full chain is the evidence") and Step 5 ("the narrative is the evidence") coexist without contradiction — the reconstructed chain is the evidence base, the narrative is its rendering.

No bugs, security issues, or correctness problems found. The change is a pure output-register reframe with the analysis pipeline provably unchanged.

REVIEW_PASS
