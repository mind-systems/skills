---
name: roadmap-test-coverage
description: >-
  Orchestrates full test coverage planning for a project. Filters areas by
  silent-failure risk, then researches each and writes up the findings. Use
  when you want a complete test plan from a roadmap with no prior test strategy.
argument-hint: "[roadmap-file]"
disable-model-invocation: true
user-invocable: true
allowed-tools: Read Glob Grep Bash(find *) Bash(npm *) Bash(npx *) Bash(dart *) Bash(flutter *) Bash(python *) Bash(pytest *) Bash(go *) Bash(cargo *) Bash(mkdir *) Bash(git *) AskUserQuestion Agent Write Skill
loads: test-philosophy roadmap-engine
---

# roadmap-test-coverage — Test Coverage Orchestrator

Eight-layer pipeline. Layers 4, 5, and 7 run in isolated agents to protect
the main context. Agents write results to disk and return only one-line
summaries back to the orchestrator.

Ensure `roadmap-engine` is loaded once this chat (via the Skill tool, only if not
already loaded) — it defines the named-roadmap resolution referenced below.

---

## Layer 1 — Load Project Context

Read in order (skip if absent):
- `.ai-factory/ARCHITECTURE.md` — module boundaries, folder structure
- The roadmap in play per `roadmap-engine`'s named-roadmap resolution order
  (explicit `$ARGUMENTS` wins, then "my roadmap", then the default
  `.ai-factory/ROADMAP.md`; see the engine's "Named roadmaps" section for the
  slug/owner mechanics) — all tasks

Store: `$STACK` (e.g. "NestJS/Jest"), `$TEST_CMD` (e.g. `npm test`),
`$ROADMAP_PATH`.

Infer stack from `package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`.

---

## Layer 2 — Coverage Scan

```bash
find . -name "*.spec.*" -o -name "*.test.*" | grep -v node_modules | grep -v dist | grep -v build
```

Read each completed and pending task in the roadmap. Group related
tasks into **candidate areas** — one area per logical component or
service. Each area maps to one or a few source files with a clear
responsibility boundary.

For each candidate area, classify:
- **No coverage** — no spec file for the target source file(s)
- **Partial coverage** — spec exists but visibly incomplete
- **Full coverage** — spec exists and appears thorough

Drop "Full coverage" areas. Carry forward "No coverage" and "Partial".

---

## Layer 3 — Silent-Failure Filter

Load `test-philosophy` once via the `Skill` tool, then apply its silent-failure
discriminator to each remaining candidate area.

Apply the filter to every area. Drop loud-failure areas.

Present the result to the user:

```
After silent-failure filter: N areas remain (dropped M).

[Kept — fails silently]
  - AreaName — src/path/to/file.ts
  - ...

[Dropped — fails loudly]
  - AreaName — reason (e.g. "TypeScript catches type mismatch immediately")
  - ...

Research all N kept areas? (y / let me pick)
```

Store confirmed list as `$RESEARCH_AREAS`.

---

## Layer 4 — Deep Research (parallel agents)

Determine next note number:
```bash
mkdir -p .ai-factory/specs
find .ai-factory/specs -name "[0-9][0-9]-*.md" | sort | tail -1
```
Extract highest two-digit prefix + 1. If none, start at `01`.
Store as `$NEXT_NOTE_NUM`.

Launch one `Explore` agent per area in a **single message** (parallel).
Each agent writes its note to disk and returns one line to the orchestrator.

**Agent prompt template:**

```
You are researching test coverage for one area of a codebase.

Area: <area name>
Source file(s): <file paths>
Existing spec file (if any): <path or "none">
Note to write: .ai-factory/specs/<NN>-<slug>.md

Your task:
1. Read the source file(s) in full — every public method, constructor args,
   internal branches, error paths, edge cases.
2. If a spec file exists, read it and identify what is covered and what is
   missing.
3. Identify dependencies that need to be mocked or faked.
4. Produce a structured list of test cases grouped by method or behavior.

For each test case write:
  - "should <expected behavior> when <condition>"
  - Which method/function it exercises
  - Any non-obvious setup needed

Write the following document to .ai-factory/specs/<NN>-<slug>.md:

# <Area Name> — Test Plan

**Date:** <YYYY-MM-DD>
**Source:** roadmap-test-coverage agent

## Source Overview
(2–3 sentences: what this class/module does, role in the system)

## Instantiation
(How to construct in tests: direct new X(), NestJS Testing module, etc.
List what needs to be mocked and how.)

## Existing Coverage
(What is already tested, or "None".)

## Test Cases
(Grouped by method. Use ### per group.)

## Gotchas
(Timers, private fields, fire-and-forget async, decorator bypass, invariants.)

After writing the file, return exactly one line:
saved: .ai-factory/specs/<NN>-<slug>.md
```

