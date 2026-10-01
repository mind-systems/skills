# Phase 47 — the phase-note skill decides what its budget counts, what grounds a note and how it uses the engine

What still diverges, all in `src/skills/roadmap-outline-deep/SKILL.md`:

- **What the budget counts.** § "Step 2: Compress the preamble and attach the pointer" sets the preamble at "~200–500 characters … keeping the phase's gate and its `Phase note:` pointer" and never says whether the pointer counts toward it. The pointer is long enough that the answer decides whether a preamble fits.
- **What grounds a note.** § "Step 1: Write the phase note" asks, through its verbosity directive, for grounding "in the docs and code read at Step 0", conjunctively, with no clean way to say a note is grounded in the code alone. Its template covers an absent document with "Where no doc says how it must be, the note says so in one line", which answers the template's question and not the directive's presupposition.
- **How the skill uses the engine.** § "Load-once / dependencies" takes from `roadmap-engine` only the roadmap format and the named-roadmap resolution, while the other phase-tier and task-tier skills run the engine's maintenance flow and declare its hooks. This skill declares none of them and has no confirmation step before it rewrites preambles and mints files: its frontmatter allows `AskUserQuestion` and its body never uses it. Whether it should run the engine's flow is undecided.

What no longer diverges. The failure that named the phase, a note keyed one entry per task, was never reproducible in this repository, and the skill's template already defines the note as what diverges now and what decomposition cuts tasks from, in words, with links to the documents. The `skill-cycle.md` description of the pass was rewritten and agrees with the skill, so the two phase notes the earlier text named by file are no longer a standard to measure against. The re-run rule's third branch belongs to another phase.

Nothing under `docs/` is written.
