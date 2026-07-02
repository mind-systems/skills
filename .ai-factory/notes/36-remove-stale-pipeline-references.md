# roadmap-outline + roadmap-decompose: remove stale /aif-plan, /aif-implement, /decompose references

**Date:** 2026-07-02
**Source:** conversation context (skill-pipeline review)

## Key Findings

- Both planning skills still point users at a pipeline that no longer exists in the active set: `aif-plan` is stored but deliberately not symlinked into `active/skills/`, and `aif-implement` does not exist in this repo at all. Execution belongs to the orchestrator (see `docs/workflow.md`).
- Affected spots in `src/skills/roadmap-outline/SKILL.md`: Critical Rule 1 ("not a granular task (that's `/aif-plan`)") and Critical Rule 5 ("use `/aif-plan` to start a feature and `/aif-implement` to execute").
- Affected spots in `src/skills/roadmap-decompose/SKILL.md`: Critical Rule 5 (same `/aif-plan` + `/aif-implement` wording) and Mode 3 heading/body ("`/decompose check`", "tell the user to run `/decompose` first") — a pre-rename artifact; the skill is `/roadmap-decompose`.

## Details

- **outline Critical Rule 1:** replace the `/aif-plan` parenthetical with a pointer to `/roadmap-decompose` (granular tasks are decompose's tier).
- **outline Critical Rule 5:** rephrase to "NO implementation — this skill only plans; implementation is the orchestrator's job (a separate run)".
- **decompose Critical Rule 5:** same rephrase — plans only; the orchestrator implements.
- **decompose Mode 3:** heading `(/decompose check)` → `(/roadmap-decompose check)`; "run `/decompose` first" → "run `/roadmap-decompose` first".
- No other behavior changes. Grep both files for any remaining `aif-plan` / `aif-implement` / bare `/decompose` occurrences and fix them the same way.

## What NOT to do

- Do not touch the upstream mirror (`upstream/ai-factory/`) — only our `src/skills/` copies.
- Do not change any workflow logic, modes, or gates — this is a reference cleanup only.
