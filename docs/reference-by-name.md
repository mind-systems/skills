# reference-by-name — naming must go as deep as reference

A reference addresses a thing either by its **name** or by its **position**. A name survives everything that happens around it; a position survives nothing. Code gets the first for free — the language guarantees that a symbol resolves, and refuses to compile when it does not. Prose gets nothing: a document's only guaranteed handles are its path and its headings, so every meaning finer than a heading can be addressed only by counting lines. Nothing checks such a reference, and nothing reports it when it rots.

## What a position address costs, measured

Across `tradeoxy_core`'s planning artifacts, 203 line-addresses point into TypeScript sources. **149 of them land inside a named declaration** — the name was there and went unused. One method collects four separate addresses: `alert-engine.service.ts` at `:28`, `:29`, `:32` and `:36`, all inside `process`, where `AlertEngineService.process` would have named all four and outlived every edit between them.

Path rot compounds it. Splitting a document into a folder leaves every reference to the old path dangling — `tradeoxy_core`'s roadmap still names `docs/design/backtest-replay.md`, whose content now lives in `docs/backtest-replay/01-model.md` and its siblings. Crossing a repository boundary silently does the same: `tradeoxy_broker` is a Swift project with no `src/` at all, and eleven of its artifacts' targets are core's files written as though core were the current repository.

## Granularity, not size

A document is not hard to reference because it is long. It is hard to reference when **the level at which it is named is coarser than the level at which it is used**. `note` carries a heading roughly every nine lines and is still addressed by line, because what a caller needs is one hook out of three, and the three are unnamed bullets under a named heading. `command-pin-gaps` carries no headings at all, and its three finding classes are cited by name everywhere, because each opens with a bold lead-in that names it.

So the unit of naming is not the section. It is **anything that will be depended on** — a heading, a bold lead-in, a numbered item, a named clause.

## In code the names already exist

Nothing has to be added there. A symbol is an address the compiler maintains: it survives reordering, insertion, and moving between files. Citing `:41` where `watcher.mappers.ts` already declares the function is choosing the fragile handle over the guaranteed one, for no gain beyond a second saved while writing.

## What follows for writing

Split a document where its **reason to change** differs, never where it merely grows long — the same rule that separates modules. Give a name to what will be depended on, and only to that: a heading over every paragraph is the documentation equivalent of an interface with trivial methods, and buys the same nothing. Where a reference crosses a repository boundary, the path names the repository and resolves from the family root; a bare path silently means "this repository" to every reader and every tool.

## The check

**A `file:line` reference is a defect report against its target.** It says: the thing I needed had no name. The repair belongs in the target — a name added, or an existing name used — never in the reference. Position addresses belong in a work-order, which is thrown away when it is applied; they never enter a spec, a roadmap line, or a document, all of which outlive the line numbering they were written against.

A second form of the same defect carries no marker that invites suspicion. A definite article or a demonstrative standing where a name belongs — "the engine", "that engine", "the same section", "the file above" — resolves by proximity to whatever was named last, and proximity is position wearing ordinary grammar. It survives exactly as long as its neighbouring sentence does, and nothing reports it when that neighbour is rewritten. It escapes notice where a `file:line` does not: a `file:line` looks like an address and invites the question of whether it still resolves; an article reads as ordinary English and invites no question at all. That is the whole of its danger.

The test that separates the two forms: ask whether the reference would still resolve if the sentence beside it were replaced. A name survives that question undisturbed; an article survives neither that question nor a move. Replacing a single clause in one roadmap line left two such references pointing at nothing in the same stroke, because the replaced clause held the only naming of the thing both reached for — the first was caught reading the line whole, the second only on a second reading of the same line.

## Where things are normed

The walked layer this discipline serves is [context-tree](philosophy/context-tree.md); the always-loaded layer that sets its direction is [always-loaded-discipline](always-loaded-discipline.md), and the one-home-per-fact rule it rests on is normed in the global CLAUDE.md § "Grounding claims". The composition rule that decides when a named thing becomes a file of its own is `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy".
