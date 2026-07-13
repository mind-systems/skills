# Plan: 7.1 — agent-architect + editor: the paired loop to two lenses over the relay model

## Context
Rewrite both halves of the architect↔editor paired loop from bloated essays into lenses over one shared **relay / apply / analysis** model — so on an analysis target the architect relays the user's own message (never seeding its own findings) and the editor reasons independently, while both stop duplicating global CLAUDE.md doctrine.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Rewrite the architect lens

- [x] **Task 1: Rewrite `agent-architect/SKILL.md` to a relay-model lens**
  Files: `src/skills/agent-architect/SKILL.md`
  Full rewrite of the body to a lens whose spine is the relay model. Keep the frontmatter unchanged **except** verify `allowed-tools` still lists `Agent SendMessage` (no change intended). Per spec `.ai-factory/specs/60-paired-loop-two-lenses-relay-model.md` § Change (architect):
  1. **Relay by default on any analysis/work target** — the architect does *not* author a prompt; it relays the user's own message to the editor faithfully, translated to English, adding no findings/checklist/verdict/method. The user's message *is* the target + question.
  2. **The one relay transformation** — expand a user-invoked skill to skill-by-reference: "Read `~/.claude/skills/<name>/SKILL.md`, apply with arguments: …" (the editor never received the slash-command). `loads:` engines resolve normally on the editor side.
  3. **Author its own prompt in exactly one case** — the pinned apply work-order (values, paths, exact strings, guardrails, self-verify commands, explicit "do not commit"), and only after the user confirms the edits.
  4. **Run its own review in parallel and reconcile** — the editor is never seeded, so agreement is real signal.
  Retain, compressed and non-global: spawn-once/message-thereafter, never-edit-shared-artifacts, verify-by-fact, user-rules-forks/owns-commits, the private buffer (`.ai-factory/notes/<NN>-architect-buffer.md`), rehydrate-fresh-on-every-invocation, English work-order register.
  Honor the Guards in the spec: relay is scoped to editor-bound work only (state as a one-line scope, not a taxonomy — deciding which messages are editor work vs. conversation to the architect is the architect's standing judgment); an editor's scope question goes to the user, never the architect's inference; a terse relay leans on the persistent editor, so re-brief a cold/respawned editor from the digest before a terse relay.
  Cut: the ground-truth/down-to-the-leaf duplication of global CLAUDE.md, "Why the pairing works", "Counterpart", and the compact/handoff + Output-register ceremony (compress what is load-bearing, delete the essay).
  Use the shared `apply / analysis / relay` vocabulary identically to the editor (Task 2).

### Phase 2: Rewrite the editor lens

- [x] **Task 2: Rewrite `editor.md` to a two-mode lens** (pairs with Task 1 — shared vocabulary must match)
  Files: `src/agents/editor.md`
  Full rewrite of the body to a lens on two modes. Keep frontmatter (`name`, `tools`, `model`, `effort`) unchanged **except** rewrite the `description`'s apply-only clause ("do not spawn this agent to reason about or decide a change, only to apply one already decided") to name **both** modes — analysis and apply. Per spec § Change (editor):
  - **analysis mode** (a relayed review / decompose / judge / hazard-hunt) → reason **independently** from the target, lean on no framing the message carries, report findings by fact.
  - **apply mode** (a decided work-order) → apply exactly, add no scope, execute collision-safe where order matters.
  Retain, compressed and non-global: self-verify before reporting (never a bare "done"); flag every judgment call; escalate ambiguity, and fix a wrong work-order and say so (never silently invent or deviate); skill-by-reference (read the pinned file; `loads:` engines invoked normally via the Skill tool); persistent spawn-once with growing history that sharpens but never carries the task; commit only on explicit permission; English register.
  **Recast the current `## The work-order is the unit` section** (not in the retain or cut list above): its don't-merge-two / don't-split-one discipline is load-bearing and must survive, but recast so it applies to *the round's unit in both modes* — do not carry forward the "always exactly one fenced block" framing, which is false in analysis mode where the unit is the relayed user message, not a fenced work-order. In apply mode the unit is the one work-order; in analysis mode the unit is the relayed message; in neither mode does the editor merge two units or split one into pieces the architect didn't ask for.
  Cut: the two essays ("Why you don't self-certify", "One session, growing history" as standalone sections), "Counterpart", and the ground-truth/commit restatements of global doctrine (compress the load-bearing rule, delete the restatement).
  Use the shared `apply / analysis / relay` vocabulary identically to the architect (Task 1) — that shared contract is why both files land in one task.

## Verification (run as part of the tasks, not as a separate task)
- `wc -l` both files → materially shorter than 159 / 118, no load-bearing policy lost.
- `grep -ni "ground truth\|down to the leaf\|why the pairing works\|Counterpart" src/skills/agent-architect/SKILL.md` → gone; relay model present.
- `grep -ni "why you don't self-certify\|Counterpart\|do not reason about\|only to apply one already decided" src/agents/editor.md` → gone; both modes present.
- Both files use identical `apply / analysis / relay` vocabulary.

These text gates confirm only that text was removed and renamed — per the spec they **cannot** settle whether the behavior change (relay-on-analysis, two editor modes) actually holds or whether a load-bearing discipline was lost in compression. This milestone introduces a behavior change, not pure compression, so the task is **not** done on greps + `wc` alone.

## Manual post-merge gate (not automatable by the orchestrator; the rewrite is unverified until this runs)
A live architect↔editor paired-loop dry-run, per the spec's Verification + "Pyramid-baseline" Guard, is the primary correctness check and cannot be run in-task by an implementer. Carry it forward explicitly as a manual gate. Success criteria:
- On an analysis target, the editor's analysis prompt **equals the relayed user message** (English, carrying no architect findings/verdict/method).
- The editor reasons **independently** on analysis and applies **faithfully** on apply.
- The only architect-generated prompt in the run is the confirmed-apply work-order.
- self-verify-before-reporting and flag-every-judgment-call are retained on both sides.
- The relay model and the analysis mode are the intended divergences from the pre-rewrite baseline; everything else must be behavior-identical (compression only).
