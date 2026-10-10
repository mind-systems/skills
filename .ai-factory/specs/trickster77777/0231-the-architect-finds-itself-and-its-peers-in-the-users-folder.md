# 76.2 — the architect reaches a peer in its owner's folder

## What is true now

`src/skills/agent-architect/SKILL.md`, § "Working with another architect", opens "The user names the peers by folder number, in this repository or a neighbour's." and sends a message "at the session name held in `.ai-factory/architects/<NN>/address.md` — of this repository, or of the neighbour, a sibling directory under the same root".

As 76.1 leaves it, the engine's § "The architect's buffer" puts a head's folder at `.ai-factory/architects/<user-slug>/<NN>/`, inside its user's own folder, with `<user-slug>` the user's slug and the number counted within that folder. `docs/paired-loop.md` § "Working with another architect" names a peer "by folder number, with the owner's slug when the peer is another user's".

The heads founded so far sit at the flat path, `.ai-factory/architects/<NN>/`.

## What must be true after

In `src/skills/agent-architect/SKILL.md`, § "Working with another architect", the sentence that begins "The user names the peers" reads: "The user names the peers by folder number, with the owner's slug when the peer is another user's, in this repository or a neighbour's." The address reads `.ai-factory/architects/<user-slug>/<NN>/address.md`, `<user-slug>` being the peer owner's slug, and the rest of the sentence stands.

## What breaks on contact

A peer whose folder is still at the flat path is not reached at the new address until it is moved. Moving a folder into its user's folder is the user's, by hand.

**Rule:** a text breaks on this change if it addresses a peer at a path without the owner's folder.

**Sweep:**
```
grep -rn "architects/<NN>" src docs CLAUDE.md
grep -rn "by folder number" src docs CLAUDE.md
```

**Finding.** The search for `architects/<NN>` returns the peer-address sentence in `agent-architect`, the target, and the engine's sentence, which 76.1 changes. The search for `by folder number` returns the peer sentence in `agent-architect`, the target; the sentence in `docs/paired-loop.md` and the `CLAUDE.md` row for it, both of which name the owner's slug; and the `CLAUDE.md` row for `docs/the-pipeline-speaks-to-an-architect.md`, which says "named by folder number" and no more.
