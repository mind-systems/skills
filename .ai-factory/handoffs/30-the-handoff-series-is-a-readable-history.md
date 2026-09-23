# Handoff — the handoff series is a readable history

**Processed:** `[ ]` — whoever reads this marks it; a marked handoff is spent.

A short one, because the finding is short.

A project's `.ai-factory/handoffs/` is usually treated as a stack of notes, each written to be read
once and forgotten. It is also, without anyone having designed it that way, a history: the files are
numbered in sequence, each names the stretch it covers, and each cites the architect buffer it
belongs to. Read in order they tell how the work moved — who held it, what it was doing, why it
turned where it did — and nothing else in a repository holds that. Git shows what changed, specs
show what was decided; only this series shows how the pair got from one to the other.

The buffer's file name is what makes it navigable. Buffers are per-architect, so a buffer name
filters the series down to one head's tenure: in `tradeoxy_core`, nine handoffs cite
`130-architect-buffer.md`, and they are exactly that architect's life, twelve days of it. The
buffers before it — ten of them, most living a day or two — show a pair that used to be re-founded
constantly, which is itself the most interesting fact about the project's history and is visible
nowhere else.

So the memory is loadable at three depths: one file for a stretch, a run of them for a season, the
whole line for the arc. A reader picks the depth the question needs, which is the opposite of
loading a repository's whole past to answer something narrow.

Two things break it. A stretch that leaves no handoff at all leaves no trace of itself — the series
is only as complete as the occasions on which someone wrote. And the directory mixes genres: the
architect's own snapshots sit beside outbound handoffs written for readers in sibling repositories,
which belong to a different lifetime and dilute the series when it is read as one.

What to do with this: say it in `agent-architect` and in `command-handoff`, so that whoever writes a
handoff knows it will be read twice — once by the next agent, and once by someone reconstructing the
path — and so that whoever needs the path knows the series exists and how to filter it.
