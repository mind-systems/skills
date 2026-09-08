# always-loaded-discipline — the layer that acts before it is called

The always-loaded layer has two halves, and they differ in kind. One names what exists: the [skill-description-field](skill-description-field.md), every skill's `description:` read as one continuous text — vocabulary, surfaces, the moment to invoke. The other prescribes how to act: the global CLAUDE.md, § "Grounding claims" — change moves docs → roadmap → code, a claim is grounded by walking to the leaf, held context decays back into description, the `[x]`/`[ ]` seam is where a run stands. Both sit in the system prompt every turn. The first is read as knowledge; the second is executed as instruction.

## The discipline produces behavior with no skill invoked

A phase whose documentation does not describe what its tasks would build is not decomposed: the agent stops and puts the documentation first. No skill carries that gate and none needs to — the direction docs → roadmap → code is present in every session and is enough by itself. The same layer supplies the refusal to trust a description over the file it describes, and the re-read of a leaf before acting on it.

That is what makes the layer load-bearing rather than ambient. A guarantee that holds in every session of every project, without a call, is a guarantee a skill may build on.

## What a skill body holds

Only what the layer does not already guarantee. A skill that restates the discipline pays for the restatement on every load, and drifts from its source the moment the source moves — the copy then argues with the original inside one context window. The body carries mechanism, format, and the decisions of its own tier.

## Reliance is declared where it is leaned on

A skill that stands on a guarantee of the layer names it in one sentence, at the point where it stands on it. An implicit reliance is invisible: the guarantee lives in a file the skill never mentions, no grep joins the two, and a change above removes a behavior nobody can trace back. This is the rule the repository already applies to a cross-file invariant — one sentence at the coupling point, in both files — applied to the coupling between a skill and the layer above it.

## The layer sets direction; the walk still happens

Always-loaded means compressed and lossy. The discipline states which way change moves and how a claim is grounded; it never carries the wording of a gate or the exact rule of a format. Where the edge matters, the walk to the leaf still runs — the same pairing described in [context-tree](philosophy/context-tree.md) and in the sibling half at [skill-description-field](skill-description-field.md).

## Where things are normed

The discipline itself is normed in the global CLAUDE.md § "Grounding claims", whose source in this repository is `src/global/CLAUDE.md`. The description half is [skill-description-field](skill-description-field.md); the walked layer is [context-tree](philosophy/context-tree.md); the authoring rule that follows from this file — a skill restates nothing the layer guarantees, and declares what it leans on — is normed in `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy".
