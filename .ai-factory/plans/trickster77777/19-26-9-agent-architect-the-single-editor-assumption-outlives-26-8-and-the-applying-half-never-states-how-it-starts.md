# Plan: 26.9 — agent-architect: the single-editor assumption outlives 26.8, and the applying half never states how it starts

## Context
26.8 widened one sentence's addressee from "the editor" to "the editor or the paired architect", and left the same single-editor assumption standing in the two neighbours that decide when a round closes (`agent-architect:179-180`) and when the verify-by-fact duty fires (`:209`, `:211-215`) — the second silently exempting the deciding half, whose research-only editor never has an `APPLY-EDIT` round to report on. This task widens all three to name either reporter, and closes the asymmetry one file over: `architect-pairing-engine`'s applying half gains the spawn-trigger statement its deciding counterpart already has.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## How to read the line numbers
**Every line number below is a `HEAD` coordinate — an anchor, not an address.** The edits shift each other; each task therefore also names the text it anchors on (the quoted opening words, "the paragraph between the blank lines at …"), and where a number and its text anchor disagree at execution time, **the text anchor wins**. Tasks carry `depends on` edges fixing one total order, and each downstream task states where its target sits *at execution time* under that order.

## Grounded state (read fresh, confirms the spec)
`src/skills/agent-architect/SKILL.md` at HEAD: the round-closing paragraph is `:179-183`; the paired-architect paragraph 26.8 settled is `:185-190`; the section heading is `:209`; the verify paragraph is `:211-215`. `src/skills/architect-pairing-engine/SKILL.md` § "The applying half" opens at `:57`, its first paragraph is `:59-64` ending "…where the work-order's content comes from." Neither heading this task touches is cross-referenced anywhere: `grep -rn "Verify the editor's report\|Nothing closes a round" src/ docs/ CLAUDE.md` returns only the two definition lines themselves, so renaming `:209` breaks no pointer.

## Assumption (width check, pinned here)
The spec's width check is explicitly the round's own delta, not the file's absolute state. Both files already carry pre-existing over-76 lines outside this task's hunks. Read the check as:

- **every line added by `git diff HEAD -- src/` is ≤76** under `python3 len()` (decoded text — never `awk length()` or `wc -m`, which count bytes and read a 3-byte em-dash as three);
- **no pre-existing over-width line outside the rewritten hunks changes.** That list, measured under `python3 len()`: `agent-architect` `:4-8`, `:13`, `:19-21`, `:23`, `:80`, `:82`, `:119`, `:194`; `architect-pairing-engine` `:31` (the `grep` code span). All stay byte-identical.

`agent-architect:212` (103) and `:213` (78) are *inside* the paragraph task 3 replaces whole, so they necessarily disappear. That retirement is a side effect of the reword, not a goal — nothing else in the file is rewrapped to chase width.

## Tasks

### agent-architect — the round closes on whoever reported

- [x] **Widen the round-closing sentence's reporter**
  Files: `src/skills/agent-architect/SKILL.md`
  Replace `HEAD:179-183` — the paragraph between the blank lines at `:178` and `:184`, opening "A round opens when a channel-message goes out and closes when the editor's" — with exactly:

  ```
  A round opens when a channel-message goes out and closes when the report on
  it comes back — from your editor, or, for the deciding half of a pairing,
  from the paired architect through the user. Between those two moments
  nothing that closes the round leaves your hands — not a summary of the
  payload, not a verdict on it, not an apply work-order. Your own parallel
  pass runs through that window exactly as it always does: what waits is the
  announcement, never the work.
  ```

  Only the paragraph's opening sentence changes words; everything from "Between those two moments" on keeps its words exactly and moves only its line breaks, because the longer opening sentence rewraps the paragraph. Five lines become seven, shifting everything below by **+2**.

  Guard: the *next* paragraph (`HEAD:185-190`, the paired-architect clause 26.8 settled, opening "An apply work-order closes a round as finally as a verdict") is not part of this hunk and stays word-for-word and line-for-line. Guard: the section heading at `HEAD:177` — "## Nothing closes a round before the editor's report exists" — is **not** in this task's scope and stays word-for-word; the spec enumerates four edits and this heading is not one of them.

### agent-architect — the verify duty fires on any report

