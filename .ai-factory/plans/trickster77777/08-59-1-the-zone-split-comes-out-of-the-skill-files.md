# Plan: 59.1 — the zone split comes out of the skill files

## Context

The user has ruled the architect's buffer has no zones: no settled/live split, no region the editor may not read. `docs/paired-loop.md` § "What the memory holds, and who holds it" already states the ruling and is the governing text this task conforms the code to — it opens "The head is the memory's only writer. The hand reads it in full — that is what makes the memory the link between the two halves — and never writes to it." Three files still define or reference the removed split and are brought into line with it: the engine that defines the buffer, the architect skill that points at that definition, and the editor agent that holds the buffer from birth.

**Every replacement is pinned word for word** in `.ai-factory/specs/trickster77777/164-the-zone-split-comes-out-of-the-skill-files.md` § "What must be true after". Copy the wording from there; a paraphrase is a defect, not a variant. This plan quotes the same wording so the implementer can work from one file, but the spec is the authority if they ever differ.

**Copy the pinned text, not this plan's formatting of it.** Where this plan names which word changed inside a pinned sentence, it says so in prose — no emphasis markup is ever added to mark a change. None of the replacement text carries bold or italics, and none of it should land carrying any. This matters most in the engine's § "The architect's buffer", where the paragraph being deleted uses bold for real (`The **settled** zone`, `The **live** zone`): markup surviving into the replacement would read as file text rather than as a pointer, and the word-for-word read-back compares words, not markup.

**No file gains a replacement boundary of any kind** — no "always read, sometimes private", no renamed split, no softened zone. The two rules that survive, stated plainly wherever the buffer is defined or referenced: the head is the memory's only writer; the hand reads it in full and never writes to it.

**The three edits are one deliverable.** A buffer defined without zones in the engine while the architect skill still points at "its two zones and what each holds" leaves the pair reading two contradictory contracts at birth. Land all three or none.

**Scope boundaries, verified against the current tree:**

- `.ai-factory/notes/07-architect-buffer.md` — the live architect buffer in this repository, literally structured with `# Live` and `# Settled` headings. Out of scope per the task line and the spec; it is the architect's own file to restructure, never this task's. Do not touch it.
- The repository-wide sweep `grep -rniE "settled zone|live zone|two zones|the split|zone" src/ docs/` returns hits outside these three files, and the spec's rule decides all of them without a list: **any hit that does not actually describe the buffer is a false positive, unrelated to this task, and stays untouched.** The vocabulary recurs elsewhere for its own ordinary meaning — a factual/judgment split, a task's own scope-zone, a step that splits a state file, an unrelated data table — and none of that usage is this task's to correct. Read each survivor and classify it; do not check it against an enumeration. The spec retired its own list of these for exactly this reason: a new file anywhere using either word ordinarily makes the list wrong on the spot, while the rule stays true.
- Inside `src/skills/agent-architect/SKILL.md` the same rule applies to that file's own ordinary uses of the words — "a live task registry", "leaving both buffers live", "where the round is settled is what counts". These are named because they sit in a file the implementer is editing, where the risk is an over-edit rather than a missed one: leave all three exactly as they stand.
- **Flagged, not acted on:** the project `CLAUDE.md`'s documentation-table row for `docs/paired-loop.md` still summarises it as "the buffer's two zones and who holds which, why the live zone stays private". That row is already stale against its own target today — `docs/paired-loop.md` carries no zone language — so it is a pre-existing defect this task neither creates nor breaks, in a file outside the task's three named sites. It is left untouched and raised here for the architect's attention.

All three targets are reached through symlinks that already exist (`active/skills/architect-editor-engine`, `active/skills/agent-architect`, `active/agents/editor.md`). Editing the `src/` files is the whole job — no second copy, no symlink to create.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The engine — where the buffer is defined

- [x] **Replace the zone clause in the engine's frontmatter `description:`**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  In the `description:` block, replace the two-zone clause with the rule that survives, so the field reads, in the same position:

  > the definition of the
  > architect's buffer the pair shares: its path and numbering, the rule that the
  > head is its only writer and the hand reads it in full and never writes to
  > it, the editor's re-read of the memory on change, and the drain rule that a
  > ruling leaves the buffer once it reaches the artifact that should hold it,

  The clause being replaced currently spans four wrapped lines beginning "architect's buffer the pair shares: its path and numbering, its settled zone" — locate it by matching that text, never by line number. The anchor line "the definition of the" above it is unchanged and is quoted only to place the block.
  **Take the replacement's line breaks as given**: the four lines above are the pinned block, and copying them with the two-space YAML continuation indent the field already uses is the whole instruction. Do not re-wrap them to some other width — they already sit in the range the field's existing lines occupy.
  Everything before that clause ("Shared contract for the architect↔editor paired loop…" through "the token that literally opens each message, and") and everything after it ("and the rule that no architect reads another's buffer and an editor reads only its own architect's. When-to-use policy stays with the caller.") stays word-identical. The other frontmatter fields — `name:`, `user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read` — are untouched.
  This field is a skill description: it is always loaded as part of the skill-description-field, so it must read as a definition of the buffer, not as a note about a change. The resulting field measures 810 characters against the 1024-char limit — no trimming anywhere else is needed or wanted.

