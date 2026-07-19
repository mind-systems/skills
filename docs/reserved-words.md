# Reserved words — the shared vocabulary of the sakshi system

A project family this size needs a fixed vocabulary: one set of concepts, each with exactly one name, none named twice. This file is that vocabulary's registry — the glossary every skill, skill description, and system doc draws on; reading these words you recognize the system's one voice. What is **reserved** is the *meaning*, not the spelling: each entry binds a concept to its one name, and the name to its one concept. The terms themselves are ordinary English, written by ordinary prose rules — capitalized where a sentence capitalizes, hyphenated where English hyphenates. A term is not a token, and no text is ever swept for its typography.

It is a **contract** with a precise scope: **the product we author — skill bodies, skill descriptions, and the docs that specify the system — calls each concept by its registry name**: no synonyms, no repurposing. Working text the system produces at runtime (plans, plan-reviews, reviews) and the free prose inside individual roadmaps and specs is ordinary language — the vocabulary sharpens it, never polices it — and what the system *reads* is mapped by context, never bound: a user may type "milestone", and the agent maps it to the intended meaning, as it already does well. Where the vocabulary binds and where it is only available is its own discipline — [using-the-language](using-the-language.md); a reserved word is never banned from working text.

The rule is bidirectional: **one meaning, one word** — a concept is never named two ways — and **one word, one meaning** — a reserved word is never repurposed for another concept.

A term takes a qualifier only when the qualifier does work — resolving a collision ("spec" → "task spec" / "governing spec") or telling apart members of a family sharing a stem ("skill description" / "skill description field"). A word already unambiguous within the set stays single (leaf, map, walk, seam); length is spent only where it buys disambiguation.

**Fixed-form strings are a different axis.** Names a machine resolves — skill and directory names (`task-rescue`), file paths, frontmatter fields (`loads:`, `description:`), and the protocol tokens a program scans (`PLAN_REVIEW_PASS`, `## Deferred observations`) — are identifiers, not vocabulary: they stay byte-exact because code depends on the characters, whatever the surrounding prose does. The discipline is in [using-the-language](using-the-language.md) § "Protocol tokens are a different axis".

The registry is not a second home for meanings. It fixes the **name** of a concept — which must recur — and points to the name's one home, where the fact is defined; it indexes names, it never re-homes facts. This is the vocabulary rule applied to the vocabulary itself: reinforce the word, never copy the fact.

## Roadmap artifacts

Home — `roadmap-engine` format.

- **direction** — a `## <Name>` section grouping phases under one goal and preamble.
- **phase** — a `### Phase N` header with a prose intro; the strategic tier; produced by `roadmap-outline`.
- **task** — an `N.M` entry; atomic, one reason to revert; produced by `roadmap-decompose`.
- **contract line** — the ~600-char task line in the roadmap.
- **task spec** — one task's full specification file under `.ai-factory/specs/`, written through `note`, referenced by the contract line's tag; the implementation-tier work-order.
- **two-tier** — a contract line plus its task spec: two levels of one task.
- **governing spec** — a phase's spec, named on the phase header; the authority every reader of the phase conforms to — the meaning of what the system *must* do, written before code, code implements it. Lives in `docs/`. Home — [skill-cycle](sakshi-harness/skill-cycle.md), `aif-docs`.

## Entry maps

Home — global CLAUDE.md § "Grounding claims", [context-tree](philosophy/context-tree.md).

- **ROADMAP** — `.ai-factory/ROADMAP.md`, the project's time axis.
- **ARCHITECTURE** — `.ai-factory/ARCHITECTURE.md`: module boundaries, the chosen pattern, compacted history.
- **seam** — the `[x]`/`[ ]` boundary; where the project lives now; the entry aim.
- **stratum** — an `[x]` line is a layer of history describing the moment of its own planning; a later line on the same surface supersedes an earlier one.
- **Features** — the `## Features` section in ARCHITECTURE.md: compacted history anchored to commit hashes. Home — `roadmap-prune`, `aif-architecture`.

