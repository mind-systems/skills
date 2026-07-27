# Paired-loop protocol post-review cleanup: thin the engine, fix `agent-architect` before-mark

A handoff-focused code review of 22.1's implementation (`.ai-factory/reviews/trickster77777/06-22-1-...-review-2.md` and a follow-up independent read, cross-checked against handoffs 02 and 03) found residues in two files. `architect-editor-engine/SKILL.md` shipped too heavy for what it's supposed to be — a resident, load-once "header" both entities carry, not an essay — restating its own frontmatter and re-homing `APPLY-EDIT` mechanics that already live in the callers, plus a whole section devoted to disclaiming `::` when the real fix is to never mention `::` at all. `agent-architect/SKILL.md`'s `## Relay on the marker` section has a more load-bearing problem: its enrich clause reads "you **may** enrich the payload with named context" — architect discretion — when handoff 02 §3.1 named the enrich pattern as a **user-triggered** command (`<payload> :: <"enrich this for the editor with X">`) in the same breath as the user's explicit objection to "per-architect randomness they must police every time." A bare "may enrich" is exactly that randomness, reinstated. Two structural gaps sit alongside it: the reconcile mechanic lives only inside the review-specific section, which claims to be "a specific case of" a general rule that doesn't yet contain the thing being specialized; and the skill-expansion worked example doesn't literally show the token it's supposed to model.

This task covers **two files** — `src/skills/architect-editor-engine/SKILL.md` and `src/skills/agent-architect/SKILL.md` — as one task (folded back from an initial two-task split on an orchestrator-cost argument: two tasks would make the orchestrator load the same paired-loop protocol context twice for one coherent cleanup). `src/agents/editor.md` is untouched — no finding from the review lands on it.

## Part A — `architect-editor-engine/SKILL.md`: slim to a thin `.h`-style shell, purge all `::`

### Current state (grounded, verified live today)

`src/skills/architect-editor-engine/SKILL.md`, 63 lines total (14 frontmatter + 1 blank + 48 body):

- **Frontmatter description** (L3–10) ends with the sentence to drop: "Carries no `::` grammar and no policy about when to use which format; that stays entirely with the caller." (L7–8).
- **L18–29** — intro paragraph: "This is a shared pure-content leaf engine... holds one discriminator... caller stays in control of when and what to send; the receiver stays in control of how it reasons... no I/O of its own... Load this skill once at birth..." — restates the frontmatter description before reaching the mandatory load-once/reverse-graph sentence (L23–29).
- **L31–47** — `## The two channel-message formats`: the two bullets. Each carries a full mechanics restatement (L42–47 for `APPLY-EDIT`: "every value, path, and exact string pinned; the guardrails stated... the commands to run to self-verify... an explicit do-not-commit") plus a trailing "Used for…" usage-policy sentence on each bullet (L40–41, L46–47).
- **L49–55** — `## The mode rule`: the keying rule and ambiguity default — this content stays.
- **L57–62** — `## What this engine does not hold`: an entire section whose only job is to say the engine carries nothing about `::` — the section itself names `::` twice (L59) to disclaim it.
- Frontmatter fields otherwise: `user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`, no `loads:`.

### The change

Rewrite the frontmatter `description:` to drop the `::` sentence, keeping the "holds only the two formats; when-to-use policy stays with the caller" idea:

```yaml
description: >-
  Shared channel-message-format contract for the architect↔editor paired loop.
  Holds the two channel-message formats — REPORT-ONLY and APPLY-EDIT — and the
  rule that a receiver keys its mode strictly off the token that literally
  opens each message. Holds only the two formats; when-to-use policy stays
  with the caller. Loaded once at birth by both the architect
  (`src/skills/agent-architect`) and the editor (`src/agents/editor.md`).
```

Rewrite the body to this target (~20 lines), verbatim:

