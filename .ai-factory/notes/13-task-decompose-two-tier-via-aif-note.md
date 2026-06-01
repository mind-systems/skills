# Task Spec — roadmap-decompose always emits two-tier output by invoking aif-note

**Date:** 2026-06-01
**Roadmap:** ROADMAP.md Milestones
**Provenance:** user request. Supersedes the *mechanism* of note `09-decompose-spec-notes-extraction.md` (keeps its concept). Builds on this session lifting aif-note's model-invocation ban.

## Current state

`roadmap-decompose/SKILL.md` writes the **full spec inline** in each `ROADMAP.md` bullet — Mode 1 Step 1.3 ("Generate roadmap file"), Mode 2 Steps 2.4/2.5, and the "Roadmap File Format" section all show inline specs. There is no contract-line / spec-note split, no `Spec:` tag, no aif-note invocation (confirmed: grep for `two-tier` / `Spec:` / `notes/<NN>-task` / `summary line` in the skill returns nothing).

To get the two-tier shape the user wants, they currently **chain two skills manually** — `/roadmap-decompose` then `/aif-note` — or use the freeform prompt *"Давай ноуты со спеками и короткие декомпозированные саммари таски по ним."* Both **fire inconsistently**, the same flakiness class as the handoff feature, for two technical reasons: (1) `/a /b` parses only `/a` as a slash command — the rest becomes `$ARGUMENTS` text, so the second skill never runs as a skill; (2) until this session, aif-note had `disable-model-invocation: true`, so the agent couldn't invoke it via the Skill tool and fell back to wandering the filesystem / reinventing the format. Cause (2) is now fixed (ban lifted). This task fixes cause (1) by making decompose orchestrate the note itself instead of relying on the user to chain.

Note 09 is a prior, **unimplemented** plan for the same two-tier output, but via an **inline Tier-2 template embedded in decompose**. This task changes that mechanism: decompose **delegates** note-writing to aif-note rather than embedding a template. Keep note 09's *concept* (contract line + per-task spec note + char budget + `Spec:` tag + rationale); drop its "embed the template / Where to change the skill writes inline" instruction.

The skill is already strong ("godlike" per the user) — this is a **small, surgical** change, not a restructure.

## Target

Three changes to `roadmap-decompose/SKILL.md`:

1. **Always invoke the aif-note skill to write each task's spec note.** After a task passes the Atomicity Gate, decompose invokes `aif-note` (via the Skill tool) to persist that task's full spec as a per-task note — one note per atomic task (a gate split → two invocations). This is internal orchestration by the skill, **not** the user chaining two slash commands. Make the invocation instruction explicit in the skill body so the agent does it reliably every run.

2. **Define the roadmap entry as a contract/interface line.** Spell out in the skill (body + "Roadmap File Format") that each roadmap entry is the *interface*, not a lossy summary: target **~600 characters** (range **400–1000**, 1000 = extreme edge), naming the key files / types / guards involved (the "signature"), and **ending with the exact tag** `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` pointing at the note aif-note just wrote. Rationale to encode: this length lets the user verify intent and still fit 3–4 tasks on screen; the note is the implementation, the line is the header.

3. **Tell aif-note the content is a spec — but do not constrain or alter it.** When invoking aif-note, decompose passes the instruction that the note's content is the **task spec** (what exists today, the exact change, guards, files to touch, how to verify). It does **not** override aif-note's template, limit its capabilities, or change its behavior in any way — aif-note structures the note with its own judgment, just aimed at a spec rather than a generic research summary.

Touchpoints (same locations note 09 lists, but the action is "invoke aif-note + write contract line", never "write inline spec"): Mode 1 Step 1.3; Mode 2 Steps 2.4 and 2.5; the "Roadmap File Format" section (replace the inline-spec example with the contract-line + `Spec:` tag form); "Critical Rules" (add: every task is two-tier — a contract line in the roadmap + a spec note written by aif-note; never write a full spec inline).

## Guards

- **Small change only.** Do not restructure the modes or the Atomicity Gate. Redirect note-writing to aif-note and define the contract line — nothing more.
- **Do not touch aif-note.** No template override, no capability limits, no behavior changes. The only thing decompose tells it is "the content is a task spec."
- **One note per atomic task**, written *after* the gate passes; a split produces two invocations + two contract lines.
- **Every contract line ends with the `Spec:` tag** pointing at the note just written.
- **Char budget is guidance, not a hard clamp** — ~600 sweet spot, 1000 the extreme edge; enough to verify intent, 3–4 tasks per screen.
- **Reconcile with note 09:** read it for concept/rationale, but do **not** apply its "embed inline Tier-2 template" instruction — this task supersedes that mechanism with delegation.
- `roadmap-decompose` is a custom / never-overwrite-from-upstream skill (CLAUDE.md) — safe to edit directly.

## Files

- `~/projects/skills/.claude/skills/roadmap-decompose/SKILL.md` (modify)

## Verify

- `/roadmap-decompose` on a task list produces, per atomic task: a **contract line** in the roadmap (~600 chars, names files/types/guards, ends with the `Spec:` tag) **plus** a spec note written **by aif-note** — with no second manual skill invocation and no filesystem wandering.
- Re-running across sessions behaves the same way deterministically (the flakiness from manual chaining is gone).
- aif-note's own behavior/format is unchanged when invoked directly outside decompose.

## Resolved decisions

- **Note shape — take aif-note in its original form, affect it in no way.** decompose does **not** nudge aif-note toward any template (the Tier-2 shape from note 09 is dropped as a constraint). The only thing decompose passes is **what to note** — "specs" — and lets aif-note structure the note with its own native judgment. Same principle as the handoff command, which tells aif-note to note "context/handoff." aif-note stays a black box; callers only declare the subject matter.
