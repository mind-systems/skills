# 78.2 — the folder holds the hand's snapshots

## What is true now

`src/skills/architect-editor-engine/SKILL.md`, § "The architect's buffer", defines the folder in this sentence: "The folder holds `buffer.md`, the buffer itself; `address.md`, the architect's address; and the head's own snapshots, each a `<NN>-<slug>.md` file with a lowercase-hyphenated slug, numbered inside the folder, the highest number being the latest." It has no `editor/`, no line naming a writer and no history of hands. The body also says "The head is the memory's only writer. The hand reads it in full — that is what makes the memory the link between the two halves — and never writes to it.", and the frontmatter description carries "the rule that the head is its only writer and the hand reads it in full and never writes to it", where "its" reads as the folder. A description is capped at 1024 characters, and this one is long. A new snapshot takes "the number one above the highest snapshot in its folder".

As 78.1 leaves it, the same section holds the snapshot genre: what a snapshot carries and that each new one supersedes the last by name.

`docs/paired-loop.md`, § "Where the memory lives", has the folder hold the head's snapshots and `editor/`, the hand's snapshots, "numbered on their own", each hand snapshot opening with the line ``Writer: `<handle>`, relieved <date>.``, and `editor/` as the history of hands, "nothing else lists them — not the keeper a peer reads, not the buffer". The head's snapshots stay in the folder itself; no `architect/` subfolder exists.

## What must be true after

In `src/skills/architect-editor-engine/SKILL.md`, § "The architect's buffer", the sentence reads:

"The folder holds `buffer.md`, the buffer itself; `address.md`, the architect's address; the head's own snapshots, each a `<NN>-<slug>.md` file with a lowercase-hyphenated slug, numbered inside the folder, the highest number being the latest; and `editor/`, the hand's snapshots, named and numbered the same way and on their own."

and directly after it:

"Each hand snapshot opens with the line ``Writer: `<handle>`, relieved <date>.``; `editor/` is the history of hands, and nothing else lists them — not `address.md`, not the buffer."

The rest of the paragraph stands.

In the same section the opening of the next paragraph reads:

"The head is the buffer's only writer, as it is of its own snapshots; `editor/` is the hand's to write. The hand reads the buffer in full — that is what makes the memory the link between the two halves — and never writes to it. The buffer holds the working discipline, the rulings the user has made about how the pair works, the method learned from repeated failure, and the register of where the skills still lag the practice: the editor reads it as its own working context from the head it is the hand of, not as an outsider glancing at private notes, which is what lets an order name meaning instead of restating the discipline every time."

In the engine's frontmatter description, the clause reads "the rule that the head alone writes the buffer and the hand reads it in full and writes only `editor/`" in place of "the rule that the head is its only writer and the hand reads it in full and never writes to it", the rest of the description standing and the whole within the cap.

## What breaks on contact

**Rule:** a text breaks on this change if it lists the folder's contents without the hand's snapshots, lists the hands somewhere beside `editor/`, or makes the head the only writer of the folder or the hand a reader of all of it.

**Sweep:**
```
grep -rn "head's own snapshots" src docs CLAUDE.md
grep -rn "its snapshots" src docs CLAUDE.md
grep -rn "your snapshots" src docs CLAUDE.md
grep -rn "only writer" src docs CLAUDE.md
grep -rn "never writes to it" src docs CLAUDE.md
```

**Finding.** The search for `head's own snapshots` returns the engine's sentence, the target. The search for `its snapshots` returns the engine's frontmatter description, "its buffer, its snapshots and its address file", and the `CLAUDE.md` paragraph on `.ai-factory/`, "each with its buffer, its snapshots and its address file"; each reads true of a folder that holds the head's snapshots with the hand's in `editor/` beside them. The search for `your snapshots` returns `agent-architect`'s § "Your buffer is shared; you alone write it", which has the head the only writer of "your snapshots"; it stays true of the head's own. The search for `only writer` returns the engine's description and body sentence, each a target; `agent-architect`'s "you are their only writer", which reads true of the buffer, `address.md` and the head's snapshots it names; and `docs/paired-loop.md`, whose sentence says the buffer's only writer. The search for `never writes to it` returns the same engine description and body, `agent-architect`'s "the rule that the hand reads the buffer in full and never writes to it", which reads true of the buffer alone, and the doc's sentence. `src/agents/editor.md` and `CLAUDE.md` hold neither clause.
