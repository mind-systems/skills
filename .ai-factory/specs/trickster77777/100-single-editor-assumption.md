# agent-architect: the single-editor assumption, and the applying half's start

26.8 corrected one sentence that assumed an apply work-order always addresses the architect's own editor. The same assumption stands in two more places in the same file, one of them a few lines above the corrected sentence and one of them the section that enforces verification-by-fact — where it silently exempts the deciding half from the duty. Separately, the pairing skill gives the deciding half a whole paragraph on its spawn trigger and the applying half nothing, though the applying half faces the same question from the other side.

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md:179-180`, opening the round-closing section:

> "A round opens when a channel-message goes out and closes when the editor's report on it comes back."

For the deciding half a round closes on the paired architect's report, relayed through the user; its own editor no longer runs `APPLY-EDIT` rounds at all (`architect-pairing-engine:35-36`).

`src/skills/agent-architect/SKILL.md:209` and `:211-215`, heading and paragraph:

> "## Verify the editor's report by fact
>
> When the editor reports done on an `APPLY-EDIT` round, run your own greps and reads against the real files..."

The trigger names a round the deciding half's research-only editor never has, so the section reads as not applying to it — while the duty it states is exactly what the deciding half owes the paired architect's report.

`src/skills/agent-architect/SKILL.md:212` is 103 characters under `python3 len()` (105 under `awk length()`, which counts the em-dash's three bytes) — the file's widest body line. It predates this phase and falls inside the paragraph change 3 rewrites, so the rewrap retires it as a side effect rather than as a goal.

`src/skills/architect-pairing-engine/SKILL.md:57-73`, "## The applying half", states what it does with an arriving work-order and never how it recognizes or starts on one. The deciding half gets `:50-55` for exactly that question. The generic spawn trigger names "the first authored apply work-order" (`agent-architect:34-35`), and whether composing an arriving decision counts as authoring is nowhere stated.

## The change

Four edits across two files.

1. In `agent-architect/SKILL.md`, replace the sentence at `:179-180` word-for-word with:

   A round opens when a channel-message goes out and closes when the report on
   it comes back — from your editor, or, for the deciding half of a pairing,
   from the paired architect through the user.

2. In `agent-architect/SKILL.md`, replace the heading at `:209` word-for-word with:

   ## Verify the report by fact

3. In `agent-architect/SKILL.md`, replace the whole paragraph at `:211-215` word-for-word with:

   When a report comes back on an `APPLY-EDIT` round — from your editor, or
   from the paired architect when you are the deciding half — run your own
   greps and reads against the real files: confirm the substance landed,
   cross-references and family-references stayed intact, nothing drifted past
   the work-order, and check the reporter's own judgment calls the same way,
   on the file, not on the note. Surface the evidence, not a "looks good."

4. In `architect-pairing-engine/SKILL.md` § "The applying half", append to the end of the first paragraph (which ends "...where the work-order's content comes from."):

   Composing an arriving decision into that `APPLY-EDIT` is authoring it, so
   the generic spawn trigger applies here unchanged, both alternatives intact.
   An arriving work-order carries no `::` and needs none: this half authors
   rather than relays, and the marker governs relays alone.

## Files & types

- edit: `src/skills/agent-architect/SKILL.md` — `:179-180`, `:209`, `:211-215`.
- edit: `src/skills/architect-pairing-engine/SKILL.md` — § "The applying half", first paragraph only.

## Guards

- `:185-187`'s paired-architect clause, added by 26.8, is already correct and stays word-for-word.
- Both `description:` fields untouched. `agent-architect`'s describes the unpaired default, which the pairing skill departs from by declaration; that is not this task's subject.
- `## The deciding half` untouched in full, including its own spawn-trigger paragraph.
- `src/agents/editor.md` and `src/skills/architect-editor-engine/SKILL.md` untouched — the editor never needs to know which half its architect plays.
- The round-closing invariant and the verification duty are unchanged in substance; only their addressee widens from "the editor" to whoever reported.
- New prose wraps to 76 characters. Do not split a hyphenated word across a line break: `cross-references` and `family-references` each stay whole.

## Verification

Every phrase count below is taken against a whitespace-normalized read of the file — never a line-oriented `grep`. These files are hard-wrapped, so any phrase may straddle a line break and a line-oriented count then returns 0 whether the phrase is present or not: a check that cannot fail. Count with `python3 -c "import re,sys; print(re.sub(r'\s+',' ',open(sys.argv[1],encoding='utf-8').read()).count(sys.argv[2]))" <path> "<phrase>"`.

- "closes when the editor's report on it comes back" in `src/skills/agent-architect/SKILL.md` → 0
- "## Verify the editor's report by fact" in `src/skills/agent-architect/SKILL.md` → 0
- "When the editor reports done on an `APPLY-EDIT` round" in `src/skills/agent-architect/SKILL.md` → 0
- "from the paired architect through the user" in `src/skills/agent-architect/SKILL.md` → 1
- "## Verify the report by fact" in `src/skills/agent-architect/SKILL.md` → 1
- "check the reporter's own judgment calls" in `src/skills/agent-architect/SKILL.md` → 1
- "for the deciding half of a pairing, the paired architect" in `src/skills/agent-architect/SKILL.md` → 1, unchanged from 26.8
- "is authoring it" in `src/skills/architect-pairing-engine/SKILL.md` → 1
- "the marker governs relays alone" in `src/skills/architect-pairing-engine/SKILL.md` → 1
- No line this task writes or rewraps exceeds 76 characters under `python3 len()` — the paragraph replaced by change 3, the sentence replaced by change 1, and the clause appended by change 4. This is the round's own delta, not the file's absolute state: `:19` and `:80` are 79 characters, predate this task, are outside its scope, and stay exactly as they are.
- Every paragraph rewrapped has the same words as before, bar the pinned substitutions: compare its whitespace-normalized word sequence against `git show HEAD:<path>`.
- `git diff HEAD --stat -- src/ .ai-factory/roadmaps/` lists exactly `src/skills/agent-architect/SKILL.md`, `src/skills/architect-pairing-engine/SKILL.md` and the roadmap — scoped so the check is invariant to any other file's tracking state.
- No count above is trusted as evidence until it was taken by the normalized method named at the head of this section.
