---
name: aif-handoff — rich self-handoff prompt that survives /compact
description: A skill that, on demand, generates a dense self-contained continuation/handoff prompt (read-first artifacts + model spine + current state + next step + working-discipline + error log) so a fresh post-compact agent rehydrates the whole effort — far richer than the default /compact summary.
type: project
---

# aif-handoff — A Skill that Emits a High-Quality Continuation Prompt

**Date:** 2026-05-31
**Source:** conversation context — produced a hand-written handoff prompt at the end of a long, knowledge-dense session and it was dramatically better than what `/compact` would have generated.

## Key Findings

- **The problem:** the built-in `/compact` continuation summary is often *impoverished*. After a long session that built a real knowledge base (a spec, a set of decisions, a working rhythm), the auto-summary loses the rationale, the working discipline, and the hard-won "don't do X" lessons. The next turn feels like a brand-new chat with amnesia.
- **The fix the user wants:** a skill that, when invoked, **writes a handoff/continuation prompt** capturing the session the way an expert would brief their replacement — and the user pastes it into the post-compact (or new) session. It consistently produces the "great" result instead of the bare summary.
- **The single most important principle the good prompt encodes:** *knowledge is durable in the repo's files, not in the chat.* The prompt's job is to **point the next agent at the right artifacts and tell it to rehydrate from them** — not to restate everything (which a summary does badly). Plus it carries the two things a summary always drops: the **working relationship/discipline** and the **error log**.
- This is a **generation** skill (mines the live conversation), not a fixed template — the section *skeleton* is fixed; the *content* is extracted from the session.

## Details

### Why the default summary fails (what to beat)

- It paraphrases recent turns, so it keeps *transcript* and loses *structure* (the model, the decisions, why).
- It never preserves **how to work with this user** — the confirm-before-execute rhythm, "show the diff before applying," when to stop and ask.
- It never preserves the **mistakes made and corrected** — so the next agent happily repeats them.
- It tries to re-state knowledge inline instead of saying "the truth lives in `file X`; read it."

### What the skill should produce — the section skeleton (mined from the session)

A single self-contained prompt with these parts (omit a part only if genuinely empty):

1. **Frame** — one line: where we are, and the load-bearing instruction *"the chat is compacted but the knowledge is durable in files; rehydrate from them, don't trust memory."*
2. **Read-first artifacts, in order** — the minimal set of files that re-hydrate everything, with a one-line "what it answers" each. Lead with the single best entry doc if one exists. (This replaces restating content.)
3. **Orientation** — the moving parts: the project, the key directories, any "two of a kind" traps (e.g. two roadmaps, two agents) that are easy to confuse.
4. **The domain model spine** — the settled model in one screen, headlined, with "don't re-litigate" + pointers to the doc per point.
5. **Current state** — what's done vs in-flight; explicitly call out **uncommitted** working-tree state.
6. **Immediate next step** — the one thing to do next, and who does what.
7. **Working discipline with this user** — their decision rhythm, review preferences, interrupt habits; how to behave. (Highest-value, always dropped by summaries.)
8. **Error log / cautionary tales** — the concrete mistakes made this session and the corrections, so they aren't repeated. Name them specifically.
9. **Hard rules** — commits/permission, file language, memory-write triggers, project conventions (e.g. "spec notes are self-contained").

### Behavior / shape

- **Trigger:** user invokes near end of context or before a deliberate `/compact` / new session. Likely names: `aif-handoff`, `aif-continuation`, `compact-handoff`.
- **Output:** emit the prompt as a chat message the user copies; **optionally** also write it to a file (e.g. `.ai-factory/HANDOFF.md` or `.ai-factory/notes/<NN>-handoff.md`) so it survives even if the message scrolls away. Decide default vs flag.
- **Adaptivity:** it must *extract* artifacts, decisions, current state, next step, and the error log **from the actual conversation** — not emit a blank template. If the session has no durable artifacts to point at, it should say so and lean harder on inlined state.
- **Tone:** dense, organized, addressed to the next agent ("you are picking up…"), English regardless of conversation language (matches repo conventions).

### Reference example

The hand-written prompt that motivated this (sections 1–9 above, mined live) lived in a `tradeoxy_core` indicator-engine v2 session. Worth pasting a sanitized version into the skill as a few-shot exemplar when building it — it demonstrates the density and the "rehydrate from files + discipline + error-log" emphasis that the default summary lacks.

### Relationship to existing skills

- Complements `aif-note` (extracts a *topic* note) — this extracts a *whole-session handoff* aimed at a future agent, not a knowledge note.
- Not the same as `/compact` — it's the *better-authored alternative* the user pastes back; could also be positioned as "run this, then compact."

## Open Questions

- Default output: chat-only, file-only, or both? (Leaning both — file as the durable copy.)
- Should it auto-detect the "single best entry doc" (e.g. a migration guide / index note) heuristically, or ask the user which artifact is the canonical entry point?
- Should there be a companion "rehydrate" verb that, given a handoff file, reads the listed artifacts in order before resuming?
