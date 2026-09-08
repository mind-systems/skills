# 31.1 — three plan rounds against a spec whose requirements outran its checks

**Project:** skills
**Date:** 2026-09-08
**Stopped at:** planned:3
**Elapsed before the rescue:** 1054

The first round read the drafted plan against the task's specification and found four defects. The rule the plan put in the command's body did not say whom it addressed, so a reader could take it as permission for the command's own write path to amend an existing handoff, when that path always produces a new numbered file. The verification method the plan mandated required a whitespace-normalised read for two checks that depend on line structure the normalisation destroys, so a run following the plan literally would either report a check it had not taken or silently abandon the stated method. The prose-shape edit introduced a title requirement that no verification bullet covered. And the instruction to copy the mark's unprocessed literal named four candidate files without saying which one carries it, when only one does.

The second round confirmed all four closed, and found one more. The rule in the body has four parts; the plan's verification counted three, dropping the clause stating that an unprocessed handoff is the one that may be edited and that the flip is the mark's two states and nothing else. That clause is named verbatim in the roadmap's own contract line. A plan passing its own gate could still ship a paragraph that says only what may not be done and never what may.

The third round confirmed that closed, and found a third. The plan instructed the implementer to cite the distiller's default template as precedent for a fully literal line, naming a line that is in fact a literal label with a placeholder value — the opposite of the shape the exemption needs. The line one below it is the one that is literal end to end. The review also noted that whether this precedent was meant for the shipped file or was only the plan's own rationale was never settled, and that if it entered the file nothing counted it.

No single defect recurred: each round closed the previous round's finding cleanly. What recurred was their shape. Three times a requirement was stated in the task text and given no counterpart in the list of checks, and twice the reviewer said so in as many words. Tracing the third finding to its source settles where the fault lies: the inaccurate precedent is pinned in the specification itself, and a planner following a pinned clause word for word reproduces the error it contains. Two of the three gaps were repaired in the plan and never returned to the specification, so discarding the plan would have re-exposed them on the next attempt.

> The specification did not give each requirement it states a check of its own, and named a placeholder-filled label as its example of a fully literal line.

Root-cause category: specification gap. Recurring-issue signal: no individual defect recurred; the pattern is three consecutive single-round findings of one shape.

## What was done

Repaired at specification depth. The precedent was corrected to the line that is literal end to end, and pinned as the specification's own rationale rather than text for the shipped file, so no one-sided claim about another skill's internals is written where that skill carries no counterpart declaration. The rule in the body gained the audience it addresses — whoever holds a handoff file, never the command's own write path — and the two requirements that had reached the plan but never the specification, the prose-shape title and the flip clause, gained checks of their own. A further check now guards the shipped file against the cross-file claim.

The plan, its three reviews, and the run's status file were deleted; the task returns to planning from a repaired specification. The roadmap's contract line was already correct and was not touched.

One observation carried by all three reviews concerned a different task, which asserts that a system document already states the handoff's lifetime. It does not, and after a ruling that a skill is its own documentation, the lifetime stays in the command and the claim was narrowed to what the document actually holds. That correction was applied outside this task.

## How the specification acquired the defects

The three defects the reviews found were not old. All three entered the specification during the same working session, a few hours before the run, across four consecutive readiness passes over that one file — the passes whose whole purpose is to close the places an implementer would otherwise have to guess.

Each entered the same way. The prose-shape requirement and its check were written in one pass; the requirement named a title and a mark line, the check named only the mark line. The precedent for a fully literal line was named from memory of the distiller's template rather than from the template, and the line named is a literal label with a placeholder value, one line above the one that is literal end to end. The rule's clause count was recomputed after an unrelated clause was struck: the struck clause was a fourth, not one of the three that remained, so a check that had read "three parts" was rewritten to read "two" and the clause about the permitted edit lost its cover.

One shape underlies all three. Requirements were added to the section that states what changes, while the list of checks was treated as prose to be kept tidy alongside it, rather than as the structure it is — one entry for every requirement, or the requirement ships uncovered. A fourth claim from the same session, about what a system document says, reached the neighbouring task by the same route: asserted from memory of a file instead of read from it.

None of the four was caught by the pass that introduced it, or by any later pass over the same file. Each was found by a reader — three by the plan review, in three consecutive rounds, and the fourth only when it was questioned out loud. A readiness pass that reasons about a file it has stopped reading produces exactly this: text that is more confident with each pass and no more grounded.
