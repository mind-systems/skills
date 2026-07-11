# Plan: 1.7 — roadmap-test-coverage: pyramid pass

## Context
Compress `src/skills/roadmap-test-coverage/SKILL.md` (328 lines) by cutting inter-layer ceremony, duplicated rationale, and any inline restatement of the silent-failure discriminator that the loaded `test-philosophy` engine owns — while landing the 8-layer algorithm and every layer contract byte-identical. A compression, not a redesign: behavior-identical (same layers, same order, same outputs, same handoff-list format).

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Phase 1: Compress roadmap-test-coverage to a lens over its algorithm

- [x] **Task 1: Pin the verbatim-protected inventory + cut list**
  Files: (read-only) `src/skills/roadmap-test-coverage/SKILL.md`, `.ai-factory/specs/27-roadmap-test-coverage-pyramid-pass.md`, `src/skills/test-philosophy/SKILL.md`
  Do not edit yet — this is preparatory reading with **no diff**; Task 1 and Task 2 run in one implement session, and the checklist is fully re-derivable from SKILL.md + spec 27 + the engine (all readable at Task 2 time). An empty diff here is expected, not a stale/no-op implementation. Read the current skill, the spec, and `test-philosophy`, and record as an in-session checklist for Task 2 — the contract Task 2 must not break. Two lists:
  - **Verbatim-protected (must land byte-identical):**
    (1) the **8-layer pipeline structure** — the eight layer headers (Layer 1 … Layer 8), in order, and each layer's contract: the agents each layer spawns (`Explore` in Layer 4, `general-purpose` in Layers 5 and 7), which layers run parallel-in-a-single-message, and each layer's hand-off to the next;
    (2) the **agent prompt templates** copied through untouched — Layer 4's deep-research prompt and its embedded note document skeleton (`# <Area Name> — Test Plan` through `saved: …`), Layer 5's testability-review prompt and its `clean | … / needs-refactor | …` return format, Layer 7's classification prompt including the **Class A / Class B classification table** (`| Test (describe > it) | Source file | Class | Reason | Action |`) and the Class A (API drift) / Class B (silent bug) definitions;
    (3) the **Layer 6 and Layer 8 handoff-list mechanics** — the two-tier handoff decision in full: Layer 6's `$HANDOFF_LIST` append (area + one-sentence refactor + Layer-4 note pointer) plus the `## Refactor Required` note-append; Layer 7's Class-A patch action (assertions intact, only update the call signature) and Class-B `$HANDOFF_LIST` append with the **source-file fallback-pointer** paragraph (a Class B failure can belong to an area with no Layer-4 note — dropped in Layer 2 or 3 — so the source-file column is the fallback pointer); Layer 8's `Handoff — paste into /roadmap-decompose` block and its per-item pointer rule ("attach the Layer-4 note path when the area was researched … otherwise print the source file path … none are left blank");
    (4) **Critical Rule 1's precise wording** — "**Never write new test files** — research and planning only. The one allowed exception: Layer 7 patching an existing Class-A (API-drift) failure … Keep assertions intact — only update the call signature." word-for-word; and the rest of the Critical Rules list (Rules 2–6) preserved;
    (5) **Layer 7's inline Class A/B classification is protected, NOT a cut site** — it is deliberately inlined in the isolated agent's prompt because that agent does not load `test-philosophy` (the After-the-Fact Corollary). Copy it through untouched. The one-sentence pointer that names the corollary ("The Class A / Class B split below applies `test-philosophy`'s After-the-Fact Corollary — the agent runs in isolation and does not load the skill, so the classification stays inline in its prompt.") is the load-pointer rationale and stays.
  - **Cut candidates (ceremony / restated discriminator):**
    - Any **inline restatement of the silent-failure discriminator** — the `fails silently` / `fails loudly` definition that `test-philosophy` owns. Layer 3 must only **load and apply** the engine's discriminator (via the `Skill` tool), never restate its definition inline. The kept-vs-dropped presentation block in Layer 3 (`[Kept — fails silently] / [Dropped — fails loudly]`) is output-format labeling the user sees, not a restatement of the rule's definition — keep the labels but ensure no sentence re-defines what "fails silently/loudly" *means* beyond the load pointer. (Verification grep in Task 3 pins this.)
    - **Transitional prose between layers** — connective narration ("Proceed to Layer 5.", "This is the most important gate in the pipeline. It prevents Layer 4 from wasting agent capacity …" and similar rationale glosses) where the layer sequence already carries the flow. Trim rationale that merely re-explains why a layer exists; keep any sentence that states a contract an executor would otherwise get wrong.
    - **Duplicated rationale** — the same justification stated in both a layer body and the Critical Rules, or restated across layers. Keep one home.
  - Frontmatter (`name`, `description`, `argument-hint`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `loads: test-philosophy`) is **unchanged** — the spec pins `loads: test-philosophy` and frontmatter unchanged.

