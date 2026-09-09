# 32.1 — three plan rounds, five findings, every one a requirement with no check underneath it

**Project:** skills
**Date:** 2026-09-08
**Stopped at:** planned:3
**Elapsed before the rescue:** 806

The task was drafted three times, and each draft was read and sent back with a finding that was true.

The first draft pinned the new paragraph's position as "immediately after the seven-bullet list and before the blank line", which in Markdown makes text at column zero a lazy continuation of the seventh bullet — the paragraph would have rendered as part of the contract-line rules, the exact mis-scoping the task exists to prevent, and no listed check would have caught it because the text carries no bullet marker. The same draft told the second file to point at the method by naming its place in the engine in quotes, while the engine paragraph it was creating had no name to quote: the only quotable handles were a heading about contract lines and a thirty-line section, so both the implementer and its reader would have had to invent the address, and could have invented different ones. The draft also grounded its refusal of `wc -m` in a claim about bytes that the shell it was reviewed in contradicts.

The second draft fixed all three at the root rather than around them: the separating blank line was pinned with its Markdown reason, the paragraph was given the name `**Counting characters:**` in the shape the engine already uses for its named paragraphs, the pointer's address was pinned verbatim, and the discarded byte claim was replaced by the durable, locale-independent reason — `wc -m` counts the trailing newline the rule excludes. Its reader then found the next requirement without a check: the draft forbade the second file from restating either the unit or the command, and counted only the command. A bullet that named the address and also spelled the unit out would have passed every listed check while giving the method a second home — precisely what the task's one-home guard exists to stop.

The third draft added that count, and its reader found two more of the same shape. The paragraph is required to state the rule for every budget in this family — the task's entire point, argued twice in the draft's own prose — yet every engine-side check would pass on a paragraph that scoped the rule to contract lines alone. And three of the checks on the second file are written against one bullet while the draft's opening gate mandates that every count be taken over the whole file: read literally, the engine's name occurs six times in that file and the refusal phrase twice once the bullet adopts it, so those checks report failure on a correct edit.

Nothing here is a defect of execution. Each draft was better than the one before it, every finding was true, and none repeated. What repeated is their shape — a requirement stated in prose with no check underneath it — and three of the five trace past the draft into the task's own specification: the specification mandates quoting an address it never creates, states the family-wide scope without asking anyone to verify it, and carries the same whole-file/one-bullet ambiguity in its own check list. A draft discarded now takes its repairs with it, and the specification would hand the next one the same three holes.

> The task's specification states its requirements in prose and verifies only some of them, so each draft satisfied the prose and left a different unverified requirement exposed — had every requirement carried its own check, the first draft would have been the last.

Root-cause category: specification gap. Recurring-issue signal: no individual defect recurred; the pattern is five findings across three rounds of one shape, named as such by the reader twice.

## What was done

Repaired at spec + plan depth, so the three rounds of drafting survive and only the discarded readings are cleared.

The specification gained what the drafts had been supplying by hand: the paragraph is named `**Counting characters:**` and the separating blank line is stated with its reason, so the address the second edit must cite now exists in the specification that mandates citing it; the family-wide scope gained a check of its own, which a paragraph scoping the rule to contract lines fails even when every structural check passes; and the check list now says which counts are taken within one bullet's extent and which across the whole file, so a correct edit no longer reports failure. Its account of the environment was corrected in kind: whether `wc -m` yields characters or bytes depends on the locale of the shell it runs in, which varies between shells on this machine — the earlier text asserted one shell's answer as the machine's.

One observation had been carried, unresolved, by all three readings: the method being pinned is a shell command, and the skill holding the second budget declares no shell grant at all, so obeying the rule literally would take it outside its own grant. It is disposed of here rather than deferred again, and the disposal is a guard in the specification: no skill runs the command. The budget is guidance, not a hard clamp; the command settles a count once it is disputed, run by whoever disputes it. No grant widens.

The plan kept its three rounds of refinement and gained only the two checks its last reading asked for. The three readings themselves were deleted, and the run's marker was rolled back so the repaired plan is read again rather than rewritten from nothing.
