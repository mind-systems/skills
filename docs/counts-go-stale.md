# counts-go-stale — a measurement rots, a decision does not

A number in a durable artifact is one of two things, and only one of them is a defect. Telling
them apart is the whole rule; the campaign against numbers that the distinction is sometimes
flattened into costs more than the numbers ever did.

**A decision — keep.** A number someone chose: a budget, a timeout, a pinned literal, a named pair.
It is what the artifact is for.

**A measurement of the current tree — remove.** How many call sites, how many files a sweep
reaches, how many tests a suite holds, a timing, a probe's result. It is false as soon as a
neighbour lands, and a date does not help: a reader takes the figure as true now. Write what
produces it instead — the suite's name, the symbol, the search.

## The test, in one sentence

A number stays where **the sentence would still read true after someone adds a member without
touching it.** A pair named in the same sentence that counts it cannot drift — "both doors", "the
two gateways" — and stripping the count there loses precision for nothing. A measurement cannot pass
this test by construction: adding a member is exactly what falsifies it.

## Why an agent suffers

People do not talk to each other in numbers, and where they do, nobody holds anyone to the figure.
For an agent a number is an authority: it gets copied, checked, reconciled and failed on.

A spec recorded the gate it was written against, dated to a commit, with the suite's test count.
The plan took that count as its baseline and computed an expected total. A neighbouring task landed
first and added a case; the plan's review failed on the arithmetic, the only issue left open. The
date did not protect it.

## The worse failure is reconciling one

**Never reconcile two counts, never fail anything on arithmetic.** The question that closes a
disagreement is about membership, never about the figure: *which member does one list have that the
other lacks?*

Plain words carry size: "a couple of places change" means *this is small*, and no one checks it for
exactly two. A figure that does appear is read as an order of magnitude — "five documents change"
signals something wrong with the task's shape, and that, not the arithmetic, is worth acting on.

## Its kinship, and its boundary

A measurement is a position address in the time dimension: it addresses a set by its size at one
instant, and it rots unreported, exactly as `file:line` rots in space —
[reference-by-name](reference-by-name.md) is the spatial case. But the kinship stops there. What
the position rule forbids is a reference that stops resolving; it says nothing about quantity, and
growing it into a prohibition on numbers is the churn this document exists to prevent.

## Why this is written down here

The distinction was derived independently in several architects' private buffers, each time after a
human asked for it, and each version drifted from the others — a buffer is by design not read by any
other architect, so a rule that lives only there can never converge. This is its first home outside
one head.

## The check

Ask of a number: **a decision, or a measurement of the current tree?** A decision is written. For a
measurement, write what produces it. And if two counts disagree, ask which member is missing.
