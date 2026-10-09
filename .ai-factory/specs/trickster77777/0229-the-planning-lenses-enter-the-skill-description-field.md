# 79.2 — the planning lenses enter the skill description field

## What is true now

`src/skills/roadmap-outline/SKILL.md`, `src/skills/roadmap-outline-deep/SKILL.md`, `src/skills/roadmap-decompose/SKILL.md` and `src/skills/roadmap-decompose-skeleton/SKILL.md` each carry `disable-model-invocation: true` in their frontmatter. A skill with the flag has no description in the field, and no agent can load it through the `Skill` tool. `src/agents/editor.md` lists `Skill` among its `tools:` and has no `skills:` field, so the hand reaches a flagged lens only by the pinned path of a work-order. `architect-editor-engine` and the other engines carry `disable-model-invocation: false`.

As 79.1 leaves it, `docs/skill-description-field.md` says the field holds the description of each skill the agent may call on its own, and that a skill whose work is reviewed only before it happens, with the user present, and never after, stays out of it. The planning lenses write additive text, which is reviewed after; they are not of that kind. No open task above this one edits their files.

## What must be true after

In the frontmatter of each of them, the flag line reads:

```
disable-model-invocation: false
```

as `architect-editor-engine` carries it. Nothing else in those files changes.

## What breaks on contact

**Rule:** a text breaks on this change if it presents one of these planning lenses as called by the user alone.

**Sweep:**
```
grep -rn "disable-model-invocation" src docs CLAUDE.md
```

**Finding.** The sweep returns the flag line of every skill, the frontmatters of these skills among them; no doc and no `CLAUDE.md` text mentions the flag. The descriptions of these skills join the field of every session that loads the personal skills, the sessions of the orchestrator's agents among them.
