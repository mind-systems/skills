## Code Review Summary

**Files Reviewed:** 2 targets (`src/commands/command-pin-gaps.md`, `.ai-factory/specs/trickster77777/138-four-witnesses-each-trusted-where-it-is-blind.md`), plus the task spec `168-…md`, the phase note `169-…md`, the governing spec `docs/what-a-task-carries.md`, and the roadmap's Phase 61
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture:** OK. Both edits are prose inside existing files. There is no new module, no `loads:` edge, and no change to the skill graph. `active/commands/command-pin-gaps.md` symlinks to `src/commands/command-pin-gaps.md`, so editing the `src/` file is the right place.
- **Rules:** WARN (informational). `.ai-factory/RULES.md` and `.ai-factory/skill-context/aif-review/SKILL.md` do not exist, so no project overrides apply.
- **Roadmap:** OK. The plan maps to contract line 61.1 in `.ai-factory/roadmaps/trickster77777.md` under Phase 61, whose `Governing spec:` is `docs/what-a-task-carries.md`. The plan's Context names the task spec (`168-…md`) and the governing spec correctly.

### Verification performed
- **Both old substrings match exactly once.** Old substring 1 occurs once in `command-pin-gaps.md`, inside the single-line **Blast-radius holes** paragraph. Old substring 2 occurs once in `138-…md`, inside the single-line `Q4 needs no new class.` paragraph. Both files write each paragraph on one line, as the plan says.
- **The edits reproduce the spec.** I applied both replacements in a simulation, then took the task spec's `> ` quote blocks from § "What must be true after" and joined each block's lines with one space. After the replacements:
  - The spec's full replacement Repair sentence appears in `command-pin-gaps.md`.
  - The spec's full Q4 paragraph appears in `138-…md`.
  - Only one line changes in each file.

  This confirms the plan's working assumption that each line break in the spec's blocks becomes one space, with nothing else changing.
- **The two endings are handled correctly.** Target 1 ends in `.` and target 2 ends in `"`. The rest of the Blast-radius holes paragraph stays unchanged: the opening definition, the contradiction/blocker sentence, and the too-large-sweep sentence. So do **What the pass never writes** and the `**default:**` line with its "rule-sweep-invariant".
- **The leave-untouched list matches the spec's own sweep.** I ran the spec's sweep, `grep -rln "must satisfy after the change" src/ docs/ .ai-factory/`. It returns the two targets plus these files:
  - the roadmap
  - the 56.1 plan
  - the 56.1 plan-review-1
  - `150-…md`
  - `154-…md`
  - `168-…md`
  - `169-…md`
  - handoff `27-…md`

  That is exactly the set the plan lists as historical and leaves untouched. I also searched `src/` and `docs/` for paraphrases ("broken pattern", "sweep must return", "every match must"). The only hit is the target paragraph itself.
- **The task order is sound.** Task 2 depends on task 1 because the quote has to match the new sentence.

### Critical Issues
None.

### Positive Notes
- The plan grounds every edit in the target files' real form. It notes that the files use single-line paragraphs, that the spec's line wrapping belongs to the quote only, and that the two targets end differently. It then pins exact before/after substrings instead of paraphrasing them.
- The untouched set is named explicitly and traced back to the spec's § "What breaks on contact". This leaves the implementer nothing to guess.
- The plan adds no verification tasks. That fits both the governing spec ("Three parts, and none of them is a check") and the point of this task.

## Deferred observations
- Affects: `.ai-factory/specs/trickster77777/168-the-repair-is-a-mood-not-a-mechanism.md` / Phase 61 — The pinned replacement defines the invariant as "a recorded finding of what the sweep, run now, reaches and how each match reads against the rule". The governing spec's § "Blast radius: the rule, not the snapshot" (`docs/what-a-task-carries.md`) says a spec "never records … a snapshot of what a search returned at spec-writing time". The new wording tries to separate the two with its closing "never the sweep's own enumeration of what it found". Still, "what the sweep, run now, reaches" sits close to the snapshot that section forbids, and a future `command-pin-gaps` run may read it as permission to record one. The wording is pinned word for word by the task spec, so the plan cannot and should not change it. The phase's author should decide whether the governing spec and the new Repair sentence say the same thing, or whether one of them needs a clarifying clause.

PLAN_REVIEW_PASS
