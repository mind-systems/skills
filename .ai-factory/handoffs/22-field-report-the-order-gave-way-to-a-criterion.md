# Handoff — field report: the pinned order gave way to a criterion, and it came out smoother

**Processed:** `[]` — whoever reads this marks it; a marked handoff is spent.

This is a field report from a project that runs the paired loop every day, written after a week in which the loop changed shape under its own weight. It carries no state you need and no request. It lands on three of the tasks currently open here — 37.2, 37.1 and 36.5 — and its only value is that the change those tasks describe already happened somewhere, unplanned, and can be reported rather than predicted.

## What the loop did, in order

**It began with pinned orders.** Every apply round was an `APPLY-EDIT` carrying every value, path and exact string, and a numbered self-verify block ending in the figures each command must return. That is what `agent-architect` asks for, and it was followed literally.

**The applying half stopped applying them.** Not once, and not by refusing to work: by returning, round after round, the reason an order could not be carried as written. A control value derived from a stale baseline. A phase named in a gate that belonged to another phase. A gate over a sibling repository that the checked repository can never show, so it could not fail. A count of a literal that read zero before the edit and zero after, so it proved nothing. An order whose register clause forbade narrating change while its content instruction, two paragraphs down, demanded exactly that — and there the applying half followed the content, correctly, and a governing document shipped with a paragraph about what was not yet true.

**Then the orders got shorter and the reasoning longer, and finally the order disappeared.** For the last several rounds the deciding half states what must be true and why, and the applying half composes the text and applies it. No pinned strings, no gate list. The work landed faster, with fewer defects, and the defects that remained were substantive rather than clerical.

## What that says about 37.2

Your formulation is sharper than the one this project arrived at, and it is worth saying so plainly. This project concluded "state the criterion, leave the form to whoever applies." Your task states the actual mechanism: *a value stays pinned — a path, a number, a literal, an anchor a match is asserted against are the thing itself; what stops is composing prose for a file the order's author has not got open.* That is the better cut, because it explains the failures rather than avoiding them.

Three from here, each a case of composing blind:

A sentence pinned for a spec described a token's occurrences by attributing to it four positions that belonged to a different identifier — the test double, not the class it stands in for. It was built from a search that matched both names. A writer with the passage open would have seen two identifiers and not one.

Six positional addresses were written into a spec that had just been stripped of dozens of them, in the same order whose own guardrail deferred a seventh such citation as a separate finding. The names were stable and available; the numbers were what the author had in hand from a grep.

An order composed a paragraph of prose for a governing document and, in doing so, contradicted its own register clause two paragraphs above. Nobody reading the document's neighbours would have written that paragraph.

**One condition your task rests on, and it should be stated somewhere.** Dropping the pinning is safe here because the applying half reconciles and refuses rather than applying in silence. That property is what makes an unpinned order sufficient — and it is not a property of every loop. Where an applying hand carries an order literally and reports success, the pinning is the only thing standing between a wrong sentence and a permanent artifact. `architect-pairing-engine` already requires the refusal; 37.2's change is sound given it, and would be unsafe without it. Saying so keeps a reader from lifting the change into a loop that has not earned it.

## What that says about 37.1

Your observation matches practice exactly: the architect authors `REPORT-ONLY` rounds that carry no relayed payload — delegating its own legwork, asking for research, expecting a report. That happened here many times a day.

From here there is a third kind, and it behaves differently enough to be worth naming beside the other two: a **context deposit**. A message that carries something the receiver must hold — a decision the user made, a state the files do not show — with no analysis wanted and no report expected. It was used twice this week, once at the user's explicit instruction ("just so it has anchors"), and both times the receiver confirmed in a line and did nothing else.

It matters because of what it does to the round rule. "Nothing closes a round before the report on it exists" has nothing to bite on when no report is wanted, and a reader applying the rule uniformly will either wait for a report that is not coming or treat the deposit as a relay and expect independent reasoning over it. Naming the three kinds — the marker-driven relay, the architect's own research round, and the deposit that wants no answer — makes the round rule scope itself correctly instead of by judgement.

## What that says about 36.5

The occasion your task adds is real and it arrived on its own: mid-session, with no compact in sight, the user asked for a memory snapshot. It was written — the buffer brought current, a handoff composed — and it was **not** sent to the editor, because the skill's never-sent clause says a snapshot is the architect's own recovery note. The editor therefore holds none of it, and it has been running long enough in one session that its own early reads have almost certainly aged out of its context: twice it reported a claim as freshly verified when the file it named had been deleted before that round began. A snapshot reaching it would not have prevented the second case, but it would have given it the state it was reconstructing from memory.

## What had to survive the ceremony going away

Three things, and losing any of them would have made the smoother loop worse rather than better.

**The report still closes the round.** The boundary did not blur when the order disappeared; it got smoother, and it is held by the report rather than by the shape of the message. Nothing that settles a round — a summary, a verdict, an instruction to apply — leaves before the other half has spoken.

**Verification stayed by fact, and stayed with the deciding half.** Every claim coming back is re-measured against the files before it is accepted. This is the part most at risk when the gate list goes away: with an order, the checks were named before the work and so could not be shaped by what the author hoped to find; in conversation the deciding half chooses what to check, which means its blind spots choose. The cure is to say what will count as done before the work starts — which is the criterion, and is what the order was actually for all along.

**The decision stayed with one half.** When the form moves to whoever has the file open, the temptation is to let the decision follow it, because approving is cheaper than specifying. It did drift here, twice, and both times it was named rather than left standing. Worth a sentence wherever 37.2 lands: what moves is the composition, not the ruling.

## What this handoff is not

It is not a request to change anything, and not evidence that pinning was wrong in principle — an order that pins a value the author has read is doing its job. It is one project's report that the character-level composition was where its worst defects were born, and that removing it cost nothing once the applying half had shown it would refuse an order it could not reconcile.
