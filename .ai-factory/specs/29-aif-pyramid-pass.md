# aif: pyramid pass — progressive disclosure into `references/`, config machinery verbatim

## Current state

`src/skills/aif/SKILL.md` (496 lines) is the package's heaviest top. Its fork already cut the marketplace half and made CLAUDE.md the first artifact, but the body still carries everything inline: three modes, stack analysis, the config.yaml machinery, MCP setup, `rules/base.md` generation. The `aif-docs` diet set the repo's pattern for exactly this shape: rare branches move to `references/`, the body keeps rule + when-to-read pointer.

## Change

One pyramid pass using the established `references/` pattern:

- **Body keeps (the lens):** the three-mode skeleton and mode detection, CLAUDE.md-first ordering, the language-resolution rule, the final `/aif-architecture` call, and per-topic one-line pointers to references.
- **Move to `references/`:** per-stack analysis detail, MCP catalog/setup mechanics, the `rules/base.md` template content, any long generation templates — each read only on the branch that needs it.
- **Verbatim-protected:** the config.yaml machinery (`update-config.mjs` + template — explicitly verbatim per the fork's own contract), the CLAUDE.md update-not-clobber rule, mode-detection wording.
- Two-reader register.

## Guards

- **Behavior-identical** — every mode produces the same artifacts with the same content; moved text lands byte-identical in `references/` (progressive disclosure, not rewriting).
- Frontmatter unchanged; the reconcile-by-diff relationship with `upstream/ai-factory/aif` noted in CLAUDE.md stays meaningful — moved content must remain diffable (note the mapping in the spec-note of the move, not in the skill body).
- Live baseline before the next phase task: run `/aif` in a scratch project pre/post and diff the generated CLAUDE.md / config.yaml / rules artifacts.

## Verification

- Body materially under 300 lines; each reference file reachable from a when-to-read pointer.
- Baseline diff of generated artifacts → empty.
