## Plan Review Summary

**Plan:** `81-1-12-observe-logs-pyramid-pass.md` (milestone 1.12 — observe-logs: pyramid pass)
**Artifacts Reviewed:** plan, spec `32-observe-logs-pyramid-pass.md`, ROADMAP.md line 1.12, target `src/skills/observe-logs/SKILL.md` (235 lines), `scripts/query-loki.sh` (untouched), `.env`/`.env.example` presence
**Risk Level:** 🟢 Low

### Context Gates
- **Roadmap linkage — PASS.** The plan's `# Plan: 1.12 — observe-logs: pyramid pass` heading resolves to ROADMAP.md:181 under Phase 1 ("Rewrite the skill package to the pyramid") of the "Pyramid rewrite" direction. The milestone's `Spec:` tag points at `specs/32-observe-logs-pyramid-pass.md`, which the plan follows faithfully. The phase names no separate `Governing spec:`.
- **Artifact reconciliation — PASS (and correctly done).** The working tree carries uncommitted edits to ROADMAP.md and spec 32 that replace the phantom `OBS_LOKI_URL` with the real `--env`/`.env` endpoint registry, and add the explicit **partition rule**. Plan, spec, and roadmap line are now mutually consistent. The plan's Assumptions section grounds the `OBS_LOKI_URL` drift against ground truth (`SKILL.md:44–73`) exactly right — there is no `OBS_LOKI_URL`; the endpoint is selected via required `--env`. Ground truth wins, and the plan introduces none.
- **Architecture gate — PASS.** Moving deep detail into an intra-skill `references/` file is standard progressive disclosure, already applied by 1.9.2 / 1.10 / 1.11 in this same phase. It is not a skill extraction, so the composition rule (mechanism-vs-policy) and `loads:`/reverse-graph markers do not apply — no frontmatter or dependency-map change is needed, and the plan correctly requires none.
- **Rules gate — N/A.** No `.ai-factory/RULES.md` in this repo.

### Critical Issues
None.

### Line-reference verification
Every line anchor the plan cites matches the current SKILL.md:
- Raw LogQL templates section — `:188–222` ✓ (header 188, curl blocks 199–222, export preamble 194–197)
- Structured-metadata schema detail — `:32–37` ✓; the "single most common mistake" blockquote — `:39–40` ✓ (plan keeps it in the body, one home)
- `since-restart` two-step LogQL blocks — `:104–120` ✓; the "Error if no marker … 7-day lookback" note — `:121–123` ✓ (kept as caller-facing failure behavior)
- `trace` base-selector note (`{service_name=~".+"}`) — `:140–142` ✓; `--limit` (default 200) flag — `:143` ✓ (verbatim-protected, kept)
- `window` default-selector note — `:162–163` ✓; "Two calling modes" block — `:168–175` ✓ (kept as caller-facing output behavior)

### Partition soundness
The keep/move dispositions tile every touched section with no gap or overlap. The one non-obvious case is handled correctly and explicitly: the single sentence at `:162` ("All filters are optional; omitting them defaults to `{service_name=~".+"}` …") is split at the clause boundary — "all filters optional" stays in the body (lens), the default-selector mechanism clause moves to references. The plan calls this out in Task 2 and grounds it in the spec's per-line partition rule, so it is a deliberate sub-line disposition, not silent byte loss.

The verbatim-protected set (`--limit` default 200 and where it applies, unbounded `since-restart`, the `GET`-only `/ready`/`query_range`/`labels`/`series` discipline and "No push, no delete … ever") is all correctly retained in the body. The re-basing rule is a defensive no-op here (no `references/` pointers exist inside the moved blocks yet) but the plan correctly instructs grep-not-enumeration rather than asserting none exist.

### Positive Notes
- The OBS_LOKI_URL drift is resolved by ground truth, not papered over — and the spec/roadmap were brought into line rather than left contradicting the body.
- Verbatim-protection, closure, re-basing, and partition rules are each pinned with an explicit mid-pass resolution policy, so a disposition discovered during implementation is handled without re-planning.
- The verification bar is concrete and matches the spec: `query-loki.sh` byte-identical, materially slimmer body, and a live pre/post baseline on `since-restart` and `window --level` (the `.env` registry is present, so the local Loki baseline is runnable).
- Forward note for the implementer (non-blocking, wording latitude already granted by the plan): `references/logql.md` will hold not only ad-hoc/hand-written-query detail and deep schema but also *subcommand LogQL internals* (the `since-restart` two-step, the base-selector mechanism). When authoring the intro line and the body pointer, phrase them so a reader seeking "why does `since-restart` issue two queries" is still routed there — the plan leaves this wording to the implementer, so no plan change is required.

PLAN_REVIEW_PASS
