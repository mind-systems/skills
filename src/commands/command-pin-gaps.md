---
description: >-
  Scan a plan, task, phase, or task spec for where the implementing agent
  would have to guess: read the task, its task spec, and the code it lands
  in, walking the task's transformation into the code along named
  references to the leaf, then reason the way the orchestrator would plan
  and review it. Reports three finding classes: value holes (an unpinned
  value from the code), meaning holes (an undefined edge, or a constraint
  no document states, routed to its owner), and blast-radius holes (what
  the change breaks elsewhere in the repository). Closes what it can in
  place. Pass "scan" to only list findings without editing.
argument-hint: "[path | scan]"
allowed-tools: Read Edit Grep Glob Bash(ls *) Bash(rg *) Bash(git *) Skill
loads: roadmap-engine
---

Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not
already loaded) — it defines the named-roadmap resolution referenced below.

Target, in priority order: the file(s) in `$ARGUMENTS`, if given — else the scope under discussion in chat (a named task, phase, or task spec) — else all open `- [ ]` tasks of the roadmap in play per `roadmap-engine`'s named-roadmap resolution order (explicit argument → "my roadmap" → default `.ai-factory/ROADMAP.md`; see the engine's "Named roadmaps" section for the slug/owner mechanics) above `---STOP---`, scanning each contract line and its `Spec:`-tagged task spec.

Any question that would need an answer *during implementation* is space for the agent to fantasize. Close all of it now.

The walk answers it. The command reads the task, its task spec, and the code the task lands in, following named references to the leaf — depth along named edges, never a sweep across unrelated branches — and it walks what the orchestrator will do with the task: how the planner would build a plan for it against this code, and how the reviewer would judge the implementation that comes back. That emulation is a way of reasoning toward the finding list; it produces no plan and no verdict, and no prompt of the orchestrator's is carried into this file or named in it.

The unit of the walk is one behavior the task claims. Each such behavior either ends at a `file:line` landing in the code or becomes a finding; the walk descends into code the named files themselves reference only as far as that behavior's landing requires, never past the question. Two questions decide a finding: would the run, holding this task and nothing else, have to invent — and can the task be implemented on the code that exists at all.

The pass does not locate the phase, does not read the pointers on its header, and reports nothing about their presence or absence — that tier belongs to `roadmap-outline-deep` and `roadmap-decompose`. Reading a document to understand the task is ordinary and needs no branch of its own, exactly as the orchestrator reads one when it needs one. Behavior the task wants that no governing document describes is a hole like any other: change moves one way, docs → roadmap → code, and the documentation is the foundation the code stands on. The weight of the pass sits on the code side — nothing in the family has looked there until now.

A task states how the docs currently differ from the code and what it will change; a hole is wherever that statement fails to connect. **Toward the code:** desired behavior with no landing — no file named, no call site, an existing shape it must fit that nobody looked at, work already half-done, something that breaks on contact. This end is the one no other skill owns. **Toward the docs:** behavior the task assumes that no document states, because it surfaced during decomposition rather than during specification — the hole is then in the governing spec, not in the task, and the command points there.

The two ends are not classes: every finding carries exactly one of three, and the end shows only in how it closes — in place, or `owner: <skill>` in the scan line's `fix` token. A missing file or call site is a value hole; an existing shape nobody looked at, or work already half-done, is a meaning hole; something that breaks on contact is a blast-radius hole.

A task spec that repeats a paragraph from a document instead of linking to it is not a finding. An agent does not reliably walk to the leaf — it guesses a file's content from its name — so the copy earns its place; it goes stale, and that is proper to this tier, because the roadmap is the perishable seam between the documentation and the code, pruned as it closes, unlike the two surfaces it sits between.

**The shape it repairs toward:** a task spec holds three parts — *what is true now*, *what must be true after*, *what breaks on contact* — defined in `roadmap-engine`'s "What a task spec holds" paragraph and not restated here; each hole class supplies exactly one of them. A class is named by the part its repair supplies, never by the part that went unread: a value hole is closed by pinning *what is true now*, a meaning hole by deciding *what must be true after* — which is why an existing shape nobody looked at is a meaning hole, the fit it must satisfy being what is undecided — and a blast-radius hole by enumerating *what breaks on contact*. The three classes are therefore the whole of what "all of it" means above: with none of them left open the spec is whole and the pass stops.

**What the pass never writes:** it pins values and enumerates breakage, and it never authors a verification check — no step, command, or bullet whose only job is to confirm the instruction was carried out. Such a check can only fail where the instruction was ignored, and by `test-philosophy`'s discriminator that is a loud failure, which is not written. A surface that fails silently still owes a test, routed to its owner as below.

**Value holes:** TODO/TBD/«решим по ходу», unpinned symbols (enum names **and values**, error codes, exact strings, versions, paths, field **types**), magic numbers, a missing file or call site. Repair: read the code/proto and pin the **exact** value, naming its source as the file and the name of the thing inside it that holds the value — a symbol, a heading, a bold lead-in — never a line number, because the spec outlives the numbering it was written against; never invent.

**Meaning holes:** undefined behavior at the edges (error/timeout/reconnect/cancel/empty/race), open forks («либо…либо») with no decision, an unnamed invariant or interaction contract between components the task touches, an undrawn scope boundary (which files/services are outside the task's zone), unstated task ordering, an existing shape nobody looked at, work already half-done. Repair: write the missing constraint as a spec clause derived from the observed behavior of the actual code, citing the code that grounds it where a concrete source exists; when the code can't settle it (genuine product decision), don't fabricate it — raise it as a one-line question under `## Blocking decisions` at the top of the file. When the missing constraint is behavior no document states, route it instead: name `aif-docs` as the owner rather than writing the clause from the code.

**Blast-radius holes:** what the repository already contains that this change breaks — a caller, a format, an assumption elsewhere in the code that the change invalidates on contact. Repair: a `Grep`/`rg` sweep whose enumeration goes into the task spec, never a sentence saying something may need updating. A contradiction that resolves against the code is closed in place; a fundamental conflict, or code that does not come apart, is raised as an explicit blocker instead of being quietly repaired. A sweep too large to enumerate is itself a finding: report the search and its count with owner `roadmap-decompose`, never filed under `## Blocking decisions`.

A task that cannot be planned coherently belongs to `roadmap-decompose` or `roadmap-decompose-skeleton`; behavior no document describes belongs to `aif-docs`; a surface that fails silently, by `test-philosophy`'s discriminator, owes a test. The command names which one and performs none: it does not decompose, does not write documentation, does not author tests, and loads none of the four. A hole it can close in place it closes, exactly as today; a hole whose repair belongs elsewhere is reported, in both modes. Judging a task too large, and judging a behavior undocumented, are comparative — from inside one task every task looks normal-sized; both are made where the whole roadmap is readable, which is where this command runs.

**scan mode** (`$ARGUMENTS` contains `scan`/`report`/`только скан`): list findings as `[file:line|spec-location] → value|meaning|blast-radius → what's missing → fix`, where `fix` reads `owner: <skill>` for a hole whose repair belongs elsewhere, and stop.
**default:** edit the file in place — replace each vague spot with the concrete value, spec clause, or sweep enumeration — then report `N closed from source · M blocking · K owned elsewhere`.
