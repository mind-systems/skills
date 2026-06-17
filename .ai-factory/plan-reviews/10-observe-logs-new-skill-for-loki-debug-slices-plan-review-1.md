# Plan Review: observe-logs — new skill for Loki debug slices

**Plan:** `.ai-factory/plans/10-observe-logs-new-skill-for-loki-debug-slices.md`
**Files Reviewed:** plan + spec note `notes/20-observe-logs-skill.md`, ROADMAP milestone, repo skill conventions, validate.sh, symlink topology
**Risk Level:** 🟢 Low

## Context Gates

- **Architecture (`ARCHITECTURE.md`):** PASS. ARCHITECTURE.md does not enumerate individual skills, so adding a new package under `src/skills/` introduces no boundary or dependency violation and needs no registration entry (unlike `command-handoff`, which added a brand-new artifact *type*). No action required.
- **Rules (`RULES.md`):** none present → skipped (WARN: optional file absent, non-blocking).
- **Roadmap (`ROADMAP.md`):** PASS. Cleanly linked — milestone "observe-logs: new skill for Loki debug slices" (line 25, `[ ]`) and spec `notes/20-observe-logs-skill.md` both match the plan scope, label schema, endpoint default, and three-slice design. Strong traceability.
- **Skill-context (`skill-context/aif-review/SKILL.md`):** absent → no project overrides to apply.

## Critical Issues

None. The plan is well-scoped, read-only by design, and faithful to the spec note. No security concerns (no writes, no secrets, endpoint env-configurable with a local default).

## Findings

### 🟡 Medium — `since-restart` marker search has an unspecified (and likely too-narrow) time window
Task 2's marker query is "backward `direction`, `limit=1`" but never specifies a `start` for that first `query_range` call. Loki's `/loki/api/v1/query_range` defaults `start` to roughly **one hour ago** when omitted. If the target service last restarted more than the default window ago (the common case for a long-running backend), the marker query returns zero rows and the script will report a false **"no marker found"** — defeating the slice's purpose.

*Recommendation:* mandate an explicit, generously wide look-back for the marker query (e.g. default 7d, ideally overridable via a flag/env), independent of the subsequent record fetch. Worth calling out in Task 2's acceptance criteria.

### 🟢 Low — structured-metadata key names are unverifiable assumptions
The plan correctly flags that `event.name` / `service.name` sanitize to underscored keys, and instructs the implementer to "match the actual structured-metadata key." Good. But neither `event_name` nor the `trace_id` metadata key can be confirmed without a live backend (`make backend-up`), and the "Done when" in the spec note explicitly requires validation against a running Loki. Since this plan's Settings say *Testing: no*, there is no in-plan verification step that would catch a wrong key (a wrong key silently returns empty results, not an error).

*Recommendation:* add a small "verify against a running backend" step (or note it as a post-implementation manual check), and keep the metadata key names in clearly-marked single constants in the script so a mismatch is a one-line fix.

### 🟢 Low — add a structure/security validation step
No task runs `aif-skill-generator/scripts/validate.sh` against the finished package. The frontmatter as specified is comfortably within limits (~48 words vs. the 100-word cap; `name` matches dir; `argument-hint` brackets are quoted), so this is preventive, not a known defect — but a quick `validate.sh src/skills/observe-logs` after Task 3 cheaply guards the spec constraints.

### ℹ️ Info — no migration / symlink work needed (correctly omitted)
Confirmed `~/.claude/skills → src/skills` is a **directory-level** symlink, so the new `observe-logs/` package is auto-discovered with no per-skill link step. The plan rightly omits one. Likewise, no security scan is required (self-authored, not external per CLAUDE.md). No gaps here.

## Positive Notes

- Tight alignment between plan, spec note, and roadmap — label schema, `OBS_LOKI_URL` default, read-only endpoint allowlist, and the two-request `since-restart` recipe are consistent across all three.
- Read-only discipline is explicit and repeated (only `GET` to `/ready`, `/query_range`, `/labels`, `/series`) — good security posture for a debug tool.
- Backend-down guard with `--max-time` and a clear actionable message (`make backend-up`) is the right ergonomic call and prevents hangs.
- Correctly captures the three highest-value traps as first-class instructions: `service.name`→`service_name`, `trace_id` as structured metadata not a label, and `since-restart` being two requests.
- Sensible dependency ordering (plumbing → subcommands → SKILL.md) and the 500-line `references/` overflow valve is pre-planned.

## Verdict

The plan is solid and implementable. The Medium finding (marker-query window) is the only item that could cause an outright wrong result rather than a cosmetic issue, and even that is a refinement within the existing task rather than a missing task. None block proceeding; fold them into Task 2/Task 3 acceptance notes during implementation.

PLAN_REVIEW_PASS