```markdown
# Architect-Editor Engine — the Paired-Loop Channel-Message Contract

Load this skill once at birth — the architect via its own `loads:` frontmatter edge, the editor as the first action on spawn — so the contract is resident before any channel-message arrives. This is a load-once engine; its callers depend on its exact behavior, and the reverse graph resolves via `` grep -l "architect-editor-engine" src/skills/*/SKILL.md src/commands/*.md src/agents/*.md ``.

## The two channel-message formats

Every channel-message the architect sends opens literally with its format token — `REPORT-ONLY` or `APPLY-EDIT` — held byte-exact, like `PLAN_REVIEW_PASS`, never paraphrased.

- **`REPORT-ONLY`** — a research relay: the receiver reads or runs the target, reasons independently, reports by fact, writes no files.
- **`APPLY-EDIT`** — a pinned apply work-order: the receiver makes exactly the edits specified, self-verifies, and does not commit.

## The mode rule

A receiver keys its mode strictly off the token that opens the message — never off content, never off a referenced skill's own default. Ambiguity resolves to `REPORT-ONLY`. The full authoring and execution mechanics of each format stay with the callers; this engine holds only the two formats and the rule for telling them apart.
```

Net effect: the intro's restated framing (L18–22) is cut, keeping only the load-once/reverse-graph sentence; the two bullets shrink to a one-line definition each, dropping both the `APPLY-EDIT` mechanics restatement and the "Used for…" policy notes; `## What this engine does not hold` is removed outright — its one job (disclaiming `::`) is no longer needed once nothing in the file mentions `::` to begin with; the mode rule keeps its keying/ambiguity content and gains one closing sentence pointing full mechanics at the callers, replacing the deleted section's role without naming `::` to do it.

### Guards (Part A)

- Frontmatter fields other than `description:` are byte-identical: `user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`, no `loads:` (the engine stays a leaf with no callees).
- `agent-architect/SKILL.md` and `editor.md` — the slim removes the engine's own duplicate copy of the `APPLY-EDIT` mechanics; it does not remove or alter the mechanics' real home in either caller (Part B edits `agent-architect` for unrelated reasons; `editor.md` is untouched by this task entirely).
- Preserve the engine's existing register — a trim, not a rewrite in a different voice.

### Verification (Part A)

- `grep -n "::" src/skills/architect-editor-engine/SKILL.md` → zero hits, in frontmatter and body alike.
- `grep -niE "collision|self-verify|do not commit" src/skills/architect-editor-engine/SKILL.md` → zero hits (the `APPLY-EDIT` mechanics are no longer duplicated in the engine).
- Body line count ≤ ~22 lines.
- `grep -n "## What this engine does not hold" src/skills/architect-editor-engine/SKILL.md` → zero hits (section removed).

## Part B — `agent-architect/SKILL.md`: gate enrich, fold reconcile into the general rule, show the literal token

### Current state (grounded, verified live today)

`src/skills/agent-architect/SKILL.md`, `## Relay on the marker...` section:

- **L71–84** — the general before-mark rule: "worked **in parallel** by both entities... you perform your own part, never a mere pass-through. Before sending, you **may** enrich the payload with **named context** already resident in your own chat — a path, a value, the referent of a pronoun the user left implicit, including one named in the after-mark remainder of the same message. You add nothing beyond that: no findings, no inventory, no collision-hint, no checklist, no verdict, no method — supplying named context and injecting a conclusion are different acts, and only the first is yours to do." No reconcile step is stated here — the section ends at "real signal rather than manufactured echo" (L84).
- **L91–95** — "Where the marker splits mid-message, the after-mark remainder is yours alone — never itself forwarded — but it is exactly the kind of source an enrichment is drawn from: a clarifying path, a value, the answer to 'which one,' addressed to you so you can enrich the before-mark payload before you send it, not so you can analyze on the editor's behalf." — describes the after-mark as *a source* enrichment may draw from, not a *trigger condition* for whether to enrich at all.
- **L97–101** — the skill-expansion transformation: "expand it to skill-by-reference inside the same `REPORT-ONLY` message — 'read and run `~/.claude/skills/<name>/SKILL.md` with arguments: … as a report; write no files'" — the quoted example text does not itself open with the literal `REPORT-ONLY` token, though the surrounding prose says it's sent "inside the same `REPORT-ONLY` message."
- **L133–146** — `## Review in parallel, reconcile before the apply order`: "A review target is a specific case of the general before-mark rule above: when the relayed payload is a review, run your own review concurrently with the editor's — reaching your own verdict independently before weighing the editor's, the same working-in-parallel the payload rule already requires for any before-mark relay, just for a review-shaped target... Then reconcile: concede where the editor's catch is sharper and say why, hold where the principle says so and say why. Draft the apply work-order only for what survives reconciliation, and only after the user's explicit go. Show the user your own review and your summary of the editor's; be adversarial — name the specific, plantable failure, not a vague caution — and hunt propagation gaps, a decision taken earlier that never reached a file it should have." The reconcile/concede-hold/show-user mechanic exists only here, even though L135 calls this section a specialization of the general rule.

