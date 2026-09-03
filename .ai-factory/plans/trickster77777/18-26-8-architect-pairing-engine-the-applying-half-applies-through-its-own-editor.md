# Plan: 26.8 — architect-pairing-engine: the applying half applies through its own editor

## Context
The pairing contract has the applying half act on shared artifacts with its own hands, overriding the generic editor-is-the-hand rule — a model never asked for and backwards: the half originates no edit, but what arrives is a *decision* it composes into an `APPLY-EDIT` for its own editor. This task removes the wrong model from all three places it lives (section body, `description:`, the "the way an editor would" simile), adds the one-code-block relay rule to the deciding half, and closes two wiring gaps in `agent-architect` (a `loads:` edge with no load instruction; the editor named as a work-order's only addressee).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## How to read the line numbers
**Every line number in this plan is a `HEAD` coordinate — an anchor, not an address.** The edits shift each other, so each task also names the text it anchors on (the quoted opening words, "the paragraph between the blank lines at …", "immediately after the paragraph ending …"); when a number and its text anchor disagree at execution time, the **text anchor wins**. The tasks below carry `depends on` edges fixing one total order, and each downstream task states where its target sits *at execution time* under that order.

## Assumption (verification method, pinned here)
The spec's width check reads "No prose line in either edited file exceeds 76 characters." Ground truth disagrees for `src/skills/agent-architect/SKILL.md`, which already carries pre-existing over-76 lines outside this task's hunks (`:4-8`, `:13`, `:19-21`, `:23`, `:79`, `:81`, `:118`, `:192`, `:210-211`) — a whole-file check would fail on text this task never touches. Read the check as scoped to the lines this task writes:

- **every added line in `git diff` is ≤76** under `python3 len()`;
- **no pre-existing over-width line outside the two re-wrapped paragraphs changes.**

The exclusion is real and deliberate: `agent-architect:186` is 77 characters and sits *inside* the paragraph `:184-188` that this task re-wraps whole, so it necessarily changes and is not on the must-stay list above. (`:210-211` and the rest are outside every hunk and must be untouched.) `architect-pairing-engine:30` (the `grep` code span) stays exempt and untouched. All pinned blocks below are already wrapped to ≤76 (the `description:` block to ≤74) — reproduce them verbatim rather than re-wrapping.

## Tasks

### architect-pairing-engine — the applying half loses the own-hands model

- [x] **Replace the originates-no-edit paragraph**
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Replace `HEAD:52-56` — the paragraph between the blank lines at `:51` and `:57`, opening "It originates no edit of its own: every change it makes to a shared artifact" — with exactly:

  ```
  It originates no edit of its own: every change to a shared artifact traces
  to an arriving work-order, never to its own judgment. What arrives is a
  decision, not a delivery — it composes that decision into an `APPLY-EDIT`
  message to its own editor, exactly as an unpaired architect does. The editor
  is the hand here as everywhere; the only departure is where the work-order's
  content comes from.
  ```

  What disappears with it: "every change **it makes** to a shared artifact", the simile "the way an editor would", and the clause "does not route it onward to an editor of its own — its hands are its own, not delegated a second time." Five lines become six, shifting everything below by +1.

- [x] **Substitute one phrase in the check paragraph** (depends on Replace the originates-no-edit paragraph)
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Target: the check paragraph 26.6 settled, opening "Applying exactly is not obeying blindly." — `HEAD:58-64`, sitting at **`:59-65` at execution time** after the previous task's +1. Replace the single phrase `before you touch them` with `before sending it to your editor`. **Change no other word.** The substitution lengthens the paragraph, so re-wrap it to 76; the result is exactly:

  ```
  Applying exactly is not obeying blindly. Read the arriving work-order
  against the files before sending it to your editor: where it is
  underspecified, contradicts itself, or would break something it never named,
  report that back instead of guessing your way through it, and name in your
  report every decision the work-order left unpinned. The deciding half
  verifies what landed against the files, so an unflagged judgment call is the
  one thing its check cannot see.
  ```

  Seven lines in, seven lines out — no further shift. Guard: no correction licence, no round-closing clause, no third mode may return with this re-wrap. Confirm the paragraph's whitespace-normalized word sequence differs from `git show HEAD:src/skills/architect-pairing-engine/SKILL.md`'s only by `before you touch them` → `before sending it to your editor`.

- [x] **Delete the supersession paragraph** (depends on Substitute one phrase in the check paragraph)
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Delete the blank line at `HEAD:65` and the whole paragraph at `HEAD:66-69` — opening "This half supersedes the generic default" and ending "act on the arriving work-order." — sitting at **`:66` and `:67-70` at execution time**. The file — and § "The applying half" — now ends at "…its check cannot see." with a single trailing newline. § "The applying half" is left with exactly two paragraphs. The generic editor-is-the-hand rule at `agent-architect:25-26` is what the half falls back on; nothing replaces the deleted text.

- [x] **Name the editor as the hand in `description:`** (depends on Delete the supersession paragraph)
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  In the `description:` field, replace `applies only what an arriving work-order pins` with `applies through its own editor only what an arriving work-order pins`. Nothing else in the field changes. Only the lines the substitution lengthens are re-wrapped: lines `4-8` stay byte-identical, and lines `9-13` (unshifted — every edit so far was below them) become exactly (2-space continuation indent, the field's settled ≤74 total width):

  ```
    originates no edit of its own, applies through its own editor only what
    an arriving work-order pins, and reports back an order that is
    underspecified, self-contradicting, or would break something it never
    named instead of applying it in silence. Load only when the user has
    assigned it one of these two roles for the session; never in an unpaired
    session.
  ```

  Five lines become six, shifting the whole body below by +1.

### architect-pairing-engine — the deciding half gains the one-block relay rule

- [x] **Insert the single-code-block rule into § "The deciding half"** (depends on Name the editor as the hand in `description:`)
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Insert a new paragraph (preceded by a blank line) immediately after the paragraph ending "…not this half's own editor." (`HEAD:41`, at **`:42` at execution time**) and before "Departure from the generic spawn trigger" (`HEAD:43`, at **`:44` at execution time**). Exact text:

  ```
  Because that delivery is a human copy-paste and not a `SendMessage` call,
  the work-order ships as one single code block — every pinned value,
  guardrail, self-verify command and the "do not commit" inside it — so the
  user can copy it whole and relay it unmodified. Never split it across
  several blocks or interleave prose between them.
  ```

  Guard: both existing paragraphs of § "The deciding half" stay word-for-word; this change only inserts between them. The rule is pairing-specific and never enters `architect-editor-engine`, which stays delivery-agnostic.

### agent-architect — the two wiring gaps

- [x] **Instruct the load where the pairing role is recorded**
  Files: `src/skills/agent-architect/SKILL.md`
  Replace the sentence at `HEAD:61-65` — "A pairing role the user assigns for the session … need not coincide with the spawn." — with the version that also instructs the load. The sentence starts mid-line at `:61`, so lines `55-62` are unchanged and only `63-65` are rewritten; the resulting tail from `:61` reads exactly:

  ```
  contracts the name's behavior beyond the run. A pairing role the user
  assigns for the session (`architect-pairing-engine`'s deciding or applying
  half) gets a recording moment of its own: at the moment the user assigns it
  — which may be mid-session and need not coincide with the spawn — load
  `architect-pairing-engine` via the `Skill` tool if it is not already loaded,
  then write the role into the buffer.
  ```

  Three lines become four, shifting everything below by +1. This closes the gap where `loads: architect-pairing-engine` (`:14`) had no instruction anywhere in the body. The existing `architect-editor-engine` load instruction (`:42-45`) is a separate, untouched moment — that engine loads once at birth, this one only when a role is assigned.

- [x] **Name the paired architect as a possible work-order addressee** (depends on Instruct the load where the pairing role is recorded)
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Nothing closes a round before the editor's report exists", replace the sentence at `HEAD:184-186` — "An apply work-order closes a round as finally as a verdict … not who reads it." — with the version naming the deciding half's addressee. The paragraph runs `HEAD:184-188`, sitting at **`:185-189` at execution time** after the previous task's +1; re-wrap it whole to 76 so it reads exactly:

  ```
  An apply work-order closes a round as finally as a verdict, and it does so
  even though it is addressed to the editor — or, for the deciding half of a
  pairing, the paired architect — rather than the user: where the round is
  settled is what counts, not who reads it. A relay and its work-order sent in
  one message therefore close the round before any report could exist: the
  same violation as an early summary, never an exception to it.
  ```

  The trailing "A relay and its work-order…" sentence keeps its words exactly; only its line breaks move with the re-wrap. The 77-character line inside this paragraph (`HEAD:186`) is rewritten by design — see § Assumption.

### Verify

- [x] **Run the spec's verification list** (depends on Name the paired architect as a possible work-order addressee, Insert the single-code-block rule into § "The deciding half")
  Files: `src/skills/architect-pairing-engine/SKILL.md`, `src/skills/agent-architect/SKILL.md`
  Every phrase count is taken against a **whitespace-normalized** read — never a line-oriented `grep`. These files hard-wrap at 76, so a phrase can straddle a line break and a line-oriented grep then returns 0 whether the phrase is there or not: a check that cannot fail. Use:

  ```bash
  count() { python3 -c "import re,sys; print(re.sub(r'\s+',' ',open(sys.argv[1],encoding='utf-8').read()).count(sys.argv[2]))" "$1" "$2"; }
  ```

  Expected, in `src/skills/architect-pairing-engine/SKILL.md`:
  - `does not route it onward to an editor of its own` → 0
  - `This half supersedes the generic default` → 0
  - `before you touch them` → 0
  - `the way an editor would` → 0
  - `every change it makes` → 0 (the third carrier of the own-hands model, dropped by the wholesale paragraph replacement — nothing else in the Verify list witnesses it)
  - `applies through its own editor` → 1
  - `single code block` → 1

  Expected, in `src/skills/agent-architect/SKILL.md`:
  - `architect-pairing-engine` → 3 (the `loads:` frontmatter edge, the parenthetical naming the two halves, the load instruction added here) — occurrences, not line numbers
  - `paired architect` → 1

  Then:
  - Width: every line **added** by `git diff HEAD -- src/` is ≤76 under `python3 len()` (decoded text — never `awk length()` or `wc -m`, which count bytes and read a 3-byte em-dash as three). No pre-existing over-width line *outside* the two re-wrapped paragraphs changes; `agent-architect:186` is inside one of them and is expected to change (§ Assumption).
  - Word preservation: for each re-wrapped paragraph (the check paragraph, the `description:` tail, `agent-architect`'s `HEAD:184-188`), compare its whitespace-normalized word sequence against the same paragraph in `git show HEAD:<path>` — differences must be exactly the pinned substitutions and nothing else. A width check alone cannot see a word dropped in a re-wrap.
  - Scope: `git diff HEAD --stat -- src/ .ai-factory/roadmaps/` lists exactly `src/skills/agent-architect/SKILL.md`, `src/skills/architect-pairing-engine/SKILL.md` and the roadmap. `src/agents/editor.md`, `src/skills/architect-editor-engine/SKILL.md`, `agent-architect`'s `description:` and `:25-26`, and `architect-pairing-engine:30` show no diff.
  - No count above is evidence until taken by the normalized method; a number from a line-oriented `grep` is not evidence, whatever it returned.
