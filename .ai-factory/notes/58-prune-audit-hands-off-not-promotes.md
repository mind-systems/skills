# milestone-rescue-audit prune: hand off findings and halt, never graft into finished artifacts

**Date:** 2026-07-11
**Source:** conversation context (live `roadmap-prune` → `milestone-rescue-audit prune` run on `tradeoxy_core`; promote wrote review-jargon into completed-task specs and `ARCHITECTURE.md`)

## Key Findings

- `milestone-rescue-audit` **prune mode** disposes of each still-real deferred observation by **promoting** it: appending the entry **verbatim** under a `## Deferred observations` heading in the file its `Affects:` names, then marking the source line `[promoted → <path>]`. The routing test is purely "does that path resolve to an existing file under the repo root." On a real repo that test misfires two ways:
  - **Finished specs are records, not editable surfaces.** Most `Affects:` targets resolve to the specs of **completed `[x]` tasks** — in this run `specs/10-replay-indicator-replayer.md` (task 6.2), `specs/11-replay-merge-stream.md` (6.3.2), `specs/13-replay-order-enrichment-seam.md` (7.2.2), all shipped. A completed spec is a historical artifact; grafting a fresh section into it corrupts the record. The existence test cannot tell an open, editable spec from a frozen one.
  - **Product docs are not observation dumps.** One `Affects:` named `ARCHITECTURE.md`; the text promoted into it was a raw reviewer note full of pipeline jargon ("`Docs: no` this milestone", "fold into the next docs pass for the replay subsystem") — meaningless sitting in a clean architecture document. Promote never sanitizes; it pastes review-speak into a product doc.
- Net effect: the disposal step **writes into artifacts it must never touch**, and the "gate can now pass" state it manufactures is illusory — the observations were *relocated*, not *resolved*.
- The user's intended workflow is the opposite. The audit is an **evaluator + reporter that halts**, not an auto-resolver. After its work it must collect every finding with full descriptions, **hand them off** (via `command-handoff`) together with the context the next agent needs to work through them, and then **park the prune**. The prune session waits; the user resolves the findings in a **dedicated session** (that is where pins get set), and only then re-invokes `roadmap-prune`. The audit never sets the "resolved" state on the user's behalf.

## Proposed direction (ratify before respec)

- Prune-audit's disposal **stops mutating target files** — it never appends to an `Affects:` target. With no promote-append, it can never write into a finished spec or a product doc.
- After evaluation, prune-audit **terminates into a handoff**: it calls `command-handoff`, writing every finding — gist, the reviewer's original text, the `Affects:` value, and the audit's verdict (moot / real-and-open / needs-routing) — plus resolution context, into `.ai-factory/handoffs/`. Then it **halts**; the prune loop is parked, deliberately still gate-blocked.
- **Pinning moves into the resolution session.** The gate staying blocked *is* the "park and wait" state. The user resolves each finding there — fixing it, routing it into an **open** task's spec, or genuinely dismissing it — sets the pins, and re-runs `roadmap-prune` only when all pins are set.

## Open question for the user

The complaint was specifically about **promote** — the only disposal step that writes into *other* files. The read-only review-line markers (`[audit-dismissed]`, `[unrouted-reported]`) do not. Decide whether prune-audit still applies those markers itself, or whether it should purely report-and-halt and let the resolution session set every pin. This governs how much of the current prune-mode survives.

## What NOT to do

- Do not append a deferred observation into the file its `Affects:` names when that file is a completed-task spec or a product doc — finished artifacts are records, not editable surfaces.
- Do not treat "the file exists" as "the file is a safe promote target."
- Do not let prune-audit's disposal stand in for human resolution — its deliverable is a handoff plus a parked prune, not a passed gate.