- [x] **Rename the verify heading** (depends on Widen the round-closing sentence's reporter)
  Files: `src/skills/agent-architect/SKILL.md`
  Replace the heading `HEAD:209` — "## Verify the editor's report by fact", sitting at **`:211` at execution time** after the previous task's +2 — with exactly:

  ```
  ## Verify the report by fact
  ```

  One line in, one line out — no further shift. Nothing links to this heading (see § Grounded state), so no pointer needs updating alongside it.

- [x] **Widen the verify paragraph to any reporter** (depends on Rename the verify heading)
  Files: `src/skills/agent-architect/SKILL.md`
  Replace `HEAD:211-215` — the whole paragraph under that heading, opening "When the editor reports done on an `APPLY-EDIT` round, run your own greps" and ending "evidence, not a \"looks good.\"" — sitting at **`:213-217` at execution time**, with exactly:

  ```
  When a report comes back on an `APPLY-EDIT` round — from your editor, or
  from the paired architect when you are the deciding half — run your own
  greps and reads against the real files: confirm the substance landed,
  cross-references and family-references stayed intact, nothing drifted past
  the work-order, and check the reporter's own judgment calls the same way,
  on the file, not on the note. Surface the evidence, not a "looks good."
  ```

  This block is already wrapped to ≤76 — **reproduce it verbatim, do not rewrap it.** Do not split `cross-references` or `family-references` across a line break; the block above already keeps each whole. The trigger widens from "the editor reports done" to "a report comes back", so the deciding half's duty toward the paired architect's report stops reading as exempt; the duty itself is unchanged in substance, and the em-dash clause replaces the old dash-run so the sentence still reads as one. Five lines become six, shifting § "Your buffer is yours alone" and everything after it by a further +1 — those sections are untouched.

### architect-pairing-engine — the applying half states how it starts

- [x] **Append the spawn-trigger clause to the applying half's first paragraph**
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  In § "The applying half" (`HEAD:57`), extend the first paragraph (`HEAD:59-64`) — the one ending "…the only departure is where the work-order's content comes from." Lines `HEAD:59-63` stay **byte-identical**; replace line `HEAD:64` (`content comes from.`) with exactly:

  ```
  content comes from. Composing an arriving decision into that `APPLY-EDIT` is
  authoring it, so the generic spawn trigger applies here unchanged, both
  alternatives intact. An arriving work-order carries no `::` and needs none:
  this half authors rather than relays, and the marker governs relays alone.
  ```

  One line becomes four, shifting everything below by **+3**. The clause answers, for this half, the question `:50-55` already answers for the deciding half — and answers it the opposite way: the deciding half loses the second spawn alternative, this half keeps both, because composing an arriving decision into an `APPLY-EDIT` *is* authoring one. The `::` sentence forecloses the natural misread that an arriving work-order is a relay needing the marker.

  Guard: § "The deciding half" (`HEAD:33-55`) is untouched in full, including its own spawn-trigger paragraph `:50-55`. Guard: the check paragraph `HEAD:66-72` ("Applying exactly is not obeying blindly") is untouched — it is a separate paragraph and this task extends only the first. Guard: the `description:` field (`:3-14`) is untouched; `:31` stays exempt and byte-identical. This edit is independent of the three above and may run before or after them; only its own file shifts.

### Verify

- [x] **Run the spec's verification list** (depends on Widen the verify paragraph to any reporter, Append the spawn-trigger clause to the applying half's first paragraph)
  Files: `src/skills/agent-architect/SKILL.md`, `src/skills/architect-pairing-engine/SKILL.md`
  Every phrase count is taken against a **whitespace-normalized** read — never a line-oriented `grep`. These files hard-wrap at 76, so any phrase may straddle a line break, and a line-oriented count then returns 0 whether the phrase is present or not: a check that cannot fail. Use:

  ```bash
  count() { python3 -c "import re,sys; print(re.sub(r'\s+',' ',open(sys.argv[1],encoding='utf-8').read()).count(sys.argv[2]))" "$1" "$2"; }
  ```

  Expected, in `src/skills/agent-architect/SKILL.md`:
  - `closes when the editor's report on it comes back` → 0
  - `## Verify the editor's report by fact` → 0
  - `When the editor reports done on an \`APPLY-EDIT\` round` → 0
  - `from the paired architect through the user` → 1
  - `## Verify the report by fact` → 1
  - `check the reporter's own judgment calls` → 1
  - `for the deciding half of a pairing, the paired architect` → 1, **unchanged from 26.8** — this is the guard on `HEAD:185-187` surviving task 1's neighbouring rewrap

  Expected, in `src/skills/architect-pairing-engine/SKILL.md`:
  - `is authoring it` → 1
  - `the marker governs relays alone` → 1

  Then:
  - **Width:** every line *added* by `git diff HEAD -- src/` is ≤76 under `python3 len()`. No pre-existing over-width line outside the rewritten hunks changes — see § Assumption for the exact list; `agent-architect:212-213` are inside task 3's hunk and are expected to go.
  - **Word preservation:** for the paragraph task 1 rewraps, compare its whitespace-normalized word sequence against the same paragraph in `git show HEAD:src/skills/agent-architect/SKILL.md` — the difference must be exactly the opening sentence's pinned substitution and nothing else. A width check alone cannot see a word dropped in a rewrap. Same comparison for `architect-pairing-engine`'s first applying-half paragraph: the difference must be exactly the appended clause, with `:59-63` byte-identical.
  - **Scope:** `git diff HEAD --stat -- src/ .ai-factory/roadmaps/` lists exactly `src/skills/agent-architect/SKILL.md`, `src/skills/architect-pairing-engine/SKILL.md` and the roadmap — scoped so the check is invariant to any other file's tracking state. `git diff HEAD -- src/agents/editor.md src/skills/architect-editor-engine/SKILL.md` is empty: the editor never needs to know which half its architect plays. Both `description:` fields show no diff (`agent-architect:3-9`, `architect-pairing-engine:3-14`), and `agent-architect:177` shows no diff.
  - No count above is evidence until it was taken by the normalized method named at the head of this task; a number from a line-oriented `grep` is not evidence, whatever it returned.
