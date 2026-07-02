# roadmap-outline: slim to philosophy-only; delegate maintenance flow to roadmap-engine

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- Depends on note 43 (engine gains the shared maintenance flow); presumes note 36 (stale `/aif-plan`, `/aif-implement` references removed) has landed — do not reintroduce them.
- After the engine absorbs the flow, `src/skills/roadmap-outline/SKILL.md` keeps only its **strategic lens**; the duplicated flow machinery is deleted and replaced with "ensure `roadmap-engine` is loaded once this chat and run its maintenance flow with the hooks below".

## Details

What stays (the philosophy):

- **Granularity:** each entry is a high-level goal — a capability the system gains, not a task; 5–15 milestones is the sweet spot (fewer = too vague, more = too granular); milestones later serve as **phase names** for the decomposition pass; order by logical sequence, dependencies first; mark already-done work `[x]`.
- **Coarse two-tier rendering:** entries render per the engine's format at strategic granularity (contract line + spec note), vision line sourced from `DESCRIPTION.md` or user input.
- **The spec note is optional at this tier:** when the contract line alone fully carries a milestone-phase (often it is just a named capability), skip the note — the entry then ends without a `Spec:` tag instead of pointing at an invented one. Write a note only when there is real strategic content the line can't hold (constraints, ordering rationale, scope boundaries). Never pad a note to justify its existence; `roadmap-decompose` will produce the real spec notes when the phase is atomized.
- **Target-file routing** (trivial policy): always `.ai-factory/ROADMAP.md`.
- Philosophy-tier critical rules: milestones are high-level (granular tasks belong to `/roadmap-decompose`); never remove silently (if kept here rather than in the engine's mechanism rules — keep it in exactly one place, the engine); completed stay `[x]` until `roadmap-prune`; plans only — the orchestrator implements (post-36 wording).
- No per-entry gate — outline registers no gate hook (that is decompose's atomicity gate); state this explicitly so the agent does not improvise one.

What goes: Step 0, mode determination, all Mode 1/2/3 machinery, dialogs, check-mode scan, summary blocks — all covered by the engine's flow section.

Expected size: roughly 40–70 lines. Frontmatter unchanged (minus the `Questions` pseudo-tool, removed by note 41 — do not reintroduce).

## What NOT to do

- Do not change any behavior — `/roadmap-outline` in any mode must interact exactly as today, flow text coming from the engine.
- Do not restate engine flow or format content inline.
- Do not add an atomicity-style gate to outline — restraint at the strategic tier is the 5–15 rule, not a split gate.
