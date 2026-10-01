# 67.1 — the seed gains a team section

## What is true now

`src/skills/agent-architect/templates/buffer-seed.md` opens with one paragraph on what the seed is, and then holds these headings, in order: `## Where things stand`, `## Rulings in force`, `## Method`, `## Orientation`, `## Ledger`, `## Candidates — not tasks` and `## Current thread`. Each carries a placeholder in angle brackets saying what it holds, and `## Method` also holds the standing entries. None of them holds a head's links: the goal it serves, its liaison above, and those it leads below.

`docs/paired-loop.md` § "The team" has each head keep those links in its own buffer, each named by repository and folder number and never by session name. A newly founded head is copied from this seed, so it has no place for them and nothing that tells it a team can exist. The seed's opening paragraph ends "The headings below are filled over the session, not left as placeholder prose."

## What must be true after

The seed's headings read, in order: `## Team`, `## Where things stand`, `## Rulings in force`, `## Method`, `## Orientation`, `## Ledger`, `## Candidates — not tasks` and `## Current thread`. The `## Team` heading is literal, and it follows the opening paragraph directly. Under it stands a placeholder in the seed's own angle-bracket form:

> <Where this head sits in a team, as `docs/paired-loop.md` § "The team" has it: the goal it serves, linked to where it is written; its liaison above; those it leads below — each by repository and folder number, never by session name.>

The section is the head's own. It carries no bold "Standing entry —" lead-in, so it is not among the entries the refresh matches by that lead-in: the head fills it, and the seed never overwrites it.

## What breaks on contact

**Rule:** a text breaks on this change if it reads the seed's structure — if it names the seed's headings, or treats every part of the seed as refreshed.

**Sweep:**
```
grep -rn "buffer-seed" src/ docs/ CLAUDE.md
grep -rn "Where things stand" src/ docs/ CLAUDE.md
grep -rn "Standing entry" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches `agent-architect/SKILL.md` alone, in the founding step and in the refresh; the seed's own opening paragraph, the engine and the doc speak of the seed and its standing entries without naming its file or its headings. The founding step copies the seed whole into a new buffer, so the new heading and its placeholder arrive in every buffer founded afterwards. The refresh reads the standing entries of the seed against the buffer's, matching each by its bold lead-in; the new section has none, so the refresh does not touch it, and the entries it adds go to the section of the buffer that holds its method, which the new heading does not change. The opening paragraph names only the standing entries under `## Method` as what is brought to the seed's text, and says the headings are filled over the session, so it stays true with a placeholder under the new heading and needs no edit. The second and third searches reach the seed alone; no skill, command or doc names its other headings or its entries by their lead-ins, and the skill, the engine and the doc speak of standing entries and never of a heading. The engine's sentence on what the memory holds names the working discipline, the rulings, the method and the register of where the skills lag, and no links; it describes the usual content rather than closing a list, and `docs/paired-loop.md` § "The team" already places a head's links in its own buffer. A buffer founded before this change gets no `## Team` heading from the refresh, since it is not an entry, and the heads that keep one added it by hand.
