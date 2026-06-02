---
name: roadmap-decompose
description: >-
  Create or update a project roadmap with atomic, granular milestones. Each roadmap
  entry is a ~600-char contract line naming the key files, types, and guards, with
  the full spec persisted as a per-task note written by aif-note. Use when user says
  "decompose", "break down tasks", "spec tasks", "create tasks", or when adding
  milestones that need to be implementation-ready.
argument-hint: "[check | task description or requirements]"
allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion Skill
disable-model-invocation: true
---

# Decompose — Granular Task Planning

Create and maintain a project roadmap where every milestone is a two-tier entry: a contract line in the roadmap and a full spec note written by `aif-note`.

## Workflow

### Step 0: Load Project Context

**Read `.ai-factory/DESCRIPTION.md`** if it exists to understand:
- Tech stack (language, framework, database, ORM)
- Project architecture and conventions
- Non-functional requirements

**Read `.ai-factory/ARCHITECTURE.md`** if it exists to understand:
- Chosen architecture pattern and folder structure
- Module boundaries and communication patterns

### Step 1: Determine Target File and Mode

**Determine `$TARGET_FILE`** from the argument and conversation context:

- Default → `$TARGET_FILE = .ai-factory/ROADMAP.md`
- If the argument explicitly names a file (e.g. `ROADMAP_TESTS.md`) → `$TARGET_FILE = .ai-factory/<that file>`
- If the argument or conversation context is explicitly about writing **tests** (keywords: test, tests, spec, testing, тест, тесты) → `$TARGET_FILE = .ai-factory/ROADMAP_TESTS.md`

All subsequent steps use `$TARGET_FILE` as the roadmap path.

**Determine mode:**

If argument is `check` → Mode 3: Check Progress (requires `$TARGET_FILE` to exist)

Otherwise check if `$TARGET_FILE` exists:
- **Does NOT exist** → Mode 1: Create Roadmap
- **Exists** → Mode 2: Update Roadmap

---

### Mode 1: Create Roadmap (First Run)

**1.1: Gather Input**

If user provided arguments (task list or description):
- Use as primary input for milestones

If no arguments:
- Ask interactively:

```
AskUserQuestion: What tasks should I decompose into the roadmap?

Options:
1. Let me describe the tasks
2. Analyze codebase and suggest tasks
3. Both — I'll describe, you'll add what's missing
```

If user chooses to describe → ask follow-up:

```
AskUserQuestion: Any priorities or deadlines?

Options:
1. Yes, let me specify
2. No, just order by logical sequence
3. Skip — I'll reprioritize later
```

**1.2: Explore Codebase**

Scan the project to understand what's already built:
- `Glob` for project structure (key directories, modules)
- `Grep` for implemented features (routes, models, services)
- Check git log for completed work: `git log --oneline -20`

**1.3: Generate draft roadmap**

Draft the roadmap **in memory (do not write `$TARGET_FILE` yet)**. The format to build toward:

```markdown
# Project Roadmap

> <project vision — one-liner from DESCRIPTION.md or user input>

## Milestones

- [ ] **Task Name** — <contract line: problem today + the change + key files/types/guards>. Spec: `<note pending>`.
- [x] **Task Name** — <contract line>. Spec: `<note pending>`. (already done based on codebase analysis)
```

**Rules for milestones:**
- Each milestone is **one atomic task** — one file boundary, one concern, one reason to revert
- For each milestone: draft the full spec, run the **Atomicity Gate** (Step 1.3.1), then write a draft contract line with a placeholder `` Spec: `<note pending>`. `` — do **not** invoke `aif-note` yet; note invocations happen after the user confirms in Step 1.4
- Order by logical sequence (dependencies first)
- Mark already-completed milestones as `[x]`

**1.3.1: Atomicity Gate**

After drafting each milestone's full spec, before writing its draft contract line — apply the gate:

> "Can the first half be deployed without the second half and still make sense?"

If **yes** → split into two draft milestones, apply the gate to each half recursively until no half passes. Each gets its own draft contract line; both receive note invocations at Step 1.4 after confirmation.
If **no** → the milestone is atomic, write its draft contract line.

"Make sense" means: compiles, doesn't break existing functionality, and delivers some independently observable value.

**1.4: Confirm with user**

