# Plan: 56.2 — the task-spec-shape root stops feeding the census instruction downstream

## Context
`roadmap-engine/SKILL.md`'s "What a task spec holds" paragraph is the root definition `command-pin-gaps` names for the task-spec shape and does not restate; its third clause orders *what breaks on contact* "enumerated rather than hedged" — the census `docs/counts-go-stale.md` rules out. This task replaces one word in that clause with the verb the family already uses for stating a fact precisely, leaving everything eight callers reach by name byte-identical.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The root clause

- [x] **Reword the third clause of "What a task spec holds"**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Line 49 currently reads `*what breaks on contact*, enumerated rather than hedged.` and is the file's only occurrence of `enumerat` (verified by grep). Replace the single word `enumerated` with `pinned`, so the clause reads `*what breaks on contact*, pinned rather than hedged.` — the final paragraph text becomes exactly what spec `155-…` § "The change" quotes. Nothing else on the line changes: the italic span `*what breaks on contact*`, the comma, `rather than hedged.` and the trailing period stay as they are. The paragraph is hard-wrapped at ~80 columns and `pinned` is shorter than `enumerated`, so no rewrap of lines 46–49 is needed or wanted — leave the existing line breaks exactly where they are.
  Byte-identical, per the spec's untouched list: the bold heading `**What a task spec holds:**` (`command-pin-gaps.md` line 36 cites this heading by name and it must keep resolving); the first two clauses (`*what is true now*, read from the code with exact values, so the implementer does not re-derive it` and `*what must be true after*, in the code's own terms: which file, which text, which value`); the `**Why two tiers:**` paragraph immediately above (lines 42–44); the `**Never write a full spec inline in the roadmap**` sentence immediately below (lines 51–52); every other section of the file, including frontmatter and the `loads:`/reverse-graph lines. No other file is edited by this task.

- [x] **Verify the blast-radius invariant** (depends on Reword the third clause of "What a task spec holds")
  Files: `src/skills/roadmap-engine/SKILL.md`
  Run the spec's own re-runnable sweep from the repo root:
  `grep -rln "What a task spec holds\|enumerated rather than hedged" src/ docs/ .ai-factory/`
  Check the results against two rules, not against a list of expected paths — the set of matches grows as this task's own run artifacts land, and a fixed tally would be false before the task closes.
  **The heading still resolves.** `src/skills/roadmap-engine/SKILL.md` and `src/commands/command-pin-gaps.md` both still match on the heading text, and the heading in the engine is unchanged: `git diff` on the engine shows exactly one changed line, whose only difference is `enumerated` → `pinned`.
  **No file claims the old wording is current.** Every remaining match quotes `enumerated rather than hedged` either as the problem it describes or as the record of a past moment — this task's spec and its roadmap contract line, phase 56's note `150-…`, handoff `27-…`, and the run artifacts of phase 56 including this plan file itself and the reviews of this very task — never as a statement of what the engine says now. The engine is the only file that had to change, and it drops out of this half of the sweep. A match that fails this rule is a real finding; a match that satisfies it is not a collision, however many of them there are.
  Do not touch `src/commands/command-pin-gaps.md`. Its line 36 ("a blast-radius hole by enumerating *what breaks on contact*") and line 38 ("it pins values and enumerates breakage") still say "enumerating" after this change; spec `154-…` pins every other line of that file as untouched and spec `155-…` scopes this task to the engine paragraph alone. The residue is already recorded as a deferred observation on 56.1's reviews and belongs to a follow-up task, not to this one.
