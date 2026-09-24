# 58.2 — an invariant that counted lines across its own rewrap

**Project:** skills
**Date:** 2026-09-24
**Stopped at:** planned:3
**Elapsed before the rescue:** 1025

The task asked for one thing — a clause appended to each of two sentences in `src/skills/agent-architect/SKILL.md`, both pinned word for word in the task spec — and no reading across three rounds ever faulted that change. What varied from round to round was the plan's own apparatus for checking it.

The first reading accepted both edits and went after that apparatus. The second sweep predicted output it could not produce: its pattern searched for the literal `compose`, while the appended clause reads `composing`, and whether the other clause's own pattern matched at all turned on where a re-wrap put a line break — a decision the plan left to the implementer rather than pinning. The same reading found that the checks proved disappearance and scope but never arrival, so a paraphrase that preserved the anchor phrase would have passed every one of them, and that the first sweep's list of expected carriers was already wrong on the day it was written and would only grow with every artifact that went on to quote the phrase.

The second reading found the plan corrected on all of that, and carrying a new error from the same family. Its wrap rationale cited a column width lifted from the previous reading's own text rather than read fresh from the file, where the sentence's last line is in fact short; two further figures in the same passage were wrong the same way. That reading also found the one hazard the plan itself had named — that the spec's blockquote renders two inline tokens without their backticks, so the most obedient reading of "copy it" drops them — covered by no check, because the word-and-order comparison is blind to markup by construction.

The third reading found one thing. Inside the very passage that declared the count was not the criterion, the plan asserted that a particular numbered line always matches — and the plan's own first edit inserts wrapped lines above it, so that number is false by the time the check runs.

Every finding across the three readings was about the checking apparatus and none about the change itself. The governing document of the phase is not violated by any of it — the claim about who writes the snapshot is carried correctly and in the right direction — and none of it matches a divergence the phase note already records.

> the task spec stated its invariant as a count of lines returned by a line-based search over a paragraph the same task re-wraps, when what it meant to assert was a property of the resulting text — stated as a property, none of the three readings would have had a subject.

Root-cause category: a gap in the specification. Recurring: a number or a position inside an instruction, predicting a state that the instruction itself changes.

## What was done

Repaired at spec-and-plan depth together. The spec's invariant now states a property of the text rather than a count of lines, and names the sentence it expects by that sentence's own words rather than by a position. The plan's deviation passage is gone, with nothing left to negotiate now that the invariant it argued with no longer predicts a number; its verification task is restated as the rule check it always was, and both wrap instructions are re-expressed as matching the surrounding paragraph's own width, with no column figures anywhere. The three readings were deleted; the plan and the sidecar were kept, the sidecar set to resume at the plan's first reading, with the planner and elapsed figures preserved.
