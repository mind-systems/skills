---
name: architect-editor-engine
description: >-
  Shared contract for the architect↔editor paired loop, loaded once at birth by
  both the architect (`src/skills/agent-architect`) and the editor
  (`src/agents/editor.md`). Holds the two channel-message formats — REPORT-ONLY
  and APPLY-EDIT — with the rule that a receiver keys its mode strictly off the
  token that literally opens each message, and the definition of the
  architect's buffer the pair shares: its path and numbering, its settled zone
  held by both halves and its live zone held by the architect alone, the
  editor's re-read of the settled zone on change, and the drain rule that a
  ruling leaves the buffer once it reaches the artifact that should hold it,
  and the rule that no architect reads another's buffer and an editor reads
  only its own architect's. When-to-use policy stays with the caller.
user-invocable: false
disable-model-invocation: false
allowed-tools: Read
---

# Architect-Editor Engine — the Paired-Loop Contract: Channel-Messages and the Shared Buffer

Load this skill once at birth — the architect per the instruction in its own body, the editor as the first action on spawn — so the contract is resident before any channel-message arrives and the buffer's definition below is held by both halves from birth. This is a load-once engine; its callers depend on its exact behavior, and the reverse graph resolves via `` grep -l "architect-editor-engine" src/skills/*/SKILL.md src/commands/*.md src/agents/*.md ``.

## The two channel-message formats

Every channel-message the architect sends opens literally with its format token — `REPORT-ONLY` or `APPLY-EDIT` — held byte-exact, like `PLAN_REVIEW_PASS`, never paraphrased.

- **`REPORT-ONLY`** — a research relay: the receiver reads or runs the target, reasons independently, reports by fact, writes no files.
- **`APPLY-EDIT`** — a pinned apply work-order: the receiver makes exactly the edits specified, self-verifies, and does not commit.

## The mode rule

A receiver keys its mode strictly off the token that opens the message — never off content, never off a referenced skill's own default. Ambiguity resolves to `REPORT-ONLY`. That fallback never reaches what keeps the hand current: as § "The architect's buffer" states, what rides alongside a channel-message opens no message of its own, so there is no opening for this rule to classify — it travels inside a message that already carries its own token. The full authoring and execution mechanics of each format stay with the callers; this engine holds the two formats, the rule for telling them apart, and the buffer's definition below — when-to-use policy stays with the caller.

## The architect's buffer

The pair shares one working memory: the architect's buffer, a file at `.ai-factory/notes/<NN>-architect-buffer.md`, numbered like the other temporary notes in that directory so that several architects coexist without colliding. This engine is the home of that path and that numbering; the architect's own skill points here rather than restating them.

The buffer has two zones, and the split is load-bearing. The **settled** zone — the working discipline, the rulings the user has made about how the pair works, the method learned from repeated failure, and the register of where the skills still lag the practice — is held by both halves: the editor reads it as its own working context from the head it is the hand of, not as an outsider glancing at private notes, which is what lets an order name meaning instead of restating the discipline every time. The **live** zone — the editor's handle, the architect's current read of an open question, a diagnosis still forming — is the architect's alone: a hand that already holds the head's conclusion returns an echo where an independent reading was wanted, and an independent reading is the only reason to ask for one.

The editor re-reads the settled zone when it changes, not once at birth — and the same rule covers being named a different buffer's path outright by its architect: either way the memory has moved, and the hand adopts what it is now told, replacing what it held, holding one memory at a time.

A channel-message the architect is already sending may carry, alongside its payload, what keeps the hand current: a fact about where the shared memory sits — that the settled zone has moved, or the buffer's path itself — or what the hand needs in order to work at all. This opens no message of its own and takes no form of its own; it rides inside a message that already opens with its own token. It is never a reading of the payload: no finding, no conclusion, no verdict about what the message carries — what crosses for an independent reading still reaches the hand undisturbed, and a fact about where the memory sits carries no reading of it.

A ruling recorded in the buffer is a debt against the skill, not a record of one. It leaves the buffer when it reaches the artifact that should hold it; without that drain the buffer accumulates decisions everyone follows and no artifact states.

Two architects are two heads, and a head that reads another's memory is no longer holding its own. Several architects coexist under the numbering above, and each keeps its own buffer: no architect reads another architect's buffer. An editor reads only its own architect's buffer — the memory of the head it is the hand of — never another architect's, settled zone included.
