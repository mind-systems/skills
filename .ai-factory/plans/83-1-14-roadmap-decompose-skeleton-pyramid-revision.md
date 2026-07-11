# Plan: roadmap-decompose-skeleton — pyramid revision

## Context
Audit `src/skills/roadmap-decompose-skeleton/SKILL.md` (157 lines) — already the pyramid shape (a philosophy top over two engines, `loads: roadmap-engine test-philosophy`) — against the pyramid and the two-reader register; fix only what the audit finds. "No change" plus a one-paragraph audit report is a complete, legal outcome — padding a conformant skill is itself a failure.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Audit

- [x] **Task 1: Audit the skill against the philosophy and write the report**
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md` (read-only in this task)
  Read the body in full against three lenses, using `docs/skill-pyramid.md` and `docs/skill-composition-model.md` as the audit standard:
  - **Leaked engine content** — the spec's primary target. Judge whether any content owned by the two loaded engines is *restated* inline instead of delegated:
    - `test-philosophy` owns the silent-failure discriminator. Lens 2 (lines 83–84) spells it out inline ("write tests only for surfaces that fail *silently* … skip surfaces that fail *loudly* (compile error, exception, DI failure, 4xx/5xx)"). Judge whether this is a leaked restatement that should collapse to a load/link, or whether it is the one intentionally-inline TDD sentence that Critical Rule 1 pins. Resolve the tension against the walkable-tree rule (a fact's second home is a link to its first) — do not assume; decide and record the reasoning.
    - `roadmap-engine` owns the two-tier artifact format (contract line + spec note). Check Step 4 and the "Load-once / dependencies" section for any restated format fragments that should be a link rather than a copy.
  - **Procedural ceremony** — per the composition model (what-to-pin vs what-to-trust): flag narration the executor performs unprompted (obvious step sequencing, the ASCII call-graph diagram at lines 42–45 if it merely restates the `loads:` frontmatter, self-describing prose). Distinguish it from **pinned decision contracts that must stay verbatim** (see Guards in Task 2).
  - **Two-reader register** (`docs/skill-composition-model.md` § "У каждой строки два читателя") — verify each line addresses the right reader: instructions to the executor are imperatives; knowledge for the editor is declarative. Flag any misaddressed or doubled lines.
  Produce a one-paragraph audit report that names **each finding with its concrete fix**, or states conformance. This report is the task's primary deliverable and gates Task 2.

### Phase 2: Apply findings (only if the audit finds any)

- [x] **Task 2: Apply only the audit-confirmed fixes** (depends on Task 1)
  Files: `src/skills/roadmap-decompose-skeleton/SKILL.md`
  Apply **only** what Task 1's report names — inline engine restatements become loads/links to their owner, procedural ceremony is cut, misaddressed lines are re-registered. Skip this task entirely if the audit reported conformance.
  Guards (from the spec's Guards):
  - **Behavior-identical** whatever the outcome; **frontmatter unchanged** — `name`, `description`, `argument-hint`, `disable-model-invocation`, `allowed-tools`, and `loads: roadmap-engine test-philosophy` byte-identical.
  - **The three lenses' decision contracts stay pinned verbatim** — these are contract text, not ceremony:
    - Fusion at skeleton:impl **1:1** into one "contract" milestone (Step 2).
    - Standalone shared-scaffold milestone when the skeleton is shared across **2+** impl tasks (Step 2 Exception).
    - Concurrency contract-task for a **heavy** task touching **≥2 of** {async I/O, stateful buffer/event queue, lifecycle} (Lens 3).
    - Both canon anchors — m36 (`PassThroughIndicator` stateful-double) and m37 (`clearHeap()`/`drainHeap()`) — stay verbatim.
  - **Restraint-first-class wording stays** — the restraint bullets under Lenses 1 and 3, and Critical Rule 5.
  - Do not add or expand content; a revision only removes / relinks / re-registers. No new `references/` subdirectory unless the audit explicitly names a rarely-read branch — do not invent structure.

- [x] **Task 3: Live baseline verification (only if the body changed)** (depends on Task 2)
  Files: none (verification only)
  If and only if Task 2 changed the body, confirm behavior is identical per the spec's baseline guard: run one skeleton pass over a real heavy task and compare the produced splits pre/post — they must be identical. Pick a heavy open task from a project roadmap (or reconstruct one from the m36/m37 canon surfaces) and dry-run the three lenses; verify the skeleton/TDD/concurrency dispositions, the fuse-vs-standalone decision, and the rendered contract-line + spec-note shape are unchanged. If Task 2 was skipped (conformance), no baseline is needed.
