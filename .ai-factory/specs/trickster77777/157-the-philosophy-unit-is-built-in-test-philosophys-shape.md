# 57.2 — the philosophy unit itself

## Current state

No skill for this exists anywhere in the repository — checked directly (`ls src/skills/ active/skills/ | grep -i "polymorphism\|oop"` returns nothing). This phase's own note, `.ai-factory/specs/trickster77777/151-…md`, settles the unit's content in full — the question, the trigger, the exemption, the vocabulary — and this task does not re-derive it or add to it.

The precedent this task mirrors, `src/skills/test-philosophy/SKILL.md`, is a shared pure-content philosophy unit: one discriminator, no I/O, `user-invocable: true`, loaded once per chat by its callers, with a reverse-graph grep line in its own body rather than a caller list. `active/skills/test-philosophy` is a symlink: `test-philosophy -> ../../src/skills/test-philosophy` (confirmed by `ls -la active/skills/`), matching `active/skills/roadmap-engine -> ../../src/skills/roadmap-engine` exactly — the pattern every symlink in that directory follows.

**Directory name — decided.** `polymorphism-philosophy`, parallel to `test-philosophy`: it names the unit's subject and its genre in the same two words that already name the precedent. `name:` in frontmatter matches the directory name exactly (validator-enforced, per `CLAUDE.md` § "Key constraints"), and both are machine-resolved identifiers that outlive any later rewording of the skill's prose.

## The change

A new directory, `src/skills/polymorphism-philosophy/`, holding one file, `SKILL.md`:

```yaml
---
name: polymorphism-philosophy
description: >-
  Shared philosophy unit for the roadmap family. Holds one question — to add a
  third kind, how many places must change — fired only when a kind gains its
  second member, never on style. Carries no refactoring procedure of its own.
user-invocable: true
disable-model-invocation: false
allowed-tools: Read
---

# Polymorphism Philosophy — Shared Shape-of-a-Distinction Philosophy

This is a shared pure-content philosophy unit for the roadmap family, built in
`test-philosophy`'s own shape. It holds one discriminator — whether a distinction
is carried by a type or by a field — not any refactoring procedure. The calling
skill (`roadmap-decompose-skeleton`) stays in control of when and how it applies
the question; this skill has no I/O of its own. It is also directly invocable: the
user supplies the route himself, naming a region and what raises suspicion, with
no thin lens required over this file. Load this skill once per chat. This is a
load-once engine: its callers depend on its exact behavior — edits here must honor
their expectations as part of its contract; the reverse graph resolves via
`` grep -l "polymorphism-philosophy" src/skills/*/SKILL.md src/commands/*.md ``.

## The question

Put to the code as the open/closed principle, not as an invented threshold:

> **To add a third kind, how many places must change?**

One place — the site that constructs — is correct on its own terms. More than one
means the distinction was never actually polymorphic, whatever the type signatures
suggest.

## The two entries

One question, reached two ways. The **time** entry takes what a change just
brought: does this change bring a second member to a kind, and was a seam cut
at that arrival or not — its evidence is the diff. The **space** entry takes a
named region with no change to trigger it — a module, a directory, a class —
and inventories the kinds declared there (a union of two or more members, an
enum, a boolean field naming a mode, a set of subclasses), asking the same
question of each. A consumer skill reaches this unit through the time entry; a
direct invocation, naming a region, reaches it through the space entry.

## The trigger

The arrival of the second invariant — an event, not a count of branches and not a
threshold. Before the second invariant there is nothing to do; after it there is
exactly one question to ask, above.

## The exemption

The constructing site is never itself a finding. Branching before the object
exists is construction; branching after it, on a field the object already
carries, is the smell.

## The vocabulary

Classical, cited rather than re-derived: a conditional over a type code, replaced
by polymorphism. A type-code field itself, replaced by subclasses, by state, or by
strategy. For the data-side twin of the same smell: illegal states made
unrepresentable.

Default: no finding at all. It fires only on the event, never on style.
```

Plus one symlink: `active/skills/polymorphism-philosophy -> ../../src/skills/polymorphism-philosophy`, created the way the existing symlinks in that directory are — `ln -sfn ../../src/skills/polymorphism-philosophy active/skills/polymorphism-philosophy` — matching `test-philosophy`'s and `roadmap-engine`'s exactly.

`CLAUDE.md` gains the new name in both of its exhaustive skill rosters, inserted immediately after `test-philosophy` in each — the sibling this unit is built beside. **"The active set"** paragraph becomes, only the touched span shown: "...`aif-docs`, `test-philosophy`, `polymorphism-philosophy`, `roadmap-outline`,...". **"Everything else in `src/skills/` is ours"** paragraph becomes: "...`note`, `test-philosophy`, `polymorphism-philosophy`, `observe-logs`,...". No other word in either paragraph changes; the "Repository Structure" tree a few lines above the first of these already ends its skill sample in `…` and makes no completeness claim, so it does not change.

This deploys alone and makes sense: the skill exists, is directly invocable per the user's own standing ruling, and needs no consumer wired to it to be usable — task 57.3 is what gives it its first consumer, not what makes it exist.

## Blast radius

**Rule:** the directory name and the frontmatter `name:` value must match each other and must not collide with any existing skill or symlink; the symlink target must resolve.

**Sweep (re-runnable):**
```
ls src/skills/ active/skills/ 2>/dev/null | grep -i "polymorphism-philosophy"
```

**Invariant:** after the change, `src/skills/polymorphism-philosophy` exists as a real directory and `active/skills/polymorphism-philosophy` exists as a symlink resolving to it, and no other entry anywhere claims the same name. Before this task, neither path existed, confirming no prior claim on the name.

**A second rule:** `CLAUDE.md` carries two exhaustive rosters of skills that this task's own addition would invalidate — the **"The active set"** paragraph, naming every skill actually symlinked into `active/skills/`, and the **"Everything else in `src/skills/` is ours"** paragraph, naming every no-upstream-counterpart skill in `src/skills/`. Neither carries an ellipsis or any other mark of incompleteness, so both assert completeness and both go stale the moment this task's skill exists unnamed in them.

**Sweep (re-runnable):**
```
grep -c "polymorphism-philosophy" CLAUDE.md
```

**Invariant:** after the change, `polymorphism-philosophy` stands named in both of the two rosters above — the "Repository Structure" tree makes no completeness claim and is outside this invariant, per the guard above. Before this task, the sweep finds it in neither roster.
