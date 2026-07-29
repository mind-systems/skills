# Handoff — the plan-citation rule and the prune scan are both narrower than the leak they were built for

Cross-repo handoff from the orchestrator side (`orchestrator/`), 2026-07-29. Answers a question the skills side left open since 2026-07-12, and reports that the fix already in place — home rule plus prune scan — misses the shape the leak actually takes. Nothing was edited on either side; this is diagnosis plus a recommendation for the skills side to decide, since it owns the home.

## 1. The reachability question is answered — YES

`orchestrator/.ai-factory/handoffs/05-code-cites-plan-layer-orchestrator-side.md` §4 asked whether the orchestrator's agents run under `~/.claude/CLAUDE.md`, and made the whole single-homing decision conditional on the answer. It has sat open since 2026-07-12. It is now settled by a live trace, not by inspection of code alone.

`~/.claude/CLAUDE.md` is a symlink to `skills/active/CLAUDE.md`, which is itself a symlink to `skills/src/global/CLAUDE.md` — `readlink -f ~/.claude/CLAUDE.md` resolves the whole two-hop chain to that one file. So the authoritative home is the exact file every agent loads — there is no second copy to keep in sync, only the question of whether the loading actually happens for a headless, non-interactive invocation.

`orchestrator/orchestrator/agents.py`, function `_run_claude` (~:172–212), builds the CLI command with `--system-prompt` — a full replacement of the default system prompt — and only does so when there is no session to resume (~:203–206); on `--resume` no system prompt is passed at all. `cwd` is set to the target project directory (~:212), never to the orchestrator repo itself.

The open question was whether `--system-prompt` suppresses the CLI's normal implicit loading of the user-global `CLAUDE.md`. It was probed twice with that exact flag shape: once from inside this family's own `orchestrator/` — the weaker run, since that repo's own project `CLAUDE.md` is also in play there — and once from `mind/mind_mcp`, a project with no relation to this family at all, which is the run that rules out any project-local explanation. Both used:

```
claude -p "Reproduce verbatim the bullet in your context that begins with the words 'Comments never cite'. If no such text is present in your context, reply exactly: NONE" --model claude-haiku-4-5-20251001 --system-prompt "You are a helpful assistant."
```

Both runs returned the bullet verbatim.

**Conclusion:** `--system-prompt` does not suppress the user-global `CLAUDE.md`, and the channel is cwd-independent. The global rule reaches all four orchestrator actors — planner, test-planner, implementer, reviewer — in every target project, regardless of which project the orchestrator is currently driving. A pointer to the home is therefore technically viable; restating the rule inside a prompt is a choice the orchestrator side made, not a necessity the runtime forced on it.

This corrects one thing stated on the orchestrator side. `orchestrator/.ai-factory/handoffs/08-plan-layer-citations-recur-in-docstrings.md` §2's claim that "three of four actors are never told" is false as stated — all four are told, because all four load the home file whether or not any prompt restates the rule. What is true is narrower and worse: all four are told, in the same wording, and that wording is the thing that fails.

## 2. The home's wording is the single point of failure

`skills/src/global/CLAUDE.md:18` reads: **"Comments never cite the plan layer. No code or test comment carries a phase/note number, a `ROADMAP`/`Plan` reference, or an `.ai-factory/` path."**

Two gaps live in that one line, and because it is the home every actor loads, both gaps propagate to every actor at once — widening a downstream prompt cannot close either of them.

**Construct.** It says "comment". Every violation Herald's prune scan surfaced (per handoff 08 §1) is a Python module docstring — not a comment, and not a construct the rule names. The word `docstring` appears in none of the four orchestrator prompt files either, so no downstream copy narrows the gap.

**Shape.** The four listed shapes — `Phase N`, note number, `ROADMAP`/`Plan`, `.ai-factory/` path — are not the shape that actually leaks in this repo's own code. `orchestrator/tests/` carries 45 section comments of the form `# Task N:` — `test_agents.py` 18, `test_main.py` 13, `test_roadmap.py` 7, `test_runtime.py` 5, `test_notify.py` 2 — against zero occurrences of that form in `orchestrator/*.py`. (The `# Step 1: Plan` / `# Step 1.5: Iterative plan review` / `# Step 2-3: Implement → Verify loop` / `# Step 4: Mark done + commit` comments in `main.py` at lines 262, 280, 315, 355 name real pipeline steps in the code's own domain and are legitimate — they are not plan citations and should not be confused with the hazard.) `Task N` is in neither the home rule's shape list nor the prune scan's grep set, so nothing currently looks for the form that dominates in practice.

**One of those 45 is the predicted hazard, already live, not hypothetical.** `orchestrator/tests/test_agents.py:260` reads `# Task 5: RED case -- semver ordering (fixed in task 2.2)`. `2.2` is a roadmap coordinate — commit `693a6a5`, "2.2 — Isolate nvm version ordering into a pure semver-aware helper and fix the pick". The active roadmap, `orchestrator/.ai-factory/roadmaps/trickster77777.md`, now opens at `### Phase 3` (line 11) — phase 2 is already pruned. The citation dangles today, and turns into a *false* resolution the moment the prune's number reuse hands `2` to some later, unrelated direction — exactly the hazard handoff 05 §7 named, now concretely instantiated rather than a class-level worry.

