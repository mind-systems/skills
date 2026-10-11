# Plan: 78.4 — the hand rehydrates from the buffer and its predecessor's snapshot

## Context
Today `src/agents/editor.md` has a hand born fresh at every spawn, its spawn prompt giving only the buffer's own path, and it names no snapshot — so a new hand starts from the buffer alone. This change brings the agent definition in line with the governing spec `docs/paired-loop.md` § "How the memory begins, and how it survives" (a new hand "reads the buffer and that snapshot"), building on 78.2 (`architect-editor-engine` § "The architect's buffer" defines `editor/`, the hand's snapshots, beside `buffer.md`, the highest number being the latest) and 78.3 (`agent-architect` has the head replace its hand and ask it for its snapshot; the spawn prompt still carries the buffer's path and nothing else). After it, a hand, once the engine is loaded and before its first round, reads the buffer whole and the latest snapshot in `editor/` where one exists, and takes that snapshot as its own memory — after a replacement and after a death alike — with the head naming nothing beyond the buffer's path.

The task spec `.ai-factory/specs/trickster77777/0241-the-hand-rehydrates-from-the-buffer-and-its-predecessors-snapshot.md` pins the after-text verbatim under "What must be true after". Copy it from there byte for byte, keeping the backticks around `editor/`. The spec is the one home of the wording; this plan names the edit by its anchor and does not restate it.

Folder style: `editor.md`'s body is hard-wrapped prose at about 72–78 columns, paragraphs separated by one blank line. Wrap the new paragraph to the same width; rewrapping changes no words.

Scope: only `src/agents/editor.md` changes, and only by the one inserted paragraph. The frontmatter `description:` names no buffer or snapshot and stays as it is. The existing opening paragraph ("born fresh into this role at every spawn", "the spawn prompt gives you the buffer's own path") stays word for word — the spec's finding keeps both true. The closing paragraph of § "Self-verify, flag every judgment call, escalate ambiguity" ("You carry history across rounds … a fresh editor picking up from the next round alone must succeed just the same.") stays as it is; the spec does not touch it. `agent-architect` and `architect-editor-engine` are not edited: the spec's sweep finds their "buffer's own path" / "spawn prompt" sites still true of a path alone.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### `src/agents/editor.md` — the hand's start

- [x] **Insert the rehydration paragraph after the opening paragraph**
  Files: `src/agents/editor.md`
  - Find the opening paragraph under `# Editor — the two-mode half of the paired loop`, the one that opens "You are the **editor** — a persistent subagent" and ends "and it is where that memory lives.".
  - Directly after it, separated by one blank line on each side, insert the spec's pinned paragraph as a new paragraph: it opens "Before your first round, with the engine loaded, read the buffer whole" and closes "…and you read it the same after a replacement and after a death.". Strip the surrounding quotation marks the spec wraps it in; the paragraph itself carries none.
  - The next paragraph, opening "Each round is either a `REPORT-ONLY` channel-message", follows the new one unchanged.

- [x] **Verify the edit and the sweep** (depends on Insert the rehydration paragraph after the opening paragraph)
  Files: `src/agents/editor.md`
  - Run `git diff src/agents/editor.md`: the only change is the added paragraph; no existing line is altered. Collapse the new paragraph's wrapped lines and compare with the spec's quoted text — identical words and punctuation.
  - Run the spec's sweep (`grep -rn "buffer's own path" src docs CLAUDE.md`, `grep -rn "spawn prompt" src docs CLAUDE.md`, `grep -rn "born fresh" src docs CLAUDE.md`) and confirm the hits are exactly those the spec's "Finding" accounts for: `src/agents/editor.md` and the two `agent-architect` sites. Any other hit is a flag, not an edit.
