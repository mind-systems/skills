# Code Review: 1.12 — observe-logs: pyramid pass

**Scope:** `src/skills/observe-logs/SKILL.md` (modified), `src/skills/observe-logs/references/logql.md` (new). Non-code artifacts (ROADMAP, spec, plan, plan-review, plan JSON) reviewed for consistency but not the subject of code correctness.

**Nature of change:** Documentation/skill reorg (pyramid pass). No executable code changed — `scripts/query-loki.sh` is untouched (confirmed: not in the diff, not in `git status`). The correctness bar for this change is the spec's guard **"every fact moved lands byte-identical in `references/`"** plus behavior-identical (same command lines chosen for the same asks) and the verbatim-protected set.

## What is correct

- **Script untouched.** `scripts/query-loki.sh` does not appear in the diff or status — the engine is byte-identical, satisfying the spec's central guard and the roadmap contract.
- **Byte-identical moves (4 of 5 blocks exact).** Verified against the pre-change text:
  - Structured-metadata subsection → `logql.md:11-16` — exact.
  - `since-restart` two-step block → `logql.md:22-37` — exact.
  - `trace` base-selector note → `logql.md:43-45` — exact.
  - Raw LogQL templates (intro + `export` block + all five `curl` templates) → `logql.md:58-90` — exact.
- **Re-basing rule correctly a no-op.** No moved block contained a `references/<X>` path or a step/label cross-reference, so no relative pointer needed rewriting. Nothing was spuriously rewritten under that banner.
- **Verbatim-protected set intact:**
  - `--limit N` default 200 kept in both `trace` (`SKILL.md:116`) and `window` (`:137`).
  - Unbounded `since-restart` ("full log feed … no line cap") kept (`:90-91`).
  - Read-only `GET`-only discipline block (`:165-174`) — the `/ready` / `query_range` / `labels` / `series` list and "No push, no delete, no write of any kind — ever" — unchanged.
  - Frontmatter (`:1-12`) unchanged.
- **Dispositions from the plan honored.** The `since-restart` "Error if no marker" note (`:97-98`) kept in body; the `window` "Two calling modes" block (`:140-147`) kept in body; the "single most common mistake" callout (`:32-33`) kept as a choosing-level fact. `Endpoint` and `Running the script` kept as the caller-facing lens. Pointer (`:160-161`) matches the repo sibling-style convention.
- **No `OBS_LOKI_URL` introduced** — the plan's grounding decision was executed; the body keeps the real `--env`/`.env` mechanism.

## Findings

### 1. (Low) The `window` default-selector fact was reworded, not moved byte-identical

The one moved block that is **not** byte-identical. Original single sentence (pre-change `SKILL.md:162-163`):

> `All filters are optional; omitting them defaults to {service_name=~".+"} (Loki requires at least one non-empty matcher — bare {} is rejected).`

Post-change this was split: the body keeps `All filters are optional.` (`SKILL.md:135`) and the moved fragment landed at `references/logql.md:51-52` as:

> `Omitting filters defaults to {service_name=~".+"} (Loki requires at least one non-empty matcher — bare {} is rejected).`

The moved fragment was edited — `omitting them` → `Omitting filters`, lowercase→capital, and reflowed — rather than transplanted verbatim. This breaches the spec's guard "every fact moved lands byte-identical" and the plan's Task 1 instruction to move `:162-163` byte-identical. The re-basing exception does **not** sanction this: it covers relative-path/step-label pointers, not pronoun antecedents.

**Assessment:** meaning is fully preserved and the reword was *forced* by the plan-sanctioned split (the pronoun "them" lost its antecedent "filters" once the sentence was divided), so **behavior is identical** and there is no runtime or user-visible defect. This is a contract-text nit, not a bug. Severity Low.

**Options to resolve:**
- Make the fragment verbatim-plus-minimal: land it as `omitting them defaults to {service_name=~".+"} …` and let the reference's own sentence flow carry it (still reads, keeps the original bytes) — or
- Consciously accept the standalone adaptation as the minimal grammar change the split requires, and record it as an in-spirit re-basing (pronoun re-pointed to its new home, exactly parallel to the sanctioned "cross-reference re-pointed to its new home" clause).

Either is fine; the point is that this is the sole deviation from the byte-identical contract and should be an explicit decision rather than a silent edit.

## Behavior / runtime check

No runtime surface changed. The three subcommands still resolve to the same `query-loki.sh` invocations with the same flags and defaults; the reorg only relocates prose. The live baseline in the plan's Verification (`since-restart` and `window --level` pre/post) will pass — the command lines a reader would issue for the three asks are unchanged, because the subcommand one-liners, flags, and examples are intact.

## Verdict

One Low-severity finding (a moved fact that is meaning-identical but not byte-identical, forced by a sanctioned sentence split). No bugs, no security issues, no correctness/runtime risk. The finding is a contract-text precision nit worth an explicit accept-or-restore decision, not a blocker on behavior.
