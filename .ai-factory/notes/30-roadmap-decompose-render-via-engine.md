# roadmap-decompose: render via roadmap-engine

**Date:** 2026-06-30
**Source:** conversation context

## Key Findings

- Once `roadmap-engine` exists (note 28), refactor `roadmap-decompose` to **call the engine for all output**, removing the duplicated render machinery.
- Keep decompose's philosophy intact: the **Atomicity Gate** (Step 1.3.1 / 2.4.1, gate question verbatim), target/mode determination, codebase exploration, `AskUserQuestion` flow.
- Remove from decompose: the "Two-Tier Output (per task)" rendering steps (ensure-aif-note + write note + write contract line) and the entire "Roadmap File Format" section — these now live in `roadmap-engine`.

## Details

### The seam

decompose's current "Two-Tier Output (per task)" is steps 1–5. After the refactor:
- **Stays in decompose (philosophy):** step 1 (draft the full spec) and step 2 (apply the Atomicity Gate — split into two tasks and recurse if the gate passes).
- **Moves to roadmap-engine (form):** steps 3–5 (ensure aif-note loaded once, write the note, write the contract line) + save.

New per-task flow: draft full spec → Atomicity Gate → hand `{name, full spec}` to `roadmap-engine` to render note + contract line + save.

### Concrete edits to `src/skills/roadmap-decompose/SKILL.md`

- **Target file** — decompose keeps its Step 1 `$TARGET_FILE` determination (default `ROADMAP.md`; test context/keywords → `ROADMAP_TESTS.md`) and **passes the resolved file to `roadmap-engine`** on each render call. The engine does not infer it.
- **Two-Tier Output section** — collapse steps 3–5 into: "Ensure `roadmap-engine` is loaded once in this chat (load-once, same rule decompose currently applies to aif-note), then hand the gated task to it to render." decompose no longer invokes `aif-note` directly — the engine does.
- **Roadmap File Format section** — delete; the format is the engine's. Reference the engine instead of restating the contract-line rules / char budget / `Spec:` tag.
- **Mode 1 Step 1.4, Mode 2 Steps 2.4 / 2.5** — where they currently call the Two-Tier Output procedure, they now call the engine per confirmed task.
- **Frontmatter `allowed-tools`** — keep `Skill` (now used to load `roadmap-engine`); aif-note is reached transitively via the engine.
- **Atomicity Gate (1.3.1 / 2.4.1)** — untouched, gate question wording unchanged.
- **Critical Rules** — keep all; "Every task is two-tier" now reads "rendered two-tier via `roadmap-engine`".

### Files

- Edit `src/skills/roadmap-decompose/SKILL.md`.
- `CLAUDE.md` already lists `roadmap-decompose` under "Custom skills — never overwrite from upstream" — no change needed.

### Regression guard (static diff)

After the edit, `git diff src/skills/roadmap-decompose/SKILL.md` must contain **only**: the removed "Two-Tier Output" render steps 3–5 + the removed "Roadmap File Format" section, and the added "load `roadmap-engine` once, hand the gated task to it" glue. The text moved into `roadmap-engine` must be **byte-identical** to what was removed here (diff the removed lines against the engine's copy). Any change to preserved text — the Atomicity Gate, modes, exploration, `AskUserQuestion` blocks — is a regression; revert it.

### What NOT to do

- **Preserve verbatim, do not paraphrase.** The Atomicity Gate (1.3.1 / 2.4.1, gate wording), the modes, exploration, and `AskUserQuestion` blocks stay **byte-identical**. The text moved to the engine (the "Roadmap File Format" section + "Two-Tier Output" steps 3–5) is **copied verbatim** into `roadmap-engine`, not rewritten. The only new prose is the thin "load engine once, hand task to it" glue. A refactor here is a move, not a rewrite.
- Do not move the Atomicity Gate or the gate question into the engine — it is decompose's philosophy.
- Do not change the gate wording or restructure the modes.
- Do not leave a second copy of the roadmap format in decompose — the engine is the single source of truth.
