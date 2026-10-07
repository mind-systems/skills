# 77.5 — the seed's counts entry holds a count in a work-order to the rule

## What is true now

`src/skills/agent-architect/templates/buffer-seed.md`, the entry "**Standing entry — the counts rule.**", reads: "It governs what is read later by someone who cannot ask back — a spec, a plan, a roadmap line, this buffer after a compact; in conversation a number or a position is fine, since a wrong one costs one reply." A work-order is a message the architect sends and is thrown away once applied, so by that wording it sits on the permitted side; the spec is composed from it, and a count in an order reaches the spec.

The entry is refreshed into every buffer from the seed's text: at each rehydration a head takes the seed's text where its own differs, matched by the bold lead-in.

## What must be true after

The entry's first sentence and the sentence after it read:

"It governs what is read later by someone who cannot ask back — a spec, a plan, a roadmap line, this buffer after a compact; in conversation a number or a position is fine, since a wrong one costs one reply. A count in a work-order is held to the same rule: the spec is composed from the order, and a count in it becomes a count in the spec."

The rest of the entry, from "A number someone decided is written:", is unchanged.

## What breaks on contact

**Rule:** a text breaks on this change if it carries the counts rule as permitting a number in a work-order, or restates the "in conversation" clause.

**Sweep:**
```
grep -rn "in conversation a number" . --include="*.md" --exclude-dir=.git
grep -rln "counts rule" src docs --include="*.md"
```

**Finding.** The first search reaches the seed, the target; the buffers of existing heads, which hold a copy of the entry and take the seed's text at their next rehydration; and the phase note for this phase, which quotes the clause. The second reaches only the seed. No skill or doc restates the "in conversation" clause.
