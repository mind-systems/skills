# 53.1 — A step deferred to a task that landed without it

**Project:** tradeoxy_core
**Date:** 2026-09-18
**Stopped at:** escalated (implementer)
**Elapsed before the rescue:** 667

Task `53.1` is the schema-only floor of Phase 53: a fourth `IndicatorConfigState` member, a nullable `failure_reason` column, the widened state check, and the cause surfaced on the response DTO. The plan passed review on its second round; the implementer made the entity edits, ran `migration:generate` against a fully-migrated database, and stopped exactly where the plan told it to: the generator emitted a statement the task did not account for — `ALTER TABLE "layouts" ALTER COLUMN "mode" DROP DEFAULT`.

The statement is not noise. In July, the task that added `layouts.mode` kept a `DEFAULT 'live'` on purpose — without it, layout creation and duplication would have failed on `NOT NULL` until the write paths learned to name `mode` — and its plan deferred the `DROP DEFAULT` to the task that finished that wiring, saying so in as many words: "add a `DROP DEFAULT` step to the 40.4 task when it is decomposed." That task landed without a migration. The entity has never declared the default; both write paths name `mode` explicitly today; and the schema has carried a default the entity does not know about ever since. Phase 53's first task was simply the first `migration:generate` since — the phantom would have surfaced on whichever task ran the generator next, and on every one after it until something dropped the default.

Two more things the run found on the way, both correct and both pointing upstream. The reviewer caught that the task's own description — widen the check "under its existing name" — is unreachable through the generator: TypeORM diffs check constraints by name alone, so a same-name widening emits nothing and the database keeps the two-value constraint until the first `state = 'failed'` write is refused at runtime. The planner renamed the constraint and recorded the deviation; the second review passed it. And both reviews flagged that the project's own rule text quotes a `--name=<name>` form the installed CLI does not have, so every plan that copies the rule fails on its first run.

> The decision the run stopped on: where does the deferred `DROP DEFAULT` land — folded into this task's migration as a fourth statement, in its own task ahead of this one, or left for every future generate to re-decide?

The user ruled the second. The migration file for this task keeps its own name honest, and the debt of Phase 40 closes where someone would look for it.

## What was done

A new task was written ahead of `53.1` in file order: the schema catches up with `Layout.mode` — one generated migration with exactly one statement and its mirror, with stop conditions for more (escalate) and for none (already caught up, no empty migration). `53.1`'s own description and contract line were corrected to the reachable target: the widened check under a new name, the generator's positional command form, and a dependency on the new task so its own migration carries only its own statements. The rule text in `RULES.md` and `ARCHITECTURE.md` was corrected to the command the CLI accepts. The architecture map's schema table gained the `layouts.mode` column it had lacked since July, and the phase note took on the obligation to update the `active_indicators` row once the phase's schema tasks land.

The failed run's plan, both plan reviews, its sidecar, its partial entity edits, and the migration it generated were all removed, so the task re-plans from a clean tree against a description that can be executed.
