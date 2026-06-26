# Plan: milestone-rescue — refactor — repair by depth, roll back to the repaired state

## Context
Refactor `src/skills/milestone-rescue/SKILL.md` so its model becomes diagnose → repair to the depth the root cause reaches → roll the `{NN}-{slug}.json` sidecar + artifacts back to exactly that repaired state, with the user picking the depth — compressing the bloated non-convergence / template / sidecar-prose machinery while keeping every real capability (downstream propagation, scope-overload-as-flag) and the three precision-floor blocks intact.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Constraints (read before editing — apply to every task)
- **One file only:** `src/skills/milestone-rescue/SKILL.md`. No Python, no orchestrator changes (one CLAUDE.md verification touch in Task 8).
- **Leaner by compression, not by gutting.** Do NOT drop diagnose, repair, rollback, downstream propagation, or scope-overload flagging.
- **Precision floor — keep word-for-word, never compress away:**
  1. The exact deleted-file set per variant (which dirs; `git clean -f` for `??` untracked vs `git rm -f` for `A ` staged).
  2. The `step` closed-set table mirroring `_validate_sidecar_step()` / `_detect_milestone_step()` in `orchestrator/main.py` (5 values: `"planned"`, `"plan_review_failed:N"`, `"plan_reviewed"`, `"implemented"`, `"review_failed:N"`).
  3. The "only touch `step`, preserve `planner`/`implementer`/`elapsed`" rule.
  4. The Step-1 artifact-discovery block (referenced by `milestone-rescue-audit`, note 22).
- **Body ≤ 500 lines** (current ~401; compression should keep it well under).
- **Repair depths → rollback states (the core mapping):**
  1. **spec** = spec note `.ai-factory/notes/<NN>-<slug>.md` + its ROADMAP contract line → plan is stale → regenerate it. Delete plan `.md`, plan-reviews, reviews, patches, **and** the sidecar. Orchestrator re-plans (plan absent → plan attempt 1).
  2. **spec + plan** = repair spec + plan `.md`. Keep plan + sidecar. Delete plan-reviews, reviews, patches. Sidecar `step` → `"planned"`.
  3. **spec + plan + code** = repair spec + plan + code by hand in the working tree. Keep plan + passing plan-reviews + hand-fixed diff + sidecar. Delete reviews, patches. Sidecar `step` → `"implemented"`.
  - The spec tier is the **top** of the range, edited only when the requirement itself was wrong; in practice the spec may already be fine and only plan/code need touching. **The contract line IS edited** when the spec tier is in scope.
  - **User picks the depth**; an explicit "fix Y / delete X" overrides.
- **`$TARGET_FILE` resolution is load-bearing — preserve it.** The current Step 4 prose (lines ~130–135) resolves `$TARGET_FILE` (arg-named file → `ROADMAP.md` → `ROADMAP_TESTS.md` for test slugs) and locates the milestone line. This must survive the template removal: the spec-tier contract-line edit must target the correct roadmap file, and Step 5.5 propagation scans `$TARGET_FILE` for downstream `- [ ]` milestones. The retained `argument-hint` (`ROADMAP.md | ROADMAP_TESTS.md`) depends on it.
- **Non-convergence is a fourth, terminal outcome — commit-as-is, no rollback.** When diagnosis is non-convergence and the user commits, perform NO artifact cleanup and NO sidecar change — every artifact describes completed, correct work pending a commit. This is distinct from the three repair depths (which all roll something back).
- **The `"plan_reviewed"` write is intentionally retired.** The new flow only ever *writes* `"planned"` (spec+plan), *writes* `"implemented"` (spec+plan+code), or *deletes* the sidecar (spec). Do not re-introduce a `"plan_reviewed"` write. The other three `step` values (`plan_review_failed:N`, `plan_reviewed`, `review_failed:N`) stay in the closed-set table **only** as the orchestrator-contract reference (precision floor keeps the full 5-row table).

## Tasks

### Phase 1: Reframe the wrapper sections

