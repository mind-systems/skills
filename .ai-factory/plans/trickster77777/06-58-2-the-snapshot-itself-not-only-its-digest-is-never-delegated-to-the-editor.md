# Plan: 58.2 — the snapshot itself, not only its digest, is never delegated to the editor

## Context
`src/skills/agent-architect/SKILL.md` forbids sending the snapshot's *digest* to the editor but says nothing about the snapshot file itself, while a later sentence in the same file describes what the `APPLY-EDIT` channel carries with no such exclusion — so a reader arriving at that later sentence finds nothing forbidding an apply work-order for the snapshot. Two sentences in the same file gain the missing exclusion, on the ground `docs/paired-loop.md` § "How the memory begins, and how it survives" already states: the conversation is the surface a snapshot reports on, and only the head that held it can write about it.

Both replacement sentences are pinned word for word in `.ai-factory/specs/trickster77777/160-the-snapshot-itself-is-never-delegated.md` § "What must be true after". They are copied, never re-derived — a paraphrase is a defect, not a variant.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The edit

- [x] **Extend the digest sentence with the snapshot-delegation prohibition**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", the memory-snapshot paragraph holds a sentence ending `the digest is your own recovery note and is never sent to the editor.` (around line 72 — locate it by matching that text, never by the number). Append a clause so the sentence reads, per the task spec's `## What must be true after`: `…the digest is your own recovery note and is never sent to the editor, and for the same reason the snapshot itself is never delegated to the editor to compose — the conversation is the surface a snapshot reports on, and only the head that held it can write what happened there.` The phrase "digest is your own recovery note" must survive verbatim — other artifacts' sweeps key on it. Keep the backticked `architect-editor-engine` reference in the sentence's first half intact.
  Nothing else in this paragraph changes: the two sentences that open it ("The memory snapshot continuing this same architect has two occasions…" and "The on-request one is the architect's own capability…") are 58.4's anchors, and the "What a snapshot carries is the volatile residue…", thickness, and supersession sentences are 58.1's landed work — all stay word-identical.
  Re-wrap the edited sentence to match the width the surrounding paragraph already uses.

- [x] **Close the same door in the channel-contents sentence** (depends on the previous task)
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Relay on the marker; author the apply work-order and your own legwork", the paragraph beginning "The two channel-message formats govern what opens a round…" ends with a sentence reading `A REPORT-ONLY message carries either the before-mark payload, worked in parallel and enriched only with named context, or your own delegated legwork; the APPLY-EDIT channel carries the apply work-order alone, and it **never** carries your own analysis of an analysis target.` (around line 270 — again, match on the text). Append the clause given in the task spec, so the sentence ends: `…and it **never** carries your own analysis of an analysis target — nor, ever, the memory snapshot: composing that file is forbidden to the editor outright, not merely absent from this channel's ordinary cases (see "Spawn once, message thereafter").`
  Preserve the existing inline formatting exactly as it stands in the file: `` `REPORT-ONLY` `` and `` `APPLY-EDIT` `` stay backticked (the quotation above collapses them for readability only), and `**never**` keeps its emphasis. The cross-reference names the section by its heading text, in the quoted-heading style the file already uses — `(see "Nothing closes a round before the report on it exists")` appears in this same section — never a line number.
  Re-wrap to match the width the surrounding paragraph already uses, as task 1 does. The appended clause is long and the sentence's last line is short (it ends the paragraph on `an analysis target.`), so running the clause onto that line would produce a line far wider than the paragraph's own width — wrap the clause across new lines instead.
  No other sentence in this section changes. In particular the "the text is written by the editor, who has the file open" sentence that opens the apply-work-order paragraph stays untouched — the spec's reasoning is that it describes composing an `APPLY-EDIT` in general and the exclusion added here closes the door later in the same section.

### Verification

