# Plan: 34.4 — `work-order` names one thing in the registry

## Context
`docs/reserved-words.md` states its contract in both directions — "one meaning, one word … and one word, one meaning — a reserved word is never repurposed for another concept" — and then spends `work-order` on two concepts: the task spec, called "the implementation-tier work-order" in § "Roadmap artifacts", and the artifact the architect drafts for its editor in § "Paired loop". They are different artifacts with different readers and different lifetimes. This task removes the phrase from the task-spec entry, which already names the artifact fully without it; the paired-loop entry keeps the word.

The file's first line reads `> This document is final and is not subject to update.` — and this edit is licensed anyway, because it is not an update to the registry's meanings, which that line forecloses. It removes a collision the registry's own bidirectional rule already forbids: the document is being made to obey itself. The set of terms it binds is unchanged — no term is added, retired, or given a new meaning.

Blast radius is already established and needs no re-derivation: `work-order` occurs elsewhere only in `docs/sakshi-harness/skill-cycle.md`, `docs/reference-by-name.md`, `src/agents/editor.md`, `src/skills/agent-architect/SKILL.md`, `src/skills/architect-pairing-engine/SKILL.md`, `src/skills/architect-editor-engine/SKILL.md` and `src/global/CLAUDE.md`, and every one of those hits names the paired-loop artifact — `reference-by-name.md` and `src/global/CLAUDE.md` name a work-order and a spec as separate things in the same sentence. No paraphrase of the edited entry exists anywhere: `CLAUDE.md`, the grove root `../CLAUDE.md` and `.ai-factory/ARCHITECTURE.md` name the registry file without quoting the phrase. Nothing outside `docs/reserved-words.md` moves.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

- [x] **Drop `the implementation-tier work-order` from the task spec entry**
  Files: `docs/reserved-words.md`
  In § "Roadmap artifacts", the `- **task spec** —` bullet currently reads: `one task's full specification file under `.ai-factory/specs/`, written through `note`, referenced by the contract line's tag; the implementation-tier work-order.` Remove the final clause together with the semicolon joining it, so the entry ends `… referenced by the contract line's tag.` — the sentence closes on the `Spec:`-tag clause with a period.
  Negative space, read while making the edit: the bold term, the em-dash and the two inline-code spans on that line stay byte-identical; the file is one unwrapped line per entry, so do not re-wrap or reflow. The neighbouring `contract line`, `two-tier` and `governing spec` entries are not rephrased to compensate for the removed tier. The § "Paired loop" `- **architect** —` entry keeps `drafts work-orders` — that is the one concept the word now names. No term is added, retired, or re-homed, and no other entry, section or heading in the file moves.
