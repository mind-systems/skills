## Plan Review Summary

**Plan:** `57-observe-logs-mandatory-env-selection-via-env-registry-grafana-only.md`
**Files Reviewed:** plan + spec `.ai-factory/specs/11-observe-logs-multi-environment-registry.md` + target code (`src/skills/observe-logs/SKILL.md`, `scripts/query-loki.sh`), `.gitignore`, ROADMAP line 125
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap:** ROADMAP.md:125 (`observe-logs: mandatory env selection via .env registry (Grafana-only)`) matches the plan heading; the contract line's `Spec:` points at `.ai-factory/specs/11-observe-logs-multi-environment-registry.md`, which exists and governs. Linkage intact. **OK.**
- **Spec fidelity:** Every spec directive is covered — remove localhost/no-auth default (Task 3), `.env.example` committed + `.env` gitignored/chmod-600 (Tasks 1–2), parse-never-source with `IFS='|' read` (Task 3), required top-level `--env` stripped before subcommand parsers (Task 3), `${BASH_SOURCE[0]}` resolution for symlink correctness (Task 3), three hard-error paths listing available names (Task 3), lean agent-facing SKILL.md rewrite with `--project` inference (Task 5), bash 3.2 constraint preserved (Task 3). **OK.**
- **Architecture/Rules:** `observe-logs` is a standalone skill with no `loads:` edges — no engine contract to honor, no dependency-graph impact. Adding a gitignored secret store next to the skill introduces no boundary violation. `.ai-factory/RULES.md` absent. **OK (no ARCHITECTURE conflict).**

### Critical Issues
None.

### Correctness / technical verification

- **`set -u` interaction is handled.** The script runs under `set -euo pipefail` (`:5`). Deleting the `LOKI_URL`/`LOKI_AUTH` default assignments (`:10–11`) leaves both unset until env resolution. Task 3 correctly moves the `AUTH_ARGS` construction (currently top-level at `:19–20`) to *after* resolution, and the hard-error paths guarantee the script exits before any use of `LOKI_URL`/`LOKI_AUTH` when no valid env resolves. No unbound-variable hazard is introduced, provided the implementer honors "populated only by env resolution" literally and does not leave a bare `[[ -n "$LOKI_AUTH" ]]` at file-source time. The plan states this explicitly — good.
- **Ordering is correct.** Task 3 places the `--env` parse *before* `check_backend` (`:462`), so the "no `--env` / unknown / missing `.env`" errors fire with no network call, satisfying the spec's "no fallback, no network" guard.
- **Argument stripping matches the subcommand parsers.** The per-subcommand parsers treat any unrecognized `-*` as a fatal "Unknown flag" (`:258`, `:337`, `:390`). Stripping `--env <name>` from the head before dispatch keeps them untouched — consistent with the plan. Note the design accepts `--env` only in leading position (spec example `query-loki.sh --env stage window 30m --project mind`); a mis-ordered `--env` would hit the "Unknown flag" path. This is the intended, agent-constructed contract, so acceptable.
- **`.env` parse under `set -e` is safe.** `while IFS='|' read -r name url auth; do …; done < "$env_file"` — `read` returning non-zero at EOF is the loop condition, not a `set -e` trigger. Standard and fine.
- **gitignore anchoring is right.** Task 2's exact path `/src/skills/observe-logs/.env` (leading slash, not `.env*`) keeps `.env.example` tracked. The repo-root `.gitignore` today has no `.env` pattern, so there is no pre-existing rule that would swallow `.env.example`. **OK.**
- **Symlink visibility needs no extra step.** `active/skills/observe-logs` is a directory symlink into `src/skills/observe-logs`; a new `.env.example` (and a user's `.env`) appears through it automatically — consistent with the spec's inode-equality claim. No manual re-symlink task is required, and the plan correctly omits one.
- **Registry-key naming resolved correctly.** The spec is internally inconsistent — its "Target/chosen design" and agent-facing sections say keys are `stage`/`dev`/`prod`, but the Verify section's examples say `staging`/`local`. The plan consistently uses `stage`/`dev`/`prod`, matching the authoritative design sections. Right call.
- **argument-hint + examples.** Task 5 updates the `argument-hint` frontmatter and all `bash scripts/query-loki.sh …` examples to carry `--env <name>`, and Task 4 adds `--env` to `usage()` and its Environment block. Both current sources (`SKILL.md:10`, script `usage()` `:446–449`) are the ones needing edits — coverage is complete.

### Positive Notes
- Task dependencies and the two-commit split are correctly sequenced (registry+gitignore first, then the script/SKILL rewrite that depends on the registry existing).
- The plan preserves the existing bash-3.2-safe `${AUTH_ARGS[@]+…}` guard rather than reintroducing an unguarded array expansion — a real trap on macOS this repo has already been bitten by.
- Scope discipline is good: pagination, `format_response`, and the `--project/--service/--level/--limit` filters are explicitly left untouched.

## Deferred observations
- Affects: verification of this milestone (`scripts/query-loki.sh` `check_backend` / `/ready`) — This milestone makes the Grafana datasource proxy the *only* endpoint, so `check_backend`'s `GET ${LOKI_URL}/ready` now *always* resolves to `https://<host>/api/datasources/proxy/uid/<uid>/ready`. The plan correctly leaves the three curl sites unchanged (this behavior was introduced in note `26-observe-logs-remote-auth.md`), but the localhost fallback that previously masked any proxy-path issue is now gone. If Grafana's datasource proxy does not forward `/ready` to Loki's readiness endpoint with a 2xx, `check_backend` will hard-fail before every query and the skill is unusable. The plan's own Verify step (`--env stage window 5m --project mind` returns logs) exercises this path and will catch it — flagging only so the verifier treats a `check_backend` failure as the proxy-`/ready` question, not a token/URL typo.

PLAN_REVIEW_PASS
