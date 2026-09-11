# A delegated round's report is an echo, not signal, and the skill says so

## Current state (grounded, read fresh)

`docs/paired-loop.md` § "The user's marker" states two different weights for two different kinds of answer: "When the user's payload is relayed, the editor reasons over it from the ground up and its agreement is signal, reconciled against the architect's own read. When the head delegates its own work, there is no second opinion in the result — it is a hand, and treating its agreement as corroboration mistakes an echo for evidence."

`src/skills/agent-architect/SKILL.md` names the delegated case — "a `REPORT-ONLY` round on your own initiative, delegating your own legwork — a message you compose yourself, carrying no relayed user payload and asking for no edit" — but states a weighing rule for only the other kind: "This reconcile step applies to every before-mark relay, not only a review-shaped one." Reconcile, by its own text, is what happens to a *relay's* report against the architect's own independent read; nothing says what a delegated round's report is, or is not, once it comes back. The governing spec's rule that its agreement is an echo, not evidence, has no sentence of its own anywhere in the skill.

## The change

The paragraph that names the delegated case gains the governing spec's rule beside it, worded the way the file already words this case — the architect's own delegated legwork, not a name for the round: a report on the architect's own delegated legwork carries no second opinion, because the editor did the architect's own asking, not the user's — reading its agreement as corroboration is mistaking an echo for evidence, the same way the governing spec states it. This is stated as its own fact, not folded into the reconcile-step sentence, because reconcile is what a relay gets and the architect's own delegated legwork does not; the two are different rules for different reports, not one rule with an exception.

Nothing about the reconcile step itself changes: "This reconcile step applies to every before-mark relay, not only a review-shaped one" stays exactly as written, since a delegated round was never a before-mark relay and the sentence never claimed otherwise — this task adds the missing other half, it does not correct the sentence that was already narrow on purpose.

## Blast radius

`editor.md` is not touched: how the editor's own report is weighed is the architect's own reading discipline, not an instruction to the hand that produces the report — the editor already reports "by fact" regardless of which mode produced the round, and nothing here changes what the editor writes.

`docs/paired-loop.md` is not edited — this task carries its rule into the skill, the direction this phase moves in throughout; the governing spec already states the rule this task grounds itself on.

This task lands beside the sentence naming the delegated case, in the same paragraph 37.1 authored; it does not touch the rescoped inventory paragraph beneath it, the marker-flagging paragraph, or any other section of the file.
