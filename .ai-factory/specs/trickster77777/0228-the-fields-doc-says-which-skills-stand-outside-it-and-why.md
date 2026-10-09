# 79.1 — the field's doc says which skills stand outside it, and why

## What is true now

`docs/skill-description-field.md`, in its opening paragraph, describes the field as "the skill-description (the `description:` of every skill in the family)" and says "All skill-descriptions loaded at once form one layer — the **skill-description-field**." The doc says nothing of `disable-model-invocation`, and nothing of which skills stand outside the field. `docs/always-loaded-discipline.md`, in its opening paragraph, says "the [skill-description-field](skill-description-field.md), every skill's `description:` read as one continuous text".

The skills that carry `disable-model-invocation: true` today are `agent-architect`, `roadmap-outline`, `roadmap-outline-deep`, `roadmap-decompose`, `roadmap-decompose-skeleton`, `roadmap-test-coverage`, `roadmap-prune` and `task-rescue`; the engines and the other skills carry `false`. A flagged skill's description is not in the field. What `roadmap-prune`, `task-rescue`, `agent-architect` and `roadmap-test-coverage` do is reviewed only before it happens, with the user present, and never after: `roadmap-prune` deletes files, `task-rescue` rolls artifacts back, `agent-architect` founds a head's folder, and `roadmap-test-coverage` spends research whose scope the operator sets first (`docs/test-coverage-pass.md` § "The operator vets scope before research spends anything"). The planning lenses write additive text, roadmap lines, task specs and phase notes, which is reviewed after. No open task above this one edits either doc.

## What must be true after

In `docs/skill-description-field.md`, the opening paragraph's parenthesis reads "(the `description:` of each skill the agent may call on its own)", and directly after the sentence "All skill-descriptions loaded at once form one layer — the **skill-description-field**." this sentence stands:

"A skill whose work is reviewed only before it happens, with the user present, and never after (deleting files, for one) is called by the user alone, and stays out of the field."

In `docs/always-loaded-discipline.md`, the opening paragraph's "every skill's `description:` read as one continuous text" reads "the `description:` of each skill the agent may call on its own, read as one continuous text".

Nothing else in either file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it says the field holds the description of every skill in the family.

**Sweep:**
```
grep -rn "of every skill in the family\|every skill's \`description:\`\|all skill descriptions" docs CLAUDE.md
```

**Finding.** The sweep returns the field doc's opening paragraph, the target; the opening paragraph of `docs/always-loaded-discipline.md`, which reads wider than the field once the sentence above stands and changes as pinned; and the registry entry in `docs/reserved-words.md`, which says "all skill descriptions loaded at once", true of the descriptions that are loaded, and stays, the registry being the user's to touch. No `CLAUDE.md` text appears in its output.
