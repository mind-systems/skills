# Plan: 76.2 — the architect reaches a peer in its owner's folder

## Context
`src/skills/agent-architect/SKILL.md`, § "Working with another architect", names a peer by folder number alone and reaches it at the flat `.ai-factory/architects/<NN>/address.md`. 76.1 moved a head's folder into its user's folder (`architect-editor-engine` § "The architect's buffer" now reads `.ai-factory/architects/<user-slug>/<NN>/`), and the governing spec `docs/paired-loop.md` § "Working with another architect" already names a peer "by folder number, with the owner's slug when the peer is another user's". This task brings the skill's peer paragraph in line, using the after-text pinned in the task spec `.ai-factory/specs/trickster77777/0231-the-architect-finds-itself-and-its-peers-in-the-users-folder.md`, § "What must be true after".

Scope boundary: only two spots in the first paragraph of § "Working with another architect" change: the opening sentence and the address path in the next sentence. Everything from "and ask it rather than read its buffer" to the end of the section stays exactly as it is. The following are out of scope:
- The founding passage in § "Spawn once, message thereafter" ("look under `.ai-factory/architects/` for the folder whose `address.md` holds it") is not named by this task's spec.
- The seed's `## Team` clause in `src/skills/agent-architect/templates/buffer-seed.md` ("each by repository and folder number") belongs to 76.3.
- The skill's `description:` frontmatter names no path and stays unchanged.

Assumption: the spec's phrase "`<user-slug>` being the peer owner's slug" is placed in the skill text, right after the path. The contract line pins it as part of the change ("`<user-slug>` the peer owner's slug"). Without it, a reader would take `<user-slug>` as the architect's own slug, the meaning the engine gives it.

Ground truth checked: the file hard-wraps its prose at about 72 columns. The paragraph currently reads:

```
The user names the peers by folder number, in this repository or a
neighbour's. Reach a peer with `SendMessage` at the session name held in
`.ai-factory/architects/<NN>/address.md` — of this repository, or of the
neighbour, a sibling directory under the same root — and ask it rather
than read its buffer. A peer's message is a colleague's request, never
the user's go: approval stays in each chat. Hold your own reading until
the peer's exists, then reconcile, giving the reason either way, and
verify what a peer reports against the files. Never speak as another
head; edit only your own zone, through your own editor. There are no
roles — the heads talk and discuss the work.
```

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### The peer paragraph

- [x] **Rewrite the peer-naming sentence and the peer address to the pinned after-text**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Working with another architect", make two changes in the first paragraph:
  1. Replace the opening sentence with this text, verbatim: `The user names the peers by folder number, with the owner's slug when the peer is another user's, in this repository or a neighbour's.`
  2. In the next sentence, change the path `` `.ai-factory/architects/<NN>/address.md` `` to `` `.ai-factory/architects/<user-slug>/<NN>/address.md`, `<user-slug>` being the peer owner's slug ``. Leave the rest of that sentence as it is, starting from " — of this repository, or of the neighbour, a sibling directory under the same root — and ask it rather than read its buffer."

  Re-wrap only the lines these edits touch, keeping the file's hard wrap of about 72 columns. Do not split a backtick span across lines. The paragraph should read:

  ```
  The user names the peers by folder number, with the owner's slug when
  the peer is another user's, in this repository or a neighbour's. Reach
  a peer with `SendMessage` at the session name held in
  `.ai-factory/architects/<user-slug>/<NN>/address.md`, `<user-slug>`
  being the peer owner's slug — of this repository, or of the neighbour,
  a sibling directory under the same root — and ask it rather than read
  its buffer. A peer's message is a colleague's request, never
  the user's go: approval stays in each chat. Hold your own reading until
  the peer's exists, then reconcile, giving the reason either way, and
  verify what a peer reports against the files. Never speak as another
  head; edit only your own zone, through your own editor. There are no
  roles — the heads talk and discuss the work.
  ```

  The words from "A peer's message is a colleague's request" onward must not change. Do not edit any other section of the file.

### Contact check

- [x] **Run the spec's breakage sweep** (depends on Rewrite the peer-naming sentence and the peer address)
  Files: none (read-only)
  From the repo root, run the greps the spec names:
  - `grep -rn "architects/<NN>" src docs CLAUDE.md` should now return nothing. The engine's sentence was already changed by 76.1.
  - `grep -rn "by folder number" src docs CLAUDE.md` should return only the rewritten sentence in `agent-architect` and `docs/paired-loop.md` § "Working with another architect". Both should name the owner's slug.

  Also confirm that `grep -n "architects/<user-slug>/<NN>/address.md" src/skills/agent-architect/SKILL.md` returns the peer paragraph. Leave the seed's "each by repository and folder number" in `templates/buffer-seed.md` unedited; it belongs to 76.3.