A second-order symptom sits directly beneath it: the docstring immediately under that comment (`test_agents.py:265–268`) still reads *"...this assertion encodes the correct behavior and is expected to fail until the sort is semver-aware"* — but `2.2` already fixed the sort. The file is narrating the plan's timeline instead of describing current behavior, and it now actively misstates what the code does. This is the same failure class the rule is meant to prevent, compounding: not only does the comment cite a coordinate that will dangle or falsely resolve, the prose next to it has gone stale because it was written as a plan-relative claim ("expected to fail until...") instead of a fact about the code today.

## 3. Why it leaks into tests and not into production code

This is a mechanism, not a compliance failure, and worth stating as one rather than re-litigating "the model ignored the rule." A production file's structure comes from its own domain — a section comment in `main.py` names a pipeline step that exists in the code, so there is nothing from the plan layer left to cite. A generated test file has no comparable intrinsic structure: the implementer writes it by walking the plan's numbered task list, and labels each section with the coordinate it is currently walking — the plan's structure becomes the file's table of contents, because nothing else supplies one. The citation is the file's skeleton, not a stray reference bolted on. The same pressure produces the module docstring found on the Herald side: for a generated test file, the honest answer to "what does this file cover" lives in the spec that specified it, so the implementer reaches for that spec by name. A rule aimed at "comments" carrying "`Phase N`" has close to zero purchase on exactly the place where plan structure and file structure coincide — which is precisely where all the observed violations, on both sides of this pair of repos, actually occurred.

## 4. The prune scan works, and should be widened and pointed at the backlog

Credit where due, stated plainly: `roadmap-prune`'s Step 7.5 citation scan is the piece of the coordinated fix that did its job. It fired during Herald's full prune and surfaced three live citations at exactly the arming moment handoff 05 §3 designed it for. Nothing in this handoff argues against the scan or its placement — the ask is narrower reach, not a redesign.

The orchestrator-side evidence shows the scan currently sees less than what leaks, so the ask is that the skills side re-examine it:

- Widen its grep set to the shapes actually found in practice — `Task N` and `task N.M` alongside the existing `Phase N`, note number, `ROADMAP`/`Plan`, `.ai-factory/` path — and keep that set identical to whatever shape list the home rule ends up carrying, so the writer's rule and the scanner's net never diverge from each other again.
- Widen the construct it inspects beyond comments to docstrings and module headers, matching whatever the home rule's construct list ends up saying.
- Consider whether the scan should sweep the whole repository, not only the surface of the task currently being pruned, so citations accumulated before the rule existed converge toward zero over time rather than only new ones being caught going forward. The orchestrator side's stated goal is that code converges to zero references into the plan layer — not merely that the rate of new references drops to zero.
- Keep the boundary directional when widening either list: the plan layer citing itself remains legitimate — a spec referencing another spec, a contract line's `Spec:` tag. A wider construct or shape list must not read as a ban on phase numbers appearing inside `.ai-factory/` itself.

## 5. What the skills side is being asked to decide

The wording fix belongs in the home, because the home is the one file every actor actually reaches — fixing only the orchestrator's restated copy in `implementer.md` would leave the source weaker than its own downstream copy, which inverts "one fact, one home" rather than upholding it.

Worth stating for the record, since it changes what "keep single-homing" is actually asking to preserve: single-homing was never achieved even once. Commit `8753c43` (orchestrator repo, 2026-07-12) planted a fully restated rule in `orchestrator/prompts/implementer.md` at two sites (~:108 and ~:128), with no pointer to the home anywhere in the file. The copy has already diverged from its source: `implementer.md:108` adds an escape hatch — *"link a file under `docs/` (the only reference target allowed in code)"* — that `skills/src/global/CLAUDE.md:18` does not carry at all. Handoff 05 §10 required a pointer, never a restated copy; that requirement has not held for a single day since it was written.

The open decision, now that a pointer is proven reachable rather than merely proposed, is what "one home" should mean going forward — a literal pointer line in every consuming prompt, or a single wording edited in one place and deliberately copied outward whenever it changes, with the four downstream copies audited against the source rather than left to drift independently. That decision belongs to the skills side, since it owns the home. The orchestrator side's own reviewer gate (giving `reviewer.md` an explicit check instead of relying on its general cosmetics clause) is a separate, local matter for that repo and is not part of this ask.

## 6. State of both repos

Nothing was edited in the skills repo. Nothing was edited in the orchestrator repo — no prompt, no code, no roadmap. The `# Task N` citations in `orchestrator/tests/` and the stale docstring at `test_agents.py:265–268` described above are untouched and remain live, deliberately, as evidence. Herald's own instance fix (three docstrings rewritten self-contained) was already committed there, per `orchestrator/.ai-factory/handoffs/08-plan-layer-citations-recur-in-docstrings.md` §4 — that is a different repo, already resolved, and not part of this ask.

One orientation note for whoever picks this up: `orchestrator/.ai-factory/handoffs/05-code-cites-plan-layer-orchestrator-side.md` §2's read-first map is now entirely dead as written. It points at `~/projects/skills/...`, and that path no longer exists — the repo lives at `skills/` under the `sakshi/` root. The source analysis it names as the must-read-first item, `handoffs/15-code-cites-fluid-plan-layer-false-resolution.md`, has itself been pruned from this repo's `.ai-factory/handoffs/` directory (confirmed absent; only `01`–`03` and this file remain). Anyone re-deriving the class analysis from handoff 05 alone will find nothing at either path — the class-level diagnosis handoff 05 §§7–8 summarizes is still the right starting point, not the vanished source it cites.
