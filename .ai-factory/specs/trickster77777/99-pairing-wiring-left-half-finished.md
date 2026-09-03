# architect-pairing-engine: the applying half applies through its own editor

The pairing contract says the applying half acts on shared artifacts with its
own hands, overriding the rule that the editor is always the hand. That was
never asked for, and it is backwards: the applying half originates no edit,
but the edit it receives still travels through its own editor. The wrong model
is in three places — the section body, the always-loaded `description:`, and a
simile that no longer describes the mechanism. Two wiring gaps sit alongside
it: the generic skill declares `loads: architect-pairing-engine` without ever
instructing the load, and it names the editor as an apply work-order's only
possible addressee. One rule is added: a work-order the user relays by hand
ships as a single code block.

## Current state (grounded, read fresh)

`src/skills/architect-pairing-engine/SKILL.md:52-56`:

> "It originates no edit of its own: every change it makes to a shared artifact
> traces to an arriving work-order, never to its own judgment. It applies
> exactly what that work-order pins, the way an editor would, and does not
> route it onward to an editor of its own — its hands are its own, not
> delegated a second time."

`src/skills/architect-pairing-engine/SKILL.md:66-69`:

> "This half supersedes the generic default that the architect never touches
> shared artifacts with its own hands, that hand always being the editor's:
> for the applying half, the architect's own hands are the ones that act on
> the arriving work-order."

`src/skills/architect-pairing-engine/SKILL.md:8-9`, inside `description:` — the
always-loaded summary read before the body is ever loaded:

> "and applying, which originates no edit of its own, applies only what an
> arriving work-order pins"

`src/skills/agent-architect/SKILL.md:14` declares
`loads: architect-editor-engine architect-pairing-engine`. The body instructs
loading only the first, at `:42-45`; the second appears once more, at `:62`,
as a parenthetical inside the role-recording sentence — never as a load.

`src/skills/agent-architect/SKILL.md:184-186`:

> "An apply work-order closes a round as finally as a verdict, and it does so
> even though it is addressed to the editor rather than the user — where the
> round is settled is what counts, not who reads it."

## The change

Seven edits across two files.

1. In `architect-pairing-engine/SKILL.md`, replace the paragraph at `:52-56`
   word-for-word with:

   It originates no edit of its own: every change to a shared artifact traces
   to an arriving work-order, never to its own judgment. What arrives is a
   decision, not a delivery — it composes that decision into an `APPLY-EDIT`
   message to its own editor, exactly as an unpaired architect does. The
   editor is the hand here as everywhere; the only departure is where the
   work-order's content comes from.

2. In the check paragraph at `:58-64`, replace the phrase "before you touch
   them" with "before sending it to your editor". Change no other word of that
   paragraph.

3. Delete the blank line at `:65` and the entire paragraph at `:66-69`. The
   section ends at "...its check cannot see."

4. In `architect-pairing-engine/SKILL.md`'s `description:` field, replace
   "applies only what an arriving work-order pins" with "applies through its
   own editor only what an arriving work-order pins". Change nothing else in
   the field, and re-wrap only the lines the substitution lengthens.

