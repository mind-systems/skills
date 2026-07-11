# Plan: 1.12 — observe-logs: pyramid pass

## Context
The 235-line `observe-logs/SKILL.md` restates the engine that already lives in `scripts/query-loki.sh`; this pass slims the body to a lens (when-to-use, three subcommands + flags, endpoint selection, read-only discipline, choosing-level schema facts) and moves the raw LogQL templates and deep schema detail to `references/`, byte-identical, with the script untouched.

## Assumptions
- **`OBS_LOKI_URL` drift:** the roadmap line and spec name `OBS_LOKI_URL`, but the actual skill (and `.env.example`) select the endpoint via a required `--env <name>` flag resolving a `.env` registry — there is no `OBS_LOKI_URL`. Ground truth wins: the plan keeps the real `--env`/`.env` endpoint-selection facts in the body verbatim and introduces **no** `OBS_LOKI_URL`. The spec's `OBS_LOKI_URL` phrasing is read as shorthand for "the endpoint-selection fact the caller needs to choose/invoke a query".
- No `references/` directory exists yet; it will be created.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Extract deep detail to references

- [x] **Task 1: Create `references/logql.md` with the moved engine detail**
  Files: `src/skills/observe-logs/references/logql.md` (new)
  Move, **byte-identical**, the content that a reader needs only when the canned subcommands don't fit and a hand-written query is required:
  - The **Raw LogQL templates** section (current SKILL.md lines ~188–222): the `export LOKI_URL`/`LOKI_AUTH` preamble and every `curl` template (error logs, service+level, trace filter, list labels, list label values).
  - The **structured-metadata schema detail** beyond the choosing-level facts (current lines ~32–37): the "all other fields are structured metadata" explanation, the `trace_id` / `span_id` / request-ID / `event.name`→`event_name` pipeline rules. The `> **The single most common mistake:**` blockquote at `:39-40` is **not** part of this move — it stays in the body per Task 2's keep-list (one home, no double disposition).
  - The **subcommand LogQL internals** that the script already embodies: the `since-restart` two-step query blocks (`event.name="service.start"` marker query, direction/limit, the paginated `{service_name="<svc>"}` fetch — current lines ~104–120); the `trace` base-selector mechanism note (`{service_name=~".+"}` — current lines ~140–142); and the `window` default-selector mechanism note (`omitting them defaults to {service_name=~".+"}` / bare `{}` is rejected — current lines ~162–163). Move the LogQL/mechanism prose; the flag semantics stay in the body (see Task 2).
  Give the file a short intro line stating it holds ad-hoc/hand-written-query detail read only when the three subcommands don't suffice.
  **Re-basing rule (the one documented exception to byte-identical):** inside every moved block, rewrite any relative pointer for its new base — a `references/<X>` path becomes the sibling `<X>`, and any cross-reference to a step/label that no longer exists is re-pointed to its new home. Find occurrences by `grep`, never by enumeration; fix any discovered mid-pass on the spot. All other bytes land identical.
  **Closure rule:** any sentence stating a contract is protected verbatim whether or not it is listed here; a contract-bearing sentence found mid-pass joins the protected set on the spot.
  **Partition rule (per spec 32):** Task 1's move-set and Task 2's keep-set must partition every touched section — each line has exactly one home (body or `references/logql.md`), no line undispositioned, no line dispositioned twice. Verify with one continuous sweep over the touched sections (line accounting, never per-instance enumeration); a gap or overlap found mid-pass is resolved on the spot by the line's nature (contract/lens → body; mechanism restatement → reference) — not a plan defect.

### Phase 2: Slim the body to the lens

- [x] **Task 2: Reduce `SKILL.md` to the lens and add the references pointer** (depends on Task 1)
  Files: `src/skills/observe-logs/SKILL.md`
  Keep the body as the lens; cut what Task 1 moved. Specifically:
  - **Label schema →** keep only the choosing-level facts: the label names (`project`, `service_name`, `level`) and the `service.name`→`service_name` rule (the "single most common mistake" that decides *which* selector to write). Remove the structured-metadata subsection (moved to references).
  - **Endpoint** and **Running the script** → keep as-is; this is how a caller chooses and invokes a query (the `--env`/`.env` lens). Do not introduce `OBS_LOKI_URL`.
  - **Subcommands** `since-restart` / `trace` / `window` → keep one-line semantics + flags + the example invocations for each; drop the two-step LogQL query blocks and the base-selector mechanism prose (moved to references). For `since-restart` specifically: **keep** the "Error if no marker is found (service may not emit this event, or hasn't restarted in the 7-day lookback window)" note (`:121–123`) in the body — caller-facing failure behavior that tells the caller why an empty feed came back, part of the lens; only the two-step LogQL query blocks (`:104–120`) move. For `window` specifically: **keep** the "all filters optional" fact and **keep** the "Two calling modes" block (`:168–175` — single-service vs cross-service, and the cross-service output being globally time-ordered / interleaved chronologically, not grouped by service) in the body — this is caller-facing output behavior a caller needs to *choose* between the two modes, part of the lens, not engine restatement; **move** only the raw default-selector mechanism note (`:162–163`, per Task 1).
  - **Raw LogQL templates** section → remove entirely; replace with a one-line pointer in the sibling style used across the repo, e.g. `Ad-hoc / hand-written queries and the deep label schema → read \`references/logql.md\`.`
  - **Read-only discipline** section → keep verbatim.
  **Verbatim-protected (do not reword):** the subcommand flag semantics — `--limit` default 200 and where it applies (`trace`, `window`), the unbounded/no-line-cap `since-restart` feed — and the read-only, `GET`-only discipline (the `/ready`, `query_range`, `labels`, `series` list; "No push, no delete, no write of any kind — ever"). Frontmatter unchanged.
  **Two-reader register:** the body reads top-to-bottom as a lens for choosing a query; the reference is consulted only when a hand-written query is needed.

## Verification
- `scripts/query-loki.sh` byte-identical (untouched).
- `SKILL.md` materially slimmer; raw LogQL detail and deep schema reachable only via the `references/logql.md` pointer.
- Baseline (before the next phase task): run `since-restart` and `window --level` against local Loki pre/post — the same command lines are issued for the same asks.
