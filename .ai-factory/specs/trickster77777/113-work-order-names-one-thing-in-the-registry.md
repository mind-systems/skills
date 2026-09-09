# `work-order` names one thing in the registry

## Current state (grounded, read fresh)

`docs/reserved-words.md` states its contract in both directions: "**one meaning, one word** — a concept is never named two ways — and **one word, one meaning** — a reserved word is never repurposed for another concept."

The word `work-order` appears in two of its entries, for two different concepts. Under § "Roadmap artifacts": "**task spec** — one task's full specification file under `.ai-factory/specs/`, written through `note`, referenced by the contract line's tag; the implementation-tier work-order." Under § "Paired loop": "**architect** — the plan-and-review persona: reasons, decides, drafts work-orders; never touches shared artifacts itself."

The two are different artifacts. A task spec is read by whoever plans the work and by whoever reviews it, and it outlives both; a work-order is handed to one executor, applied once, and thrown away. The registry names them with one word, and that conflation is what licensed a task spec to be written in a work-order's register — the register the phase this task belongs to is removing.

The file opens with "> This document is final and is not subject to update."

## The change

The task spec entry loses the phrase `the implementation-tier work-order` and ends at its `Spec:`-tag clause. The entry already names the artifact fully — its file, its directory, how it is written, how it is reached — and the tier it belongs to is stated by § "Roadmap artifacts" holding it beside the contract line.

The § "Paired loop" architect entry keeps the word: that is the concept `work-order` names.

No other entry changes, no term is added, and no term is removed from the registry.

## Blast radius

This is not an update to the registry's meanings, which its opening line forecloses. It removes a collision the registry's own bidirectional rule already forbids — the document is being made to obey itself, and the set of terms it binds is unchanged.

A sweep of `docs/`, both CLAUDE.md files and `.ai-factory/ARCHITECTURE.md` finds no other place where `work-order` names the task spec, so nothing else has to move with it.
