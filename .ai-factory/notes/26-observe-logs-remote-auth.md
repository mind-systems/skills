# observe-logs: remote Loki auth

**Date:** 2026-06-26
**Source:** conversation context

## Key Findings

- `query-loki.sh` has no auth support — all curl calls are unauthenticated.
- Two env vars cover both local and remote: `OBS_LOKI_URL` (base URL) and `OBS_LOKI_AUTH` (Authorization header value). Nothing else, nothing hardcoded in the skill.
- For remote via Grafana Service Account, the datasource UID is embedded in `OBS_LOKI_URL` — the script stays unaware of Grafana internals.
- Default (both vars unset) must be a no-op — local backend works without any configuration.

## Details

### Two modes, two env vars

**Local (no auth):**
```bash
# OBS_LOKI_URL defaults to http://localhost:3100 — nothing to set
# OBS_LOKI_AUTH unset — no Authorization header sent
```

**Remote via Grafana Service Account:**
```bash
export OBS_LOKI_URL=https://grafana.example.com/api/datasources/proxy/uid/<datasource-uid>
export OBS_LOKI_AUTH="Bearer <grafana-service-account-token>"
```

The Grafana datasource UID is baked into `OBS_LOKI_URL`. The script appends Loki API paths (`/loki/api/v1/query_range`, `/ready`, etc.) to whatever base URL is set — it never inspects the URL structure.

### Files to edit

**`src/skills/observe-logs/scripts/query-loki.sh`**

1. Configuration section — add after `LOKI_URL` line:
   ```bash
   LOKI_AUTH="${OBS_LOKI_AUTH:-}"
   ```

2. Auth header helper (before `check_backend`):
   ```bash
   auth_header() {
     [[ -n "$LOKI_AUTH" ]] && echo "-H" "Authorization: ${LOKI_AUTH}"
   }
   ```

3. Add `$(auth_header)` to every `curl` call — three sites: `check_backend`, `query_range`, `/ready` check. When `OBS_LOKI_AUTH` is unset the helper outputs nothing — no empty header is sent.

**`src/skills/observe-logs/SKILL.md`** — replace Endpoint section:

```markdown
## Endpoint

Two environment variables control the connection. Neither has a hardcoded fallback
beyond the local defaults — the skill never stores or assumes a credential.

| Variable | Default | Purpose |
|---|---|---|
| `OBS_LOKI_URL` | `http://localhost:3100` | Loki base URL |
| `OBS_LOKI_AUTH` | _(unset)_ | Full `Authorization` header value |

**Local backend (no auth):** leave both unset. The script hits Loki directly on localhost.

**Remote via Grafana Service Account:** set both. The datasource UID goes into the URL:

```bash
export OBS_LOKI_URL=https://grafana.example.com/api/datasources/proxy/uid/<uid>
export OBS_LOKI_AUTH="Bearer <service-account-token>"
```

Set these in the shell environment or a secrets manager — never in committed files.
```

### How to find the datasource UID

```bash
curl -s http://localhost:3000/api/datasources/name/Loki \
  -H "Authorization: Bearer <admin-token>" | jq '.uid'
```

### Verification

```bash
# Local
query-loki.sh window 5m

# Remote
export OBS_LOKI_URL=https://grafana.example.com/api/datasources/proxy/uid/abc123
export OBS_LOKI_AUTH="Bearer glsa_xxxx"
query-loki.sh window 5m
```

Wrong token → `ERROR: Loki backend unreachable` (HTTP 401 from Grafana).
