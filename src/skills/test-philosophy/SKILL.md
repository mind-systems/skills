---
name: test-philosophy
description: >-
  Shared testing philosophy for the roadmap family. Holds one rule — write tests
  only for surfaces that fail silently (wrong output, no crash), skip surfaces that
  fail loudly (compile error, exception, DI failure, 4xx/5xx). Carries no
  test-generation or coverage-pipeline logic.
user-invocable: true
disable-model-invocation: false
allowed-tools: Read
---

# Test Philosophy — Shared Silent-Failure Testing Philosophy

This is a shared pure-content philosophy unit for the roadmap family. It holds one
discriminator — the rule for which surfaces are worth testing — not any
test-generation procedure or coverage pipeline. The calling skill (`roadmap-test-coverage`,
`roadmap-decompose-skeleton`) stays in control of when and how it applies the rule; this
skill has no I/O of its own. Load this skill once per chat. This is a load-once engine:
its callers depend on its exact behavior — edits here must honor their expectations as
part of its contract; the reverse graph resolves via
`` grep -l "test-philosophy" src/skills/*/SKILL.md src/commands/*.md ``.

## The Silent-Failure Discriminator

For any surface being considered for a test, ask one question:

> **"If the logic here is wrong, does the system signal it immediately (compile
> error, runtime exception, DI failure, 4xx/5xx response), or does it continue
> running and produce wrong output silently?"**

| Fails loudly → skip | Fails silently → test |
|---|---|
| Mapper with wrong field type | Aggregator with off-by-one cursor |
| Controller missing route param | State machine with wrong transition |
| DI wiring missing a provider | Dedup logic with wrong key |
| Thin adapter with no branches | Flush threshold calculated incorrectly |
| gRPC interceptor that throws | Session expiry computed from wrong timestamp |

Rule: **test only silent-failure surfaces.** Loud-failure surfaces are already caught
by the compiler/runtime/DI/HTTP layer.

## The After-the-Fact Corollary (for test triage)

When an existing test fails after a source change, the same axis classifies it:

- **Class A — API drift:** the source API changed (renamed method, new required arg,
  changed return shape) but the test was not updated. The test is outdated, not
  meaningful. Safe to patch.
- **Class B — Silent bug:** the source behavior changed in a way the test was
  designed to catch. The system would produce wrong output. The test is doing its
  job — escalate, never suppress.
