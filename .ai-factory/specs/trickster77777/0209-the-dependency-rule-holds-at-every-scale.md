# 73.2 — the dependency rule holds at every scale

## What is true now

`src/skills/aif-architecture/references/architecture.md` states the dependency rule once, under the Explicit Architecture: "**Dependency rule:** Dependencies point INWARD. Outer layers implement interfaces (ports) defined by inner layers. Inner layers NEVER import from outer layers." — and its principle "**Ports and Adapters (Hexagonal):**" repeats it for the whole application. The Structured Modules' principle "**Separation from DDD:**" says it "does not enforce strict Aggregate roots, isolated Domain Events, or rigid hexagonal ports". The Layered pattern's "**Strict Downward Dependencies:**" has each layer depend on the layer below it, the data layer last. Nothing in the file names a pattern for the inside of a feature module or of a presentation layer, and no text says the rule is the same one at those scales. The user builds this way, a loose VIPER-like split per feature module and MVVM inside presentation, and names it so: "все эти умные слова — тоже инварианты гексагональной архитектуры".

## What must be true after

After the section "## Where the System Varies — Ports and Adapters" that 73.1 adds, and before "## Terminology", the reference gains this section:

"## The Dependency Rule at Every Scale

One rule — details depend on abstractions the core owns, never the reverse — holds at each scale at which a system has a core with details around it. The scales nest; the rule does not change.

- **The system's edge** — Ports and Adapters. The domain core owns the ports; storage, network and providers are adapters; the composition root assembles them.
- **A feature module** — three responsibilities, a loose likeness of VIPER and no letter-for-letter mapping of it: the data the module owns, the layer that decides, and presentation. Presentation depends on what the deciding layer exposes, and the deciding layer on what the data exposes, never the reverse; modules nest, each owning the abstractions its parts depend on.
- **The inside of presentation** — MVVM. The view depends on its view-model, and the view-model on the deciding layer's abstractions.

This is Clean Architecture's dependency rule seen at each scale, not a different architecture at each. How strictly a packaging pattern enforces it is the matrix's "Domain purity" row. At every scale there are the same two things to look for: where the variations live and which way the dependencies point; the folders that follow from them are packaging, named second."

Nothing else in the file changes.

## What breaks on contact

**Rule:** a text breaks on this change if it states the dependency rule as a property of one pattern or one scale only, or states a direction between a deciding layer and its details that the new section reverses.

**Sweep:**
```
grep -n -i "dependency rule\|point inward\|hexagonal\|strict downward\|viper\|mvvm" src/skills/aif-architecture/references/architecture.md
grep -rn -i "viper\|mvvm" src docs CLAUDE.md --include="*.md"
```

**Finding.** The first search reaches the Explicit Architecture's "Dependency rule" and the "Ports and Adapters (Hexagonal)" principle, which are the system-edge case of the new section and stay; the Structured Modules' disclaimer of "rigid hexagonal ports", which stays, the new section describing a loose split and not a rigid one; and the Layered pattern's "Strict Downward Dependencies", which stays, since the Layered pattern does not invert and the matrix's "Domain purity" row, which the new section points to, scores it as such. The VIPER and MVVM terms occur only in this file's new text; the second search reaches no other file.
