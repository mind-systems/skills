# Code Review (pass 3) — command-handoff (self-handoff prompt command that survives /compact)

**Plan:** `.ai-factory/plans/02-command-handoff-self-handoff-prompt-command-that-survives-compact.md`
**Scope:** `git diff HEAD` + `git status`. The command file was revised since pass 2 (blob `3220d10` → `b08d349`); doc edits unchanged.
**Risk:** 🟢 Low — prompt/documentation artifact, no executable application code.

## What changed since pass 2 (prior findings resolved)
- ✅ **review-1 #1 / `mkdir` not pre-approved** — fixed. The `mkdir -p .ai-factory/notes` step was removed from Step 3.2.a; the note path now only runs `Bash ls` (pre-approved) and `Write` (auto-creates parents). No un-approved call remains.
- ✅ **review-1 #2 / review-2 #3 — `Glob` unused** — fixed. `allowed-tools` is now `Read Write Bash(ls *)`; `Glob` removed.
- ✅ **review-2 #2 — `<!-- optional -->` marker leak** — fixed. The literal template marker is gone; sections 7–9 now stand on their own with their per-section "Only if session produced these" gating.

---

## Findings (remaining — all non-blocking)

### 1. `ls` on a possibly-absent `.ai-factory/notes/` in fresh projects (Low / robustness)
With `mkdir` removed, the note path opens with `ls .ai-factory/notes/`. This command is generic and ships to every project via the global symlink. In a brand-new project where `.ai-factory/notes/` does not yet exist, `ls .ai-factory/notes/` errors (`No such file or directory`) rather than returning an empty list. The flow still works — a reasonable agent reads the error as "no notes yet → start at `01`", and `Write` creates the parent directory — so this is not a break, only an interpretive ambiguity. Suggest making the body explicit: in Step 3.2.a, "if the directory does not exist **or** is empty, start at `01`." One-line robustness tweak; the dir-absent case is the one the removed `mkdir` used to cover.

### 2. `Read` is declared in `allowed-tools` but never used (Informational)
The body uses only `Bash ls` and `Write`; the default chat path uses no tools. `Read` is now dead in the tool list (the same class of nit as the removed `Glob`). Harmless — drop it to keep the surface to exactly what runs, or keep it if intended as headroom for the agent to inspect a candidate entry doc while mining. Optional.

### 3. CLAUDE.md structure tree mixes artifact depths (Informational, pre-existing)
The Repository Structure tree shows skills (`aif/`, …) at repo root but nests `.claude/commands/` under `.claude/`, while both actually live under `.claude/`. Pre-existing simplification; non-blocking.

---

## Verified correct (independent re-check)
- **Frontmatter** — no `name` field (correct: commands derive name from filename); `argument-hint: "[note]"` brackets quoted; `description` states the run-before-`/compact` timing. Command resolves globally via the live `~/.claude/commands` symlink.
- **`Bash(ls *)`** correctly pre-approves the `ls .ai-factory/notes/` scan; it is the only Bash call, and `mkdir` is no longer present — so the note path no longer stalls on permissions.
- **Mode dispatch** — note triggers (`note`/`ноут`/`давай ноут`/`с ноутом`, case-insensitive substring) vs chat-only for everything-including-empty; chat mode writes no file and uses no tools.
- **No `aif-note` routing** — Step 3.2 writes directly via `Write` and explicitly forbids `/aif-note`, preserving the skeleton.
- **Numbering** — scan `[0-9][0-9]-*.md`, highest +1, zero-pad, start `01`; single agent, no race.
- **Slug** — semantic lowercase-hyphen with explicit "do NOT use literal `handoff`" guard; content H1 `# Handoff — <slug>` is distinct from the filename slug.
- **Skeleton** — `~~~`-fenced (avoids nested-backtick breakage), all 9 sections in order, English-only, "no placeholders/no invented content," optional 7–9 gated. Matches plan.
- **Doc edits** — README symlink + "that's it" line; CLAUDE.md Upstream Sync registration; ARCHITECTURE.md one-line registration. ARCHITECTURE.md and CLAUDE.md agree on what the repo produces.

---

## Conclusion
The two substantive findings from passes 1–2 are resolved. What remains is one low-severity robustness suggestion (#1, the dir-absent `ls` case for fresh projects) and two informational nits (#2 unused `Read`, #3 doc-tree depth). None break at runtime and none block. The implementation is in good shape.
