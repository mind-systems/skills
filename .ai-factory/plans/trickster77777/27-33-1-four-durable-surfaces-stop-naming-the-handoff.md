# Plan: 33.1 — four durable surfaces stop naming the handoff

## Context
Four skills reference the handoff — an artifact spent on first read — from surfaces that outlive it (a format block, a permission, a deletion-safety rationale, a protocol's definition of its own writer). Drop the handoff from all four, narrowing each sentence without weakening what it says.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Narrow the four sites

- [x] **Format block drops the handoff from the direction preamble**
  Files: `src/skills/roadmap-engine/SKILL.md`
  In the roadmap file format block, line 86 currently reads `<direction preamble: source handoff/spec links, hard rules, gating for this direction>`. Change it to `<direction preamble: source spec links, hard rules, gating for this direction>`. Exactly that one line changes; nothing else in the format block moves, and no line is re-wrapped.

- [x] **Preamble-links permission grants task-spec links only**
  Files: `src/skills/roadmap-outline/SKILL.md`
  Line 40 opens the permission sentence `Links to handoffs and task specs are allowed as plain markdown links inside the` (continuing on line 41 with `intro/preamble prose — no formal `Spec:` tag, no invented task specs.`). Rewrite line 40 alone to `Links to task specs are allowed as plain markdown links inside the`; line 41 is untouched, so the sentence reads "Links to task specs are allowed as plain markdown links inside the intro/preamble prose — no formal `Spec:` tag, no invented task specs." Leave the shortened line short — no re-flow.

- [x] **Prune's `Phase note:` rationale narrows to task-spec links** (depends on the preamble-links permission)
  Files: `src/skills/roadmap-prune/SKILL.md`
  In the Step-1 `Also capture` paragraph, line 284 reads `preamble: `roadmap-outline` permits unrelated handoff and task-spec links in that`. Rewrite that line alone to `preamble: `roadmap-outline` permits unrelated task-spec links in that`. Only the enumeration narrows: the paragraph must still state all three of — keying on the literal `Phase note:` token and never on a link's position, links living in that same prose, and this skill holding `Bash(rm *)` so a positional key would follow one of those to a deletion. Do not touch the blocked-gate resolution (lines ~61–63, `/command-handoff` and `.ai-factory/handoffs/`) or the `Do not touch `handoffs/` — it is never swept` line (~447): those are the act of handing off, which this task leaves alone.

- [x] **Status-marker grammar names its writer without routing through the artifact**
  Files: `src/skills/orchestrator-artifacts/SKILL.md`
  In § "6. Status-marker grammar", the writer clause spans lines 67–69. Line 67 (`Append-only space-separated bracketed suffix at the end of the entry line. Written by`) stays as is; rewrite lines 68–69 to:
  `the **resolution session** — the dedicated session the user opens when a prune parks —`
  `at the moment it disposes of an observation:`
  Only those two lines change — the rest of the section keeps its breaks and the bullet list below is untouched. The new line 68 (~87 chars) sits inside the file's existing wrap range (longest line is 96), so no re-wrap is warranted. The trigger — a parked prune — stays legible; the handoff leaves.

### Verify the narrowing

- [x] **Confirm the counts and the diff scope** (depends on all four edits)
  Files: `src/skills/roadmap-engine/SKILL.md`, `src/skills/roadmap-outline/SKILL.md`, `src/skills/roadmap-prune/SKILL.md`, `src/skills/orchestrator-artifacts/SKILL.md`
  Run the spec's checks against the edited files: case-insensitive `handoff` → 0 in `roadmap-engine`, `roadmap-outline` and `orchestrator-artifacts` (each carries exactly 1 today); → 4 in `roadmap-prune` (5 today — the four survivors being two on the `/command-handoff` line, one on the `.ai-factory/handoffs/` destination line, one on "never swept"). Confirm the narrowed lines kept their remaining content — `roadmap-engine`'s preamble line reads `<direction preamble: source spec links, hard rules, gating for this direction>`, `roadmap-outline` still grants "Links to task specs are allowed as plain markdown links inside the intro/preamble prose" and still ends "no formal `Spec:` tag, no invented task specs", prune's rationale still carries its three clauses, and the status-marker grammar still names the resolution session as writer and a parked prune as trigger. Finally `git diff HEAD --stat -- src/` must list exactly these four files and nothing else; `docs/`, `CLAUDE.md` and `active/` show no change. Do not edit the sibling `orchestrator` repository — per the spec, the clause edited here is not part of the mirrored protocol surface, so no lockstep change is owed.
