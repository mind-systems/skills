# roadmap-test-coverage: Layer 5 testability review — substitution-friction axis, stack-parametric

Origin: a live orchestrator run this session — a Python milestone whose Layer-5 verdict came back `needs-refactor` off a testability checklist phrased in TS/NestJS idiom (`process.env`, `(req as any).user`, constructor-DI-vs-module-singleton). The executing agent hand-translated the vocabulary to Python but flagged that the underlying value ("inject, don't read from a module singleton") maps badly onto Python, where a module singleton / `os.environ` / `datetime.now()` is trivially overridable via `monkeypatch`. The misfire nonetheless surfaced a **real** finding — a class that self-acquired its config instead of receiving it — and the design goal is to keep that finding reachable without the false "untestable" framing.

## Current state

`src/skills/roadmap-test-coverage/SKILL.md` is stack-parametric everywhere except Layer 5. Layer 1 (`:37-40`) infers `$STACK` / `$TEST_CMD` across npm / pubspec / go.mod / Cargo.toml; Layer 7 runs the abstract `$TEST_CMD`; Layer 3 defers to `test-philosophy`'s language-agnostic silent-failure discriminator.

**Layer 5 — Testability Review (`:158-187`)** is a direct, un-abstracted sla of the NestJS origin. Its agent prompt template hardcodes four checks entirely in TS/NestJS idiom:
1. "Are all dependencies injected (constructor params, not module-level singletons or static imports)?" — DI-presence as the axis;
2. `process.env` reads, `Date.now()` calls, `fs` calls;
3. "unawaited promises inside observable pipes, `setTimeout` without returned handle" — RxJS/Node;
4. metadata via `(req as any).user`, `(metadata as any)[KEY]` — TS casts.

The verdict is binary on a **DI-presence** axis: `clean` or `needs-refactor | <area> | <sentence>`. On Python this axis both (a) mistranslates its examples and (b), more deeply, encodes a language-specific value — in NestJS "no DI ⇒ cannot substitute" is one axis; in Python the two axes diverge, so a `self-acquired` **and** `patchable` class (the live finding) gets judged `needs-refactor` for the wrong reason ("not DI") or, under a naive binary "patchable? → clean" reframe, would vanish entirely.

## Change

Rewrite Layer 5's agent prompt template so the axis is **graded on friction-to-substitute-in-a-test**, expressed in the stack's own testing idiom — not binary DI-presence.

**The friction gradient (the new axis):**

| How the dependency is obtained | Friction to substitute in a test | Verdict |
|---|---|---|
| Received (constructor param / function arg / injected) | none — pass a fake | `clean` |
| Self-acquired but overridable (module singleton, `os.environ`, `get_config()`, `datetime.now()`) | some — must know and patch the acquisition site | `needs-refactor`, framed as friction |
| Truly unoverridable in this stack | blocking | `needs-refactor`, strong |

- **The verdict vocabulary stays `clean | needs-refactor | <area> | <sentence>` byte-identical** — only the criteria behind it change. Layer 6 (`:191-203`) consumes the verdict unchanged: a friction flag *is* a refactor recommendation ("inject the dependency to drop test-setup friction"), and the `## Refactor Required` section it appends still describes the post-refactor API. Layers 6/7/8 untouched.
- **Middle-band framing is the point:** the `<sentence>` for a self-acquired-but-patchable finding names the *friction* and the fix ("self-acquires its config; inject it to drop test-setup friction"), never "not injected / not DI" and never "untestable" — the honest register for a language where the thing is patchable.
- **Stack-parametric examples, not hardcoded ones:** the agent is handed `$STACK` and judges friction in *that* language's test idiom (pytest `monkeypatch` / `unittest.mock.patch`, jest, etc.). The prompt teaches the gradient and that the *same* construct carries different friction per language — a module singleton is high-friction-blocking in some stacks, low-friction-patchable in Python; it gives per-stack examples as illustrations of the gradient, not as a universal checklist. The RxJS/`setTimeout` teardown check and the `(req as any)` cast check become stack-conditional (named only when `$STACK` is TS/Node), not universal lines.
- **Explicit scope boundary (must be stated in the prompt):** Layer 5 flags coupling **only to the exact degree it taxes test-setup**. A `self-acquired` dependency that is *also* near-zero-friction to substitute (a plain module function with an obvious patch site) is **not** flagged — pure design-smell "coupling for its own sake" is out of scope and belongs to a code-review lens, not a test-coverage planner. This fence is load-bearing: without it, the reframe re-admits general design review under the "testability" banner — the same contamination, inverted.

## Files & types

- `src/skills/roadmap-test-coverage/SKILL.md` — Layer 5's agent prompt template (`:158-187`) only. Frontmatter, Layers 1–4, 6–8, and the Critical Rules byte-identical. No new `loads:` edge — `test-philosophy` owns the silent-failure axis (Layer 3); this is the orthogonal testability-friction axis and stays inline in Layer 5, as it is today.

## Guards

- **Layer 6/7/8 are downstream consumers — the verdict token grammar is a contract.** `clean` / `needs-refactor | area | sentence` must survive verbatim so Layer 6's collect step and Layer 8's handoff render unchanged. Only the decision criteria and the one-sentence framing change.
- **This is not the silent-failure axis.** `test-philosophy` (Layer 3) decides *which surfaces are worth a test*; Layer 5 decides *how expensive the test is to author*. Do not fold friction into the silent-failure discriminator or vice versa — two orthogonal axes, two owners.
- **Do not translate vocabulary while keeping the DI-presence value** — that is the rejected half-fix (Python config-fetch → false `needs-refactor` "not DI"). The value judgment itself moves to friction; the examples follow the stack.
- **The scope fence is mandatory, not optional prose** — the prompt must say Layer 5 ignores coupling that carries no test-setup cost. Omitting it re-smuggles design review in.
- **`$STACK` is the parameter source** — Layer 5 receives it (Layer 1 already stores it); the agent judges friction in that stack's test idiom. No hardcoded `process.env`/`(req as any)` as universal lines.
- **Behavior-baseline** — unverified until a live Layer-5 run on the misfiring Python case reproduces the *finding* (self-acquired config → `needs-refactor`) with the friction framing, and a trivially-patchable module singleton comes back `clean`.

## Verification

- Live Layer-5 run on the Python class that misfired this session → verdict `needs-refactor`, `<sentence>` names test-setup friction and "inject" as the fix, **not** "not DI" and **not** "untestable".
- Live Layer-5 run on a Python module that reads `os.environ` / a module singleton but is trivially `monkeypatch`-able and carries no other setup cost → verdict `clean` (near-zero friction, and no design-smell escalation).
- `grep -n "process.env\|(req as any)\|(metadata as any)\|observable pipes\|Date.now" src/skills/roadmap-test-coverage/SKILL.md` → these appear only inside stack-conditional TS/Node illustrations, never as universal checklist lines.
- Diff Layers 1–4, 6–8 and Critical Rules pre/post → byte-identical; the only change is the Layer 5 prompt template.
- The scope-fence sentence (coupling flagged only where it taxes test-setup; zero-friction design-smell out of scope) is present in the Layer 5 prompt.
