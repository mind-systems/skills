# 53.1 — three skill sentences agree with the shape they describe

## What is true now

Three files carry a sentence that describes a shape the family has since moved from. The text of each is wrapped in its file at a fixed column.

`src/skills/roadmap-decompose/SKILL.md`, hook "(d) Extra update action — "Decompose existing"", reads: "Register an added update-menu action: expand a vague task into a full spec (what exists today, the exact change, files/types/methods to touch, guards, how to verify)." `roadmap-engine`'s "What a task spec holds" excludes a clause that is "a check that the instruction was carried out".

`src/commands/command-pin-gaps.md` has two sentences. In "**The shape it repairs toward:**", the closing clause of its second sentence reads: "…and a blast-radius hole by enumerating *what breaks on contact*." "**What the pass never writes:**" opens: "it pins values and enumerates breakage, and it never authors a verification check". The same file's Blast-radius repair is "the **rule** … the literal `Grep`/`rg` **sweep** … and the **invariant** — a recorded finding of what the sweep, run now, reaches … never the sweep's own enumeration of what it found".

`src/skills/roadmap-decompose-skeleton/SKILL.md` § "Load-once / dependencies" lists two loaded skills: "- `roadmap-engine` — the shared two-tier artifact format (contract line + task spec) that every lens renders its output through." and "- `test-philosophy` — the silent-failure discriminator the TDD lens applies to decide what gets a test." Its `loads:` field and Lens 1 name `polymorphism-philosophy` as well. The section's "only the three lenses below" agrees with § "Step 1: Apply the three lenses", which holds Lens 1, Lens 2 and Lens 3.

## What must be true after

The hook's sentence reads: "Register an added update-menu action: expand a vague task into a full spec (what exists today, the exact change, files/types/methods to touch, guards)."

In `command-pin-gaps`, the closing clause reads: "…and a blast-radius hole by recording *what breaks on contact*." The opening of the other sentence reads: "it pins values and records breakage, and it never authors a verification check".

The skeleton's list gains a third bullet after `test-philosophy`: "- `polymorphism-philosophy` — the question Lens 1 puts to each task: to add a third kind, how many places must change, fired only when a kind gains its second member."

## What breaks on contact

**Rule:** a text breaks on this change if it quotes one of these sentences, or states the shape they describe.

**Sweep:**
```
grep -rn "how to verify" src/ docs/ CLAUDE.md
grep -rn -i "enumerat" src/ docs/ CLAUDE.md
grep -rn "Decompose existing\|Load-once" src/ docs/ CLAUDE.md
```

**Finding.** The first search reaches the hook's sentence, the task's target, and `docs/what-a-task-carries.md`, whose "a spec that also says how to verify hands the implementer a job" is prose about the shape the hook now stops asking for, and agrees with the change. The second reaches the two `command-pin-gaps` sentences, the task's targets, the same file's Blast-radius repair, whose "never the sweep's own enumeration of what it found" stays and agrees with the new wording, and unrelated uses of the word in `roadmap-prune`, the global `CLAUDE.md` and the `CLAUDE.md` index. The cycle doc's account of the blast-radius class already reads "правилом, что задаёт затронутое множество, поиском, который его находит, и записью того, что поиск достигает сейчас", which the new clause matches. The third reaches the hook's name in `roadmap-decompose`, where the engine's flow cites "Decompose existing" without quoting its parenthesis, and the two skills' own "Load-once / dependencies" sections, each describing its own loads. No other text quotes the three sentences. The skeleton's count word holds and its parenthesis is a gloss, so neither is edited. "Guards" stays in the hook's parenthesis by the user's word.
