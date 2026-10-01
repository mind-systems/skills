# Phase 52 — the test-plan note's title follows its slug, and its writer can write

What still diverges, in `src/skills/roadmap-test-coverage/SKILL.md`, § "Layer 4 — Deep Research (parallel agents)":

- **The note's title.** The Layer 4 prompt names `Area: <area name>` and tells the agent to choose its slug "not for the Area label above", once research is done. The template it writes then opens `# <Area Name> — Test Plan`, so a note whose slug says what the area turned out to be carries a title that says what it was called before research began. The later layers' area annotations fill from the same label.
- **The writing agent.** Layer 4 spawns an `Explore` agent per area and has it write the note itself ("You write the file yourself"). That agent type can be read-only in a harness, with `Bash` but no `Write` or `Edit`. If it cannot write, the returned `saved:` path is the first place the failure shows.

What no longer diverges. The overstatement of what `aif` mandates for `$TEST_CMD` was in a pruned task spec's paraphrase and never in a shipped skill: the `$TEST_CMD` rule in `roadmap-test-coverage` § "Layer 1 — Load Project Context" reads "Primary — the test command the project declares in its `CLAUDE.md` `## Commands` section … whatever its shape — a list entry or a bare line counts too", and no live text repeats the inaccuracy.

Nothing under `docs/` is written by this phase's own note.
