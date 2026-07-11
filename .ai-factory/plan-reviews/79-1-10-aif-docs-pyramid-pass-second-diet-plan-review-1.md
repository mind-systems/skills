## Plan Review Summary

**Plan:** `79-1-10-aif-docs-pyramid-pass-second-diet.md`
**Target:** `src/skills/aif-docs/SKILL.md` (454 lines) → second `references/` diet
**Files Reviewed:** plan + target SKILL.md (full) + spec 30 + ROADMAP line 1.10 + ARCHITECTURE composition rule + `references/` dir
**Risk Level:** 🟢 Low

### Context Gates

- **ROADMAP (`ROADMAP.md:177`, milestone 1.10):** Plan aligns with the contract line — extend the `references/` pattern to remaining per-state procedures, keep state detection / Core Principles / the genre sentence / CLAUDE.md-index contract, dialogs byte-identical, re-basing as the sole exception. No drift. ✅
- **Spec 30 (`.ai-factory/specs/30-aif-docs-pyramid-pass.md`):** Every spec directive is honored:
  - "Body keeps … the CLAUDE.md index contract, the key-artifact updating duty first-class" → Task 4 lifts 2.2b out of the State A branch into a first-class body section. This is the correct structural call (States A and B both reach it), and it matches spec line 11 precisely. ✅
  - "Verbatim-protected: every `AskUserQuestion` dialog, the genre sentence at `:19`" → carried as Constraints; the topic dialog / split-proposal / audit-results blocks travel byte-identical. ✅
  - "Re-basing rule — symmetric, grep-not-enumeration" → Tasks 1 and 3 apply it and cite grep evidence. ✅
  - "Closure rule / mid-pass discovery is not a plan defect" → carried verbatim as a Constraint. ✅
- **ARCHITECTURE (`ARCHITECTURE.md:9-10`, ≤500-line + `references/` progressive-disclosure norm):** Plan extends the existing mechanism (Constraint "don't invent a second one"), drives the body to <300 — well within norm. No boundary or dependency violation. ✅
- **RULES.md:** absent — gate skipped. ✅
- **Prior reviews for this milestone:** none — first pass.

### Line-number / path verification (all confirmed against ground truth)

- `SKILL.md` is **454 lines** (`wc -l`) — matches the plan. ✅
- `references/` dir exists with exactly `topic-guides.md`, `html-generation.md`, `consolidation.md`, `REVIEW-CHECKLISTS.md` — the four the plan names as the established pattern. ✅
- Genre sentence at **`:19`** — confirmed. ✅
- `:253` topic-guides pointer (State A 2.3) and `:327` REVIEW-CHECKLISTS pointer (State C 2.1.1) — confirmed as the **only two** `read \`references/\`` pointers inside blocks being moved. Body-resident pointers `:102` (Step 1.1), `:355` (Step 3), and the differently-phrased `:363` (Step 4) stay put. The plan's grep claim is exactly right. ✅
- `:434` "(Step 2.2b)" in Step 5 — confirmed; Task 4's re-point of this dangling label is necessary and correct. ✅
- Internal State-C cross-refs `:323` "(see 2.1.1)" and `:329` "(Step 2.2)" — confirmed; both referents (2.1.1, 2.2) travel together into `audit-state-c.md`, so they stay coherent with no fix, as the plan states. ✅
- The `--web` State-C routing (`:78-96`) reaching "Step 2 (State C)" — the plan explicitly routes the audit paths to `audit-state-c.md` and gates on "routing still resolves / no step-number dangling." ✅

### Sibling-path re-basing logic — correct

When the `references/topic-guides.md` / `references/REVIEW-CHECKLISTS.md` pointers move *into* a `references/` file, `references/<X>` would resolve to `references/references/<X>` (broken). Rewriting to the sibling form `<X>` is the correct fix, symmetric across both occurrences, and squarely inside spec 30's one documented exception. Sound.

### Critical Issues

None.

### Positive Notes

- **The 2.2b decision is the crux and the plan gets it right.** Splitting 2.2b out of the moved State A block and lifting it to a first-class body home — rather than dragging it into `generate-state-a.md` — is what keeps the single-home-per-fact invariant intact while States A and B both reach the index contract. The plan reasons this explicitly instead of moving mechanically.
- **Byte-identical discipline is scoped precisely**, with each of the three re-basing deviations (State A `:253`, State C `:327`, Step 5 `:434`) named, justified, and bounded — no hand-waving "adjust as needed."
- **The flow-preservation pointer** inserted where State A reached 2.2b (Task 1) correctly reads as a re-basing of a "label that ceases to exist … re-pointed to its new home," keeping a State A run's behavior identical even though 2.2b now lives in the body.
- **Verification is concrete and falsifiable:** body <300 lines, one pointer per moved procedure, dialogs + genre sentence byte-identical, and a State C baseline replay pre/post — matching spec 30's verification block.
- Dependency ordering (Task 4 depends on 1-3) is correct: the body rewire must follow the carve-outs.

### Confirmations for the implementer (not defects — the plan already gates these)

- When collapsing each moved procedure to a pointer, retain enough of the state-named heading that Step 1's routing references ("run … Step 2 (State C)") still resolve — the plan's result gate ("no step-number dangling") already requires this; it is called out here only to keep it front-of-mind during the edit.
- Line numbers cited in the plan (`:253`, `:327`, `:434`, etc.) are pre-edit anchors and will shift as text is removed top-to-bottom — locate by content/grep, not by frozen line number, exactly as the re-basing rule instructs.

The plan is accurate against ground truth, architecturally sound, complete, and self-verifying. No missing steps, no wrong codebase assumptions, no bad paths or API misuse.

PLAN_REVIEW_PASS
