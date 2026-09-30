# Plan: 64.1 — `agent-architect` drops the roles and gains the peer account

## Context
`src/skills/agent-architect/SKILL.md` still speaks of a pairing role, a deciding or applying half, and a paired architect, and has no account of working with a peer. After this task every such mention is gone or speaks of the editor alone, the `loads:` edge to `architect-pairing-engine` is dropped, and a new short section "Working with another architect" carries the peer account. Governing spec: `docs/paired-loop.md` § "Working with another architect". Task spec: `.ai-factory/specs/trickster77777/177-agent-architect-drops-the-roles-and-gains-the-peer-account.md` — its "What must be true after" section pins the target wording of every passage below; the implementer copies those pinned passages verbatim from the spec.

Assumption: 62.2 and 63.1 have landed (verified — the snapshot paragraph no longer carries the "Of the recorded state, only the buffer's path travels" sentence, and § "Your buffer is shared; you alone write it"'s first paragraph already ends with "The memory snapshot continuing you sits in your folder beside this buffer, …"; `allowed-tools` already holds `Read`, `SendMessage` and `ListAgents`). Only this one file changes. Per the spec's "What breaks on contact": "the paired loop" in the description and the title line, and "each half" in the handle paragraph ("so each half holds the other's address") name the architect↔editor loop, not a role — they stay. `architect-pairing-engine` itself, its `active/` symlink and `CLAUDE.md`'s lists are 64.2's scope and must NOT be touched here; `docs/`, `architect-editor-engine` and `src/agents/editor.md` stay unedited.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Strip the pairing roles from `agent-architect/SKILL.md`

- [x] **Frontmatter drops the pairing engine**
  Files: `src/skills/agent-architect/SKILL.md`
  The `loads:` line becomes exactly `loads: architect-editor-engine`. No other frontmatter field changes (`allowed-tools` already carries `SendMessage` and `ListAgents`).

- [x] **Handle paragraph ends at its `name:` sentence**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", the paragraph opening "At the moment you spawn the editor (see above), write its handle into the buffer" ends with "…since the parameter is absent from some builds and nothing contracts the name's behavior beyond the run." Delete the sentence starting "A pairing role the user assigns for the session (`architect-pairing-engine`'s deciding or applying half)" and everything after it in that paragraph (through "then write the role into the buffer."). The rest of the paragraph, including "so each half holds the other's address from the spawn on", stays byte-unchanged. Rewrap the last line to the file's existing ~75-column prose width.

- [x] **§ "Nothing closes a round before the report on it exists" speaks of the editor alone**
  Files: `src/skills/agent-architect/SKILL.md`
  Replace the section's three paragraphs with the spec's pinned text verbatim: the round "closes when the report on it comes back from your editor"; the apply work-order "is addressed to the editor rather than the user"; the reason is "the second reader's independence — your editor's." Every "deciding half", "pairing", and "paired architect" clause in the section disappears; the rest of each paragraph reads as the spec pins it (which matches the current wording otherwise). Heading unchanged. Wrap to the file's prose width.

- [x] **§ "Verify the report by fact" speaks of the editor alone**
  Files: `src/skills/agent-architect/SKILL.md`
  Replace the section's paragraph with the spec's pinned text verbatim: "When a report comes back on an `APPLY-EDIT` round from your editor, run your own greps and reads against the real files: …" — the dash clause "— from your editor, or from the paired architect when you are the deciding half —" goes; the remainder is unchanged.

- [x] **§ "Your buffer is shared; you alone write it" drops the pairing role**
  Files: `src/skills/agent-architect/SKILL.md`
  In the first paragraph, the list of what the buffer holds becomes "the editor's handle and the deferral entries below" (the "any pairing role the user has assigned for the session" item goes). In the second paragraph, "This is the occasion for every entry beyond the handle and the pairing role, both already timed above." becomes "This is the occasion for every entry beyond the handle, already timed above." Everything else in the section — including the 63.1 sentence "The memory snapshot continuing you sits in your folder beside this buffer, …" — stays as it reads.

### Add the peer account

- [x] **New section "Working with another architect"** (depends on the tasks above only for ordering within the file)
  Files: `src/skills/agent-architect/SKILL.md`
  Insert a new section `## Working with another architect` between § "The user rules the forks and owns the commits" and § "On every invocation", holding the spec's pinned paragraph verbatim and nothing more: peers named by folder number in this repository or a neighbour's; reach a peer with `SendMessage` at the session name held in `.ai-factory/architects/<NN>/address.md` — of this repository, or of the neighbour, a sibling directory under the same root — and ask it rather than read its buffer; a peer's message is a colleague's request, never the user's go, approval stays in each chat; hold your own reading until the peer's exists, then reconcile, giving the reason either way, and verify what a peer reports against the files; never speak as another head, edit only your own zone through your own editor; no roles — the heads talk and discuss the work. The spec states "The account is these sentences." — add no further rules, examples, or pointers. Wrap to the file's prose width.

- [x] **Sweep confirms no role mention remains** (depends on all tasks above)
  Files: `src/skills/agent-architect/SKILL.md`
  Run the spec's re-runnable sweep: `grep -n -i "pairing\|paired architect\|deciding half\|applying half" src/skills/agent-architect/SKILL.md`. The only surviving hits allowed are "paired plan-and-review loop" in the description and "the paired loop" in the title line; any other hit is a miss to fix in this file. Do not edit anything the second, repo-wide sweep reaches (the pairing engine and `CLAUDE.md` belong to 64.2; the remaining hits are ordinary uses of the word).
