# Plan: 40.3 — `editor.md` drops the false equation between `REPORT-ONLY` and a relay

## Context
`src/agents/editor.md`'s round-type paragraph defines a `REPORT-ONLY` channel-message as "a relayed analysis target — the architect forwarding the user's own payload, worked independently", and § "Analysis mode: reason independently" tells the editor to reason "exactly as if the user handed it to you directly". Both clauses were written for the relayed case only; `src/skills/agent-architect/SKILL.md` (§ starting "You author your own prompt in two cases") now names a `REPORT-ONLY` round the architect authors on its own initiative, "carrying no relayed user payload". This task rewrites those two sites in `editor.md` so the format is described by what it is — an analysis target, worked independently — with its origin unstated, and nothing else moves.

Grounded read (fresh):
- Round-type paragraph, current text: "Each round is either a `REPORT-ONLY` channel-message (a relayed analysis target — the architect forwarding the user's own payload, worked independently) or an `APPLY-EDIT` channel-message (a decided apply work-order — the architect's own, pinned instruction). Tell which strictly by which of the two format tokens literally opens the message — …"
- § "Analysis mode: reason independently", current text: "A relayed message — a review, decompose, judge, hazard-hunt — carries no architect framing: no findings, no checklist, no verdict for you to confirm. Reason over the target yourself, from the ground up, exactly as if the user handed it to you directly, and report findings by fact — never by ratifying a conclusion the message doesn't actually contain."
- Sending side, for grounding only: `architect-editor-engine/SKILL.md` § "The two channel-message formats" — "**`REPORT-ONLY`** — a research relay: the receiver reads or runs the target, reasons independently, reports by fact, writes no files." Not touched.
- `grep -rn "relayed analysis target\|handed it to you" src/ docs/` hits only `src/agents/editor.md` — no other file carries either clause.

Scope note: the file's frontmatter `description:` also says "reasons independently over a relayed analysis target". The task spec names exactly two sites — the round-type description and the origin-specific phrase in the analysis-mode section — and the frontmatter is not one of them, so this plan leaves it as is. The implementer must not extend the edit there; it is a candidate for a deferred observation at review, not for this diff.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Drop the equation in the round-type description

- [x] **Rewrite the `REPORT-ONLY` parenthetical so it no longer equates the format with a relay**
  Files: `src/agents/editor.md`
  In the paragraph beginning "Each round is either a `REPORT-ONLY` channel-message (…)", replace only the parenthetical after `REPORT-ONLY` channel-message. Current: `(a relayed analysis target — the architect forwarding the user's own payload, worked independently)`. New wording must:
  - Describe the message as an analysis target, worked independently — "worked independently" survives verbatim from the original clause.
  - Say nothing about origin: no "relayed", no "forwarding the user's own payload", no "delegated" either — the spec's rule is that origin is *left unstated* because nothing downstream depends on it, so the rewrite neither names the relayed case nor enumerates both cases. E.g. `(an analysis target, worked independently)` or an equivalent that adds no origin claim.
  - Keep the contrast intact: the `APPLY-EDIT` half — `(a decided apply work-order — the architect's own, pinned instruction)` — stays byte-identical, as does everything after it in the paragraph ("Tell which strictly by which of the two format tokens literally opens the message — … treat it as `REPORT-ONLY`.").
  Guardrail: no marker, no branch, no new sentence telling the editor to behave differently by origin — the editor's conduct is identical either way; how the architect weighs the report is 40.5's and belongs in `agent-architect`, not here.

### Reword the origin-specific phrase in analysis mode

- [x] **Replace "exactly as if the user handed it to you directly" with wording that carries full independence without a user handing anything over** (depends on the round-type rewrite)
  Files: `src/agents/editor.md`
  In § "Analysis mode: reason independently", the first sentence — "A relayed message — a review, decompose, judge, hazard-hunt — carries no architect framing: no findings, no checklist, no verdict for you to confirm." — stays **exactly as written**, character for character; the spec quotes it as grounding and explicitly does not touch it. Edit only the second sentence: replace the phrase `exactly as if the user handed it to you directly` with wording that states the phrase's intent — full independence, no deference to the architect's own authority in having sent it — while making no claim that the user handed anything over (e.g. "owing the sender's authority nothing", "as if no one had read it before you", or equivalent). The sentence's surrounding parts stay: it still opens "Reason over the target yourself, from the ground up," and still closes ", and report findings by fact — never by ratifying a conclusion the message doesn't actually contain." The rewritten phrase must read as true whether the target was relayed from the user or composed by the architect itself, without naming either case.
  Guardrails — nothing else in the file moves: not § "Apply mode: apply exactly, add no scope", not the pinned-skill paragraphs, not § "The round's unit", not the frontmatter `description:` (see the scope note in Context). `src/skills/agent-architect/SKILL.md`, `src/skills/architect-editor-engine/SKILL.md`, and `docs/paired-loop.md` are not touched.

### Verify the boundary

- [x] **Confirm the two sites are the only changes and the untouched sentence is intact** (depends on both rewrites)
  Files: `src/agents/editor.md`
  Run `git diff -- src/agents/editor.md` and confirm exactly two hunks-worth of change, both inside the body: the round-type parenthetical and the analysis-mode phrase. Run `grep -n "forwarding the user's own payload\|handed it to you" src/agents/editor.md` — expected: no hits. Run `grep -n "relayed analysis target" src/agents/editor.md` — expected: exactly one hit, on the frontmatter `description:` line (out of scope, see Context), none in the body. Run `grep -n "hazard-hunt — carries no$" src/agents/editor.md && grep -n "^architect framing: no findings, no checklist, no verdict for you to confirm.$" src/agents/editor.md` — expected: one hit each on two consecutive lines (the sentence is hard-wrapped there in the file), reading as before. Confirm `git status --short` lists no file other than `src/agents/editor.md` (plus this plan's own artifacts), and that the frontmatter is untouched: `diff <(git show HEAD:src/agents/editor.md | head -12) <(head -12 src/agents/editor.md)` — expected: no output (the first 12 lines, the whole frontmatter block, are byte-identical to `HEAD`).
