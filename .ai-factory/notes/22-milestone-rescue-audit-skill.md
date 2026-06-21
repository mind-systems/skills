# milestone-rescue-audit: outside-view convergence audit skill

**Date:** 2026-06-21
**Source:** conversation context

## Key Findings

- New downstream-only skill `src/skills/milestone-rescue-audit/` that audits ONE task that
  looped at a stage (2–3 rounds at plan-review/implement-review, or a wall-clock outlier) —
  **even if it PASSED**. The question is not "why did it fail" but "did it converge by
  understanding or by attrition (band-aid accretion around one structural/spec gap)".
- Sibling to `milestone-rescue`, not a mode of it. Different trigger (looped/outlier task,
  often green — vs rescue's "PASS never achieved" failure), different output (a diagnosis +
  one upstream recommendation to chat — vs rescue's ROADMAP description edit).
- The decisive procedure is the **one-sentence root-cause test**: can you write the SINGLE
  sentence that, had it been in the spec/design, would have prevented ALL N findings at once?
  Structural + exists → band-aid accretion (name it, give the structural reframe). No single
  sentence → independent legitimate fixes → "healthy convergence", stop. Default is NOT
  band-aid; over-flagging legitimate fixes is itself a failure mode.
- **Do NOT re-document the orchestrator artifact layout.** The skill is invoked mostly right
  after `milestone-rescue` in the same chat, so plan / plan-reviews / diffs / code-reviews
  are already in context. A thin `Inputs` block names the artifacts and points to
  `milestone-rescue` for the full layout — one source of truth, no drift.

## Details

### Invocation & scope (decided)
- **Manual only** — the user invokes it; no auto-scan of run logs for round-count outliers.
- **Output to chat** — pure diagnosis, no file written, no ROADMAP/spec auto-edit.
- **One task is the unit.** The user may ask to audit several tasks in one call; that is not
  reflected in the skill body (it stays single-task; the user drives the repetition).
- Primary flow: run `milestone-rescue` → then `milestone-rescue-audit` while the artifacts
  are warm in context.

### File to create
`src/skills/milestone-rescue-audit/SKILL.md` only (no references/, scripts/, templates/).

### Frontmatter
- `name: milestone-rescue-audit` (must match dir exactly)
- `description:` what it does + when — outside-view audit of a looped/outlier task (even if
  it passed) to tell band-aid accretion from healthy convergence; run after `milestone-rescue`.
- `allowed-tools: Read` (read-only; it diagnoses, never edits or implements).

### Body — keep the user's audit procedure almost verbatim
The body is the "Outside-View Audit: Convergence by Understanding or by Attrition?" text:
1. **Step 1** — Reconstruct the finding→fix chain (ordered: round → finding(s)+severity → fix
   applied → did the fix introduce/reveal the next round's finding). Note round count,
   severity trend, pass/fail.
2. **Step 2** — Central question: N independent local corrections, or N symptoms of ONE
   structural/spec gap the implementation routes around?
3. **Step 3** — The one-sentence root-cause test (decisive; see above).
4. **Step 4** — Discriminators (corroborate, don't replace the test): BAND-AID ACCRETION
   signals (one common root; local/additive fixes — flag/guard/special-case; whack-a-mole
   same-class finding next round; growing boolean complexity; workaround-named state like
   `sessionHasData`/`isBridging`; a fix fighting stated design intent; reviewer language
   "carried over"/"still"/"transient, self-heals"/"accepted behavior") vs LEGITIMATE FIXES
   (independent findings, genuinely local problems, severity trends down + diverse surface,
   fixes map to domain concepts and hold/reduce complexity).
5. **Step 5** — Verdict on the spectrum: [Independent legitimate fixes]—[Mixed]—[Band-aid
   accretion] + confidence + evidence. "Mixed" allowed. Default is NOT band-aid; require the
   common-root-cause evidence before claiming accretion.
6. **Step 6** — Output: verdict + confidence + one-line justification; the finding→fix chain
   table as evidence; if accretion/mixed — the root-cause sentence, the structural reframe
   that dissolves findings by construction (data-model / derived-state / invariant change at
   the *what* level, not a full redesign), and a band-aid → replacement mapping;
   recommendation (fix upstream — amend spec / decompose milestone / re-architect — vs accept
   as-is, said plainly); cost note (round count + wall-clock).
7. **Guardrails** — both outcomes valid; judge the SEQUENCE not any single fix; not rewriting
   the plan or implementing — produce a diagnosis and one upstream recommendation.

### Thin `Inputs` block (replaces re-documenting artifacts)
Add near the top, ~3–4 lines: "Expects the orchestrator artifacts for one task — the plan,
all plan-reviews, implementation diffs, code-reviews, and final state. Usually run right after
`milestone-rescue`, so they are already in context. If run cold, locate them; for the artifact
layout see `milestone-rescue`." Names the artifacts (Step 1 needs to know what to collect) but
does NOT duplicate where they live or how they parse.

### Register against upstream sync (same atomic concern)
`milestone-rescue-audit` is downstream-only. Add it to `CLAUDE.md` → "Custom skills — never
overwrite from upstream" list, next to `milestone-rescue` / `detangle` / etc., so the next
upstream sync does not wipe it. This is part of the same task (a downstream-only skill that
must survive sync), not a separate milestone.

### Naming history
Considered `milestone-convergence-audit` (describes the question) and `milestone-rescue-deep`.
User chose `milestone-rescue-audit` — keeps the `milestone-rescue` family link visible while
`audit` marks the read-only forensic mode.

## Open Questions

- None blocking. If cold-start invocation (without a prior rescue run) turns out common in
  practice, revisit whether the `Inputs` pointer to `milestone-rescue` is enough or a minimal
  inline artifact-locating recipe is warranted.
