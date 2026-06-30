# test-engine: shared silent-failure testing philosophy

**Date:** 2026-06-30
**Source:** conversation context

## Key Findings

- New skill `test-engine` — holds **one philosophy**: tests exist to catch **silent** failures; surfaces that fail **loudly** do not need tests.
- Content extracted from `roadmap-test-coverage/SKILL.md`: Layer 3 (the Silent-Failure Filter — the core question + the loud/silent table). The same axis underlies Layer 7's Class A (API drift) / Class B (silent bug) classification.
- Consumers: `roadmap-test-coverage` (Layer 3 filter + Layer 7 classification) and `roadmap-decompose-skeleton` (TDD lens). Both **load test-engine** for the rule instead of inlining it.
- Pure content unit — no procedure, no I/O. Loaded for its discriminator; caller stays in control. Load-once per chat.
- **The content is lifted verbatim** from `roadmap-test-coverage`: copy the exact Layer 3 core question + loud/silent table (and the Layer 7 Class A/B definitions). The reproduction below in this note is a pointer to that source text, **not** a rewrite to follow — the source skill is authoritative.

## Details

### The content — the silent-failure discriminator

The core question, applied to any surface being considered for a test:

> "If the logic here is wrong, does the system signal it immediately (compile error, runtime exception, DI failure, 4xx/5xx response), or does it continue running and produce wrong output **silently**?"

| Fails loudly → skip | Fails silently → test |
|---|---|
| Mapper with wrong field type | Aggregator with off-by-one cursor |
| Controller missing a route param | State machine with a wrong transition |
| DI wiring missing a provider | Dedup logic with a wrong key |
| Thin adapter with no branches | Flush threshold calculated incorrectly |
| Interceptor that throws | Session expiry computed from a wrong timestamp |

Rule: **test only silent-failure surfaces.** Loud-failure surfaces are caught by the compiler/runtime/DI/HTTP layer already.

### The after-the-fact corollary (for test triage)

When an existing test fails after a source change, the same axis classifies it:
- **Class A — API drift:** the source API changed (renamed method, new required arg, changed return shape); the test is merely outdated → patch the test.
- **Class B — silent bug:** the source behavior changed in a way the test was designed to catch; the system would produce wrong output → the test is doing its job → escalate, never suppress.

### Frontmatter

```yaml
---
name: test-engine
description: >-
  Shared testing philosophy for the roadmap family. Holds one rule — write tests
  only for surfaces that fail silently (wrong output, no crash), skip surfaces that
  fail loudly (compile error, exception, DI failure, 4xx/5xx). Loaded by
  roadmap-test-coverage and roadmap-decompose-skeleton for the discriminator;
  holds no test-generation or coverage-pipeline logic.
user-invocable: false
disable-model-invocation: false
allowed-tools: Read
---
```

### Files

- Create `src/skills/test-engine/SKILL.md`.
- Register `test-engine` in `CLAUDE.md` → "Custom skills — never overwrite from upstream" and the Repository Structure tree.

### What NOT to do

- No test-generation procedure, no coverage pipeline, no agent orchestration here — that is `roadmap-test-coverage`. Keep test-engine to the discriminator and its corollary.
- Do not couple to any specific stack or test runner — the rule is stack-agnostic.
