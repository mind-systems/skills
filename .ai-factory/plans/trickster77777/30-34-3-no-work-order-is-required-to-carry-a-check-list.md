# Plan: 34.3 — no work-order is required to carry a check list

## Context
The apply work-order's required "self-verify commands" component is dropped from the three files that prescribe it, leaving the architect's own post-round file check (`agent-architect` § "Verify the report by fact") as the single check on a landing, and the editor's diff read-back as its self-verification.

Every edited paragraph is pinned below as a fenced block holding the exact post-edit text, hard-wrapped as it must land. Replace the named line span with the block's contents verbatim — nothing in these three files is re-wrapped by judgment.

All line spans are **pre-edit coordinates**, read off the files as they stand now. Where one file takes two span replacements and the first changes its line count, apply them bottom-up — the lower span first — so no span moves under another; each task below states its own order.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Drop the component at its three homes

- [x] **Remove the self-verify component from `agent-architect`'s apply-work-order list**
  Files: `src/skills/agent-architect/SKILL.md`
  The paragraph at lines 155–161 opens "You author your own prompt in exactly one case" and its `APPLY-EDIT` list carries four components; delete the third — `the commands the editor runs to self-verify before reporting;` — leaving three: pinned values, guardrails, and the explicit "do not commit". Replace lines 155–161 with exactly:

  ```
  You author your own prompt in exactly one case: the **apply work-order**, once
  the user has confirmed the edits. Send it as an `APPLY-EDIT` channel-message:
  pin every value, path, and exact string it needs; state the guardrails — what
  NOT to touch, a collision-safe method where order matters; and an explicit
  **"do not commit."** Leave the mechanical steps to the editor — it does the
  obvious unprompted, and over-told steps only drift.
  ```

  Guards: no replacement component is added, and the editor's diff read-back is not named here — the list simply names one fewer thing. § "Verify the report by fact" is not touched — addressed by name, since this edit shifts the lines below it by one; after this task it is the only check on a landing. No prose in this file numbers the list ("four"/"three"), so nothing else moves; frontmatter, `loads:`, and the `description:` field are unchanged.

- [x] **Remove the same component from both `architect-pairing-engine` enumerations**
  Files: `src/skills/architect-pairing-engine/SKILL.md`
  Two edits in § "The deciding half", in lockstep with the above. Both spans are pre-edit coordinates and edit (1) shortens the file by one line, so **apply (2) first, then (1)** — bottom-up, so neither span moves under the other. (1) Replace lines 35–42 with exactly:

  ```
  Its editor becomes research-only: every `REPORT-ONLY` relay still reaches it
  exactly as the generic discipline has it. No `APPLY-EDIT` work-order does —
  the architect still authors the apply work-order exactly as today: same
  format, the same pinned values, guardrails, and the explicit "do not commit."
  But it addresses that work-order to the paired architect and delivers it
  through the user, who carries or confirms the relay. The applying architect
  is the one that acts on shared artifacts, not this half's own editor.
  ```

  (2) Replace lines 44–48 with exactly (this is the edit to apply first):

  ```
  Because that delivery is a human copy-paste and not a `SendMessage` call,
  the work-order ships as one single code block — every pinned value,
  guardrail and the "do not commit" inside it — so the user can copy it
  whole and relay it unmodified. Never split it across several blocks or
  interleave prose between them.
  ```

  The deleted spans are `self-verify commands, ` in (1) and `, self-verify command` in (2) — each takes its adjoining comma with it, which is what the pinned blocks show. Guards: the single-code-block rule itself, the spawn-trigger departure, and § "The applying half" are unchanged; the straight quotes around `"do not commit."` are preserved (this file carries no curly quotes).

- [x] **State the editor's apply-mode verification as the diff read-back**
  Files: `src/agents/editor.md`
  In § "Self-verify, flag every judgment call, escalate ambiguity", the paragraph at lines 73–83 currently opens "Before you report, make the claim true, not just plausible: run the work-order's own verify commands and read the diff back in apply mode". The diff read-back becomes unconditional and a verify command is run only where the order pins one. Replace lines 73–83 with exactly:

  ```
  Before you report, make the claim true, not just plausible: read the diff
  back in apply mode, running a verify command only where the work-order pins
  one; re-check your findings against the target once more in analysis mode.
  Never close with a bare "done" — state what you found or changed and paste
  the verification output. Explicitly surface anything you had to decide that
  the round didn't pin — an unflagged judgment call is the one thing the
  architect's file-check can miss. If a round is underspecified, contradicts
  itself, or would break something unintended, flag it back rather than
  guessing; if you catch it outright wrong (a stale reference, a mismatched
  value, an unaccounted collision), fix it and say so explicitly — never
  silently deviate and let the architect discover the difference later.
  ```

  Only the first sentence's apply-mode clause changes; every word from "re-check your findings" to "difference later." is byte-identical to the current text, re-flowed across the same eleven lines. Apostrophes stay ASCII (`didn't`, `architect's`). Guards: the section heading keeps the word "Self-verify"; the `description:` frontmatter ("self-verifying and reporting back by fact either way") is unchanged; "paste the verification output" is unchanged and stays true of the diff read-back.

### Confirm the blast radius stayed closed

- [x] **Leave `architect-editor-engine` untouched and confirm no fourth home remains** (depends on all three edits above)
  Files: `src/skills/architect-editor-engine/SKILL.md` (read-only)
  `architect-editor-engine`'s `APPLY-EDIT` line — "the receiver makes exactly the edits specified, self-verifies, and does not commit" — is deliberately unchanged: reading the diff back is the self-verification it names, and editing a format engine to carry policy would cross the tiering in `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy". Do not edit this file.
  After the three edits, sweep the product surfaces for the prescription that was removed — `grep -rni "self-verif" src/ docs/` — and expect exactly three hits (the `-i` is load-bearing: one of the three is a capitalized heading, and a case-sensitive sweep returns two and reads a clean landing as a defect), all of them the word standing for a step that still happens rather than a component a work-order must carry: `src/agents/editor.md` `description:`, `src/agents/editor.md`'s section heading, and `src/skills/architect-editor-engine/SKILL.md`'s `self-verifies`. Do **not** sweep for `verify command`: `editor.md`'s new body sentence keeps that phrase by design ("running a verify command only where the work-order pins one"), so a zero-expectation on it would only pass by reversing the task above.
  Working artifacts under `.ai-factory/` — the roadmap line, architect buffers, handoffs, prior plan-reviews — are history and are not edited; no already-written work-order is retracted. `active/skills/agent-architect`, `active/skills/architect-pairing-engine` and `active/agents/editor.md` are live symlinks into `src/`, so all three edits go live with no `active/` work.