### The change

One concern per file region, three edits, same file:

1. **Gate enrich on an explicit after-mark instruction.** Rewrite L76–84 (and the related L91–95 framing) so enrichment happens **only** when the after-mark remainder is itself an explicit instruction to enrich — the `<before-mark> :: <"enrich this for the editor with X">` pattern, where the user names the context `X` to add. When the after-mark is anything else (a plain clarifying answer, empty, or absent because the marker trailed instead of splitting), the before-mark payload relays as-is, unenriched — no architect-initiated enrichment on its own judgment. Trim the elaboration: keep only that enrichment adds the user-named context and never a finding, verdict, or method; drop the "supplying named context and injecting a conclusion are different acts" sentence as redundant once the trigger itself is explicit and external (the user's own instruction), not a line the architect has to judge case-by-case.
2. **Move the reconcile mechanic into the general rule.** Insert into the general before-mark paragraph (after "you perform your own part, never a mere pass-through," roughly where L75–76 sits): the architect reaches its own independent read of the before-mark payload, then — once the editor's report comes back — reconciles: concede where the editor's catch is sharper and say why, hold where the principle says so and say why, and show the user both its own read and a summary of the editor's. This applies to **every** before-mark relay, not only review-shaped ones. Then shrink `## Review in parallel...` to state only the review-specific flavor on top of the (now-general) mechanic: be adversarial, name the specific plantable failure rather than a vague caution, and hunt propagation gaps — referencing the general rule by name instead of restating "run your own review concurrently... reaching your own verdict independently" and the reconcile/concede-hold/show-user steps a second time. This is a structural fold, not a cross-reference sentence bolted onto an otherwise-unchanged section.
3. **Show the literal token in the skill-expansion worked example.** Rewrite L97–101's quoted example so it literally opens with the token, e.g. `"REPORT-ONLY — read and run `~/.claude/skills/<name>/SKILL.md` with arguments: … as a report; write no files"` — consistent with the byte-exact-token rule the engine (Part A) states.

### Guards (Part B)

- `src/agents/editor.md` untouched — no finding from the review lands on it.
- `src/skills/architect-editor-engine/SKILL.md` — Part A is this task's own edit to that file; Part B makes no additional change to it.
- Everything else in `agent-architect/SKILL.md` outside the `## Relay on the marker...` and `## Review in parallel...` sections stays byte-identical — the spawn-once discipline, the apply-work-order authoring paragraph (L111–117), "Verify the editor's report by fact," the buffer section, and the closing sections are out of scope for this task.
- Preserve register — targeted rewrites of the existing voice in the affected paragraphs, not a wholesale rewrite of the section.

### Verification (Part B)

- `grep -n "you may enrich" src/skills/agent-architect/SKILL.md` → zero hits (no bare architect-discretion enrich phrasing remains).
- The enrich text explicitly names the after-mark-instruction trigger (e.g. contains the pattern `"enrich this for the editor"` or an equivalent explicit-instruction phrasing) as the sole gate.
- The general before-mark section (within the old L71–84 span) contains the reconcile/concede-hold/show-user mechanic; `## Review in parallel...` no longer restates "run your own review concurrently... reaching your own verdict independently" or the concede/hold/show-user steps — it references the general rule and states only its review-specific additions.
- `grep -n 'REPORT-ONLY — read and run' src/skills/agent-architect/SKILL.md` (or equivalent) → the worked example now opens with the literal token.

## Files & types (both parts)

- edit: `src/skills/architect-editor-engine/SKILL.md` (Part A).
- edit: `src/skills/agent-architect/SKILL.md` (Part B).

## Guards (whole task)

- `src/agents/editor.md` untouched by this task — no finding lands on it.
- `reserved-words.md`, root `CLAUDE.md`, `docs/` untouched.

## Verification (whole task)

All the Part A and Part B checks above, plus:

- `src/agents/editor.md` is byte-identical to its pre-task state (`git diff` shows no changes to it).
