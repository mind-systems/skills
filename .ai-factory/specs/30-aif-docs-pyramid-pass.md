# aif-docs: pyramid pass — second diet, dialogs and 3D carve-outs verbatim

## Current state

`src/skills/aif-docs/SKILL.md` (454 lines) already went through one diet (topic guides, HTML mechanics, consolidation → `references/`), but remains the second-heaviest top. The skill's identity is settled: everything under the resolved docs directory is **governing-spec genre** — present-tense behavior, protocols, data flows, connections, "whether the code behind it exists yet or not" (`SKILL.md:19`) — i.e. the skill is the ТЗ-writer, with README + onboarding relatives as the only genre exception. The remaining body mixes that lens (state detection A/B/C, Core Principles, state-not-process, CLAUDE.md-index targeting) with branch detail that can follow the established `references/` pattern deeper.

## Change

One pyramid pass continuing the same pattern:

- **Body keeps:** state detection, Core Principles (the governing-spec genre statement — present tense whether the code exists yet or not — and state-not-process), the CLAUDE.md `## Documentation` index contract, the key-artifact updating duty (the agent perceives the ТЗ through CLAUDE.md and the index — this stays first-class), when-to-read pointers.
- **Move to `references/`:** remaining long per-state procedures and audit checklists not already moved — each behind its branch pointer.
- **Verbatim-protected:** every `AskUserQuestion` dialog (contract text — never compressed), the Core Principles wording — above all the genre sentence (`:19`).
- **Closure rule — protection is by criterion, not enumeration:** *any* sentence stating a contract is protected verbatim whether or not listed above; a contract-bearing sentence discovered mid-pass joins the protected set on the spot — it is not a plan defect and does not require re-planning.
- **The diet must not dilute the orientation:** the skill is fully tuned to writing the ТЗ — that identity may only sharpen through this pass, never blur into generic "documentation maintenance".
- Two-reader register.

## Guards

- **Behavior-identical** — a State A/B/C run produces the same dialogs, same files, same index rows; moved text lands byte-identical.
- Frontmatter unchanged; the >references pattern already established — extend it, don't invent a second mechanism.
- Live baseline before the next phase task: a State C (update) run on a real project pre/post; compare proposed changes.

## Verification

- Body materially under 300 lines; dialogs byte-identical; every reference behind a pointer.
- Baseline State C run: identical proposal set.
