## Plan Review Summary

**Plan:** 65.1 — the phase-note directive names a file and a heading, never a line
**Files targeted:** 1 (`src/skills/roadmap-outline-deep/SKILL.md`), plus a read-only sweep
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` lists `roadmap-outline-deep` as the owner of phase notes and preambles. The change stays inside that skill's own Step 1. It doesn't touch `note`, the engine it loads, or `note`'s hook contract, which still reads the directive as free text (`src/skills/note/SKILL.md`, the **Verbosity directive** hook).
- **Rules** — WARN (non-blocking): the repo has no `.ai-factory/RULES.md`, and there's no `.ai-factory/skill-context/aif-review/SKILL.md` either.
- **Roadmap** — OK. The plan matches contract line 65.1 in `.ai-factory/roadmaps/trickster77777.md` (Phase 65, governing spec `docs/reference-by-name.md` among others) and its task spec `.ai-factory/specs/trickster77777/180-…`. It targets the spec's § "What must be true after" and repeats the spec's § "What breaks on contact" sweep.

### Verification against ground truth
- **Target text:** the plan quotes the current bullet exactly as it stands in § "Step 1: Write the phase note": three wrapped lines, led by `- **Verbosity directive** —`.
- **Verbatim sentence:** the replacement, with its wrapped lines joined, contains the spec's pinned sentence exactly, em dashes included.
- **Wrapping:** the new lines are 83, 83, 85 and 41 characters. The longest existing lines in this section are 85, so the new bullet stays within the section's own column. The two-space continuation indent matches the sibling **Destination directory** and **Template** bullets.
- **Re-run rule:** the "template and verbosity directive above" reference in the same Step refers to the directive by name. As the plan says, it needs no edit.
- **Sweep, first search:** running it today returns the pin-gaps walk paragraph and scan-line form, the `roadmap-prune` handoff item, this target, the global CLAUDE.md, `docs/counts-go-stale.md`, `docs/reference-by-name.md`, and the root `CLAUDE.md` index row. That is the plan's expected set exactly.
- **Sweep, second search:** it returns `note`'s hook definition and its template paragraph, the target bullet, the re-run rule, `command-handoff` and `task-rescue`. The spec's Finding also names `docs/sakshi-harness/skill-graph.md` for this search, but the grep does not hit it today. The plan's expected list leaves it out, which matches ground truth. Its "report, don't edit" fallback covers any drift.

### Critical Issues
None.

### Positive Notes
- The plan gives the exact before and after text and states the wrap column, so the implementer has nothing to guess.
- It says outright what not to touch: the `note` skill and the sibling bullets.
- The sweep has a clear expected result and a safe fallback (report any unexpected hit, don't edit it). That keeps work owned by 65.3 and 65.4 out of this task.

PLAN_REVIEW_PASS
