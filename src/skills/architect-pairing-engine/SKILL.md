---
name: architect-pairing-engine
description: >-
  Pairing-role contract for two architects working together with no direct
  channel between them — every message crosses through the user, who
  carries or confirms each relay. Holds the two role halves: deciding,
  whose editor becomes research-only and whose apply work-orders address
  the paired architect instead of its own editor; and applying, which
  originates no edit of its own, applies through its own editor only what
  an arriving work-order pins, and reports back an order that is
  underspecified, self-contradicting, or would break something it never
  named instead of applying it in silence. Load only when the user has
  assigned it one of these two roles for the session; never in an unpaired
  session.
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

Because that delivery is a human copy-paste and not a `SendMessage` call,
the work-order ships as one single code block — every pinned value,
guardrail, self-verify command and the "do not commit" inside it — so the
user can copy it whole and relay it unmodified. Never split it across
several blocks or interleave prose between them.

Departure from the generic spawn trigger: the generic rule offers two
alternatives for the first channel-message — the first `::` relay or, where
none has arrived, the first authored apply work-order. For this half the
second alternative is deleted, since the apply work-order no longer travels
to the editor and can never be the spawn. The spawn trigger for the deciding
half is the first `::` relay alone.

## The applying half

It originates no edit of its own: every change to a shared artifact traces
to an arriving work-order, never to its own judgment. What arrives is a
decision, not a delivery — it composes that decision into an `APPLY-EDIT`
message to its own editor, exactly as an unpaired architect does. The editor
is the hand here as everywhere; the only departure is where the work-order's
content comes from. Composing an arriving decision into that `APPLY-EDIT` is
authoring it, so the generic spawn trigger applies here unchanged, both
alternatives intact. An arriving work-order carries no `::` and needs none:
this half authors rather than relays, and the marker governs relays alone.

Applying exactly is not obeying blindly. Read the arriving work-order
against the files before sending it to your editor: where it is
underspecified, contradicts itself, or would break something it never named,
report that back instead of guessing your way through it, and name in your
report every decision the work-order left unpinned. The deciding half
verifies what landed against the files, so an unflagged judgment call is the
one thing its check cannot see.
