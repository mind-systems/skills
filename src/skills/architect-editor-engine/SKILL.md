---
name: architect-editor-engine
description: >-
  Shared channel-message-format contract for the architect↔editor paired loop.
  Holds the two channel-message formats — REPORT-ONLY and APPLY-EDIT — and the
  rule that a receiver keys its mode strictly off the token that literally
  opens each message. Holds only the two formats; when-to-use policy stays
  with the caller. Loaded once at birth by both the architect
  (`src/skills/agent-architect`) and the editor (`src/agents/editor.md`).
user-invocable: false
disable-model-invocation: false
allowed-tools: Read
---

# Architect-Editor Engine — the Paired-Loop Channel-Message Contract

Load this skill once at birth — the architect via its own `loads:` frontmatter edge, the editor as the first action on spawn — so the contract is resident before any channel-message arrives. This is a load-once engine; its callers depend on its exact behavior, and the reverse graph resolves via `` grep -l "architect-editor-engine" src/skills/*/SKILL.md src/commands/*.md src/agents/*.md ``.

## The two channel-message formats

Every channel-message the architect sends opens literally with its format token — `REPORT-ONLY` or `APPLY-EDIT` — held byte-exact, like `PLAN_REVIEW_PASS`, never paraphrased.

- **`REPORT-ONLY`** — a research relay: the receiver reads or runs the target, reasons independently, reports by fact, writes no files.
- **`APPLY-EDIT`** — a pinned apply work-order: the receiver makes exactly the edits specified, self-verifies, and does not commit.

## The mode rule

A receiver keys its mode strictly off the token that opens the message — never off content, never off a referenced skill's own default. Ambiguity resolves to `REPORT-ONLY`. The full authoring and execution mechanics of each format stay with the callers; this engine holds only the two formats and the rule for telling them apart.
