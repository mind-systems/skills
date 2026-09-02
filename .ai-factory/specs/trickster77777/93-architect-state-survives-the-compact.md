# agent-architect: the architect's own state survives the compact

`src/skills/agent-architect/SKILL.md` holds two pieces of its own state — the
editor's handle and its buffer's path — in prose that assumes the context
holding them survives a compact. The handoff paragraph never says *whose*
handoff carries it; the buffer section still describes itself as a
deferral log although the handle now lives there too; and the liveness
sentences name the outcomes without ever naming the test, so the gap was
filled in with the wrong tool. These are one merged task: the handoff
paragraph and the buffer section sit a few lines apart in the same file,
one names the other ("your buffer's path (below)"), and a single planning
attempt to split them tried to build a derivable-identity scheme the buffer
never needed — replaced here with the reduced fix.

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md:47-58`:

> "Before a compact, your handoff records the editor's handle, a digest of
> what it has accumulated, and your buffer's path (below); the digest is
> your own recovery note and is never sent to the editor. Continue in the
> same conversation if the editor is still alive. If it is dead — a stale
> handle discovered at recovery, or a failed send — report to the user
> **before anything is sent onward**; an undelivered payload is never
> auto-replayed into a fresh spawn, because the user phrased it for a warm
> context. The respawn is the next channel-message after that report, never
> eager with authored prose: the user re-phrases a relay as a self-contained
> spawn prompt, or an apply work-order is resent as-is. A respawned editor
> resumes through the same two channels, self-contained per round. Losing
> the editor is never fatal; losing it silently is the defect."

`src/skills/agent-architect/SKILL.md:161-169`:

> "## Your buffer is yours alone
>
> Keep one private buffer file for anything deliberately deferred — each
> entry names *what*, *why deferred*, and the *trigger* that resolves it;
> delete an entry once it's done. It lives at
> `.ai-factory/notes/<NN>-architect-buffer.md`, numbered like the other
> temporary notes so several architects can coexist without colliding. The
> editor is never told about it and no work-order references it — nothing is
> broken if it happens to see the file; it is the one file you edit
> directly, because it isn't a shared artifact."

## Defect A — the handoff's addressee is unstated

The paragraph says a handoff records the editor's handle and the buffer's
path, but never says *for whom* the handoff is written. A handoff written
for another agent — the user reading it, a fresh unrelated session picking
up the project — has no buffer to point at. A handoff that continues *this
same architect* across a compact is the only kind that must carry it.
Nothing outside this skill ever learns about the buffer or the handle; a
handoff addressed elsewhere has no reason to mention either, and the
paragraph must say so rather than reading as if every handoff carries it.

## Defect B — the buffer is described as a deferral log while it also holds the handle

"Your buffer is yours alone" opens by describing the file purely as a
deferral log — entries with a *what*, a *why deferred*, and a *trigger*.
Nothing in that description covers the editor's handle, which the paragraph
above sends there too. The section must state the buffer's real scope: it
holds whatever of the architect's own state must survive a compact — not
deferral entries alone. Deferral entries keep their existing shape
(*what* / *why deferred* / *trigger*; delete an entry once it's done) and
stay the file's primary content; the section also holds the editor's
handle and any assigned pairing role, and says so.

## Defect C — the liveness test is never named

The paragraph names the outcomes — "still alive" and "dead — a stale handle
discovered at recovery, or a failed send" — without ever naming the
procedure that tells them apart. Left to fill that gap on its own, the
architect reached for `ListAgents` and reported a warm, days-old editor
dead on that basis alone — disproven the same session when the user took
the identical handle from history and sent to it directly, reaching a live
editor.

The mechanism, stated correctly: a compact does not touch the editor at
all — its only effect is erasing the address from the architect's own
context. Two separate systems answer two different questions:

- **`ListAgents`'s subagent rows come from the live task registry** — the
  bookkeeping of what is currently an active, running task under this
  session. A completed subagent's round is dropped from that registry on
  the order of a minute after the round ends. Absence from that listing
  means only "not an active task right now," never "gone."
- **A send resolves the handle independently of that registry** — from the
  on-disk sidecar recorded for it, and resumes the agent from its own full,
  persisted transcript. This is why a handle taken from history and
  addressed directly reached the editor when the task-registry listing did
  not show it.

## The rule

- **Absence from a listing is never evidence of death.** `ListAgents`
  answers "what's an active task right now," not "does this handle still
  resolve."
- **A failed delivery is the only death signal.** The next channel-message
  is itself the probe: attempting to send it to the recorded handle *is*
  the liveness check, and its outcome — not a prior lookup — is the signal.
  No third message kind is introduced beside `REPORT-ONLY` and `APPLY-EDIT`
  to serve as a separate probe.
- **A handle that was never recorded is recovered from
  `~/.claude/projects/<project-key>/<session-id>/subagents/agent-<id>.meta.json`
  files** (`<project-key>` is the working directory's path with separators
  replaced by hyphens; `<session-id>` is the running session's own id;
  `"agentType"` inside the file names the editor's agent type, newest first
  by file mtime; the id is the filename segment between `agent-` and
  `.meta.json`) — never from a listing, for the identical reason
  `ListAgents` is ruled out as the liveness test above.

## Prevention

Spawn the editor with `Agent`'s `name:` parameter wherever the running build
exposes it: a named agent can then be addressed by that name rather than by a
raw handle. Treat this as a convenience and never as the carrier — the
parameter is absent from some builds, and nothing contracts the name's
behavior beyond the run itself. The carrier is the recorded handle, written
into the buffer per Defect B at the moment of spawn; it is what the discipline
stands on in every build. Where `name:` is exposed, it is an addressing
convenience layered on top of that carrier — never a second guarantee it could
be mistaken for.

## The change

Two edits to `src/skills/agent-architect/SKILL.md`, in the same paragraph
and section named above — no restructuring beyond them:

1. Rewrite `:47-58` to state, in order: the handoff addressed to this same
   architect across a compact is the one that carries the buffer's path
   (Defect A); the recording happens at spawn, via `Agent`'s `name:` where
   the build exposes it, with the handle also written into the buffer at
   that same moment, which holds it and any assigned pairing role and says
   so (Prevention, Defect B); at recovery, the only liveness test is
   the next channel-message itself, with `ListAgents` explicitly ruled out
   as a death signal and the
   `~/.claude/projects/<project-key>/<session-id>/subagents/agent-<id>.meta.json`
   fallback named for a handle that was never recorded (Defect C, The rule); the
   existing consequence of "dead" carries forward unchanged — report to the
   user before anything is sent onward, no auto-replay of an undelivered
   payload, the respawn is the next channel-message after that report,
   self-contained per round, losing the editor is never fatal, losing it
   silently is the defect.
2. Open `:161-169` so the section acknowledges that it holds the editor's
   handle and any assigned pairing role, and that the handoff continuing
   this architect carries the buffer's path alone.

Recorded state now spans three things, not two: the editor's handle, the
buffer's own path, and — wherever the user has assigned one — the
architect's pairing role (task 26.4). The buffer holds all three; only its
own path travels in the handoff that continues the architect across a
compact, and none of the three is treated as more durable than the others.

## Files & types

- edit: `src/skills/agent-architect/SKILL.md` — the `:47-58` paragraph and
  the "Your buffer is yours alone" section (`:161-169`) only.

## Guards

- The buffer's path stays exactly `.ai-factory/notes/<NN>-architect-buffer.md`
  with its present numbering — no slug key, no session-derived id, no
  fallback directory scan, no echo-the-path step. A prior attempt at this
  task built exactly that machinery for a problem this reduced fix does not
  have; all of it is retired by this spec, not left as an open option for a
  later planner to reconsider.
- `src/skills/note/SKILL.md`, `src/commands/command-handoff.md`,
  `src/skills/roadmap-engine/SKILL.md`, `src/agents/editor.md`, and
  `src/skills/architect-editor-engine/SKILL.md` are all untouched — this
  knowledge lives entirely in the architect's own skill and nowhere else.
- `ListAgents` is not banned outright — only ruled out as the liveness
  oracle for a handle the architect holds or is trying to recover.
- One spawn per session stays unchanged — this task does not add a second
  spawn path or change when a spawn happens, only what happens at the
  moment it already does.
- The report-before-anything-is-sent-onward rule, the no-auto-replay rule,
  and the respawn discipline stay byte-identical in substance.
- No line of this spec, or of the skill text it produces, rests on
  undocumented harness behavior; the recorded handle is the carrier precisely
  because it does not.

## Verification

- Manual read: `:47-58` states, in order, the addressee of the handoff that
  carries the buffer's path, the at-spawn recording via `name:`
  and the buffer write, the send-based liveness test with `ListAgents`
  explicitly ruled out, the
  `~/.claude/projects/<project-key>/<session-id>/subagents/agent-<id>.meta.json`
  fallback for an unrecorded handle, and the unchanged "dead" consequence.
- Manual read: `:161-169` opens by acknowledging that the section holds the
  editor's handle and any assigned pairing role, states that the handoff
  continuing this architect carries the buffer's path alone, keeps the
  deferral-entry shape unchanged, and keeps the closing sentence's
  substance.
- `grep -n "name:" src/skills/agent-architect/SKILL.md` → at least one hit
  in the rewritten paragraph.
- `grep -n "ListAgents" src/skills/agent-architect/SKILL.md` → at least one
  hit, explicitly ruling it out as the death signal.
- `grep -n "subagents/agent-" src/skills/agent-architect/SKILL.md` → the
  never-recorded-handle fallback is present, with the full
  `~/.claude/projects/<project-key>/<session-id>/` root stated, not the bare
  `subagents/agent-<id>.meta.json` form.
- `grep -n "<NN>-architect-buffer.md" src/skills/agent-architect/SKILL.md`
  → the buffer's path and numbering are unchanged from today's form.
- `git diff --stat` shows exactly one file changed.
