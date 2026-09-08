# The census nobody takes — why a round gets spent

**Project:** tradeoxy_core
**Date:** 2026-09-08
**Written by:** the architect that decomposed Phase 46, from the same session's measurements

## What this file is

A second reading of the same week as `01-the-week-the-record-does-not-hold.md`, asking a different question. That file asks what the week cost and why the record of it does not survive. This one asks why a task needs three rounds to become shippable at all — what enters the roadmap, in what state, and what the rounds are actually spent on.

It disagrees with `01` in two places, both named below. Neither disagreement touches that file's conclusions.

## Rounds are not bought by bad design

Of the 73 slugs whose plan-reviews survive on disk, **57 of the 73 first rounds carry no critical finding at all** — the section is empty or reads "none". Only 16 carry one.

And yet 38 of those 73 needed a second round, 9 needed a third, and none ever reached a fourth.

Most second rounds were therefore bought by findings *below* critical. This is the pass bar meeting the long tail: a plan review passes only with no findings at all inside the task's boundary, cosmetics included, so a stale comment in a file the task edits ends the round exactly as a design error would. A task does not have to be going badly to run out of rounds. It only has to be imprecise in three small places, one per round.

## What the findings actually are

Nineteen round-1 findings survive in numbered form. Read together they fall into three shapes, and the shapes matter more than the counts:

**A set enumerated in part.** "The plan pins the id's new birthplace but not both of its use sites." "The plan's Settings line and its doc task account for one new terminal failure mode, but the change introduces two." "The stated migration rule does not reach `'sub-invalid-layout'`, the one fixture the plan itself identifies as most dangerous." In each, the plan names a member and the repository holds several.

**A fact restated where the code says otherwise.** "`createdAt` is the bar's OPEN time, not the 'close' — the plan says 'close' in four places." "`resolveTimeframe(config.timeframe).seconds` dereferences without the null guard the live code uses." The plan asserted from a read, and the read was wrong or shallow — then the assertion propagated to four places before anyone opened the line.

**A placement left implicit.** Where a reset belongs relative to a retry boundary; whether an acknowledgement arriving immediately after the opening message is dropped. The plan is not wrong; it simply does not say, and two readings both compile.

The three are one defect wearing three faces. A task spec is written from **a read**, and a read is a sample. Nothing in decomposition turns that sample into a counted census.

## How it enters the roadmap — measured on my own work, this session

I decomposed Phase 46 into seven tasks in the session that produced this file. Five census failures, all mine, all caught before shipping only because something else looked:

- Two anchors written from position inside a chunk I had already read, rather than counted in the same pass: `ARCHITECTURE.md:235` for a convention that sits at `:237`, and an entity's `:18` for a decorator at `:20`. The editor opened both and corrected them.
- Six tasks decomposed against `BrokerAlert` without ever opening `src/signals/signal.types.ts`, which declares a second, unrelated type of the same name. Every spec would have sent the implementer to the wrong import. Found by the editor, not by me.
- A verification gate that asserted an absolute where the intent was a delta — "`git status --short` contains no entry under `docs/`" — which could never pass, because two files under `docs/` were already dirty. Flagged by the editor rather than silently passed.
- A truncating filter used to test whether a string was present in a diff. A command carrying an output limiter cannot establish presence or absence; I re-ran it without one.

And one that is live in the tree right now: the open contract line of 39.6.2.2.2 states that `replay-rpc.spec.ts` is "1259 lines and 483 of them are order-axis". The file is **1364 lines**. The number was true when written and was never re-measured, and any plan built on it starts from a false premise about the surface it must edit.

None of those five is a reasoning failure. Every one is a measurement failure, committed while writing the artifact that the planner is then obliged to trust.

## Why the procedure does not stop it

The atomicity gate asks whether the first half could ship without the second and still make sense. It is a good question and it is the wrong one for this defect: a task can be perfectly atomic and still ship with a surface nobody counted.

The two gap classes a spec is normally swept for — an unpinned value, an undefined edge — both interrogate the artifact's own text. Neither asks what already exists around it. That is the blast-radius hole `01` names, and it is the majority of what the reviews here return.

## Why three rounds and not one

Because a review returns **instances, never the missing census**. It finds the second use site, not the fact that the set was never counted. The instance gets fixed, the round ends, and the next round finds the third. The wall at three rounds is where the budget ends, not where the set does — which is why the tasks that died at three did not die of one big thing.

## Where this file disagrees with 01

**The round distribution.** `01` reads "across the 71 slugs whose artifacts are on disk: 35 passed plan review on round 1, 27 on round 2, 9 on round 3". Counting the files present: 73 distinct slugs carry plan-reviews, with 73 round-1 files, 38 round-2 and 9 round-3 — so 35 passed at round 1, **29** at round 2, and 9 at round 3, totalling 73. The first and third buckets agree; the denominator and the middle bucket differ by two, and I cannot reproduce 71 and 27 from the files. The conclusion both readings support — three rounds is a hard wall, not a soft budget — is untouched by which count is right.

**The suite's size.** `01` calls `replay-rpc.spec.ts` "the 1259-line suite". It is 1364 lines. The figure came from 39.6.2.2.2's contract line, which is stale. The disagreement is small and the point is not: this file inherited a number from an artifact that does not own it, which is exactly the defect this report is about, committed inside a report about it.

## What this sample cannot see

Nineteen findings is the subset written in numbered form; most reviews write prose, and I did not classify those. Worse, and structurally: the rounds that were destroyed by rescues are not in this sample at all, and those were the expensive ones. Everything above is therefore measured on the tasks that went comparatively well.

That is `01`'s own thesis turned on this file. It does not invalidate the shapes — they recur too consistently across the surviving sample — but the true tail is longer than anything counted here, and it cannot be recovered.

## The one change that would matter

Not better prose in specs. A decomposition step that turns every clause of the form "the change touches X" into a command whose output is pasted into the spec — the sites counted, the consumers listed, the size measured on the day. Every failure above is a sentence that would have survived that step, and did not get it.
