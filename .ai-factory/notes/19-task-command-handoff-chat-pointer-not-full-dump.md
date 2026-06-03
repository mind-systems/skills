# Task — command-handoff: note mode should emit a short chat *pointer*, not the full handoff

## Problem

In **note mode**, the skill's Step 3 currently says:

> **Note mode:** Do both of the following:
> 1. Emit the handoff prompt to chat (same as chat mode).
> 2. Persist the handoff prompt as a note file …

So the **same full handoff is dumped twice** — once into the chat and once into the file, byte-identical.

Note mode is invoked precisely when the user is about to **/compact**. Dumping the entire (often long, "don't limit size") handoff back into the chat **re-bloats the very context the user is trying to clear** — the opposite of the intent. Observed live: the user interrupted a full-handoff re-dump and asked "are you just dumping the note into chat?" — the verbatim re-emit was pure noise on top of the file that already holds it.

The two outputs have **different audiences and should be different content**:
- **The note file** = the durable, full rehydration document, read by the *next agent* after compact.
- **The chat output** = a short *pointer* the *human* keeps (or pastes into the next session) so they/the next agent know **which note holds the full handoff** and roughly what it covers — without re-dumping it.

## Desired behavior

Note mode emits **two distinct contents**:

1. **Chat** — a short pointer/summary only:
   - the written note **path**,
   - a 3–5 line orientation: the one-sentence **frame**, the **next step**, and (optionally) the count of work-units covered.
   - It must be **paste-back-able**: the user can drop this snippet into the next session to point the fresh agent at the full note. It must **not** reproduce the full handoff body.
2. **File** — the full handoff (the existing skeleton, verbatim), unchanged.

Chat mode is unaffected (no file; the full handoff is the chat output, since there's nothing else to point at).

## Change to the skill (`src/commands/command-handoff.md`)

In **Step 3 — Output**, rewrite the Note-mode block so step 1 is a *pointer*, not a re-emit:

> **Note mode:**
> 1. Write the full handoff to the note file (steps a–d below).
> 2. Emit to chat **only a short pointer** — the note path plus a 3–5 line orientation (frame + next step) the user can paste into the next session. **Do not** re-emit the full handoff body to chat; the file holds it.

Keep the file-writing sub-steps (a–d) as they are. Update the trailing "report the path … as a one-line confirmation" so it's clearly part of the pointer, not in addition to a full dump.

Also adjust the self-check note: the proportionality/completeness gate applies to the **file** content; the **chat pointer** is intentionally minimal regardless of session size.

## Rationale

- Note mode exists to **survive compaction**; the chat half must be cheap, because the chat is what gets compacted away.
- File = for the machine (next agent rehydration). Chat = for the human (relay handle). Separating them removes the redundancy and the context bloat in one move.
