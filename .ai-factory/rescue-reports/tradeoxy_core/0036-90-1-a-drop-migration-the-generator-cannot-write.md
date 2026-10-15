# 90.1 — a drop migration the generator cannot write

**Project:** tradeoxy_core
**Date:** 2026-10-15
**Stopped at:** escalated
**Elapsed before the rescue:** 122
**Sessions:** planner: 8a770565-3f9b-442b-9bc5-bd3bf4be086f, plan-reviewer-1: cdc769aa-d64e-4429-ae89-552979b32a5e

The planner covered the task in full. It removed the `45s` entry, its gap-fill row, the entity and its registrations, and the DTO texts, and adjusted the suites that held the width. For the table it planned to delete the entity, run `migration:generate`, and stop if the generator emitted no drop. The plan reviewer stopped on a decision outside its authority. The task spec asked for «a generated migration [that] drops `candles_45s`», and RULES.md «Migrations — never write by hand» forbids a hand-written one. TypeORM 0.3.28's generator cannot emit that drop: `RdbmsSchemaBuilder` loads only the tables of existing entities, and nothing in it calls `dropTable`. So the plan's own stop would fire on every run. The earlier table drop the plan cited, `DropIndicatorConfigs`, was caught hand-written by its first review, and how it was later «regenerated» is recorded nowhere. The reviewer offered four ways: generate inverted against a scratch database and swap `up` and `down`, record a RULES.md exception for table drops, generate from an empty database and extract, or leave the table in place.

The governing spec, `docs/candle-pipeline/what-a-bar-is.md`, was not at issue; it says nothing about migrations.

> Decide how a migration that drops a table with no entity is produced in this repository, when the generator cannot emit it and the rule forbids writing it by hand.

## What was done

The user ruled that no drop migration is needed: there is no data, so the migration that creates the table is edited instead. RULES.md gets nothing, so that a case like this escalates again rather than passing under a standing exception. Escalation option 1 was taken: the decision is recorded in this task's spec.
- **Spec `0334` and the 90.1 contract line:** the creating migration, `1710000000010-Add45sContinuousAggregate.ts` (class `CreateCandles45sHypertable1710000000010`), which creates only `candles_45s` and its hypertable, is deleted, and no new migration is written. TypeORM's `getPendingMigrations` ignores an executed migration whose file is gone. The `Database:` clause says the application's database keeps its empty `candles_45s` and the migration's row as they are, and nothing drops them.
- **Full reset:** the plan, the plan review and the sidecar were deleted.
- **Propagation:** no other open spec of the phase touches a migration.
