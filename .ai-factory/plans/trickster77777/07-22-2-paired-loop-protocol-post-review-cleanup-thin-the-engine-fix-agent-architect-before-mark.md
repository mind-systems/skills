# Plan: 22.2 — paired-loop protocol post-review cleanup: thin the engine, fix `agent-architect` before-mark

## Context
Fold two post-review residues from 22.1 into one cleanup: slim `architect-editor-engine/SKILL.md` to a thin `.h`-style shell with no `::` mention, and fix three before-mark/enrich/token defects in `agent-architect/SKILL.md`. `editor.md` stays untouched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Part A — thin the engine

- [x] **Task 1: Rewrite `architect-editor-engine` frontmatter description**
  Files: `src/skills/architect-editor-engine/SKILL.md`
  Replace the `description:` block (L3–10) with the target text given verbatim in the spec (§ Part A → "The change", the ```yaml``` block): drop the `::`-grammar sentence, keep "Holds only the two formats; when-to-use policy stays with the caller." Leave every other frontmatter field byte-identical — `user-invocable: false`, `disable-model-invocation: false`, `allowed-tools: Read`, no `loads:`.

- [x] **Task 2: Replace the engine body with the ~20-line shell** (depends on Task 1)
  Files: `src/skills/architect-editor-engine/SKILL.md`
  Replace the whole body (L16–62) with the target markdown block given verbatim in the spec (§ Part A → "The change", the ```markdown``` block). Net effect per spec: cut the restated intro framing (keep only the load-once/reverse-graph sentence); shrink the two format bullets to one-line definitions each (drop the `APPLY-EDIT` mechanics restatement and the "Used for…" notes); remove `## What this engine does not hold` outright; keep the mode rule's keying/ambiguity content and add the closing sentence pointing full mechanics at the callers — without naming `::`. Preserve the engine's existing register — a trim, not a re-voicing.
  Verify: `grep -n "::"` → 0 hits; `grep -niE "collision|self-verify|do not commit"` → 0 hits; `grep -n "## What this engine does not hold"` → 0 hits; body ≤ ~22 lines.

### Phase 2: Part B — fix `agent-architect` before-mark

- [x] **Task 3: Gate enrich on an explicit after-mark instruction**
  Files: `src/skills/agent-architect/SKILL.md`
  Rewrite L76–84 and the related L91–95 framing so enrichment happens **only** when the after-mark remainder is itself an explicit instruction to enrich — the `<before-mark> :: <"enrich this for the editor with X">` pattern where the user names the context `X`. When the after-mark is anything else (plain clarifying answer, empty, or absent because the marker trailed), the before-mark payload relays as-is, unenriched — no architect-initiated enrichment on its own judgment. Trim: keep only that enrichment adds the user-named context and never a finding/verdict/method; drop the "supplying named context and injecting a conclusion are different acts" sentence as redundant once the trigger is external. Remove the bare "you **may** enrich" discretion phrasing.
  Verify: `grep -n "you may enrich"` → 0 hits; the enrich text names the after-mark-instruction trigger (e.g. contains `"enrich this for the editor"` or equivalent explicit-instruction phrasing) as the sole gate.

- [x] **Task 4: Fold the reconcile mechanic into the general before-mark rule** (depends on Task 3)
  Files: `src/skills/agent-architect/SKILL.md`
  Insert into the general before-mark paragraph (after "you perform your own part, never a mere pass-through," ~L75–76): the architect reaches its own independent read of the before-mark payload, then — once the editor's report returns — reconciles (concede where the editor's catch is sharper and say why, hold where the principle says so and say why) and shows the user both its own read and a summary of the editor's. This applies to **every** before-mark relay. Then shrink `## Review in parallel...` (L133–146) to state only the review-specific flavor on top of the now-general mechanic: be adversarial, name the specific plantable failure rather than a vague caution, hunt propagation gaps — referencing the general rule by name instead of restating "run your own review concurrently... reaching your own verdict independently" and the reconcile/concede-hold/show-user steps a second time. This is a structural fold, not a bolted-on cross-reference. Preserve register.
  Verify: the general before-mark span contains the reconcile/concede-hold/show-user mechanic; `## Review in parallel...` no longer restates the concurrent-review/independent-verdict or concede/hold/show-user steps.

- [x] **Task 5: Show the literal `REPORT-ONLY` token in the skill-expansion example** (depends on Task 4)
  Files: `src/skills/agent-architect/SKILL.md`
  Rewrite L97–101's quoted worked example so it literally opens with the token, e.g. `"REPORT-ONLY — read and run `~/.claude/skills/<name>/SKILL.md` with arguments: … as a report; write no files"` — consistent with the byte-exact-token rule Part A's engine states.
  Verify: `grep -n 'REPORT-ONLY — read and run'` (or equivalent) → the example opens with the literal token.

### Phase 3: Whole-task guards

- [x] **Task 6: Confirm out-of-scope files untouched** (depends on Task 2, Task 5)
  Files: (verification only)
  Confirm `src/agents/editor.md` is byte-identical to its pre-task state (`git diff` shows no changes to it), and that `reserved-words.md`, root `CLAUDE.md`, and `docs/` are untouched. In `agent-architect/SKILL.md`, everything outside `## Relay on the marker...` and `## Review in parallel...` stays byte-identical (spawn-once discipline, apply-work-order authoring paragraph L111–117, "Verify the editor's report by fact", the buffer section, and the closing sections).
