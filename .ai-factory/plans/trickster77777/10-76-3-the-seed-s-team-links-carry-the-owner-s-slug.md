# Plan: 76.3 — the seed's team links carry the owner's slug

## Context
The buffer seed's `## Team` placeholder tells a new head to name those it leads below "each by repository and folder number", which no longer names a head once folders sit under `.ai-factory/architects/<user-slug>/<NN>/`. The clause must carry the owner's slug, matching the form `docs/paired-loop.md` § "The team" already holds (governing spec of phase 76; per task spec `.ai-factory/specs/trickster77777/0232-the-seeds-team-links-carry-the-owners-slug.md`).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Seed edit

- [x] **Rewrite the `## Team` placeholder's link clause**
  Files: `src/skills/agent-architect/templates/buffer-seed.md`
  In the `## Team` placeholder (the angle-bracketed prose under the `## Team` heading), replace the clause "each by repository and folder number, never by session name" with "each by repository, owner's slug and folder number, never by session name". The clause currently wraps across the line beginning "leads below —"; keep the placeholder's existing hard-wrap style (~76-char lines) and re-wrap only the affected lines as needed. Every other word of the placeholder — the goal it serves, the liaison above, "After a compact this is how the head knows its place." — stands unchanged; no other section of the seed (including the `# Architect buffer — <this folder's number>` heading and the `## Method` standing entries) is touched.
  After the edit, `grep -rn "repository and folder" src docs CLAUDE.md` returns nothing (the task spec's sweep found the seed's placeholder as its only hit).
