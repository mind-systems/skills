# Review — 36.2 — the buffer's creation is conditional, and it moves to the architect's own start

## Code Review Summary

**Files Reviewed:** `src/skills/agent-architect/SKILL.md` (the only source change, read in full — 263 lines), against the plan, spec 117, `docs/paired-loop.md` § "How the memory begins, and how it survives", `src/skills/architect-editor-engine/SKILL.md`, `src/agents/editor.md`, and specs 122/123 for the neighbour anchors.
**Risk Level:** 🟢 Low — one skill body, one section rewritten as prose; no frontmatter, no `loads:` edge, no engine or editor change.

### What landed, checked against the file

- § "Spawn once, message thereafter" now opens with the architect's own start, two steps in a fixed order: `architect-editor-engine` made resident via `Skill` first (reason kept: it holds the two formats and the buffer's definition; it is where the path, zones, and rules are defined, so it loads ahead of the buffer, and is in place long before a `REPORT-ONLY`/`APPLY-EDIT` message is composed), then the buffer as a conditional — a memory snapshot naming a buffer means work in it, the same memory resumed; no such pointer means a new architect creates its own first, at the path and numbering the engine defines — closing "Either way the buffer exists before any editor does." This is the governing spec's rule, restated in the skill's second-person register and without restating the engine's path or numbering.
- The snapshot ↔ handoff bridge is present: "a memory snapshot naming a buffer — the handoff below that carries your buffer's path —". "below" resolves: the handoff paragraph is the third paragraph of the same section. The bridge names the artifact, not a compact or "pre-compact", so 36.5's rework of the occasion leaves it true.
- The "work alone" sentence now reads "you work alone — holding your buffer, no editor's hand yet —"; "hand" is the file's existing figure for the editor (intro paragraph), and `\bhead\b` occurs 0 times in the file (the one `grep -c head` hit is "ahead").
- The old engine-load paragraph is gone; "Before that first channel-message" occurs 0 times. Every fact it carried is in the start paragraph — nothing was dropped and no second load moment survives.
- The spawn-moment sentence is shortened to the handle write: "write its handle into the buffer — a write into a file that exists by then, whichever of the two starts above you came through." "if it does not exist yet" occurs 0 times. The `name:` clause and the pairing-role recording moment after it are byte-identical.
- The sentence "The first channel-message is the spawn — … its content *is* the spawn prompt; there is no spawn before one exists." is byte-identical (36.4's anchor). The handoff paragraph and § "On every invocation" are byte-identical (36.5's surface). The recovery paragraph with the `agent-<id>.meta.json` fallback, the dead-editor paragraph, § "Your buffer is yours alone", and the frontmatter (diffed against HEAD) are unchanged.
- Cross-references still resolve: the three by-name references to "Spawn once, message thereafter" (intro, § "Relay on the marker…" "loaded once at birth — see …", § "Your buffer is yours alone") all point at a section that still holds the engine load and the recording moments; the engine's own "the architect per the instruction in its own body" still finds the instruction. `.ai-factory/notes/<NN>-architect-buffer.md` occurs 0 times in `agent-architect` — the engine remains its only home under `src/`.
- `git diff --stat` on `src/` and `docs/`: only `src/skills/agent-architect/SKILL.md`. No tabs, no trailing whitespace introduced (the diff's blank-line hits are context lines). Body 263 lines, far under 500. `active/skills/agent-architect` is a symlink into `src/`, so `~/.claude` loads the edit as-is. Buffer files under `.ai-factory/notes/` untouched.

### Critical Issues

None.

### Findings

None.

### Notes (non-blocking)

- Line 68 ("starts above you came through.") is a short line followed on line 69 by the untouched "Where the running build exposes …" — the paragraph was not re-wrapped past the edited sentence. That is exactly what the plan asked ("Re-wrap only the edited sentence's lines"), and Markdown renders it as one paragraph; cosmetic only, and leaving the following lines byte-identical keeps 36.4's landing zone stable.
- The anchor 36.4 quotes, `write its handle into the buffer`, is split across a line break in this file ("write its handle into the\nbuffer") — as it already was at HEAD before this task. A line-wise grep counts 0 both before and after; the words are present verbatim on lines 66–67. Not a regression; 36.4's implementer should match across the wrap.

### Positive Notes

- The rewrite reads as one sequence — start (engine → buffer) → work alone until the spawn → handoff → handle write into an existing buffer → liveness → dead editor — with no rule stated twice and no timing stated two ways.
- The reason for loading the engine ahead of the buffer ("it is where your buffer's path … are defined") is stated at the point of reliance, one sentence, no restatement of the engine's content — the always-loaded-discipline shape ARCHITECTURE.md asks for.
- Scope fences held: nothing from 36.3–36.6 leaked in (no isolation rule, no path-giving to the editor, no on-request snapshot, no write occasion or announce obligation).

## Deferred observations

- Affects: `docs/paired-loop.md` § "How the memory begins, and how it survives" / phase 36 (36.4, 36.5) — carried forward from plan-review 2, unchanged by the implementation: the recovery paragraph in § "Spawn once, message thereafter" already anticipates an architect that holds no pointer while a buffer with its handle exists ("recorded into a buffer whose path did not reach you — an auto-compact that fired before any handoff was written, or a handoff addressed elsewhere") and recovers the *handle* from `agent-<id>.meta.json`. Under the new start paragraph that architect is "a new architect" and creates a fresh buffer, then re-addresses the old editor, which (after 36.4) still holds the old buffer's path and re-reads the old settled zone — the pair silently diverges on which file is the shared memory. The governing spec assigns the no-pointer case unconditionally to a new head, so this task implements it faithfully; whether a recovered handle should lead the architect back to the buffer it was recorded in, or whether 36.5's on-request snapshot narrows the window enough, is a decision for the governing spec, not this task's file.

REVIEW_PASS
