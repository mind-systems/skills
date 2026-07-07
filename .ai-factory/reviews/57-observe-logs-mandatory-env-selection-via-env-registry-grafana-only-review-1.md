# Code review: observe-logs mandatory env selection via `.env` registry

Scope reviewed: `src/skills/observe-logs/scripts/query-loki.sh`, `src/skills/observe-logs/.env.example`, `src/skills/observe-logs/SKILL.md`, `.gitignore`.

## Findings

### 1. (Medium) Last line of `.env` is silently dropped when it has no trailing newline

`resolve_env` (`query-loki.sh:64`) and `list_env_names` (`query-loki.sh:43`) both parse the registry with:

```bash
while IFS='|' read -r name url auth; do
  ...
done < "$REGISTRY_FILE"
```

The classic pitfall: when the final line of the file is **not** terminated by a newline, `read` populates the variables but returns a non-zero exit status at EOF, so the `while` condition is false and the loop body **never runs for that last line**. The line is silently skipped.

The registry is authored by hand (copy `.env.example`, edit, save). It is entirely plausible for the last environment line — e.g. `prod` — to lack a trailing newline (typed with an editor that doesn't append one, `printf ... >> .env`, pasted from chat, etc.). When that happens:

- `resolve_env prod` → falls through the loop without matching → `ERROR: Unknown environment 'prod'` even though the entry is present.
- `list_env_names` omits `prod` from the "Available environments" list, so the very error message that is supposed to help the user is also wrong.

Failure scenario: user's `.env` ends with `prod|https://…/uid/…|Bearer glsa_…` and no final `\n`. `query-loki.sh --env prod window 30m` hard-errors with "Unknown environment 'prod'. Available environments: stage dev" — a confusing, hard-to-diagnose failure for a correctly-configured entry.

Fix: guard the loop so a final unterminated line is still processed, e.g.

```bash
while IFS='|' read -r name url auth || [[ -n "$name" ]]; do
```

in **both** `resolve_env` and `list_env_names` (keep the two parsers consistent).

### 2. (Low) Stale "backend down" recovery hint now that all access is remote Grafana

`check_backend` (`query-loki.sh:95`) still prints:

```
To start it: make backend-up  (in the observability repo)
```

and SKILL.md `:73` repeats the same `make backend-up` hint. With the localhost/direct-Loki path removed, every endpoint is now a remote Grafana datasource proxy (`stage`/`dev`/`prod`). `make backend-up` cannot bring up a remote environment, so on an unreachable staging/prod host the guidance is misleading — the real causes are a bad/expired token, wrong URL/UID in `.env`, or network/VPN. The spec left the three curl sites' auth wiring untouched, but the human-facing message content wasn't part of that constraint and is now inaccurate. Consider a hint that points at the `.env` URL/token and connectivity instead.

## Notes (no action required)

- `.env.example` itself ends with a trailing newline (verified), so a plain `cp .env.example .env` followed by uncommenting preserves termination — finding 1 only bites when the user re-types or appends the last line without one. Still worth the one-line guard given how silent the failure is.
- Parsing (not sourcing) is done correctly — no `eval`/`source`, so a malicious token or URL field in `.env` cannot execute. Good.
- `--env` value handling is sound: missing value (`--env` with nothing after) is caught at `:532`; an unknown/ambiguous value (`--env window`) surfaces as "Unknown environment" with the available list. Acceptable.
- `SCRIPT_DIR` via `${BASH_SOURCE[0]}` + `cd … && pwd` correctly resolves `.env` through the `~/.claude/skills` symlink regardless of `$PWD`. Correct per spec.
- Heredoc was switched from `<<'EOF'` to `<<EOF` to allow `$(list_env_names)` expansion; the body contains no other `$`/backtick that would expand unintentionally. Correct.
- `.gitignore` uses the exact path `/src/skills/observe-logs/.env`, which ignores the real registry without touching `.env.example`. Correct.
