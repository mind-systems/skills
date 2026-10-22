# 80.3 — the answers become questions, and the rescue pauses on the report

## What is true now

The skill is as 80.1 and 80.2 leave it.

`src/skills/task-rescue/SKILL.md`, § "Step 2 — Diagnose root cause and depth", classifies the stop as escalated, plan-phase failure, implement-phase failure, stale implementer session or non-convergence, and calls the result "an internal routing signal" for Step 4's depth choice. § "Step 3 — Extract root cause" sorts the findings into four root-cause categories, treats recurrence in two rounds as the signal that determines the depth, judges the findings against the governing spec and phase note in a paragraph that requires the report to say whether the failure violates the spec and to quote the clause, tells the narrative to end on a standalone root-cause sentence, and attaches the category and the recurring signal as a classification that "carries into Step 4". The narrative is chronological prose, round by round, in complete sentences, with no tables or bullet lists, and it has special forms for an escalation and for a stale implementer session. It is "printed before the Step 4 depth menu", and it ends with the first write of the report, which 80.1 puts there.

§ "Step 1 — Discover artifacts" reads the phase's governing spec and phase note in a paragraph that resolves `$TARGET_FILE` "the same resolution Step 4 determines", locates the phase, says the read is "unconditional, not suspicion-based", says to proceed as before when the task is under no phase or neither pointer is named, says the read is additive to Step 4's own resolution, and says a named file that does not exist is told to the user and carried into the report as a finding. It also says to ask the user which task to rescue when artifacts of several slugs are present.

§ "Step 4 — Choose repair depth" resolves `$TARGET_FILE`, with an explicit argument first, a test sibling for test tasks and the roadmap in play otherwise, and locates the contract line of the slug, and then puts four questions through `AskUserQuestion` menus with option texts: an escalation's three options, non-convergence's three options, a depth menu with four options, and, ahead of the menu, a scope-overload flag and a stale-implementer flag. Step 5 carries a paragraph per escalation and non-convergence option, and opens "for the depth chosen in Step 4". § "Step 5.5 — Propagate findings to open tasks" scans the open tasks for the same gaps, in a priority order built on the categories and a list of ways to match, and puts one `AskUserQuestion` menu: apply all, review each, skip.

§ "What NOT to do" holds bullets that each restate something a step already says (committed files and other slugs, the `planner`, `elapsed` and `implementer` keys, the guards on writing `planned:1` and `implemented:1`, reading every round, reading the governing spec and phase note, pinning only what was evaluated, checking for an escalation first, no fifth menu entry) or fence the logic of a repair.

The frontmatter lists `AskUserQuestion` in `allowed-tools`. The `description:` says the skill "diagnoses how deep the root cause reaches and repairs to that depth, then rolls the task's state back". `docs/reserved-words.md` defines a rescue as repairing a task "to the depth of its root cause", and calls itself final.

The opening of the skill calls "the orchestrator exhausting its iteration limit and stopping" the tripwire, and names as its subject "the defect in the task's specification (task spec + contract line) and its implementation": the rescue reads the artifacts, "diagnoses how deep that defect reaches (specification gap? bad plan? broken implementation?)" and repairs "to exactly that depth". The second paragraph calls the repair "depth-keyed" and lists its reach as task spec and contract line, plan, or working-tree code, and says "The user picks the depth".

§ "Step 5.6 — Pin disposed observations" has the rescue pin each deferred-observation entry it disposes of at the moment it disposes of it, and a sentence that says to pin "at the moment of the judgment — routing or dismissal — not at session end". § "Step 5.7 — Write the durable report", in "When the write cannot happen", says on a failed first write to "say so plainly to the user and complete the rescue anyway".

The user: «рескью, тут я хочу читать отчёты и что б агент на паузе ждал… но не как вопрос, этот интерфейс- бред какой то». Asked whether the rollback runs before the pause or after his word: «да, я хочу видеть отчёты рескью».

## What must be true after

**Steps 1 to 3 keep two facts and ask five questions.** The facts are what an agent cannot get elsewhere:
- An escalating agent, whether planner, implementer or either reviewer, writes `ESCALATION` on the last line of the artifact it owns, and for a planner or an implementer that is the plan file, possibly with no plan-review on disk; the sidecar reads `step: escalated`, and the missing decision lies in the artifact's escalation section. It is read first, ahead of every other reading, since a plan with no plan-review otherwise reads as an unfinished planning.
- A resumed implementer session can come back having produced no diff: every review reports the product files identical to HEAD although the plan was ratified. Then no spec, plan or code defect exists, and the gap lies in the pipeline's record of the attempt.

The questions are put to the stalled task; the rescue answers them by reading, and none of them routes to a repair:
1. Does the same finding recur, or is it a new one each round while severity falls?
2. Did the spec leave the planner something to decide or enumerate?
3. Is anything the spec says false of the code, or did its own text, a check or a fence, cause the findings?
4. Should the task exist as written, and is the system ready for it?
5. Do open tasks below carry the same gap?

