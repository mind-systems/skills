# Plan: agent-architect: pre-compact handoff record names the buffer path

## Context
Close a state-recovery hole in `agent-architect`: the pre-compact handoff mandate records the editor but not the architect's per-session buffer, so a post-compact architect has no pinned way to find it. Add one sentence naming the buffer path.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Handoff-record mandate

- [x] **Task 1: Name the buffer path in the pre-compact handoff record**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn the editor once, message it thereafter" (the handoff-record paragraph, currently lines 53–58 beginning "Before a compact, your handoff must record the editor: ..."), add exactly one sentence stating that the handoff also names the buffer path (`.ai-factory/notes/<NN>-architect-buffer.md`), so the re-invoked architect resumes both halves of its state — the editor (handle/digest/recovery) and the buffer (path). Do NOT change anything else: no buffer genres, no lifetime prose, no invocation-time scanning — the buffer stays the architect's ungoverned private file. Everything else in the skill (buffer section, disciplines, lifecycle, parallel review, languages, greenlight, frontmatter) stays byte-identical. Keep the body ≤ 500 lines.
  Verify: `grep -n "buffer" src/skills/agent-architect/SKILL.md` shows the buffer path inside that section; `git diff` is a one-sentence addition with no other hunks.
