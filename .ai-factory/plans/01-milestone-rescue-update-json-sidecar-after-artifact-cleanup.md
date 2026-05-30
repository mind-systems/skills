# Plan: milestone-rescue — update JSON sidecar after artifact cleanup

## Context
Extend the `milestone-rescue` skill so that after deleting stale plan-review/review artifacts in Step 5, it also rewrites the `step` key in the orchestrator's `plans/{seq}-{slug}.json` sidecar to reflect what actually remains on disk — preventing the next orchestrator run from resuming against a deleted file.

## Design decisions (from plan-review-1)
- **Tool-agnostic prose, not Python-prescribed.** The rest of `SKILL.md` is written in tool-agnostic language ("use Edit to modify…", "use `git status --short` …"). The sidecar sub-step will match that style: "parse it as JSON" / "serialize it back as JSON with 2-space indentation", not `json.load` / `json.dump`. The mapping table is still copied verbatim (the source note demands it), but surrounding prose is rewritten.
- **`allowed-tools` gains only `Write`.** Because the prose is tool-agnostic, the agent reads the sidecar with `Read` (already granted) and writes it back with `Write` (new). No Python permission is needed.
- **"Existence" means working tree.** Consistent with the deletion block (which uses `git clean -f` / `git rm -f` on working-tree paths), the agent checks for the sidecar by listing/reading the working-tree path.
- **Positioning.** The new sub-step lives at the tail of Step 5, after the artifact deletion block, before the final "Show the user the list of deleted files…" confirmation, and therefore before Step 5.5.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Frontmatter

- [x] **Task 0: Add `Write` to `allowed-tools` in `milestone-rescue/SKILL.md`**
  Files: `.claude/skills/milestone-rescue/SKILL.md`
  Current line 11:
  ```yaml
  allowed-tools: Read Edit Glob Grep Bash(git *) AskUserQuestion
  ```
  Change to:
  ```yaml
  allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion
  ```
  Insert `Write` immediately after `Read` to keep related tools adjacent. Do not add any Bash subcommand grant — the new sub-step is tool-agnostic and does not need Python.
  Do not change any other frontmatter field.

### Phase 2: Skill body update

- [x] **Task 1: Add sidecar-update sub-step at the tail of Step 5 of `milestone-rescue/SKILL.md`** (depends on Task 0)
  Files: `.claude/skills/milestone-rescue/SKILL.md`
  Insert a new sub-step **after** the artifact deletion block (the `Files marked '??' → git clean ...` / `Files marked 'A ' → git rm ...` block and the "Do NOT delete committed files…" paragraph that follows it), and **before** the final `Show the user the list of deleted files and confirm the rescue is complete.` line. This places it inside Step 5 and therefore **before** Step 5.5 (Propagate findings to open milestones) — do not insert it after Step 5.5 or at the top of Step 5.

  The new sub-step must:

  1. Open with a bolded title in the same style as `**Clean up artifacts.**`, e.g. `**Update the sidecar.**`
  2. State the sidecar path: under `.ai-factory/plans/`, named `{seq}-{slug}.json` using the same `<NN>-<slug>` prefix identified in Step 1. Tell the agent to check the working tree for the file (consistent with the working-tree-only deletion block above) — for example by attempting to read it, or listing with `Glob`.
  3. Instruct the agent in tool-agnostic prose: "If the file exists, read it and parse it as JSON. If it does not exist, start from an empty JSON object." Do **not** use the words `json.load` or `json.dump` — they prescribe Python and depart from the rest of the skill's style.
  4. Instruct the agent to inspect what plan-review and review files for this slug remain on disk **after** the cleanup deletions, and decide the correct `step` value using the mapping table below.
  5. **Include the mapping table verbatim** (do not paraphrase) — copy it exactly from `.ai-factory/notes/08-milestone-rescue-sidecar-update.md`:

     | Situation after cleanup | Write `step` |
     |---|---|
     | Plan-reviews deleted (or none pass) | `"planned"` |
     | Plan-reviews exist and pass, reviews deleted | `"plan_reviewed"` |
     | Plan-reviews pass, reviews exist but none pass | `"plan_reviewed"` (re-implement) |
     | Sidecar doesn't exist | create it with correct `step` |

  6. **Immediately after the table**, add a one-sentence clarification for the recursive last row: "When the sidecar does not exist, determine `step` from the first three rows (the on-disk state of plan-reviews and reviews), then create a new sidecar file containing only that key — e.g. `{ "step": "planned" }`." This prevents an agent from writing the literal string `"create it with correct step"` or getting stuck on the recursion.
  7. Instruct the agent to write **only** the `step` key back. Preserve every other key already present in the sidecar (`planner`, `implementer`, `elapsed`, and any other unrelated keys) untouched. Tool-agnostic phrasing: "serialize the result back as JSON with 2-space indentation and write it to the sidecar path using `Write`." Do not mention `json.dump`.
  8. Explicitly forbid touching `planner` / `implementer` / `elapsed`. (This duplicates the bullet added in Task 2 by design — defense in depth: the in-flow reminder catches the agent while it's editing the file, the "What NOT to do" bullet catches the agent reviewing constraints up-front.)
  9. Add a fall-through case sentence: "If both plan-reviews and reviews pass on disk, the orchestrator finished — surface this to the user and skip the sidecar update." This covers manual invocations of rescue against a still-green pipeline; the mapping table does not address it.
  10. End with a user-visible confirmation line in the exact form: `Sidecar updated: step set to "{value}"` (skip emitting this when the fall-through case above applies).

  Match the existing prose style of Step 5 (short imperative sentences, bullet lists where appropriate). Do not alter any other Step 5 content. Do not bump section numbering — this is a sub-step inside Step 5, not a new top-level step. Do not modify Step 5.5.

- [x] **Task 2: Extend the "What NOT to do" section** (depends on Task 1)
  Files: `.claude/skills/milestone-rescue/SKILL.md`
  Add one bullet to the existing `## What NOT to do` list at the bottom of the file:
  - Do not overwrite `planner`, `implementer`, or `elapsed` in the sidecar — only the `step` key is updated by this skill.

  Keep the bullet phrased in the same imperative voice as the surrounding bullets. Do not reorder existing bullets. This duplicates the in-flow forbiddance from Task 1 instruction 8 intentionally (see rationale there).
