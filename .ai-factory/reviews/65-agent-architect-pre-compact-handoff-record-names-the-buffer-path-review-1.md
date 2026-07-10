# Review: agent-architect: pre-compact handoff record names the buffer path

## Scope
Reviewed the code change against the plan and spec `19-agent-architect-buffer-genres.md`.
Sole product change: `src/skills/agent-architect/SKILL.md` (§ "Spawn the editor once, message it thereafter").

## What changed
One sentence appended to the handoff-record paragraph (lines 58–60):

> The handoff must also name your buffer's path (`.ai-factory/notes/<NN>-architect-buffer.md`), so the re-invoked architect can find it.

## Correctness checks

- **Matches the spec exactly.** The spec mandated one sentence naming the buffer path so the re-invoked architect resumes both halves of its state (editor + buffer). The added sentence does exactly that and nothing more — no buffer genres, no lifetime prose, no invocation-time scanning.
- **Path is consistent.** `.ai-factory/notes/<NN>-architect-buffer.md` is byte-identical to the path already used in the buffer section (line 122). No drift between the two mentions.
- **Placement is correct.** The sentence sits inside the named section, appended after "Recording it is not optional." — the natural end of the editor-recording mandate.
- **Guards honored.** `git diff` shows a single hunk in this file — one added sentence, no other edits. Everything else (buffer section, disciplines, lifecycle, parallel review, languages, greenlight, frontmatter) is byte-identical. Body is 160 lines, well under the ≤500 limit.
- **Verification commands pass.** `grep -n "buffer"` surfaces the path inside the section; the diff is a one-sentence addition with no other hunks.

## Runtime / behavior
This is a skill instruction file (natural-language operating discipline), not executable code — no migrations, types, or race conditions apply. The instruction is unambiguous and self-consistent.

## Notes (non-findings)
Line 153 ("...the pre-compact handoff that recorded your editor's handle") still mentions only the editor's handle in the rehydration note. This is not a defect: the spec constrained the change to exactly one sentence in the handoff-record mandate, and line 153 remains accurate (the handoff does record the editor's handle among other things). Expanding it would violate the one-sentence guard.

REVIEW_PASS
