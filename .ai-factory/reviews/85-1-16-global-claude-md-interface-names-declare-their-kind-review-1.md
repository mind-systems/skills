# Review: 1.16 — global CLAUDE.md: interface names declare their kind

## Scope
Single-file change: `src/global/CLAUDE.md`, one bullet appended to § "Planning workflow".

## Verification against spec (`.ai-factory/specs/40-global-interface-names-declare-kind.md`)

- **Verbatim text** — the added bullet matches the spec's contract text character-for-character, including em-dashes, backtick-wrapped markers, and the closing "that form is mandatory." sentence. No rewording. ✓
- **Placement** — appended as the new last item in § "Planning workflow" (line 56), after the "Deferred questions mean unfinished planning." bullet. Planning workflow is the final section; no later section is displaced. ✓
- **Additions only / byte-identical** — `git diff HEAD` shows a single added line (`@@ -53,3 +53,4 @@`); no existing line removed or altered. ✓
- **One home / no skill edits** — no skill body, no project `RULES.md` touched. The global file already loads into every planning tier's session, so the rule reaches decompose/skeleton/architect/orchestrator without any skill edit. ✓
- **Nothing project-specific** — the `IPLRService`/tradeoxy examples are absent from the bullet; the language stays generic (`I` prefix / `Protocol` suffix / language convention). ✓
- **grep guard** — `grep -n "declare their kind" src/global/CLAUDE.md` returns exactly one hit, inside § "Planning workflow". ✓

## Runtime / correctness considerations
This is a Markdown instruction file, not executable code — no migrations, types, or race conditions apply. Markdown syntax of the bullet is well-formed and consistent with neighboring bullets (`- **Title.** …`).

No findings.

REVIEW_PASS
