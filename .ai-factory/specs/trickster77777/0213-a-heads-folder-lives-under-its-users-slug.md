# Phase 76 — a head's folder lives under its user's slug

[paired-loop](../../../docs/paired-loop.md) § "Where the memory lives" now puts a head's folder at `.ai-factory/architects/<user-slug>/<NN>/`, inside its user's own folder, numbered within it, the slug derived as for a named roadmap, and § "The team" names a link by repository, owner's slug and folder number. The skills still describe the flat layout.

- **`architect-editor-engine`**, § "The architect's buffer": the buffer "lives in the architect's own folder, `.ai-factory/architects/<NN>/`", and a new head's folder "takes the number one above the highest folder under `.ai-factory/architects/`". Path and numbering are this skill's alone, so every other reader inherits the flat form from it.
- **`agent-architect`**: § "Spawn once, message thereafter" has the probe "look under `.ai-factory/architects/` for the folder whose `address.md` holds" the session id, and the session id is unique, so it finds the head's folder wherever it lies under that directory, the user's folder included, and the probe needs no change; a founding creates the folder at the engine's path; § "Working with another architect" names peers "by folder number" and reaches one at "`.ai-factory/architects/<NN>/address.md`".
- **`templates/buffer-seed.md`**: the `## Team` placeholder has links "each by repository and folder number".

Existing heads are moved into their user's folder by hand by the user, as before; that is not a skill feature.
