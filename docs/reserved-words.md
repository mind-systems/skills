# Reserved words — the semantics of the sakshi language

A programming language has reserved words: a fixed set, each with one meaning, none reusable for anything else. The sakshi environment needs the same set. But this file is more than a word list — it is the **semantics** of the language the system is written in. These words run through every skill, skill-description, roadmap, and spec; reading them you recognize the language, the way reading Java you recognize Java.

It is a **contract**, and its scope is precise: everything the system *produces* — skills, skill-descriptions, roadmaps, specs, docs — conforms to it. What the system *reads* does not. A user may type "milestone", and the agent maps it to the intended meaning from context, as it already does well; the contract binds the system's own output, never the user's input.

**Multi-word reserved words are kebab-case.** A term of two or more words is joined with hyphens — `contract-line`, `task-spec`, `named-roadmap` — following Claude's own frontmatter fields (`allowed-tools`, `argument-hint`). A reserved word is then one visible token, and the boundary between our language and ordinary prose stays legible even inside English text, where an unjoined term would dissolve into the sentence.

A reserved word takes a qualifier only when the qualifier does work — resolving a collision (`spec` → `task-spec` / `governing-spec`) or marking a family of two or more terms sharing a stem (`skill-description` / `skill-description-field`). A word already unambiguous within the set stays single (`leaf`, `map`, `walk`, `seam`); the token is both a variable and a carrier of meaning, so length is spent only where it buys disambiguation.

The registry is not a second home for meanings. It fixes the **form** of a word — which must recur — and points to the word's one home, where the fact is defined; it indexes forms, it never re-homes facts. This is the vocabulary rule applied to the vocabulary itself: reinforce the word, never copy the fact.

The rule is bidirectional, like a language's reserved words: **one meaning, one word** — a concept is never named two ways — and **one word, one meaning** — a reserved word is never repurposed for another concept.

## Roadmap artifacts

Home — `roadmap-engine` format.

- **direction** — a `## <Name>` section grouping phases under one goal and preamble.
- **phase** — a `### Phase N` header with a prose intro; the strategic tier; produced by `roadmap-outline`.
- **task** — an `N.M` entry; atomic, one reason to revert; produced by `roadmap-decompose`.
- **contract-line** — the ~600-char task line in the roadmap.
- **task-spec** — one task's full specification file under `.ai-factory/specs/`, written through `note`, referenced by the contract-line's tag; the implementation-tier work-order.
- **two-tier** — a contract-line plus its task-spec: two levels of one task.
- **governing-spec** — a phase's spec, named on the phase header; the authority every reader of the phase conforms to — the meaning of what the system *must* do, written before code, code implements it. Lives in `docs/`. Home — [skill-cycle](philosophy/skill-cycle.md), `aif-docs`.

## Entry maps

Home — global CLAUDE.md § "Grounding claims", [context-tree](philosophy/context-tree.md).

- **ROADMAP** — `.ai-factory/ROADMAP.md`, the project's time axis.
- **ARCHITECTURE** — `.ai-factory/ARCHITECTURE.md`: module boundaries, the chosen pattern, compacted history.
- **seam** — the `[x]`/`[ ]` boundary; where the project lives now; the entry aim.
- **stratum** — an `[x]` line is a layer of history describing the moment of its own planning; a later line on the same surface supersedes an earlier one.
- **Features** — the `## Features` section in ARCHITECTURE.md: compacted history anchored to commit hashes. Home — `roadmap-prune`, `aif-architecture`.

## Grounding

Home — global CLAUDE.md § "Grounding claims", [context-tree](philosophy/context-tree.md).

- **leaf** — the code at the end of a branch; a walk reaches ground-truth only here, never at a doc.
- **ground-truth** — the actual present behavior, read from code; the authority on what the system *does* — a description of it drifts, code does not (distinct from the governing-spec, the authority on what the system *must* do).
- **map** — your branches one layer deep, raised at entry.
- **walk** — the descent along a branch to its leaf at the moment you act on it.
- **one-home-per-fact** — a fact has one home; its second home is a link, never a copy.
- **decay** — raised context ages back into a description; re-read the leaf fresh before acting.

## Skill graph

Home — [skill-composition-model](philosophy/skill-composition-model.md), [skill-pyramid](philosophy/skill-pyramid.md), ARCHITECTURE.md § "Composition: mechanism vs policy".

- **engine** — a mechanism skill: the shared *how*, two or more callers.
- **lens** — a top-level skill: route plus policy, a thin top over engines (a "philosophy" skill).
- **skill-description** — a skill's `description:` frontmatter field; the always-loaded atom Claude reads in the skills manifest to decide when to invoke.
- **skill-description-field** — all skill-descriptions loaded at once as one layer of the system prompt. Home — [skill-description-field](skill-description-field.md).
- **abstraction-level** — how far a statement sits above the mechanism it describes; skill-descriptions held at an even abstraction-level is a condition of the skill-description-field's coherence.
- **`loads:`** — the frontmatter edge declaration on the calling skill; the forward graph.
- **folder-style** — a destination folder's settled style, read before writing into it.

## Tests

Home — `test-philosophy`.

- **silent-failure** — a surface that on a wrong result keeps running and produces wrong output with no signal → test it.
- **loud-failure** — fails loudly (compiler, exception, DI, 4xx/5xx) → skip the test.

## Orchestrator

Home — `orchestrator-artifacts`, [skill-cycle](philosophy/skill-cycle.md).

- **orchestrator** — the CLI that executes a finished roadmap task by task; it plans nothing.
- **sidecar** — a task run's status file.
- **PASS-signal** — `PLAN_REVIEW_PASS` / `REVIEW_PASS`, a stage's pass marker.
- **deferred-observations** — review remarks left unresolved; unpinned ones block a prune.
- **prune · rescue · audit** — operations: fold `[x]` tasks into Features; repair a task that did not converge to the depth of its root cause; an outside-view look at a task that looped.

## Multiuser

Home — [multiuser-roadmaps](philosophy/multiuser-roadmaps.md), `roadmap-engine` format.

- **named-roadmap** — `.ai-factory/roadmaps/<slug>.md`, one developer's buffer.
- **owner-line** — `> Owner: <email>`, the first line; the single writer.
- **slug** — the local-part of `git config user.email`.
- **grove** — a family of repositories under one coordinating root. Home — [context-grove](philosophy/context-grove.md).

## Where the registry itself is normed

Forms here are pointers; the facts live at their homes. The vocabulary rule the registry grows from is in [skill-description-field](skill-description-field.md) ("Weight through repetition"); one-home-per-fact and grounding are in the global CLAUDE.md § "Grounding claims" and [context-tree](philosophy/context-tree.md).
