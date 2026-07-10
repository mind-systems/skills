## Plan Review Summary

**Plan:** 1.4 — command-handoff: rewrite to a lens over `note`
**Artifacts reviewed:** plan (rev. 3), spec `20-command-handoff-destination-always-handoffs.md`, governing chain spec 15 (one-path design, via spec 20's reference), `src/commands/command-handoff.md` (current, 140 lines), `src/skills/note/SKILL.md`, ROADMAP.md milestone 1.4 + Phase 1 intro, ARCHITECTURE.md composition rule, prior plan-reviews 1 & 2.
**Risk Level:** 🟢 Low — both prior findings fully resolved; no new issues.

### Context Gates
- **Roadmap** — PASS. Plan `# Plan: 1.4 …` heading matches ROADMAP.md:157 milestone `1.4 — command-handoff: rewrite to a lens over note`, sitting on the `[x]`/`[ ]` seam (1.1–1.3 done, 1.4 next). `Spec:` tag resolves to `.ai-factory/specs/20-…`. Phase 1 intro (ROADMAP.md:149) names no explicit `Governing spec:`; spec 20 references spec 15's one-path design, which the current file reflects and the plan preserves. The roadmap line's own contract (destination invariant, three hooks, grid skeleton inline, cut what `note` does, byte-equivalent except the fix, ~80 aspiration never a clamp) maps 1:1 onto the plan's Tasks. Chain intact.
- **Architecture** — PASS. `ARCHITECTURE.md:30` "Composition: mechanism vs policy" — the plan honors "a top loads the engine, never inlines it": Task 2 keeps `loads: note` + the three-hook delegation surface and cuts every mechanic `note` already owns, inlining no engine mass.
- **Rules** — `.ai-factory/RULES.md` absent (WARN, optional; no project rule file to check).
- **Skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` absent; no project overrides.

### Critical Issues
None.

Both issues raised across the prior reviews are resolved in this revision:

1. **Grant-set preservation (plan-review-1 blocker).** Task 2 bullet 1 now explicitly keeps `allowed-tools: Read Write Bash(ls *) Bash(mkdir *) Glob Skill` with the correct rationale — `note` loads via the Skill tool and runs inline in the same agent, so its Step 3 `mkdir -p <destination>`/`Write` are performed by this command's agent; a foreign-root handoff creates a new dir and writes into it, so the grants are required. It correctly scopes spec 20's "no file mechanics re-enter the command" to the **body** (no restated prose), not the frontmatter. Independently confirmed against `note/SKILL.md:52-64` (mkdir + Write execute in-agent) and the sibling precedent `roadmap-decompose` (keeps `Write` despite delegating note-writing). Task 3 asserts the grant set is preserved unchanged, matching.

2. **grep-guard exemption under-enumeration (plan-review-2 minor).** Task 3 now spells out that `Write` matches as a bare substring and enumerates the benign expected hits — the frontmatter `allowed-tools` line, the "do not mkdir/Write/number yourself" negations, and the "Write **in English**" language directive (explicitly called out as a language rule, not a file mechanic, that survives the rewrite). It fails only on a hit that *restates* file mechanics as command procedure. Correspondingly, Task 1's checklist item (8) now pins the "write the handoff in English regardless of conversation language" directive into the byte-equivalence inventory, so its survival is no longer undecided.

The two plan-review-1 minors also remain explicit: `argument-hint: ""` is a conscious keep tied to spec 20's "no new parameters" (Task 2 bullet 1), and the literal `Read `$ARGUMENTS`` opener is explicitly dropped (Task 2 bullet 2) because under the new invariant `$ARGUMENTS` names a project-root **directory**, not a file — verified in Task 3.

### Positive Notes
- **Destination invariant correct and mechanically sound.** A named `$ARGUMENTS` path resolves to the project root only; destination is always `<root>/.ai-factory/handoffs/`, current project when unset, never `notes/` — passed verbatim to `note`'s destination-directory hook (`note/SKILL.md:31`, used for mkdir/scan/path). Matches spec 20 exactly.
- **Byte-equivalence discipline well-structured.** Task 1's in-session policy inventory (meaning-tree mandate, next-step-scoped read-first map, 11-section grid verbatim + prose directive, tree-completeness gate with paste-back-pointer exemption, verbosity override, semantic-slug rule, minimal pointer contract, English directive) is the contract Task 3 walks — the right protection for a "behavior byte-equivalent" rewrite.
- **Slug delegation correct.** Slug stays `note`'s `$1`/topic derivation "supplied semantically" with the explicit "never the literal word `handoff`" rule, correctly avoiding passing the project-root path as `note`'s `$1`.
- **Three-hook surface intact.** Destination / template (grid skeleton passed **blank** as the mining lens, or prose directive through the same hook) / verbosity directive — matches `note`'s three hooks, with the correct warning against pre-filling the skeleton (which would make distillation a no-op).
- **Live-baseline honesty.** Task 3 flags the spec's pre/post session-baseline check as user-run (needs a real mineable session) and refuses to fabricate one — exactly right for the plan-review→orchestrator pipeline.
- **Composition boundary respected** throughout: top loads the engine, no engine mechanics restated in the body.

The architecture, destination fix, grant-set handling, and byte-equivalence protocol are all sound. The plan is ready for the orchestrator.

PLAN_REVIEW_PASS
