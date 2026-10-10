# 76.3 — the seed's team links carry the owner's slug

## What is true now

`src/skills/agent-architect/templates/buffer-seed.md`, in the `## Team` placeholder, tells a new head to name those it leads below "each by repository and folder number, never by session name". `docs/paired-loop.md` § "The team" names each link "by repository, owner's slug and folder number and never by session name, since the folder resolves through the keeper", and § "Where the memory lives" puts a folder at `.ai-factory/architects/<user-slug>/<NN>/`, so a folder number alone no longer names a head across users.

The seed is copied into a buffer at a founding; a head found at a start rereads only the standing entries under `## Method`, so the `## Team` placeholder reaches new buffers alone. No open task above this one edits the seed.

## What must be true after

In `src/skills/agent-architect/templates/buffer-seed.md`, the `## Team` placeholder reads, in that clause: "each by repository, owner's slug and folder number, never by session name". The rest of the placeholder stands.

## What breaks on contact

**Rule:** a text breaks on this change if it tells a head to name a link by repository and folder number without the owner's slug.

**Sweep:**
```
grep -rn "repository and folder" src docs CLAUDE.md
```

**Finding.** The sweep returns the seed's placeholder, the target, and nothing else. A buffer founded before this lands keeps its `## Team` as it stands, since a start rereads only the standing entries.
