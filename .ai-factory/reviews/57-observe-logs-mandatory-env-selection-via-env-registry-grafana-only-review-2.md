# Code review (re-review): observe-logs mandatory env selection via `.env` registry

Re-review after fixes for `.ai-factory/reviews/57-…-review-1.md`. Files re-read from disk (not session memory).

## Verdicts on previous findings

### Finding 1 (Medium) — last `.env` line dropped without trailing newline: **FIXED**

Both parse loops now carry the guard. `query-loki.sh:43` (`list_env_names`) and `query-loki.sh:64` (`resolve_env`):

```bash
while IFS='|' read -r name url auth || [[ -n "$name" ]]; do
```

On a final line with no trailing newline, `read` sets `name`/`url`/`auth` and returns non-zero, but `[[ -n "$name" ]]` is true, so the loop body still processes that line. On real EOF, `name` is empty and the loop terminates. Applied to both parsers consistently — the fix is correct.

### Finding 2 (Low) — stale `make backend-up` recovery hint: **FIXED**

`query-loki.sh:95`:

```bash
echo "       Check the URL/token for this environment in .env, and your network/VPN connectivity." >&2
```

SKILL.md `:70-72`:

```
If the backend is unreachable the script prints one clear line pointing at the
`.env` URL/token for that environment and network/VPN connectivity, then
exits non-zero immediately.
```

The `make backend-up` / observability-repo hint is gone from both the script and SKILL.md, replaced with guidance appropriate to a remote-only Grafana setup.

## New review

Re-read the changed regions of `query-loki.sh`, `SKILL.md`, `.env.example`, and `.gitignore` in full. No new correctness, security, or runtime issues:

- The `|| [[ -n "$name" ]]` guard preserves the comment/blank-skip logic (`[[ -z "$name" || "$name" == \#* ]] && continue`) unchanged.
- `.env.example` still terminates with a newline (`…Bearer glsa_<token>\n`), so a `cp .env.example .env` + uncomment keeps the file well-formed.
- Parsing (not sourcing) via `IFS='|' read` remains — no injection surface from `.env` contents.
- `${BASH_SOURCE[0]}`-based `SCRIPT_DIR`/`REGISTRY_FILE` resolution, mandatory leading `--env` dispatch, and the exact-path `/src/skills/observe-logs/.env` gitignore (leaving `.env.example` tracked) are all correct.

REVIEW_PASS
