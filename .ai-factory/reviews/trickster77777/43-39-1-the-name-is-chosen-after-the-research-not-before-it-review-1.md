## Code Review Summary

**Task:** 39.1 — the name is chosen after the research, not before it
**Plan:** `.ai-factory/plans/trickster77777/43-39-1-the-name-is-chosen-after-the-research-not-before-it.md`
**Files changed by this task:** 1 (`src/skills/roadmap-test-coverage/SKILL.md`, +13/−4 inside the Layer 4 agent prompt template)
**Risk Level:** 🟢 Low

### Scope check

`git status` also shows `.ai-factory/notes/07-architect-buffer.md` (M), a handoff under `.ai-factory/handoffs/`, and the plan/plan-review artifacts for this task. The note and handoff were already uncommitted before this task's implementation began and are not part of its diff; the plan and plan-review files are the pipeline's own. Nothing outside the one skill body is attributable to 39.1.

### What was verified against the leaf (file re-read in full around the edit)

- **The three template sentences are the only edit.** The header `Note to write: .ai-factory/specs/<NN>-<slug>.md` is replaced by `Note number: <NN>` + `Note directory: .ai-factory/specs/` plus a three-line instruction that the slug is the agent's own choice, made only after reading the source, "short, lowercase, hyphens" (matches `note` § "Step 2: Determine Slug"), named for what the area turns out to be rather than the `Area:` label. The write instruction now assembles the path as `<Note directory><NN>-<slug>.md` and states the agent writes the file itself, at the path it chose, in the same act — the task spec's "easy to get backwards" point is carried in. The return line reports the exact path written with a four-digit example (`0042-actual-slug.md`), consistent with the width 38.2 landed.
- **Path assembly is correct.** `Note directory: .ai-factory/specs/` carries a trailing slash, so `<Note directory><NN>-<slug>.md` (no separator) yields `.ai-factory/specs/0042-slug.md`. The plan wrote `<Note directory>/<NN>-<slug>.md`; the implemented form avoids a doubled slash and is the right one given the directory line — no defect.
- **Directory matches the number's scan scope.** The `$NEXT_NOTE_NUM` block above the template scans the flat `.ai-factory/specs/` only; the directory now handed to the agent is the same one, so number and destination stay on one space. That block is byte-identical to HEAD.
- **Out-of-scope placeholder sites unchanged.** `grep -n "<NN>-<slug>"` returns five hits: the reworded write instruction plus the four the task spec names as needing no edit — the Layer 6 refactor pointer and the three Layer 8 pointers ("Notes written", handoff Refactor, handoff Bugs). All four are identical to HEAD. `Collect all one-line confirmations.` after the block is the sole consumer of the `saved:` line and is unchanged, so the orchestrator now receives the real path from the only place it exists.
- **Inputs kept.** `Area:`, `Source file(s):`, `Existing spec file (if any):`, the four-step task list, the per-test-case bullets, and the document body template `# <Area Name> — Test Plan` … `## Gotchas` are untouched.
- **Constraints.** Body is 444 lines (≤ 500). Frontmatter — `name`, `description`, `argument-hint`, `allowed-tools`, `loads: test-philosophy roadmap-engine` — untouched; no engine edited; no `loads:` edge changed. No runnable surface, so nothing to execute; the change is prose an agent follows at runtime, and it reads unambiguously in order (number and directory given → slug chosen after reading → path assembled at the write → real path returned).

### Findings

None.

## Deferred observations

- Affects: `roadmap-test-coverage` (outside 39.1's three-sentence boundary, carried forward from plan-review-1) — The note's H1 `# <Area Name> — Test Plan` and the Layer 8 `(<area name>)` annotation still carry the spawn-time `Area:` label while the slug now names what research found; the prompt itself now says "not for the Area label above", which makes the gap between slug and title visible. Whoever next touches the template should decide whether the title follows the slug.
- Affects: unknown (carried forward from plan-review-1) — The template is spawned as an `Explore` agent; in this harness's own definition that type excludes `Write`/`Edit` (Bash remains). Pre-existing and untouched by 39.1, but 39.1 makes the agent the sole holder of the pen, so if the agent type cannot write, the returned `saved:` path is the first place the failure would surface.

REVIEW_PASS