- [x] **Task 1: Rewrite frontmatter**
  Files: `src/skills/milestone-rescue/SKILL.md`
  Rewrite `description` around the new model: diagnose root cause → repair to depth (spec / spec+plan / spec+plan+code) → roll sidecar + artifacts back to the repaired state → check downstream milestones. Drop the outdated "proposes a ROADMAP milestone-description update … output is exactly one ROADMAP.md edit" framing. Keep trigger phrases "rescue", "milestone failed", "pipeline stopped". Keep `argument-hint: "[path/to/ROADMAP.md | ROADMAP_TESTS.md]"` and `allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion` unchanged. Keep `name: milestone-rescue`.

- [x] **Task 2: Rewrite the intro paragraphs**
  Files: `src/skills/milestone-rescue/SKILL.md`
  Replace the intro (currently lines ~16–24, "Translates failed pipeline artifacts into a concrete ROADMAP.md improvement … The output is exactly one ROADMAP.md edit") with a short framing of the repair-by-depth + rollback model: after the orchestrator exhausts its iteration limit and stops (everything uncommitted), this skill reads the artifacts, diagnoses how deep the cause reaches, repairs to that depth, and rolls the sidecar + artifacts back to exactly that state so the orchestrator re-validates from there. Note the contract line is the roadmap half of the two-tier spec pair (with the spec note) and IS edited when the spec tier is repaired.

### Phase 2: Compress diagnosis (Steps 2–3)

- [x] **Task 3: Compress Step 2 — classify / diagnose** (depends on Task 2)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Keep the plan-phase vs implement-phase classification and the lightweight blocking/non-blocking severity check. Collapse the multi-step non-convergence special-case machinery (current lines ~67–90) into **one diagnosis outcome**: when implement-phase holds (PLAN_REVIEW_PASS present, no REVIEW_PASS) **and** all review rounds are non-blocking (Low/Informational only) **and** the deliverable is present/produced on disk → the work is likely done; recommend committing instead of re-running. One short clause, not its own sub-procedure. Reframe the step so its purpose is "diagnose the root cause and how deep it reaches" feeding the depth choice.

- [x] **Task 4: Compress Step 3 — issue extraction** (depends on Task 3)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Drop the 4-attribute numbered-list output format and the verbose dedup-across-rounds prose (current lines ~95–125). Keep the essence: read all rounds (not just the latest); the recurring root cause across rounds is the primary signal; it decides the repair depth. Keep the root-cause categories (specification gap, scope overload, mechanical error) only as brief context since they inform depth + the scope-overload flag — do not re-expand into the old long form.

### Phase 3: Depth choice + apply/rollback (the core — Steps 4–5)

- [x] **Task 5: Replace Step 4 templates with one compact depth choice** (depends on Task 4)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Replace the three large `AskUserQuestion` code blocks (non-convergence / milestone-update / decompose, current lines ~128–219) with **one compact depth choice** presented via `AskUserQuestion`, ordered by variant: **spec** → **spec + plan** → **spec + plan + code** (shallowest spec edit first, deepest hand-fixed code last). Each option names the resulting rollback state. The user's explicit "fix Y / delete X" overrides the menu. Preserve the **scope-overload flag**: if diagnosis shows the task is genuinely malformed (too many concerns / wrong framing) rather than under-specified, the skill does NOT decompose — it flags this and points the user to `roadmap-decompose` (user decides whether to remove/replace or rewrite). Fold the non-convergence "recommend commit" outcome in here as the diagnosis result from Task 3, not a separate template.
  **Preserve the `$TARGET_FILE` resolution** (current lines ~130–135) — it is NOT part of the templates being removed. Keep: arg-named file → `.ai-factory/<file>`; test-slug keywords → `ROADMAP_TESTS.md`; otherwise → `ROADMAP.md`; then locate the milestone line for the slug. It feeds the spec-tier contract-line edit (Task 6) and Step 5.5 propagation (Task 7).

