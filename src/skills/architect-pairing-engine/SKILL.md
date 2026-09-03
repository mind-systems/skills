---
name: architect-pairing-engine
description: >-
  Pairing-role contract for two architects working together with no direct
  channel between them — every message crosses through the user, who carries
  or confirms each relay. Holds the two role halves: deciding, whose editor
  becomes research-only and whose apply work-orders address the paired
  architect instead of its own editor; and applying, which originates no
  edit of its own and applies only what an arriving work-order pins. Load
  only when the user has assigned it one of these two roles for the session;
  never in an unpaired session.
user-invocable: false
disable-model-invocation: false
allowed-tools: Read
---

# Architect Pairing Engine — the Two-Architect Pairing-Role Contract

Two architects work together as a pair, one deciding and one applying, with
no direct channel between them — every message between them crosses through
the user, who carries or confirms each relay. This skill states only the
**departures** from `agent-architect`'s generic discipline; anything it does
not name here stays exactly as the generic skill has it.

Load this skill only when the user has assigned you one of the two roles
below — never in an unpaired session. This is not a load-once-at-birth
engine like `architect-editor-engine`; the reverse graph resolves via
`` grep -l "architect-pairing-engine" src/skills/*/SKILL.md src/commands/*.md src/agents/*.md ``.

## The deciding half

Its editor becomes research-only: every `REPORT-ONLY` relay still reaches it
exactly as the generic discipline has it. No `APPLY-EDIT` work-order does —
the architect still authors the apply work-order exactly as today: same
format, the same pinned values, guardrails, self-verify commands, and the
explicit "do not commit." But it addresses that work-order to the paired
architect and delivers it through the user, who carries or confirms the
relay. The applying architect is the one that acts on shared artifacts, not
this half's own editor.

Departure from the generic spawn trigger: the generic rule offers two
alternatives for the first channel-message — the first `::` relay or, where
none has arrived, the first authored apply work-order. For this half the
second alternative is deleted, since the apply work-order no longer travels
to the editor and can never be the spawn. The spawn trigger for the deciding
half is the first `::` relay alone.

## The applying half

It originates no edit of its own: every change it makes to a shared artifact
traces to an arriving work-order, never to its own judgment. It applies
exactly what that work-order pins, the way an editor would, and does not
route it onward to an editor of its own — its hands are its own, not
delegated a second time.

This half supersedes the generic default that the architect never touches
shared artifacts with its own hands, that hand always being the editor's:
for the applying half, the architect's own hands are the ones that act on
the arriving work-order.
