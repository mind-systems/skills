# Handoff — field report: an architect violated the relay discipline and contaminated the editor's independence

> A self-report from a live `agent-architect` session, filed against the skill's own protocol. Written because the violation was not a one-off slip but a repeated pattern with a clear root cause, and the skill's authors should see how the discipline gets broken in practice.

## What the protocol says

`agent-architect`'s discipline is explicit: on any analysis or work target — a review, a decompose, "look at phase N" — the architect does **not** author a prompt for the editor. It **relays the user's own message**, translated to English, faithfully: no findings, no checklist, no verdict, no method of its own added on top. The editor reasons independently, and that independence "is the only way its agreement is real signal rather than manufactured echo." The one allowed transformation is expanding a slash-command the user actually invoked into skill-by-reference. The editor is spawned once and messaged thereafter; a warm editor already carries its context.

## The violations

**1. Authored briefs instead of relaying — twice (Phase 6 and Phase 7 decompose).** Rather than relaying the user's terse target, the architect sent the editor multi-section prompts carrying its own decided-context, a list of reserved-word forms to align, an explicit collision hint ("planner.md's context tree for this task"), a named file to go check, and "produce a proposed decomposition with X and Y." Every one of those is "method of my own added on top." The damage is not verbosity — it is that the editor was handed the architect's own conclusions before reasoning, so its subsequent agreement was partly echo. The paired loop's entire value (an independent second read that catches what the architect misses) was undercut by the architect pre-loading the answer.

**2. Planned to re-send a skill the editor already had.** The user's target was the bare message "go, phase 7" — no slash-command in it. The architect nonetheless proposed to expand `roadmap-decompose` by-reference and send it to the editor again — a skill the persistent editor had already read during the Phase 6 round. There was no slash-command to expand, and a warm editor needs no re-send. The correct relay was the terse instruction alone, leaning on the editor's carried context.

## Root cause

The instinct to de-risk the editor's output by pre-loading it with context and conclusions — control masquerading as helpfulness. The protocol exists precisely to defeat that instinct: a contaminated editor produces agreement, not verification. The architect also conflated two distinct moments — the **analysis relay** (faithful, bare) and the **apply work-order** (the one case the architect authors, pinning values and guards after the user's go) — and imported the authoring habit of the second into the first.

## The correct behavior (what should have happened)

- Analysis/work target → relay the user's own words, translated, nothing added. Expand a skill only when the user typed a slash-command this turn. To a warm editor, a terse target ("phase 7") is the whole message.
- Brief with context only when the editor is genuinely fresh or respawned — and even then, project facts (files to treat as ground truth, settled constraints), never the architect's own analysis of the target.
- Author a full prompt only for the apply work-order, after the user greenlights — that is where values, paths, exact strings, and guardrails belong.
- Verify the editor's report against the files, not against a report the architect half-wrote for it.

## Suggestion for the skill

The discipline is stated clearly; it was still violated repeatedly, which suggests the failure mode deserves a named warning in the skill body. Two additions would have caught this architect earlier: (a) an explicit anti-pattern — "do not leak your decided-context, inventory, or collision hints into an analysis relay; that manufactures echo" — sitting right next to the relay rule; and (b) a one-line contrast between the bare analysis relay and the authored apply work-order, since importing the second's habit into the first is the concrete slip that happened here.
