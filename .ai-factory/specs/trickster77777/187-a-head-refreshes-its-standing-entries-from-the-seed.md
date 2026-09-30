# 66.2 — a head refreshes its standing entries from the seed

## What is true now

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" decides a start by the folder the head finds. Its second step reads:

> Second, the buffer — and which of two starts this is decides what you do: you read your session id, by the probe this section describes, and look under `.ai-factory/architects/` for the folder whose `address.md` holds it on its `session-id:` line. A folder found is yours: you work in its `buffer.md`, rebuilding from the buffer and, if the folder holds one, its latest snapshot. No folder found, for whatever reason, means you are a new head — you never ask the user which — and you found your own folder first, at the path and numbering the engine defines: create `buffer.md` in it, seeded in full from `templates/buffer-seed.md` at the moment of its founding — read once, copied whole, never reread for a buffer that is merely resumed — and write `address.md`. Either way the buffer exists before any editor does.

The seed, `src/skills/agent-architect/templates/buffer-seed.md`, opens: "This is the starting shape of a newly founded architect's buffer, read once by `agent-architect/SKILL.md`'s "Spawn once, message thereafter" step at the moment a new buffer is created — never reread for a buffer that already exists, which is simply resumed. Copy it whole into the new buffer file; the headings below are filled over the session, not left as placeholder prose." The passages say the seed is never read again for a buffer that exists. § "On every invocation" points back to the founding passage for how a head finds its folder and says nothing of the seed.

`docs/paired-loop.md` § "Where the pair's behaviour lives" has the head read the seed's standing entries against its own at every rehydration, take the seed's text where the two differ, and add what the seed has that its buffer lacks. The seed's standing entries are the bold-led entries under `## Method` whose lead-in begins "Standing entry —".

## What must be true after

The second step of the founding passage reads:

> Second, the buffer — and which of two starts this is decides what you do: you read your session id, by the probe this section describes, and look under `.ai-factory/architects/` for the folder whose `address.md` holds it on its `session-id:` line. A folder found is yours: you work in its `buffer.md`, rebuilding from the buffer and, if the folder holds one, its latest snapshot; you also read the standing entries of `templates/buffer-seed.md` against the buffer's, matching an entry by its bold lead-in, and where the two differ you take the seed's text, and you add any entry the buffer lacks to the section of the buffer that holds its method. No folder found, for whatever reason, means you are a new head — you never ask the user which — and you found your own folder first, at the path and numbering the engine defines: create `buffer.md` in it, seeded in full from `templates/buffer-seed.md` at the moment of its founding, copied whole, and write `address.md`. Either way the buffer exists before any editor does.

The seed's opening reads: "This is the starting shape of a newly founded architect's buffer and the source of its standing entries — the bold-led entries under `## Method` whose lead-in begins "Standing entry —". `agent-architect/SKILL.md`'s "Spawn once, message thereafter" step copies it whole into a new buffer file, and reads its standing entries again at every start that finds an existing folder, to bring the buffer's entries to the seed's text. The headings below are filled over the session, not left as placeholder prose."

## What breaks on contact

**Rule:** a text breaks on this change if it says the seed is read once or never reread, or if it describes how a head rebuilds itself without the refresh.

**Sweep:**
```
grep -rn "never reread" src/ docs/ CLAUDE.md
grep -rn "read once" src/ docs/ CLAUDE.md
grep -rn "buffer-seed" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches the passages above and nothing else. The second reaches the same passages and a sentence of `docs/test-coverage-pass.md` that uses the words for something else. The third reaches the founding passage, the seed's opening, and the doc's section on where behaviour lives, which states the refresh and agrees with the new text. § "On every invocation" sends a head to the founding passage for finding its folder, so it reads true once that passage holds the refresh and needs no edit of its own. The passages are one behaviour stated in the skill and in the seed's opening; changing one alone leaves the other false, so they are one task. The seed is also edited by the task that adds entries under `## Method`; that task touches the section and this one the opening, regions of the file that do not meet.

**On placement.** A buffer founded earlier may not carry a `## Method` heading of its own, so the new text places an added entry "in the section of the buffer that holds its method" and leaves to the head, which knows its own buffer, which section that is.
