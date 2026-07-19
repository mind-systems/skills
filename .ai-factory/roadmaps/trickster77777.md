> Owner: trickster77777@gmail.com

# Skills Roadmap

> Generic AI Factory skills — reusable slash-command packages for Claude Code.

## Skills generate to today's norm, not yesterday's

### Phase 19 — the aif family stops generating what Phase 2 just cleaned out

Governing spec: `docs/sakshi-harness/sakshi-harness.md`

Phase 2's five alignment passes found the same three defects landing in every project family, always from the same source: `aif` (and its `config-template.yaml`) still generate a contentless CLAUDE.md title+boilerplate intro, the rules file at the orchestrator-invisible `.ai-factory/rules/base.md` instead of the canonical `.ai-factory/RULES.md`, and a `.ai-factory/config.yaml` the orchestrator never reads. Every future `/aif` run regenerates the junk this whole day was spent removing. This phase conforms the generators to the harness contract at the source.

- [ ] **19.1 — aif family: stop generating retired artifacts, align to the canonical harness contract** — `aif/SKILL.md` still generates a CLAUDE.md title+boilerplate intro (unwritten default, needs an explicit prohibition), the rules file at `.ai-factory/rules/base.md` instead of canonical `.ai-factory/RULES.md`, and a `.ai-factory/config.yaml` (with its language.ui/language.artifacts persistence apparatus) the orchestrator never reads — retire `config-template.yaml`/`config-persistence.md`/`update-config.mjs` outright, verified unreferenced elsewhere; `aif-architecture`/`aif-docs` drop their config.yaml-first read for their existing default-fallback path. Guard: fixed-English-headings for generated artifacts stays, restated directly since its current home is removed. Spec: `.ai-factory/specs/trickster77777/78-aif-generates-to-norm.md`.

## Test-coverage: Layer 1 should read the stack it already has, not guess it again

Phase 8's 8.1 review (all three rounds) flagged Layer 1 as having "no Python detector" — but Layer 1 already reads `.ai-factory/ARCHITECTURE.md` for module boundaries one bullet earlier, and every `ARCHITECTURE.md` `aif-architecture` generates already declares `- **Tech stack:** [language, framework]`. Growing the hard-coded manifest-sniff list per stack (Python today, the next language tomorrow) repeats a generic-skill regression instead of closing it; the fix is to consult the project's own declared stack first.

### Phase 20 — Layer 1 reads the declared stack before guessing

- [ ] **20.1 — roadmap-test-coverage: Layer 1 reads `$STACK` from ARCHITECTURE.md, manifest-sniff becomes fallback** — Layer 1 already reads `ARCHITECTURE.md` for module boundaries but never consults its own `- **Tech stack:** ...` line for `$STACK`, instead re-deriving it from a closed four-manifest list (`package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`) with no Python entry (flagged across all three 8.1 review rounds) and no room for the next missing stack either. Reorder: `$STACK` = ARCHITECTURE.md's Tech-stack value when filled in (not the unfilled `[language, framework]` placeholder); the four-manifest sniff becomes fallback only, unextended — no new per-language detector ever again. Guard: Layers 2–8 byte-identical. Behavior-baseline: a scratch project with a filled Tech-stack line and no manifest resolves `$STACK` from it; one with no ARCHITECTURE.md but a `package.json` still falls through unchanged. Spec: `.ai-factory/specs/trickster77777/79-test-coverage-layer1-python-stack-detection.md`.

---STOP---
