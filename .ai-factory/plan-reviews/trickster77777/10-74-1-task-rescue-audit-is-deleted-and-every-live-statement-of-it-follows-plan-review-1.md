## Plan Review Summary

**Plan:** 74.1 — task-rescue-audit is deleted and every live statement of it follows
**Files in scope:** 4 edited/removed (`src/skills/task-rescue-audit/`, `active/skills/task-rescue-audit`, `src/skills/task-rescue/SKILL.md`, `docs/sakshi-harness/skill-cycle.md`, `CLAUDE.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap** — OK. The plan maps to `.ai-factory/roadmaps/trickster77777.md`, Phase 74 "task-rescue-audit is retired", task 74.1. The contract line's `Spec:` tag resolves to `.ai-factory/specs/trickster77777/0207-…`, and I read it in full. The phase header names no `Governing spec:`.
- **Architecture** — OK. `.ai-factory/ARCHITECTURE.md` does not name `task-rescue-audit`. Its Rescue rows in `## Features` refer to `task-rescue` only, so nothing there needs to change.
- **Rules** — WARN (non-blocking). `.ai-factory/RULES.md` is not present. `.ai-factory/skill-context/aif-review/SKILL.md` is not present either.

### Verification against ground truth

Every before-text the plan quotes matches what is on disk now:

- **`src/skills/task-rescue/SKILL.md`**: the wrapped paragraph ends with `evidence. This narrative register is shared with \`task-rescue-audit\`'s output —` / `change it in both files or neither.`, followed by a blank line and "No tables, no fragment-style bullet lists…". The plan deletes exactly the two sentences, and the paragraph ends at "evidence.", which matches the spec's after-text.
- **`docs/sakshi-harness/skill-cycle.md`**:
  - The heading on disk is "## Когда task не сходится — `task-rescue`, `task-rescue-audit`".
  - The first two sentences of the paragraph under it are byte-identical to the after-text the spec pins.
  - The scheme line `          │   task-rescue-audit          ← взгляд снаружи на зациклившуюся task` sits between the kept `task-rescue` line and the `          ▼` line.
  - All three edits match the spec.
- **`CLAUDE.md`**: all four places are present as quoted (the Skill cycle row, the tree comment, the active-set list, and the "Everything else in `src/skills/` is ours" list). The after-texts match the spec. `AGENTS.md` is a symlink to `CLAUDE.md`, as the plan says.
- **Removal**: `src/skills/task-rescue-audit/` contains only `SKILL.md`. `active/skills/task-rescue-audit` is a symlink to `../../src/skills/task-rescue-audit`. The plan warns against deleting through the link, which is correct.

**Completeness.** I ran both spec sweeps from the family root.
- The first sweep hits only the skill's own file and the places the plan already lists. The orchestrator gives no hit at present; the plan's note that an orchestrator hit would stay as it is still holds.
- The second sweep also hits `docs/reserved-words.md` and `docs/self-analysis.md`. The spec leaves both untouched, and so does the plan.
- Neither sweep covers `upstream/*.md`, `.ai-factory/ARCHITECTURE.md`, the `src/` `loads:` fields, `src/commands/` or `README.md`, so I checked those separately. None of them names the skill.
- The only other `audit` strings are:
  - the legacy `[audit-corroborated]`/`[audit-dismissed]` markers, which stay as protocol tokens;
  - the unrelated "audit" in `aif-docs` and `ui-ux-pro-max`.

The plan's list of files is complete.

### Critical Issues

None.

### Positive Notes

- The plan writes the first sweep with single quotes. The spec gives it in double quotes, and in a shell double quotes would run the backticked `` `-audit` `` as a command substitution. The plan's form actually runs.
- Every edit names its exact before-text and after-text, including the lines next to it that must stay byte-identical (the `task-rescue` scheme line, the `▼` line, the blank line and the "No tables…" paragraph). This keeps the implementer away from nearby text.
- What the spec says stays (the final registry, `self-analysis.md`, the legacy markers, the orchestrator repository, `.ai-factory/` history) is restated as out of scope, with the reason for each.
- The final read-only sweep task also checks that no symlink in `active/skills/` is left dangling.

PLAN_REVIEW_PASS
