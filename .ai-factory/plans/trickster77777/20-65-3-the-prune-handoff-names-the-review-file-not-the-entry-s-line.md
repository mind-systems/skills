# Plan: 65.3 — the prune handoff names the review file, not the entry's line

## Context
`src/skills/roadmap-prune/SKILL.md` § "Step 0 — Deferred-observations gate" has an item, "If any unpinned entry exists → stop the skill entirely", that names a resolution. Its first part has the `/command-handoff` handoff carry the "`file:line` of the entry". A later resolution session reads that handoff after the review file may have changed, so the line would point at the wrong place. `docs/reference-by-name.md` calls that form a defect. This task swaps that field for the review file the entry sits in. The review file plus the entry's original reviewer text is enough to find the entry. Task spec: `.ai-factory/specs/trickster77777/182-the-prune-handoff-names-the-review-file-not-the-entrys-line.md`. Governing specs: `docs/reference-by-name.md` and `docs/counts-go-stale.md` (neither is edited).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the handoff field list

- [x] **Replace the handoff part of the resolution in the Step 0 gate item**
  Files: `src/skills/roadmap-prune/SKILL.md`
  In § "Step 0 — Deferred-observations gate", find the item led by `4. If any unpinned entry exists → stop the skill entirely`. Its nested resolution list opens with part `1.`, which currently reads (three wrapped lines, indented 3 spaces for the number and 6 for continuation lines):
  ```
     1. the user runs `/command-handoff` on this session — the handoff carries every
        unpinned observation (gist, original reviewer text, `Affects:`, `file:line` of
        the entry) plus the gate context into `.ai-factory/handoffs/`;
  ```
  Replace it with exactly this. The sentence is pinned verbatim by the spec. Keep the indentation and the file's wrap column, which is about 88 characters here:
  ```
     1. the user runs `/command-handoff` on this session — the handoff carries every
        unpinned observation (gist, original reviewer text, `Affects:`, the review file
        the entry sits in) plus the gate context into `.ai-factory/handoffs/`;
  ```
  Nothing else in the file changes. In particular, leave these alone:
  - The chat line this item prints just before the resolution, `<file>:<line> — <entry text>`. It stays exactly as it is.
  - Parts `2.` and `3.` of the resolution, and the "Make no edits…" sentence.
  - Items 1–3 and 5–6 of Step 0.
  - The other `<file>:<line> — <matched text>` echoes elsewhere in the skill, in the plan-layer citation scan and the summary report. They are chat output that no handoff carries.

  Do not touch `src/commands/command-handoff.md`, because it reads no field list from this item. Do not touch `orchestrator-artifacts`, whose dedup rule reads no line.

### Confirm the blast radius

- [x] **Re-run the spec's sweep** (depends on the task above)
  Files: none (read-only check)
  Run:
  ```
  grep -rn "unpinned" src/ docs/ CLAUDE.md
  grep -rn "command-handoff" src/ docs/ CLAUDE.md
  grep -n "file:line" src/skills/roadmap-prune/SKILL.md
  ```
  Expected:
  - The third search returns nothing. The `<file>:<line>` chat-line form is spelled differently and does not match it.
  - The stop condition is the spec's **Rule**, not whether a hit is on the list below. A hit breaks only if it names what the handoff carries for each unpinned entry, or reads an entry's line from a handoff. Among the hits, only the edited part `1.` of item 4 in `roadmap-prune` names that field list, and after the edit it names the review file. If some other hit does either of these, report it and do not edit it.
  - For reference, the tree currently returns these hits. The first search (`unpinned`) finds:
    - `src/skills/roadmap-prune/SKILL.md` Step 0: item 2 (the repo-wide scan), item 4 (the gate line and the edited part `1.`), and item 5 (none unpinned → proceed). None of them reads a line from a handoff.
    - `docs/reserved-words.md`: the definition of deferred observations. It names no line.
    - `src/commands/command-pin-gaps.md`, two lines. There "unpinned" refers to value holes, which is unrelated.
    - `docs/test-coverage-pass.md` (the heading "Grouping is left unpinned, on purpose") and the matching index row in `CLAUDE.md`. Both are about grouping, which is unrelated.
  - The second search (`command-handoff`) finds:
    - `src/skills/roadmap-prune/SKILL.md` Step 0 item 4, part `1.`. This is the edited line.
    - `src/skills/agent-architect/SKILL.md`: the passage that names the handoff as a different genre. It names no field list.
    - `docs/sakshi-harness/skill-cycle.md`, two lines: the gate description and the diagram arrow. Neither names a line.
    - `docs/sakshi-harness/skill-graph.md`: the funnel into `note`, which is unrelated.
  - `src/commands/command-handoff.md` does not contain its own name, so neither search reaches it. It mines the session for meaning and reads no field list from `roadmap-prune`, so it needs no edit.
  - None of these hits needs an edit. A mismatch between this list and the actual output is not a reason to stop. Only a hit that meets the Rule is.
