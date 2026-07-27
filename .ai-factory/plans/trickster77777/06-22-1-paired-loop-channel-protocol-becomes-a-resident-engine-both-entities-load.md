# Plan: 22.1 — paired-loop channel protocol becomes a resident engine both entities load

## Context
Extract the architect↔editor channel's output contract into a new thin global engine `architect-editor-engine` that both entities load at birth, holding only the two channel-message formats (REPORT-ONLY, APPLY-EDIT) and the rule that a receiver keys its mode off the token literally opening each message — so the contract travels with the pair into other projects where this repo's docs are absent.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: The engine

- [x] **Task 1: Create the `architect-editor-engine` engine skill**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  Create the new leaf engine. Follow the thin-engine shape of `src/skills/test-philosophy/SKILL.md` (pure content, no procedure, load-once + reverse-graph marker paragraph, matching register).
  Frontmatter:
  - `name: architect-editor-engine` (must match directory name)
  - `description:` (≤1024 chars) stating it is the shared channel-message-format contract for the architect↔editor pair — the two formats and the rule that a receiver keys mode off the opening token; carries no `::` grammar and no policy.
  - `user-invocable: false`
  - `disable-model-invocation: false` (engine baseline — never `true`)
  - `allowed-tools: Read`
  - **No `loads:` field** — it is a leaf engine with no callees.
  Body (thin, self-describing) holds only:
  - The **REPORT-ONLY** format: a research relay — the receiver reads/runs the named target, reasons independently from the ground up, reports by fact, and writes no files. Used for every relayed analysis target and every relayed skill-expansion.
  - The **APPLY-EDIT** format: the pinned apply work-order — exact edits, guardrails (what not to touch; a collision-safe method where order matters), the commands to self-verify, and an explicit do-not-commit. Used only for the architect's own authored, confirmed change.
  - The mode rule: a receiver keys its mode strictly off **the format token that literally opens the message** (`REPORT-ONLY` / `APPLY-EDIT`) — never off content, never off a referenced skill's own default behavior; ambiguity (no recognizable token) resolves to REPORT-ONLY. Treat `REPORT-ONLY` / `APPLY-EDIT` as byte-exact protocol tokens, on the same axis as `PLAN_REVIEW_PASS`.
  - An explicit statement that the engine holds nothing about `::` — how the architect parses raw user input stays entirely with its caller.
  - The standard load-once + reverse-graph marker paragraph, whose grep line names **all three** caller sources (this is the one engine in the family with an agent caller):
    `` grep -l "architect-editor-engine" src/skills/*/SKILL.md src/commands/*.md src/agents/*.md ``

### Phase 2: Wire the two callers

- [x] **Task 2: Rewrite `agent-architect` to load the engine and restate its `::` grammar in the engine's terms** (depends on Task 1)
  Files: `src/skills/agent-architect/SKILL.md`
  - Frontmatter: add `loads: architect-editor-engine` **and** add `Skill` to `allowed-tools` (L13 today is `Read Grep Glob Bash Write Edit AskUserQuestion Agent SendMessage` — no `Skill`). The `loads:` field is only the forward-graph declaration; the Skill tool performs the actual runtime load, so it must be pre-approved — every engine-loading skill in this repo pairs the load instruction with `Skill` in `allowed-tools`. Without it the "load at birth" guarantee silently fails while the `loads:` grep still passes.
  - Add an instruction (alongside the existing "Spawn once, message thereafter" discipline) to ensure the engine is loaded once this session via the Skill tool, only if not already loaded.
  - Rewrite the `::` grammar in the `## Relay on the marker; author a prompt in exactly one case` section (currently L54–107) **in place**: the marker never *opens* the message (a leading slash-command is preserved exactly as today) but may **trail or split mid-message**; everything before the mark is the payload worked by **both** the architect and the editor in parallel, then reconciled — the architect performs its own part, not a mere relay; everything after the mark is for the architect alone, and name the enrich pattern there (the architect enriches the before-mark payload with named context from its own chat before sending it on).
  - **Revise the "add nothing of your own" paragraph (currently L58–61)** so it no longer contradicts the new enrich+parallel model, while retaining the anti-contamination property it protects. State the boundary explicitly: enrichment supplies **named context** (paths, values, the target of a pronoun from the architect's own chat) — never **findings, verdict, method, checklist, or a collision-hint**. The editor still reasons over the payload independently from the ground up, so its agreement remains real signal, not manufactured echo. Enriching with context and injecting conclusions are different acts; the rewrite keeps the second banned. Do not delete the anti-echo guarantee wholesale.
  - Rewrite the relay-expansion transformation (currently the `"apply it with arguments"` skill-expansion at L76–87) to emit a **REPORT-ONLY**-formatted message: "read and run `<SKILL.md>` with arguments … as a report; write no files."
  - Reframe the "author your own prompt in exactly one case" paragraph (L89–98) as authoring an **APPLY-EDIT**-formatted message. Keep the apply-work-order authoring mechanics behavior-identical (pin every value/path/guardrail, self-verify commands, explicit do-not-commit) — only the framing changes.
  - **Rework the scope-question carve-out (currently L100–107) in place too** — it occurs inside the L54–107 span and is keyed twice on a user reply "ending with `::`" (L102, L106); under the mid-message-split model this trailing-only phrasing is stale and also carries the second occurrence of the retired phrase. Restate it in the new split-marker terms (a marked reply reaches the editor; an unmarked one is the architect's to hold), preserving the same discipline: the architect carries a flagged scope question to the user verbatim and never resolves it itself.
  - Reframe the `## Review in parallel, reconcile before the apply order` section (L109+) as an explicit special case of the general before-mark-both-entities rule; **keep** its review-specific discipline intact (adversarial, name the specific plantable failure, hunt propagation gaps, concede/hold on reconciliation) — do not dilute it.
  - Retire the three exact phrases so verification greps return zero hits: "ending with `::`" (**both** occurrences — L56 and L102), "literal payload text", "apply it with arguments".
  - Leave `## Verify the editor's report by fact` behavior-identical apart from APPLY-EDIT framing. Preserve register — targeted rewrites of the existing voice, not a wholesale rewrite.

- [x] **Task 3: Rewrite `editor.md` to load the engine on spawn and key its mode off the two tokens** (depends on Task 1)
  Files: `src/agents/editor.md`
  - Add a body instruction (not a frontmatter `loads:` — agents carry no such field) directing the editor to load `architect-editor-engine` via the Skill tool as the **very first action on spawn**, before processing the first channel-message. (`Skill` is already in the `tools` list — do not change frontmatter tools.)
  - Rewrite the opening mode-tell paragraph (currently L18–22) to key strictly off which of the engine's two format tokens (`REPORT-ONLY` / `APPLY-EDIT`) opened the message, replacing the current content-based "tell which by what arrived" framing.
  - Add a hard report-only default under the pinned-skill-path paragraph (currently L43–48): a pinned skill's own write-capable default never by itself promotes a round to APPLY-EDIT — only an explicit `REPORT-ONLY` vs. `APPLY-EDIT` token on the message decides mode, and any ambiguity defaults to REPORT-ONLY, full stop (the same way auth-ambiguity already defaults to no-authorization elsewhere in this file).
    DEVIATION: plan said to phrase this "the same way auth-ambiguity already defaults to no-authorization elsewhere in this file" / file showed no such auth-ambiguity precedent anywhere in `editor.md` (grepped, zero hits) / done: stated the REPORT-ONLY-on-ambiguity rule directly, without the ungrounded back-reference.
  - Preserve register — targeted rewrites, not a wholesale rewrite.

### Phase 3: Activate

- [x] **Task 4: Add the `active/` symlink for the engine** (depends on Task 1)
  Files: `active/skills/architect-editor-engine`
  Create the symlink following the established pattern (confirmed against `note`, `roadmap-engine`, `test-philosophy`):
  `ln -sfn ../../src/skills/architect-editor-engine active/skills/architect-editor-engine`
  Without it neither caller can resolve the skill via the Skill tool. Verify: `ls -la active/skills/architect-editor-engine` resolves to `../../src/skills/architect-editor-engine`.

## Guards (from spec — do not violate)
- `reserved-words.md`, root CLAUDE.md, and everything under `docs/` are untouched by this task.
- The engine frontmatter stays at the engine baseline — `user-invocable: false`, `disable-model-invocation: false` — never `true`.
- `::` parsing stays entirely inside `agent-architect`; the engine carries zero `::` grammar and zero policy.
- `REPORT-ONLY` / `APPLY-EDIT` are byte-exact protocol tokens in both callers' operative text — not prose to paraphrase.
