# Plan: 58.1 — the snapshot carries reasoning, not just residue, and is thick by default

## Context
`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" defines what a memory snapshot carries as "only the volatile residue", naming nothing about the stretch's own reasoning and stating no thickness default; the sentence immediately after it retires a whole older snapshot by name. This task replaces the first sentence with the wording pinned in the task spec (reasoning required, thick by default) and appends a scoping clause to the second so that only the next action goes stale. One file, two adjoining sentences of one paragraph, both pinned verbatim upstream.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## What is pinned, and what this plan adds

`.ai-factory/specs/trickster77777/159-the-snapshot-carries-reasoning-and-is-thick-by-default.md` § "What must be true after" gives **both replacements verbatim**. They are the deliverable, not a sketch to re-derive: copy the words and their order from the spec. Everything below adds only what the spec leaves to the implementer — where in the file the anchors sit, how the destination wraps, and which neighbouring sentences must not move.

Ground truth confirmed before planning (`src/skills/agent-architect/SKILL.md`, § "Spawn once, message thereafter", the memory-snapshot paragraph):

- Sentence 1 begins exactly at the start of a line, immediately after the sentence ending `…is never sent to the editor.` — the sentence **58.2 owns**. It ends with `never an inventory of the session.` mid-line, and sentence 2 (`Each new`) starts on that same line.
- Sentence 2 ends `…a stale next action.` mid-line, and the next sentence (`Of the recorded state, only the buffer's path travels:`) starts on that same line. That sentence belongs to no task in this phase and its words must survive byte-identical.
- The paragraph opens with the two-occasions sentence, which **58.4 owns**.
- Nothing else in the repository defines what a snapshot carries: `src/skills/architect-editor-engine/SKILL.md` and `src/agents/editor.md` mention no snapshot at all, and this file's other four mentions (§ "Spawn once…" opening, the liveness passage, § "Your buffer is shared…", § "On every invocation") speak only of the buffer pointer and the recovery occasion — none of them asserts residue-only content or unscoped supersession. So the change stays inside one paragraph, as the spec's blast radius states.
- The frontmatter `description:` makes no claim about snapshot content and is deliberately untouched — always-loaded description text is its own decision, and the spec's change list does not name it.

**Two mechanical facts the implementer must plan for.** Both sentences share lines with their neighbours, so applying either edit re-wraps the paragraph. That is expected and permitted: **verbatim means the words and their order, never the newlines.** The wrap convention here is the paragraph's own — hard-wrapped at roughly 63–76 columns, well under the file's widest body line — and the new text lengthens the paragraph by several lines, taking the file from 371 lines to under 380, inside the ≤ 500-line body constraint. One consequence to expect: a phrase of the new text may span a line break afterwards, so any later grep against this passage matches per line, never per sentence.

## Tasks

### The two sentences

