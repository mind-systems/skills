# 61.2 — the three parts are the whole, and none is a check or a line

## What is true now

`src/skills/roadmap-engine/SKILL.md`'s **What a task spec holds** paragraph reads in full:

> **What a task spec holds:** three parts and nothing else — *what is true now*, read from the code with exact values, so the implementer does not re-derive it; *what must be true after*, in the code's own terms: which file, which text, which value; and *what breaks on contact*, pinned rather than hedged.

"Three parts and nothing else" states that the list is exhaustive but never states what a fourth part would be — so a fourth part can arrive without ever contradicting the letter. It already has: `.ai-factory/notes/07-architect-buffer.md`'s finding names two such arrivals, both recorded there as debts against no artifact for weeks and stated nowhere under `docs/` or `src/` (checked directly, zero hits — phase 61's own note carries the sweep). The first is a checking instruction — `command-pin-gaps.md`'s Blast-radius holes Repair sentence ordered its invariant as "every match must satisfy after the change," an instruction to a later run — whose cost is measured: task 58.2's rescue plan carried four verification tasks against two edit tasks, every one of three failed rounds landing inside the verification half, the change itself never faulted (task 61.1 repairs this occurrence). The second is a position: the user's own ruling that a spec explains what an artifact must hold, never where in the file to type it.

`src/commands/command-pin-gaps.md` names and quotes this paragraph by its heading text, as the source its own hole classes derive from and do not restate: *"defined in `roadmap-engine`'s 'What a task spec holds' paragraph and not restated here."* Checked directly: `grep -l "roadmap-engine" src/skills/*/SKILL.md src/commands/*.md` finds the engine itself and many callers reaching this paragraph for the task-spec shape, `command-pin-gaps` among them by name — the only one that names the heading directly, the rest inheriting the shape by construction.

## What must be true after

The paragraph gains one sentence, appended after its current text:

> **What a task spec holds:** three parts and nothing else — *what is true now*, read from the code with exact values, so the implementer does not re-derive it; *what must be true after*, in the code's own terms: which file, which text, which value; and *what breaks on contact*, pinned rather than hedged. Nothing else means, concretely: no clause is a check that the instruction was carried out — that belongs to the review the orchestrator already runs — and no clause is a position in the file; each states what the artifact must hold, never where to write it.

Untouched, byte-identical: the paragraph's own bold heading text, `**What a task spec holds:**` — many callers reach this engine and `command-pin-gaps` cites this heading by name, and the name must still resolve; the existing three clauses ("what is true now," "what must be true after," "what breaks on contact, pinned rather than hedged"); the "Why two tiers" paragraph immediately above; the "Never write a full spec inline in the roadmap" sentence immediately below; every other section of the file, including frontmatter and the `loads:`/reverse-graph lines.

## What breaks on contact

**Rule:** any file that names this paragraph by its exact heading text depends on that name resolving to a real heading; any file that quotes or paraphrases the paragraph's current full wording — "three parts and nothing else" with no stated exclusion — as live ground truth for what a spec may contain reads stale once the added sentence lands.

**Sweep (re-runnable):**
```
grep -rln "What a task spec holds" src/ docs/ .ai-factory/
```

**Finding.** The sweep separates into two kinds. The live kind is what this task carries: the target paragraph, and `command-pin-gaps.md`, citing it by heading name only, never its body, so its citation resolves unchanged once the heading stays byte-identical, confirmed by this task's own guard above. Everything else is the other kind, one category: artifacts recording a past moment rather than tracking the code going forward — a closed task's spec, its plan, its plan-reviews and reviews, a phase note, a handoff, and the roadmap's own contract line quoting the paragraph as the history of an edit already landed. This task's own spec and the roadmap's own contract line for it join that same historical kind once written, quoting the pre-task wording permanently as the problem they describe.

**On sequencing against 61.1.** This task edits `src/skills/roadmap-engine/SKILL.md`; task 61.1 edits `src/commands/command-pin-gaps.md` and a phase note. The two share no file, no sentence, and no citation — 61.2 does not quote or depend on command-pin-gaps.md's Repair sentence, and 61.1 does not quote or depend on this paragraph's wording. Neither task's `## What is true now` cites the other's target as ground truth. There is no ordering dependency between them in either direction; they may land in either order, or in parallel.
