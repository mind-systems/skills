# 69.1 — the session probe prints its nonce in one command and searches for it in the next

## What is true now

`src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter", in the paragraph that opens "On every start and every rehydration", reads: "Read your session id by running a command that prints a random nonce, then searching the project's transcripts — the `.jsonl` files directly under `~/.claude/projects/<project-key>/`, `<project-key>` being the working directory's path with every character that is not a letter or a digit replaced by a hyphen — for the printed nonce: exactly one file matches, and its name without `.jsonl` is your session id." The next sentence reads: "When the probe does not yield exactly one file, write no session id and carry on: leave `address.md` as it was, or unwritten at a founding, and mention in passing that you could not read your session id; never ask, never stop, never pick one file and never guess." The text wraps in the file at a fixed column.

A single command that both prints the nonce and searches for it finds nothing, because its output is not in the transcript until the command returns. The founding passage of the same section says "No folder found, for whatever reason, means you are a new head — you never ask the user which", so a resumed head that combines the two steps founds a second folder and leaves its whole memory in the first.

## What must be true after

The first of the two sentences reads: "Read your session id in two commands: the first prints a random nonce and ends, since its output reaches the transcript only when it returns; the next searches the project's transcripts — the `.jsonl` files directly under `~/.claude/projects/<project-key>/`, `<project-key>` being the working directory's path with every character that is not a letter or a digit replaced by a hyphen — for the printed nonce: exactly one file matches, and its name without `.jsonl` is your session id."

## What breaks on contact

**Rule:** a text breaks on this change if it states how the head reads its session id, or reads the probe's sentence.

**Sweep:**
```
grep -rn -i "nonce" src/ docs/ CLAUDE.md
grep -rn "session id" src/ docs/ CLAUDE.md
grep -rn "address.md" src/ docs/ CLAUDE.md
```

**Finding.** The word "nonce" occurs only in the probe's sentence, the task's own target; no other skill, command or doc describes the mechanism. The founding passage points at the probe as "the probe this section describes", so it reads the new sentence unchanged. The second sentence, the zero-match policy, keeps its words, and the two-command rule does not touch it: a probe that yields no single file still writes no id, never asks and never stops. `docs/paired-loop.md` § "Where the memory lives" says the head "reads its own session id" and finds the folder that holds it, without naming a mechanism, so it does not contradict the new text. The `CLAUDE.md` rows for the paired loop and the pipeline design speak of the session id and `address.md` and state no mechanism. The seed holds no probe, and `architect-editor-engine` defines `address.md` and its two lines and says nothing of how the id is read. Nothing in `docs/future/` states the probe. No other text states or contradicts it, so none needs aligning.
