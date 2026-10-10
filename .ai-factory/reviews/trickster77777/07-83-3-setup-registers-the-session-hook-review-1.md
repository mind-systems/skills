## Code Review Summary

**Files Reviewed:** 1 (`README.md`; the staged plan, plan-review and sidecar files under `.ai-factory/` are pipeline artifacts, not product changes)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap: OK.** The diff carries out 83.3 in `.ai-factory/roadmaps/trickster77777.md`, the open line at the seam after 83.1 and 83.2.
- **Task spec: OK.** I checked against `.ai-factory/specs/trickster77777/0235-setup-registers-the-session-hook.md`, § "What must be true after":
  - The new README paragraph is byte-identical to the spec's quoted text. A string comparison returned equal.
  - The fenced `json` block is byte-identical to the spec's block. `diff` returned empty.
  - "The rest of the section stands": the diff is a pure 19-line insertion with no other line touched.
- **Governing spec: OK.** `docs/sakshi-harness/sakshi-harness.md` (Phase 83) already says that a `SessionStart` hook registered at activation gives each session the slug line, and links to README § Setup. This change supplies that target.
- **Architecture: OK.** `.ai-factory/ARCHITECTURE.md` places no constraint on setup or hooks.
- **Rules: WARN (non-blocking).** `.ai-factory/RULES.md` and `.ai-factory/skill-context/aif-review/SKILL.md` are absent.

### What was verified

- **Placement.** The paragraph sits after the per-surface merge bullets and before "The whole flow is idempotent…", as the plan intends.
  - The column-0 paragraph, set off by a blank line, ends the nested list cleanly.
  - The idempotence sentence still closes the whole flow. The hook surface itself is idempotent through "If a `SessionStart` entry already runs that script, skip it".
- **The JSON parses** (`python3 -I` + `json.load`). The decoded `command` is `s=$(… user-slug.sh 2>/dev/null) && printf "The user's slug: %s\n" "$s" || true`.
- **Positive case.** With the real `HOME`, where `~/.claude/skills/roadmap-engine` resolves to `src/skills/roadmap-engine`, running `sh -c "$command"` in this repo prints `The user's slug: trickster77777` and exits 0.
- **Negative case: the script yields no slug.** I used a temporary `HOME` holding a `.claude/skills/roadmap-engine` symlink to the repo's engine, with `GIT_CONFIG_GLOBAL=/dev/null` and `GIT_CONFIG_NOSYSTEM=1`, outside any repo. The script alone exits `2` and writes its stderr notice. The hook command prints nothing (stdout and stderr both empty) and exits `0`. This matches the spec: a status-2 exit would otherwise surface as a hook error notice in every session.
- **Sweep.** `grep -n "symlink" README.md` returns the section's own symlink flow, the new paragraph ("not a symlink"), and the `active/` and adding-a-skill lines. All of them stay true.
- **Security.** The command interpolates the slug only through `printf %s` with a quoted argument. The slug's character set is `[a-z0-9-]`, which `user-slug.sh` guarantees. There is no injection surface. The README text tells the agent to write `settings.json` only on the user's word and to preserve existing keys and `SessionStart` entries, so the user's settings are never overwritten silently.

### Critical Issues

None.

### Positive Notes

- The pinned text was copied exactly, including the trailing space in `` `The user's slug: ` ``, the JSON escapes `\"` and `\\n`, and two-space indentation.
- `2>/dev/null` plus `&& … || true` correctly turns both "no slug" (exit 2) and "script missing" (exit 127) into a silent zero exit. A user who has not linked `roadmap-engine` therefore gets no per-session error noise.

## Deferred observations
- Affects: sakshi root repository `README.md` (outside this repo) — The root README's Setup prompt still says "to activate the ~/.claude symlinks", and its closing sentence says "(the `~/.claude` symlinks)". Both describe activation as symlinks only, while this repo's setup now also registers a non-symlink `SessionStart` hook surface. The spec's "What breaks on contact" assigns that repair to the root repository, so it cannot be fixed within this task's file boundary.

REVIEW_PASS
