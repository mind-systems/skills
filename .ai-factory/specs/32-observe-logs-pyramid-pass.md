# observe-logs: pyramid pass — the script is the engine, the skill becomes its lens

## Current state

`src/skills/observe-logs/SKILL.md` (235 lines) duplicates its own engine: the real mechanism lives in `scripts/query-loki.sh` (three subcommands, pagination, merged formatting, backend guard), yet the body restates the label schema, raw LogQL templates, and recipe detail alongside the subcommand documentation. The pyramid shape is already there — script below, skill above — but the skill carries mass the script already embodies.

## Change

One pyramid pass:

- **Body keeps (the lens):** when-to-use, the three subcommands with one-line semantics each (`since-restart` / `trace` / `window` + flags), the read-only discipline, `OBS_LOKI_URL` and its default, and the one schema fact callers must know to *choose* a query (label names; `service.name`→`service_name`).
- **Move to `references/`:** raw LogQL templates and schema detail beyond the choosing-level facts — read only when the canned subcommands don't fit and a hand-written query is needed.
- **Verbatim-protected:** the subcommand flag semantics (`--limit` default 200 and where it applies; unbounded `since-restart`), read-only `GET`-only discipline.
- Two-reader register.

## Guards

- **Behavior-identical** — the script is untouched; only the SKILL.md reorganizes; every fact moved lands byte-identical in `references/`.
- Frontmatter unchanged.
- Live baseline before the next phase task: `since-restart` and `window --level` runs against local Loki pre/post — same commands chosen, same output.

## Verification

- `scripts/query-loki.sh` byte-identical; body materially slimmer; LogQL detail behind a pointer.
- Baseline runs: identical command lines issued for the same three asks.
