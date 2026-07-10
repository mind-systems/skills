# Plan: 1.1 — global CLAUDE.md: grounding recalibrated — the map at entry, depth at the moment of action, the roadmap seam

## Context
Recalibrate the global CLAUDE.md grounding rule so it triggers at session entry (raise the map, walk to the leaf at the moment of action), guards against decayed held context, and defines the ROADMAP/ARCHITECTURE entry maps — plus the walkable-tree link bullet.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Constraints (from spec `.ai-factory/specs/22-global-grounding-to-the-leaf.md`)
- **The four quoted blocks are the contract — insert them verbatim, no rewording.** Existing section text must stay byte-identical outside the insertions (`git diff` shows only additions).
- **No eager/bulk-loading mandate.** The "however much context that takes" phrasing is dropped deliberately and must not reappear; `grep -i "however much context"` → zero.
- The file is user-level instructions loaded into every session of every project — nothing project-specific.

## Tasks

### Phase 1: Recalibrate grounding

- [x] **Task 1: Append the three grounding blocks to § "Grounding claims"**
  Files: `src/global/CLAUDE.md`
  In § "Grounding claims" (after the existing single paragraph, currently ending "...rather than invent."), append the following three paragraph blocks **verbatim**, in this order, each as its own paragraph:

  Block 1:
  > The session's opening task statement is itself the first artifact: raise its **map** first — which branches of the project are yours, one layer deep. Walk a branch **to the leaf at the moment you act on it**, not all branches up front — and the leaf is code, on both sides of the spec: docs are the crown, code is the root system, and a chain that stops at a doc has not reached ground truth. Never the whole tree — deep along the branch in your hands.

  Block 2:
  > Held context decays: a file read hours ago is a description again, not the file. Before acting on a branch, re-read its leaf fresh — even when you "already know it"; the larger the context, the stronger the illusion that you don't need to.

  Block 3:
  > When the project has `.ai-factory/ROADMAP.md`, it is the entry map of **time**: the seam between `[x]` and `[ ]` is where the project lives now — aim there. A `[x]` line is always history, never current state: it describes the moment of its own planning, a later line on the same surface supersedes an earlier one, and the present is verified only against the files. Its counterpart `.ai-factory/ARCHITECTURE.md` is the entry map of **space** — module boundaries, the chosen pattern, and the compacted history in `## Features`; the two maps together orient a cold session before any skill is invoked.

  Do not alter the existing paragraph. These render as plain paragraphs (the spec quotes them with `>` to delimit the exact text; match the existing section's formatting — plain prose paragraphs, not blockquotes).

- [x] **Task 2: Append the walkable-tree bullet to § "Documentation style"** (depends on Task 1)
  Files: `src/global/CLAUDE.md`
  At the end of the § "Documentation style" bullet list (after the "Describe current state only" bullet), append this bullet **verbatim**:

  > - **Docs form a walkable tree.** Inline links are the edges grounding walks: every doc links to the deeper docs and code it depends on, at the moment they are load-bearing. A fact's second home is always a link to its first, never a copy.

### Phase 2: Verify

- [x] **Task 3: Verify the contract holds** (depends on Task 2)
  Files: `src/global/CLAUDE.md`
  Run the spec's checks: `grep -n "first artifact\|decays\|entry map\|walkable tree" src/global/CLAUDE.md` → four hits in the right sections; `grep -i "however much context" src/global/CLAUDE.md` → zero; `git diff` shows additions only, no changes to pre-existing lines. Fix any deviation before finishing.
