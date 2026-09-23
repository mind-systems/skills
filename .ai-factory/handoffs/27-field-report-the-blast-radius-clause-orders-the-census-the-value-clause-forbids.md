# Handoff — field report: the blast-radius clause orders the census the value clause forbids

**Processed:** `[]` — whoever reads this marks it; a marked handoff is spent.

A field report from a project that runs `command-pin-gaps` daily. It carries no state you need. It proposes a repair to the command itself rather than applying one, and it closes with a question for the maintainer rather than an answer. It lands beside handoff `24-field-report-running-pin-gaps-to-exhaustion.md`, on the very clause that report already quoted — read together, they disagree about that clause's soundness, and this report explains why.

## Where this sits against 24

Handoff `24` already names the **Blast-radius holes** clause and its repair line — "a sweep whose enumeration goes into the task spec, never a sentence saying something may need updating" — and calls it the single most productive line in the skill, crediting it for catching whole files a descriptive clause would have missed. That praise is not wrong about what the clause catches. It is silent about what the clause writes down once it catches it, which is this report's whole subject. Nothing below repeats `24`'s corollaries about vacuous negative assertions, unsatisfiable requirements, or verifying evidence versus instruction — those stand as written, and this report does not touch them.

## The finding

`src/commands/command-pin-gaps.md` — the source behind `active/commands/command-pin-gaps.md` — instructs, in its **Blast-radius holes** clause: "Repair: a `Grep`/`rg` sweep whose enumeration goes into the task spec, never a sentence saying something may need updating." That enumeration is a census of code positions, and a census written into a task spec is perishable in exactly the way the same command already refuses in its own **Value holes** clause. A run holding this instruction writes, faithfully, sentences of the shape "exactly two production callers", "four call sites, all in this repo", "thirteen files reference the type", "×2, in two different handlers" — each true when written and false the moment the first task that touches that surface lands.

The field consequence is why this earns a report rather than a note to self: one task gets implemented and every other spec has quietly drifted, and then the orchestrator trips over the drift the enumeration left behind. This failure is worse than ordinary staleness, because a tally carries false authority — a reader treats a number as verified where a sentence would have invited a check. Nothing reports the rot, and the census is exactly the kind of statement a planner leans its scope decision on.

## The asymmetry inside the same file

The **Value holes** clause already gets this exactly right, and for the reason it states plainly: pin the value "naming its source as the file and the name of the thing inside it that holds the value — a symbol, a heading, a bold lead-in — never a line number, because the spec outlives the numbering it was written against." That reasoning is the whole argument, already written down, in the same command. It simply never reached the **Blast-radius holes** clause a few lines below it, where the perishable thing is a tally of call sites rather than a line number. Same mechanism — an address or a count that survives only until the next unrelated edit — different clothes: one clause protected against it, the other still orders it.

## Contract, census, measurement

"Don't enumerate" alone would break the clause's real purpose — the sweep is the whole reason the clause catches what a hedge would miss. The distinction the repair needs to encode:

- **Contract — keep.** A protocol's member set with full signatures. A pinned value, enum case, error code, or literal. A type or file name. A decision about scope — "this holder moves to the protocol, the others stay on the concrete type" is a contract even though it concerns many files, because the decision is the content and the roll-call naming each file is not.
- **Census — remove.** How many call sites exist, how they distribute across files, which handler holds more than one of them.
- **Measurement — keep, and it is not a census.** A dated test-run result — these fixture cases fail on today's code, measured on this date — records an experiment, not a code position. It stays true for its date, and a reader knows on sight to re-run it rather than trust it forever.

## The repair, concretely

In the **Blast-radius holes** clause, the repair form becomes: the **rule** that defines the affected set, plus the **literal sweep** that finds it on demand, plus the **invariant** the sweep's result must satisfy after the change — replacing the sweep's own enumeration, not the sweep itself.

The clause's tail stays correct exactly as written: "A sweep too large to enumerate is itself a finding: report the search and its count with owner `roadmap-decompose`." That count goes into a chat report to the orchestrator, which is ephemeral and dated, not into a spec that outlives it. The spec/report boundary is the thing any edit here must preserve — the finding-report line already respects it; only the ordinary-sized repair line does not.

## What this does not propose

Not banning sweeps — the sweep is the clause's own point. Not banning counts in reports — the finding-report line above already carries one correctly. Not touching the **Value holes** clause, which needs nothing; it is the model, not the patient.

## Field evidence: `substitutable-setup-managers`

In the broker repository this session, censuses were swept out of specs `command-pin-gaps` had just written, replaced with the rule-sweep-invariant form. Name the worked example rather than tallying it: `tradeoxy_broker/.ai-factory/specs/0011-substitutable-setup-managers.md`'s **Blast radius** section read as a roll-call of call sites split across `SubscriptionController.swift` and `StrategySettingsController.swift`, naming which handler held more than one call on the same method. It became: the rule that every call through `App.shared.strategySettingsManager` or `App.shared.subscriptionManager` has its receiver's compile-time type change; the literal `grep -rn "App\.shared\.strategySettingsManager\|App\.shared\.subscriptionManager" Sources/` that lists them on demand; and the invariant that every match resolves to a member already named on the new protocol, so the conversion compiles with no source edit. The scope decision this section also carried — which manager moves, which stays — is a contract and survived untouched; only the roll-call went.

## Blast radius of the proposed edit

Stated as the rule plus its sweep, the way the repair itself asks for, rather than as a list: the command is shared across every project that loads it, so a change to its wording alters what every run of it writes from the moment it lands. And the same prescription may not be unique to this one clause — `src/commands/command-pin-gaps.md` itself attributes the **Blast-radius holes** clause's shape to a root definition it does not restate: `roadmap-engine`'s "What a task spec holds" paragraph, in `src/skills/roadmap-engine/SKILL.md`, names *what breaks on contact* as "enumerated rather than hedged" — the same instruction, one level up, feeding every skill that loads `roadmap-engine` for its task-spec shape, not only this command. Fixing the clause here while leaving that root paragraph as it stands would repair the branch and leave the root ordering the same census back into it. The rule for anyone editing this: sweep `src/skills/` and `src/commands/` for the enumeration-into-spec instruction (`rg -n "enumerat" src/`) before editing, and treat `roadmap-engine`'s own paragraph as a match to weigh, not a separate question — so one clause is not fixed while the definition it cites keeps ordering the census.

## An open question, left open

Whether the specs already carrying censuses in other projects are worth a sweep of their own, or whether they are left to rot and get corrected on contact, the way this session's own were. We fixed ours; we cannot see the others.
