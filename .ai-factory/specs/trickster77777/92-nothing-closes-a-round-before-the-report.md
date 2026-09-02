# agent-architect: nothing closes a round before the editor's report exists

The skill states a reconcile step and a work-order-authoring step, both keyed
to a report that already exists — and states neither by way of a rule that
says what may not happen before one. The ordering a reader takes away is an
inference from where the sentences sit, not a written invariant, and an
inference is exactly what a compact or a hurried round drops first.

## Current state (grounded, read fresh)

`src/skills/agent-architect/SKILL.md:76-79`, inside `## Relay on the marker;
author a prompt in exactly one case`:

> "...part, never a mere pass-through. Once the editor's report returns,
> reconcile your independent read against it: concede where the editor's
> catch is sharper and say why, hold where the principle says so and say why,
> and show the user both your own read and a summary of the editor's."

`src/skills/agent-architect/SKILL.md:149-150`, inside `## Review in parallel,
reconcile before the apply order`:

> "Draft the apply work-order only for what survives reconciliation, and only
> after the user's explicit go."

Both passages describe the step that follows a report — reconciling against
it, drafting the work-order out of what survives reconciliation. Neither
states a prohibition on what may leave before a report exists. The sequence
"report, then reconcile, then release" is what a reader infers from reading
top to bottom; nothing in the file asserts it as a standing rule the way the
file asserts other invariants explicitly (e.g. the marker's own
unconditional-forwarding rule, `:93-96`). An inference from exposition order
holds only as long as the exposition is read in full and in order — which a
compact interrupts and a hurried round skips.

## Why the narrow form fails

A rule phrased as "no early summary" only closes the channel a summary
travels through — the one addressed to the user. It leaves the round
closable by an apply work-order sent alongside the relay, because a
work-order settles the target as finally as a verdict does: once it reaches
the editor, the round's outcome is decided, whether or not anything was ever
said to the user. A work-order is not a lesser closing act because it is
addressed to the editor rather than the user — where a round is settled is
what counts, not who reads the artifact that settles it. This is why the
formulation below names three artifacts — summary, verdict, apply work-order
— rather than one: naming only the user-facing artifact reproduces exactly
the gap a narrower rule leaves open.

## The reason the rule protects

The editor's parallel pass has diagnostic value only for as long as it runs
independently of the architect's own conclusion. Once that conclusion has
been released — to the user as a summary or a verdict, or to the editor as a
work-order — the editor's own report can no longer be told apart from an
echo of it: agreement stops being evidence of anything, because there is
nothing left for the editor to have reasoned to on its own. This is the
mechanism the reconcile step depends on for its entire value, and it belongs
in the shipped skill text as the rule's own stated reason, not left as
something a reader has to reconstruct from why reconciliation is described
at all.

## The change

One standalone `##` section, inserted between `## Relay on the marker; author
a prompt in exactly one case` and `## Review in parallel, reconcile before
the apply order`, with this exact text:

```markdown
## Nothing closes a round before the editor's report exists

A round opens when a channel-message goes out and closes when the editor's
report on it comes back. Between those two moments nothing that closes the
round leaves your hands — not a summary of the payload, not a verdict on it,
not an apply work-order. Your own parallel pass runs through that window
exactly as it always does: what waits is the announcement, never the work.

An apply work-order closes a round as finally as a verdict, and it does so
even though it is addressed to the editor rather than the user — where the
round is settled is what counts, not who reads it. A relay and its work-order
sent in one message therefore close the round before any report could exist:
the same violation as an early summary, never an exception to it.

The reason is the editor's independence. Its pass is signal only while it is
uncontaminated by yours; once your read has been released in any form, its
agreement can no longer be told from an echo, and the second reading you were
waiting on returns nothing. Holding the announcement is what keeps the
reconcile step worth doing.
```

## Why the heading, not a paragraph

The rule must survive a thinning pass over this file, and a named `##`
section can only be lost by deleting the heading itself — a reader or an
editor doing a pass for length has to notice and remove it deliberately. A
paragraph folded into an existing section can be absorbed or trimmed as part
of tightening that section's prose without anyone having to decide to drop
the rule specifically. The section's placement — before `## Review in
parallel, reconcile before the apply order`, not inside it or after it — is
equally deliberate: the rule governs every `::` relay, not only a
review-shaped target, so it sits with the general relay mechanics it
constrains and closes them, rather than living inside the review-specific
section where a reader could take it as scoped to review.

## Files & types

- edit: `src/skills/agent-architect/SKILL.md` — one insertion, a new `##`
  section at the boundary between `## Relay on the marker; author a prompt in
  exactly one case` and `## Review in parallel, reconcile before the apply
  order`. No existing section's text is altered.

## Guards

- **Additive only.** The `::` marker mechanics, the before-mark/after-mark
  split, the enrichment gating, the skill-expansion rule, and the two
  channel-message formats (`REPORT-ONLY` / `APPLY-EDIT`) stay byte-identical
  — this task inserts one new section and touches no existing sentence.
- **No existing sentence is amended to carry this rule as a clause** — it is
  a standalone section with its own heading, never folded into the reconcile
  paragraph or the work-order-authoring paragraph it constrains.
- `editor.md` and `architect-editor-engine` are untouched — the rule governs
  only what the architect releases and when; neither the editor's own
  discriminator nor the engine's two channel-message formats change.
- The new section's text narrates no history — no incident, no "this was
  broken", no "previously" — it states behavior and its reason only, matching
  the register of every other section in this file.

## Verification

- Manual read: a `##` section titled "Nothing closes a round before the
  editor's report exists" exists between `## Relay on the marker…` and
  `## Review in parallel…`, with its own heading (not a paragraph inside
  either neighboring section).
- Manual read: the section names all three closing artifacts — summary,
  verdict, apply work-order — explicitly.
- Manual read: the section states the work-order closes a round "as finally
  as a verdict" despite being "addressed to the editor rather than the user."
- Manual read: the section states its own reason (independence as the source
  of the editor's pass being signal, not echo) rather than leaving it
  implied.
- `grep -n "^## " src/skills/agent-architect/SKILL.md` → the new heading
  appears, positioned between the two named sections.
- `git diff --stat` shows exactly one file changed, and `git diff` shows only
  an insertion — no line in any existing section removed or reworded.
