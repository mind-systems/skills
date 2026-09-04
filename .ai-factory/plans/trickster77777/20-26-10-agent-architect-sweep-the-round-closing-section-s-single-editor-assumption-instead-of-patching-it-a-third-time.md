# Plan: 26.10 — agent-architect: sweep the round-closing section's single-editor assumption instead of patching it a third time

## Context
Three passes (26.8, 26.9) widened the round-closing section's "the reporter is always your own editor" assumption one sentence at a time, and 26.9 left the section self-contradicting — the heading at `:177` still says a round closes on *the editor's* report, two lines above the sentence that denies it. This task closes the last two carriers, the heading and the reasoning paragraph's "the editor's independence", so a fourth pass has nothing left to find.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Grounded state (read fresh at plan time)
`src/skills/agent-architect/SKILL.md` at HEAD:

- `:177` — `## Nothing closes a round before the editor's report exists` (the heading, 59 chars).
- `:179-185` — the round-closing paragraph 26.9 widened; already reads "…closes when the report on it comes back — from your editor, or, for the deciding half of a pairing, from the paired architect through the user."
- `:187-192` — the apply-work-order paragraph 26.8 widened; already carries "or, for the deciding half of a pairing, the paired architect".
- `:193` and `:199` — blank lines bracketing the target paragraph.
- `:194-198` — the reasoning paragraph, opening "The reason is the editor's independence."
- `:213-214` — the verify paragraph 26.9 widened; already carries "from the paired architect when you are the deciding half".

The spec's line numbers (`:177`, `:194-198`) match the file exactly — no drift, no re-anchoring needed.

**Heading rename ripples nowhere.** `grep -rn "Nothing closes a round" src/ docs/ CLAUDE.md` across the grove returns exactly one hit: the definition line `src/skills/agent-architect/SKILL.md:177` itself. Other occurrences live only in `.ai-factory/specs/`, `plans/`, `plan-reviews/` and `reviews/` — historical artifacts of 26.3/26.9, strata that record their own moment and are never rewritten. This satisfies the spec's "Confirm before renaming" guard; re-run the grep at execution time before editing.

## Width check — the round's delta, not the file's absolute state
The file already carries pre-existing over-76 lines outside this task's hunks. Measured under `python3 len()` (decoded text — never `awk length()` or `wc -m`, which count bytes and read a 3-byte em-dash as three): `:4-8`, `:13`, `:19-21`, `:23`, `:80`, `:82`, `:119`, `:196`. All stay byte-identical **except `:196` (77), which sits inside the paragraph task 2 replaces whole** and therefore necessarily disappears. That retirement is a side effect of the reword, not a goal — nothing else in the file is rewrapped to chase width.

Both pinned blocks below are already wrapped to ≤76 under `python3 len()` (heading 56; paragraph 70/75/76/70/72/42). **Reproduce them verbatim — do not rewrap them, and do not split a hyphenated word across a line break.**

## Tasks

### agent-architect — the heading names whoever reported

- [x] **Rename the round-closing section heading**
  Files: `src/skills/agent-architect/SKILL.md`
  Replace the heading at `HEAD:177` — the line reading `## Nothing closes a round before the editor's report exists` — with exactly:

  ```
  ## Nothing closes a round before the report on it exists
  ```

  One line in, one line out — nothing below shifts. This is the spec's edit 1, pinned word-for-word; do not paraphrase or re-order it. Before editing, re-run `grep -rn "Nothing closes a round" src/ docs/ CLAUDE.md` and confirm the only hit under `src/` is this definition line, so no pointer needs updating alongside the rename.

  Guard: the paragraph directly below (`:179-185`, widened by 26.9, opening "A round opens when a channel-message goes out") is not part of this hunk and stays word-for-word and line-for-line, including `:180`'s "from your editor, or, for the deciding half of a pairing".

### agent-architect — the reasoning names the second reader

