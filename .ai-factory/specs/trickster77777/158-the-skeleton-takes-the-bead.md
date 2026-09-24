# 57.3 — the skeleton takes the bead

## Current state

`src/skills/roadmap-decompose-skeleton/SKILL.md`'s Lens 1 reads in full:

> **Lens 1 — Skeleton (primary).** Scan the target task(s) for a shared type/interface surface — shared between 2+ tasks, or a single task whose shape is non-obvious — where an interface / abstract-class skeleton genuinely makes the surface testable. Where appropriate, extract a **skeleton task**: interfaces, types, abstract classes only — **no implementation bodies**. This is the scaffold the TDD lens writes tests against.
> - Restraint: contracts/protos are usually laid first anyway — do not blanket-cover tasks with abstract classes. Only extract a skeleton where it makes a shared or non-obvious surface testable.

Its own `loads:` line, in frontmatter, reads:

```
loads: roadmap-engine test-philosophy
```

Per this phase's note (`151-…`), Lens 1's justification today is testability — the seam is cut because the result becomes testable — while the polymorphism unit's own question — does a third kind cost more than the one place obliged to change? — is a different reason entirely. Checked directly: no other section of this file (Lens 2 — TDD, Lens 3 — Concurrency, Step 2 — Order and fuse, Step 3 — Deliverability, Step 4 — Render, or the "Critical Rules / What NOT to do" list) names or depends on Lens 1's testability wording; the restraint clause immediately below Lens 1 is the only text in the file adjacent to it.

## The change

Lens 1 becomes:

> **Lens 1 — Skeleton (primary).** Load `polymorphism-philosophy` once via the `Skill` tool, then apply its question to the target task(s). Where it fires, extract a **skeleton task**: interfaces, types, abstract classes only — **no implementation bodies**. This is the scaffold the TDD lens writes tests against.
> - Restraint: contracts/protos are usually laid first anyway — do not blanket-cover tasks with abstract classes. The question is the gate; it fires only on the event, never on style.

Lens 1 does not restate the question's own wording, on the same ground this file already states for `test-philosophy` in Critical Rule 2 and already follows in Lens 2 ("apply its silent-failure discriminator to that surface" — never a copy of the discriminator itself): the loaded skill stays in control of its own content, and a copy here would be a second, driftable home for a fact `polymorphism-philosophy` alone should hold. This is also why Lens 1 leans on nothing about the unwritten file beyond its name — the question's text lives only in `polymorphism-philosophy`'s own body (task 57.2), never duplicated into this one.

The `loads:` line becomes:

```
loads: roadmap-engine test-philosophy polymorphism-philosophy
```

Sequenced last of the three tasks in this phase: it names a skill (`polymorphism-philosophy`) that does not exist until task 57.2 lands, so it cannot be decomposed or implemented before that file exists.

Untouched, verbatim: Lens 2 (TDD) and Lens 3 (Concurrency) in full, including their own restraint clauses; the "Load-once / dependencies" section's prose about `roadmap-engine` and `test-philosophy`, which stays accurate and gains no restatement of the third dependency there — the `loads:` field is the one place a new engine dependency is declared, per this family's own graph discipline; Step 2 through Step 4; the "Critical Rules / What NOT to do" list, including its restraint items 5 and 6 against blanket-covering with abstract classes and against splitting simple tasks — the note gives no reason to move or restate either, and neither is this task's subject.

## Blast radius

**Rule:** any file quoting Lens 1's current testability wording verbatim, as ground truth for its own argument, reads stale once the wording changes; any file naming this skill's `loads:` field by its current content does the same.

**Sweep (re-runnable):**
```
grep -rln "genuinely makes the surface testable\|loads: roadmap-engine test-philosophy$" .
```

**Invariant:** after the change, `roadmap-decompose-skeleton/SKILL.md`'s Lens 1 reads the new wording in full — it says neither "genuinely makes the surface testable" nor carries a `loads:` line ending in `test-philosophy`; it loads `polymorphism-philosophy` via the `Skill` tool and applies its question, and its `loads:` line now ends in `polymorphism-philosophy`. Any file the sweep still returns beyond this one falls under the rule's own exceptions — this task's own spec (which quotes the old wording permanently as the problem it describes, exactly as `## Current state` does above) and this phase's own note (`151-…md`, which documents the pre-task state and is not invalidated by the file now saying something else — a phase note describes a moment, not a standing claim about the present). No other file in the repository quotes either passage, before or after this task. The sweep locates candidates; reading decides.