- [x] **Task 2: Compress the file** (depends on Task 1)
  Files: `src/skills/roadmap-test-coverage/SKILL.md`
  Rewrite for compression, not redesign — the 8-layer structure (Layer 1 … Layer 8 → Critical Rules) and every routing/classification/handoff decision stay identical; only ceremony and restated discriminator shrink. Requirements:
  - **Land every verbatim-protected block from Task 1 byte-identical.** Do not paraphrase, re-order clauses within, or "improve" a protected block — copy it through untouched. This especially covers the eight layer contracts, all three agent prompt templates, the Layer 7 Class A/B table, the Layer 6/8 handoff-list mechanics, and Critical Rule 1.
  - **Cut the inline discriminator restatement:** Layer 3 loads `test-philosophy` and applies its discriminator by reference — never restate the `fails silently` / `fails loudly` definition inline beyond the load pointer. Follow the composition rule: a top loads the engine, never inlines its content (`.ai-factory/ARCHITECTURE.md` → "Composition: mechanism vs policy").
  - **Cut inter-layer ceremony and duplicated rationale:** collapse transitional narration between layers and remove rationale that re-explains a layer's purpose without stating a contract. Keep the Layer 3 kept/dropped presentation labels and every layer's operative instructions.
  - **Two-reader register throughout:** rules stated as intent for the executing orchestrator; contracts (agent prompts, tables, handoff formats) pinned exact for the editor. (Spec: "Two-reader register.")
  - **Frontmatter unchanged:** `loads: test-philosophy` and all other frontmatter fields byte-identical.
  - Write in English.

- [x] **Task 3: Verify against guards** (depends on Task 2)
  Files: (read-only) `src/skills/roadmap-test-coverage/SKILL.md`
  Confirm each spec guard before declaring done:
  - **8 layers intact and ordered:** `git diff src/skills/roadmap-test-coverage/SKILL.md` shows Layers 1–8 all present, in order, with each layer's agents/hand-offs/outputs unchanged. Removed hunks are ceremony / discriminator-restatement only — report any layer-contract edit as a failure.
  - **Protected blocks byte-identical:** the three agent prompt templates, the Layer 7 Class A/B table, the Layer 6/8 handoff-list mechanics (including the Class-B source-file fallback-pointer paragraph and Layer 8's per-item pointer rule), and Critical Rule 1's wording each survive verbatim. Spot-check the decisive lines: "**Never write new test files**", the `| Test (describe > it) | Source file | Class | Reason | Action |` header, "Keep assertions intact — only update the call signature.", and "none are left blank."
  - **Discriminator not restated inline:** run `grep -n "fails silently\|fails loudly" src/skills/roadmap-test-coverage/SKILL.md` — the only surviving occurrences are the Layer 3 kept/dropped presentation labels (output format), not a definition of the rule. No sentence re-defines the discriminator beyond the load pointer; the Layer 7 After-the-Fact Corollary inline classification is intact (it is protected, not a restatement).
  - **Frontmatter intact:** `loads: test-philosophy`, `allowed-tools`, `argument-hint`, `description`, and the invocation flags all unchanged.
  - **Every behavior preserved:** same layers, same order, same outputs, same handoff-list format — Layer 2's coverage classification, Layer 3's filter + user confirmation prompt, Layer 4/5 parallel-agent one-line-return contract, Layer 6 collect, Layer 7 run/classify/patch/re-run, Layer 8 handoff print, and Critical Rules 1–6 all still present and unchanged in behavior.
  - **Line count:** report actual; meaningful ceremony shrinkage expected, but the 8-layer algorithm and its agent prompts are legal mass — do not pad or clamp to a line number.
  - Note for the reviewer: the spec's live baseline (run Layers 1–3, the analysis tier, on a real project pre/post and compare the produced classification) requires a real target project and is **user-run**, not orchestrator-fabricated. Flag it as user-run; do not invent a baseline.
