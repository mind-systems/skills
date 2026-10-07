# Phase 79 — the lenses carry their descriptions in the field and the hand can load one

[skill-description-field](../../../docs/skill-description-field.md) says the field is "the `description:` of every skill in the family", "present every turn, whether the skill is invoked or not", and leans on lenses to show it: the agent knows a roadmap's file and format "without loading `roadmap-decompose`" (§ "A skill-description reads as knowledge, not an index"), and § "One vocabulary for the field" names `roadmap-outline`'s and `roadmap-decompose`'s skill descriptions as where "phases" and "tasks" are said. Those skills carry `disable-model-invocation: true`, which per Claude Code's skills documentation means "Description not in context, full skill loads when invoked", that Claude "can't invoke the skill on its own", and that it "Also prevents the skill from being preloaded into subagents". So the field the doc describes does not hold them, and what the doc offers as its proof is read from descriptions that are not there.

Where the files stand:
- **The flag** is in the frontmatter of `agent-architect`, `roadmap-outline`, `roadmap-outline-deep`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-test-coverage`, `roadmap-prune` and `task-rescue`. `roadmap-prune` and `task-rescue` delete or roll back files with the user present and keep it. `architect-editor-engine` and the other engines carry `disable-model-invocation: false`.
- **`architect-editor-engine`** says "Load this skill once at birth — the architect per the instruction in its own body, the editor as the first action on spawn". It says this of itself and of no other skill.
- **`src/agents/editor.md`**: the frontmatter has no `skills:` field, and `tools:` lists `Skill`. Its body has the hand load the engine "as the very first action on spawn". For a lens the hand has only the pinned path, "Either mode's target may arrive via a pinned skill path", which `agent-architect` § "Relay on the marker; author the apply work-order and your own legwork" fills by expanding a payload's slash command to "read and run `~/.claude/skills/<name>/SKILL.md`". That route is the workaround for a skill the hand cannot invoke.

Claude Code's subagents documentation, on a definition's `skills:` field: "The full skill content is injected into the subagent's context at startup, not only the description"; a skill with the flag cannot be preloaded, and a missing or disabled one is skipped with a warning. Without the field, "the subagent can discover and invoke project, user, and plugin skills through the Skill tool during execution".

The hand keeps loading the engine itself as its first action at spawn, and no skill is preloaded through `skills:`: a preload injects a whole skill at every spawn, and a missing or flagged one is skipped with only a warning. A lens a round needs is loaded once through the `Skill` tool when the work needs it, which removing the flag opens, and is then held.

Where no doc says how it must be:
- `skill-description-field.md` says nothing of the flag or of which skills are in the field.
- `paired-loop.md` says nothing of the flag, and nothing of a skill the work needs being loaded once by whoever does the work and then held; it states the engine "both halves load at birth" and that a skill "is read once, when a head starts, and fades within a few messages" (§ "Where the pair's behaviour lives"). The docs are amended first.

With descriptions back in the field the orchestrator's agents see the lenses too. A planner there invoking a planning lens is the first thing to watch.
