# "Supersedes the last by name" gets an operational referent

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md` states: "Each new snapshot supersedes the last by name, so a reader never follows a stale next action." The file never says where a memory snapshot lands, what it is named, or what makes one supersede another — "by name" has nothing in the file to resolve against. A reader cannot tell whether a newer snapshot is picked out by a filename convention, replaces the one before it under an identical name, or is told apart some other way.

Practice already has an answer the skill never states, and `note` — which `command-handoff.md` delegates a memory snapshot's numbering to — states it directly, in its own folder-style step: "'Most recent (highest-numbered)' is decided over the parsed integer, not the string — the 1–2 siblings with the numerically highest prefixes, so a name with a longer prefix outranks any shorter-prefixed one." The numerically highest-numbered sibling is the most recent one — the fact `agent-architect`'s own sentence needs and does not state. The sentence reads this way because 38.1 made the comparison numeric rather than lexicographic; the grounding holds precisely because that task landed first.

## The change

The sentence gains the comparison rule alone: the numerically higher-numbered snapshot is the current one. Nothing about how that number is produced, where the file lands, or whether an old one is overwritten rides with it — those are `note`'s and `command-handoff`'s own facts, stated at their own home and quoted above only to ground this one clause.

The rest of the sentence and its reason — "so a reader never follows a stale next action" — is untouched; only the missing referent is added, and it is added as narrowly as the file can state it: a comparison rule, not an account of the mechanism behind it.

## Blast radius

This task edits a sentence in § "Spawn once, message thereafter," the paragraph naming the two occasions for a memory snapshot; it does not touch `command-handoff.md` or `note`, and restates neither's mechanics nor the bound 38.1 installed — it points at the one fact `agent-architect`'s own sentence needs, the comparison rule quoted above from `note`'s own folder-style step, without repeating either file's own rules for how that numbering or that destination is chosen.

`editor.md`, `architect-editor-engine`, and `docs/paired-loop.md` are not touched: the governing spec already states a memory snapshot "carries a pointer to the buffer's place, never a copy of what the buffer holds" without naming where the snapshot itself lives, and this task does not change that — it grounds only the skill's own sentence, which is where the ungrounded claim sits.
