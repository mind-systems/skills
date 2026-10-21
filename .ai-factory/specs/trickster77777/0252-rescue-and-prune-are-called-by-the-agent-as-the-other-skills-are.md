# 92.1 — rescue and prune are called by the agent as the other skills are

## What is true now

`src/skills/task-rescue/SKILL.md` and `src/skills/roadmap-prune/SKILL.md` each carry `disable-model-invocation: true` in their frontmatter, so only the user's slash command invokes them; the agent cannot call either on its own and neither description is in the skill description field. The other skills that load and write roadmap artifacts carry `disable-model-invocation: false`. The head that launches the orchestrator answers for the run: on a stop it must be able to take a rescue itself, and after the run a prune. The user: «я хочу свободу агентам. Скилы не про заборы, а про то, как система роадмапа работает».

## What must be true after

In `src/skills/task-rescue/SKILL.md` the frontmatter line reads `disable-model-invocation: false`.

In `src/skills/roadmap-prune/SKILL.md` the frontmatter line reads `disable-model-invocation: false`.

Nothing else in either file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it says that the user alone calls `task-rescue` or `roadmap-prune`, or if it keeps either skill out of the field on account of the flag.

**Sweep:**
```
grep -rn "disable-model-invocation" src docs CLAUDE.md
```

**Finding.** In `src` the search returns the two targets and, besides them, `agent-architect` and `roadmap-test-coverage`, which keep `true` and are not targets; every other skill already reads `false`. In `docs` and `CLAUDE.md` it returns nothing: `docs/skill-description-field.md` and `docs/always-loaded-discipline.md` describe the field as the descriptions of the skills the agent may call on its own, which now includes both targets, so neither needs a change.
