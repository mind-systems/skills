# Handoff — pin-gaps is scoped as a linter and must become the final readiness gate

## 1. Frame

Phase 29 is in flight and correct as far as it goes, but the request that produced it was too small: `command-pin-gaps` is written as a text-linter over one artifact, while the role it actually has to fill is the **final line under a task** — the last place the governing spec, the task, and the code are stitched together before the orchestrator sees any of it — and closing that gap is a rewrite, not another class — the originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

### Must-read now (minimal rehydration set)

- `src/commands/command-pin-gaps.md` — the file to rewrite, 26 lines ← lead here. Frontmatter `:1-12`; target resolution `:17`; the premise sentence `:19`; **value holes** `:21`; **meaning holes** `:23`; scan mode `:25`; default mode `:26`. Two of those 26 lines survive the rewrite intact (`:17`, `:19`); the rest is replaced or absorbed. That is the arithmetic behind the user's own estimate of "85%".
- `.ai-factory/handoffs/09-pin-gaps-blast-radius-class.md` — the previous request. **Its content is right and stays; its scope is what was wrong.** Read it before this file so you know what is being kept.
- `.ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md` and Phase 29 in `.ai-factory/roadmaps/trickster77777.md` — the in-flight task built from handoff 09, written carefully and grounded. §4 names the one decision to take about it. Do not discard it unread.
- `src/commands/command-pin-gaps.md:10` — `allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git *) Skill`. **`Write` is not granted, and no Task/Agent tool is.** A command that must be able to create a task spec or a documentation file cannot do either today. This one line is the hardest structural constraint on the rewrite.
- `src/commands/command-pin-gaps.md:11` — `loads: roadmap-engine`. The rewrite's capabilities live in skills that are not loaded here.

### Read on demand

- `src/skills/roadmap-decompose/SKILL.md` — holds the decomposition power (`allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill`), and `src/skills/roadmap-decompose-skeleton/SKILL.md` the spec-before-code split.
- `src/skills/aif-docs/SKILL.md` — holds the documentation power, and states the doc philosophy the gate has to enforce: docs as a **present-tense governing spec of behavior**.
- `src/skills/roadmap-engine/SKILL.md` — the two-tier artifact format any new task the gate emits must render through.
- `src/skills/test-philosophy/SKILL.md` — the silent-failure discriminator, for deciding which surfaces the gate must demand coverage of.
- `src/skills/orchestrator-artifacts/SKILL.md` — the artifact protocol downstream of the gate.
- `~/projects/sakshi/orchestrator/orchestrator/prompts/reviewer.md` and `planner.md`, plus `orchestrator/agents.py` and `orchestrator/roadmap.py` — a different repository, read-only here, but §8 rests on four facts measured in them.

## 3. Current state

**Done:**

- The diagnosis is complete and evidenced by a full emulation of the orchestrator's own plan-and-review cycle against a real task in a downstream project (§6). Nothing has been written into this repository for it.

