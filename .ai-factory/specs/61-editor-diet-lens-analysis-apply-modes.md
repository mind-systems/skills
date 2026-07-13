# editor: diet to a lens — accommodate analysis vs apply, cut ceremony and global-CLAUDE duplication

Origin: same session as [handoff 16](../handoffs/16-architect-overspecifies-editor-kills-its-independence.md) / task 7.1 — the architect half is dieted there; this is the editor half. The pair lands coherently, 7.1 then 7.2.

## Current state

`src/agents/editor.md` is 118 lines — a subagent definition that should be a lens like its architect counterpart. Three faults:

1. **Apply-only framing contradicts the relay model.** The description says "do not spawn this agent to reason about or decide a change, only to apply one already decided" (`:8-9`) and the body "You do not reason about *whether* the change should happen — that call is already made" (`:22-24`). But under 7.1's relay model the editor receives **relayed analysis tasks** — a review, a decompose/skeleton pass, a judge/hazard-hunt — and its whole value there is **independent reasoning**. The def has no analysis mode; it forbids the very thing the loop already uses it for.
2. **Ceremony/essay.** "Why you don't self-certify" (`:26-35`), "One session, growing history" (`:37-44`), and "Counterpart" (`:114-118`) restate the obvious or the frontmatter description.
3. **Global-CLAUDE duplication.** Ground-truth-over-memory ("never work from a memory of what the skill does", `:57`) and commit-on-permission (`:100-105`) are global doctrine (§ "Grounding claims", § "Git") the subagent inherits — a subagent loads user-scoped `~/.claude/CLAUDE.md` (the reachability established in the orchestrator's spec 18).

## Change

Rewrite `editor.md` as a **lens** whose spine is two modes.

- **Two kinds of work.** The architect hands you either an **analysis** task (a relayed review / decompose / judge / hazard-hunt) or an **apply** work-order (a decided change). On **analysis**: reason independently from the target itself, lean on no framing the message carries, and report findings by fact. On **apply**: apply exactly as written, add no scope, execute collision-safe where the order of edits matters.
- **Retain, compressed** (load-bearing and not global): self-verify before reporting — run the work-order's verify commands, read the diff back, never a bare "done"; flag every judgment call; escalate ambiguity, and fix a wrong work-order and say so — never silently invent or deviate; skill-by-reference (read the pinned `…/SKILL.md` and apply as invoked; its `loads:` engines invoke normally via the Skill tool); persistent (spawn once, history sharpens but never carries the task — every work-order self-contained); commit only on explicit permission (one line); work and report in English.
- **Cut:** the "Why you don't self-certify" and "One session, growing history" essays (fold each to one line inside the retained disciplines), the "Counterpart" section, the ground-truth-over-memory restatement (folded into the skill-by-reference line), and the apply-only absolute (replaced by the two-mode spine).

## Files & types

- edit `src/agents/editor.md` only — full rewrite to a lens. Frontmatter (`name`, `tools`, `model`, `effort`) unchanged **except** the description's apply-only clause, rewritten to name both modes.

## Guards

- **The only behavior change is the analysis mode.** Apply-mode behavior is unchanged; the addition is that the editor now explicitly reasons independently on an analysis task. That mirrors 7.1's other half: the editor reasons from the target and **resists any verdict/framing that slipped through the relay**, so the pair's two minds stay genuinely independent — defense in depth against the architect seeding.
- **Do not restate global doctrine** (grounding, git) — the editor inherits it; a restatement is the duplication being removed. The repo's one-home rule applied to the subagent.
- **Lens, not clamp** — keep every load-bearing discipline, cut only ceremony and duplication.
- **Runs after 7.1** — shares the apply/analysis vocabulary; no same-file collision (different files), but the two rewrites must stay coherent, so 7.1 lands first.
- **Pyramid-baseline** — verify by a live paired-loop run; the analysis mode is the one intended divergence, the rest is compression.

## Verification

- `wc -l src/agents/editor.md` → a lens (down from 118), no load-bearing discipline lost.
- `grep -ni "why you don't self-certify\|Counterpart\|do not reason about\|only to apply one already decided" src/agents/editor.md` → the essays, ceremony, and apply-only absolute gone.
- Both modes present and unambiguous: analysis → reason independently; apply → apply faithfully, collision-safe.
- Live paired-loop dry-run: on a relayed analysis task the editor reasons independently from the target; on an apply work-order it applies faithfully; self-verify + flag-every-judgment-call retained on both.
