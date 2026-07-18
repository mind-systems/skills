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

One criterion governs the whole table: **does the API offer a parameter for the thing
a test must vary?** "Zero friction" means there is nothing to substitute (static
reference data) or the value arrives as an argument — never "the patch is easy": a
cheap `monkeypatch` is still friction, because the test author must know the
acquisition site and patch it instead of passing a value.

| How the dependency is obtained | Friction to substitute in a test | Verdict |
|---|---|---|
| Received (constructor param / function arg / injected); module-level names touched only as static reference data | none — pass a value | `clean` |
| Varying data or a collaborator the API offers no parameter for — acquired at construction or reached inside the call; the only way to vary it is to patch the acquisition site, however cheap the patch (stack illustrations: module singleton, `os.environ`, `get_config()`, `datetime.now()`) | some — know and patch the acquisition site | `needs-refactor`, framed as friction |
| Truly unoverridable in this stack | blocking | `needs-refactor`, strong |

Whether the acquisition can *fail* is irrelevant to the band — a defensive `.exists()`
guard returning a default keeps construction from crashing but adds no parameter, so
it still flags.

**Not every reached function is a collaborator.** A helper whose behavior is fully
determined by the parameters the caller passes it is not a substitution point — the
test already controls it by controlling those parameters, so calling it directly is
free. A reached function counts as a collaborator only when it supplies varying data
or an effect the test must control and the API offers no parameter for it. This is
what separates `_load_csv(filepath)` — the path is the caller's own parameter, so a
test steers it by passing a temp path — from `search(query, domain, …)` reached inside
`DesignSystemGenerator`, where nothing in the class's API supplies the corpus it
searches.

- **The verdict vocabulary stays `clean | needs-refactor | <area> | <sentence>` byte-identical** — only the criteria behind it change. Layer 6 (`:191-203`) consumes the verdict unchanged: a friction flag *is* a refactor recommendation ("inject the dependency to drop test-setup friction"), and the `## Refactor Required` section it appends still describes the post-refactor API. Layers 6/7/8 untouched.
- **Middle-band framing is the point:** the `<sentence>` for a self-acquired-but-patchable finding names the *friction* and the fix ("self-acquires its config; inject it to drop test-setup friction"), never "not injected / not DI" and never "untestable" — the honest register for a language where the thing is patchable.
- **Stack-parametric examples, not hardcoded ones:** the agent is handed `$STACK` and judges friction in *that* language's test idiom (pytest `monkeypatch` / `unittest.mock.patch`, jest, etc.). The prompt teaches the criterion and gives per-stack construct names only as illustrations of it, never as a universal checklist. The stack's patchability sets the `<sentence>` register — friction to drop, never "untestable" — not the verdict: a patchable acquisition of varying data still flags. The RxJS/`setTimeout` teardown check and the `(req as any)` cast check become stack-conditional (named only when `$STACK` is TS/Node), not universal lines.
- **Explicit scope boundary (must be stated in the prompt):** Layer 5 flags coupling **only to the exact degree it taxes test-setup**. Code that receives its varying inputs as arguments and touches module-level names only as static reference data is **not** flagged, whatever those names are — pure design-smell "coupling for its own sake" is out of scope and belongs to a code-review lens, not a test-coverage planner. The fence clears *nothing-to-substitute* cases; it never clears a patchable acquisition of varying data — "the patch is easy" is not the fence. This fence is load-bearing: without it, the reframe re-admits general design review under the "testability" banner — the same contamination, inverted.

## Files & types

- `src/skills/roadmap-test-coverage/SKILL.md` — Layer 5's section (`:158-187`) only: the fenced agent prompt template plus the orchestrator line that binds `$STACK` to the prompt's `<stack>` placeholder. Frontmatter, Layers 1–4, 6–8, and the Critical Rules byte-identical. No new `loads:` edge — `test-philosophy` owns the silent-failure axis (Layer 3); this is the orthogonal testability-friction axis and stays inline in Layer 5, as it is today.

## Guards

