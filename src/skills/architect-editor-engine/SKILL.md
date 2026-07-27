---
name: architect-editor-engine
description: >-
  Shared channel-message-format contract for the architect↔editor paired loop.
  Holds the two channel-message formats — REPORT-ONLY and APPLY-EDIT — and the
  rule that a receiver keys its mode strictly off the token that literally
  opens each message. Carries no `::` grammar and no policy about when to use
  which format; that stays entirely with the caller. Loaded once at birth by
  both the architect (`src/skills/agent-architect`) and the editor
  (`src/agents/editor.md`).
user-invocable: false
disable-model-invocation: false
allowed-tools: Read
---

# Architect-Editor Engine — the Paired-Loop Channel-Message Contract

This is a shared pure-content leaf engine for the architect↔editor paired loop. It
holds one discriminator — which of two formats a channel-message is, and how a
receiver tells — not any procedure for composing a message or deciding when to send
one. The caller (`agent-architect`) stays in control of when and what to send; the
receiver (the editor) stays in control of how it reasons once the format is known.
This skill has no I/O of its own beyond reading itself. Load this skill once at
birth — the architect via its own `loads:` frontmatter edge, the editor as the very
first action on spawn — not lazily per message: the contract must be resident the
moment a channel-message arrives. This is a load-once engine: its callers depend on
its exact behavior — edits here must honor their expectations as part of its
contract; the reverse graph resolves via
`` grep -l "architect-editor-engine" src/skills/*/SKILL.md src/commands/*.md src/agents/*.md ``.

## The two channel-message formats

Every channel-message the architect sends the editor is exactly one of these two
formats, and it literally opens with the format's token — `REPORT-ONLY` or
`APPLY-EDIT`. Treat both tokens as byte-exact protocol tokens, on the same axis as
`PLAN_REVIEW_PASS` — never paraphrased, never inferred from content.

- **`REPORT-ONLY`** — a research relay. The receiver reads or runs the named
  target, reasons over it independently from the ground up, reports back by fact,
  and writes no files. Used for every relayed analysis target and every relayed
  skill-expansion.
- **`APPLY-EDIT`** — a pinned apply work-order. The receiver makes exactly the
  edits specified: every value, path, and exact string pinned; the guardrails
  stated (what not to touch, a collision-safe method where changes interact and
  order matters); the commands to run to self-verify before reporting; and an
  explicit do-not-commit. Used only for the architect's own authored, confirmed
  change.

## The mode rule

A receiver keys its mode strictly off the format token that literally opens the
message — never off content, never off a referenced skill's own default behavior
(a relayed skill whose own default writes files does not by itself promote a
`REPORT-ONLY` round to an edit). Ambiguity — no recognizable token opening the
message — resolves to `REPORT-ONLY`.

## What this engine does not hold

This engine carries nothing about `::` — how the architect parses raw user input
into a channel-message, and when it decides to send one, stays entirely with its
caller. It carries no policy of its own; it only describes the two formats a
channel-message can take and the rule for telling them apart.
