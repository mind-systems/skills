# Plan: 35.1 — the global CLAUDE.md says a reference addresses by name

## Context
Insert one pinned paragraph stating how a reference is *written* (by name, never by position) into `src/global/CLAUDE.md` § "Grounding claims" — the one surface every session of every project loads — then tell `tradeoxy_core`, via a handoff in its own `.ai-factory/handoffs/`, that its local `RULES.md` copy of that rule is now a duplicate it may drop.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Ground truth read for this plan
- `src/global/CLAUDE.md` § "Grounding claims" holds seven paragraphs; the fourth ends "— never invent." and the fifth begins "The opening task statement is the first artifact". Neither the section nor the file mentions a line number today; `reference-by-name` appears 0 times in the file.
- `active/CLAUDE.md` is already a symlink → `../src/global/CLAUDE.md`, so editing the source is editing what every session loads. No symlink work.
- `tradeoxy_core`'s `.ai-factory/handoffs/` is writable; its highest existing number is `45-how-a-task-is-built-and-the-defect-that-got-into-ours.md`, so **46** is the next free number, unpadded like its neighbours. Folder form is taken from files 44 and 45: `# Handoff — <slug>` title, blank line, then the mark line, then prose sections (file 43 has no mark line).
- `tradeoxy_core`'s `.ai-factory/RULES.md` carries the local rule under the heading ``## Citing `ARCHITECTURE.md` — by rule name, never by line number``, and its other rules carry position addresses: `package.json:13-14`, `src/indicators/runtime/indicator-protocol.ts:58-79`, `src/replay/__tests__/replay-indicator-replayer.spec.ts:288` and `:298`.
- **Deviation from the spec's verification, pre-existing:** `tradeoxy_core`'s working tree is already dirty before this task starts — six modified files under `.ai-factory/` (`notes/123-`, `127-`, `128-architect-buffer.md`; `specs/98-`, `99-`, `108-…`) and two untracked handoffs (`44-…`, `45-…`). The spec's check "`git status --short` shows the new handoff and nothing else" cannot hold literally; verify by delta instead (below), and leave every one of those eight pre-existing entries untouched.

## Tasks

### Insert the paragraph

- [x] **Insert the pinned paragraph into § "Grounding claims"**
  Files: `src/global/CLAUDE.md`
  Insert exactly one new paragraph immediately after the paragraph beginning "Before acting on an artifact" (the one ending "— never invent.") and immediately before the paragraph beginning "The opening task statement is the first artifact", separated by a blank line on each side like every other paragraph in the section.

  The paragraph is a **plain Markdown paragraph**, formatted exactly like its seven neighbours — no block-quote `> ` prefix, no list marker, no indentation, no fence. The pinned string, shown fenced here only so this plan does not decorate it:

  ```
  A reference addresses by **name**, never by position. A heading, a bolded rule, a symbol, a numbered item survives every insertion above it; a line number survives none, and nothing reports it when it rots. A `file:line` is a defect report against its target: the thing you needed had no name. The repair belongs there — add the name, or use the one present — never in the reference. Position addresses live in a work-order, thrown away when applied; they never enter a doc, a spec, or a roadmap line, which outlive the numbering they were written against.
  ```

  Copy that string from the task spec (`.ai-factory/specs/trickster77777/111-…`, the paragraph under § "The change") rather than retyping it or lifting it from this plan — the em dashes, the backticks around `file:line`, and the bold `**name**` are part of the pinned string, and the spec is its source. Nothing else in the file changes: no heading, no other paragraph, no link. In particular the deep home `docs/reference-by-name.md` is **not** linked — this file loads in projects that do not have it (spec § Guards).

