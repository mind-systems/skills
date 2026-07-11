# Plan: aif-architecture: pyramid pass

## Context
Apply one pyramid pass to `src/skills/aif-architecture/SKILL.md` (236 lines): move the full ARCHITECTURE.md output template (both policy branches) behind a `references/` pointer byte-identical, confirm the decision matrix is reached only through its existing pointer, and leave the body a lean lens (step flow + the protected contracts) — behavior-identical on the same project.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Ground-truth note (read before Task 1)
The spec's "current state" lists **both** the decision matrix and the template as inline mass. Ground truth of `SKILL.md` (which overrides the description): the **scoring Decision Matrix already lives in `references/architecture.md:5`**, and the body already reaches it via pointers at `:76`, `:101` and the CRITICAL read at `:103`. There is **no inline scoring-matrix table** in `SKILL.md`. So the matrix half of the spec is already satisfied by an existing pointer; the genuinely inline mass to relocate is the **ARCHITECTURE.md output template** (`:128`–`:191`) plus its "Rules for generation" (`:193`–`:197`). The plan therefore *moves* the template and *verifies/confirms* the matrix pointer rather than re-relocating content that already lives in references.

## Constraints (apply to every task)
- **Behavior-identical.** A run on the same project must yield the same recommendation and the same generated `ARCHITECTURE.md` — same dialogs, same sections, same `## Features` anchor comment. All moved text lands **byte-identical**: same wording, headers, code fences, `[placeholder]` tokens, ✅/❌ markers.
- **Verbatim-protected, never compressed or reworded:** Step 1.5 Codebase Alignment Check procedure and its `AskUserQuestion` block; the recommendation flow's decision wording (the Step 1 `AskUserQuestion` recommendation dialog and the without-suffix variant-ask questions); both policy branches of the template (Option 2 "Legacy vs New Code Policy" and Option 1 "Code Organization Note"); the template's reserved `## Features` section including its `roadmap-prune` anchor comment; the CRITICAL `references/architecture.md` read; Step 3's CLAUDE.md `## Architecture` pointer contract.
- **Closure rule — protection is by criterion, not enumeration.** *Any* sentence stating a contract is protected verbatim whether or not named above; a contract-bearing sentence discovered mid-pass joins the protected set on the spot — not a plan defect, no re-planning.
- **Re-basing rule — the one documented exception to byte-identical.** Inside every moved block, a relative pointer is rewritten for its new base: a `references/<X>` path becomes the sibling form `<X>` once the text lives inside `references/`; a cross-reference to a step number/label that ceases to exist is re-pointed. Find occurrences by `grep`, never by enumeration; apply symmetrically; all other bytes land identical. An occurrence found mid-pass is fixed on the spot. (Note: the moved template references "Step 1.5" — that step **stays** in the body, so those references remain valid and are **not** rewritten.)
- **Frontmatter unchanged.**
- **Two-reader register.** The slimmed body must read cleanly for both the executor running the skill and a maintainer scanning its shape.
- **Body kept first-class (never moved):** Step 0 config/context load; Step 1 recommendation flow (argument resolution + the recommendation `AskUserQuestion` — this is "step flow"); Step 1.5 Alignment Check; the CRITICAL `references/architecture.md` read; Step 2's operational lead-in (create parent dir, "generate … with the following structure, adapted to the project's tech stack and language"); Step 3 CLAUDE.md pointer; Step 4 Confirm; Artifact Ownership.

## Tasks

### Phase 1: Carve the output template into a reference (byte-identical)

- [x] **Task 1: Move the ARCHITECTURE.md output template into `references/architecture-template.md`**
  Files: `src/skills/aif-architecture/references/architecture-template.md` (new), `src/skills/aif-architecture/SKILL.md`
  Create the new reference file and move into it, **byte-identical**, the Step 2 output template — the fenced `# Architecture: [Pattern Name]` markdown block (`SKILL.md:128`–`:191`, including **both** policy branches at `:161`–`:171` and the reserved `## Features` section with its `roadmap-prune` anchor comment at `:189`–`:191`) together with the "**Rules for generation:**" bullets (`:193`–`:197`). Give the file a one-line heading/intro in the same lean style as the existing `references/architecture.md` (e.g. "Output template for the generated `ARCHITECTURE.md`. Both policy branches and the reserved `## Features` section land in the file exactly as written.") so the reader knows what it is.
  Apply the **re-basing rule**: `grep` the moved block for any `references/<X>` pointer or step-number/label cross-reference; the block's only step reference is to **Step 1.5** (Option 1/Option 2 selection), which stays in the body and therefore is **not** rewritten — verify there are no other occurrences. Everything else lands byte-for-byte identical.
  Do **not** move the Step 2 operational lead-in (`:122`–`:126`, create parent dir + "generate … with the following structure") — that is step flow and stays in the body (wired to the pointer in Task 2).

### Phase 2: Slim the body, wire the pointer, keep the contracts visible

- [x] **Task 2: Rewire Step 2 to the template pointer and keep the `## Features` rule first-class** (depends on Task 1)
  Files: `src/skills/aif-architecture/SKILL.md`
  - Replace the removed template + generation-rules mass in Step 2 with a short branch pointer in the established style, e.g. "→ read `references/architecture-template.md` and generate the artifact from it, adapted to the project's tech stack and language". Keep the Step 2 lead-in (`:122`–`:126`) byte-identical.
  - **Keep the `## Features` reserved-section rule visible in the body as a first-class one-liner** (parallel to how the CLAUDE.md-index contract was lifted in the aif-docs pass): assert that the generated `ARCHITECTURE.md` MUST end with an empty `## Features` section reserved for `roadmap-prune`/`temporal-tree` anchoring. This keeps the contract asserted in the body even though the full template (with the byte-identical section) now lives in the reference.
  - **Confirm the decision-matrix pointer is intact and the matrix is not inlined anywhere:** the body must still reach the scoring matrix only via `references/architecture.md` (existing pointers at `:76`, `:101`) and retain the CRITICAL read at `:103` verbatim. If any matrix fragment turns out to be inlined in the body, move it to `references/architecture.md` byte-identical; otherwise leave the existing pointers untouched.
  - **Leave verbatim, untouched:** Step 0; Step 1 argument resolution + recommendation `AskUserQuestion` (incl. the without-suffix variant-ask questions); Step 1.5 Alignment Check + its dialog; the CRITICAL `references/architecture.md` read; Step 3 CLAUDE.md pointer contract; Step 4 Confirm; Artifact Ownership; frontmatter.
  - **Result gate:** body materially slimmer than 236 lines (template + generation rules now behind exactly one pointer); matrix and template both reachable behind pointers; every protected block byte-identical to the pre-pass file. **Live baseline before this task is considered done:** run the skill on a real project pre/post and diff the recommendation and the generated `ARCHITECTURE.md` — both diffs must be empty.
