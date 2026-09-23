# 56.2 — the task-spec-shape root stops feeding the census instruction downstream

## Current state

`src/skills/roadmap-engine/SKILL.md`'s **"What a task spec holds"** paragraph reads in full:

> **What a task spec holds:** three parts and nothing else — *what is true now*, read from the code with exact values, so the implementer does not re-derive it; *what must be true after*, in the code's own terms: which file, which text, which value; and *what breaks on contact*, enumerated rather than hedged.

`src/commands/command-pin-gaps.md` names and quotes this exact paragraph, by its heading text, as the source its own Blast-radius holes clause's shape derives from and does not restate: *"defined in `roadmap-engine`'s 'What a task spec holds' paragraph and not restated here."* The paragraph's third clause — "enumerated rather than hedged" — is the wording that clause's own `Repair:` sentence concretized into a census, per this phase's note.

Checked directly: `grep -l "roadmap-engine" src/skills/*/SKILL.md src/commands/*.md` returns nine files — the engine itself plus eight callers (`roadmap-decompose-skeleton`, `roadmap-decompose`, `roadmap-outline-deep`, `roadmap-outline`, `roadmap-test-coverage`, `task-rescue`, `temporal-tree`, `command-pin-gaps`). Of these, only `command-pin-gaps.md` names this paragraph by its heading text; the other seven reference `roadmap-engine`'s format generally, without naming this specific paragraph, though any of them that renders a task spec inherits its shape by construction.

## The change

The paragraph's third clause becomes:

> **What a task spec holds:** three parts and nothing else — *what is true now*, read from the code with exact values, so the implementer does not re-derive it; *what must be true after*, in the code's own terms: which file, which text, which value; and *what breaks on contact*, pinned rather than hedged.

The opposition the sentence does its work with — pinned/stated-precisely versus hedged — survives unchanged; only the word that had been read as an instruction to write a list is replaced with the verb this family already uses elsewhere for stating a fact precisely without implying a tally (`command-pin-gaps`'s own Value holes clause: "pin the **exact** value").

Untouched, verbatim: the paragraph's first two clauses ("what is true now," "what must be true after"); the paragraph's own bold heading text, `**What a task spec holds:**`, byte-identical — eight callers reach this engine and `command-pin-gaps` cites this heading by name, and the name must still resolve; the "Why two tiers" paragraph immediately above; the "Never write a full spec inline in the roadmap" sentence immediately below; every other section of the file.

## Blast radius

**Rule:** any file that names this paragraph by its exact heading text depends on that name resolving to a real heading; any file that quotes the paragraph's third clause's exact wording ("enumerated rather than hedged") as current ground truth reads stale once the wording changes.

**Sweep (re-runnable):**
```
grep -rln "What a task spec holds\|enumerated rather than hedged" src/ docs/ .ai-factory/
```

**Invariant:** after the change, every result naming the paragraph by heading still resolves — the heading text is byte-identical, confirmed by this task's own guard above. Every result quoting "enumerated rather than hedged" verbatim falls into one of four categories, none a collision: this task's own target (`roadmap-engine/SKILL.md`, now carrying the new wording, so it drops out of this half of the sweep); this task's own spec and the roadmap's own contract line for it, both of which quote the old wording permanently as the problem they describe, exactly as `## Current state` quotes it above and exactly as any closed task's artifacts do; a phase note whose own subject is this exact divergence (this phase's own note, `150-…`, which documents what the paragraph used to say and is not invalidated by the paragraph now saying something else — a phase note describes a moment, not a standing claim about the present); or a handoff (`27-…`, a different genre from a phase note — read once, at the point it is mined for context, never re-read unconditionally the way a phase note is).
