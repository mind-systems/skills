# Plan: roadmap-engine: shape-condition the checkbox flows; soften the two-tier opener

## Context
Milestone 52 shape-conditioned the engine's note/placeholder mandates (draft/finalize/Add) but left the checkbox-marking flows and the section opener assuming every entry is a checkbox'd two-tier milestone. This milestone closes that gap in one file — `src/skills/roadmap-engine/SKILL.md` — by shape-conditioning Review progress and Check mode and softening the opener, while keeping the engine caller-agnostic and the already-loosened wording byte-identical.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Shape-condition the checkbox flows and opener

- [x] **Task 1: Soften the two-tier opener (`SKILL.md:27`)**
  Files: `src/skills/roadmap-engine/SKILL.md`
  In "## The two-tier artifact", replace the categorical first sentence "Each milestone is a two-tier entry: a contract line in the roadmap plus a full spec note …" so the two-tier entry is scoped to the **task tier**: a caller's hook (a) may define entries with no contract line (e.g. a phase header), and the note/tag machinery of this section applies only where a contract line exists. One–two sentences, no restructuring — keep the `<NN>`/`<slug>` note-path detail and the exact `Spec:` tag text that follow. Use the same "e.g. a phase header" register the draft/finalize/Add loosening already uses; introduce no skill names.

- [x] **Task 2: Shape-condition "Review progress" (`SKILL.md:201-203`)**
  Files: `src/skills/roadmap-engine/SKILL.md`
  In the Update-mode action list, amend the "Review progress" bullet so the `[x]` marking applies to **checkbox entries only** — entries whose shape carries no checkbox (e.g. a phase header) are never marked. Where such entries coexist with `N.M` tasks in the same file, phase progress may be **reported** as derived from its child tasks (all `[x]` → phase reads complete), report-only — the flow never marks anything at the phase tier. Keep the existing scan-for-evidence / propose / apply-on-confirmation / leave-the-rest-unchanged mechanics intact for checkbox entries.

- [x] **Task 3: Add the Check-mode shape-condition sentence (`SKILL.md:225-264`)**
  Files: `src/skills/roadmap-engine/SKILL.md`
  At the top of "### Check mode" (before or alongside the "Non-interactive scan" line), add one sentence: Check mode operates on **checkbox entries only**; when the caller's entry shape (hook a) carries no checkbox, there is nothing to scan and the caller registers no check mode (its argument routing should not advertise one). Do not change the scan/evidence/scoring/report mechanics for checkbox callers, and do not touch the mode-determination routing at `:116`.

## Guards (apply to every task)
- **One file only:** `src/skills/roadmap-engine/SKILL.md`.
- **Byte-identical — do not touch:** the create-mode draft wording (`:154-160`), finalize (`:174-180`), update-mode Add (`:204-208`), the "## Roadmap File Format" section, the numbering rules, and the contract-line rules.
- **Caller-agnostic:** no skill names anywhere in the engine — `grep -n "roadmap-outline\|roadmap-decompose\|skeleton" src/skills/roadmap-engine/SKILL.md` must return zero matches. Use only generic "e.g. a phase header" phrasing.
- **File stays ≤500 lines** (274 today).

## Verify
- `grep -n "Each milestone is a two-tier entry" src/skills/roadmap-engine/SKILL.md` → no categorical match.
- Review progress and Check mode each carry a shape-condition sentence; draft/finalize/Add sections unchanged from HEAD.
- `grep -n "roadmap-outline\|roadmap-decompose\|skeleton" src/skills/roadmap-engine/SKILL.md` → zero matches.
