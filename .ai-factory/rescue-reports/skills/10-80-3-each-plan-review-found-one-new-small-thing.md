# 80.3 — each plan review found one new small thing

**Project:** skills
**Date:** 2026-10-22
**Stopped at:** planned:3 — the plan-review cycle spent at its round 3, no `PLAN_REVIEW_PASS`
**Elapsed before the rescue:** 672
**Sessions:** planner: 62f47100-bf50-4fb2-b42c-728ea462882f; plan-reviewer-1: 2656a731-b754-46af-b05d-2c13e52345d1; plan-reviewer-2: da862b0c-7121-44af-9512-71cd1685e170; plan-reviewer-3: a07b1910-61d7-45c3-8e92-510b861e6e95

The task rewrites the rest of `task-rescue` after 80.1 and 80.2 landed: Steps 2 and 3 become two facts and five questions, Step 4, § 5.5 and § "What NOT to do" go, the rescue writes its report with the repair and rollback it intends and stops for the user's word, and the frame follows. The planner wrote one plan of some hundred and seventy lines against spec `0255`, grounded every block it deletes in the file at HEAD, and added a second sweep for stragglers the spec's own grep misses.

The first review rated it medium risk on one finding and low on three. Once the plan removed the chat printout, a failed first write of the report left nothing to show the user, and § 5.7's "complete the rescue anyway" could be read as leave to skip the pause; the spec did not cover that case. A new template section made "this section" in the finders paragraph point at the wrong section. The narrative's defect-chain sentence stayed, though the plan removed its twin for presetting the root. And the claim that every fact of "What NOT to do" found a home was not true of three fences.

The planner fixed all four, and the second review rated the plan low risk with two new findings, both small: the plan placed the signal-semantics pointer in Step 3 when it lives in Step 2, and the narrative still wove in findings "from the recurring rounds (2+)", a qualifier left over from a paragraph the plan deletes and one that would hide exactly the evidence question 1 now asks about. It also deferred a question the plan could not settle: with the pause in place, § 5.6 pins at the moment of a judgment that is now made before the user's word.

The planner fixed both, and the third review again rated low risk, with one new finding. The opening's subject sentence — "the defect in the task's specification (task spec + contract line) and its implementation" — survives the plan's rewrite of its tail, and it presets the root's kind and place: Step 2's own facts say a no-diff run and an escalation are not defects, and question 4 exists because the root may lie above the task. The review deferred the same shape one level down: spec `0255` pins the reach of a repair as "task spec and contract line, plan, or working-tree code", which leaves out the phase-level repairs of cases `0024` and `0038`.

No finding recurred, and the severity fell from medium to low and stayed there; each round closed what the last one found and met one new thing in a corner the spec had not decided. The plan is close to done. What stopped it is two places where spec `0255` itself still carries the answer the phase removes — the subject sentence it left standing and the reach list it pinned — and one decision it did not make, when a pin is written now that the rescue waits.

> Spec `0255` should have said that the opening names what the rescue looks at without fixing the root's kind or place, that a repair may reach above the task, and that pins are written with the repair, after the user's word.

## Who found what

**Root cause found by:** the plan-reviewer at round 3, in the run (the subject sentence, and the pinned reach list as a deferred observation)

- A failed first write leaves the pause with nothing to show — the plan-reviewer at round 1, in the run
- "This section" in the finders paragraph points at the new section — the plan-reviewer at round 1, in the run
- The narrative's defect-chain sentence presets a defect — the plan-reviewer at round 1, in the run
- Three fences of "What NOT to do" have no home, contrary to the plan's claim — the plan-reviewer at round 1, in the run
- The signal-semantics pointer is placed in the wrong step — the plan-reviewer at round 2, in the run
- "From the recurring rounds (2+)" hides non-recurring findings — the plan-reviewer at round 2, in the run
- § 5.6 pins before the user's word — the plan-reviewer at round 2, in the run
- The opening's subject sentence presets the root — the plan-reviewer at round 3, in the run
- Spec `0255` pins the repair's reach to the task — the plan-reviewer at round 3, in the run
- `skill-cycle.md` still describes the rescue as diagnosing a depth — head 09, before the run (placed in phase 95's preamble); met again by the plan-reviewers at rounds 1–3
- No finding recurred and the severity fell, so this is not a task too large for its shape — the rescue itself, in the rescue

## Intended repair

Repair the spec and the plan; keep the plan.

- Spec `0255`, § "What must be true after", the frame: the opening keeps the tripwire sentence, with "exhausting its iteration limit" widened to "stopping" so it covers an escalation; its subject sentence names what the rescue looks at — what the stopped task needs, read from the artifacts it left — without fixing the root's kind or place; the reach of a repair is not a closed list, and may go above the task (a phase in front of it, a phase closed, the task deleted).
- Spec `0255`: § 5.6's pin is written when the repair is applied, after the user's word, not at the moment of a judgment made before it. One sentence of § 5.6 changes.
- Spec `0255` carries the plan's resolution of a failed first write: the rescue says why, tells the report's content in the conversation, and still waits for the word.
- The plan: the frame task and the § 5.6 sentence follow the spec. Nothing else in the plan changes.

Rollback: `planned:1` — the plan stays, the three plan-reviews are deleted, `step` is `"planned:1"`. The deferred observations they carry are all disposed of by this repair or already placed (phase 95), so nothing is left to pin.

Waiting for the user's word.

## 2026-10-22

Head 09, the third view, read the diagnosis before the repair: the repair is the phase's own direction carried one step deeper, and `planned:1` with the plan kept is proportionate. One cut, taken: the spec does not carry a resolution of a failed first write. That would be a guard against the rescue's own machinery, a sentence per excluded case; the pause is already unconditional at the end of Step 3, and a write that returns no path is loud. The repair instead drops "and complete the rescue anyway" from § 5.7's "When the write cannot happen", so the sentence says the failure plainly and stops, and the plan's four bullets on it go. The other intended repairs stand.

- Writing a failed-first-write resolution into the spec is a guard, not a fix — head 09, in the rescue

## 2026-10-22 — the repair, on the user's word

The user gave the word. Spec `0255` now has the opening's tripwire widened to cover an escalation, a subject sentence that names what the rescue looks at without fixing the root's kind or place, and no closed list of how far a repair reaches, which may go above the task. § 5.6's timing sentence moves the pin to when the repair is applied, on the user's word. § 5.7's "and complete the rescue anyway" goes, with no further resolution of a failed first write. The plan follows in its frame task, a new task for the § 5.6 sentence, and its § 5.7 task; nothing else in it changed. The three plan-reviews were deleted; the plan stays; the sidecar reads `planned:1`.
