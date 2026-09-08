# Four durable surfaces stop naming the handoff

## Current state (grounded, read fresh)

A handoff is `note` aimed at a different genre and a different folder; `docs/sakshi-harness/skill-graph.md` already states that much. That the artifact is spent on first read is stated in `command-handoff` itself, where a skill's own behaviour belongs — the docs describe the system, and a skill is its own documentation. Notes obey that with no rule written: a sweep for a note-file path outside `.ai-factory/notes/` returns only architect buffers, cited from handoffs and plan-reviews — never from a skill, a doc, a roadmap, or a task spec. The handoff is the one genre that acquired a top-level skill name, and four skills went on to write that name into surfaces that outlive the artifact.

`src/skills/roadmap-engine/SKILL.md` — the roadmap file format block renders the direction preamble as `<direction preamble: source handoff/spec links, hard rules, gating for this direction>`. The format engine, the deepest surface in the family, names the genre.

`src/skills/roadmap-outline/SKILL.md` — a standing permission: "Links to handoffs and task specs are allowed as plain markdown links inside the intro/preamble prose".

`src/skills/roadmap-prune/SKILL.md` — the `Phase note:` capture rationale rests on that permission. It keys on the literal token "and on nothing else — never on a link's position in a preamble", because `roadmap-outline` "permits unrelated handoff and task-spec links in that same prose and this skill holds `Bash(rm *)`, so a positional key would follow one of those to a deletion". Remove the permission and the sentence cites something that no longer exists.

`src/skills/orchestrator-artifacts/SKILL.md` — the status-marker grammar defines its own writer as "the **resolution session** — the dedicated session the user opens from the parked prune's handoff".

Two further uses are the act of handing off, not a reference to a spent artifact, and stay untouched: `roadmap-prune`'s blocked-gate resolution tells the user to run `/command-handoff` and carry the gate context into a resolution session, exactly as `docs/sakshi-harness/skill-cycle.md` describes it; and `agent-architect` carries its buffer path across a compact, agent to agent, one shot.

The sibling `orchestrator` repository is touched in one way and not in another. Its own CLAUDE.md declares that the consumer skills mirror its file protocol in `orchestrator-artifacts`, and that any change to that protocol — directory layout, artifact naming, PASS signals, sidecar fields, review-section format — must be reflected there; the clause this task edits names the writer's provenance and is none of those, so no lockstep change is owed on that side. Separately, that repository's own roadmap and task specs carry handoff citations of their own, one of them naming a skills-side handoff number that does not exist here — the harm this direction describes, already realized across a repository boundary.

## The change

1. `roadmap-engine` — in the roadmap file format block, the direction preamble line reads `<direction preamble: source spec links, hard rules, gating for this direction>`. Nothing else in the block changes.

2. `roadmap-outline` — the permission sentence reads "Links to task specs are allowed as plain markdown links inside the intro/preamble prose — no formal `Spec:` tag, no invented task specs." The remainder of the sentence is untouched.

3. `roadmap-prune` — the `Phase note:` rationale reads "`roadmap-outline` permits unrelated task-spec links in that same prose". The safety argument keeps its full force: task-spec links still live in that prose, a positional key would still follow one to a deletion, and the skill still holds `Bash(rm *)`. Only the enumeration narrows; no clause of the reasoning is dropped.

4. `orchestrator-artifacts` — the status-marker grammar names its writer without routing through the artifact: "Written by the **resolution session** — the dedicated session the user opens when a prune parks — at the moment it disposes of an observation:". The trigger stays legible; the handoff leaves.

## Files & types

- edit: `src/skills/roadmap-engine/SKILL.md` — the roadmap file format block
- edit: `src/skills/roadmap-outline/SKILL.md` — the preamble-links permission
- edit: `src/skills/roadmap-prune/SKILL.md` — the `Phase note:` capture rationale only
- edit: `src/skills/orchestrator-artifacts/SKILL.md` — the status-marker grammar's writer clause

## Guards

- `roadmap-prune`'s blocked-gate resolution is not touched. It names `/command-handoff` and `.ai-factory/handoffs/` and keeps doing so: that is the act of handing off, and the cycle doc describes it.
- `roadmap-prune`'s "Do not touch `handoffs/` — it is never swept" is not touched.
- `agent-architect` is not touched.
- `roadmap-test-coverage` is not touched. Its `$HANDOFF_LIST` is a different concept wearing the same word, and settling that needs a decision about the reserved-words registry that this task does not carry.
- The `Phase note:` rationale does not weaken. Narrowing the enumeration is the whole edit; the reason for keying on the literal token stays stated in full.
- No document changes. `docs/sakshi-harness/skill-graph.md` already holds the position this task reconciles to, and `docs/sakshi-harness/skill-cycle.md` already describes the act that stays.
- The plan layer is not swept. Task specs and direction preambles that open with a source-handoff line keep their text and leave with their tasks at prune.
- No frontmatter changes: no `loads:` edge, no grant, no `description:`, no new skill.
- The line breaks stay where the removed words leave them. All four sites are hard-wrapped prose and every edit shortens a line; no paragraph is re-flowed and no line outside the removed phrase is rewritten. At the three sites where the phrase sits inside one line — `roadmap-engine`, `roadmap-outline`, `roadmap-prune` — exactly that line changes. At `orchestrator-artifacts` the phrase spans a line break, so the two lines it spans are rewritten and the rest of the paragraph keeps its breaks. A re-wrap would swell four diffs that should each read as one phrase removed.
- The sibling `orchestrator` repository is not edited and owes no lockstep change; the mirror contract its CLAUDE.md declares covers a protocol surface this task does not touch. Its own roadmap and task specs keep their handoff citations — that is another repository's plan layer, pruned on its own cycle, and this task changes only what this repository owns.

## Verification

Counts against a whitespace-normalized read of each named file.

- `handoff`, case-insensitive, in `roadmap-engine`, `roadmap-outline` and `orchestrator-artifacts` → 0 each; each carries exactly 1 today
- the two narrowed lines still carry their remaining content, so an over-deletion cannot pass as a narrowing → in `roadmap-engine`, the format block's direction-preamble line reads `<direction preamble: source spec links, hard rules, gating for this direction>` → 1; in `roadmap-outline`, the permission sentence still grants what item 3's rationale relies on — "Links to task specs are allowed as plain markdown links inside the intro/preamble prose" → 1 — and still ends "no formal `Spec:` tag, no invented task specs" → 1
- `handoff`, case-insensitive, in `roadmap-prune` → 4; it carries 5 today. The four that remain: two on the blocked-gate resolution's `/command-handoff` line, one on its `.ai-factory/handoffs/` destination line, one on "never swept"
- the `Phase note:` rationale still states all three of: keying on the literal token, links living in that same prose, and the skill holding `Bash(rm *)` → each 1
- the status-marker grammar still names the resolution session as the writer and still names a parked prune as the trigger → each 1
- the wrapping did not move → the `roadmap-engine`, `roadmap-outline` and `roadmap-prune` hunks change exactly one line each, and the `orchestrator-artifacts` hunk changes the two lines its phrase spans; in every hunk the changed text differs from its predecessor by the removed words and the re-wrap those words force, and no paragraph outside the edited phrase appears in the diff at all
- `git diff HEAD --stat -- src/` lists exactly the four named files and nothing else; `docs/`, `CLAUDE.md` and `active/` show no change from this task
- no frontmatter line changes in any of the four files → `git diff HEAD -- src/skills/*/SKILL.md | grep -cE '^[+-](name|description|loads|allowed-tools|argument-hint):'` → 0
