## Code Review Summary

**Files Reviewed:** 1 plan, plus the files it targets: `src/skills/orchestrator-artifacts/SKILL.md`, `src/skills/task-rescue/SKILL.md`, the task spec `0248`, the phase note `0247`, and the roadmap line 86.1 in `.ai-factory/roadmaps/trickster77777.md`
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` cites no orchestrator source file, and the plan does not touch it. The only remaining root-relative citations of orchestrator files are in `docs/` (`docs/the-pipeline-speaks-to-an-architect.md`, `docs/reserved-words.md`). Per the phase note, a doc may name a sibling repo's path, so leaving them alone is correct.
- **Rules** — WARN (informational): `.ai-factory/RULES.md` does not exist, which the plan already says. `.ai-factory/skill-context/aif-review/SKILL.md` does not exist either, so no project overrides apply.
- **Roadmap** — OK. The plan heading matches the open line **86.1** under Phase 86 in `.ai-factory/roadmaps/trickster77777.md`. That line's `Spec:` tag resolves to `0248`, which the plan cites, and the phase note `0247` is cited too. The phase has no `Governing spec:`. This is consistent with the phase note, which says no doc states this rule beyond the standing one.

### Verification against ground truth
- **`orchestrator-artifacts` § "7. Mirrors-the-orchestrator invariant"**: the current paragraph is a single sentence over three lines. It opens "This file mirrors the orchestrator's file protocol (`orchestrator/main.py`," and ends "do not let them diverge.", exactly as the plan describes. Replacing the whole paragraph with the spec's pinned sentence is therefore the same as replacing "the sentence", as the spec requires. The surrounding prose wraps at about 84 columns (the current line 2 is 84 characters long), so the plan's wrap guidance is accurate.
- **`task-rescue` § "Valid sidecar `step` states"**: the first paragraph matches the plan's four-part breakdown exactly:
  1. The closed-set sentence.
  2. The mirror sentence, citing `_validate_sidecar_step()` / `_detect_task_step()` in `orchestrator/resume.py`.
  3. The artifact-paths sentence.
  4. The rest of the paragraph.

  The mirror sentence shares its first line with the end of the closed-set sentence ("one. This table mirrors …"). The plan's rule "re-wrap only the lines the edit touches" handles that correctly. The wrap width of about 88 matches the current lines.
- **Sweep**: I ran the four greps from the spec over `src`.
  - `orchestrator/`, `_validate_sidecar_step` and `_detect_task_step` currently match only the two target sentences.
  - `\.py` matches the two targets and otherwise only `ui-ux-pro-max`: its `SKILL.md` invocations of its own `scripts/search.py`, the script's own usage lines, and binary `__pycache__/*.pyc` matches. All of these belong to that skill.

  After both edits, the plan's expected results hold. `src/commands` and `src/agents` sit under `src`, so the sweep covers them. Neither skill's `description:` field names an orchestrator source, so leaving the frontmatter unchanged is correct.
- **Scope**: no other file in `src` refers to § 7 by its heading, so no reference breaks.

### Critical Issues
None.

### Positive Notes
- The plan follows the file where the spec's prose is loose. The spec's "What breaks on contact" places the `task-rescue` sentence "after the valid-states table", but in the file it opens the section, before the table. The plan locates it by its surrounding sentences, not by that description.
- Each anchor is a heading or a quoted sentence, never a line number, so it still works if lines shift.
- The pinned after-texts are copied verbatim. The plan also explicitly says to keep the neighbouring sentences byte-identical, as the spec's "The rest of each paragraph stands" requires.
- The sweep is read-only and has stated expected outcomes, so the implementer has a concrete check for "done".

## Deferred observations
- Affects: `.ai-factory/specs/trickster77777/0248-the-skills-mirror-the-orchestrators-protocol-without-citing-its-source.md` — The spec's "What breaks on contact" → **Finding** paragraph says the `task-rescue` mirror sentence comes "after the valid-states table". In the file it is part of the paragraph that opens § "Valid sidecar `step` states", before the table. The plan already follows the file, so this does not affect the edit. Only the spec's prose is inaccurate, and fixing it is a spec edit outside this plan's file boundary.

PLAN_REVIEW_PASS
