# Code Review (pass 2) — command-handoff (self-handoff prompt command that survives /compact)

**Plan:** `.ai-factory/plans/02-command-handoff-self-handoff-prompt-command-that-survives-compact.md`
**Scope:** `git diff HEAD` + `git status` — code changes are unchanged since review-1 (no fix applied; only `review-1.md` was added to the tree).
**Risk:** 🟢 Low — prompt/documentation artifact, no executable application code. Only runtime surface is the `note` path's tool usage.

## Files reviewed in full
- `.claude/commands/command-handoff.md` (new) — the command
- `CLAUDE.md`, `README.md`, `.ai-factory/ARCHITECTURE.md` — doc registration
- plan / plan-review / `.json` sidecar — orchestrator bookkeeping, not product code

---

## Findings

### 1. `mkdir` invoked by the note path is not in `allowed-tools` (Low — still open)
Step 3.2.a runs `mkdir -p .ai-factory/notes`, but `allowed-tools: Read Write Glob Bash(ls *)` pre-approves only `ls`. `mkdir` therefore triggers a permission prompt, defeating the command's own "pre-approve to skip stalls" rationale. Fix by removing the `mkdir` (the directory exists — notes `01`–`15` are present — and `Write` auto-creates parents) or by adding `Bash(mkdir *)` as `aif-note` does. Confirmed independently this pass; consistent with review-1 finding #1 and the plan-review.

### 2. Literal `<!-- optional -->` template marker can leak into output (Low — new this pass)
The skeleton in Step 2 contains a literal annotation line:
```
<!-- optional -->
## 7. Orientation
```
The surrounding instruction says **"Use the skeleton below exactly — do not change section names or order"** and to emit the prompt **"verbatim"** to both chat and file. A literal-minded execution will copy the `<!-- optional -->` comment into the emitted handoff (and the persisted note). It's a template directive meant for the author, not output content. Recommend either deleting that marker line and relying on the per-section "Only if session produced these" notes already present in sections 7–9, or replacing it with an explicit instruction like *"(sections 7–9 below are optional; include only if the session produced material — do not emit this note)"*. Low impact (cosmetic noise in the handoff), but it slightly undercuts the "dense, no-cruft" goal.

### 3. `Glob` declared but never used (Informational)
`allowed-tools` lists `Glob`, but the body scans via `Bash ls` (Step 3.2.a). Either use `Glob` for the scan and drop `Bash(ls *)`, or drop the unused `Glob`. Tightens the surface to what actually runs.

### 4. CLAUDE.md structure tree mixes artifact depths (Informational)
The Repository Structure tree shows skills (`aif/`, `aif-plan/`, …) at repo root but nests `.claude/commands/` under `.claude/`, while both artifact types actually live under `.claude/`. Pre-existing simplification made more visible by this edit; non-blocking.

---

## Verified correct (independent re-check)
- **No `name` field in frontmatter** — correct for commands (name derives from filename); `argument-hint: "[note]"` brackets quoted per convention. Command resolves globally via the live `~/.claude/commands` symlink.
- **Mode dispatch** — note triggers (`note`/`ноут`/`давай ноут`/`с ноутом`, case-insensitive substring) vs chat-only for everything-including-empty. Chat mode writes no file and uses no tools, matching the "pure chat, ~95% case" spec. Greedy substring on `note` is acceptable since the argument carries no other payload (the slug is always derived, never passed).
- **No routing through `aif-note`** — Step 3.2 writes directly via `Write` and explicitly forbids `/aif-note`, preserving the skeleton (core constraint).
- **Numbering** — "scan `[0-9][0-9]-*.md`, highest +1, zero-pad, start `01`" matches `aif-note`; next prefix correctly `16`. No concurrency, so no race.
- **Slug** — semantic lowercase-hyphen with an explicit "do NOT use the literal `handoff`" guard; the content H1 `# Handoff — <slug>` is distinct from the filename slug, no collision.
- **Skeleton fencing** — the skeleton is wrapped in `~~~` tildes, correctly avoiding breakage from the inline backtick paths inside it. Thoughtful.
- **Skeleton content** — all 9 sections, correct order, English-only, "no placeholders/no invented content" guard, optional 7–9 gated on session material. Matches plan.
- **Doc edits** — README adds the commands symlink and updates the "that's it" line; CLAUDE.md Upstream Sync registers `.claude/commands/` as ours/never-synced; ARCHITECTURE.md adds the one-line registration. ARCHITECTURE.md and CLAUDE.md now agree on what the repo produces.

---

## Conclusion
No runtime-breaking defects, no security issues. Two low-severity authoring nits worth fixing before commit: the `mkdir`/`allowed-tools` mismatch (#1) and the `<!-- optional -->` marker leak (#2). Both are one-line edits and neither blocks. #3 and #4 are optional tidy-ups.