- [x] **Rewrite § "The architect's buffer" to the no-zone contract** (depends on the frontmatter edit — same file, land them together)
  Files: `src/skills/architect-editor-engine/SKILL.md`
  Work the numbered list below to its end — every item is a separate change and the section is not done until all of them have landed. Nothing else in the section changes.

  1. The opening paragraph gains the writer/reader rule in its pointer sentence, so it reads:

     > The pair shares one working memory: the architect's buffer, a file at `.ai-factory/notes/<NN>-architect-buffer.md`, numbered like the other temporary notes in that directory so that several architects coexist without colliding. This engine is the home of that path and that numbering, and of the rule that governs who may write to it and who may only read; the architect's own skill points here rather than restating them.

  2. The whole two-zone paragraph — the one opening "The buffer has two zones, and the split is load-bearing." — is **replaced** by:

     > The head is the memory's only writer. The hand reads it in full — that is what makes the memory the link between the two halves — and never writes to it. It holds the working discipline, the rulings the user has made about how the pair works, the method learned from repeated failure, and the register of where the skills still lag the practice: the editor reads it as its own working context from the head it is the hand of, not as an outsider glancing at private notes, which is what lets an order name meaning instead of restating the discipline every time.

     The replacement carries no bold anywhere — the two emphasised zone names go out with the paragraph and nothing takes their place.
     Note what the replacement deliberately drops and does not relocate: the live zone's contents (the editor's handle, the architect's current read of an open question, a diagnosis still forming) and the echo argument that justified keeping them private. They do not reappear under another name anywhere in the file. The handle's own timing and home are stated in `agent-architect`'s own sections and need no echo here.

  3. The re-read paragraph loses the zone from its subject — "the settled zone" becomes "the memory", and the rest of the sentence stays word-identical:

     > The editor re-reads the memory when it changes, not once at birth — and the same rule covers being named a different buffer's path outright by its architect: either way the memory has moved, and the hand adopts what it is now told, replacing what it held, holding one memory at a time.

  4. The paragraph on what rides alongside a channel-message loses the zone from its example — "that the settled zone has moved" becomes "that the memory has moved":

     > A channel-message the architect is already sending may carry, alongside its payload, what keeps the hand current: a fact about where the shared memory sits — that the memory has moved, or the buffer's path itself — or what the hand needs in order to work at all.

     The remainder of that paragraph — from "This opens no message of its own…" to "…carries no reading of it." — stays word-identical.

  5. The closing two-architects paragraph drops its trailing qualifier, ending: "An editor reads only its own architect's buffer — the memory of the head it is the hand of — never another architect's." The phrase ", settled zone included" goes; nothing replaces it. The separation between architects is unchanged by this task — only the zone it named is gone.

  The drain-rule paragraph ("A ruling recorded in the buffer is a debt against the skill…") is untouched.
  Write each paragraph as **one unwrapped line**: this file's body prose is not hard-wrapped — its paragraphs are single long lines. Do not introduce hard wrapping.
  The section heading `## The architect's buffer` stays byte-identical: § "The mode rule" in this same file cites it by name ("as § \"The architect's buffer\" states"), and that reference must keep resolving. The file's §§ "The two channel-message formats" and "The mode rule", and the load-once/reverse-graph paragraph under the title, are untouched.

### The architect — the skill that points at the definition

