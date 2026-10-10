## Code Review Summary

**Files Reviewed:** 1 (`src/skills/roadmap-engine/scripts/user-slug.sh`, new). The other staged files are pipeline artifacts: the plan, its sidecar and the two plan-reviews.
**Risk Level:** 🟢 Low

### Context Gates
- **Architecture:** OK. `.ai-factory/ARCHITECTURE.md` lists `scripts/` as a skill's folder for executable helpers. `active/skills/roadmap-engine` symlinks the whole skill directory, so the script resolves at `~/.claude/skills/roadmap-engine/scripts/user-slug.sh` with no new symlink. Task 83.3 depends on that path.
- **Rules:** WARN. `.ai-factory/RULES.md` is absent (it is optional). `.ai-factory/skill-context/aif-review/SKILL.md` is also absent.
- **Roadmap:** OK. The change matches 83.1 in `.ai-factory/roadmaps/trickster77777.md` and its spec `0233`. The engine's **Slug derivation** paragraph is left untouched, which is correct, because 83.2 owns that rewrite and the spec defers to it. There is no hook either, since that belongs to 83.3.
- **Spec conformance (§ "What must be true after"):** I compared the script against `_derive_identity_slug` and `_git_config_value` in `orchestrator/orchestrator/main.py` and ran it against fixture identities in throwaway repos, with `GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1`:
  - `john.doe@example.com` → `john-doe`
  - `--John..Doe--@x` → `john-doe`
  - `MiXeD_Case+tag@x` → `mixed-case-tag`
  - email `...@x` with name `Jane Q. Public` → `jane-q-public`
  - no email, name `Ann` → `ann`
  - no email, name `Ann⏎Lee` → `ann-lee` on exactly one line, confirmed with `od -c`
  - `Ünïcödé Name` → `n-c-d-name`
  - email `@x` with name of whitespace only → empty stdout, one stderr line, exit `2`
  - neither key set → empty stdout, one stderr line, exit `2`

  Python's `_slugify` gives the same value on every input. A local `user.email` overrides a global one. A multi-valued `user.email` gives the last value, the same as `git config` does for the orchestrator. With `git` absent from `PATH` the script exits `1` with a stderr message, so `2` stays reserved for the case where no slug can be derived. `bash -n` passes, and the file mode is `-rwxr-xr-x`.

### Critical Issues
None.

### Positive Notes
- The collapse uses `tr -cs`, not `sed`, so an embedded newline in a git value is collapsed like any other byte. The single-line contract holds, and this closes the gap the first plan-review raised.
- Every stage runs under `LC_ALL=C`, so the result does not depend on the locale. The script uses only bash 3.2-safe constructs.
- Writing `|| email=""` / `|| name=""` mirrors the orchestrator's "a non-zero exit means unset" rule without tripping `set -e`.
- The header comment describes behaviour only and cites no plan layer. It also states the exit-code contract, which the hook in 83.3 and the agents that call the script rely on.

REVIEW_PASS
