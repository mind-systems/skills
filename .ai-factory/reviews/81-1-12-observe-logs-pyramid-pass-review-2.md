# Code Review (re-review): 1.12 — observe-logs: pyramid pass

Re-review after fixes to review-1. Files re-read fresh via `git diff HEAD`; session memory not trusted.

## Per-finding verdicts from review-1

### Finding 1 (Low) — `window` default-selector fact reworded, not moved byte-identical — **FIXED**

Previous state: `references/logql.md` held a reworded fragment (`Omitting filters defaults to …`), diverging from the source text.

Current content, `src/skills/observe-logs/references/logql.md:49-52`:

```
## `window` default selector

omitting them defaults to `{service_name=~".+"}` (Loki requires at least
one non-empty matcher — bare `{}` is rejected).
```

Source fragment (pre-change `SKILL.md:162-163`, the tail of the fused sentence after `All filters are optional; `):

> `omitting them defaults to {service_name=~".+"} (Loki requires at least one non-empty matcher — bare {} is rejected).`

**Verdict: Fixed.** The moved fragment is now the verbatim tail of the original sentence — token-for-token identical (only soft-wrap column differs, which markdown ignores). This is exactly option 1 the prior review offered. The body keeps `All filters are optional.` (`SKILL.md:135`), so the fused sentence's two facts are split with each landing verbatim in its home. The byte-identical guard is now satisfied for all five moved blocks.

Note (not a finding): under its standalone heading the fragment opens lowercase with a pronoun (`omitting them …`) whose antecedent lived in the body. This is the deliberate, sanctioned tradeoff of a verbatim move — cosmetic only, meaning unambiguous given the `## \`window\` default selector` heading. No action needed.

## Full re-review for new issues

- **Diff scope unchanged.** `git status` + `git diff HEAD` show only the two skill files (`SKILL.md` modified, `references/logql.md` new) plus non-code artifacts. `scripts/query-loki.sh` is absent from the diff — engine byte-identical, spec's central guard held.
- **The four previously-verified byte-identical moves are unchanged** (structured metadata → `logql.md:9-16`; `since-restart` two-step → `:20-37`; `trace` base selector → `:41-45`; raw LogQL templates → `:56-90`). The only edit since review-1 is the Finding-1 fix.
- **Verbatim-protected set still intact:** `--limit` default 200 in `trace` (`SKILL.md:116`) and `window` (`:137`); unbounded `since-restart` "full log feed … no line cap" (`:90-91`); read-only `GET`-only discipline block (`:165-174`); frontmatter (`:1-12`).
- **Plan dispositions still honored:** `since-restart` error note kept in body (`:97-98`); `window` "Two calling modes" kept (`:140-147`); "single most common mistake" callout kept (`:32-33`); `Endpoint` + `Running the script` kept as the lens; pointer `references/logql.md` in sibling style (`:160-161`). No `OBS_LOKI_URL` introduced.
- **Runtime/behavior:** no executable surface changed; the three subcommands resolve to the same `query-loki.sh` invocations with the same flags/defaults. The plan's live baseline (`since-restart`, `window --level` pre/post) will issue identical command lines. No migration, type, or race concern — this is a prose relocation.

No new issues.

REVIEW_PASS
