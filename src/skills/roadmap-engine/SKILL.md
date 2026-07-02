---
name: roadmap-engine
description: >-
  Shared explanation of the canonical two-tier roadmap artifact format — a ~600-char
  contract line plus a full spec note written via note — plus the shared
  create/update/check roadmap-maintenance flow, applied by the calling agent.
  Caller-agnostic: holds no decomposition philosophy of its own. Load-once.
user-invocable: false
disable-model-invocation: false
allowed-tools: Read
loads: note
---

# Roadmap Engine — Shared Two-Tier Artifact Format

This is the shared explanation of the roadmap artifacts — the contract line, the spec
note, and the roadmap file format — not any decomposition philosophy. The calling
philosophy skill stays in control of what to build and when; this engine describes the
artifact format the caller applies once a task is decided. **Load this skill once per
chat** — once loaded, the format stays in context; never re-invoke it per task or per
mode.

## The two-tier artifact

Each milestone is a two-tier entry: a contract line in the roadmap plus a full spec
note at `.ai-factory/notes/<NN>-<slug>.md` (`<NN>` scanned against `.ai-factory/notes/`
so it never collides; `<slug>` lowercase-hyphenated). The contract line ends with the
exact tag `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. ``

The note follows `note`'s format — **load `note` once per chat** (via the Skill
tool, only if not already loaded), never per task.

**Why two tiers:** the contract line lets the user verify intent while fitting 3–4
tasks on screen; the note holds the full implementation detail. The char budget below
is guidance, not a hard clamp.

**Never write a full spec inline in the roadmap** — the contract line is the header;
the note is the implementation.

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
- Always end with the `Spec:` tag pointing at the spec note
- One reason to revert — if two concerns are independently shippable, make two milestones
- Full current-state / target / guards / verify detail lives in the spec note, not the roadmap line

## Roadmap maintenance flow

This is the shared interactive flow for creating, updating, and checking a roadmap
file — the calling philosophy skill applies it while staying in control of what to
build and when. The caller supplies the hook points listed below; the engine supplies
the mechanism around them. **Load this flow once per chat** — like the format above,
it stays in context once loaded; never re-invoke it per entry or per mode.

**Hook points (caller-supplied):**
- **(a) Granularity** — what one entry is and the rules for sizing it. The engine
  holds no opinion here.
- **(b) Per-entry gate (optional)** — a check the caller applies to each drafted
  entry before its contract line is written. The engine does not define or require
  one.
- **(c) Target-file routing** — which file the flow reads and writes (`$TARGET_FILE`).
  The engine never infers this; the caller resolves it before Step 0 runs.
- **(d) Extra update-mode actions** — the caller may register actions beyond the
  built-in menu (review progress / add / reprioritize).

### Step 0 — Project context

**Read `.ai-factory/DESCRIPTION.md`** if it exists to understand:
- Tech stack (language, framework, database, ORM)
- Project architecture and conventions
- Non-functional requirements

**Read `.ai-factory/ARCHITECTURE.md`** if it exists to understand:
- Chosen architecture pattern and folder structure
- Module boundaries and communication patterns

### Mode determination

If the argument is `check` → **Check mode** (requires `$TARGET_FILE` to exist).

Otherwise check whether `$TARGET_FILE` exists:
- **Does NOT exist** → **Create mode**
- **Exists** → **Update mode**

`$TARGET_FILE` itself is the caller's routing hook (c) — the engine never infers
which file it points to; it only branches on whether that file exists.

### Create mode (first run)

**Gather input:** if the caller's argument carries the input (vision, tasks, or
requirements), use it as the primary input. Otherwise ask interactively:

```
AskUserQuestion: <caller phrases this for its own granularity>

Options:
1. Let me describe it
2. Analyze codebase and suggest entries
3. Both — I'll describe, you'll add what's missing
```

If the user chooses to describe → ask a follow-up:

```
AskUserQuestion: Any priorities or deadlines?

