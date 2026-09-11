# The name is chosen after the research

## Current state (grounded, read fresh)

`src/skills/roadmap-test-coverage/SKILL.md`'s research-agent prompt hands each spawned agent both the number and the name of the file it will write, settled before the agent has read anything: "Area: `<area name>`" opens the prompt, and the destination follows immediately — "Note to write: `.ai-factory/specs/<NN>-<slug>.md`." Further down, the same fixed pair recurs: "Write the following document to `.ai-factory/specs/<NN>-<slug>.md`:" introduces the note template, and the agent's own required return line — "saved: `.ai-factory/specs/<NN>-<slug>.md`" — echoes the identical placeholder back rather than reporting what it actually wrote. All of them are the same `<NN>-<slug>` pair, fixed once, before Step 1 of the agent's own task list ever runs.

Checked every site in the file that names this destination, not assumed: the sites named above, plus the pointer Layer 6 keeps for a refactor item, the confirmation line Layer 8 prints per note, and the pointer forms in Layer 8's handoff block. Every one of them carries the bare placeholder `<NN>-<slug>.md`; none carries a literal name anywhere in the file.

`docs/test-coverage-pass.md` § "A number is fixed before research; a name is not" states the governing behaviour this current state falls short of: "The number a new note is filed under has to be settled before research starts, or two areas researched in parallel collide on the same file. The name cannot be settled at the same moment: research is what can show that an area named for one thing is really something else, and an area has had to be renamed after the fact for exactly this reason. The two are pinned at different moments on purpose — the number early enough to prevent a collision, the name late enough to still be true once research has actually looked."

The skill does not yet do this. An area named for one thing has turned out, on research, to be something else — every identifier the named surface was supposed to involve returned zero occurrences — and the file already written under that name had to be renamed after the fact. The number caused no such trouble; only the name, fixed at the same moment as the number, did.

## The change

The number stays exactly where it is: computed once, before any agent is spawned, and handed to each agent already fixed — that half of the prompt is untouched. The name comes out of that same moment and moves to the end of the agent's own task, after it has read the source and knows what the area actually is.

The prompt hands the agent the number alone for its destination, not a finished path, and instructs the agent to choose the slug itself from what its own reading found, once that reading is done — the same point at which the document body itself is composed. The instruction that currently reads "Write the following document to `.ai-factory/specs/<NN>-<slug>.md`" is reworded so the slug is the agent's own choice, made at that moment, not a value carried in from the spawn prompt. The agent's return line stops echoing the placeholder and instead reports the exact path it used, slug included, since that is the only place the real name exists until the agent reports it.

One point is easy to get backwards, so it is stated directly: the agent is the one holding the pen — it writes the file itself, at the path it chooses, in the same act. A name "returned afterward" for the caller to apply retroactively would arrive after the file already exists under whatever the caller decides, which is not what "the agent derives the name" means; the decision has to sit with the agent at the moment it writes, not with the caller after the agent is done.

## Blast radius

38.2 already landed, and it changed a different, earlier part of the same agent-spawning step — the number's own computation, above where the agent prompt begins — not any of the sentences this task touches. The two sit next to each other in the file, not inside one another; grounding above is taken from the file as it already stands after 38.2, not from an earlier state, so there is no ordering left to state.

The destination-naming sites named in Current State carry only the placeholder `<NN>-<slug>.md`, whose meaning follows from the place the pair is actually decided — the same shape 38.2 already established for the number alone, now extended to the name: none of them needs its own edit. Only the agent-prompt template's own wording — the "Note to write" line, the "Write the following document to" line, and the return line — changes; nothing else in the file names or depends on when the slug is chosen.
