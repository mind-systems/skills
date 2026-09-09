# 32.1 — a word already spent in the file it lands in

**Project:** skills
**Date:** 2026-09-09
**Stopped at:** planned:3
**Elapsed before the rescue:** 1706

This is the task's second stop. The first was repaired at specification-and-plan depth, keeping the plan that three rounds had already polished; three further rounds then failed against it, and the reason the plan could not converge turned out to be in the specification the plan was drawn from.

The first round found three defects. The plan's reason for refusing one counting command had collapsed to a single objection — that the command counts a trailing newline the rule excludes — while the specification it was drawn from records something stronger and different: in a shell with no locale set the same command counts bytes, not characters. An off-by-one is a defect a caller can correct and a byte count is not, so the reduced rationale left a wrong command looking like a legal equivalent. Separately, the phrase the specification used to name the new paragraph's scope leaned on a word that the target file has already spent on another concept, ten lines below the insertion point and inside the same section, while the file names no such thing about itself anywhere — the phrase had no antecedent to resolve against and collided with a live use. Third, the plan silently corrected a count the specification stated and did not mark the correction as one.

The second round confirmed all three closed and found two more, both about the same scope phrase: an address in the plan's own enumeration pointed at a line that carries nothing, and the phrase was pinned in one section of the plan and paraphrased differently in the section that checks it, so the one semantic check had two candidate strings and could pass or fail on wording alone.

The third round confirmed both closed and found one. The guard that was supposed to catch the word collision stated a baseline of one occurrence where the file holds two — both on a single line, so a line-oriented count returns one, which is the very counting method the plan elsewhere forbids. A correct edit would have failed that check, and the natural way to reconcile the failure would have been to delete one of two pre-existing uses that nothing else was watching.

Five of the six findings across the two stops trace to one phrase in the specification, and the sixth to a count in it that was wrong.

> The specification named the new paragraph's scope with a word the target file has already spent on another concept and never claims for itself, so every round had to phrase its checks around a word that could not carry them.

Root-cause category: specification gap.

## What was done

Repaired at specification depth. The paragraph's text is now pinned verbatim rather than described, so its scope is stated by naming the two budgets it governs instead of by a word that had to be resolved; the colliding word is named in the specification as unavailable, with the reason. The false count was corrected against the file. Pinning the text removed two checks outright — a check that the scope phrase appears, and a check counting the parts of a reference shape — because a pinned text needs no check that it says what it says.

The plan, its three reviews and the run's status file were deleted; the task returns to planning from a repaired specification. The contract line was already correct and was not touched.

The choice of depth was decided by the first stop: that rescue kept the plan on the grounds that three rounds had improved it, and the kept plan carried the specification's defect into three more. A plan drawn from a text that cannot be satisfied is not improved by polishing.
