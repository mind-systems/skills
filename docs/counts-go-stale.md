# counts-go-stale — a census rots, a contract does not

A number in a durable artifact is one of three things, and only one of them is a defect. Telling
them apart is the whole rule; the campaign against numbers that the distinction is sometimes
flattened into costs more than the numbers ever did.

**Contract — keep.** A member set with its signatures, a pinned literal, a type name, a scope
decision — even one that concerns many files. These are what the artifact is for.

**Census — remove.** How many call sites there are, how they spread across files, how many files a
sweep will touch. A census is true at the moment of writing and false as soon as any sibling task
lands.

**Measurement — keep, dated.** A test run, a probe, a timing. An experiment is true for its date and
is re-run on sight; it is not a position address and it does not rot, because it never claimed to
be current.

## The test, in one sentence

A number stays where **the sentence would still read true after someone adds a member without
touching it.** A pair named in the same sentence that counts it cannot drift — "both doors", "the
two gateways" — and stripping the count there loses precision for nothing. A census cannot pass this
test by construction: adding a member is exactly what falsifies it.

## What a census costs, measured

`tradeoxy_core`'s corpus carries every form of it. A phase record said "seven codes" and a task
record "four defects" — neither names which, and both were struck. A spec enumerated a lint rule's
targets as "nine files" and a sibling task removed one before that rule was ever written, so the
spec asserted a false number from the moment its neighbour landed. A plan listed the files a
compiler would report; the list was accurate when written, stale when the phase's earlier tasks
landed, and three successive readings spent themselves auditing it.

## The worse failure is reconciling one

**Never re-measure a count, never reconcile two counts, never fail anything on arithmetic.** A
sweep pinned at one figure and re-run at another, one apart, consumed a round of review and ended
"named, not resolved" — and the question that would have closed it in a minute was never about the
figure: *which file does the rule cover that the enumeration lacks?* Membership is answerable and
actionable; a discrepancy in a total is neither.

Where a number reads as an order of magnitude, read it as one. "Two lines change" means *this is
small*. "Five documents change" means something is wrong with the task's shape — and that, not the
arithmetic, is the signal worth acting on.

## Its kinship, and its boundary

A census is a position address in the time dimension: it addresses a set by its size at one
instant, and it rots unreported, exactly as `file:line` rots in space —
[reference-by-name](reference-by-name.md) is the spatial case. But the kinship stops there. What
the position rule forbids is a reference that stops resolving; it says nothing about quantity, and
growing it into a prohibition on numbers is the churn this document exists to prevent.

## Why this is written down here

The distinction above was derived independently in three architects' private buffers, in three
different projects, each time after a human asked for it, and each version drifted from the others —
because a buffer is by design not read by any other architect, so a rule that lives only there can
never converge. This is its first home outside one head.

## The check

Ask of a number: **contract, census, or measurement?** Keep the first, date the third, delete the
second and write what the set is instead. And if two counts disagree, do not reconcile them — ask
which member is missing.
