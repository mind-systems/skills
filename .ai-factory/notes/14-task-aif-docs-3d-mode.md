# Task Spec — aif-docs: docs describe state not process (always-on no-motivation rule + `3d`/`3д` target-state mode)

**Date:** 2026-06-01
**Roadmap:** ROADMAP.md Milestones
**Provenance:** user request; concept captured in note `11-document-driven-docs-mode.md`. Recurring workflow — the user has repeatedly had to argue with the agent, which refuses to write docs for not-yet-existing code.

## Current state

`aif-docs` always assumes the documented code is **already shipped**. Several steps actively fight target-state (ahead-of-implementation) authoring:

- **Step 1 "Determine Current State"** (`SKILL.md:93`) — frames the whole run around what exists today.
- **Step 2.1 audit** (`SKILL.md:409`) — flags *"Stale content — do docs reference files/APIs that no longer exist?"* as a defect.
- **Step 4 Technical Accuracy** checklist (`SKILL.md:474`, defined in `references/REVIEW-CHECKLISTS.md`) — verifies docs against the live codebase; absent code reads as broken.
- Global doc-style rule (user's `~/.claude/CLAUDE.md`): *"Describe current state only. Never reference what was changed/added."*

Net effect: when asked to document a feature before it's built, the agent treats the missing code as an error and **refuses or rewrites** the doc to match reality — the opposite of what 3D needs.

There is no mode parameter; the skill has one behavioral path.

**Second, separate standing problem (both modes):** the skill describes **motivation and process** in docs — "we changed X to Y because…", "this was replaced", "previously it did…". Docs should state the **factual target state**, not the history of how it got there. The global doc-style rule (`~/.claude/CLAUDE.md`: *"Never reference what was changed/added… History belongs in commit messages"*) already says this, but `aif-docs` doesn't enforce it, so the user corrects it with an extra prompt **every run**. This is mode-independent — it must hold in normal mode and 3D alike.

**Distribution caveat:** `aif-docs` is **not** in CLAUDE.md's custom/never-overwrite list — it currently falls under "all other skills, safe to overwrite directly from upstream." So a 3D branch added here will be **wiped on the next upstream sync** unless `aif-docs` is registered as intentionally diverged (handled in this task).

## Target

Two coupled changes to the same skill, one theme — **docs describe factual *state*, not *process***. Both are **small, surgical**; the skill is strong — do not restructure or fork it into a second skill.

### Change A — always-on: state, never motivation/history (both modes)

Add/strengthen a Core Principle in `aif-docs` so it holds on **every** run regardless of mode: *"Documentation states the factual state, never the process or motivation behind it. Never write 'we changed X to Y', 'this replaces…', 'previously…', 'because we…'. Describe what **is**, not how it came to be — history lives in commit messages."* Wire it into the Step 4 review so motivation/history/process language is **flagged and removed**, not produced. This is the recurring problem the user otherwise patches with an extra prompt every run. It is **not** param-gated — it applies in normal mode and 3D alike (in 3D the "state" is the *target* state; the no-motivation rule is identical).

### Change B — the `3d`/`3д` target-state mode

Add a `3d` / `3д` input parameter that activates a **Document-Driven Development** branch.

1. **Parameter detection.** If the invocation arguments contain the token `3d` or `3д` (case-insensitive) → set a `MODE = 3D` flag at the top of the workflow. Absent → behavior is **byte-identical to today**.

2. **Explain what 3D *is*, in the skill body** — this is the core of the fix, because the agent refuses out of not understanding the intent. State plainly: *"Document-Driven Development (3D) is the docs analogue of TDD: author the documentation as if the feature is already shipped — present tense, target behavior, end to end. The doc is the contract; code will be written to conform to it. Documenting APIs, columns, endpoints, or files that do not exist yet is the **intended** behavior in this mode, never an error or staleness."* The agent must read this and proceed without arguing.

3. **Branch exactly the conflicting points in 3D mode (and nothing else):**
   - **Step 1 "Determine Current State" → "Determine Target State"** — gather what the feature *will* do from the ROADMAP milestone / spec note / user intent, not from existing code.
   - **Step 2.1 staleness audit** — suppress the *"files/APIs that no longer exist"* check; absent code is expected, not stale.
   - **Step 4 Technical Accuracy** — suppress/invert the verify-against-codebase check; do **not** flag non-existent code as broken. Keep Readability & Completeness.
   - **"Current state only" doc-style** — reinterpret as *"describe the target shipped state"*: present tense, behavior-focused, still **no history/rationale** ("was added", "we changed", "this milestone"). 3D drops the *current-state* constraint, not the *no-history* one.

4. **Keep everything else intact** — README-as-landing, the docs-directory split, navigation, cross-links, scannability, language matching, no-file-trees, and all project/skill-context overrides apply unchanged in 3D mode.

5. **Optional — conformance pointer.** After authoring, optionally emit a line the user can drop into the relevant ROADMAP milestone: *"implementation must conform to `<doc-path>`."* Lean **print-for-user-to-place**, not auto-insert (less magic, matches the confirm-before-acting rhythm). Mirrors the `Spec:` tag pattern: here the durable **doc** is the contract a task points at.

6. **Register the divergence** (part of this task). Update `CLAUDE.md` "Upstream Sync": move `aif-docs` into the **"Intentionally diverged from upstream — review diff before updating"** list, with a one-line reason ("3D / target-state docs mode added downstream"). Without this the next sync overwrites the mode.

## Guards

- **Minimal change.** Change A = one Core Principle + a Step 4 check. Change B = one mode flag + a branch at the four conflicting points + the 3D explanation block. No workflow restructure, no second skill, no duplication.
- **Default path unchanged except Change A.** Without `3d`/`3д` the mode/verify behavior is identical to today — *plus* the always-on no-motivation rule, which now applies in normal mode too (intended; it's the recurring patch the user wants baked in).
- **3D drops *current-state* and *verify*, NOT *no-history*.** Change A's no-motivation rule is exactly what 3D keeps — target-state docs are pure behavior with no "was changed / we added / because / milestone" language.
- **Do not touch other skills.** Only `aif-docs/SKILL.md` (+ possibly `references/REVIEW-CHECKLISTS.md` if the accuracy suppression must live there) and `CLAUDE.md`.
- **Register the upstream divergence** or the change gets wiped on sync.

## Files

- `~/projects/skills/.claude/skills/aif-docs/SKILL.md` (modify) — Change A: state-not-process Core Principle + Step 4 check. Change B: param detection, 3D explanation, branch at Steps 1 / 2.1 / 4.
- `~/projects/skills/.claude/skills/aif-docs/references/REVIEW-CHECKLISTS.md` (modify, if the Technical-Accuracy suppression is cleaner there).
- `~/projects/skills/CLAUDE.md` (modify) — Upstream Sync: register `aif-docs` as intentionally diverged.

## Verify

- **Change A:** docs in **both** modes contain no motivation/history — no "we changed / was replaced / previously / because we…". Step 4 flags and removes any such language.
- `/aif-docs 3d` (or `3д`) authoring a doc for a not-yet-built feature **proceeds without refusing**, writes present-tense target-state behavior, and does not flag missing code as stale/broken.
- `/aif-docs` without the token behaves as before (current-state + full audit + accuracy verify), plus Change A now strips motivation/history.
- All formatting/navigation/language rules hold in both modes.
- A subsequent upstream sync does not silently overwrite the changes (divergence registered).

## Resolved decisions

- **Aspirational-doc marker — dropped.** Considered a `status: target` frontmatter marker so a later *normal* audit wouldn't flag the ahead-of-implementation doc. Decision (user): **do not add it.** Change A + the 3D branch make the skill much softer overall (it no longer treats absent code as a hard error), so the two modes don't violently fight; the marker is over-engineering. Revisit only if a normal audit actually starts re-flagging target-state docs in practice.
- **Conformance pointer — print, not auto-insert.** The optional ROADMAP "implementation must conform to `<doc>`" line is printed for the user to place, not written automatically.
