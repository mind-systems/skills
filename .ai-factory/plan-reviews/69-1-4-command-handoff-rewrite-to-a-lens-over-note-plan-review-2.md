## Plan Review Summary

**Plan:** 1.4 — command-handoff: rewrite to a lens over `note`
**Artifacts reviewed:** plan (rev. 2), spec `20-command-handoff-destination-always-handoffs.md`, governing chain spec `15-command-handoff-single-path-transfer-the-meaning-tree.md` (via roadmap line), `src/commands/command-handoff.md` (current), `src/skills/note/SKILL.md`, sibling `src/skills/roadmap-decompose/SKILL.md`, ROADMAP.md milestone 1.4, ARCHITECTURE.md composition rule, prior plan-review-1.
**Risk Level:** 🟢 Low — the blocking issue from plan-review-1 is fully resolved; one minor verification-guard imprecision remains.

### Context Gates
- **Roadmap** — PASS. Plan `# Plan: 1.4 …` heading matches ROADMAP.md:157 milestone `1.4 — command-handoff: rewrite to a lens over note`, sitting exactly on the `[x]`/`[ ]` seam (1.1–1.3 done, 1.4 next). `Spec:` tag resolves to `.ai-factory/specs/20-…`. Phase 1 intro (ROADMAP.md:149) names no explicit `Governing spec:`; spec 20 references spec 15's one-path design, which the current file already reflects and the plan preserves. Chain intact.
- **Architecture** — PASS. `ARCHITECTURE.md:30` "Composition: mechanism vs policy" — the plan honors "a top loads the engine, never inlines it": Task 2 keeps `loads: note` + the three-hook delegation surface and cuts everything `note` already does, inlining no engine mass.
- **Rules** — `.ai-factory/RULES.md` absent (WARN, optional; no project rule file to check).
- **Skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` absent; no project overrides.

### Critical Issues
None. The single blocking issue raised in plan-review-1 — Task 2 instructing the editor to strip `Write`/`Bash(mkdir *)` from `allowed-tools` — has been fully corrected in this revision:
- Task 2 bullet 1 now reads "keep `allowed-tools` at `note`'s full grant set plus `Skill` … do **not** strip `Write` or `Bash(mkdir *)`" with the correct rationale (`note` runs inline in the same agent via the Skill tool; its Step 3 `mkdir -p`/`Write` are executed by the command's agent, so the grants are required, e.g. a foreign-root handoff that creates a new dir).
- Task 3's verification now asserts the grant set is **preserved unchanged** (`Read Write Bash(ls *) Bash(mkdir *) Glob Skill`) rather than that the grants were dropped.
- This matches the sibling precedent: `roadmap-decompose` (`allowed-tools: … Write … Skill`, `loads: roadmap-engine` → `note`) keeps `Write` despite delegating note-writing. Independently confirmed the note engine (`note/SKILL.md:52-64`) executes `mkdir -p <destination>` and the `Write` in the same agent.

The two minor points from plan-review-1 are also now explicit in the plan: `argument-hint: ""` is a conscious keep (Task 2 bullet 1, tied to spec 20's "no new parameters"), and the literal `Read `$ARGUMENTS`` opener is explicitly dropped (Task 2 bullet 2, verified in Task 3).

### Positive Notes
- **Destination invariant correctly specified.** Task 2's framing — a named `$ARGUMENTS` path is the **project root only**, destination always `<root>/.ai-factory/handoffs/`, current project when unset, never `notes/`, no new modes — matches spec 20 exactly and is mechanically sound against `note`'s destination-directory hook (`note/SKILL.md:31`, `<destination>` used verbatim for mkdir/scan/path).
- **Byte-equivalence discipline is well-structured.** Task 1's in-session policy inventory (meaning-tree mandate, next-step-scoped read-first map, 11-section grid verbatim, tree-completeness gate + paste-back-pointer exemption, verbosity override, semantic-slug rule, minimal pointer contract) as the contract Task 3 walks is the right protection for a "behavior byte-equivalent" rewrite.
- **Slug delegation is correct.** Keeping the slug as `note`'s `$1`/topic derivation "supplied semantically" — with the explicit "never the literal word `handoff`" rule — correctly avoids passing the project-root path as `note`'s `$1`.
- **Live-baseline honesty.** Task 3 flags the spec's pre/post session-baseline check as user-run (needs a real mineable session) and refuses to fabricate one — exactly right for the plan-review→orchestrator pipeline.
- **Composition boundary respected** throughout: three hooks as the delegation surface, no engine mechanics restated in the body.

### Minor
- **Task 3 grep-guard exemption is under-enumerated.** The guard `grep -n "mkdir\|Write\|numbering" src/commands/command-handoff.md` is described as matching "only inside the frontmatter `allowed-tools` line and any … negations." But `Write` is matched as a bare substring, so any surviving body prose containing the word — most plausibly a restated "Write **in English**" line (present at `command-handoff.md:39` today, and *not* itself listed in Task 1's byte-equivalence checklist, so its survival is undecided) — would also match and is neither the frontmatter line nor a negation. This does not change the implementation outcome (the guard's purpose, catching restated file mechanics, is still served after a manual eyeball), but the exemption clause overclaims. Tighten it in Task 3 — either add "…and benign body prose such as 'Write in English'" to the exemption, or narrow the pattern to file-mechanic contexts (e.g. `Bash.*mkdir`, `` `Write` `` as a tool reference) — so the verifier isn't left reconciling an unexpected match against an exemption list that doesn't cover it.

Resolve the Minor guard-tightening and the plan is ready for the orchestrator. The architecture, destination fix, grant-set handling, and byte-equivalence protocol are all sound.
