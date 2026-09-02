# agent-architect: pairing roles for two architects working together

`src/skills/agent-architect/SKILL.md` describes exactly one architect
working with exactly one editor. Nothing in the file, or anywhere else
under `src/`, gives a second architect-level agent a name, a role, or a
rule for how two of them divide the work between them — yet this session's
own family history already improvised exactly that division once, informally,
and found it valuable. This task gives the improvisation a name and a rule,
without changing the generic skill every unpaired architect still runs.

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md:19-28`:

> "You are the **architect** — this file is the operating discipline you
> rehydrate into on every invocation, whatever unit of work `$ARGUMENTS`
> names: a roadmap phase, a task, a class, a module, a review dimension.
> You reason, review, and decide; the **editor** — a persistent subagent
> you keep once spawned (see "Spawn once, message thereafter") — is the
> hand that applies every change and reports back; you check what landed
> against the files themselves, never against the report. You never touch
> the shared artifacts — roadmap, specs, code, docs — with your own
> hands; that hand is always the editor's. The editor is a separate agent
> with its own definition; this skill is the architect alone."

This is the file's only statement of who does what, and it names one architect
and one editor throughout — no second architect-level role exists anywhere in
it, or in any other skill. Verified with `grep -rniE "second architect|paired
architect|dual.?architect" src/` — zero hits (the only "pairing" hits anywhere
under `src/` are unrelated font pairings in `ui-ux-pro-max`'s design data).

## The requirement

The pairing is the user's own working arrangement, stated as a decision: two
architects run as a pair with no direct channel between them — one reasons,
reviews and decides, the other is the hand that applies — and the user assigns
each its half by naming it. Nothing in the repository documents this
arrangement; it is a decision to implement, not an observation to cite.

## Why an add-on, not a change to the generic skill

Which role an architect plays — deciding-and-reasoning, or hand-that-
applies — is not a property of `agent-architect` as a skill; it is a fact
about one deployment, assigned per agent and per session by the user when
two architects are actually running together. A generic skill that
hardcoded one role, or hardcoded the existence of a second architect at
all, would have to be re-edited for the next pairing, the next project, or
the next session that runs unpaired — the same "deployment-specific fact
baked into generic mechanism" failure the family's own composition rule
(mechanism vs policy) exists to prevent. The rule belongs in a skill an
architect opts into, not in the skill every architect always runs.

## The change

One new skill, `src/skills/architect-pairing-engine/SKILL.md`, on the
precedent of `architect-editor-engine`: one contract, seen from two ends,
loaded by both entities that need it — except here both ends are
architects, not an architect and its editor.

The skill holds both role halves in one file:

- **The deciding half.** Its own editor becomes a research-only channel —
  every `REPORT-ONLY` relay still goes to it as today, but no `APPLY-EDIT`
  work-order does. Application of a confirmed edit is instead addressed to
  the paired architect, through the user — the deciding architect states
  what it wants applied, the user carries or confirms the relay, and the
  applying architect is the one that acts on shared artifacts.
- **The applying half.** It originates no edit of its own — every change
  it makes to a shared artifact traces back to a work-order it received,
  never to its own independent judgment. It applies only what the arriving
  work-order pins, exactly as an editor would, and it does not route the
  work onward to its own editor — the applying architect's hands are its
  own, not delegated a second time.

An architect loads this skill only when the user has assigned it one of
these two roles for the session; an architect running unpaired never loads
it and never learns either half exists.

## The wiring

Landing this skill for real needs the same three edges any new skill in
this repo needs, per this repo's own dependency rule:

1. A `loads:` edge on `agent-architect/SKILL.md`'s frontmatter, naming
   `architect-pairing-engine`.
2. A per-skill symlink, `active/skills/architect-pairing-engine`, pointing
   at `../../src/skills/architect-pairing-engine`.
3. The skill named in `CLAUDE.md`'s active-set paragraph (the "**The
   active set**…" line), alongside `agent-architect` and the rest of the
   list actually loaded.

Flagging, not fixing, one existing gap found while checking item 3:
`architect-editor-engine` — the direct precedent for this new skill — is
already symlinked under `active/skills/` (verified:
`active/skills/architect-editor-engine -> ../../src/skills/architect-editor-engine`)
but is **not** named in that same `CLAUDE.md` active-set paragraph today.
Whatever caused that gap for `architect-editor-engine` is a pre-existing
defect this task does not touch or repeat by omission — it is named here
so the wiring step above does not silently reproduce it for the new skill,
and so the existing gap is on record for whoever picks it up.

## Files & types

- new: `src/skills/architect-pairing-engine/SKILL.md`.
- edit: `src/skills/agent-architect/SKILL.md` — frontmatter `loads:` only,
  to add the new edge.
- new: `active/skills/architect-pairing-engine` (symlink).
- edit: `CLAUDE.md` — the active-set paragraph, to name the new skill.

## Guards

- `editor.md` and `architect-editor-engine` stay untouched — this task
  adds a new skill loaded by two architects; it does not alter the
  architect-editor contract or the editor's own definition.
- The `::` mechanics and the two channel-message formats
  (`REPORT-ONLY` / `APPLY-EDIT`) stay byte-identical — the new skill
  routes existing channel-messages to a different recipient in the
  deciding half; it invents no third format and no new marker.
- The generic `agent-architect/SKILL.md` keeps its default, unpaired
  behavior — one architect, one editor, work-orders addressed to that
  editor — completely unchanged; only a session where the user has
  assigned a pairing role ever departs from it.
- No deployment-specific fact — which agent, which session, which user,
  which project — enters `architect-pairing-engine` or any other skill
  file; the role assignment itself is a runtime fact the user states each
  time, never written into the skill.

## Verification

- Manual read: `src/skills/architect-pairing-engine/SKILL.md` states both
  role halves, each naming what changes about work-order addressing and
  origination for that half.
- Manual read: the generic `agent-architect/SKILL.md`'s default section
  (`:19-28`, `:25-26`) is unchanged in substance for an unpaired session.
- `grep -n "architect-pairing-engine" src/skills/agent-architect/SKILL.md`
  → the `loads:` edge is present.
- `ls -la active/skills/architect-pairing-engine` → resolves to
  `../../src/skills/architect-pairing-engine`.
- `grep -n "architect-pairing-engine" CLAUDE.md` → the skill is named in
  the active-set paragraph.
- `git diff --stat` shows the new skill file, the `agent-architect`
  frontmatter edit, the new symlink, and the `CLAUDE.md` edit — nothing
  else.
