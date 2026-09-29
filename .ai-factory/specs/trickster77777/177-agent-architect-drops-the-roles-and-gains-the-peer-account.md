# 64.1 — `agent-architect` drops the roles and gains the peer account

## What is true now

Phase 64 runs after phases 62 and 63, so `src/skills/agent-architect/SKILL.md` is read here as specs 175 and 176 leave it. They leave the passages below as the file has them, with two exceptions: spec 176 removes the snapshot paragraph's closing sentence, "Of the recorded state, only the buffer's path travels: the pointer, never a copy of the handle or of any assigned pairing role, both of which live in the buffer.", and rewrites the last sentence of § "Your buffer is shared; you alone write it"'s first paragraph to "The memory snapshot continuing you sits in your folder beside this buffer, and you rebuild from the two together — see "Spawn once, message thereafter" for the rest of what is recorded, when, and the liveness test at recovery; this section does not restate any of that." The pairing-role mentions those two carried are gone before this task starts.

The skill still speaks of a pairing role, a deciding or applying half, and a paired architect in these places:

- the frontmatter: `loads: architect-editor-engine architect-pairing-engine`;
- § "Spawn once, message thereafter", at the close of the paragraph on the editor's handle: "A pairing role the user assigns for the session (`architect-pairing-engine`'s deciding or applying half) gets a recording moment of its own: at the moment the user assigns it — which may be mid-session and need not coincide with the spawn — load `architect-pairing-engine` via the `Skill` tool if it is not already loaded, then write the role into the buffer.";
- § "Nothing closes a round before the report on it exists", in each of its paragraphs: the round "closes when the report on it comes back — from your editor, or, for the deciding half of a pairing, from the paired architect through the user"; the work-order is "addressed to the editor — or, for the deciding half of a pairing, the paired architect — rather than the user"; and the reason is "the second reader's independence — your editor's, or the paired architect's when you are the deciding half";
- § "Verify the report by fact": "When a report comes back on an `APPLY-EDIT` round — from your editor, or from the paired architect when you are the deciding half — run your own greps and reads against the real files";
- § "Your buffer is shared; you alone write it": the buffer holds "the editor's handle, any pairing role the user has assigned for the session, and the deferral entries below", and its entries are timed "for every entry beyond the handle and the pairing role, both already timed above".

The skill has no account of working with another architect. A neighbouring repository is a sibling directory under the coordination root, whose layout the root `CLAUDE.md` fixes ("from this root, the sibling repos are `skills/` and `orchestrator/` — always"), so a neighbour's folder is reached by the same `.ai-factory/architects/<NN>/` path under that sibling. Its `allowed-tools` line, as spec 175 leaves it, already holds `Read`, `SendMessage` and `ListAgents`. `docs/paired-loop.md` § "Working with another architect" states the behaviour the skill must come to hold, and the user's verdict on how much to write governs the size: "Чем больше правил агенту навешиваешь — тем сложней ему исполнять то что он делает лучше всего."

## What must be true after

Every place `agent-architect` speaks of a pairing role, a deciding or applying half, or a paired architect goes, or is rewritten to speak of the editor alone. The replacements read:

The frontmatter line is `loads: architect-editor-engine`.

The paragraph on the editor's handle in § "Spawn once, message thereafter" ends with its `name:` sentence, "…since the parameter is absent from some builds and nothing contracts the name's behavior beyond the run."; the sentence on a pairing role and everything after it in that paragraph are gone.

§ "Nothing closes a round before the report on it exists" reads:

> A round opens when a channel-message goes out and closes when the report on it comes back from your editor. Between those two moments nothing that closes the round leaves your hands — not a summary of the payload, not a verdict on it, not an apply work-order. Your own parallel pass runs through that window exactly as it always does: what waits is the announcement, never the work.
>
> An apply work-order closes a round as finally as a verdict, and it does so even though it is addressed to the editor rather than the user: where the round is settled is what counts, not who reads it. A relay and its work-order sent in one message therefore close the round before any report could exist: the same violation as an early summary, never an exception to it.
>
> The reason is the second reader's independence — your editor's. That pass is signal only while it is uncontaminated by yours; once your read has been released in any form, its agreement can no longer be told from an echo, and the second reading you were waiting on returns nothing. Holding the announcement is what keeps the reconcile step worth doing.

§ "Verify the report by fact" reads:

> When a report comes back on an `APPLY-EDIT` round from your editor, run your own greps and reads against the real files: confirm the substance landed, cross-references and family-references stayed intact, nothing drifted past the work-order, and check the reporter's own judgment calls the same way, on the file, not on the note. Surface the evidence, not a "looks good."

§ "Your buffer is shared; you alone write it" says the buffer holds "the editor's handle and the deferral entries below", and its entries are timed "for every entry beyond the handle, already timed above".

A new section carries the peer account, between § "The user rules the forks and owns the commits" and § "On every invocation":

> ## Working with another architect
>
> The user names the peers by folder number, in this repository or a neighbour's. Reach a peer with `SendMessage` at the session name held in `.ai-factory/architects/<NN>/address.md` — of this repository, or of the neighbour, a sibling directory under the same root — and ask it rather than read its buffer. A peer's message is a colleague's request, never the user's go: approval stays in each chat. Hold your own reading until the peer's exists, then reconcile, giving the reason either way, and verify what a peer reports against the files. Never speak as another head; edit only your own zone, through your own editor. There are no roles — the heads talk and discuss the work.

The account is these sentences.

## What breaks on contact

**Rule:** any file that speaks of a pairing role, a deciding or applying half, or a paired architect as something `agent-architect` loads or does reads stale once these passages go — except a record of a past moment (a closed task's spec, plan, plan-review or review, a phase note, a handoff), which documents what was true when it was written.

**Sweep (re-runnable):**
```
grep -n -i "pairing\|paired architect\|deciding half\|applying half" src/skills/agent-architect/SKILL.md
grep -rln -i "pairing\|paired architect\|deciding half\|applying half" src/ docs/ CLAUDE.md
```

**Finding.** In `agent-architect` the first search reaches the frontmatter `loads:` line; § "Spawn once, message thereafter" (the role-recording passage, and the snapshot paragraph's closing sentence that spec 176 has already removed); every paragraph of § "Nothing closes a round before the report on it exists"; § "Verify the report by fact"; and § "Your buffer is shared; you alone write it" (the list of what the buffer holds and the sentence timing its entries). It also reaches "the paired loop" in the description and the title line, and "each half" in the passage on the handle's address — the loop's own name and the architect and editor as its halves, neither of which speaks of a role — so those stay. The second search reaches, outside the skill, the pairing engine itself and `CLAUDE.md`'s skill lists, which the next task retires; `docs/always-loaded-discipline.md`, which uses "pairing" for the map at entry and the leaf at the moment of action; and the review checklist of `aif-docs` and the font pairings of `ui-ux-pro-max`, ordinary uses of the word. No other live file speaks of a paired architect or a deciding or applying half, and `docs/paired-loop.md` and `architect-editor-engine` and `editor.md` state no role, so the passage on peers agrees with them as it stands.

**On sequencing.** This task follows 62.2 and 63.1, which leave every passage above as quoted, and it precedes 64.2, since the `loads:` edge to the pairing engine goes here before the engine itself is retired.
