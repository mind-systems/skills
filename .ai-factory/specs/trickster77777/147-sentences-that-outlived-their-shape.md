# Phase 53 — the skill bodies stop describing retired shapes

**Touches:** 2

Three sentences in three files outlived the shape they describe, and share that cause.

- **`roadmap-decompose`, hook (d), "Decompose existing".** It registers an action to "expand a vague task into a full spec (what exists today, the exact change, files/types/methods to touch, guards, how to verify)". `roadmap-engine`'s bold lead-in "What a task spec holds" says a task spec holds what is true now, what must be true after and what breaks on contact, and nothing else, with no clause that is "a check that the instruction was carried out". "How to verify" is that check, in the one mode dedicated to writing a task spec. "Guards" stays by the user's word: he wants to keep watching tasks with guards, and the contract-line rule in `roadmap-engine` itself allows "guard conditions … only for real pitfalls".
- **`command-pin-gaps`, two sentences.** The bold lead-in "The shape it repairs toward" ends "and a blast-radius hole by enumerating *what breaks on contact*", and the bold lead-in "What the pass never writes" opens "it pins values and enumerates breakage". The file's own Blast-radius holes repair asks for the rule, the sweep and "a recorded finding of what the sweep, run now, reaches", "never the sweep's own enumeration of what it found". The two sentences describe the pass's output as an enumeration, which the file's own repair forbids, and derive their wording from the root `roadmap-engine` moved to "pinned rather than hedged".
- **`roadmap-decompose-skeleton`, § "Load-once / dependencies".** It lists the engines the skill loads once per chat, `roadmap-engine` and `test-philosophy`, while its `loads:` field reads `roadmap-engine test-philosophy polymorphism-philosophy` and Lens 1 loads `polymorphism-philosophy` through the `Skill` tool. The list of members reads as the member set and omits one. The section's count word holds: "only the three lenses below" agrees with § "Step 1: Apply the three lenses", Lens 1 Skeleton, Lens 2 TDD and Lens 3 Concurrency. Its parenthesis after that, "(targeting, skeleton, TDD, concurrency, ordering/fusion, restraint)", names more than the three lenses, and is a gloss and not a count.

No document governs these; a skill is its own documentation, and none is written.

What leaves the phase, as cosmetic with no field failure: the link-grant paraphrase in `roadmap-outline-deep`, the one-sided coupling between `roadmap-prune` and `roadmap-outline`, `editor.md`'s "relayed" register, and the engine description's omission of the ride-alongside bound.