- [x] **Task 6: Merge Step 5 into one apply section keyed by the three depths** (depends on Task 5)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Merge the old propose/apply overlap (Steps 4 + 5) into one apply section organized by the three repair depths. For each depth state the repair → keep → delete → sidecar `step`:
  1. **spec:** repair spec note + contract line in `$TARGET_FILE` (`Edit`); delete plan `.md`, plan-reviews, reviews, patches, **and** the `.json` sidecar; orchestrator re-plans.
  2. **spec + plan:** repair spec (note + contract line in `$TARGET_FILE`) + plan `.md`; keep plan + sidecar; delete plan-reviews, reviews, patches; sidecar `step` → `"planned"`.
  3. **spec + plan + code:** repair spec + plan + code by hand; keep plan + passing plan-reviews + hand-fixed diff + sidecar; delete reviews, patches; sidecar `step` → `"implemented"`.
  - **Non-convergence (commit-as-is) — terminal, no rollback:** when the Task 3 diagnosis is non-convergence and the user commits, do NOT delete any artifact and do NOT touch the sidecar (current lines ~225–229). Every artifact describes completed, correct work pending a commit. State this path explicitly so it is not lost when the apply section is reorganized around the three depths.
  **Precision floor — preserve verbatim:** the exact per-variant deleted-file set with git-native commands (`??` untracked → `git clean -f -- <path>`; `A ` staged → `git rm -f -- <path>`; never delete committed files or other slugs' files; never touch `notes/` except the deliberate spec-note repair); the `step` closed-set table mirroring `orchestrator/main.py` (with the "orchestrator owns it, don't diverge" note and the always-valid-state precondition); the "update ONLY `step`, preserve `planner`/`implementer`/`elapsed`" rule. Compress the surrounding sidecar prose: fold the silent-failure-mode / always-valid-guard / test-mode paragraphs (current lines ~289–302) into the table + one line each. Keep emit lines (`Sidecar deleted (full reset).` / `Sidecar updated: step set to "<value>".`) adapted to the three depths.

### Phase 4: Downstream + cleanup

- [x] **Task 7: Keep & lightly compress Step 5.5 — downstream propagation; update What NOT to do** (depends on Task 6)
  Files: `src/skills/milestone-rescue/SKILL.md`
  Keep downstream propagation: after the milestone is rescued, scan the following `- [ ]` milestones — if a later task touches the same files/APIs/pattern or shares the corrected assumption, surface it and offer to apply the same fix to its spec note + contract line (recurring > mechanical > spec-gap priority). Compress only verbose prose, not the logic. For non-convergence, propagation is a no-op. Then update the **What NOT to do** list: remove outdated bans tied to the old "only output is a ROADMAP edit / never edit the contract line / do not rewrite the plan or implement" framing that now conflict with repair-by-depth (the contract line IS edited; spec/plan/code ARE repaired at the chosen depth). Keep the still-valid bans: don't delete committed files or other slugs' files; don't skip earlier rounds; don't overwrite `planner`/`implementer`/`elapsed`; don't write always-valid `step` values when their artifact is absent.

- [x] **Task 8: Final consistency pass + CLAUDE.md guard verification** (depends on Task 7)
  Files: `src/skills/milestone-rescue/SKILL.md`, `CLAUDE.md`
  Re-read the full refactored `SKILL.md` end to end: confirm step numbering/cross-references are coherent after the merge, the three precision-floor blocks survive word-for-word, body ≤ 500 lines, and `name`/`allowed-tools`/`argument-hint` are intact. Verify `CLAUDE.md` still lists `milestone-rescue` under "Custom skills — never overwrite from upstream" (it already is — confirm, add only if missing). No other CLAUDE.md edits.

## Commit Plan
- **Commit 1** (after tasks 1–2): "Reframe milestone-rescue around repair-by-depth"
- **Commit 2** (after tasks 3–4): "Compress milestone-rescue diagnosis steps"
- **Commit 3** (after tasks 5–6): "Rework milestone-rescue into depth-keyed apply and rollback"
- **Commit 4** (after tasks 7–8): "Keep downstream propagation and finalize milestone-rescue refactor"