The classification, the categories, the routing to a depth, the lightweight severity pass, the paragraph that judges against the governing spec, the closing root sentence, the "carries into Step 4" classification and the narrative's special forms for an escalation and for a stale implementer session go; the two facts carry those cases. The narrative stays in its prose form. Both steps' headings stop promising a depth.

Step 1 holds the resolution of `$TARGET_FILE`, an explicit argument first and otherwise the roadmap in play as `roadmap-engine` resolves it, and the location of the slug's contract line, since Step 1 is where they are first needed. The roadmap in play is the one whose contract line carries the slug; Step 4's guess of a test sibling from keywords in the slug or the artifacts does not move with them. Its read of the governing spec and phase note is one sentence: the rescue locates the task's phase in `$TARGET_FILE` and reads in full every document the phase header or intro names as `Governing spec:` or `Phase note:`; its guards go. The instruction to ask which task to rescue stays in prose.

**Step 4 is gone, and so is Step 5.5.** Step 4's resolution and locate have moved to Step 1; the scope-overload flag, the stale-implementer flag, the escalation options, the non-convergence menu and the depth menu go, and so do § 5.5 and its menu. The later steps keep their names and numbers. § 5.5's scan is question five, answered in the report, and applying a clause to an open task is part of what the user's word releases.

**Step 3 ends in a stop.** The rescue decides the repair and the rollback state it intends, and the first write of the report, made per § 5.7 at the end of Step 3, holds the intended repair and the intended rollback beside the diagnosis and the section on who found what. An escalated stop is told there as a decision for the user, with its options. The rescue then stops, and says in the conversation where the report lies and what it waits for. The diagnosis itself lives in the report.

On the user's word the rescue applies the repair and the rollback and extends the report. Step 5 opens on that word and loses the paragraphs keyed to the options; its four states stay as 80.2 leaves them. The section appended to the report after the repair says what the repair did, the rollback state the task was left in, and what was deleted or kept; the sentence in § 5.7 that carries "the depth chosen, or the escalation option taken, or the non-convergence choice made", and the sentence on a branch that produced no root-cause sentence, go.

**§ "What NOT to do" goes**, each fact it held living once in the step that acts on it.

**The frame follows the body.** `allowed-tools` keeps `AskUserQuestion`. The `description:` tells what the skill does now: it reads the failed artifacts, writes its report with the intended repair and rollback, waits for the user's word, then repairs to the depth of the root cause and rolls the task back so the orchestrator re-validates from there; it keeps its trigger phrases and stays within the field's limit.

The opening keeps the tripwire sentence, the stop being how the failure was noticed and not what failed, with "exhausting its iteration limit" widened so that it covers an escalation, which stops before its budget is spent. The subject sentence names what the rescue looks at: what the stopped task needs, read from the artifacts it left. It fixes neither the root's kind nor its place, since Step 2's two facts say a no-diff run and an escalation are not defects, and question 4 exists because the root may lie above the task. The reach of a repair is not a closed list: it may go above the task, a phase put in front of it, a phase closed, the task deleted (cases `0024` and `0038` in the phase note `0226`). The repair reaches as deep as the root cause, steered by the user's word; the pinned list of task spec and contract line, plan, or working-tree code goes from the second paragraph, and so does the sentence that the user picks the depth.

**§ "Step 5.6 — Pin disposed observations" changes in one sentence.** A pin is written when the repair is applied, on the user's word, and not at the moment of a judgment made before it; the sentence that says to pin at the moment of the judgment says this instead. The rest of § 5.6 stays.

**§ "Step 5.7 — Write the durable report" changes in one sentence.** In "When the write cannot happen", "and complete the rescue anyway" goes, so the sentence says the failure plainly to the user and ends. The bans that follow it stay, and no further resolution of a failed first write is carried.

## What breaks on contact

**Rule:** a text breaks on this change if it names a classification, a category, a flag, a menu, a depth choice, Step 4, § 5.5 or § "What NOT to do" that no longer exists.

**Sweep:**
```
grep -n -E "AskUserQuestion|categor|flag|routing|menu|Step 4|Step 5.5|What NOT" src/skills/task-rescue/SKILL.md
```

**Finding.** The search returns Step 2, Step 3, Step 4, Step 5's opening and its option-keyed paragraphs, the references to Step 4 in Step 1 and Step 5, § 5.7's sentences on the depth chosen and on a branch with no root sentence, the `description:` and the heading and body of § "What NOT to do"; each is a target above, except the words "routing" and "flag" in § 5.6, which mean pinning there and stay wherever § 5.6 keeps them, and the `allowed-tools` line, which keeps its tool. Step 1's "ask the user which task to rescue" stays. The table of valid states and the four rollback states are not touched; § 5.6 and § 5.7 change in the one sentence each named above.

Outside the skill, `docs/reserved-words.md` binds the rescue to repairing to the depth of the root cause, and the description keeps that clause. `docs/sakshi-harness/skill-cycle.md` describes the rescue as diagnosing the depth of the root cause; that doc is another phase's. The orchestrator's `docs/concepts/non-convergence.md` describes the same concept and stays true. `orchestrator-artifacts`, § "Sidecar fields", still finds the closed set in this skill.
