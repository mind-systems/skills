# 76.1 — the engine puts a head's folder in its user's folder

## What is true now

`src/skills/architect-editor-engine/SKILL.md`, § "The architect's buffer", in the paragraph that opens "The pair shares one working memory", defines the head's folder and its numbering in two sentences:

"The pair shares one working memory, and it lives in the architect's own folder, `.ai-factory/architects/<NN>/`; the folder's number is the head's identity."

"A new head's folder takes the number one above the highest folder under `.ai-factory/architects/`, and a new snapshot the number one above the highest snapshot in its folder; both start at `01` and are at least two digits wide, so several architects coexist without colliding."

The same paragraph names a snapshot's file `<NN>-<slug>.md` "with a lowercase-hyphenated slug", the placeholder `<slug>` standing there for a file's title. The paragraph that opens "Two architects are two heads" says "Several architects coexist under the numbering above". `docs/paired-loop.md` § "Where the memory lives" already puts the folder at `.ai-factory/architects/<user-slug>/<NN>/`, inside its user's own folder, the number counted within that folder. The engine is the home of the path and the numbering; `agent-architect` and the buffer seed point to it. No open task above this one edits the engine's buffer section.

As 83.2 leaves it, `roadmap-engine` § "Named roadmaps" reads: "**Slug derivation:** the user's slug is given at session start, as the line `The user's slug: <user-slug>`; a session that holds no such line runs `scripts/user-slug.sh` and takes its output as the slug." The label is the hook's, not the script's.

## What must be true after

In `src/skills/architect-editor-engine/SKILL.md`, § "The architect's buffer", in that paragraph, the two sentences read:

"The pair shares one working memory, and it lives in the architect's own folder, `.ai-factory/architects/<user-slug>/<NN>/`, inside its user's own folder: `<user-slug>` is the user's slug, the one the session holds in the line `The user's slug: <user-slug>` or otherwise takes from running `roadmap-engine`'s `scripts/user-slug.sh`, and the folder's number, counted within that user's folder, is the head's identity there."

"A new head's folder takes the number one above the highest folder under its user's folder, `.ai-factory/architects/<user-slug>/`, and a new snapshot the number one above the highest snapshot in its folder; both start at `01` and are at least two digits wide, so several architects coexist without colliding."

The rest of the paragraph and of the section stands, the snapshot's `<NN>-<slug>.md` among it.

## What breaks on contact

**Rule:** a text breaks on this change if it puts a head's folder at `.ai-factory/architects/<NN>/`, or numbers a new head's folder across every user's folders.

**Sweep:**
```
grep -rn "architects/<NN>" src docs CLAUDE.md
grep -rn "highest folder" src docs CLAUDE.md
```

**Finding.** The search for `architects/<NN>` returns the engine's sentence, the target, and the peer-address sentence in `agent-architect`'s § "Working with another architect", which 76.2 changes; no doc and no `CLAUDE.md` text appears in its output. The search for `highest folder` returns the engine's paragraph alone, the target.
