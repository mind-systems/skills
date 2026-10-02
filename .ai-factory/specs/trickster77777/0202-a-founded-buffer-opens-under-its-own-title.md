# 70.1 — a founded buffer opens under its own title

## What is true now

`src/skills/agent-architect/templates/buffer-seed.md` opens: "# Buffer seed — the architect's memory at founding", and then "This is the starting shape of a newly founded architect's buffer and the source of its standing entries — the bold-led entries under `## Method` whose lead-in begins "Standing entry —". `agent-architect/SKILL.md`'s "Spawn once, message thereafter" step copies it whole into a new buffer file, and reads its standing entries again at every start that finds an existing folder, to bring the buffer's entries to the seed's text. The headings below are filled over the session, not left as placeholder prose." Its first heading after that is `## Team`. The text wraps in the file at a fixed column.

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter", the founding passage, says: "…create `buffer.md` in it, seeded in full from `templates/buffer-seed.md` at the moment of its founding, copied whole, and write `address.md`."

Copied whole, a founded buffer opens with the seed's title and the seed's paragraph about being a seed, so it misnames itself. The paragraph also defines "standing entry", which a head reads in its buffer and finds clear for that reason. The `<…>` guidance lines stand in a founded buffer's empty sections, are replaced where content lands, and work.

## What must be true after

The seed opens with its own title and a paragraph about the seed, and then the buffer's own title and opening, each under its own `#` heading:

> # Buffer seed — the architect's memory at founding
>
> This is the starting shape of a newly founded architect's buffer. The step "Spawn once, message thereafter" in `agent-architect/SKILL.md` copies it into a new buffer file from the `# Architect buffer` heading down, and at every start that finds an existing folder reads the standing entries under `## Method` again, to bring the buffer's entries to the seed's text.
>
> # Architect buffer — <this folder's number>
>
> The standing entries of this buffer — the bold-led entries under `## Method` whose lead-in begins "Standing entry —" — come from the seed, `agent-architect`'s `templates/buffer-seed.md`, and are brought to its text at every start that finds this folder. The headings below are filled over the session, not left as placeholder prose.

The first heading after the buffer's opening stays `## Team`. In the founding passage, the clause reads: "…create `buffer.md` in it, seeded from `templates/buffer-seed.md` at the moment of its founding — copied from its `# Architect buffer` heading down, the folder's number filling that title — and write `address.md`."

## What breaks on contact

**Rule:** a text breaks on this change if it reads the seed's opening, states what the founding step copies, or depends on the seed's own title.

**Sweep:**
```
grep -rn "copies it whole\|copied whole" src/ docs/ CLAUDE.md
grep -rn "Buffer seed" src/ docs/ CLAUDE.md
grep -rn "buffer-seed" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches the seed's opening and, in the skill, the founding passage's "copied whole", the two texts this task rewrites. The second reaches the seed's own title alone. The third reaches the founding passage and the refresh in the skill, and the seed. The refresh reads the standing entries of the seed against the buffer's and matches each by its bold lead-in; it reads nothing of the seed's title or opening, so the new two-title shape does not touch it, and the entries keep their words. Buffers already founded keep their own title and opening, since the refresh matches standing entries only and this part is not an entry, so no existing buffer changes; the heads whose buffers opened as copies of the seed keep that opening unless they edit it. The seed's guidance lines, its `## Team` placeholder and its headings are unchanged. No other skill, command, doc or `CLAUDE.md` reads the seed's opening: the doc and the engine speak of seeding a buffer and of standing entries without quoting it, and closed notes and specs that quote the old opening are records.
