# Plan: 66.4 — the counts entry opens with its scope

## Context
In `src/skills/agent-architect/templates/buffer-seed.md`, under `## Method`, the entry **Standing entry — the counts rule.** opens with "A number someone decided is written…". Because it states no scope, it reads as a ban on numbers anywhere, including plain conversation. The reason the entry itself gives covers only text that someone reads later and cannot ask back about. `docs/counts-go-stale.md` already scopes the rule to "a number in a durable artifact". The phase's governing spec is `docs/paired-loop.md`, which makes the seed the home of the pair's base behaviour. This task adds one opening sentence that gives the entry that scope. The spec `.ai-factory/specs/trickster77777/189-the-counts-entry-opens-with-its-scope.md` pins the sentence and the full entry verbatim.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Seed text

- [x] **Open the counts entry with its scope sentence**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  Under `## Method`, find the paragraph that begins **Standing entry — the counts rule.** It ends with "ask which member is missing." and comes just before **Standing entry — what a spec holds.** Keep the bold lead-in exactly as it is. Directly after the lead-in, before "A number someone decided is written:", insert this sentence verbatim:
  "It governs what is read later by someone who cannot ask back — a spec, a plan, a roadmap line, this buffer after a compact; in conversation a number or a position is fine, since a wrong one costs one reply."
  The rest of the entry stays word for word as it is. Only the line breaks move.

  Re-wrap the whole paragraph to the file's own column: no line may be longer than 76 characters, which is the widest line in the current `## Method` section. Count characters, not bytes. Each em dash is one character but takes three bytes, so a byte count such as `awk length` reports lines as too wide. Do not start any line with an em dash. This wrapping meets both conditions, and you can use it as is:

  ```
  **Standing entry — the counts rule.** It governs what is read later by
  someone who cannot ask back — a spec, a plan, a roadmap line, this buffer
  after a compact; in conversation a number or a position is fine, since a
  wrong one costs one reply. A number someone decided is written: it stays
  true however the tree grows. A measurement of the current tree is not
  written, dated or not — write what produces it, the rule or the search that
  gives it fresh each time. A spec least of all carries a number measuring the
  tree: tasks run one after another, and each one changes the tree the next
  was written against, so such a number in a queued spec is false before the
  orchestrator reaches it, and the orchestrator cannot execute a spec whose
  facts no longer hold. A number met in a spec, a plan or a report is read as
  an order of magnitude; one that has gone stale is not a defect to correct,
  count again or stop on. Two counts that disagree are not reconciled against
  each other; ask which member is missing.
  ```

  Verify the edit in two ways. First, join the paragraph's lines with single spaces; the result must equal the quoted entry in the spec § "What must be true after", character for character. Second, measure the line widths in characters, for example with `python3` and `len()` on decoded text; the widest line must be no more than 76. Keep the blank lines before and after the paragraph. Do not change any other entry, heading, or the seed's opening passage.

### Blast radius

- [x] **Confirm nothing else needs to change** (depends on Open the counts entry with its scope sentence)
  Files: none (verification only)
  Run the sweep from the spec § "What breaks on contact":
  `grep -rn "counts rule" src/ docs/ CLAUDE.md`, `grep -rn "durable artifact" src/ docs/ CLAUDE.md`, `grep -rn "measurement of the current tree" src/ docs/ CLAUDE.md`.
  Expected hits:
  - The entry itself, which is the target of this task.
  - `docs/counts-go-stale.md` and the `CLAUDE.md` index row that describes it. Both scope the rule to "a number in a durable artifact" and already agree with the new opening, so they stay unchanged.
  - In the pinned wrap, "counts rule" and "measurement of the current tree" each still sit whole on one line ("…true however the tree grows. A measurement of the current tree is not"), so the sweep gives the same hits before and after the edit.

  If the sweep finds any other text that states the counts rule with no scope, or that depends on the entry's old opening wording, stop and report it. Do not edit any file outside `src/skills/agent-architect/templates/buffer-seed.md`.
