# Plan: 67.1 — the seed gains a `## Team` section

## Context
A new head's buffer is copied whole from `src/skills/agent-architect/templates/buffer-seed.md`. The seed has no section for a head's links: the goal it serves, its liaison above, and those it leads below. Yet `docs/paired-loop.md` § "The team" (the phase's governing spec) has every head keep these links in its own buffer. This task adds a `## Team` heading as the seed's first section, with a placeholder pinned verbatim in `.ai-factory/specs/trickster77777/190-the-seed-gains-a-team-section.md` § "What must be true after". The section belongs to the head. It has no "Standing entry —" lead-in, so the refresh step in `agent-architect/SKILL.md`, which matches entries by their bold lead-in, never touches it.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Seed text

- [x] **Insert the `## Team` heading and its placeholder**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  The seed opens with a paragraph that ends "…not left as placeholder prose." After it come a blank line and then `## Where things stand`. Insert the following between the two, so the order becomes: opening paragraph, blank line, `## Team`, blank line, placeholder, blank line, `## Where things stand`. The heading `## Team` is literal. The placeholder must match the spec's quoted text character for character once its lines are joined with single spaces:

  ```
  ## Team

  <Where this head sits in a team, as `docs/paired-loop.md` § "The team" has
  it: the goal it serves, linked to where it is written; its liaison above;
  those it leads below — each by repository and folder number, never by
  session name.>
  ```

  This wrap follows the seed's convention for multi-line placeholders (see the `## Method` and `## Current thread` placeholders). No line is longer than 76 characters, counted as characters and not bytes, and no line starts with an em dash. Do not add a bold lead-in or a "Standing entry —" entry to this section. Leave the opening paragraph and every other heading, placeholder, and entry unchanged. The spec says the opening paragraph stays true as written.

  Verify the edit:
  - `grep -n "^## " src/skills/agent-architect/templates/buffer-seed.md` lists, in order: `## Team`, `## Where things stand`, `## Rulings in force`, `## Method`, `## Orientation`, `## Ledger`, `## Candidates — not tasks`, `## Current thread`.
  - The placeholder's four lines, joined with single spaces, equal the spec's quote exactly.
  - `git diff` shows only added lines.

### Blast radius

- [x] **Confirm nothing else needs to change** (depends on Insert the `## Team` heading and its placeholder)
  Files: none (verification only)
  Run the sweep from the spec § "What breaks on contact":
  `grep -rn "buffer-seed" src/ docs/ CLAUDE.md`, `grep -rn "Where things stand" src/ docs/ CLAUDE.md`, `grep -rn "Standing entry" src/ docs/ CLAUDE.md`.
  Expected hits:
  - `buffer-seed` appears only in `src/skills/agent-architect/SKILL.md`, in the founding step ("copied whole") and in the refresh step ("matching an entry by its bold lead-in"). Neither step names the seed's headings, so both stay unchanged.
  - `Where things stand` and `Standing entry` appear only in the seed itself.

  If the sweep finds any other text that lists the seed's headings or treats every part of the seed as refreshed, stop and report it. Do not edit any file outside `src/skills/agent-architect/templates/buffer-seed.md`. Existing buffers under `.ai-factory/architects/` are not touched. The spec says heads founded before this change added their `## Team` sections by hand.
