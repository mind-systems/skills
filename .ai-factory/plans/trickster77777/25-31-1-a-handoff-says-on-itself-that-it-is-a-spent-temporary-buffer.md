# Plan: 31.1 — a handoff says on itself that it is a spent, temporary buffer

## Context
`src/commands/command-handoff.md` emits handoffs that carry no record of whether they have been used, and its `description:` calls the result "a durable note" — the opposite of what a handoff is. This task makes the artifact say on itself that it is a temporary buffer spent once read, and gives the file the rule that mark carries.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The single file

All five edits below land in `src/commands/command-handoff.md` and nowhere else. `active/commands/command-handoff.md` is already a symlink to it — no symlink work. `note`, `roadmap-prune`, and every skill under `src/skills/` stay untouched; the handoffs already on disk are not backfilled.

The mark's two literal forms already exist in the corpus (`.ai-factory/handoffs/15,16,17,18`) and are reproduced byte-for-byte; no alternative wording is invented for either state:

```
**Processed:** `[ ]` — whoever reads this marks it; a marked handoff is spent.
```

with `[x]` in place of `[ ]` as the processed state.

- [x] **`description:` names the entity and its lifetime**
  Files: `src/commands/command-handoff.md`
  In the frontmatter `description:` block (lines 2–7), rewrite the closing sentence so it names what the artifact is — a temporary memory buffer that carries context from one session to the next, spent once read — and where it is persisted (`.ai-factory/handoffs/`). The word `durable` leaves the block entirely. Keep the two sentences that precede it (what the command does; run it while the session is live) as they are. State nothing about what may cite a handoff: the description says what the artifact is and stops there.

- [x] **Grid-shape template gains the mark line**
  Files: `src/commands/command-handoff.md`
  In the `~~~`-fenced skeleton under **Grid shape.** (Step 1), insert the mark line on its own line between `# Handoff — <semantic slug derived from the session subject>` and `## 1. Frame`, separated by blank lines as the surrounding skeleton spaces its blocks. Reproduce the unprocessed form byte-for-byte as given above — the backticks around `[ ]` are part of the literal. Change no section name and no other skeleton line.

- [x] **Prose-shape directive carries the identical line** (depends on the grid-shape edit)
  Files: `src/commands/command-handoff.md`
  In the **Prose shape.** paragraph, state that the file opens with the `# Handoff — <slug>` title and the mark line directly beneath it, then flows into prose. **Reproduce the unprocessed literal verbatim here** rather than pointing at the line fenced in the grid skeleton: each shape carries its own emission point, and a cross-position reference would put the byte-exactness of one shape at the mercy of the other. The consequence is deliberate — the literal, and the sentence naming the reader as the one who flips it, occur **twice** in the shipped file: once inside the grid skeleton's fence, once in this paragraph. Both are correct, and the spec's `→ each 1` counts are position-scoped (one per shape), never file-wide. It is the same literal in both places, so the corpus does not split into two forms. The rest of that paragraph (causal thread, inline references, closing next-step and working discipline) stays as written. A handoff carrying no mark is the defect this task closes, and the shape it was written in does not change that.

- [x] **Step 2's Template hook bullet exempts the mark line from the blank-skeleton rule** (depends on the two template edits)
  Files: `src/commands/command-handoff.md`
  In the **Template** bullet of Step 2, state that the mark line is literal template text — reproduced verbatim into the written file — and is exempt from the "passed **blank** / do NOT pre-fill it" rule governing the rest of the skeleton: it is not a placeholder description and nothing is mined into it. The exemption applies to both shapes. Write no claim about `note`'s internals or its own default template into this file: that would be a one-sided cross-file assertion with no counterpart declaration in `note`, which this task does not touch. In particular, `**Date:**` and `**Source:**` must not appear anywhere in the shipped file.

- [x] **The body gains the rule the mark carries** (depends on the mark line existing in both shapes)
  Files: `src/commands/command-handoff.md`
  Add a short section at the end of the file, after Step 3. **Head it as a non-numbered section addressed to the holder of a handoff file** — e.g. `## Holding a handoff` — never `## Step 4` or any other numbered heading: the file's existing `## Step N — …` headings are the stages of this command's own write path, and numbering the rule into that sequence would frame it as a fourth step of that path, which is exactly what this edit and the spec's guard forbid (nothing scans the mark; no step anywhere reads a handoff). State the rule as a property of the artifact addressed to **whoever holds a handoff file** — never as a permission granted to this command's own write path, which always produces a new numbered file through `note`. Four parts, each stated:
  1. the audience — whoever opens or holds a handoff file, not this command's write path;
  2. a processed handoff is never edited;
  3. only an unprocessed handoff is edited, and the flip is the same line with `[x]` in place of `[ ]`, nothing else changed;
  4. where a cross-project handoff is assembled in parts and the previous part is already marked processed, a new handoff is written rather than the old one extended.
  Two states and nothing else: no date, no author of the reading, no third status. Nothing scans the mark — it is prose addressed to a reader, not a protocol token, so add no step anywhere that reads it. State no rule about what may cite a handoff (`cite`, `cited` or `citation`, case-insensitive, must not appear in the file): the global CLAUDE.md § "Grounding claims" already names a handoff among the descriptions ground truth overrides, and naming that guarantee here in one sentence at the point of reliance is the most this file says on the matter.

### Verification

- [x] **Run the spec's checks** (depends on all edits above)
  Files: `src/commands/command-handoff.md`
  Take every count against a whitespace-normalized read of the file, never a line-oriented `grep`, per the spec's Verification section: mark line present between the `# Handoff` title and `## 1. Frame` with the reader-flips sentence; prose-shape directive naming both the title and the mark line beneath it, with its own verbatim copy of the literal (two file-wide occurrences of the literal and of the reader-flips sentence are the intended result — do not delete either); the Template hook's literal/verbatim exemption; `durable` gone from the `description:` block; all four parts of the body rule present under a non-numbered heading (no `## Step 4`); `**Date:**`, `**Source:**` and `roadmap-prune` at 0, and `cite`, `cited` or `citation` — case-insensitive — at 0. Then confirm `git diff HEAD -- src/skills/` is empty and `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly `src/commands/command-handoff.md` — where one of those paths was already dirty on entry, take the check against this task's own changes rather than the tree's.