- [x] **Verify the edit** (depends on Insert the pinned paragraph)
  Files: `src/global/CLAUDE.md`
  Read the section back whole — a whitespace-normalized read of the file, never a line-oriented `grep` count — and check by **equality, not presence**:
  - the inserted paragraph is character-for-character equal to the spec's pinned string, with no leading `> `, no leading spaces and no trailing decoration; a paragraph that merely contains the string does not pass;
  - it occurs exactly once in the file;
  - its neighbours are the two named paragraphs — the one above ends "— never invent.", the one below begins "The opening task statement is the first artifact";
  - `reference-by-name` still appears 0 times in the file;
  - `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly `src/global/CLAUDE.md` and nothing else, and `git diff` on that file shows one added paragraph plus its blank line and no other hunk.

### Tell tradeoxy_core

- [x] **Write handoff 46 into `tradeoxy_core`'s handoffs** (depends on Verify the edit — written after the paragraph is in place, so it reports what is true)
  Files: `/Users/max/projects/tradeoxy/tradeoxy_core/.ai-factory/handoffs/46-<slug>.md`
  New file in that folder's existing form: `# Handoff — <slug title>` on line 1, blank line, then the mark line verbatim and unprocessed —

  ```
  **Processed:** `[ ]` — whoever reads this marks it; a marked handoff is spent.
  ```

  The marker is `[ ]`, unprocessed — files 44 and 45, whose form this file copies, both carry `[x]` because both are spent; a handoff that lands pre-marked announces itself as already read, which is the one semantic the line exists to carry. Take the shape from them and the marker from here.

  — then the prose. Slug follows the folder's style (lowercase, hyphenated, descriptive of the subject, e.g. `the-naming-rule-is-now-always-loaded`). The prose says three things and stays inside them:
  1. The rule that a reference addresses by name and never by position is now stated in the global CLAUDE.md § "Grounding claims" — the paragraph opening "A reference addresses by **name**, never by position" — which every session of that project already loads. **Address it, do not reproduce it:** name the file, the section and that opening clause and stop there. Quoting the paragraph would put a second, unmaintained home for the fact in another repository — the fact this task exists to give one home — and the reader is an agent whose own system prompt already holds the live text, so there is nothing for a copy to save it. Naming the opening clause is itself the name-address the paragraph prescribes, and stays resolvable if the section grows.
  2. Its local rule in `.ai-factory/RULES.md` (``## Citing `ARCHITECTURE.md` — by rule name, never by line number``) is therefore a duplicate; dropping it is that repository's own work, on its own judgement and in its own time — this handoff reaches into nothing.
  3. The `file:line` citations that same `RULES.md` carries in its other rules — `package.json:13-14`, `src/indicators/runtime/indicator-protocol.ts:58-79`, `src/replay/__tests__/replay-indicator-replayer.spec.ts:288` and `:298` — are instances of the very defect the rule names, offered as an observation for that repository, not an instruction. Quoting these four literally is naming the defective citations as exhibits, which is what they are; it is not this handoff addressing anything by position.

  Do not link `docs/reference-by-name.md`: it lives only in the skills repository and this handoff is read from `tradeoxy_core`. If the write fails because the directory is not writable to the run, say so plainly in the run's output and treat the rest of the task as complete rather than failing it (spec's explicit fallback); the directory was writable when this plan was made.

- [x] **Read the written handoff back, and confirm `tradeoxy_core` is otherwise untouched** (depends on Write handoff 46)
  Files: read-only — the new handoff and the working tree of `/Users/max/projects/tradeoxy/tradeoxy_core`

  Read the file that was just written, in the same equality register the paragraph check uses:
  - the filename is numbered `46` and unpadded, and nothing else in the folder took that number;
  - line 1 is the title in the `# Handoff — <slug>` form;
  - the mark line is character-for-character equal to the pinned string above and its marker is **`[ ]`**, not `[x]`;
  - the prose names both halves the spec requires — the global paragraph, addressed as § "Grounding claims" and its opening clause "A reference addresses by **name**, never by position", and the local rule it makes redundant, addressed by its `RULES.md` heading — and it reproduces the paragraph nowhere.

  Then the untouched checks: `git -C /Users/max/projects/tradeoxy/tradeoxy_core status --short` must show the new handoff **as the only entry added by this run** — the six pre-existing modified files and the two pre-existing untracked handoffs listed under Ground truth stay exactly as they were, unmodified and uncommitted. `git -C … diff HEAD -- .ai-factory/RULES.md` must be empty (`RULES.md` byte-identical to HEAD). Nothing in that repository is committed.