- [x] **Widen the reasoning paragraph to the second reader** (depends on Rename the round-closing section heading)
  Files: `src/skills/agent-architect/SKILL.md`
  Replace `HEAD:194-198` — the whole paragraph between the blank lines at `:193` and `:199`, opening "The reason is the editor's independence." and ending "…keeps the reconcile step worth doing." — with exactly:

  ```
  The reason is the second reader's independence — your editor's, or the
  paired architect's when you are the deciding half. That pass is signal only
  while it is uncontaminated by yours; once your read has been released in any
  form, its agreement can no longer be told from an echo, and the second
  reading you were waiting on returns nothing. Holding the announcement is
  what keeps the reconcile step worth doing.
  ```

  The heading rename above shifts nothing, so this paragraph still sits at `:194-198` at execution time. Five lines become six, shifting `## Review in parallel, reconcile before the apply order` and everything after it by **+1** — those sections are untouched.

  Only the opening sentence changes words: "the editor's independence" becomes "the second reader's independence" plus the naming clause, and the follow-on "Its pass" becomes "That pass" because the antecedent is now the two-item clause rather than a single editor. Everything from "is signal only while it is uncontaminated by yours" onward keeps its words exactly and moves only its line breaks. The em-dash is a real `—` (U+2014), not `--`.

  Guard: the paragraph above (`:187-192`, the apply-work-order clause 26.8 settled, opening "An apply work-order closes a round as finally as a verdict") is not part of this hunk and stays word-for-word and line-for-line, including `:188`'s paired-architect clause. Guard: `:213`'s "from the paired architect when you are the deciding half" is far below the hunk and stays word-for-word.

### The sweep's record — already written, nothing to author

- [x] **Confirm the "why every other mention stays" record is in place** (depends on Widen the reasoning paragraph to the second reader)
  Files: `.ai-factory/specs/trickster77777/101-round-closing-sweep.md` (read-only)
  The contract line's second half — "record in the spec why every other mention stays" — is **already discharged** by the spec itself: § "Why the file's other mentions of the editor are correct as they stand" classifies every remaining editor mention into three groups (own-editor subagent mechanics identical for both halves; every `REPORT-ONLY` relay identical for both halves; `:22-27` and `:155-161` overridden by declaration in `architect-pairing-engine:41-42` and `:36-40`). Read that section and confirm it is present. **Write nothing** — no new note, no edit to the spec, no third mention widened in `SKILL.md`. Any widening beyond the two pinned edits is the implementer originating scope; the classification exists precisely so those mentions stay.

### Verify

- [x] **Run the spec's verification list** (depends on Confirm the "why every other mention stays" record is in place)
  Files: `src/skills/agent-architect/SKILL.md`
  Every phrase count is taken against a **whitespace-normalized** read — never a line-oriented `grep`. This file hard-wraps at 76, so any phrase may straddle a line break and a line-oriented count then returns 0 whether the phrase is present or not: a check that cannot fail. Use:

  ```bash
  count() { python3 -c "import re,sys; print(re.sub(r'\s+',' ',open(sys.argv[1],encoding='utf-8').read()).count(sys.argv[2]))" "$1" "$2"; }
  ```

  Expected, in `src/skills/agent-architect/SKILL.md`:
  - `Nothing closes a round before the editor's report exists` → 0
  - `The reason is the editor's independence` → 0
  - `Nothing closes a round before the report on it exists` → 1
  - `The reason is the second reader's independence` → 1
  - `paired architect's when you are the deciding half` → 1
  - `from the paired architect through the user` → 1, **unchanged from 26.9** — the guard on `:180`
  - `for the deciding half of a pairing, the paired architect` → 1, **unchanged from 26.8** — the guard on `:188`
  - `from the paired architect when you are the deciding half` → 1, **unchanged from 26.9** — the guard on `:213`

  Then:
  - **Width:** every line *added* by `git diff HEAD -- src/` is ≤76 under `python3 len()` — that is the heading and the six rewritten paragraph lines. No pre-existing over-width line outside the rewritten hunk changes; see § Width check for the exact list. `:196` is inside the hunk and is expected to go.
  - **Word preservation:** compare the rewritten paragraph's whitespace-normalized word sequence against the same paragraph in `git show HEAD:src/skills/agent-architect/SKILL.md` — the difference must be exactly the pinned substitution ("the editor's independence." → "the second reader's independence — your editor's, or the paired architect's when you are the deciding half." and "Its pass" → "That pass") and nothing else. A width check alone cannot see a word dropped in a rewrap.
  - **Scope:** `git diff HEAD --stat -- src/ .ai-factory/roadmaps/` lists exactly `src/skills/agent-architect/SKILL.md` and the roadmap. `git diff HEAD -- src/skills/architect-pairing-engine/SKILL.md src/agents/editor.md src/skills/architect-editor-engine/SKILL.md` is empty — this task is confined to one file. The `description:` field (`:3-9`) shows no diff, and the whole diff is exactly two hunks.
  - No count above is evidence until it was taken by the normalized method named at the head of this task; a number from a line-oriented `grep` is not evidence, whatever it returned.
