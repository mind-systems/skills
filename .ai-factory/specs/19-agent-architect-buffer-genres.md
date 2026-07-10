# agent-architect: pre-compact handoff record names the buffer path

## Current state

`src/skills/agent-architect/SKILL.md` § "Spawn the editor once, message it thereafter" mandates the pre-compact handoff record for the editor — the handle a message can reach it by, a digest, and the recovery path — but says nothing about the architect's buffer (`.ai-factory/notes/<NN>-architect-buffer.md`). The buffer is per-session and numbered, so a post-compact architect has no pinned way to find its predecessor's buffer: `command-handoff`'s meaning-tree transfer probably carries it, but "probably" is a hole.

## Change

One sentence added to that handoff-record mandate: the pre-compact handoff also names the **buffer path**, so the re-invoked architect resumes both halves of its state — the editor (handle/digest/recovery) and the buffer (path). Nothing else: no buffer genres, no lifetime prose, no invocation-time scanning — the buffer stays the architect's ungoverned private file exactly as written.

## Files & types

- edit `src/skills/agent-architect/SKILL.md` — one sentence in § "Spawn the editor once, message it thereafter"

## Guards

- **One sentence, one concern** — everything else in the skill is byte-identical: buffer section, disciplines, lifecycle, parallel review, languages, greenlight, frontmatter.
- Body stays ≤ 500 lines.

## Verification

- The handoff-record mandate lists the buffer path alongside the editor's handle/digest/recovery; `grep -n "buffer" src/skills/agent-architect/SKILL.md` shows it inside that section.
- `git diff` for the task is a one-sentence addition; no other hunks.
