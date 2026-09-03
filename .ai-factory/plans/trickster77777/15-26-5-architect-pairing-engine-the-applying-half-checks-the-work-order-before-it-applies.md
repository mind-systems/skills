# Plan: 26.5 — architect-pairing-engine: the applying half checks the work-order before it applies

## Context
`src/skills/architect-pairing-engine/SKILL.md` § "The applying half" tells the applying architect to apply what an arriving work-order pins "the way an editor would", while the check that phrase stands for lives only in `src/agents/editor.md:77-83` — a file no architect loads. This task states that check in the pairing skill's own words and amends the `description:` field so the always-loaded skill description carries it too.

## Decisions this plan pins (raised by plan-review 1)

**1. The correction case is scoped inside the arriving work-order, in the file's own words.** `:50-51` says every change traces to an arriving work-order, "never to its own judgment"; the spec's paragraph says to *fix* an outright-wrong order. Read literally these fork, and the reconciliation exists only in the task spec's Guards — a planning artifact the applying architect never loads, which is the same defect this task closes. Resolution chosen: **carry the reconciliation into the inserted paragraph**, not into `:50-54` (which the spec guards as untouched) and not into the plan alone (which the file's next reader never sees). Two departures from the spec's word-for-word text follow, both additive and both narrowing, never widening, the applying half's licence:
   - "fix it" → "correct it inside the change the work-order already asks for" — the correction happens within what the order pins, so it is not an edit originated beside it;
   - one added sentence — "Correcting an order while executing it is not originating an edit of your own: it stays within what the work-order pins and it is never silent." — stating the reconciliation the spec's Guards state, in the file that needs it.

   Everything else in the spec's paragraph is verbatim. The spec's Guard "the applying half still originates no edit of its own" is honored *more* tightly by this wording than by the unscoped original.

**2. The return leg is named, not inferred.** The paragraph speaks of "your report", and nothing in this skill currently gives the applying half a report at all (the editor's comes from `architect-editor-engine` and `editor.md`, neither of which this half loads). One clause names it — the report closes the round back through the user, the path the work-order arrived by. This names the return leg only; it defines no channel-message format, so the spec's guard against a third mode / new format holds.

**3. The `description:` clause is pinned, not left to the implementer.** It is shipped always-loaded contract text; it gets the same word-for-word discipline as the body, and the same verification.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Skill body

- [x] **Insert the check paragraph into "## The applying half"**
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Insert this paragraph into `## The applying half`, between the existing originates-no-edit paragraph (`:50-54`) and the `This half supersedes…` paragraph (`:56-59`), separated by a blank line on each side. It is contract text — insert it **word-for-word, including the line wrapping shown**:

  ```
  Applying exactly is not obeying blindly. Read the arriving work-order
  against the files before you touch them: where it is underspecified,
  contradicts itself, or would break something it never named, report that
  back instead of guessing your way through it; where it is outright wrong —
  a stale reference, a mismatched value, an unaccounted collision — correct
  it inside the change the work-order already asks for and say so explicitly
  rather than deviating silently; and name in your report every decision the
  work-order left unpinned. Correcting an order while executing it is not
  originating an edit of your own: it stays within what the work-order pins
  and it is never silent. That report closes the round back through the
  user, the path the work-order arrived by; the deciding half verifies what
  landed against the files, so an unflagged judgment call is the one thing
  its check cannot see.
  ```

  Leave `:50-54` untouched — the sentence "It applies exactly what that work-order pins, the way an editor would…" stays; the new paragraph supplies what it stands for. Add no reference to `editor.md`, `agent-architect`, `architect-editor-engine`, or any `.ai-factory/` path here: a pointer to a file the reader never loads is exactly the defect being closed, and it applies to cases this plan did not foresee. After the edit, `## The applying half` holds three paragraphs in order — originates-no-edit, the check, the supersession note.

### Skill description field

- [x] **Replace the `description:` block** (depends on the paragraph insertion)
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Replace the folded block at `:4-11` (the body of `description: >-`, currently 538 characters folded) with exactly this, wrapping and two-space indent included — the new material is the applying clause's report-back behavior, and nothing else changes:

  ```
    Pairing-role contract for two architects working together with no direct
    channel between them — every message crosses through the user, who
    carries or confirms each relay. Holds the two role halves: deciding,
    whose editor becomes research-only and whose apply work-orders address
    the paired architect instead of its own editor; and applying, which
    originates no edit of its own, applies only what an arriving work-order
    pins, and reports back an order that is underspecified,
    self-contradicting, or would break something it never named instead of
    applying it in silence. Load only when the user has assigned it one of
    these two roles for the session; never in an unpaired session.
  ```

  This folds to 680 characters, under the 1024 limit. Keep the `>-` folded scalar and its indentation; never break a line inside a hyphenated word (a folded scalar joins lines with a space, so "self-\ncontradicting" would ship as "self- contradicting"). The deciding clause and the load-only-when-assigned / never-in-an-unpaired-session sentence are carried through unchanged — the block above already contains them verbatim.

### Verification

- [x] **Verify the edit against the spec's checks** (depends on both edits)
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Read `## The applying half` back in full and confirm the three-paragraph order, then run:
  - `grep -n "the way an editor would" src/skills/architect-pairing-engine/SKILL.md` → exactly one hit.
  - `grep -c "editor.md\|\.ai-factory/" src/skills/architect-pairing-engine/SKILL.md` → 0; the fix adds no pointer to an unloaded file.
  - `grep -c "Correcting an order while executing it is not" src/skills/architect-pairing-engine/SKILL.md` → 1; the reconciliation clause is present in the file, not only in the plan.
  - `grep -c "That report closes the round back through the" src/skills/architect-pairing-engine/SKILL.md` → 1; the return leg is named.
  - Frontmatter survivors. Both fragments are wrapped differently in the pinned block than in the file today, so match what the pinned wrap actually produces, never the file's current line breaks — a check that fails on a faithful edit is worse than no check, and the contract text is never re-wrapped to satisfy one:
    - `grep -c "whose editor becomes research-only" src/skills/architect-pairing-engine/SKILL.md` → 1 after the edit (0 today: the phrase is split across `:6-7` in the current wrap, and the body's `:32` reads "Its editor becomes research-only", which does not match this string). This is the deciding clause's survivor.
    - `grep -c "never in an unpaired session" src/skills/architect-pairing-engine/SKILL.md` → **2**, the count both before and after: one copy in the frontmatter (`:11`), one in the body's load-rule paragraph (`:26`). Both are load-bearing and both must stay — the body copy is the same text the `:25-28`-unchanged guard below protects, so never resolve this count to 1 by deleting either. To check the frontmatter copy alone: `sed -n '1,15p' src/skills/architect-pairing-engine/SKILL.md | grep -c "never in an unpaired session"` → 1.
  - Fold the `description:` block to one line and confirm it is **byte-identical** to the pinned text above — this is the assertion that does the real work. As a cheap cross-check, its length is 680 characters / 682 bytes (the em dash is 3 bytes in UTF-8): `wc -m` → 680, `wc -c` → 682. Do not compare `wc -c` against 680.
  - `git diff --stat` → exactly one file under `src/` changed; nothing in `src/agents/editor.md`, `src/skills/agent-architect/SKILL.md`, or `src/skills/architect-editor-engine/SKILL.md`.
  - `git diff src/skills/architect-pairing-engine/SKILL.md` → the only hunks are the frontmatter block and the inserted paragraph; `## The deciding half` (including its spawn-trigger departure) and the load-rule paragraph at `:25-28` show no change.
