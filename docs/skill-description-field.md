# skill-description-field — part of the system prompt

Project knowledge has two layers, not one. One is walked — the context tree ([context-tree](philosophy/context-tree.md)): raised task by task, branch by branch, down to the leaf, with only the map loaded at entry. The other is loaded always — the skill-description (the `description:` of every skill in the family). The harness injects it into the system prompt as the skills manifest (the agent decides from it whether to invoke a skill), on the same always-loaded layer as the global CLAUDE.md: it is present every turn, whether the skill is invoked or not, and it weighs as a system instruction, not as an index line. All skill-descriptions loaded at once form one layer — the **skill-description-field**. The top of the pyramid ([skill-pyramid](philosophy/skill-pyramid.md)) is exactly the skill-description; here — the field they form together.

## A skill-description reads as knowledge, not an index

The stated purpose of `description` is routing: what a skill does and when to call it. But it sits in the system prompt, and the system prompt is something the agent executes, not something it consults on demand: the vocabulary and intent a skill-description carries enter behavior before and without the body being loaded. The proof is that flows run with no explicit call: "make a task in the roadmap" — and the agent already knows the file (`.ai-factory/ROADMAP.md`), the format (two-tier: contract-line plus task-spec), the `[x]`/`[ ]` axis, without loading `roadmap-decompose`. The volume of instruction that once required loading a skill is already present in the skill-description-field.

## Coherent reading of all skill-descriptions

Loaded at once, the skill-descriptions are read together, as one description. The value of the skill-description-field is its coherence: when the skill-descriptions name one world in one vocabulary at one abstraction-level, the joint reading yields a single consistent model of the project, and attention converges on what the task names. When one thing is named two ways, or from different abstraction-levels, the model diverges and behavior gets contradictory footholds. The aim of tuning the field is coherence: one vocabulary, an even abstraction-level.

A consequence of a coherent field is action without invocation. The agent recognizes that a task enters the zone of `command-pin-gaps` (close the places an implementer would guess at) and does that work without loading the skill: the skill-description set both the vocabulary and the intent before any load. So the skill-description-field shapes behavior regardless of whether the skill is invoked.

## Weight through repetition — vocabulary, not fact

A word named in the CLAUDE.md, in a skill-description, in a doc title, and in roadmap prose gains weight: repetition is emphasis, and emphasis is a tuning knob. On the surface this is the duplication that one-home-per-fact forbids — but it is not. A **fact** has one home: a value, a procedure, the exact wording of a rule; a copy of it drifts. The **vocabulary** — the words that name the world: phase, task, task-spec, silent-failure, two-tier — must recur at every abstraction-level. Each occurrence is a pointer to the home-fact, not a copy of it. Hence the legitimate tuning: raise a word's weight by naming one world one word everywhere; keep the fact in one place. Reinforce the vocabulary, never copy the fact. The canonical set of these words is in [reserved-words](reserved-words.md).

## The boundary: vocabulary, not topology

Tuning the field has a boundary. The coarse edit is to write topology into a skill-description: who loads whom, "then hands off to X", the chain of skills itself. It works, but it hard-fixes the edges in the always-loaded layer, where they can no longer be overridden per task — and the edges are already declared in the body (`loads:`, the engine body), in one home. The fine edit is the field's vocabulary and its abstraction-level: the choice of term, an even abstraction-level across all skill-descriptions, retiring an obsolete word. The rule: a skill-description carries **which world and in what words** (vocabulary and abstraction-level), not **who connects to whom** (topology). Edges are the body's job.

## One vocabulary for the field

Coherence requires every thing to be named by the artifact's own word. The artifact grammar (both bodies, `roadmap-engine`, [skill-cycle](philosophy/skill-cycle.md)) is `### Phase N` (outline's product) and `N.M — task` (decompose's), and the skill-description-field names each tier by that same word: `roadmap-outline`'s skill-description calls its product "phases", `roadmap-decompose`'s calls its own "tasks". "Milestone" is retired from the vocabulary; it survives only as a user-facing trigger word (a phrase the agent maps by context, per [using-the-language](using-the-language.md)), never as the artifact's name. Naming each tier by its artifact's own word — "phase" where outline makes phases, "task" where decompose makes tasks — is a vocabulary edit, not a fact or a topology edit.

## The field is description, not leaf

The skill-description-field is loaded always — and so it is description, not leaf: compressed, lossy, not ground-truth. Acting on the field alone rounds off exactly the sharp edges: the precise wording of a gate, the renumbering rule, a scope boundary. The field sets where to look and in what words; when the edge matters, the walk to the leaf is still required ([context-tree](philosophy/context-tree.md), global CLAUDE.md § "Grounding claims"). The field and the walk complement each other — the same pair as "the map at entry" and "the leaf at the moment of action".

## Where things are normed

This is a narrative account of the **channel** — how the always-loaded layer shapes behavior; the artifact vocabulary itself (phase, task, task-spec, two-tier) is normed in the `roadmap-engine` format and in the global CLAUDE.md, from where the field draws its weight. The walkable layer of the same knowledge is in [context-tree](philosophy/context-tree.md); the shape of the graph, where the skill-description is the top, in [skill-pyramid](philosophy/skill-pyramid.md); the order in which lenses succeed one another over a roadmap, in [skill-cycle](philosophy/skill-cycle.md); the pairwise mechanism/policy rule, in [skill-composition-model](philosophy/skill-composition-model.md).
