> Owner: trickster77777@gmail.com

# Skills Roadmap

> Generic AI Factory skills — reusable slash-command packages for Claude Code.

## Skills generate to today's norm, not yesterday's

### Phase 19 — the aif family stops generating what Phase 2 just cleaned out

Governing spec: `docs/sakshi-harness/sakshi-harness.md`

Phase 2's five alignment passes found the same two defects landing in every project family, always from the same source: `aif` (and its `config-template.yaml`) still generate the rules file at the orchestrator-invisible `.ai-factory/rules/base.md` instead of the canonical `.ai-factory/RULES.md`, and a `.ai-factory/config.yaml` the orchestrator never reads. Every future `/aif` run regenerates the junk this whole day was spent removing. This phase conforms the generators to the harness contract at the source.

- [x] **19.1 — aif family: stop generating retired artifacts, align to the canonical harness contract** — `aif` writes the rules file at the orchestrator-invisible `.ai-factory/rules/base.md`, not canonical `.ai-factory/RULES.md`, plus a `.ai-factory/config.yaml` (language persistence) the orchestrator never reads — rename the rules target to `RULES.md`, retire the three config-machinery files outright (verified unreferenced), and drop the config.yaml-first read in `aif-architecture`/`aif-docs` for their existing default-fallback. Guard: fixed-English invariant restated per-generator (`aif` and `aif-architecture` don't share a body) as `## Language Resolution` is removed; config-residue sweep grep-defined, verified by content. Spec: `.ai-factory/specs/trickster77777/78-aif-generates-to-norm.md`. [56m 49s]
- [ ] **19.2 — aif: grant `Bash(ln *)` for the AGENTS.md symlink step** — `aif/SKILL.md` L5 `allowed-tools` grants `Bash(mkdir *)` and (until 19.1) `Bash(node *update-config.mjs*)`, but the `## AGENTS.md Generation` section runs `ln -sfn CLAUDE.md AGENTS.md` with no `Bash(ln *)` grant — so the required AGENTS.md→CLAUDE.md symlink step raises a permission prompt interactively and can block a headless orchestrator run. Add `Bash(ln *)` to the grant list (not a broader `Bash(*)`); touch nothing in the AGENTS.md section itself. Guard: 19.1's first task also edits this same L5 (dropping the retired `update-config.mjs` grant) — independent concerns on one line, each must preserve the other. Spec: `.ai-factory/specs/trickster77777/80-aif-ln-grant-for-agents-symlink.md`.

## Test-coverage: Layer 1 should read the stack it already has, not guess it again

Phase 8's 8.1 review (all three rounds) flagged Layer 1 as having "no Python detector" — but Layer 1 already reads `.ai-factory/ARCHITECTURE.md` for module boundaries one bullet earlier, and every `ARCHITECTURE.md` `aif-architecture` generates already declares `- **Tech stack:** [language, framework]`. Growing the hard-coded manifest-sniff list per stack (Python today, the next language tomorrow) repeats a generic-skill regression instead of closing it; the fix is to consult the project's own declared stack first.

### Phase 20 — Layer 1 reads the declared stack before guessing

- [ ] **20.1 — roadmap-test-coverage: Layer 1 reads `$STACK` from ARCHITECTURE.md, manifest-sniff becomes fallback** — Layer 1 already reads `ARCHITECTURE.md` for module boundaries but never consults its own `- **Tech stack:** ...` line for `$STACK`, instead re-deriving it from a closed four-manifest list (`package.json` / `pubspec.yaml` / `go.mod` / `Cargo.toml`) with no Python entry (flagged across all three 8.1 review rounds) and no room for the next missing stack either. Reorder: `$STACK` = ARCHITECTURE.md's Tech-stack value when filled in (not the unfilled `[language, framework]` placeholder); the four-manifest sniff becomes fallback only, unextended — no new per-language detector ever again. Guard: Layers 2–8 byte-identical. Behavior-baseline: a scratch project with a filled Tech-stack line and no manifest resolves `$STACK` from it; one with no ARCHITECTURE.md but a `package.json` still falls through unchanged. Spec: `.ai-factory/specs/trickster77777/79-test-coverage-layer1-python-stack-detection.md`.

---STOP---
