# 56.1 — a gate red before the task began

**Project:** tradeoxy_core
**Date:** 2026-09-25
**Stopped at:** planned:3
**Elapsed before the rescue:** 987

This run was an experiment, and it is recorded as one. Phase 56 was decomposed with `roadmap-decompose` alone. Neither the skeleton pass nor the pin-gaps pass ran over it, and the aim was to see how executable a freshly decomposed task is on its own. The phase is small and its design was settled before decomposition. It gives the order-event payload the canonical subscription id core already holds, and moves the room name, the runtime's slot routing and the replay gate onto that id instead of the broker's raw string. The phase's first task stopped in planning.

The first reading found the plan faithful to its specification and raised two things. A test comment beside the runtime's routing case would go on describing the comparison the task retires. The compiler would also make the sweep edit a second test file outside the two directories the specification named, and that file was absent from the acceptance run. The specification itself was wrong on the second point: it called another suite «the one file this task reaches outside those two directories». The planner took both.

The second reading found three new and unrelated defects, all in the plan's precision. The new test case had no label. The test file's own header omitted an existing `7d` case, so anyone numbering by the header would have picked a label already in use. A comment in a neighbouring suite cited the target file by line range, and the task's insertion would shift that range. The plan also gave one test constant the wrong origin. All three were closed.

The third reading ran the whole plan in a throwaway worktree. The compiler named exactly the sites the plan's sweep rule covered, and both new cases passed against the new readers and failed against the old ones. The plan was proven. What stopped the run was the gate: the acceptance set was red on the untouched tree before any change. Two failures sat in it, neither related to the task:

- a narrow-teardown scenario left red on purpose against a stub by an earlier skeleton task;
- a replay-stream case that fails only under a parallel sweep.

The plan named neither, so an implementer holding a red gate had three bad exits: report failure, fix a stub that was not its own, or loop on a flake. Planning attempts ran out on that finding.

Both reds were known to the planning pair. They sat in the architect's own buffer as orientation facts. The first had already stopped this project's previous rescue, the one-value load-state task, for the same reason: a gate demanding green from a suite carrying a deliberately red skeleton. That repair fixed the one specification. It left no rule that a gate is run on the tree before it is pinned, and so the failure repeated one phase later. A fact the pair holds reaches the planner only through the specification.

> The specification pinned an acceptance run that is red at HEAD for reasons outside the task, and named neither the known failures nor the result expected in their presence.

**Root-cause category:** specification gap. It concerns the specification's claims about the environment the task lands in, not its design, which the third reading proved sound. **Recurring signal:** no finding recurred across rounds; each round closed its own. One inaccuracy did repeat as a deferred observation in all three readings: the specification named a sibling test case as driving the routing handler, and it does not.

## What was done

The rescue did not take a depth from the menu. After the diagnosis, the user ruled to roll back only what the run had generated. The plan, its sidecar and the three plan-reviews were deleted, and nothing had reached source. That is a full reset, and it discarded a plan the third reading had proven.

The specification tier was then repaired by a pin-gaps pass, instead of by the rescue's own edit to this one task. It covered all three tasks of the phase in order. For each task, the architect and the editor walked the task independently against the code and reconciled, and the editor applied the agreed repairs. The phase-wide pass is what made the rescue worth more than the task. It found five holes in each task: fifteen closed from source, none blocking, none owned elsewhere. Several sat in the tasks not yet run and would have failed them the same way, or worse, silently:

- **The replay task.** Its gate carried both known reds plus a third the architect did not hold: a registry skeleton red in every scenario.
- **The replay task's parameter position.** Nothing pinned where its new parameter goes. Appended last, it would have left the only compiler-blind test double passing while still asserting the retired read.
- **The replay task's coverage.** The one case it placed could not reach either surface it claimed to prove, because the runtime in that suite is a mock. The proof now lives in three suites, each reaching the surface it proves.
- **The broker handoff task.** Its cross-repository link would have broken in the destination tree. A broker handoff still carried core's claim that its replay register door refuses a mixed-case id, which has been false since that door moved to the case-insensitive parser. And one snapshot mapping lowercases two ids where the specification named one.

The finding of the experiment is narrower than "decomposition is not enough". The decomposed specifications were right about what to change and why; every reading of the design agreed with it. They were wrong about the ground the change lands on: what the gate returns today, which files the compiler will reach, which test sits where, what a mock can prove, what a link resolves to from where it will live. That is exactly the tier pin-gaps exists for. The skeleton pass would most likely have returned nothing here, as it correctly does on wiring work, so this run measured the absence of the pin-gaps pass alone. Planning attempts cost sixteen minutes, lost on one hole that a single command run on the tree would have exposed. The pass that closed it found the same class of hole in every task of the phase.

The repaired specifications and the architect's buffer were committed. A new method rule went into the buffer: a specification's gate is run on HEAD before it is pinned, and every known red is named in it. The phase is ready to run again from its first task.