- [x] **Replace the residue sentence with the pinned replacement**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", replace the sentence currently reading "What a snapshot carries is only the volatile residue — where the work stands, what the hand knows, what will slip first, and what must not be resolved by inference — because everything durable already lives outside the conversation; never an inventory of the session." with the replacement pinned in the task spec § "What must be true after" — the one beginning "What a snapshot carries is the volatile residue" and ending "…a pointer list for raising context rather than a stretch's history."
  Hold to these:
  - **Copy from the spec; do not paraphrase.** The replacement drops the word "only"; drops the "and" before "what must not be resolved by inference"; **inserts, immediately after the residue list and before the durability clause, the requirement this whole task exists for** — "— and the reasoning that shaped it: why one option was taken over another, which premise proved false and how, what the user's own correction was and in what words"; turns "because everything durable…" into "everything durable already lives outside the conversation, so restating it is never the point"; replaces "never an inventory of the session" with "a snapshot that drops the reasoning is an inventory, not a history"; and then adds the thickness default as its own sentence: thick by default carrying the reasoning in full, thin only when asked for or when what is plainly meant is a pointer list for raising context. Each of those is a pinned wording choice, not a stylistic one.
    This enumeration is a reading aid for the pinned text, **never a substitute change set** — the spec's blockquote is the deliverable, and a replacement that satisfies every entry above while dropping the reasoning clause has lost the task's entire purpose. The two later entries depend on that clause: "a snapshot that drops the reasoning is an inventory" and "carrying that reasoning in full" both point back to it.
  - **Do not restate `docs/paired-loop.md`.** The reasoning requirement leans on that document's break-destroys claim *by consequence* — it names what the snapshot must carry, and never repeats the doc's own justification for why a break destroys it. Add no citation sentence, no "per `docs/paired-loop.md`" aside, no explanation of why reasoning dies in a compact.
  - **Re-wrap to the destination.** The spec renders the replacement as a blockquote with its own line breaks; do not paste them. Wrap to the paragraph's existing width (~63–76 columns) so the passage reads as one paragraph with its neighbours.
  - **The two adjoining sentences keep their words exactly.** The sentence before it ends `…the digest is your own recovery note and is never sent to the editor.` (58.2's anchor) and the sentence after it begins `Each new snapshot supersedes the last by name` — neither loses or gains a word here. Their line breaks may shift from the re-wrap; their text may not.

- [x] **Scope the supersession sentence to the next action** (depends on Replace the residue sentence with the pinned replacement)
  Files: `src/skills/agent-architect/SKILL.md`
  In the same paragraph, the sentence "Each new snapshot supersedes the last by name — the numerically higher-numbered one is the current one — so a reader never follows a stale next action." gains the scoping clause pinned in the task spec: the terminal period becomes a semicolon, followed by "what goes stale is the next action alone, and the record beside it stays."
  Hold to these:
  - **Append only.** The sentence's existing three parts — supersession by name, the higher-numbered-is-current gloss, the stale-next-action consequence — stay byte-identical up to that final period. Nothing is reordered and nothing is deleted.
  - **Take only the operative fact.** `docs/paired-loop.md` argues at length that the series of snapshots read in order is the pair's only account of how it moved; that argument addresses a different reader and stays in the document. This clause says what goes stale and what does not, and stops there.
  - **The sentence that follows it does not move.** `Of the recorded state, only the buffer's path travels:` begins mid-line today, directly after the period being replaced. Its words — and the two lines completing it about the pointer, the handle, and the pairing role — survive unchanged; only their line breaks may shift as the paragraph re-wraps.

### Verification

- [x] **Compare the edited paragraph against the spec's pinned wording, word for word** (depends on Scope the supersession sentence to the next action)
  Files: none — read-only check
  Read § "Spawn once, message thereafter"'s memory-snapshot paragraph back off disk and set it beside the two blockquotes in `.ai-factory/specs/trickster77777/159-…md` § "What must be true after". Compare **sentence by sentence, words only, ignoring line breaks** — the paragraph is hard-wrapped, so the comparison is of the text with newlines collapsed to spaces, never of the lines themselves.
  This is the positive half of verification and the sweep below cannot stand in for it: the sweep only proves the old anchors are gone, which a truncated rewrite — one that drops "only", rewords the inventory phrase and appends the thickness sentence while never inserting the reasoning clause — would also achieve. What this step confirms is that the words that were the point of the task actually landed.
  Check, in order:
  - **The residue sentence** matches the spec's first blockquote in full, including the reasoning clause ("…and the reasoning that shaped it: why one option was taken over another, which premise proved false and how, what the user's own correction was and in what words…") and the thickness sentence that closes it.
  - **The supersession sentence** matches the spec's second blockquote in full, ending "…what goes stale is the next action alone, and the record beside it stays."
  - **The three neighbours are byte-identical to what they were before this task**: the two-occasions sentence and the digest sentence that open the paragraph (58.4's and 58.2's anchors) and the closing sentence beginning "Of the recorded state, only the buffer's path travels:". Only their line breaks may differ.
  A mismatch in the first two is a defect in this task's own edits — fix it against the spec. A mismatch in the third is a neighbour that was disturbed and must be restored to its prior wording.

- [x] **Re-run the spec's sweep and confirm the invariant** (depends on Compare the edited paragraph against the spec's pinned wording, word for word)
  Files: none — read-only check
  Run the task spec's own re-runnable sweep from the repo root:
  ```
  grep -rln "is only the volatile residue\|never an inventory of the session\|stale next action\." src/ docs/ .ai-factory/
  ```
  **The one path that must disappear is `src/skills/agent-architect/SKILL.md`.** All three anchors are gone by construction: the new wording drops "only", rewords "never an inventory of the session" into "an inventory, not a history", and continues "stale next action" with a semicolon instead of a period. That is the whole invariant this sweep carries — it is the negative half, and the step above is the positive one; neither alone finishes the task.

  Everything else the sweep returns is a hit by design, and the count is not the test. Judge each returned path by the spec's own **rule** — *does this file quote one of the two passages as ground truth for a standing claim about the present?* — never by whether it was on a list:
  - This task's own spec (`159-…md`) and the phase note (`152-…md`) record the pre-task wording as the state they describe. A spec and a note describe a moment, not the present. Correct as they are.
  - The roadmap's own contract line for this task states the problem it describes, permanently. Correct as it is.
  - The handoff (`.ai-factory/handoffs/29-…md`) is a different genre — read once, never re-read unconditionally. Leave it.
  - The architect's working buffer (`.ai-factory/notes/07-architect-buffer.md`) is a living memory this task has no authority to edit. Explicitly out of scope, not a defect.
  - This plan file, and any plan-review or review artifact of this task, match self-referentially — they quote the anchors and the sweep command rather than asserting them. Not findings.
  - A path that is none of the above **and** quotes a passage as a live claim: stop and report it, do not edit it. The spec's blast radius states no such file exists.

  Do not "fix" the grep pattern, and do not edit any matching artifact to make the output tidier.
