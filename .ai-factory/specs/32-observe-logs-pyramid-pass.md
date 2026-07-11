# observe-logs: pyramid pass — the script is the engine, the skill becomes its lens

## Current state

`src/skills/observe-logs/SKILL.md` (235 lines) duplicates its own engine: the real mechanism lives in `scripts/query-loki.sh` (three subcommands, pagination, merged formatting, backend guard), yet the body restates the label schema, raw LogQL templates, and recipe detail alongside the subcommand documentation. The pyramid shape is already there — script below, skill above — but the skill carries mass the script already embodies.

## Change

One pyramid pass:

- **Body keeps (the lens):** when-to-use, the three subcommands with one-line semantics each (`since-restart` / `trace` / `window` + flags), the read-only discipline, the `--env`/`.env` endpoint-registry selection facts (there is no `OBS_LOKI_URL` — removed by milestone 11's registry rework; ground truth confirmed at `SKILL.md:44-73`), and the one schema fact callers must know to *choose* a query (label names; `service.name`→`service_name`).
- **Move to `references/`:** raw LogQL templates and schema detail beyond the choosing-level facts — read only when the canned subcommands don't fit and a hand-written query is needed.
- **Verbatim-protected:** the subcommand flag semantics (`--limit` default 200 and where it applies; unbounded `since-restart`), read-only `GET`-only discipline.
- **Closure rule — protection is by criterion, not enumeration:** *any* sentence stating a contract is protected verbatim whether or not listed above; a contract-bearing sentence discovered mid-pass joins the protected set on the spot — it is not a plan defect and does not require re-planning.
- **Re-basing rule — the one documented exception to byte-identical:** moving text changes the base its relative references resolve against, so inside every moved block a relative pointer is rewritten for the new position — a `references/<X>` path becomes the sibling form `<X>` once the text itself lives inside `references/`; a cross-reference to a step number/label that ceases to exist is re-pointed to its new home. Applied **symmetrically to every occurrence** (find them by grep, never by enumeration); all other bytes land identical. An occurrence discovered mid-pass is fixed on the spot — not a plan defect.
- **Partition rule — keep and move tile the touched text exactly:** the keep-set and the move-set must partition every touched section — each line has **exactly one** home (body or reference), no line undispositioned (silent byte loss), no line dispositioned twice (duplicate or contradictory homes). Verified by one continuous sweep over the touched sections — line accounting, never per-instance enumeration. A gap or overlap discovered mid-pass is resolved on the spot by the line's nature (contract/lens → body; mechanism restatement → reference) — not a plan defect.
- Two-reader register.

## Guards

- **Behavior-identical** — the script is untouched; only the SKILL.md reorganizes; every fact moved lands byte-identical in `references/`.
- Frontmatter unchanged.
- Live baseline before the next phase task: `since-restart` and `window --level` runs against local Loki pre/post — same commands chosen, same output.

## Verification

- `scripts/query-loki.sh` byte-identical; body materially slimmer; LogQL detail behind a pointer.
- Baseline runs: identical command lines issued for the same three asks.
