---
name: roadmap-decompose
description: >-
  Create or update a project roadmap with atomic, granular, descriptive milestones.
  Generates .ai-factory/ROADMAP.md where each entry is a fully specified task: what
  exists today, what needs to change, which files and methods to touch, and explicit
  guard conditions. Use when user says "decompose", "break down tasks", "spec tasks",
  "create tasks", or when adding milestones that need to be implementation-ready.
argument-hint: "[check | task description or requirements]"
allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion
disable-model-invocation: true
---

# Decompose — Granular Task Planning

Create and maintain a project roadmap where every milestone is a fully specified, atomic task.

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

**1.3: Generate roadmap file**

Create `$TARGET_FILE` (ensure parent directory exists: `mkdir -p .ai-factory`) with this format:

```markdown
# Project Roadmap

> <project vision — one-liner from DESCRIPTION.md or user input>

## Milestones

- [ ] **Task Name** — [full spec — see format below]
- [x] **Task Name** — [full spec] (already done based on codebase analysis)
```

**Rules for milestones:**
- Each milestone is **one atomic task** — one file boundary, one concern, one reason to revert
- Write a full spec for each (see ROADMAP.md Format section below)
- Order by logical sequence (dependencies first)
- Mark already-completed milestones as `[x]`

**1.3.1: Atomicity Gate**

After drafting each milestone description, before writing to file — apply the gate:

> "Can the first half be deployed without the second half and still make sense?"

If **yes** → split into two milestones, then apply the gate to each half recursively until no half passes.
If **no** → the milestone is atomic, proceed.

"Make sense" means: compiles, doesn't break existing functionality, and delivers some independently observable value.

**1.4: Confirm with user**

Show the generated roadmap and ask:

```
AskUserQuestion: Here's the proposed roadmap. What would you like to do?

Options:
1. Looks good — save it
2. Add more tasks
3. Remove/modify some tasks
4. Rewrite — let me give better input
```

Apply changes if requested, then save to `$TARGET_FILE`.

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
- Write a full spec for each (see ROADMAP.md Format section)
- Insert in logical order among existing milestones
- Update `$TARGET_FILE`

**2.4.1: Atomicity Gate**

After drafting each new task description, before inserting into the roadmap — apply the gate:

> "Can the first half be deployed without the second half and still make sense?"

If **yes** → split into two milestones, then apply the gate to each half recursively until no half passes.
If **no** → the milestone is atomic, proceed.

"Make sense" means: compiles, doesn't break existing functionality, and delivers some independently observable value.

**2.5: Decompose Existing (if chosen)**

- List all `- [ ]` milestones with short descriptions
- Ask user which to expand
- Explore the codebase for the selected milestone
- Rewrite its description as a full spec (see ROADMAP.md Format)
- If the milestone bundles 2+ independent concerns, ask if user wants to split it

**2.6: Reprioritize (if chosen)**

- Show current order
- Ask user for new order or let them describe priority changes
- Reorder milestones in `.ai-factory/ROADMAP.md`

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

✅ Done (ready to mark):
- **Task Name** — found: src/auth/, JWT middleware, login/register routes

🔨 In Progress:
- **Task Name** — found: src/payments/ exists but Stripe webhook handler missing

⏳ Not Started:
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

## Roadmap File Format

```markdown
# Project Roadmap

> <project vision — one-liner>

## Milestones

- [ ] **Name** — [current state: what exists and what's wrong or missing]. [Target: specific files, methods, or types to change; exact behavior to implement; guard conditions inline if needed.]
- [ ] **Name** — [same pattern]
- [x] **Name** — [same pattern]
```

**Rules for writing a description:**
- Name the specific files, methods, types, or fields involved — not just the module
- State what exists today before stating what needs to change
- Add guard conditions inline ("do not touch X", "skip Y") only for real pitfalls, not obvious things
- One reason to revert — if two concerns are independently shippable, make two milestones
- A reader with no prior context must understand exactly what to do from the description alone

## Critical Rules

1. **Milestones are atomic and specific** — each is one concern, fully described, not a bundle of loosely related changes
2. **`$TARGET_FILE` is the source of truth** — always read it before modifying
3. **Never remove milestones silently** — always confirm with user before removing
4. **Completed milestones stay as `[x]` in the list** — `roadmap-prune` moves them to ARCHITECTURE.md
5. **NO implementation** — this skill only plans, use `/aif-plan` to start a task and `/aif-implement` to execute