Collect all one-line confirmations.

---

## Layer 5 — Testability Review (parallel agents)

Launch one `general-purpose` agent per area in a **single message** (parallel),
passing `$STACK` from Layer 1 as `<stack>`. Each agent reads the source file
and returns a one-line verdict only.

**Agent prompt template:**

```
Testability review for: <area name>
Stack: <stack>
Source file: <file path>

Read the source file. Judge how much friction it costs to substitute each
dependency in a test, in this stack's own test idiom (pytest `monkeypatch` /
`unittest.mock.patch`, jest module mocks, etc.) — not whether the stack's DI
mechanism was used.

One criterion decides every case: does the API offer a parameter for the
thing a test must vary?

- **received** — the varying input arrives as a constructor param, function
  argument, or injected collaborator, so a test drives it by passing a
  value; module-level names touched only as static reference data are not
  substitution points either → no friction → `clean`.
- **no parameter for what varies** — varying data or a collaborator is
  acquired at construction or reached inside the call, and the API offers
  no parameter to supply it instead; the only way to vary it in a test is
  to patch the acquisition site, however cheap that patch → friction →
  `needs-refactor`, framed as friction.
- **unoverridable in this stack** — no patch point exists at all → blocking
  → `needs-refactor`, strong.

A reached function is not automatically a collaborator: when its behavior is
fully determined by the parameters the caller passes it, the test already
controls it by controlling those parameters, so calling it directly costs
nothing. It counts as a collaborator only when it supplies varying data or
an effect the test must control and the API offers no parameter for it.

The same construct sits in different bands in different stacks and call
sites — the names below are illustrations of the criterion, never a
universal checklist. Reading a module singleton, `os.environ`,
`get_config()`, or `datetime.now()` is not by itself the middle band; it
lands there only when it is data the behavior varies on and the API offers
no parameter to supply it instead. Whether the acquisition can fail is
irrelevant — a defensive `.exists()` guard returning a default adds no
parameter and does not clear the flag. The stack's patchability sets the
one-sentence verdict field's register (friction to drop, never
"untestable"), never the verdict.

Stack-conditional illustrations, TS/Node only:
- Fire-and-forget async (unawaited promises inside observable pipes,
  setTimeout without a returned handle) that complicates teardown
  assertions.
- Metadata extraction via unsafe casts ((req as any).user,
  (metadata as any)[KEY]) vs. a typed decorator param.
- process.env reads and Date.now() calls with no override point.

For the middle band, name the friction and the fix in the one-sentence
verdict field (e.g. "self-acquires its config at construction; inject it to
drop test-setup friction"). Never write "not injected" / "not DI", and
never write "untestable" for anything overridable in the stack.

Flag coupling only to the degree it taxes test setup. What the fence
clears is code with nothing to substitute — varying inputs arrive as
parameters and module-level names are read only as static reference data;
that is `clean`. Coupling that is merely ugly and costs test setup nothing
is out of scope — it belongs to a code-review lens, not a test-coverage
planner. The fence never clears a patchable acquisition of varying data:
cheapness of the patch is not the fence.

Do not weigh failure-loudness, silent failure, or whether the area deserves
a test at all — that discriminator is applied earlier in this pipeline.
Judge only the cost of authoring the test.

Return exactly one line in this format:
  clean | <area name>
  OR
  needs-refactor | <area name> | <one sentence: what to refactor and why>
```

Collect all verdicts.

---

## Layer 6 — Refactor Collect

For each `needs-refactor` verdict from Layer 5:

1. Append an entry to `$HANDOFF_LIST` (in-memory, carried through to
   Layer 8): area name + one-sentence refactor description (from the
   verdict) + pointer to its Layer-4 note path
   (`.ai-factory/specs/<NN>-<slug>.md`).
