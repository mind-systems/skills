# Review 2 — command-handoff: philosophy over the note engine

Scope: `git diff HEAD` — `src/skills/note/SKILL.md` (unchanged since review 1) and `src/commands/command-handoff.md` (revised to address review 1). This is an agent-instructions repo; correctness = the prose an agent executes is internally consistent and cannot route it into the explicitly-rejected pre-filled-template behavior. Re-checked against the spec note (`.ai-factory/notes/55-handoff-philosophy-over-note.md`) and the caller convention in `src/skills/roadmap-engine/SKILL.md`.

## Review 1 findings — both resolved

- **Finding 1 (Medium) — Step 2 "Populate every field" contradicted Step 3 "passed blank."** Resolved. A per-mode guard for Steps 1–2 was added (line 18: chat mode performs mining/composition itself; note mode treats Steps 1–2 as the lens + blank skeleton that `note` executes), and the previously-unconditional "Populate every field" line was split by mode (line 108: "Chat mode: populate… / Note mode: do not populate the skeleton here — pass it blank to `note`"). No execution path now leads a note-mode agent to pre-fill the template, so the rejected inversion (note 55, "What NOT to do" #1) is closed off.
- **Non-finding (Slug mislabeled a hook).** Resolved. Line 123 now labels Slug "`note`'s `$1` / topic derivation, not a named hook," which matches `note`'s Step 2.

## Independent re-scan — clean

- **Frontmatter.** `loads: note` present; `allowed-tools` is the exact union `Read Write Bash(ls *) Bash(mkdir *) Glob Skill` (note's grants + command's own + `Skill`), per spec's "never a partial copy." Chat mode's "Do not use any tools" (line 116) is mode-scoped and does not conflict with the widened grant.
- **Delegation body (Step 3 note mode).** No leftover `ls`/`<NN>`-scan/`mkdir`/`Write` choreography; line 125 assigns numbering, directory creation, and Write to `note`. Template passed blank → `note` follows the caller skeleton verbatim (its Step 3), so no `Date/Source` default-template leak and no default-concision leak. Numbering scans the destination hook `.ai-factory/handoffs/` per-directory — same as prior behavior, no regression against existing `NN` files.
- **Self-check gate consistency.** The gate lives once (line 110) and is referenced by note mode via the verbosity hook (line 122) rather than restated; its note-mode clause ("applies to the content written to the note file; the chat pointer is minimal and exempt") stays coherent now that `note` performs the write. Matches spec's "shared once, referenced as hooks' values."
- **Map scoping (Task 2).** Proportionality-register paragraph (line 48) plus in-skeleton guidance (lines 58–69) scope "must-read now" to the next action and state the multi-tree case; error-log and working-discipline sections untouched, per Edit 3.
- **`note` verbosity hook (Task 1).** Third hook is generic (no handoff mention), count updated, concision reframed as the default directive with findings-focus/file-paths/English preserved. `roadmap-engine` supplies only the destination hook (no verbosity) → behavior-identical; standalone `/note` unchanged.
- **Security.** Prose-only instructions; Bash grants scoped to `ls`/`mkdir`; no untrusted-input execution. Nothing of concern.

No correctness, consistency, or security issues remain.

REVIEW_PASS
