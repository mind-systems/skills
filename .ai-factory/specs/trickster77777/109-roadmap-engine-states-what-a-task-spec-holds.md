# `roadmap-engine` states what a task spec holds

## Current state (grounded, read fresh)

`src/skills/roadmap-engine/SKILL.md` § "The two-tier artifact" defines the task spec: its path, its numbering, the `Spec:` tag it is reached through, that it "follows `note`'s format", and that it "holds the full implementation detail". What that detail is, the section never says.

The one enumeration of parts in the file sits elsewhere, as the last bullet of "Rules for writing a contract line": "Full current-state / target / guards / verify detail lives in the task spec, not the contract line". That is a statement about where detail goes, not a shape for the spec — and its four parts are not the three below.

`note` supplies no shape either: its template hook is caller-supplied, and its own default template — Key Findings / Details / Open Questions — is the genre of a standalone note, not of a spec.

So a task spec takes the shape of whoever writes it. A session spent authoring apply work-orders supplies the work-order's shape: guards against what nobody was going to do, and counts that restate the instruction they check.

## The change

§ "The two-tier artifact" gains one paragraph, placed after the **Why two tiers:** paragraph, naming what a task spec holds and nothing else:

- **what is true now** — read from the code, with exact values, so the implementer does not re-derive it;
- **what must be true after** — behaviour in the code's own terms: which file, which text, which value;
- **what breaks on contact** — enumerated, never "may need updating".

The contract-line bullet is brought into line with it and reads: "Full current-state / target / blast-radius detail lives in the task spec, not the contract line".

## Blast radius

`roadmap-engine` is a load-once engine with eight callers. The four-part enumeration this task changes occurs exactly once in the repository, at that bullet; no skill or command restates it, and no skill or command prescribes a task spec's sections.

Task specs already on disk are not rewritten. The paragraph states the shape for what is written next.