Options:
1. Yes, let me specify
2. No, just order by logical sequence
3. Skip — I'll reprioritize later
```

**Explore the codebase** to understand what's already built: `Glob` for project
structure, `Grep` for implemented features, and `git log --oneline -20` for
completed work.

**Draft the roadmap in memory** — do not write `$TARGET_FILE` yet. Produce each
entry as a two-tier artifact per the format above, with a placeholder
`` Spec: `<note pending>`. `` on the contract line. Before writing a drafted entry's
contract line, apply the caller's per-entry gate (hook b) if one is supplied.

**Confirm with the user:**

```
AskUserQuestion: Here's the proposed roadmap. What would you like to do?

Options:
1. Looks good — save it
2. Add more entries
3. Remove/modify some entries
4. Rewrite — let me give better input
```

Apply changes if requested, then finalize: **only after "Looks good — save it"** —
write each confirmed entry's spec note, then replace its `` Spec: `<note pending>`. ``
placeholder with the real `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` tag, then
write `$TARGET_FILE`. Entries removed or rewritten during confirmation receive no
note — only the confirmed set gets notes.

### Update mode (subsequent run)

**Read current state:** `$TARGET_FILE`, `.ai-factory/DESCRIPTION.md` for context,
and a brief codebase check for what's changed since the last update.

**Determine the action:** if the argument carries the requested changes, apply them
directly. Otherwise present the action menu — the caller may register additional
actions beyond these (hook d):

```
AskUserQuestion: What would you like to do with the roadmap?

Options:
1. Review progress — check what's done, mark completed entries
2. Add new entries
3. Reprioritize — reorder existing entries
4. Rewrite — major revision of the roadmap
```

- **Review progress:** scan the codebase for evidence of completed entries; for
  each unchecked entry, check whether the work appears done; propose marking the
  confirmed-done entries `[x]`; apply on confirmation; leave the rest unchanged.
- **Add:** explore the codebase for each new entry, produce its two-tier artifacts
  per the format above (applying the per-entry gate hook if supplied), and insert
  each in logical order among existing entries.
- **Reprioritize:** show the current order, ask for the new order or let the user
  describe priority changes, then reorder entries in `$TARGET_FILE`.
- **Rewrite:** re-run the Create-mode draft→confirm cycle (gather input, explore,
  draft in memory, apply the per-entry gate hook, confirm) over the existing
  `$TARGET_FILE`, replacing its contents on confirmation.

**Save changes** to `$TARGET_FILE`, then show the update summary:

```
## Roadmap Updated

Total entries: N
Completed: X/N
Next up: **Entry Name**
```

### Check mode

Non-interactive scan — analyze the codebase and mark completed entries without
interactive questions.

**Requires** `$TARGET_FILE` to exist. If it doesn't, tell the user to run create
mode first.

For every open `- [ ]` entry:
- Determine what evidence would prove it's done (files, routes, models, configs,
  tests)
- Search for that evidence with `Glob` and `Grep`
- Check `git log --oneline --all -30` for related commits
- Score it **done** (strong evidence), **partial** (some work started), or
  **not started**

Report the three groups:

```
## Roadmap Progress Check

Done (ready to mark):
- **Entry Name** — found: <evidence>

In Progress:
- **Entry Name** — found: <evidence>, but <what's missing>

Not Started:
- **Entry Name**

Mark completed entries? (N entries)
```

On confirmation, mark the done entries `[x]`; leave partial and not-started entries
unchanged. Show the updated summary:

```
Completed: X/N
Next up: **Entry Name**
```

### Critical rules (mechanism)

1. **`$TARGET_FILE` is the source of truth** — always read it before modifying.
2. **Never remove entries silently** — always confirm with the user before removing.
3. **Completed entries stay as `[x]` in the list** — `roadmap-prune` moves them to
   `ARCHITECTURE.md`.

Philosophy-tier rules — granularity, the per-entry gate, and two-tier discipline —
stay with the caller; the engine holds none of them.