2. Open the corresponding Layer 4 note and append a `## Refactor Required`
   section: what to refactor, and what the post-refactor API will look like
   so the test implementer knows what to expect.

Log what was collected. No user confirmation needed — collect and continue.

---

## Layer 7 — Existing Tests Run

Run the test suite:
```bash
<$TEST_CMD>
```

If all tests pass: log "All existing tests pass."

If any tests fail, launch one `general-purpose` agent with the full test
output. The agent classifies failures only — it does not write any files.
The Class A / Class B split below applies `test-philosophy`'s After-the-Fact
Corollary — the agent runs in isolation and does not load the skill, so the
classification stays inline in its prompt.

**Agent prompt:**

```
A test suite was run and some tests failed. Classify each failure.
Do not fix anything. Do not write any files.

Test output:
<paste full test runner output>

For each failing test:
1. Read the test file to understand what it asserts.
2. Read the source file it tests to understand the current implementation.
3. Run: git log --oneline -10 <source file>
   Look for recent changes that could explain the failure.

Classify each failure:

  Class A — API drift: the source API changed (renamed method, new required
  arg, changed return shape) but the test was not updated. The test is
  outdated, not meaningful. Safe to patch.

  Class B — Silent bug: the source behavior changed in a way the test was
  designed to catch. The system would produce wrong output. The test is
  doing its job. Do NOT patch — escalate.

Return a markdown table only:

| Test (describe > it) | Source file | Class | Reason | Action |
|---|---|---|---|---|
| ... | ... | A or B | one sentence | patch test / escalate |
```

Present the classification table to the user.

**For each Class A failure:** patch the failing test to match the current
source API. Keep assertions intact — only update the call signature.

**For each Class B failure:** append an entry to `$HANDOFF_LIST` — area name +
reason from the classification table + the **source file** path (the
classification table's `Source file` column). The source file matters as a
fallback pointer: a Class B failure can belong to an area that never got a
Layer-4 note — Layer 7 runs the whole suite, so a failing test may sit in a
"Full coverage" area dropped in Layer 2, or a loud-failure area dropped in
Layer 3 — and those items have no note path. Do NOT touch the test.

Re-run `$TEST_CMD`. All tests must be green before Layer 8.

---

## Layer 8 — Hand Off

Print:

```
Test coverage research complete.

Notes written: N
  - .ai-factory/specs/<NN>-<slug>.md  (<area name>)
  - ...

Refactor items handed off: M
Existing tests patched (API drift): K
Class B items handed off: J

Next step: /roadmap-decompose
```

Then print `$HANDOFF_LIST` as concrete one-line task descriptions ready to
paste into `/roadmap-decompose`:

```
Handoff — paste into /roadmap-decompose:

Refactor:
  - <area name>: <refactor description>  (.ai-factory/specs/<NN>-<slug>.md)
  - ...

Bugs (Class B — silent failures):
  - <area name>: <reason>  (.ai-factory/specs/<NN>-<slug>.md)
  - <area name>: <reason>  (<source file> — area not researched)
  - ...
```

Per-item pointer: attach the Layer-4 note path when the item's area was
researched — always true for refactor items, and true for Class B items
whose failing test belongs to a researched area. Otherwise — for Class B
items from an area that was never researched (dropped in Layer 2 or 3) —
print the source file path captured in Layer 7. Every handoff line resolves
to a pointer; none are left blank.

Do not run `/roadmap-decompose` automatically.

---

## Critical Rules

1. **Never write new test files** — research and planning only. The one
   allowed exception: Layer 7 patching an existing Class-A (API-drift)
   failure — a test broken because the source API changed, not by an
   implementation bug. Keep assertions intact — only update the call
   signature.
2. **Never write ROADMAP_TESTS.md** — that is `/roadmap-decompose`'s job
3. **Layer 4 and 5 agents return one line** — never read note contents back
   into the orchestrator context
4. **Layer 7 agent classifies only** — the orchestrator patches, never the
   agent
5. **Class B failures are wins** — the test caught a silent bug; escalate,
   never suppress
6. **One note per area** — never merge multiple areas into one note
