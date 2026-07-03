## Code Review Summary

**Files reviewed (code changes only):**
- `src/skills/observe-logs/scripts/query-loki.sh` — auth config + guarded curl args
- `src/skills/observe-logs/SKILL.md` — Endpoint section + Raw LogQL caveat + usage heredoc

(Also present in the diff but not code: ROADMAP.md checkbox move, the plan `.md`/`.json`, and two plan-reviews — informational, not reviewed as code.)

**Risk Level:** 🟢 Low — implementation matches the plan, the one blocking risk from plan-review-1 (C1) is fixed and empirically verified on the target platform.

### What the change does

Adds an optional `Authorization` header to the two `curl` call-sites in `query-loki.sh`, driven by a new `OBS_LOKI_AUTH` env var, with the local/no-auth default preserved as a strict no-op. SKILL.md documents the two-var model, and the Raw LogQL block gets a one-line remote-auth caveat.

### Verification performed (on the actual target: bash 3.2.57, macOS)

- **`bash -n query-loki.sh` → parse OK.**
- **C1 fix confirmed correct.** The critical risk called out in plan-review-1 — a bare `"${AUTH_ARGS[@]}"` aborting on bash < 4.4 under `set -u` — is avoided. The code uses `${AUTH_ARGS[@]+"${AUTH_ARGS[@]}"}` at both sites. Reproduced with both env vars unset under `set -euo pipefail`: the empty-array expansion yields nothing, the script reaches the end, exit 0 — **no `unbound variable` abort**.
- **Header integrity with embedded spaces confirmed.** With `OBS_LOKI_AUTH="Bearer glsa_ab cd"`, the expansion produces exactly two argv elements: `-H` and `Authorization: Bearer glsa_ab cd` (the space-bearing value stays a single arg). The array approach correctly supersedes the spec note's buggy `echo`/`$(...)` word-splitting form.
- **`set -e` safety of the init line.** `[[ -n "$LOKI_AUTH" ]] && AUTH_ARGS=(…)` at top level does not trip `set -e` when `LOKI_AUTH` is empty (failing test on the left of `&&` is exempt) — verified by the run reaching the end with exit 0. Consistent with the existing `parts+=` idiom at line 408.
- **Default no-op path, backend down.** `env -u OBS_LOKI_AUTH … query-loki.sh window 5m` against a dead port prints the normal `Loki backend unreachable … (HTTP 000)` line and exits 1 — byte-identical behavior to pre-change. The auth-set path against the same dead port fails identically.

### Correctness / security notes

- **Both and only both curl sites are patched.** `check_backend`'s `/ready` probe (now line 29) and `query_range`'s GET (now line 113). Grep confirms these are the only two `curl` calls in the file; `query_range_all` reuses `query_range`, so it inherits auth. The plan's correction of the spec's "three sites" miscount holds.
- **No credential leakage.** The header value is never echoed or logged; `check_backend`'s error prints `${LOKI_URL}` only (not a credential). Header placed before `--data-urlencode`/`--get` args — order-independent for curl, no interaction with `--get`.
- **Placement of `--get` + `-H`.** In `query_range` the `-H` args sit between `--get` and the `--data-urlencode` params; curl treats header and data flags independently, so this is fine.
- **SKILL.md** renders correctly: two-row table, local/remote examples, secrets-manager caveat, backend-down paragraph and trailing `---` preserved; usage heredoc gains the `OBS_LOKI_AUTH` line under `OBS_LOKI_URL`; Raw LogQL caveat placed between the intro and the code fence.

### Residual risk (documented, out of scope — not a code defect)

The proxied `/ready` health check through a Grafana datasource proxy remains unverified against a live remote (per the plan's "Known risk" section and `Testing: no`). If some Grafana returns non-2xx for proxied `/ready` while `query_range` works, `check_backend` would wrongly block queries. This is a deployment/Grafana-config dependency, correctly flagged in the plan and deliberately not "fixed" by widening the success condition. No action required in this milestone.

### Findings

None. The code is correct, the blocking risk is resolved and verified on the exact target bash, and the default path is behavior-preserving.

REVIEW_PASS