- [x] **Compare both edited sentences against the spec's pinned wording, word for word** (depends on both edits)
  Files: none — read-only check
  Read the two edited sentences back off disk and set each beside its blockquote in `.ai-factory/specs/trickster77777/160-…md` § "What must be true after". Compare **words and order only, newlines collapsed to spaces** — both paragraphs are hard-wrapped and were re-wrapped by this task, so the comparison is never of lines.
  This is the positive half of verification, and the sweeps below cannot stand in for it: they prove survival and scope, both of which a paraphrase of either appended clause would also satisfy. Check, in order:
  - **The digest sentence** ends with the full appended clause, including "the conversation is the surface a snapshot reports on, and only the head that held it can write what happened there."
  - **The channel-contents sentence** ends with the full appended clause, including "not merely absent from this channel's ordinary cases (see \"Spawn once, message thereafter\")."
  - **That same sentence keeps its inline formatting**: `REPORT-ONLY` and `APPLY-EDIT` are backticked and `never` is bolded, exactly as they stood before the edit. The word-and-order comparison is blind to this by construction, and the spec's blockquote renders both tokens without backticks — the spec is the authority on the words, the file on the markup. Dropped backticks here are a defect to restore.
  - **The neighbours are word-identical to what they were before this task**: in § "Spawn once, message thereafter", the two sentences opening the paragraph and 58.1's three sentences following it; in § "Relay on the marker…", every other sentence of that paragraph and the "the text is written by the editor, who has the file open" sentence. Only their line breaks may differ.
  A mismatch in the first two is a defect in this task's own edits — fix it against the spec. A mismatch in the third is a neighbour that was disturbed and must be restored to its prior wording.

- [x] **Re-run the spec's first sweep and classify every hit by rule** (depends on the comparison above)
  Files: none — read-only check
  ```
  grep -rln "digest is your own recovery note" src/ docs/ .ai-factory/
  ```
  **The one path that must still appear is `src/skills/agent-architect/SKILL.md`** — this edit appends to the phrase rather than replacing it, so its disappearance would mean the anchor was rewritten and the sentence must be restored.
  Everything else the sweep returns is a hit by design and **the count is not the test** — it grows with every artifact this task produces. Judge each returned path by the rule, never by a list: *does this file quote the digest passage as ground truth for a standing claim about the present?*
  - This task's own spec (`160-…md`) and the phase note (`152-…md`) record the pre-task wording as the state they describe — a spec and a note describe a moment, not the present. Correct as they are.
  - The roadmap's own contract line for this task states the problem it describes, permanently. Correct as it is.
  - This plan file, the sibling plan `05-…md`, and any plan-review or review artifact of this task quote the phrase and the sweep command self-referentially rather than asserting them as live claims. Runtime working communication, not findings.
  - A path that is none of the above **and** quotes the passage as a live claim: stop and report it, do not edit it. The spec's blast radius states no such file exists.
  Do not "fix" the grep pattern, and do not edit any matching artifact to make the output tidier.

- [x] **Re-run the spec's second sweep and read it as a rule check, not a count** (depends on the comparison above)
  Files: none — read-only check
  ```
  grep -n "written by the editor\|editor.*compose\|compose.*editor\|has the file open" src/skills/agent-architect/SKILL.md
  ```
  The purpose is the spec's own rule: **no sentence in this file describes what an `APPLY-EDIT` work-order carries, or who composes a file's text, without excluding the memory snapshot.** Run the sweep and read every line it returns against that rule. The "the text is written by the editor, who has the file open" sentence is expected and is not a contradiction — it describes composing an `APPLY-EDIT` in general, and the exclusion this task adds closes the door later in the same section. Then confirm by reading, not by grep, that no sentence anywhere in the file licenses delegating the snapshot.

- [x] **Confirm the change's scope** (depends on both sweeps)
  Files: none — read-only check
  `git diff` touches exactly one file, `src/skills/agent-architect/SKILL.md`, and exactly two sentences within it. Read the diff as sentences, not lines: re-wrapping makes both paragraphs show more changed lines than the two changed sentences, and that is expected, not a scope violation. What would be a violation is changed *words* in any sentence other than the two this task owns.
