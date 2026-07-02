# docs/workflow.md §7: reframe milestone-rescue-audit as outside-view check with healthy convergence as the expected outcome

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- `docs/workflow.md` §7 describes the audit as triggered "когда по ходу разбора видно, что оркестратор проблему не решает, а **обходит**" — i.e. you already suspect band-aid before running it. The skill itself is built the other way around: an outside-view check of **any** looped (2–3 rounds) or wall-clock-outlier milestone — even one that ultimately passed — whose decisive instrument is the one-sentence root-cause test and whose explicit default is "Default is NOT band-aid" with healthy convergence as the expected result.
- The doc's framing pre-judges the verdict: an agent reading it will reach for the audit only when band-aid is already suspected, and will arrive biased toward confirming it.

## Details

Rewrite the `milestone-rescue-audit` bullet in §7 (and the corresponding line in the ASCII scheme if needed) to say, in the doc's existing Russian style: the audit runs on any milestone that looped or took an outlier amount of wall-clock — even if it passed; it looks from outside and distinguishes convergence-through-understanding from convergence-through-attrition (band-aid accretion around one unnamed structural/spec gap); healthy convergence is the expected outcome, band-aid the exception worth naming; it emits a diagnosis plus one upstream recommendation to chat only. Keep the "обычный порядок: сперва rescue, следом audit по тёплым артефактам" sentence — it is correct — but decouple it from the "видно, что обходит" precondition.

Doc language is Russian — match it (per repo convention: match the language of neighboring docs).

## What NOT to do

- Do not touch §7's `milestone-rescue` bullet — it is accurate.
- Do not restructure the doc or other sections — this is one bullet's reframe.
- Do not describe skill internals (steps, discriminators) in the doc — behavior-level only.
