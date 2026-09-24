# Plan: 61.1 — the repair is a mood, not a mechanism

## Context
`src/commands/command-pin-gaps.md` contradicts itself. Its **Blast-radius holes** Repair sentence defines the invariant as something "every match must satisfy after the change". That is an instruction to a later run, and **What the pass never writes** in the same file forbids exactly that. This task rewrites the invariant clause so it is a recorded finding: what the sweep, run now, reaches. The note `.ai-factory/specs/trickster77777/138-four-witnesses-each-trusted-where-it-is-blind.md` quotes the Repair sentence as live grounding in its Q4 paragraph, so its quote changes in the same stroke. The task spec is `.ai-factory/specs/trickster77777/168-the-repair-is-a-mood-not-a-mechanism.md`, and its § "What must be true after" pins both new wordings. The governing spec is `docs/what-a-task-carries.md`: a spec states what must be true, never a check.

Ground truth checked before planning:
- In `command-pin-gaps.md`, the **Blast-radius holes** paragraph is one unwrapped line starting `**Blast-radius holes:** what the repository already contains`. The file writes every paragraph on a single line.
- The Q4 paragraph in `138-…md` is also one unwrapped line. It starts `Q4 needs no new class.`
- The task spec quotes both passages hard-wrapped with `> ` prefixes. That wrapping belongs to the quote, not to the target files.
- The text being replaced is the same in both files, and so is its replacement. The only difference is how the passage ends: `command-pin-gaps.md` ends it with `.`, while `138-…md` ends it with `"` because the passage sits inside a quotation.

Assumption: the spec's wrapped blocks are inserted in the target files' own form, as single lines. Each line break in the spec's blocks becomes one space. The words, punctuation, bold markers, and backticks do not change.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the invariant as a recorded finding

- [x] **Replace the invariant clause in the Blast-radius holes Repair sentence**
  Files: `src/commands/command-pin-gaps.md`
  Inside the single-line **Blast-radius holes** paragraph, replace this exact substring:
  ```
  the **invariant** every match must satisfy after the change — naming, at minimum, the task's own target as a result the sweep must return, so an empty result reads as a broken pattern rather than a clean repository — never the sweep's own enumeration of what it found.
  ```
  with:
  ```
  the **invariant** — a recorded finding of what the sweep, run now, reaches and how each match reads against the rule, naming at minimum the task's own target among what it finds, so a reader can tell a genuinely narrow set from a broken pattern — never an instruction for a later run to confirm, never the sweep's own enumeration of what it found.
  ```
  This is the spec's replacement Repair sentence with its line breaks turned into spaces. Keep the paragraph on one line.
  Leave everything else in the paragraph word-identical: the opening definition sentence, the Repair sentence up to and including `**sweep** that finds it on demand, and `, the sentence about contradictions and blockers, and the closing sentence about a sweep too large to enumerate. Leave **What the pass never writes**, the `**default:**` line (it still reads "rule-sweep-invariant"), the **The shape it repairs toward** paragraph, and every other paragraph in the file untouched.

- [x] **Update the live quote in note 138's Q4 paragraph** (depends on Replace the invariant clause in the Blast-radius holes Repair sentence)
  Files: `.ai-factory/specs/trickster77777/138-four-witnesses-each-trusted-where-it-is-blind.md`
  Inside the single-line paragraph that starts `Q4 needs no new class.`, replace this exact substring:
  ```
  the **invariant** every match must satisfy after the change — naming, at minimum, the task's own target as a result the sweep must return, so an empty result reads as a broken pattern rather than a clean repository — never the sweep's own enumeration of what it found"
  ```
  with:
  ```
  the **invariant** — a recorded finding of what the sweep, run now, reaches and how each match reads against the rule, naming at minimum the task's own target among what it finds, so a reader can tell a genuinely narrow set from a broken pattern — never an instruction for a later run to confirm, never the sweep's own enumeration of what it found"
  ```
  After this edit the quote matches the new Repair sentence character for character, apart from the closing `"`. The rest of the paragraph does not change: its opening, the text from `— one clause is owed to it` onward, and its argument about declarations versus readers. The paragraph stays on one line. Leave every other paragraph of the note untouched.

  Leave these untouched: the other files that still contain "must satisfy after the change" are records of a past moment, as the task spec's § "What breaks on contact" explains. They are the phase notes `150-…md` and `169-…md`, the landed task spec `154-…md`, the 56.1 plan and plan-review, handoff `27-…md`, this task's own spec `168-…md`, and the roadmap's contract line.
