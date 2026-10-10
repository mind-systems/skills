# 82.2 — the targeting argument names a phase, not a slug

## What is true now

`src/skills/roadmap-outline-deep/SKILL.md` carries `argument-hint: "[phase or slug]"` in its frontmatter, and its § "Targeting" opens "Optional arg — a phase or slug (matching `argument-hint`). Default: infer the target phase set from conversation context."

`src/skills/roadmap-decompose-skeleton/SKILL.md` carries `argument-hint: "[phase/slug or task description]"`, and its § "Targeting" opens "Optional arg — a phase, slug, or single task description. Default: infer the target open-`[ ]` task set from conversation context".

Neither skill defines a slug, and the user calls both by phase. The slug the registry fixes is the local-part of the git email, which names a user and not a target.

## What must be true after

In `src/skills/roadmap-outline-deep/SKILL.md`:

```
argument-hint: "[phase]"
```

and § "Targeting" opens: "Optional arg — a phase (matching `argument-hint`). Default: infer the target phase set from conversation context."

In `src/skills/roadmap-decompose-skeleton/SKILL.md`:

```
argument-hint: "[phase or task description]"
```

and § "Targeting" opens: "Optional arg — a phase or a single task description. Default: infer the target open-`[ ]` task set from conversation context".

The rest of each sentence and of each section stands.

## What breaks on contact

**Rule:** a text breaks on this change if it offers a slug as a target of either skill.

**Sweep:**
```
grep -rn "phase or slug" src docs CLAUDE.md README.md
grep -rn "phase/slug" src docs CLAUDE.md README.md
grep -rn "phase, slug" src docs CLAUDE.md README.md
```

**Finding.** The search for `phase or slug` returns the two lines of `roadmap-outline-deep`, the hint and the targeting sentence. The searches for `phase/slug` and `phase, slug` each return the one line of `roadmap-decompose-skeleton`, the hint and the targeting sentence respectively. No doc, `CLAUDE.md` or `README.md` text appears in any output.
