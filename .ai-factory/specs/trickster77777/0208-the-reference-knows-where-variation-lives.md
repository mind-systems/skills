# 73.1 — the reference knows where variation lives

## What is true now

`src/skills/aif-architecture/references/architecture.md` opens with "## Decision Matrix", a table that scores the packaging patterns by team size, domain complexity, scale requirements and the like, followed by a "**Note on subvariants:**" paragraph; "## Terminology" follows, then "## Quick Decision Guide", whose lines include "New project, small team, simple domain? → Layered" and "Simple CRUD app? → Layered Architecture". The skill reads the matrix as the basis of its recommendation (`SKILL.md` Step 1: "Consider: team size, domain complexity, scale requirements, tech stack").

Ports are taught as one thing. The Explicit Architecture's principle "**Port Abstraction for External Dependencies:**" says "All dependencies on external systems (databases, messaging systems, file systems, third-party APIs) MUST be defined as interfaces (ports) in the Domain layer.", and the "Port and Adapter (Dependency Inversion)" example pairs one port, `OrderRepository`, with one adapter, `PostgresOrderRepository`, wired in a "COMPOSITION ROOT". No text says that a port can have an adapter per mode, environment or provider, or that where such a variation lives is a question of its own. A low score on team size or domain complexity reads as a system with nothing to vary.

## What must be true after

Directly after the "**Note on subvariants:**" paragraph, before "## Terminology", the reference gains this note and this section, in this order:

"**Note on what the matrix measures:** the matrix scores packaging fit only — how files are arranged and who imports whom. It does not score how many places the system varies or how many rules it must keep, and a low score on team size or domain complexity is not a finding that the system has none; a system with few lines can still have several implementations of one thing. Where the system varies is a separate question, answered in "Where the System Varies — Ports and Adapters" below."

"## Where the System Varies — Ports and Adapters

Ports and Adapters, also called hexagonal architecture (Alistair Cockburn), is the pattern that answers where a system varies; the place where its adapters are assembled is the composition root (Mark Seemann).

Packaging patterns answer where files lie and who imports whom. A second question is independent of them: where the system's variations live — modes, environments, providers, roles — and where each one is resolved.

A **variation axis** is a kind of thing the system has several implementations of. Each axis has a **port**, the interface the logic calls; an **adapter** for each value of the axis, implementing the port; and one **composition root**, the only place that knows which adapter runs, which picks it by a key it is handed — a mode, an environment name, a provider.

A port is therefore not only an interface to an external system: a port can have an adapter per mode, for instance one source of time that reads the clock and another that a replayed run advances itself. The logic is one flow for every value of the axis and never asks which value it runs under.

The rule that follows: a difference between values is a new adapter chosen at the composition root, never a branch on the key at the point where the logic calls it. A junction that must know the key means a port is missing.

A port that exists only so a test can substitute a fake is a test seam, not an axis, and is named as one.

Variation is an axis of its own beside the packaging patterns below, not a property of any one of them: every packaging pattern can hold a system with such axes. Describing the architecture of existing code starts here — which interfaces have several implementations, where, and by what key one is chosen — and packaging is named second."

Under "## Quick Decision Guide", between the heading and its code block, one line is added: "Each line below picks packaging only; none says anything about where the system varies."

Nothing else in the file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it presents the matrix or the guide as a measure of how simple the system is, or says a port is only an interface to an external system.

**Sweep:**
```
grep -n -i "simpl\|external" src/skills/aif-architecture/references/architecture.md
grep -rn -i "decision matrix" src docs CLAUDE.md
```

**Finding.** The first search reaches the two guide lines above, which stay, now under the line that says they pick packaging; "This is the simplest architectural pattern" in the Layered section, a statement about packaging that stays; and the "Port Abstraction for External Dependencies" principle, which stays true, external systems being one case of a port and the new section saying so. The second reaches two lines in `src/skills/aif-architecture/SKILL.md`, Step 1, that name the matrix as the basis of the recommendation: the opening line is rewritten in 73.4, sequenced after this task, and "Evaluate the project against the decision matrix" stays true, the matrix now saying it scores packaging. No other file in either repository reads the reference by name.
