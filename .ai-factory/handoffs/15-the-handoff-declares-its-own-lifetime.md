# Handoff — the handoff declares its own lifetime

**Processed:** `[x]` — whoever reads this marks it; a marked handoff is spent.

## 1. Frame

Task 31.1 is written and has not run. It gives `command-handoff` three edits in one file so that a handoff states, on itself, what it is and whether it has been used. This file is written in the shape that task prescribes, before the task implements it — the mark above is the form under review.

## 2. Read-first map

### Must-read now (minimal rehydration set)

- `.ai-factory/specs/trickster77777/106-handoff-processed-mark.md` — the task spec, three items and five guards.
- The `31.1` contract line under `### Phase 31` in `.ai-factory/roadmaps/trickster77777.md`.
- `src/commands/command-handoff.md` — the file all three edits land in: its `description:` block, the emitted template's top, and the body.

### Read on demand

- `docs/reference-by-name.md` — why this handoff cites by name and not by line.
- The global CLAUDE.md, § "Documentation style", rule "Comments never cite the plan layer" — the same prohibition one tier down, deliberately not restated by this task.

## 3. Current state

The roadmap line and the spec are written and uncommitted. Nothing under `src/` is touched: the skill itself is the orchestrator's to edit.

Three things the task changes, all in `src/commands/command-handoff.md`:

- the `description:` names the entity — a temporary memory buffer carrying context from one session to the next, spent once read — and states that no document and no task references a handoff. The word `durable` leaves the block, because it asserts the opposite of what the artifact is.
- the emitted template gains one line between the `# Handoff` title and `## 1. Frame`: the mark, and the sentence naming the reader as the one who flips it.
- the body gains the rule the mark carries: a processed handoff is never edited and never cited as confirmation; only an unprocessed one is edited; where a cross-project handoff is assembled in parts and the previous part is already marked, a new handoff is written rather than the old one extended.

## 4. Next step

The task goes to the orchestrator like any other. Nothing here needs deciding first.

## 5. Working discipline

**Why the rule needs no enforcer.** Nothing in this family reads a handoff as a step: `command-handoff` writes them, `roadmap-prune` writes one when its gate blocks and states that `handoffs/` is never swept, and no other skill names the directory. So the instruction cannot live in a reader — it travels on the artifact, addressed to whoever opens it. That is the whole mechanism, and it is why no skill gains a step and nothing scans the mark.

**Why the prohibition belongs in the `description:`.** That block is always-loaded context. A rule about what may cite a handoff has to reach agents that never open this skill, and the description is the only surface that reaches them.

**Why the entity is named rather than described.** "Temporary buffer, spent once read" is what the file is. Calling it a durable note, as the block does today, is what let a spent one keep being cited as confirmation years after its facts moved.

## 6. Error log

Things weighed and deliberately left out. Re-adding any of them re-opens a decision already made:

- **The objections branch.** "Even with objections the reader marks it and writes their own" was the user's explanation of why the rule is simple, not a clause to encode. It was proposed and struck.
- **A third state, a date, an author of the reading.** Two states, nothing else.
- **A protocol token.** The mark is prose for a reader. Nothing greps it, and no verification counts it in a handoff.
- **The code-never-cites-tasks analogy.** It already exists in the global CLAUDE.md and is not repeated here; a skill restates nothing an always-loaded layer already guarantees.
- **Backfilling the handoffs already on disk.** Out of scope by guard.

## 7. Orientation

The direction above Phase 31 states the problem in one line: a spent handoff looks exactly like a live one. Everything in the task follows from making that visible on the file itself.

## 8. Domain model spine

A handoff is mined from a live session and written through `note` into `<root>/.ai-factory/handoffs/`. It is one-shot by nature: its facts age from the moment it is written, and the session it was mined from no longer exists. Its readers are humans and fresh sessions, never a skill. After this task, its lifetime is stated on it and in the always-loaded description, and its two states — unprocessed and spent — are the only thing anyone needs to know before deciding whether to trust it.
