# 80.1 — the report is the chronicle

## What is true now

`src/skills/task-rescue/SKILL.md`, § "Step 5.7 — Write the durable report", writes one report per run through `note`. Its "When" paragraph says the report is written once, at the end, when the repair is done, that `note` is invoked exactly once per run, that the file "is never reopened, by this run or a later one", and that a run that ends before the step leaves no report. Its "Which runs" paragraph lists the terminating branches and excludes the scope-overload exit of Step 4, which writes none. Its last paragraph, "The chat printout is unchanged", says the Diagnosis Report is still printed, that the file is additional, and that "no step of this skill ever reads it back". The template holds five header lines (`Project`, `Date`, `Stopped at`, `Elapsed before the rescue`, `Sessions`), the diagnosis "exactly as Step 3 wrote it", and a "What was done" section. Nothing in it says who found a finding. The paragraph "When the write cannot happen" says never to invoke `note` a second time and never to defer the write.

§ "Step 3 — Extract root cause" says nothing about writing a report, and § 5.7 sits after § 5.6, so no step in the order of the steps makes the first write. Step 3 tells the narrative to be "Domain language only" and ends that paragraph with a sentence forbidding iteration counts, PASS markers, phase names and the sidecar in it. § "What NOT to do" repeats the rule as a bullet that forbids presenting the orchestrator's mechanics as the problem, with a clause that it constrains the output and not the analysis.

The report folder `.ai-factory/rescue-reports/<project>/` shows the cost. Reports name a finder only in passing sentences, and a rescue's own repair can carry a defect found long after the report was written: the report for 88.6 in `tradeoxy_core` was extended by a head with a dated section after the rescue, and that section holds the defect the diagnosis missed. A reader of the folder cannot tell who found what, or at which moment. `orchestrator-artifacts`, § "Sidecar fields", names the session keys the sidecar holds: `planner`, `implementer`, and `plan-reviewer-<N>` per attempt; the plan-review and review files carry their round number in their names.

The user, on the line that records who found each finding: «да это нужно. Иначе я не могу принять решение - могу ли я пустить пайплайн на самотёк.»

## What must be true after

Step 3 ends with the first write of the report, made per § 5.7 through `note`, with the destination, the three hooks and the topic slug as they stand; the order of the steps carries it. The rescue keeps the path `note` returns, and the file is extended while the rescue is hot: each addition is a section headed by its date, appended, and the lines already in the file stay as written. The additions are appended directly, not through `note`. "When the write cannot happen" keeps its two rules.

The first write holds the five header lines, the diagnosis, and a section that records who found what, outside the diagnosis, which keeps its prose form. The `Stopped at` line holds the sidecar's `step` and what stopped the run: the review cycle spent at its round, or the role that escalated; the template has no second line for the stop. The section holds:
- a line for who found the root cause, separate from the stop;
- each finding the diagnosis names, with who found it and when.

Who is one of: the user; head N, by its number; the editor; the plan-reviewer or the reviewer at round R; the implementer or the planner; the rescue itself. When is one of: before the run; in the run; in the rescue; after the rescue, for a defect in the repair itself. The role and round come from the sidecar's session keys and the number each plan-review and review file carries; the user and the heads come from the conversation. A finder that no artifact and no conversation states is written as not stated.

The "What was done" section leaves the template. What it held, what the repair did and what was deleted or kept, is the first section appended once the repair is made.

The "When", "Which runs" and "The chat printout is unchanged" paragraphs are gone, and nothing in § 5.7 says the report is written once, at the end, or never read back.

In Step 3 the paragraph on the narrative keeps its instruction that the narrative describes what the task spec and the contract line stated wrongly or left ambiguous, and how the plan or the code went wrong as a consequence; its label and its sentence on the orchestrator's vocabulary go, and the narrative may name a round and a reviewer. In § "What NOT to do" the bullet on presenting the orchestrator's mechanics as the problem goes with its clause on output and analysis.

## What breaks on contact

**Rule:** a text breaks on this change if it says the report is written once, at the end, or never reopened or read back, that some run writes none, or that the narrative must avoid the pipeline's own words.

**Sweep:**
```
grep -n -E "reopened|exactly once|reads it back|Zero orch|orchestrator mech" src/skills/task-rescue/SKILL.md
```

**Finding.** The search returns the "When" paragraph and the printout paragraph of § 5.7, the sentence in Step 3 and the bullet in § "What NOT to do"; each is a target. Step 1's capture of the report facts stays: the sidecar is still overwritten by a repair, and the report names the sidecar's keys.

Outside the skill nothing needs a change. `docs/the-pipeline-speaks-to-an-architect.md`, § "The report travels on", says a head is told when the report is written, and it is told at the first write. `docs/self-analysis.md` asks the author of a report who read what and when; the new section is where the file answers it. `note` keeps its own rules: the appended sections are the rescue's own writes.
