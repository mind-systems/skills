# agent-architect + editor: the paired loop to two lenses — the relay model, both halves dieted

Origin: [handoff 16](../handoffs/16-architect-overspecifies-editor-kills-its-independence.md) + a live user finding this session (both defs duplicate global CLAUDE.md and are bloated). **One concern realized across two files** — the paired loop's shared `relay / apply / analysis` contract — not independently deployable: the architect and editor defs share a vocabulary that must stay identical, so they land together. Same "one concern, two files" shape as task 1.6.1.

## Current state

Both halves of the paired loop are essays where the repo's pyramid philosophy wants lenses, and both duplicate global CLAUDE.md.

**Architect — `src/skills/agent-architect/SKILL.md`, 159 lines:**
- duplicates global CLAUDE.md — "draft from ground truth… read the actual files, following their chain of references down to the leaf" (`:69-74`) = § "Grounding claims";
- has **only apply-mode** work-order guidance ("every contract and value pinned", "Pin the values hard", `:75-88`), so on an analysis target (review, skeleton, decompose, "aim at phase N") it composes a prompt seeded with its own candidate findings and a preliminary verdict; the editor confirms exactly those and "convergence" is manufactured echo (handoff 16 §3);
- ceremony: "Why the pairing works" (`:36-43`), "Counterpart" (`:155-159`), compact/handoff and Output-register prose.

**Editor — `src/agents/editor.md`, 118 lines:**
- **apply-only framing** — "only to apply one already decided" (`:8-9`), "You do not reason about *whether* the change should happen" (`:22-24`) — contradicts the relay model, under which the editor receives relayed analysis tasks and must reason independently;
- ceremony: "Why you don't self-certify" (`:26-35`), "One session, growing history" (`:37-44`), "Counterpart" (`:114-118`);
- global duplication: ground-truth-over-memory (`:57`) and commit-on-permission (`:100-105`), inherited by the subagent (reachability per orchestrator spec 18).

## Change

Rewrite both files as lenses on one shared model — **relay / apply / analysis**.

**Architect — lens whose spine is the relay model:**
1. On any analysis/work target, the architect does **not** author a prompt — it **relays the user's own message** to the editor (English, faithful, no added findings/checklist/verdict/method); the user's message is the target + question.
2. The one relay transformation: expand a user-invoked skill to skill-by-reference ("Read `~/.claude/skills/<name>/SKILL.md`, apply with arguments: …") — the editor never received the slash-command.
3. It authors its own prompt in exactly one case — the pinned apply work-order (values, paths, exact strings, guardrails, self-verify commands, "do not commit") — after the user confirms the edits.
4. It still runs its own review in parallel and reconciles; the editor is never seeded, so agreement is real signal.

Retain compressed, non-global: spawn-once/message-thereafter, never-edit-shared-artifacts, verify-by-fact, user-rules-forks/owns-commits, the private buffer, rehydrate-fresh. Cut: the ground-truth/leaf duplication, "Why the pairing works", "Counterpart", ceremony.

**Editor — lens on two modes:**
- **analysis** (a relayed review / decompose / judge / hazard-hunt) → reason **independently** from the target, lean on no framing the message carries, report findings by fact;
- **apply** (a decided work-order) → apply exactly, add no scope, execute collision-safe where order matters.

Retain compressed, non-global: self-verify before reporting (never a bare "done"), flag every judgment call, escalate ambiguity / fix a wrong work-order and say so (never silently invent or deviate), skill-by-reference (read the pinned file; `loads:` engines invoke normally), persistent spawn-once, commit only on permission, English. Cut: the two essays, "Counterpart", the ground-truth/commit restatements. Rewrite the description's apply-only clause to name both modes.

## Files & types

- `src/skills/agent-architect/SKILL.md` — full rewrite to a lens; frontmatter (incl. `allowed-tools: … Agent SendMessage`) unchanged.
- `src/agents/editor.md` — full rewrite to a lens; frontmatter (`name`, `tools`, `model`, `effort`) unchanged **except** the description's apply-only clause, rewritten to name both modes.

## Guards

- **The only behavior changes are the relay model (architect) and the analysis mode (editor)** — everything else is compression. Both halves must use identical `apply / analysis / relay` vocabulary; that shared contract is why this is one task, not two.
- **Relay is scoped to editor-bound work, never every message.** Deciding which user messages are work for the editor versus conversation directed at the architect itself (a fork answer, "go", a commit order, a correction, a question about approach) is the architect's own standing judgment — it works today and the diet must preserve it, not flatten it into "forward everything." State it as a one-line scope, not a taxonomy.
- **An editor's scope question goes to the user, never to the architect's inference.** A clarification the editor flags back ("which skeleton pass?", "what is the scope of phase 8?") is correct editor behavior; the architect carries the question to the user and relays the answer — resolving it with its own guess is the same contamination re-entering through the back door.
- **Terse relay leans on the persistent editor; re-brief a cold one.** A bare "phase 14" resolves only because the editor carries the session; a skill-by-reference relay carries its own path read and a full user message is self-contained, but before a *terse* relay to a fresh or respawned editor the architect re-briefs from the digest the spawn-once discipline already records.
- **Do not restate global doctrine** (grounding, git) — both inherit it; the restatement *is* the duplication being removed. The repo's one-home rule applied to the pair.
- **Lens, not clamp** — keep every load-bearing discipline, cut only ceremony and duplication.
- **Pyramid-baseline** — unverified until a live paired-loop run compares behavior against the pre-rewrite baseline; the relay model and the analysis mode are the intended divergences, the rest is compression.

## Verification

- `wc -l` both files → lenses (down from 159 / 118), no load-bearing policy lost.
- Architect greps: `grep -ni "ground truth\|down to the leaf\|why the pairing works\|Counterpart" src/skills/agent-architect/SKILL.md` → gone; the relay model present (relay the user's message on analysis; expand a user-invoked skill to a path read; generate only the confirmed-apply work-order).
- Editor greps: `grep -ni "why you don't self-certify\|Counterpart\|do not reason about\|only to apply one already decided" src/agents/editor.md` → gone; both modes present.
- Live paired-loop dry-run: the editor's analysis prompt equals the relayed user message (English, no architect findings/verdict); the editor reasons independently on analysis and applies faithfully on apply; the sole architect-generated prompt is the confirmed apply work-order; self-verify + flag-every-judgment-call retained on both sides.
