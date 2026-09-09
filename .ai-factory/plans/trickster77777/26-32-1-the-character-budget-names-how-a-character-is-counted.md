# Plan: 32.1 — the character budget names how a character is counted

## Context
The two character budgets in this family — `roadmap-engine`'s contract-line budget and `roadmap-outline-deep`'s phase-preamble budget — are stated in characters with no method named, so they are checked with byte-counting tools. This task gives the method one home in `roadmap-engine` and points `roadmap-outline-deep` at it; no number moves.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The method gets its home

- [x] **Add the "Counting characters" paragraph to `roadmap-engine`**
  Files: `src/skills/roadmap-engine/SKILL.md`
  Insert one paragraph immediately below the `**Rules for writing a contract line:**` bullet list (the list ends at the current line 105, `- Full current-state / target / guards / verify detail lives in the task spec, not the contract line`), separated from that last bullet by exactly one blank line, and followed by one blank line before the existing `**Numbering rules:**` block. It is a paragraph under the list — never an eighth bullet, never a lazy continuation of the bullet above. Its text, verbatim from the task spec:

  `**Counting characters:** every character budget in these skills — the contract-line budget above, and the phase-preamble budget in `roadmap-outline-deep` — counts Unicode code points with the trailing newline excluded. The command that yields them here is `python3 -c "import sys;print(len(sys.stdin.read().rstrip('\n')))"`.`

  (The backtick-fenced spans in that sentence — `` `roadmap-outline-deep` `` and the command — are part of the paragraph; the outer backticks above are quoting only.)

  Constraints, all load-bearing:
  - **Do not edit any of the seven bullets** of the rule list. `Target ~600 characters (range 400–1000)` and its neighbours stay byte-identical to HEAD.
  - **Do not use the word `family`** in this paragraph. That word is already spent ten lines below, in the numbering rules (`the family prefix`, `family references`), for the task-number family; the engine names no family of its own. The paragraph states its scope by naming the two budgets it governs.
  - The command's `'\n'` and `"` must land literally in the file. If writing through a shell heredoc, quote the delimiter (`<<'EOF'`) so nothing expands; otherwise use `Edit`. Verify afterwards by piping the file's own bytes, not by eye.
  - Do not touch the `description:` frontmatter of this file — its `~600-char` mention carries the vocabulary, not the rule.

- [x] **Point `roadmap-outline-deep`'s Budget bullet at that home** (depends on the paragraph existing in the engine)
  Files: `src/skills/roadmap-outline-deep/SKILL.md`
  In the **Budget** bullet of § "Step 2: Compress the preamble and attach the pointer" (currently starting `- **Budget** — rewrite the phase preamble down to **~200–500 characters**`), add a sentence naming the method's home by address: `roadmap-engine`'s "Roadmap File Format" § "Counting characters". Write it in the shape this same file already uses one section above, in the Destination-directory bullet of Step 1 — engine named, its place named in quotes, restatement explicitly refused:

  > This is `roadmap-engine`'s "Named roadmaps" § "Spec destination" routed through `note`'s destination hook — do not restate its mechanics here, and never introduce a new directory.

  Constraints:
  - **`~200–500` does not change**, and the rest of the bullet — the `Phase note:` pointer, the "short distillation, not a home for whatever the preamble sheds" prose — stays as it is.
  - **Neither the method nor the command is restated here.** The words `code point` must not appear in this file, and the `python3 …` command must not appear in this file. Naming the address and then explaining what it says would give the method a second home while still reading correctly — that is the failure mode this bullet exists to avoid.
  - `loads: roadmap-engine note` is already declared on this file — add no `loads:` edge, no tool grant, no new skill.

### Confirm the shape

- [x] **Verify against the file, not the diff** (depends on both edits)
  Files: `src/skills/roadmap-engine/SKILL.md`, `src/skills/roadmap-outline-deep/SKILL.md`
  Take every count below against a whitespace-normalized read of the named file — never a line-oriented `grep`, which will miss a paragraph that wrapped differently than expected. Per the task spec's Verification section:
  - the seven bullets of `**Rules for writing a contract line:**` are byte-identical to HEAD, and `family` in `roadmap-engine/SKILL.md` is unchanged from HEAD — the paragraph adds neither a bullet nor that word;
  - `Target ~600 characters (range 400–1000)` occurs exactly once in the engine;
  - across the whole of `roadmap-outline-deep/SKILL.md`: the pinned command → 0 occurrences, `code point` → 0 occurrences;
  - `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` lists exactly these two files and nothing else. `active/skills/roadmap-engine` and `active/skills/roadmap-outline-deep` are symlinks into `src/skills/`, so both edits are already live in the working set — do not write anything under `active/`.
  - No count above is trusted as evidence until it was taken by the normalized method named at the head of this list.
