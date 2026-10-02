# Phase 52 — the researcher can write, and the note's title is the name research chose

Governing spec: `docs/test-coverage-pass.md`

`roadmap-test-coverage` § "Layer 4 — Deep Research (parallel agents)" has two places where the researcher's work is set up against what it is.

- **The writing agent.** The section says "Launch one `Explore` agent per area in a **single message** (parallel). Each agent writes its note to disk and returns one line", and its prompt tells the agent "You write the file yourself, at the path you just chose, in the same act". `Explore` has every tool except `Edit`, `Write` and `NotebookEdit`: it is read-only by definition, and the later layers already use `general-purpose` agents. The user's field evidence: "Много раз замечал — исследователи отказываются писать и главному приходится самому записывать." The writer wants an agent type that can write, `general-purpose`.
- **The note's title.** The prompt names the area `Area: <area name>` and tells the agent to choose the slug "only after you have read the source below … not for the Area label above", and the template then opens `# <Area Name> — Test Plan`. A note whose slug says what the area turned out to be carries a title that says what it was called before research began. The title wants the same post-research name the slug takes.

[test-coverage-pass](../../../docs/test-coverage-pass.md) names neither the agent type nor the title, and does not contradict either change. Its § "Research runs in disposable hands, never a persistent one" speaks only of "one throwaway agent per area", and its § "A number is fixed before research; a name is not" says the name is pinned "late enough to still be true once research has actually looked", which is the reading the title follows. The later layers' annotations, `(<area name>)` and the like, are the orchestrator's own labels for the area as it scoped it, and are not read from the note.
