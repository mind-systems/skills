# Plan: 69.1 — the session probe prints its nonce in one command and searches for it in the next

## Context
In `src/skills/agent-architect/SKILL.md` § "Spawn once, message thereafter", the paragraph that opens "On every start and every rehydration" describes the session probe. Its sentence will name two separate commands: the first prints the nonce and ends, and the next searches the transcripts for it. One command that does both finds nothing, because its output reaches the transcript only when the command returns. The replacement sentence is pinned verbatim in the task spec `.ai-factory/specs/trickster77777/0201-the-session-probe-prints-its-nonce-in-one-command-and-searches-in-the-next.md` § "What must be true after". Copy it exactly.

Blast radius, from the spec's sweep (re-run while planning, same result): `nonce` matches only the two lines of the probe's sentence in `src/skills/agent-architect/SKILL.md`. Per the spec, these stay unchanged:
- the founding passage, which points at "the probe this section describes";
- the zero-match sentence ("When the probe does not yield exactly one file, …");
- `docs/paired-loop.md`, the `CLAUDE.md` rows, the seed, `architect-editor-engine` and `docs/future/`.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit the skill

- [x] **Replace the probe's sentence**
  Files: `src/skills/agent-architect/SKILL.md`
  In § "Spawn once, message thereafter", the paragraph opening "On every start and every rehydration, new head or resumed, `address.md` is made true again." contains a sentence that currently runs across the wrapped lines as:
  "Read your session id by running a command that prints a random nonce, then searching the project's transcripts — the `.jsonl` files directly under `~/.claude/projects/<project-key>/`, `<project-key>` being the working directory's path with every character that is not a letter or a digit replaced by a hyphen — for the printed nonce: exactly one file matches, and its name without `.jsonl` is your session id."
  Replace it with this text, verbatim:
  "Read your session id in two commands: the first prints a random nonce and ends, since its output reaches the transcript only when it returns; the next searches the project's transcripts — the `.jsonl` files directly under `~/.claude/projects/<project-key>/`, `<project-key>` being the working directory's path with every character that is not a letter or a digit replaced by a hyphen — for the printed nonce: exactly one file matches, and its name without `.jsonl` is your session id."
  These stay unchanged, word for word:
  - the paragraph's opening sentence;
  - the following sentence "When the probe does not yield exactly one file, write no session id and carry on: … never ask, never stop, never pick one file and never guess.";
  - the session-name sentences and the `address.md` write sentence after it.
  Re-wrap the paragraph at the file's existing column (lines of at most about 72 characters, as in the surrounding text). Only the lines the edit touches may change. Keep the em dashes (—) and backticks as they are in the file.
  Afterwards, run these checks. The search runs on the source, so a match that a line break splits must be checked by reading the paragraph.
  - `grep -rn "by running a" src/skills/agent-architect/SKILL.md` must return nothing.
  - `grep -n "in two commands" src/skills/agent-architect/SKILL.md` must return the edited paragraph.
  - `grep -rn -i "nonce" src/ docs/ CLAUDE.md` must match only this paragraph.