Show the draft roadmap and ask:

```
AskUserQuestion: Here's the proposed roadmap. What would you like to do?

Options:
1. Looks good — save it
2. Add more tasks
3. Remove/modify some tasks
4. Rewrite — let me give better input
```

Apply changes if requested, then finalize:

**After "Looks good — save it":** run the **Two-Tier Output** procedure (steps 3–5) for each confirmed milestone **sequentially** — invoke `aif-note` with that milestone's drafted full spec, capture the note path, and replace the placeholder `` Spec: `<note pending>`. `` with the real `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` — then write the final `$TARGET_FILE`. Milestones removed or rewritten during options 2–4 receive no note invocation; only the confirmed set gets notes.

---

### Mode 2: Update Roadmap (Subsequent Run)

**2.1: Read Current State**

- Read `$TARGET_FILE`
- Read `.ai-factory/DESCRIPTION.md` for context
- Explore codebase briefly to check what's changed since last update

**2.2: Determine Action**

If user provided arguments (new tasks/changes):
- Apply the requested changes directly

If no arguments:
- Analyze current state and present options:

```
AskUserQuestion: What would you like to do with the roadmap?

Options:
1. Review progress — check what's done, mark completed milestones
2. Add new tasks
3. Decompose existing — expand a vague milestone into a full spec
4. Reprioritize — reorder existing milestones
5. Rewrite — major revision of the roadmap
```

**2.3: Review Progress (if chosen)**

- Scan codebase for evidence of completed milestones
- For each unchecked milestone, check if the work appears done
- Propose marking completed milestones:

```
These milestones appear to be done:
- **Task Name** — [evidence: files exist, routes implemented, etc.]

Mark them as completed?
```

If confirmed:
- Change `- [ ]` to `- [x]` in the Milestones section

**2.4: Add New Tasks (if chosen)**

- Ask user to describe new tasks
- Explore the codebase for each new task (relevant files, current state)
- For each new task, run the **Two-Tier Output** procedure — invoke `aif-note` to write the spec note, then write the contract line with the `Spec:` tag
- Insert in logical order among existing milestones
- Update `$TARGET_FILE`

**2.4.1: Atomicity Gate**

After drafting each new task's full spec, before the note invocation — apply the gate:

> "Can the first half be deployed without the second half and still make sense?"

If **yes** → split into two tasks, apply the gate to each half recursively until no half passes. A split produces **two note invocations + two contract lines**.
If **no** → the task is atomic, proceed with the Two-Tier Output procedure.

"Make sense" means: compiles, doesn't break existing functionality, and delivers some independently observable value.

**2.5: Decompose Existing (if chosen)**

- List all `- [ ]` milestones with short descriptions
- Ask user which to expand
- Explore the codebase for the selected milestone
- Draft a full spec for it (what exists today, the exact change, files/types/methods to touch, guards, how to verify)
- Run the **Two-Tier Output** procedure with the following note-handling rule:
  - If the milestone already carries a `Spec:` tag, instruct `aif-note` to **update** the named note file in place (pass the exact existing note path as an explicit instruction to update rather than create). The contract line's `Spec:` tag stays unchanged.
  - If the milestone has no `Spec:` tag (legacy inline spec), invoke `aif-note` normally to create a new note, then replace the roadmap bullet with the contract line + the new `Spec:` tag.
- If the milestone bundles 2+ independent concerns, ask if user wants to split it (a split → two notes + two contract lines)
- Do not bulk-migrate pre-existing legacy inline tasks the skill isn't already touching

**2.6: Reprioritize (if chosen)**

- Show current order
- Ask user for new order or let them describe priority changes
- Reorder milestones in `$TARGET_FILE`

**2.7: Save Changes**

Update `$TARGET_FILE` with all modifications.

Show summary:
```
## Roadmap Updated

Total milestones: N
Completed: X/N
Next up: **Task Name**
```

---

### Mode 3: Check Progress (`/decompose check`)

Automated scan — analyze the codebase and mark completed milestones without interactive questions.

**Requires** `$TARGET_FILE` to exist. If it doesn't — tell the user to run `/decompose` first.

**3.1: Read roadmap and project context**

- Read `$TARGET_FILE`
- Read `.ai-factory/DESCRIPTION.md` for tech stack context

