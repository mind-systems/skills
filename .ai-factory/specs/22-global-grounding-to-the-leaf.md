# global CLAUDE.md: grounding recalibrated — the map at entry, depth at the moment of action, the roadmap seam

## Current state

`src/global/CLAUDE.md` § "Grounding claims" mandates depth-to-leaf but triggers only on "the artifact in front of you", and three gaps showed up live:

1. **No entry rule.** The session's opening task statement doesn't count as an artifact, so at session start the agent answers one docs-layer deep — or, told "прочитай строчку роадмапа", has to *guess what a roadmap even is*: nothing loaded into a session defines `.ai-factory/ROADMAP.md` as an artifact type, its `[x]`/`[ ]` seam, or how its lines relate to the present.
2. **No decay rule.** Context held long creates false confidence: a file read hours ago sits in the context with the authority of a fact, and the agent stops re-reading — a live incident this session reasoned from a stale `[x]` roadmap line ("3D mode added") about a skill the file had since changed. Eager bulk loading makes this *worse*, not better.
3. **The chain stops at docs.** In practice code opens only when a decompose-style task forces it, although the section names code as the chain's end.

§ "Documentation style" has no positive link rule (covered by the companion walkable-tree bullet, unchanged from the prior revision of this spec).

## Change

Append to § "Grounding claims" — exact text, three blocks (this **replaces** the previously drafted "however much context that takes" wording; the eager-maximal phrasing is dropped deliberately — depth is a route walked at the moment of action, not a load performed at start):

> The session's opening task statement is itself the first artifact: raise its **map** first — which branches of the project are yours, one layer deep. Walk a branch **to the leaf at the moment you act on it**, not all branches up front — and the leaf is code, on both sides of the spec: docs are the crown, code is the root system, and a chain that stops at a doc has not reached ground truth. Never the whole tree — deep along the branch in your hands.

> Held context decays: a file read hours ago is a description again, not the file. Before acting on a branch, re-read its leaf fresh — even when you "already know it"; the larger the context, the stronger the illusion that you don't need to.

> When the project has `.ai-factory/ROADMAP.md`, it is the entry map of **time**: the seam between `[x]` and `[ ]` is where the project lives now — aim there. A `[x]` line is always history, never current state: it describes the moment of its own planning, a later line on the same surface supersedes an earlier one, and the present is verified only against the files. Its counterpart `.ai-factory/ARCHITECTURE.md` is the entry map of **space** — module boundaries, the chosen pattern, and the compacted history in `## Features`; the two maps together orient a cold session before any skill is invoked.

Append to § "Documentation style" — exact text, one bullet (unchanged from the prior revision):

> - **Docs form a walkable tree.** Inline links are the edges grounding walks: every doc links to the deeper docs and code it depends on, at the moment they are load-bearing. A fact's second home is always a link to its first, never a copy.

## Files & types

- edit `src/global/CLAUDE.md` — § "Grounding claims" (+3 blocks), § "Documentation style" (+1 bullet)

## Guards

- **Exact text above is the contract** — the four quoted blocks land verbatim; no rewording; existing section text byte-identical outside the insertions.
- **No eager mandate anywhere** — the additions must not instruct bulk loading; "map first, depth at the moment of action" is the calibration, and "never the whole tree" stays inside the added text itself.
- The file is user-level instructions loaded into every session of every project — nothing project-specific.

## Verification

- `grep -n "first artifact\|decays\|entry map\|walkable tree" src/global/CLAUDE.md` → four hits in the right sections.
- `git diff` shows only additions; `grep -i "however much context"` → zero.
- Live checks: (a) a fresh session opened with "прочитай строчку роадмапа" resolves the roadmap, reads the seam, and treats `[x]` lines as strata, not state; (b) a session asked about a surface described by an old `[x]` line verifies against the file before answering.