- **Layer 6/7/8 are downstream consumers — the verdict token grammar is a contract.** `clean` / `needs-refactor | area | sentence` must survive verbatim so Layer 6's collect step and Layer 8's handoff render unchanged. Only the decision criteria and the one-sentence framing change.
- **This is not the silent-failure axis.** `test-philosophy` (Layer 3) decides *which surfaces are worth a test*; Layer 5 decides *how expensive the test is to author*. Do not fold friction into the silent-failure discriminator or vice versa — two orthogonal axes, two owners.
- **Do not translate vocabulary while keeping the DI-presence value** — that is the rejected half-fix (Python config-fetch → false `needs-refactor` "not DI"). The value judgment itself moves to friction; the examples follow the stack.
- **The scope fence is mandatory, not optional prose** — the prompt must say Layer 5 ignores coupling that carries no test-setup cost. Omitting it re-smuggles design review in.
- **`$STACK` is the parameter source** — Layer 5 receives it (Layer 1 already stores it), and the Layer 5 orchestrator line must name the substitution into the prompt's `<stack>` placeholder — an unbound placeholder degrades silently (the agent judges friction with no stack while still returning a well-formed verdict line). No hardcoded `process.env`/`(req as any)` as universal lines.
- **Behavior-baseline** — unverified until a live Layer-5 run on the three pinned fixtures in Verification reproduces both bands: the class with no parameter for the data it branches on → `needs-refactor` with the friction framing; the function that *takes arguments* yet still has no parameter for the corpus it searches → `needs-refactor` (taking arguments is not the criterion); and the function that receives its corpus path as a parameter → `clean`. Two of the three flag: the set is chosen so that no surface heuristic (module singleton? touches disk? guards with `.exists()`? takes arguments?) separates them and only the parameter criterion does.

## Verification

The origin misfire file lives in the live orchestrator run's project and is named
nowhere — it is unavailable in this repo. The baseline runs on three pinned in-repo
fixtures that reproduce the bands; the origin defect itself is not re-run, and the
report must say so. All three read a CSV whose *contents* drive the result and all
three fail quiet on missing data (`.exists()` guards returning a default), so no
surface heuristic separates them — a replay agent may misread the defensive
acquisition as low-friction, but the verdict turns on the parameter criterion, not on
whether acquisition throws.

- Live Layer-5 run (Stack: Python/pytest) on `src/skills/ui-ux-pro-max/scripts/design_system.py`, area `class DesignSystemGenerator` (`:37`): `__init__` (`:40`) takes no parameters, and the reasoning data its logic branches on (`_find_reasoning_rule`, `:64-86`) is loaded from `DATA_DIR / REASONING_FILE` with no parameter to supply it → verdict `needs-refactor`, `<sentence>` names test-setup friction and "inject" as the fix, **not** "not DI" and **not** "untestable".
- Live Layer-5 run (Stack: Python/pytest) on `src/skills/ui-ux-pro-max/scripts/core.py`, area `search()` (`:212`): `query` / `domain` / `max_results` arrive by argument and `CSV_CONFIG` (`:17`) is a static lookup table — but it resolves only a *filename*; the rows the behavior varies on sit behind `DATA_DIR / config["file"]` (`:218`) with no parameter to supply them, and the `.exists()` error-dict guard (`:220-221`) adds no parameter → verdict `needs-refactor`, same framing as above. This is the load-bearing case: a function that takes arguments and must still flag, which is what forecloses the "it takes arguments → `clean`" reframe. `search_stack()` (`:234`) is the same band and is dropped from the set as non-discriminating.
- Live Layer-5 run (Stack: Python/pytest) on `src/skills/ui-ux-pro-max/scripts/core.py`, area `_search_csv()` (`:165`): it opens a file (`:170`, via `_load_csv` `:159`) and carries its own `.exists()` guard (`:167-168`) — the same surface features as the two flagged cases — but `filepath`, `search_cols`, `output_cols`, `query` and `max_results` **all** arrive as parameters, so a test passes a temp CSV path and patches nothing → verdict `clean`. The `clean` rests on the parameter criterion, never on "touches no disk" and never on "the patch would be easy". This case also exercises the helper-vs-collaborator clause: `_search_csv` reaches the module-level `_load_csv` (`:159`), which is a helper — its path is the caller's own parameter — not a collaborator the test must control.
- `grep -n "process.env\|(req as any)\|(metadata as any)\|observable pipes\|Date.now" src/skills/roadmap-test-coverage/SKILL.md` → these appear only inside stack-conditional TS/Node illustrations, never as universal checklist lines.
- Diff Layers 1–4, 6–8 and Critical Rules pre/post → byte-identical; the only changes are the Layer 5 prompt template and the one orchestrator line binding `$STACK` to `<stack>`.
- The scope-fence sentence (coupling flagged only where it taxes test-setup; arguments-over-static-data is `clean`; zero-friction design-smell out of scope) is present in the Layer 5 prompt.
