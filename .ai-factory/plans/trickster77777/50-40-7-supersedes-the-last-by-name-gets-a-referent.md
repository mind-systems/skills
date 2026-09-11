# Plan: 40.7 — "supersedes the last by name" gets a referent

## Context
`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" states "Each new snapshot supersedes the last by name, so a reader never follows a stale next action" and gives "by name" nothing to resolve against. This task adds the one missing referent — the comparison rule: the numerically higher-numbered snapshot is the current one — and nothing else. One file, one sentence.

Grounding read fresh (per spec `.ai-factory/specs/trickster77777/134-supersedes-the-last-by-name-gets-a-referent.md`, governing spec `docs/paired-loop.md` § on the memory snapshot):
- The target sentence sits in the memory-snapshot paragraph of § "Spawn once, message thereafter" (the paragraph opening "The memory snapshot continuing this same architect has two occasions"). It is the only "supersede" in the file.
- The referent is `note`'s own folder-style step (`src/skills/note/SKILL.md`, the **Folder style** paragraph): "'Most recent (highest-numbered)' is decided over the parsed integer, not the string — the 1–2 siblings with the numerically highest prefixes, so a name with a longer prefix outranks any shorter-prefixed one". `command-handoff.md` delegates a snapshot's numbering and write to `note` ("`note` performs its own numbering, directory creation, and file write"). These two files own the mechanism (how the number is produced, where the file lands, that each write is a new numbered file) and are not edited.
- `docs/paired-loop.md` already states a snapshot "carries a pointer to the buffer's place, never a copy of what the buffer holds" without naming where the snapshot itself lives; this task does not change that and does not touch the governing spec.
- 40.6 (already `[x]`) edited the spawn and respawn sentences in the same section and explicitly left this paragraph to 40.7; the file is 370 lines, under the 500-line body limit.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Add the comparison rule

- [x] **Give "supersedes the last by name" its referent in the memory-snapshot paragraph**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", the memory-snapshot paragraph, the sentence "Each new snapshot supersedes the last by name, so a reader never follows a stale next action." Rewrite it so the "by name" clause states the comparison rule and only that: the numerically higher-numbered snapshot is the current one (e.g. "Each new snapshot supersedes the last by name — the numerically higher-numbered one is the current one — so a reader never follows a stale next action."). Constraints, all from the spec:
  - Keep the sentence's opening ("Each new snapshot supersedes the last by name") and its reason clause ("so a reader never follows a stale next action") intact in meaning; only the referent is inserted.
  - State it as a comparison rule, not a mechanism: say *numerically higher-numbered*, so a reader knows the comparison is over the integer, not the string — but do not describe how the number is produced (`note`'s scan-and-add-one), where the snapshot lands (`command-handoff`'s `<root>/.ai-factory/handoffs/`), or whether an old one is overwritten (it is not; each is a new numbered file). None of these ride with the clause.
  - No cross-reference or pointer to `note`, `command-handoff`, or task 38.1 is added in the sentence; the file already names `command-handoff`/`note` elsewhere only where it must, and the spec asks for the rule alone.
  - Every other sentence in the paragraph — the two occasions, the on-request capability, what is recorded, the volatile-residue description, "Of the recorded state, only the buffer's path travels…" — stays byte-identical.
  - Keep the file's hard-wrapped prose style (re-flow only the lines of the edited sentence as needed; do not re-wrap neighboring sentences).

### Guard

- [x] **Confirm the edit boundary held** (depends on the task above)
  Files: `src/skills/agent-architect/SKILL.md`
  Run `git diff` and confirm: exactly one hunk, confined to the memory-snapshot paragraph of § "Spawn once, message thereafter"; the added text contains no mention of `handoffs/`, `notes/`, `mkdir`, "zero-padded", "add 1", "overwrit", or "38.1"; `src/commands/command-handoff.md`, `src/skills/note/SKILL.md`, `src/agents/editor.md`, `src/skills/architect-editor-engine/SKILL.md`, and `docs/paired-loop.md` are untouched; the frontmatter is unchanged; the body stays ≤ 500 lines.