5. In `architect-pairing-engine/SKILL.md` § "The deciding half", insert a new
   paragraph immediately after the first paragraph (which ends "...not this
   half's own editor.") and before "Departure from the generic spawn
   trigger":

   Because that delivery is a human copy-paste and not a `SendMessage` call,
   the work-order ships as one single code block — every pinned value,
   guardrail, self-verify command and the "do not commit" inside it — so the
   user can copy it whole and relay it unmodified. Never split it across
   several blocks or interleave prose between them.

6. In `agent-architect/SKILL.md`, replace the sentence at `:61-65` — "A
   pairing role the user assigns for the session
   (`architect-pairing-engine`'s deciding or applying half) gets a recording
   moment of its own: write it into the buffer at the moment the user assigns
   it, which may be mid-session and need not coincide with the spawn." —
   word-for-word with:

   A pairing role the user assigns for the session
   (`architect-pairing-engine`'s deciding or applying half) gets a recording
   moment of its own: at the moment the user assigns it — which may be
   mid-session and need not coincide with the spawn — load
   `architect-pairing-engine` via the `Skill` tool if it is not already
   loaded, then write the role into the buffer.

7. In `agent-architect/SKILL.md`, replace the sentence at `:184-186` — "An
   apply work-order closes a round as finally as a verdict, and it does so
   even though it is addressed to the editor rather than the user — where the
   round is settled is what counts, not who reads it." — word-for-word with:

   An apply work-order closes a round as finally as a verdict, and it does so
   even though it is addressed to the editor — or, for the deciding half of a
   pairing, the paired architect — rather than the user: where the round is
   settled is what counts, not who reads it.

## Files & types

- edit: `src/skills/architect-pairing-engine/SKILL.md` — `description:`
  (change 4), § "The deciding half" (change 5), § "The applying half"
  (changes 1-3).
- edit: `src/skills/agent-architect/SKILL.md` — `:61-65` (change 6) and
  `:184-186` (change 7).

## Guards

- The check paragraph at `:58-64` keeps every word except the substitution in
  change 2. It is what 26.6 settled; no correction licence, no round-closing
  clause, no third mode returns with it.
- `## The deciding half`'s two existing paragraphs stay word-for-word; change
  5 only inserts between them.
- `agent-architect`'s `description:` and `:25-26` are correct and stay
  untouched — the generic rule is what the applying half now falls back on.
- `src/agents/editor.md` and `src/skills/architect-editor-engine/SKILL.md` are
  untouched. The one-block rule is pairing-specific and never enters the
  format engine, which stays delivery-agnostic.
- Prose is wrapped to the file's settled 76-character width, measured with
  `python3 len()` on decoded text — never `awk length()` or `wc -m`, which
  count bytes and read a 3-byte em-dash as three. The `grep` code span at
  `architect-pairing-engine:30` is exempt: it cannot be wrapped.

## Verification

Every phrase count below is taken against a whitespace-normalized read of the file — never a line-oriented `grep`. These files are hard-wrapped at 76 characters, so any phrase may straddle a line break, and a line-oriented grep then returns 0 whether the phrase is present or not: a check that cannot fail. Count with `python3 -c "import re,sys; print(re.sub(r'\s+',' ',open(sys.argv[1],encoding='utf-8').read()).count(sys.argv[2]))" <path> "<phrase>"`. This holds in both directions — for a phrase the task deletes and for one it introduces. The second case is why a pre-check against `git show HEAD:<path>` is not enough on its own: text the task creates is not in `HEAD` to be checked against, and that is exactly where a line-oriented count gave a false pass before.

- "does not route it onward to an editor of its own" in `src/skills/architect-pairing-engine/SKILL.md` → 0
- "This half supersedes the generic default" in `src/skills/architect-pairing-engine/SKILL.md` → 0
- "before you touch them" in `src/skills/architect-pairing-engine/SKILL.md` → 0
- "the way an editor would" in `src/skills/architect-pairing-engine/SKILL.md` → 0
- "applies through its own editor" in `src/skills/architect-pairing-engine/SKILL.md` → 1
- "single code block" in `src/skills/architect-pairing-engine/SKILL.md` → 1
- "architect-pairing-engine" in `src/skills/agent-architect/SKILL.md` → 3 occurrences: the `loads:` frontmatter edge, the parenthetical naming the two role halves, and the load instruction added by change 6. Occurrences, not line numbers — normalized reading collapses the file to one line, and line numbers are not evidence anyway: they move with any edit above them.
- "paired architect" in `src/skills/agent-architect/SKILL.md` → 1
- No prose line in either edited file exceeds 76 characters under `python3 len()`, excluding `architect-pairing-engine:30`.
- Every paragraph re-wrapped after a substitution has the same words as before it: compare its whitespace-normalized word sequence against the same paragraph in `git show HEAD:<path>`. A width check alone cannot see a word dropped during a re-wrap.
- `git diff HEAD --stat -- src/ .ai-factory/roadmaps/` lists exactly `src/skills/agent-architect/SKILL.md`, `src/skills/architect-pairing-engine/SKILL.md` and the roadmap — scoped to those two paths so the check is invariant to the spec file's own tracking state, which can change independently of this task at any time.
- No count above is trusted as evidence until it was taken by the normalized method named at the head of this section. A count taken with a line-oriented `grep` is not evidence, whatever number it returned.
