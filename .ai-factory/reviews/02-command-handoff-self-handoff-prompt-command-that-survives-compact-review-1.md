# Code Review — command-handoff (self-handoff prompt command that survives /compact)

**Plan:** `.ai-factory/plans/02-command-handoff-self-handoff-prompt-command-that-survives-compact.md`
**Scope reviewed:** `git diff HEAD` + `git status`
**Risk:** 🟢 Low — this is prompt/documentation content, no executable application code. The only runtime surface is the slash command's tool usage when the `note` path fires.

## Files changed
- `.claude/commands/command-handoff.md` (new) — the command
- `CLAUDE.md` (Repository Structure + Upstream Sync)
- `README.md` (Setup symlinks)
- `.ai-factory/ARCHITECTURE.md` (one-line registration)
- plan / plan-review / json sidecar (orchestrator bookkeeping — not product code)

---

## Findings

### 1. `mkdir` is invoked by the note path but is NOT in `allowed-tools` (Low)
`command-handoff.md` Step 3.2.a instructs the note path to run, when needed:
```
mkdir -p .ai-factory/notes
```
but the frontmatter pre-approves only `Bash(ls *)`:
```
allowed-tools: Read Write Glob Bash(ls *)
```
`mkdir` is not covered, so it would trigger a permission prompt — directly contradicting the command's own stated rationale ("pre-approves to skip permission stalls"). Same gap was flagged in the plan-review and is inherited from spec note 12.

Two clean resolutions (either is fine, just make body and frontmatter agree):
- Add `Bash(mkdir *)` to `allowed-tools` (matches `aif-note`, which lists both `Bash(ls *)` and `Bash(mkdir *)`); **or**
- Drop the `mkdir` step. `.ai-factory/notes/` already exists in this repo and the `Write` tool auto-creates parent directories, so the `mkdir` is dead weight. This keeps `allowed-tools` minimal and removes the only un-approved call.

Preferred: drop `mkdir` — it removes the inconsistency rather than papering over it, and the directory provably exists (notes `01`–`15` are present).

### 2. `Glob` and `Bash(ls *)` are redundant for the same job (Informational)
Both are listed and Step 3.2.a uses only `Bash ls`. `Glob` is never referenced in the body. Either switch the scan to `Glob` (and drop `Bash(ls *)`) or drop the unused `Glob` from `allowed-tools`. Harmless, but trims the surface to exactly what runs.

### 3. CLAUDE.md structure tree is now internally inconsistent (Informational / doc-accuracy)
The Repository Structure tree shows skill dirs (`aif/`, `aif-plan/`, …) at the repo root, then adds:
```
└── .claude/
    └── commands/           # Slash commands (e.g. command-handoff)
```
In reality the skills also live under `.claude/skills/` (per this same file's "Purpose" section and the README). So the tree now depicts commands nested under `.claude/` while skills appear at root — a reader can't tell why the two artifact types sit at different depths. This pre-existed as a simplification; the edit makes the mismatch visible. Non-blocking, but consider showing `.claude/skills/` and `.claude/commands/` at the same level if the tree is touched again. (Global doc rule discourages directory trees outside ARCHITECTURE.md, but this tree pre-dates the change.)

---

## Verified correct
- **Frontmatter shape** — commands derive their name from the filename, so the absence of `name`/`user-invocable` fields is correct (those are skill fields). `argument-hint: "[note]"` has quoted brackets per repo convention. The command is registered and resolvable (confirmed in the session skill list and the live `~/.claude/commands` symlink).
- **Mode dispatch** — note triggers (`note`/`ноут`/`давай ноут`/`с ноутом`, case-insensitive substring) match the spec; everything else (including empty) routes to chat-only. Chat mode explicitly writes no file and uses no tools — matches the "pure chat, ~95% case" requirement.
- **Does not route through `aif-note`** — Step 3.2 writes the file directly via `Write` and explicitly forbids `/aif-note`, preserving the skeleton (the core design constraint).
- **Numbering rule** — "scan `[0-9][0-9]-*.md`, take highest +1, zero-pad, start at `01`" matches `aif-note` verbatim; next prefix would correctly be `16`.
- **Slug rule** — semantic, lowercase-hyphen, with an explicit "do NOT use the literal `handoff`" guard. The H1 title `# Handoff — <slug>` is content, distinct from the filename slug — no conflict.
- **Skeleton** — all 9 sections present in correct order, optional 7–9 gated on session material, English-only instruction, "no placeholders / no invented content" guard. Matches the plan's content spec.
- **`Bash(ls *)`** correctly pre-approves the `ls .ai-factory/notes/` scan call.
- **Doc edits** — README adds the commands symlink alongside skills and updates the "that's it" line to mention commands; CLAUDE.md Upstream Sync registers `.claude/commands/` as ours/never-synced; ARCHITECTURE.md adds the one-line registration. All three keep ARCHITECTURE.md and CLAUDE.md in agreement on what the repo produces, as required.

---

## Conclusion
No bugs, security issues, or correctness defects that break at runtime. The one actionable item is finding #1 (the `mkdir`/`allowed-tools` mismatch) — low severity, causes at most a single avoidable permission prompt on the note path, and is trivially fixed by deleting the redundant `mkdir`. Findings #2 and #3 are tidy-ups. None block.
