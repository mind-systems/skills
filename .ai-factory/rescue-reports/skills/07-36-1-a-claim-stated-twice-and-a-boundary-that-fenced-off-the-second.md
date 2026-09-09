# 36.1 — a claim stated twice, and a boundary that fenced off the second

**Project:** skills
**Date:** 2026-09-09
**Stopped at:** planned:3
**Elapsed before the rescue:** 1197

The first review found a hole in the specification that made the task unbuildable from inside its own boundary. The specification calls for removing the sentence that closes the buffer to the editor, but the same claim stands in the file twice — the second time seventeen lines earlier, inside the paragraph about spawning, as a parenthetical justification that nothing outside the skill ever learns about the buffer or the handle. After the task lands that is false in exactly the way the removed sentence is false. And the boundary the specification drew — the moment of creation belongs to the next task — was read as fencing off the whole section containing it, so the second statement was unreachable. No task in the phase repaired it, and the contradiction would have shipped with the phase.

The same review found three further traces of one root. The phrase naming the shared engine narrowly lives in two callers, and the specification pinned the second of them unchanged, so after the engine's scope widens both descriptions go stale. The three things the architect records in the buffer — the handle, the pairing role, the parked entries — were assigned to no zone, though whoever rewords the privacy sentence cannot avoid deciding it. And the sentence stating where the buffer lives was to be cut while another line still refers to "its existing path", leaving that reference with nothing to resolve against.

The second review confirmed the critical finding closed and raised four smaller ones, all of the same shape: places where the engine still describes itself as a channel contract that the specification had not enumerated. The third closed those and left one — the closing verification tests what the file loses and never what it gains, so two requirements the plan states for itself have no check behind them. Severity fell round over round; the plan was converging, and the budget ran out first.

> The specification named the claim it removes as one place in one file, when the file holds it in several forms — a second statement, an appositive naming the engine, a sentence about location that other lines depend on — and drew a boundary that turned that incompleteness into a prohibition.

Root-cause category: specification gap, of the blast-radius kind — the enumeration of what the change breaks was incomplete. No finding recurred; each round closed the one before it.

## What was done

Repaired at specification-and-plan depth. The specification now names both statements of the claim and what survives at the second site, narrows the boundary with the next task to the single sentence that task owns, brings both callers' appositives into scope with the second file joining its file set, settles the zone assignment as the task's own decision rather than the implementer's, and requires the replacement pointer to name where the buffer's path and numbering now live so no reference is left dangling. The plan took the one finding the third review left and the widened file set; its earlier revisions stand, because across them it had already out-run the specification and repaired things the specification never asked for.

The three reviews were deleted and the plan kept — the reverse of the choice made on an earlier task this week, where a plan carrying its specification's defect was preserved and cost three further rounds. Here the plan was ahead of the specification, so the specification was brought up to it.

One correction followed from the repair itself. The zone assignment was first written by sorting entries into categories — parked entries to one zone, lag-register entries to the other — and the categories are not different kinds. It now turns on what the entry is: a known defect or a settled ruling the hand needs in order to act is held by both, while an open question the architect has not resolved stays with the architect, because a hand already holding an unfinished conclusion returns an echo where an independent reading was wanted.

A neighbouring task's specification referred twice to the span this repair edits as unchanged context. That account was corrected; its own change is unaffected.

## What it set off

The repair above closed the task. The questions it raised did not stop there.

The finding that blocked the phase was not in the specification at all. It asked whether the buffer comes into being at the architect's start or at its editor's spawn, and nothing on disk could settle it. Put to the user, it came back as a rule with four moments: a memory snapshot naming a buffer means that buffer; no pointer means a new one, created before any editor exists; each half learns the other's address at the spawn; and the hand's own history, which ends without a signal, is recovered by that same snapshot handed to it again. No artifact stated any of them.

The rule went into the governing spec first. It gained a section on how the memory begins and how it survives, and the phase was rebuilt against that section rather than against the conversation: the task that moved the buffer's creation was rewritten from unconditional to conditional, and the two moments belonging to no task became two tasks — the editor learning where the shared memory is, and its recovery through the snapshot, which later took in a second occasion for writing one.

The root cause recurred a tier up, in a form the rescue could not see from inside one task. A textual unit treated as though it carried one meaning is the same defect as a task addressing a file by position while its siblings rewrite that file: the first to land invalidates what the others were grounded in, silently. Every position address in both phases was replaced by a name — a heading, a task number, or a quotation verified unique against the file — and the two phase notes were corrected where the governing spec had moved out from under them. Those notes are read in full by decomposition and by any later rescue, so one of them had come to state the opposite of the truth: that something was undocumented on both sides, when one side had since documented it.

One task was withdrawn rather than repaired. It named the class of artifacts the architect writes with its own hands, and it had grown from the architect's own practice rather than from any decision of the user's.

The task itself has not re-run. Its plan still stands where this rescue left it.
