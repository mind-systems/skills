# Plan: roadmap-outline + roadmap-decompose: remove stale `/aif-plan`, `/aif-implement`, `/decompose` references

## Context
Both planning skills point users at a pipeline that no longer exists in the active set (`aif-plan` unlinked, `aif-implement` absent, execution owned by the orchestrator). This milestone rewrites those stale references to point at `/roadmap-decompose` and the orchestrator — a reference cleanup only, no logic changes.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Fix references

- [x] **Task 1: Fix `roadmap-outline` Critical Rules 1 & 5**
  Files: `src/skills/roadmap-outline/SKILL.md`
  Line 79 (Critical Rule 1): replace the `(that's /aif-plan)` parenthetical so granular tasks point at `/roadmap-decompose` — e.g. `not a granular task (that's /roadmap-decompose)`. Line 229 (Critical Rule 5): rephrase to "NO implementation — this skill only plans; implementation is the orchestrator's job (a separate run)". Remove all `/aif-plan` and `/aif-implement` mentions. Then grep this file for any remaining `aif-plan`, `aif-implement`, or bare `/decompose` occurrences and fix them the same way. Wording only — no structural or gate changes.

- [x] **Task 2: Fix `roadmap-decompose` Critical Rule 5 and Mode 3 references** (depends on Task 1)
  Files: `src/skills/roadmap-decompose/SKILL.md`
  Line 291 (Critical Rule 5): apply the same rephrase — "NO implementation — this skill only plans; implementation is the orchestrator's job (a separate run)". Line 236 (Mode 3 heading): `(/decompose check)` → `(/roadmap-decompose check)`. Line 240: "tell the user to run `/decompose` first" → "run `/roadmap-decompose` first". Then grep this file for any remaining `aif-plan`, `aif-implement`, or bare `/decompose` occurrences and fix them the same way. Wording only — no mode, gate, or logic changes.

## Notes
- **Never touch `upstream/ai-factory/`** — only the `src/skills/` copies above.
- Reference cleanup only; do not alter any workflow logic, modes, or gates.
- Fewer than 5 tasks — single commit at the end: "Remove stale pipeline references from roadmap-outline and roadmap-decompose".
