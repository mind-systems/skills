# 68.1 — a route target may be a phase, and a phase counts its touches

## What is true now

`src/skills/orchestrator-artifacts/SKILL.md` § "6. Status-marker grammar" gives the pin for a routed observation as: "- `[routed → <path>]` — routed into an **open** task's spec; `<path>` must resolve to an editable surface (the task spec of an open task), never a completed or frozen one". It admits one route target, an open task's spec, and says nothing of a phase or of a count. The text wraps in the file at a fixed column.

In this repository and in `tradeoxy_broker` the resolution session routes findings straight onto phases, at the user's word in both, and the broker's spelling for it is `[routed → <roadmap path> § Phase N]`. The user also wants a phase's touches counted, meaning how many distinct findings were routed onto it, as a light hint for sorting a long roadmap and never a rule: "не надо столько важности этому счётчику давать", and a missed count is no harm. The count lives in the phase note and not in the roadmap, and a count of one is not written. No document under `docs/` or `orchestrator/docs/` states the marker grammar.

## What must be true after

The routed bullet in § "6. Status-marker grammar" reads: "- `[routed → <path>]` — routed into an **open** task's spec, or onto a phase as `[routed → <roadmap path> § Phase N]`, `<roadmap path>` being the roadmap file's repo-root-relative path — `.ai-factory/ROADMAP.md`, or `.ai-factory/roadmaps/<slug>.md` for a named roadmap; the target must resolve to an editable surface (the task spec of an open task, or a phase still in the roadmap), never a completed or frozen one".

A paragraph follows the dedup rule in the same section:

> A phase is a route target too. Routing a distinct finding onto a phase adds one to that phase's touch count, a `**Touches:** N` line kept in the phase note, or in the phase's preamble while the phase has no note; a count of one is not written, so the line first appears at two. The count is one per distinct finding, not per occurrence the dedup rule pins. It is a hint for sorting the roadmap and never a rule; a missed count costs nothing.

## What breaks on contact

**Rule:** a text breaks on this change if it reads or writes a status marker, restates the route target, or reads a phase's preamble or note as something with no counter in it.

**Sweep:**
```
grep -rn "routed" src/ docs/ CLAUDE.md
grep -rn -i "status-marker\|status marker" src/ docs/ CLAUDE.md
grep -rn -i "routed\|marker" orchestrator/orchestrator orchestrator/docs
```

**Finding.** The first search reaches the grammar itself, the task's own target; `task-rescue` § "Step 5.6 — Pin disposed observations", whose routed branch pins `[routed → <spec path>]` for a task and a spec it wrote or repaired itself and cites § 6 for the grammar without redefining it, so it reads the new target through the cite and never routes onto a phase; and uses of the word in other senses, in `command-pin-gaps` (a hole routed to its owner), `task-rescue-audit` (an implementation that routed around a gap) and `roadmap-outline-deep` (a note routed through `note`'s destination hook). The second reaches `roadmap-prune`, whose Step 0 gate cites the engine for the status-marker grammar and the pinned definition and reads only that an entry line carries a bracketed marker, so the new spelling counts as pinned without any change, and `task-rescue`'s cite. The third reaches the orchestrator side. Its code reads the signal line and the escalation marker and the `---STOP---` seam, and never parses a status marker or a touch count; its reviewer prompt tells the reviewer never to write one. The invariant in § "7. Mirrors-the-orchestrator invariant" mirrors the file protocol the orchestrator writes and reads, and the status markers are written by the resolution session and not by the orchestrator, so the new target and the line mirror nothing there. Nothing under `docs/` or `orchestrator/docs/` states the grammar, so no governing document disagrees.

The preamble and the note are read by `roadmap-outline-deep`, which rewrites a preamble down to its budget and mints the note. It meets the line as ordinary text of the phase it deepens and carries it into the note it writes; the user ruled that skill is left to carry the line on its own, and this task states nothing to it. `roadmap-outline`'s prohibitions bar a checkbox bullet, a contract line and a formal `Spec:` tag from a phase's preamble, and a `**Touches:** N` line is none of them. `roadmap-prune` captures the `Phase note:` pointer of each phase its emptied-phase sweep will delete and removes that note, so a count in a note leaves with its phase, and the review files that carry the pins are deleted by the same prune, so a count cannot be rebuilt from them later.
