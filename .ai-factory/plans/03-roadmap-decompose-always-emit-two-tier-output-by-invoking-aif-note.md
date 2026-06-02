# Plan: roadmap-decompose — always emit two-tier output by invoking aif-note

## Context
Make `roadmap-decompose` emit two-tier output on every run: for each atomic task it invokes the `aif-note` skill itself to write the per-task spec note, then writes a roadmap **contract line** (~600 chars, names files/types/guards) ending with a `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` tag — replacing today's inline-full-spec output.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Two-tier mechanism

- [x] **Task 0: Add `Skill` to `allowed-tools` and refresh the frontmatter `description`** (load-bearing — must land first)
  Files: `.claude/skills/roadmap-decompose/SKILL.md`
  **Blocking fix (review 1 finding 1, review 2 critical issue 1).** The central mechanism — invoke `aif-note` via the Skill tool — requires `Skill` in the skill's `allowed-tools`, which is currently absent. Change the frontmatter line `allowed-tools: Read Write Edit Glob Grep Bash(git *) AskUserQuestion` to also include `Skill` (precedent: `.claude/skills/aif/SKILL.md`, the only other sub-skill-orchestrating skill, declares `Skill` in its allowlist). Without this the invocation may be blocked or surface a permission prompt mid-run — the exact flakiness this feature exists to remove.
  Also update the frontmatter `description` (review 1 finding 2 / review 2 finding 3): it currently says each roadmap entry is "a fully specified task: what exists today, what needs to change, which files and methods to touch, and explicit guard conditions." Reword so it reflects the new shape — each roadmap entry is a ~600-char **contract line** naming the key files/types/guards, with the full spec living in a per-task note written by `aif-note`. Keep it ≤ 1024 chars and preserve the existing trigger keywords ("decompose", "break down tasks", "spec tasks", "create tasks").

- [x] **Task 1: Add a shared "Two-Tier Output" procedure block and update Critical Rules** (depends on Task 0)
  Files: `.claude/skills/roadmap-decompose/SKILL.md`
  Insert a new subsection (e.g. just above "## Roadmap File Format") titled **Two-Tier Output (per task)** that defines the canonical per-task procedure once, so the mode steps reference it instead of repeating it. Spell out the operation order, mirroring note 09's order but with delegation:
  1. Draft the **full spec** for the task.
  2. Apply the **Atomicity Gate** to the full spec — a split yields **two** tasks, each runs this whole procedure independently (two note invocations + two contract lines).
  3. **Invoke the `aif-note` skill via the Skill tool** to persist that task's full spec as a note. **Scope the invocation to exactly one task** (review 2 finding 2): name the specific task, pass its **task name as aif-note's `$1` slug argument** (this is aif-note's documented input, not a behavior override), and quote/delimit *that task's drafted spec text* as the subject so aif-note does not blend it with sibling tasks or surrounding decompose chatter. Tell aif-note the **content is a task spec** (what exists today, the exact change, files/types/methods to touch, guards, how to verify) but **do not** override aif-note's template, limit its capabilities, or otherwise alter its behavior.
  4. **Capture the `.ai-factory/notes/<NN>-<slug>.md` path aif-note reports back** (its Step 4 prints `Note saved: …`) — use the reported path verbatim so the `Spec:` tag is always accurate.
  5. Write the **contract line** to the roadmap — the interface, **target ~600 characters (range 400–1000, 1000 = extreme edge)**, naming the key files / types / guards (the "signature"), **ending with the exact tag** `` Spec: `.ai-factory/notes/<NN>-<slug>.md`. `` pointing at the captured note path.
  Encode the rationale inline: this length lets the user verify intent while still fitting 3–4 tasks on screen; the note is the implementation, the line is the header; the char budget is guidance, not a hard clamp. State explicitly: one note per atomic task, written **after** the gate passes; never write a full spec inline in the roadmap. **Invoke aif-note strictly sequentially** (review 2 finding 4) — one note fully written to disk before the next invocation — so aif-note's highest-`[0-9][0-9]`-prefix scan never collides; never batch/parallelize the note invocations within a run (a gate split's two invocations run one after another).
  In "## Critical Rules" add one rule: *every task is two-tier — a contract line in the roadmap plus a spec note written by `aif-note`; never write a full spec inline in the roadmap.*

- [x] **Task 2: Wire Mode 1 into the two-tier procedure** (depends on Task 1)
  Files: `.claude/skills/roadmap-decompose/SKILL.md`
  In **Step 1.3 (Generate roadmap file)** change the output instruction from "Write a full spec for each (see Format section)" to: for each milestone, run the **Two-Tier Output** procedure — invoke `aif-note` to write the spec note, then write the contract line with the `Spec:` tag. Update the inline `# Project Roadmap` example so the bullets show the contract-line + `Spec:` tag form, not inline specs. Keep **Step 1.3.1 (Atomicity Gate)** intact; make its placement consistent with the procedure (gate runs on the full spec, before the note/contract line are written) — a split produces two notes + two contract lines. Do not restructure the mode or the gate.

- [x] **Task 3: Wire Mode 2 into the two-tier procedure** (depends on Task 1)
  Files: `.claude/skills/roadmap-decompose/SKILL.md`
  **Step 2.4 (Add New Tasks):** replace "Write a full spec for each" with running the Two-Tier Output procedure per new task (invoke `aif-note` → contract line + `Spec:` tag); keep Step 2.4.1 Atomicity Gate intact, a split → two notes + two contract lines.
  **Step 2.5 (Decompose Existing):** redefine "decompose" as writing the full spec into a **new** per-task note via `aif-note` and replacing the roadmap bullet with the contract line + `Spec:` tag; if the selected milestone is already a contract line with a note, update that note rather than the line. Do not bulk-migrate pre-existing legacy inline tasks the skill isn't already touching.

- [x] **Task 4: Rewrite the "Roadmap File Format" section to the contract-line form** (depends on Task 1)
  Files: `.claude/skills/roadmap-decompose/SKILL.md`
  Replace the inline-full-spec example with the **contract line** form: `- [ ] **Name** — <interface: problem today + the change + key files/types/guards involved>. Spec: \`.ai-factory/notes/<NN>-<slug>.md\`.` Reframe the "Rules for writing a description" so they apply to the contract line (name specific files/methods/types; ~600 chars, 400–1000 range; guard conditions named, not exhaustively listed; always end with the `Spec:` tag) and note that the full current-state/target/guards/verify detail now lives in the `aif-note`-written spec note. Keep phase/section headings and intros in the roadmap as today.

## Review history
- **Review 1 (medium):** flagged `Skill` missing from `allowed-tools` (critical), stale description, sequential numbering. → addressed in Task 0 + Task 1.
- **Review 2 (high):** re-flagged `Skill`/`allowed-tools` as still unresolved (now Task 0), plus aif-note per-task scoping risk (pass task name as `$1`, delimit the spec text) → addressed in Task 1 step 3; description and sequential-numbering carried into Task 0 / Task 1.