- [x] **Drop "zones" from the two references in `agent-architect`** (depends on the engine rewrite)
  Files: `src/skills/agent-architect/SKILL.md`
  Two edits, each a pointer at the engine's definition — neither restates the contract, and neither should start to:

  1. In § "Spawn once, message thereafter", the sentence about loading the engine currently reads "it is where your buffer's path, zones, and rules are defined, so it is". It becomes: "it is where your buffer's path and rules are defined, so it is". The rest of that sentence and the whole surrounding paragraph — the two-step start, the two kinds of start, "Either way the buffer exists before any editor does." — stay word-identical.
     Deleting the one word `zones,` shortens this line and leaves it comfortably inside the widths its neighbours already use. **Do not re-wrap the paragraph to take up the slack**: the next task, 59.2, appends at this paragraph's end, and leaving the surrounding lines where they are keeps the two tasks' spans disjoint. A slightly short line here is correct.

  2. In § "Your buffer is shared; you alone write it", the pointer sentence becomes:

     > The buffer's path and numbering, the rule that the hand reads it in full and never writes to it, the editor's re-read of the memory, and the drain rule are `architect-editor-engine`'s, loaded at birth — this section points there and restates none of them.

     Re-wrap this sentence and the text around it to the width the paragraph already uses, reading the neighbouring lines for it rather than counting to a number. The sentence before it ("Each deferral entry names *what*, *why deferred*, and the *trigger* that resolves it; delete an entry once it's done — deferral entries remain the buffer's primary content.") and the sentence after it ("It is the one file you edit directly: you are its only writer.") stay word-identical — the second one is the writer half of the surviving rule and is exactly why the pointer does not restate it.

  The section heading `## Your buffer is shared; you alone write it` stays byte-identical — this file cites it by name in two other places (the spawn-fallback passage, and § "Nothing closes a round before the report on it exists"), and both references must keep resolving.
  Nothing else in this file changes. In particular the frontmatter, the memory-snapshot paragraphs (58.1's, 58.2's, and 58.4's landed work), the handle-write paragraph, and every ordinary use of "live" and "settled" elsewhere in the file stay as they are.

### The editor — the hand that holds the memory

- [x] **Rewrite the editor's opening paragraph** (depends on the engine rewrite)
  Files: `src/agents/editor.md`
  The opening paragraph's second half — from "load `architect-editor-engine` via the `Skill` tool" to the end of the paragraph — is replaced so the passage reads:

  > load `architect-editor-engine` via the `Skill` tool — it is the shared contract for this pair, holding the two channel-message formats and the definition of the architect's buffer, which you hold in full as your own working context from birth, and it must be resident before you read anything sent to you. Alongside that first channel-message, the spawn prompt gives you the buffer's own path — held from birth, never part of the message itself, since the format token alone still opens it and decides the mode — and it is where that memory lives.

  The paragraph's first two sentences — "You are the **editor** — a persistent subagent the architect spawns once and keeps for the whole session, born fresh into this role at every spawn. As the very first action on spawn, before processing the first channel-message," — stay word-identical, bold included.
  Hard-wrap the rewritten text to the width this file already uses throughout, reading the surrounding lines for it. The wrap points are the implementer's own; the words and their order are not.
  Two things the wording is doing on purpose: "which you hold in full" replaces "whose settled zone you hold", so the editor holds the whole buffer with no carve-out; and the closing "it is where that memory lives" replaces "it is where that settled zone lives", keeping the path's antecedent pointing at the buffer as a whole. Do not reintroduce a qualifier of any kind on what the editor may read.
  The frontmatter (`name:`, `description:`, `tools:`, `model:`, `effort:`) and every section below the opening paragraph — "Analysis mode", "Apply mode", "The round's unit", "Self-verify…", "Commit only on explicit permission" — are untouched.

### Verification

- [x] **Check the three files against the spec's pinned wording, then re-run the sweep** (depends on all three edits)
  Files: none — read-only check
  Read each edited passage back against `.ai-factory/specs/trickster77777/164-the-zone-split-comes-out-of-the-skill-files.md` § "What must be true after" word for word, including the engine's `description:` field.
  Then check the markup as well as the words: no bold or italics exists anywhere in the engine's rewritten § "The architect's buffer", and the only emphasis in `editor.md`'s opening paragraph is the pre-existing "**editor**" in its first sentence. A word-for-word read-back passes markup silently, so look at it deliberately.
  Then re-run the spec's own sweep and confirm every remaining hit is a false positive by the rule above:
  ```
  grep -rniE "settled zone|live zone|two zones|the split|zone" src/ docs/
  ```
  The mechanical half of the expectation: after the edits, "settled zone", "live zone", and "two zones" return nothing anywhere under `src/`. Everything else the run returns is classified by reading it — for each surviving hit, decide whether it describes the architect's buffer, and if it does not, it is a false positive that stays untouched. Do not expect the run to match any list, this plan's included; the rule is the check, and a survivor this plan never mentioned is an ordinary outcome, not a sign the sweep was run wrong.
  The engine's closing two-architects paragraph is the easiest one to leave half-done — confirm specifically that its ", settled zone included" is gone.
  Confirm the three headings that other text cites by name survived byte-identical: `## The architect's buffer`, `## Your buffer is shared; you alone write it`, and (unchanged by this task) `## Spawn once, message thereafter`.
