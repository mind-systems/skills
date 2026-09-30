# Plan: 66.2 — a head refreshes its standing entries from the seed

## Context
`docs/paired-loop.md` § "Where the pair's behaviour lives" says that at every rehydration the head reads the seed's standing entries against its own buffer's. Where they differ, the head takes the seed's text, and it adds any entry the seed has that the buffer lacks. Two texts say the opposite today. One is the founding passage in `src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter" ("read once, copied whole, never reread for a buffer that is merely resumed"). The other is the opening paragraph of `src/skills/agent-architect/templates/buffer-seed.md` ("read once … never reread for a buffer that already exists"). Both describe one behaviour, so both change in this task, and both new texts are pinned verbatim in the task spec (`.ai-factory/specs/trickster77777/187-a-head-refreshes-its-standing-entries-from-the-seed.md`).

Ground truth checked:
- The founding passage is the paragraph in § "Spawn once, message thereafter" that runs from "Your own start comes before any editor exists" to "Either way the buffer exists before any editor does." Its second step starts at "Second, the buffer —". That paragraph is hard-wrapped at no more than 74 characters per line.
- The seed's opening is the paragraph right after the `# Buffer seed — the architect's memory at founding` heading and before `## Where things stand`. It is hard-wrapped at no more than 76 characters per line.
- Task 66.1 is done. It edited only `## Method` in the seed, which is a different region from the opening paragraph. `## Method` holds the bold-led "Standing entry —" entries that the new text refers to.

Sweep (spec's rule: a text breaks if it says the seed is read once or never reread, or if it describes how a head rebuilds itself without the refresh). Running `grep -rn "never reread\|read once\|buffer-seed" src/ docs/ CLAUDE.md` finds:
- the two passages above;
- `docs/test-coverage-pass.md`, where "read once" means something unrelated;
- `docs/paired-loop.md` "A skill is read once", which is about the skill, not the seed, and already agrees.

§ "On every invocation" in the same SKILL.md sends the head to "Spawn once, message thereafter" to find its folder and rebuild. Once the founding passage carries the refresh, that section is true without an edit of its own. No other file changes.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Founding passage and seed opening

- [x] **Rewrite the second step of the founding passage**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", replace the text from "Second, the buffer —" through "Either way the buffer exists before any editor does." with this sentence group, word for word:

  > Second, the buffer — and which of two starts this is decides what you do: you read your session id, by the probe this section describes, and look under `.ai-factory/architects/` for the folder whose `address.md` holds it on its `session-id:` line. A folder found is yours: you work in its `buffer.md`, rebuilding from the buffer and, if the folder holds one, its latest snapshot; you also read the standing entries of `templates/buffer-seed.md` against the buffer's, matching an entry by its bold lead-in, and where the two differ you take the seed's text, and you add any entry the buffer lacks to the section of the buffer that holds its method. No folder found, for whatever reason, means you are a new head — you never ask the user which — and you found your own folder first, at the path and numbering the engine defines: create `buffer.md` in it, seeded in full from `templates/buffer-seed.md` at the moment of its founding, copied whole, and write `address.md`. Either way the buffer exists before any editor does.

  Compared with the current text, two things change. First, the clause beginning "; you also read the standing entries…" is added after "its latest snapshot". Second, "— read once, copied whole, never reread for a buffer that is merely resumed —" becomes ", copied whole,". Keep the first step, which starts "Your own start comes before any editor exists", exactly as it is. Leave the rest of the paragraph and the paragraph that follows ("On every start and every rehydration, new head or resumed, …") untouched. Keep the backticks and em dashes exactly as shown. Re-wrap the paragraph from "Second, the buffer" to its end so no line exceeds 74 characters, breaking only between words. Do not edit § "On every invocation".

- [x] **Rewrite the seed's opening paragraph**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  Replace the paragraph between the `# Buffer seed — the architect's memory at founding` heading and `## Where things stand`. The current paragraph runs from "This is the starting shape of a newly founded architect's buffer, read once" to "not left as placeholder prose." The replacement must read, word for word:

  > This is the starting shape of a newly founded architect's buffer and the source of its standing entries — the bold-led entries under `## Method` whose lead-in begins "Standing entry —". `agent-architect/SKILL.md`'s "Spawn once, message thereafter" step copies it whole into a new buffer file, and reads its standing entries again at every start that finds an existing folder, to bring the buffer's entries to the seed's text. The headings below are filled over the session, not left as placeholder prose.

  Use straight double quotes and straight apostrophes as shown, and the em dash `—` inside "Standing entry —", the same character the entries under `## Method` use. Hard-wrap so no line exceeds 76 characters, breaking only between words. Keep one blank line after the heading and one before `## Where things stand`. Change nothing else in the file: not the heading, the placeholders, the `## Method` entries (task 66.1 owns them), or any other section. Buffers founded from earlier seeds are records and stay as they are.
