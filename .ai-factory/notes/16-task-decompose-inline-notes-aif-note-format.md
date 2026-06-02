# Task Spec — roadmap-decompose: write spec notes inline in aif-note's format, drop the per-task aif-note invocation

**Date:** 2026-06-02
**Roadmap:** ROADMAP.md Milestones
**Provenance:** user feedback after running decompose on real phases. Refines the delegation *mechanism* from note `13-task-decompose-two-tier-via-aif-note.md` (keeps its two-tier concept and aif-note's format).

## Current state

Per note 13's implementation, the **Two-Tier Output** procedure in `roadmap-decompose/SKILL.md` requires invoking `aif-note` via the **Skill tool once per task** to persist each spec note (procedure step 3: "Invoke the `aif-note` skill via the Skill tool"). `allowed-tools` includes `Skill` for this.

This **degrades on multi-task runs**. In Mode 1, decompose drafts every task's full spec in memory (Step 1.3), then at finalization (Step 1.4) invokes aif-note per task. By the Nth invocation the conversation holds all prior drafted specs, and aif-note — which re-analyzes the full conversation context rather than accepting passed-in content — can **blend sibling tasks** into the note. Each call is also largely **ceremony**: decompose already drafted the full spec, so aif-note's re-derivation adds risk without adding content. Validated in practice (and confirmed independently in a separate session): single or few tasks come out clean; a 6–7-task phase degrades as accumulated context noise grows.

The mechanism is the only problem — the **two-tier shape and aif-note's note format are correct and stay**.

## Target

Remove the **per-task** aif-note invocation. decompose writes each spec note **inline** (`Write`), in **aif-note's format and filing convention** — aif-note stays the single source of truth for both.

1. **Load aif-note's format once per run (soft recommendation, not a per-task mandate).** decompose recommends having aif-note's note format in context. It **may invoke `aif-note` once** at the start of a run (Skill tool) to surface its template and rules, **or** rely on the format already being in context from an earlier invocation this session (a skill's instructions persist for the session once loaded — no need to re-invoke per task). On a later decompose run in the same session, re-invoking aif-note or noting it is already loaded are both fine. **Keep `Skill` in `allowed-tools`** for this one optional load.

2. **Write each note inline.** For every confirmed atomic task, write the spec note directly with `Write`, in aif-note's format and following aif-note's filing convention — both already in context from the loaded skill. The slug is the task name (lowercase, hyphens). No aif-note invocation per task.

3. **Sequential writes.** Write notes one at a time — each fully written to disk before the next — so aif-note's numbering stays consistent (a later note sees the earlier one already on disk). Don't batch.

4. Update the affected spots to inline writes (not invocations): the **Two-Tier Output** procedure (steps 3–5 — "invoke aif-note" → "write the note inline in aif-note's format"; "capture the path aif-note reports" → "use the path you wrote"); **Mode 1 Step 1.4** finalization; **Mode 2.4 / 2.5**. The contract line, the `Spec:` tag, the char budget, and the Atomicity Gate are unchanged.

## Guards

- **No per-task aif-note invocation** — that is the degradation source being removed. At most **one** invocation per run (to load the format), or zero if already in context.
- **Keep `Skill` in `allowed-tools`** — needed for the one optional format-load invocation.
- **Write notes sequentially** — one fully written before the next — so aif-note's numbering stays consistent.
- Mode 2.5 note-update rule is unaffected in spirit: if a milestone already carries a `Spec:` tag, **update that note file in place** (inline Write to the existing path); only create a new note for a milestone without a tag.
- `roadmap-decompose` is a custom / never-overwrite-from-upstream skill (CLAUDE.md line 95) — safe to edit directly.

## Files

- `~/projects/skills/.claude/skills/roadmap-decompose/SKILL.md` (modify) — Two-Tier Output procedure (steps 3–5), Mode 1 Step 1.4, Mode 2.4/2.5, and the `allowed-tools` framing note (keep `Skill`, reframe its use as a one-time format load, not a per-task call).

## Verify

- A 6–7-task phase produces correctly-numbered, **non-blended** spec notes in aif-note's format, with **no per-task `Skill` invocation**.
- decompose invokes aif-note **at most once per run** (format load), or zero times if already in context.
- Notes match aif-note's template; contract lines and `Spec:` tags are unchanged from the current two-tier output.
- A single-task run still works and does not depend on any per-task invocation.
