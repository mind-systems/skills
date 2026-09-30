# 66.3 — the drain names its second destination

## What is true now

`src/skills/architect-editor-engine/SKILL.md` § "The architect's buffer" has a drain paragraph: "A ruling recorded in the buffer is a debt against the skill, not a record of one. It leaves the buffer when it reaches the artifact that should hold it; without that drain the buffer accumulates decisions everyone follows and no artifact states." It names one destination, and the section says nothing of a threshold at which something becomes a debt.

The engine's frontmatter description carries the same form in one clause: "the drain rule that a ruling leaves the buffer once it reaches the artifact that should hold it,". The description has a limit of 1024 code points.

`docs/paired-loop.md` § "Where the pair's behaviour lives" gives the drain two destinations: a ruling about the project or its skills drains to the artifact that should hold it and leaves the buffer, and the base behaviour of the pair drains to the seed and stays in the buffer as its standing entry. It also says that something the user had to say twice, or that failed twice, is a debt to drain, and said once it is not.

## What must be true after

The drain paragraph reads:

> A ruling recorded in the buffer is a debt against the skill, not a record of one, and it drains to one of two places. A ruling about the project or its skills leaves the buffer when it reaches the artifact that should hold it; without that drain the buffer accumulates decisions everyone follows and no artifact states. The base behaviour of the pair drains to the seed the buffer is founded from and stays in the buffer as its standing entry, which both halves re-read all session. Something the user had to say twice, or that failed twice, is a debt to drain; said once, it is not.

The frontmatter clause "the drain rule that a ruling leaves the buffer once it reaches the artifact that should hold it," reads "the drain rule — a project or skill ruling leaves the buffer once it reaches the artifact that should hold it, the pair's base behaviour goes to the seed and stays as a standing entry, and what was said or failed twice is a debt to drain —", and the description stays within the 1024-code-point limit.

## What breaks on contact

**Rule:** a text breaks on this change if it states the drain with one destination, or depends on the drain paragraph's wording.

**Sweep:**
```
grep -rn -i "drain" src/ docs/ CLAUDE.md
```

**Finding.** The search reaches the engine's paragraph and description, the task's own target; the sentence in `agent-architect` § "Your buffer is shared; you alone write it" that names the drain rule among what is `architect-editor-engine`'s and restates none of it, which stays true; a passage of `roadmap-decompose-skeleton` on draining a heap in code, which shares the word and not the subject; and `docs/paired-loop.md`, whose section states the two destinations and the threshold and agrees with the new paragraph. `editor.md` names no drain rule and carries the buffer only as what the editor holds whole, so the hand learns the two destinations by loading the engine, as it loads it at spawn. Nothing else in `src/`, `docs/` or `CLAUDE.md` states where a ruling goes.
