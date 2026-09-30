# Plan: 65.2 — the buffer seed states the counts rule as a decision and a producer

## Context
`src/skills/agent-architect/templates/buffer-seed.md`, under `## Method`, holds the entry **Standing entry — the counts rule.** Its wording ("Keep a contract, delete a census", "Date a measurement instead of asserting it as permanent") follows the account that `docs/counts-go-stale.md` no longer gives. This task replaces the entry's body with the text the task spec pins verbatim. The new body says a decided number stays, a measurement of the current tree goes (dated or not) with what produces it written instead, and a queued spec least of all carries such a number. The entry points to no doc. Task spec: `.ai-factory/specs/trickster77777/181-the-seed-states-the-counts-rule-as-a-decision-and-a-producer.md`. Governing spec: `docs/counts-go-stale.md` (not edited).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Rewrite the standing entry

- [x] **Replace the counts-rule entry's body in the seed**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  In `## Method`, the paragraph led by `**Standing entry — the counts rule.**` currently reads (six wrapped lines):
  ```
  **Standing entry — the counts rule.** Keep a contract, delete a census: a
  number stays in a durable artifact only where the sentence would still read
  true after someone adds a member without touching it; where it would not,
  state the rule instead of the tally. Date a measurement instead of asserting
  it as permanent. Two counts that disagree are not reconciled against each
  other — ask which member is missing.
  ```
  Replace the whole paragraph with exactly this text. The spec pins the words verbatim. The bold lead-in stays as it is. Wrap at the file's own column, no more than 78 characters per line, as below:
  ```
  **Standing entry — the counts rule.** A number someone decided is written:
  it stays true however the tree grows. A measurement of the current tree is
  not written, dated or not — write what produces it, the rule or the search
  that gives it fresh each time. A spec least of all carries a number
  measuring the tree: tasks run one after another, and each one changes the
  tree the next was written against, so such a number in a queued spec is
  false before the orchestrator reaches it, and the orchestrator cannot
  execute a spec whose facts no longer hold. Two counts that disagree are not
  reconciled against each other; ask which member is missing.
  ```
  Keep the placeholder paragraph above it in `## Method` (`<A mistake as the pattern behind it …>`), the blank lines around the entry, and every other section of the file exactly as they are. Add no link or pointer to `docs/counts-go-stale.md` or any other doc, and no tally or date. Do not touch `src/skills/agent-architect/SKILL.md`: it names the seed's path and the copy-whole rule, and it reads none of the entry's wording. Do not touch any existing architect buffer, including `.ai-factory/notes/07-architect-buffer.md` and the buffers under `.ai-factory/architects/`. A buffer founded from the old seed holds a copy of the old entry as a record, and only its head writes to it.

### Confirm the blast radius

- [x] **Re-run the spec's sweep** (depends on the task above)
  Files: none (read-only check)
  Run:
  ```
  grep -rln "census\|Date a measurement\|counts rule" src/ docs/ CLAUDE.md .ai-factory/notes
  grep -n "census\|Date a measurement\|Keep a contract" src/skills/agent-architect/templates/buffer-seed.md
  ```
  Expected: the second search returns nothing. The first search lists `src/skills/agent-architect/templates/buffer-seed.md`, which is still hit because the lead-in keeps "counts rule", and `.ai-factory/notes/07-architect-buffer.md`, whose own prose uses these words. The spec's **Finding** names both as expected, and neither needs an edit. If the search hits anything else, the tree has changed since the spec was written: report it and do not edit it.
