# roadmap-decompose: extract roadmap-engine (artifact format) from the philosophy

**Date:** 2026-06-30
**Source:** conversation context

## Key Findings

- The current `roadmap-engine` was built as a rigid **render procedure** with an input contract (`{task, spec, target}` → write a fresh contract line + save). That framing is **wrong** — it invented phantom "append-only / no in-place / no insertion-point" limits that looped the decompose refactor 3× at review.
- **The engine is not a procedure or an API.** Skills are reusable **instructions for one agent**, not executable programs — there is no separate process with a fixed function signature. The engine is simply the shared **explanation of the roadmap artifacts** (what a contract line looks like + its rules, the two-tier spec note via `aif-note`, the roadmap file structure). Knowing that format, the one agent writes / appends / edits the roadmap as each situation needs. No modes, no input contract, no save-ownership belong in the engine.
- This is the **split of `roadmap-decompose` into two skills**: `roadmap-engine` (the artifact-format explanation) + `roadmap-decompose` (the philosophy remainder). It is done here as one task. After it, `roadmap-engine` ≈ decompose's original "Roadmap File Format" section, verbatim — they are the same text.
- The engine already works today **inside** decompose (no problems observed). This task just **extracts** it cleanly and redoes the mis-built engine skill.

## Details

### The task

**1. Rewrite `src/skills/roadmap-engine/SKILL.md` as the artifact-format explanation — verbatim from decompose.**
Its body is decompose's format content, moved as-is:
- the **"Roadmap File Format"** section (the roadmap structure block + "Rules for writing a contract line");
- the **two-tier note explanation** (each milestone = a contract line + a full spec note; the note is written following `aif-note`'s format, `aif-note` loaded once per chat; `<NN>` scanned so it never collides; the `Spec:` tag).

**Drop** the "Input Contract", the numbered "Per-Task Render Procedure", and the "What This Engine Does NOT Own" list. The engine explains the artifacts; it does not prescribe an append-vs-edit procedure, own the file save, or expose modes/parameters. After this, diffing `roadmap-engine` against decompose's removed format section should show the **same content**.

**2. Trim `src/skills/roadmap-decompose/SKILL.md` to the philosophy remainder.**
- Keep **byte-identical**: the Atomicity Gate (Steps 1.3.1 / 2.4.1, gate wording), the modes (create / update / decompose-existing / check), Step 0 context loading, exploration, and every `AskUserQuestion` block.
- **Remove** the "Roadmap File Format" section and the inline two-tier render detail (now the engine's).
- Where decompose produces artifacts, it says: "load `roadmap-engine` once for the artifact format, then produce the two-tier artifacts per that format." The agent renders per each mode (create writes the file, add appends, decompose-existing edits in place) using the engine's format — **no** scaffold/append/content-return machinery, because there is no rigid engine procedure to work around.
- Frontmatter/intro: the two-tier entry is "rendered per `roadmap-engine`'s format" instead of "written manually following aif-note's note format".

### Files

- Rewrite `src/skills/roadmap-engine/SKILL.md` (→ verbatim format extract).
- Trim `src/skills/roadmap-decompose/SKILL.md` (→ philosophy remainder + reference to the engine).

### Verify

- `roadmap-engine`'s body is decompose's original "Roadmap File Format" + two-tier note text — same content, not a rewrite.
- decompose no longer restates the roadmap/contract-line format anywhere.
- decompose's philosophy (Atomicity Gate wording, modes, exploration, `AskUserQuestion`) is unchanged.

### What NOT to do

- Do **not** give the engine an input contract, a per-task render procedure, or modes — it is a format explanation, applied contextually by the agent.
- Do **not** add scaffold-then-append, append-only, content-return, or insertion-point machinery anywhere — that was the phantom problem this task removes.
- Do **not** change decompose's philosophy text (Atomicity Gate, modes, exploration, `AskUserQuestion`).
- The other two philosophy skills (`aif-roadmap`, `roadmap-decompose-skeleton`) follow this same shape and reference the engine's format — do not touch them in this task.
