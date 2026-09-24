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
