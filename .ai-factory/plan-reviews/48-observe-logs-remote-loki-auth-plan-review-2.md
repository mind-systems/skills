## Code Review Summary

**Files Reviewed:** 1 plan (`48-observe-logs-remote-loki-auth.md`) against 2 target files (`src/skills/observe-logs/scripts/query-loki.sh`, `src/skills/observe-logs/SKILL.md`) + spec note `.ai-factory/notes/26-observe-logs-remote-auth.md` + prior review `48-…-plan-review-1.md`
**Risk Level:** 🟢 Low — this revision resolves every finding from review-1; no blocking issue remains.

### Context Gates

- **Roadmap** (`ROADMAP.md:107`): ✅ Milestone "observe-logs: remote Loki auth" present and unchecked. Plan heading (`# Plan: observe-logs: remote Loki auth`) matches the milestone title; the milestone's `Spec:` tag points to `.ai-factory/notes/26-observe-logs-remote-auth.md`, which exists and matches the plan's scope. Linkage intact.
- **Architecture** (`ARCHITECTURE.md`): ✅ No boundary/dependency concern — the change is an env-var + curl-header addition inside a single leaf skill script; no cross-skill `loads:` contract touched.
- **Rules** (`RULES.md`): ⚠️ WARN — file absent (optional). No convention gate to apply.
- **skill-context** (`.ai-factory/skill-context/aif-review/SKILL.md`): ⚠️ WARN — absent (optional). No project overrides.

### Resolution of prior review (review-1)

- **C1 (blocking) — empty-array expansion under `set -u` on bash 3.2.57.** ✅ Resolved. Task 1 now prescribes the guarded form `curl ... ${AUTH_ARGS[@]+"${AUTH_ARGS[@]}"} ...`, names the exact target bash (3.2.57 via `#!/usr/bin/env bash` on macOS), explains why a bare `"${AUTH_ARGS[@]}"` aborts on bash < 4.4, and ties the reasoning to the file's existing empty-array discipline (`cmd_window` guard, lines 404-410). Verified correct: this idiom expands to nothing when the array is empty and preserves the embedded space in `Authorization: Bearer <token>` when set.
- **W1 — Raw LogQL templates stay unauthenticated.** ✅ Resolved. Task 4 adds a one-line caveat under the "For ad-hoc queries…" intro (SKILL.md line 172) telling the reader to append `-H "Authorization: ${OBS_LOKI_AUTH}"` for remote backends, without rewriting every example. Scoped as documentation-only, correctly.
- **W2 — `/ready` through the Grafana datasource proxy is unverified.** ✅ Handled honestly. The plan's "Known risk (out of scope, note only)" section documents the proxied-`/ready` dependency, explains it cannot be exercised under `Testing: no`, and explicitly instructs the implementer not to widen `check_backend`'s success condition without evidence. Appropriate given the milestone scope is auth-header support.

### Critical Issues

None.

### Verification performed

- **Line references are accurate.** Config line 10 (`LOKI_URL=…`) ✓; `check_backend` `/ready` curl at lines 20-22 ✓; `query_range` curl at lines 103-110 ✓; `cmd_window` empty-array guard at lines 404-410 ✓; usage heredoc `Environment:` block at lines 437-438 (line 438 is the `OBS_LOKI_URL` line to preserve) ✓; SKILL.md `## Endpoint` section 44-54 with the backend-down paragraph at 53-54 and trailing `---` at line 56 ✓; `## Raw LogQL templates` block 170-197 with intro at 172 ✓.
- **"Only two curl call-sites" is correct.** `grep -n curl query-loki.sh` returns exactly lines 20 and 103. The plan's correction of the spec's "three sites" miscount (check_backend *is* the sole `/ready` caller) is accurate, and it instructs patching any other `${LOKI_URL}` curl found during implementation as a safety net.
- **`set -e` safety of `AUTH_ARGS` init.** `[[ -n "$LOKI_AUTH" ]] && AUTH_ARGS=(…)` is safe under `set -euo pipefail` — the failing `[[ ]]` sits on the left of `&&`, which `set -e` exempts. The existing script already relies on this exact idiom (`[[ -n "$project" ]] && parts+=(…)`, line 399), so the plan is consistent with proven file behavior.
- **Security posture intact.** Task 1 forbids logging/echoing the header value; the header is provided as a full `Authorization` value via env only; `check_backend`'s error echoes `${LOKI_URL}` (not a credential). Matches the skill's read-only, no-hardcoded-vendor stance.
- **Default no-op guarantee.** With both env vars unset, `AUTH_ARGS` is empty, the guarded expansion yields nothing, and no `-H` is added — byte-identical to current behavior.

### Positive Notes

- **Correctly rejects the spec's buggy approach.** The spec note (lines 42-47) prescribes `auth_header() { … echo "-H" "Authorization: …"; }` invoked as unquoted `$(auth_header)`, which word-splits `Bearer <token>` on the space. The plan replaces it with a bash array and explains why — a justified deviation, since the note is research-genre, not contract text.
- **Deviations from prior review are all closed with concrete instructions**, not hand-waves — each fix names the file, line range, and exact syntax, leaving no fantasy holes for the implementer.
- **Settings honored:** `Testing: no` / `Docs: no` are consistent with the change (a shell-only env-var addition plus in-skill SKILL.md prose, which is skill content, not project docs).

---

**Verdict:** Solid. All review-1 findings resolved, line references verified against the live files, bash idioms correct and consistent with the script's existing discipline, and the one residual risk is explicitly documented and scoped out. Ready for implementation.

PLAN_REVIEW_PASS