## Grounding

Home — global CLAUDE.md § "Grounding claims", [context-tree](philosophy/context-tree.md).

- **leaf** — the code at the end of a branch; a walk reaches ground truth only here, never at a doc.
- **ground truth** — the actual present behavior, read from code; the authority on what the system *does* — a description of it drifts, code does not (distinct from the governing spec, the authority on what the system *must* do).
- **map** — your branches one layer deep, raised at entry.
- **walk** — the descent along a branch to its leaf at the moment you act on it.
- **one home per fact** — a fact has one home; its second home is a link, never a copy.
- **decay** — raised context ages back into a description; re-read the leaf fresh before acting.

## Skill graph

Home — [skill-graph](sakshi-harness/skill-graph.md), ARCHITECTURE.md § "Composition: mechanism vs policy".

- **engine** — a mechanism skill: the shared *how*, two or more callers.
- **lens** — a top-level skill: route plus policy, a thin top over engines (a "philosophy" skill).
- **skill description** — a skill's `description:` frontmatter field; the always-loaded atom Claude reads in the skills manifest to decide when to invoke.
- **skill description field** — all skill descriptions loaded at once as one layer of the system prompt. Home — [skill-description-field](skill-description-field.md).
- **abstraction level** — how far a statement sits above the mechanism it describes; skill descriptions held at an even abstraction level are a condition of the field's coherence.
- **`loads:`** — the frontmatter edge declaration on the calling skill; the forward graph.
- **folder style** — a destination folder's settled style, read before writing into it.

## Tests

Home — `test-philosophy`.

- **silent failure** — a surface that on a wrong result keeps running and produces wrong output with no signal → test it.
- **loud failure** — fails loudly (compiler, exception, DI, 4xx/5xx) → skip the test.

## Orchestrator

Home — `orchestrator-artifacts`, [skill-cycle](sakshi-harness/skill-cycle.md).

- **orchestrator** — the CLI that executes a finished roadmap task by task; it plans nothing.
- **sidecar** — a task run's status file.
- **PASS signal** — `PLAN_REVIEW_PASS` / `REVIEW_PASS`, a stage's pass marker.
- **deferred observations** — review remarks left unresolved; unpinned ones block a prune. The heading a program scans, `## Deferred observations`, is a protocol token.
- **prune · rescue · audit** — operations: fold `[x]` tasks into Features; repair a task that did not converge to the depth of its root cause; an outside-view look at a task that looped.

## Multiuser

Home — [multiuser-roadmaps](philosophy/multiuser-roadmaps.md), `roadmap-engine` format.

- **named roadmap** — `.ai-factory/roadmaps/<slug>.md`, one developer's buffer.
- **owner line** — `> Owner: <email>`, the first line; the single writer.
- **slug** — the local-part of `git config user.email`.
- **grove** — a family of repositories under one coordinating root. Home — [context-grove](philosophy/context-grove.md).

## Paired loop

Home — `agent-architect`, `editor` (`src/agents/editor.md`).

- **architect** — the plan-and-review persona: reasons, decides, drafts work-orders; never touches shared artifacts itself.
- **editor** — the persistent subagent the architect spawns on first contact and keeps for the session; applies every change and reports back by fact.
- **relay** — a user message ending with `::`; everything before the marker is the payload, forwarded to the editor untouched.
- **channel-message** — either message that reaches the editor — a relay or an apply work-order; the first one received is the spawn.
- **work-order** — the architect's own authored, pinned instruction for a decided apply; the one editor channel besides a relay.

## Where the registry itself is normed

Names here are pointers; the facts live at their homes. The vocabulary rule the registry grows from is in [skill-description-field](skill-description-field.md) ("Weight through repetition"); one home per fact and grounding are in the global CLAUDE.md § "Grounding claims" and [context-tree](philosophy/context-tree.md).