**In-flight (someone else's, and it belongs to this subject):**

- Phase 29 / task 29.1 with spec 103 — the blast-radius class from handoff 09, turned into a task by the architect who owns `trickster77777`. Grounded and accurate; §4 names the decision it now needs.

**Uncommitted working-tree state:**

- `HEAD` is `aa16bbd` ("Roadmap update").
- ` M .ai-factory/notes/05-architect-buffer.md`
- ` M .ai-factory/roadmaps/trickster77777.md`
- `?? .ai-factory/specs/trickster77777/103-pin-gaps-blast-radius-class.md`

The last two are Phase 29. The first is another architect's private buffer and is never edited from outside.

## 4. Next step

Two things, in this order.

**First, a decision about Phase 29, and it belongs to whoever owns that roadmap.** The blast-radius class is a genuine capability of the target skill and its spec is sound. The choice is whether 29.1 ships as written — a small, correct, self-contained edit that makes the command better without making it right — or is absorbed into the larger phase so the file is opened once rather than twice. Shipping it first is defensible; what is not defensible is letting it stand as the answer to the problem, because it is not.

**Second, the rewrite.** `command-pin-gaps` stops being "scan an artifact for holes and close them" and becomes **the readiness gate**: the last check that a task is stitched to its governing spec and to the code, run after decomposition and before the orchestrator. Its verdict is binary and it is the deliverable — this task is ready, or it is not and here is precisely what is missing.

The powers it must have, and the reason each is not optional:

- **Close value holes and meaning holes.** Unchanged; they become two of several classes rather than the whole skill.
- **Close blast-radius holes** — enumerate what the repository already contains that this change breaks. This is handoff 09's class, kept whole.
- **Emulate the plan.** Attempt the implementation plan the task will produce, and treat *everything you had to invent to write it* as a finding. This is the power that finds what none of the classes above can: mechanism the spec never names. It is not optional and it is not cheap, and §6 shows what it costs to skip.
- **Decompose when the task is too large.** A task that cannot be planned coherently is not repaired by pinning its values; route through `roadmap-decompose` / `roadmap-decompose-skeleton` and emit the split.
- **Write or extend the governing doc when the task covers a surface whose behavior is undocumented.** The project's own direction of change is docs → roadmap → code; a task standing on undocumented behavior has nothing to be executed against. Route through `aif-docs`. This is the power that most obviously does not fit the current shape: the command cannot create a file at all.
- **Demand the coverage the surface deserves**, via `test-philosophy`'s silent-failure discriminator, rather than leaving the test surface to the planner.

Frontmatter consequences, all forced: `Write` joins `allowed-tools`; `AskUserQuestion` joins it, because a genuine product decision is raised to the user, not invented; `loads:` grows past `roadmap-engine` to the skills above. The `description:` is rewritten from "scan for fantasy holes" to the gate's actual role — it is always-loaded context, so a capability absent from it is a capability the invoking agent never learns exists.

Two things to settle inside the rewrite rather than leaving to the runtime: whether the gate's modes stay `scan` / default when the default can now create files and split tasks, and what the verdict looks like on the way out — this is the artifact the whole skill exists to produce and today's `N closed from source · M blocking` counter is not it.

## 5. Working discipline

- The user marks with `::`. Everything before the mark relays verbatim to the editor as a `REPORT-ONLY` channel-message; everything after it is the architect's alone and is never forwarded. No mark anywhere means conversation, not a relay. The marker is unconditional — never judge whether it was "meant".
- **Nothing that closes a round — a summary, a verdict, or a work-order — leaves before the report on that round exists.** The parallel pass runs through the wait; what defers is the announcement.
- Verification is by fact: open the file, run the search, quote the line. A report is a claim, including one that says a thing is absent.
- Ship the sentences the request contains. This rewrite is large, which makes the temptation to grow it further larger too.
- Never commit without explicit permission. Work-orders end with "do not commit."
- Work-orders and files are English; conversation may be Russian.

## 6. Error log

The evidence, each item with the measurement that makes it checkable. None of it is this repository's mistake; all of it is what the current shape of the skill failed to prevent.

1. **Five days, two tasks, unfinished.** In a downstream project the orchestrator failed to carry two tasks to completion over five days, and each failure was diagnosed and repaired by hand, in chat, after the fact. The holes were in the tasks, not in the code generation.
2. **A task ran out of rounds with a green plan.** Task 38.5 stopped after three planning rounds at 🟢 Low risk with four remaining findings, every one of them cosmetic — a Swagger description, a miscount in an explanatory sentence, an unpinned fixture, a list of imports. It did not fail; it exhausted the budget. Measured across 71 completed tasks in that project: 35 passed plan review on round 1, 27 on round 2, 9 on round 3, **zero on round 4**.
3. **The pass bar is zero findings, and the current lens does not aim at it.** `reviewer.md` permits `PLAN_REVIEW_PASS` "only if you have no findings at all", and its deferral criterion states that anything fixable within the task's boundary is a finding "regardless of severity — down to cosmetics", with scope and severity as independent axes. A lens that closes the holes an implementer would have to *guess* still leaves every sentence the plan will get slightly wrong, and each of those costs a full round.
4. **The blast-radius class alone would not have saved the next task either.** Running it over task 38.6 found two real holes — a second, un-enumerated construction site of a service whose constructor the task changes, and an unpinned schema surface. Then emulating the plan found **three more**, all mechanism the spec never named: which function resolves the indicator schema, that the create and update paths reach that schema from different sources, and that update's params are optional so the check must be gated on their presence. Six holes total, and the three most expensive were invisible to every class-based pass, because they only appear when you actually try to write the plan.
5. **The previous request under-scoped the problem, and I wrote it.** Handoff 09 asked for one class to be added beside the two. That was a correct finding answered at the wrong altitude: it fixes one of the six holes above and leaves the shape of the skill — an artifact linter — untouched.

## 7. Orientation

- **The gate is not decompose, and it is not the orchestrator.** `roadmap-decompose` writes a spec *from* a change and legitimately looks forward. The orchestrator generates code from finished tasks; its ability to find defects in a task is its most important capability but not its main one, and it is the last watcher that the code matches the governing spec. The gate sits between them: the last check on the task, so the orchestrator spends its rounds on code rather than on discovery.
- **"Linter" versus "gate" is the whole distinction.** A linter improves an artifact and hands it on. A gate answers one question — is this ready — and is entitled to send the work back a stage, split it, or demand a document be written first. The current skill has no verdict, only a counter.
- **A blast radius is not a scope boundary** (a meaning hole says which files the task must *not* touch; a blast radius says which it *will break* whether it touches them or not), and **a plan emulation is not a blast-radius sweep** — the sweep enumerates consumers of a symbol, the emulation finds mechanism nobody wrote down. Handoff 09 conflated the second pair.
- **`Skill` in `allowed-tools` is not the same as the power to act.** The command can already invoke other skills, but without `Write` it cannot produce what those skills produce.

## 8. Domain model spine

Four facts measured in the orchestrator's own source, not in its description. They set the bar the gate has to clear and should not be re-derived.

- **The task text the planner receives is the roadmap contract line verbatim.** `roadmap.py:9`, `CHECKBOX_RE`, group 3 — everything after the bold title, including the trailing `Spec:` tag. The contract line is not a summary; it is the prompt.
- **The planner reads the reviewer's own checklist while planning.** `agents.py:400`: the planner's system prompt is `planner.md + reviewer.md + escalation.md` concatenated.
- **Every plan-review round is a fresh session with no memory of its own prior review** (`agents.py:495-496`, "Fresh session — no planner bias"), while the planner keeps its session and sees only the latest review's text. So each round re-derives from scratch and can surface something the previous round never mentioned — which is why a task can converge in severity and still never pass.
- **`PLAN_REVIEW_PASS` requires zero findings inside the task's boundary**, cosmetics included. Readiness therefore means: a fresh adversarial reader, holding the spec and the code, finds nothing to say about the plan's own text.

## 9. Hard rules

- **A count is a claim and carries its unit.** `grep -c` returns matching *lines*; occurrences need `-o | wc -l`. An unlabelled number is re-read downstream as whichever unit the reader assumes.
- **An expected value is produced by running the exact command it sits beside**, at the moment it is written — never from memory of a similar command run earlier.
- **A citation lifted out of a report, a review or another artifact is opened before it is transcribed.** Twice this session a number was reported from a file's own stale header comment rather than from the file (a spec claiming ten test cases where the file holds thirteen).
- **A literal gate is right only when the literal *is* the contract** — a marker, a filename, a number. For prose carrying an idea it verifies that a string is present, not that the idea is; there the check is "quote the resulting sentence back".
- **Docs lead tasks, tasks lead code**, never the reverse. This is why the gate must be able to write a document rather than merely complain that one is missing.
- Never commit without explicit permission; never push. All files in English regardless of the conversation's language.

## 10. Cross-cutting contracts / invariants checklist

- **The verdict is the deliverable.** Every capability the rewrite adds exists to make one binary answer trustworthy — ready, or not ready and here is what is missing. A change that adds a power without feeding the verdict has not helped.
- **Every finding class must reach every mode branch.** A class lives in the body, appears in the scan-mode line format, and is countable in the default-mode report. The current file's `value|meaning` token at `:25` is a closed enumeration and cannot express a third class without an edit — that trap scales with every class added.
- **The `description:` block is part of the contract, not a summary of it.** It is always-loaded context; a capability absent from it is a capability the invoking agent may never learn exists.
- **Routing, not reimplementation.** Decomposition, documentation, the two-tier artifact format and the coverage discriminator already exist as skills. The gate gains the authority and the tools to route into them; it does not grow its own copies. A second implementation of any of them inside this command is a defect.
- **The tool grant is the ceiling on the role.** Today: no `Write`, no Task/Agent, no `AskUserQuestion`, `loads:` limited to `roadmap-engine`. Every power in §4 is blocked by one of those four until the frontmatter changes.
- **A genuine product decision is raised, never invented.** The current file already says this for meaning holes ("don't fabricate it — raise it as a one-line question under `## Blocking decisions`"); the rewrite keeps it and needs `AskUserQuestion` to honour it interactively.

## 11. Per-unit map with watch-points

- **`src/commands/command-pin-gaps.md` — becomes the readiness gate.** *Watch:* the frontmatter is the real blocker, not the body — `:10` grants no `Write` and no Task/Agent tool, `:11` loads only `roadmap-engine`, and `:2-8` describes a linter. A rewrite that lands a beautiful body under today's frontmatter produces a command that can describe what it would do and cannot do it. Also watch the scan-mode token at `:25`: it enumerates the classes by name, so it needs a shape that survives the next class too.
- **Phase 29 / task 29.1 / spec 103 — the blast-radius class, in flight.** *Watch:* it is correct and it is not the answer; §4 states the ship-or-absorb decision, which belongs to that roadmap's owner. Whichever way it goes, spec 103's grounded reading of the file (`:21`, `:23`, `:2-8` as an edit site, `:10`'s missing `grep`, `:25`'s closed token) is accurate and worth reusing verbatim in the larger work rather than re-deriving.
- **Handoff 09 — superseded in scope, kept in content.** *Watch:* do not read it as retracted. Every sentence in it about what the blast-radius class is and how it differs from the two existing classes still holds; only its premise — that one added class is the fix — does not.
