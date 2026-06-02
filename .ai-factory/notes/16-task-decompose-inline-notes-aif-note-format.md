# Task Spec — roadmap-decompose: ensure aif-note is loaded once, then write spec notes manually

**Date:** 2026-06-02
**Roadmap:** ROADMAP.md Milestones
**Provenance:** user. Commit `0bfa177` (note 13 task) over-engineered the aif-note step; this replaces it with one simple rule.

## Current state

Commit `0bfa177` ("roadmap-decompose: always emit two-tier output by invoking aif-note") made decompose **invoke aif-note via the Skill tool once per task** to write each spec note (Two-Tier Output procedure, `src/skills/roadmap-decompose/SKILL.md` ~lines 284–298). That introduced cruft that must go:

- Step 3 tells aif-note to take "that task's drafted spec text **as the subject so aif-note does not blend it with sibling tasks**" — aif-note has no such parameter and handles its own context fine on its own. This instruction is wrong; remove it.
- "Sequential invocations", "capture the note path aif-note reports back", Critical Rule 6, and the contract-line rule at ~line 321 ("aif-note-written note file") all describe per-task aif-note invocation.

Per-task invocation degrades on long phases (each call re-reads an accumulating conversation), and the plan-reviewer rejected the implementation plan three times over it.

## Target

Replace the per-task aif-note invocation with one simple rule. decompose's per-task note step becomes exactly this and nothing more:

1. **Ensure the `aif-note` skill has been invoked at least once in this chat** — so its note-writing instructions are in context. If it has not been invoked yet, invoke it once now. If it already has been, do **not** invoke it again.
2. **Write the spec note manually** with the `Write` tool, following aif-note's instructions (already in context).

In particular:
- decompose **does not describe, embed, or modify the note format/structure**. The format lives in aif-note's instructions, loaded into the chat by step 1. Do **not** add any format description beyond what decompose already had before commit `0bfa177`.
- decompose **does not modify the `aif-note` skill** in any way.
- Drop the "pass the spec as a subject / don't blend siblings" wording entirely.

Everything else two-tier stays unchanged: the contract line in the roadmap (~600 chars, ending with the `Spec:` tag), one spec note per atomic task, the Atomicity Gate, the char budget.

**Recommended implementation approach:** revert commit `0bfa177` to restore decompose to its pre-task state, then re-add the two-tier output with the simple rule above — cleaner than editing the over-engineered procedure in place.

## Guards

- decompose carries **no** note-format description of its own; it relies on aif-note's instructions being in context (ensured by the "invoked at least once" check).
- **Do not modify the `aif-note` skill.**
- aif-note is invoked **at most once per chat** (to load its instructions), never per task.
- Keep the two-tier shape, contract line, `Spec:` tag, char budget, and Atomicity Gate unchanged.

## Files

- `~/projects/skills/src/skills/roadmap-decompose/SKILL.md` (modify, or revert `0bfa177` and re-add) — the Two-Tier Output procedure, Mode 1 Step 1.4, Mode 2.4/2.5, Critical Rule 6, and the contract-line rule (~line 321).

## Verify

- When writing specs, decompose checks whether `aif-note` was invoked in this chat; invokes it once only if it was not; then writes each spec note manually with `Write`.
- No per-task aif-note invocation remains anywhere in the skill.
- The skill describes no note format of its own.
- The `aif-note` skill is unchanged.
- Two-tier output (contract line + spec note) is still produced.
