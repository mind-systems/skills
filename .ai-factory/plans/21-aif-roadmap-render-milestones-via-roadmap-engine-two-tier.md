# Plan: aif-roadmap: render milestones via roadmap-engine (two-tier)

## Context
Repoint `aif-roadmap`'s milestone output at `roadmap-engine` so high-level milestones become two-tier artifacts (contract line + spec note) instead of inline short descriptions, while preserving its sole philosophy — granularity (5–15 high-level goals, not tasks).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Carve-out (read before editing)
This is a text-move refactor, not a rewrite. **Everything stays byte-identical EXCEPT** the render/output sites listed below. Preserve verbatim (copy exact existing lines, no rewording/reordering):
- Frontmatter except `allowed-tools`
- Step 0 (Load Project Context), Step 1.1/1.2, Step 1.4, all of Mode 2 except 2.4's insert render, all of Mode 3
- Every `AskUserQuestion` block
- Critical Rule 1 and the "5–15 milestones, high-level goal not task" granularity rules
Do **not** add the Atomicity Gate or skeleton lenses; do **not** restate the roadmap/contract-line/note format locally (it is the engine's).

## Tasks

### Phase 1: Repoint render sites

- [x] **Task 1: Add `Skill` to allowed-tools**
  Files: `src/skills/aif-roadmap/SKILL.md`
  In the frontmatter `allowed-tools` line (currently `Read Write Edit Glob Grep Bash(git *) AskUserQuestion Questions`), add `Skill` so the skill can load `roadmap-engine`. No other frontmatter change.

- [x] **Task 2: Repoint Step 1.3 (Generate ROADMAP.md) output** (depends on Task 1)
  Files: `src/skills/aif-roadmap/SKILL.md`
  In Step 1.3, remove the inline ```markdown format block that renders `- [ ] **Milestone Name** — short description ...`. Replace it with engine glue: "Ensure `roadmap-engine` is loaded once this chat (via the `Skill` tool; don't re-invoke if already loaded), then produce each milestone as a two-tier artifact — a contract line plus a spec note — per its format, at coarse (strategic) granularity. The roadmap vision line is sourced from `DESCRIPTION.md` or user input (per Step 0)."
  **Orphaned-note guard (review rec 1):** write the spec notes only for the **confirmed set after Step 1.4** — mirror `roadmap-decompose`'s rule ("milestones removed or rewritten during 1.4 receive no note; only the confirmed set gets notes"). In Step 1.3, draft the contract lines with a `` Spec: `<note pending>`. `` placeholder; after 1.4 confirmation, write each confirmed milestone's note and replace the placeholder with the real `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` tag, then save `ROADMAP.md`. Do not restructure the modes — this is a glue-sentence change spanning 1.3's render instruction, keeping the 1.4 `AskUserQuestion` block verbatim.
  **Keep the "Rules for milestones:" list verbatim** (high-level goal not task, 5–15 milestones, order by dependency, mark completed `[x]`) — that is the granularity philosophy. Do not re-explain the note format or aif-note load-once; the engine owns those.

- [x] **Task 3: Repoint Step 2.4 (Add New Milestones) output** (depends on Task 2)
  Files: `src/skills/aif-roadmap/SKILL.md`
  In Step 2.4, keep "Ask user to describe new milestones" and "Insert them in logical order among existing milestones" verbatim. Change the produce/write step to: "Ensure `roadmap-engine` is loaded once this chat, then produce each new milestone as a two-tier artifact (contract line + spec note) per its format" before updating `.ai-factory/ROADMAP.md`. Mode 2.3/2.5/2.6 and Mode 3 stay untouched (they mark/reorder existing lines, they don't render new ones).

- [x] **Task 4: Delete the local "ROADMAP.md Format" section** (depends on Task 3)
  Files: `src/skills/aif-roadmap/SKILL.md`
  Remove the entire `## ROADMAP.md Format` section (the heading and its short-description ```markdown block). The format now belongs to `roadmap-engine`. Verify no other line in the file still references the removed inline format.
  **Separator note (review rec 3):** the `---` immediately before `## Critical Rules` is a valid divider between Mode 3 and Critical Rules — it is NOT orphaned by this deletion. Leave it in place; the "collapse orphaned `---`" guard is a no-op here. Only remove a separator if the deletion actually leaves two adjacent `---` or a trailing one.

### Phase 2: Upstream-sync bookkeeping

- [x] **Task 5: Move `aif-roadmap` to "never overwrite from upstream" in CLAUDE.md** (depends on Task 4)
  Files: `CLAUDE.md`
  Under "Upstream Sync": remove the `- \`aif-roadmap\` — no Completed table ...` bullet from the "**Intentionally diverged from upstream**" list. Add `aif-roadmap` to the "**Custom skills — never overwrite from upstream:**" inline list (it now depends on the local-only `roadmap-engine` and can no longer take upstream diffs).

## Regression guard
After the edits, `git diff src/skills/aif-roadmap/SKILL.md` must contain **only**: the removed inline render at Step 1.3 / Step 2.4, the removed "ROADMAP.md Format" section, the added engine glue, and the `Skill` tool addition. Any change to Critical Rule 1, the 5–15-milestones rules, modes, exploration, or any `AskUserQuestion` block is a regression — revert it.

## Commit Plan
- **Commit 1** (after tasks 1-5): "Render aif-roadmap milestones via roadmap-engine two-tier format"