**3.2: Analyze each unchecked milestone**

For every `- [ ]` milestone:
- Determine what evidence would prove it's done (files, routes, models, configs, tests)
- Use `Glob` and `Grep` to search for that evidence
- Check `git log --oneline --all -30` for related commits
- Score: **done** (strong evidence), **partial** (some work started), **not started**

**3.3: Report findings**

```
## Roadmap Progress Check

Done (ready to mark):
- **Task Name** — found: src/auth/, JWT middleware, login/register routes

In Progress:
- **Task Name** — found: src/payments/ exists but Stripe webhook handler missing

Not Started:
- **Task Name**

Mark completed milestones? (N milestones)
```

**3.4: Apply changes (if confirmed)**

- Mark done milestones `[x]`
- Leave partial and not-started milestones unchanged

Show updated summary:
```
Completed: X/N milestones
Next up: **Task Name**
```

---

## Two-Tier Output (per task)

The canonical per-task procedure — referenced from Mode 2 (and from Mode 1's Step 1.4 finalization). Run this for every atomic task:

1. **Draft the full spec** for the task: what exists today, the exact change, files/types/methods to touch, guard conditions, how to verify completion.
2. **Apply the Atomicity Gate** to the full spec — if the gate passes (the spec covers two independently deployable halves), split into two tasks and run this whole procedure independently for each (two note invocations + two contract lines, sequentially).
3. **Invoke the `aif-note` skill via the Skill tool** to persist the full spec as a note. Scope the invocation to exactly one task: pass the task name as aif-note's `$1` slug argument (lowercase, hyphens) and supply that task's drafted spec text as the subject so aif-note does not blend it with sibling tasks or surrounding chatter. Tell aif-note the content is a task spec; do not override aif-note's template or otherwise alter its behavior.
4. **Capture the note path** aif-note reports back — its Step 4 prints `Note saved: .ai-factory/notes/<NN>-<slug>.md`. Use this path verbatim in the `Spec:` tag.
5. **Write the contract line** to the roadmap — target ~600 characters (range 400–1000; 1000 is an extreme edge), naming the key files, types, and guards (the "signature"), ending with the exact tag `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. ``

**Why two tiers:** the contract line lets the user verify intent while fitting 3–4 tasks on screen; the note holds the full implementation detail. The char budget is guidance, not a hard clamp.

**Sequential invocations only:** invoke `aif-note` one task at a time — one note fully written to disk before the next invocation — so aif-note's `NN` scan never collides. Never batch or parallelize note invocations within a run. A gate split's two invocations also run one after another.

**Never write a full spec inline in the roadmap** — the contract line is the header; the note is the implementation.

---

## Roadmap File Format

```markdown
# Project Roadmap

> <project vision — one-liner>

## Milestones

- [ ] **Name** — <problem today + the exact change + key files/types/guards involved>. Spec: `.ai-factory/notes/<NN>-<slug>.md`.
- [ ] **Name** — <same pattern>. Spec: `.ai-factory/notes/<NN>-<slug>.md`.
- [x] **Name** — <same pattern>. Spec: `.ai-factory/notes/<NN>-<slug>.md`.
```

**Rules for writing a contract line:**
- Name the specific files, methods, types, or fields involved — not just the module
- State the problem today before stating what needs to change
- Name guard conditions ("do not touch X", "skip Y") only for real pitfalls, not obvious things
- Target ~600 characters (range 400–1000) — enough to verify intent, short enough to fit 3–4 tasks on screen
- Always end with the `Spec:` tag pointing at the aif-note-written note file
- One reason to revert — if two concerns are independently shippable, make two milestones
- Full current-state / target / guards / verify detail lives in the spec note, not the roadmap line

## Critical Rules

1. **Milestones are atomic and specific** — each is one concern, one reason to revert
2. **`$TARGET_FILE` is the source of truth** — always read it before modifying
3. **Never remove milestones silently** — always confirm with user before removing
4. **Completed milestones stay as `[x]` in the list** — `roadmap-prune` moves them to ARCHITECTURE.md
5. **NO implementation** — this skill only plans, use `/aif-plan` to start a task and `/aif-implement` to execute
6. **Every task is two-tier** — a contract line in the roadmap plus a spec note written by `aif-note`; never write a full spec inline in the roadmap
