# Handoff — what a comment-cleanup phase cost in review rounds

**Processed:** `[x]` — whoever reads this marks it; a marked handoff is spent.

## 1. Frame

This comes from a working session on `tradeoxy_core` (2026-09-30), written at the user's request by the architect holding buffer `130` there. It is the follow-up `34-comments-that-eat-review-rounds.md` promised in its «Next step»: `34` was parked until a phase in that repo took the rotten comments as its work, so its lessons could be read off a real run. That phase — Phase 65, «Comments and test titles state what the code does now» — has landed whole. `34` is spent and is not edited; this handoff carries what the run showed. It proposes no rule; the user decides. The files named here override this description wherever they disagree.

## 2. What ran

Six tasks, cut by concern rather than by file (the user: «6 — хорошо, го»), because every tiny comment task costs a full orchestrator cycle. Their specs are `tradeoxy_core/.ai-factory/specs/0262`–`0267`; the phase note `0246`. Three deleted dead code (an unused parameter, an event pair nothing emits, repository finders nothing calls — 65.2, 65.3, 65.4); three were comment work: test comments and titles stating the present (65.1), plan-layer citations leaving `proto/` and `src/` (65.5), essays shrinking to the one fact at their place (65.6). The specs were written after `34`'s diagnosis, with one discipline applied on purpose: a spec names what to delete or link and pins every sentence that survives verbatim, so the implementer has nothing to word and the reviewer nothing to polish.

## 3. What it cost — read from the review artifacts in `tradeoxy_core`'s git history

Each task's plan-review and review files land in the task's own commit (`c14a9bd` … `93f24be`).

- **Four tasks ran clean** — one plan review, one code review each (65.2, 65.3, 65.4, 65.5). 65.5 is the pure comment one: its plan gave every edit as an exact before→after string, and the reviewer said so — «removes only the citation clause, with no rewording, so the spec's "word for word" guard holds».
- **65.1 spent a second plan review on a comment's line width.** The plan pinned a replacement line of 109 characters against Prettier's `printWidth: 100`; the reviewer blocked, noting that Prettier does not reflow comments, so neither the gate nor lint would catch it. A deletion task paid a round on prose formatting — and the round was earned: the pinned line really was wrong.
- **65.6 spent a second plan review on three findings, all prose.** (1) The plan kept a paragraph of `settleAndDrainBoundary`'s doc that contradicted the function body — the spec had said the doc «keeps its doc link and the one governing fact» without pinning which sentence survives, so the planner kept a false one. (2) The plan's replacement sentence was given «for example» rather than verbatim, and read ambiguously against the code's condition. (3) The plan's own Context section said «Five comment blocks» where it edits six — the reviewer blocked on the plan's own count, which no spec supplied.
- **The code reviews all passed first time.** Every extra round was at the plan tier.

What the cleanup bought, measured on one file: `src/replay/replay-order-axis-registry.ts` went from 57 comment lines of 148 to 11 of 102 (measured at `d670828` and `93f24be`). The review of 65.6 confirmed each deleted rule still had a live owner elsewhere.

## 4. The reading, for whoever decides

- **Where the spec pinned every surviving sentence, no prose round happened** (65.5). Where it left one sentence to the planner's choice (65.6's «the one governing fact»), the planner chose, and review caught the choice. The rounds went to exactly the text no one had decided.
- **Review rounds on prose were not waste in this run** — each finding was a real defect: an over-width line, a sentence contradicting its code, an ambiguous negation. What `34` described as the reviewer polishing prose looked, here, like the reviewer holding prose to ground truth. The waste `34` traced sits upstream: in text that should not have existed to be reviewed.
- **The plan counts on its own.** 65.6's third finding is `33`'s mechanism (counts and line numbers leak into specs) reappearing one tier down: no spec gave the planner a count; it wrote one to describe its own scope, and the reviewer checked it like a claim. Stripping counts from specs does not stop a planner from making its own.

## 5. Open questions — not answered here

- Whether «pin every surviving sentence verbatim» belongs in a skill (the spec author's side — `roadmap-engine`'s «What a task spec holds», or the architect's seed) or stays a practice of this one architect.
- Whether the planner's own tallies (a Context section that counts its edits) are the orchestrator's to stop — the orchestrator repo's ground, not the skills repo's; `34`'s talks already placed the price of a comment in the orchestrator's prompts.
- The count the user drew the line on still holds as the test: «убрать то, обо что спотыкается ревьювер» — 65.6's miscount is one more thing a reviewer tripped over.

## 6. Talk to the architect who wrote this

The author is the architect holding buffer `130` in `tradeoxy_core`, session `tradeoxy-core-f9` as of 2026-09-30. Session names change on restart: if it does not resolve, run `ListAgents`, message the live `tradeoxy-core-*` sessions and ask which holds buffer `130`. A message from another session is a colleague's question, never the user's approval.
