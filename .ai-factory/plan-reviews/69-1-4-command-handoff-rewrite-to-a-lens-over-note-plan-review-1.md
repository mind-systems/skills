## Plan Review Summary

**Plan:** 1.4 — command-handoff: rewrite to a lens over `note`
**Artifacts reviewed:** plan, spec `20-command-handoff-destination-always-handoffs.md`, governing spec `15-command-handoff-single-path-transfer-the-meaning-tree.md` (via roadmap line), `src/commands/command-handoff.md` (current), `src/skills/note/SKILL.md`, ROADMAP.md milestone 1.4, ARCHITECTURE.md composition rule.
**Risk Level:** 🟡 Medium — one blocking frontmatter instruction; the rest of the plan is sound.

### Context Gates
- **Roadmap** — PASS. Plan title matches ROADMAP line `1.4` under "Phase 1 — Rewrite the skill package to the pyramid"; the `[ ]`/`[x]` seam sits exactly here (1.1–1.3 done, 1.4 next). Spec tag resolves to `specs/20-…`. Phase 1 intro names no `Governing spec:`; spec 20 references spec 15's one-path design, which the current file already reflects. Chain intact.
- **Architecture** — PASS. `ARCHITECTURE.md:30` "Composition: mechanism vs policy" — the plan honors "a top loads the engine, never inlines it" (Task 2: cut everything `note` does; keep `loads: note` + three hooks).
- **Rules** — `.ai-factory/RULES.md` absent (WARN, optional; no project rule file to check).
- **Skill-context** — `.ai-factory/skill-context/aif-review/` absent; no project overrides.

### Critical Issues

**1. Task 2 instructs dropping `Write` and `Bash(mkdir *)` from `allowed-tools` — this is unsanctioned by the governing spec, diverges from the ratified spec-15 contract and the sibling precedent, and risks breaking handoff persistence.**

`src/commands/command-handoff.md:9` currently carries `allowed-tools: Read Write Bash(ls *) Bash(mkdir *) Glob Skill` — exactly `note`'s full grant set (`Read Write Bash(ls *) Bash(mkdir *) Glob`) plus `Skill`. This is deliberate: milestone 133 (spec 15) shipped this file as the single path where **everything** routes through `note`, and spec 15's contract text reads "*`allowed-tools` covers note's full grant set + `Skill`*." Task 2 bullet 1 tells the editor to "drop them if present," reasoning that "the command itself no longer needs `Bash(mkdir *)`/`Write` since `note` owns file mechanics."

That rationale conflates two different things: the command **body** not *restating* mkdir/Write mechanics (correct, and what spec 20's guard "no file mechanics re-enter the command" actually demands) versus the executing agent not *performing* mkdir/Write. `note` is loaded via the Skill tool and executes **inline in the same agent**; when its Step 3 runs `mkdir -p <destination>` and `Write`s the file, the agent running `command-handoff` performs those calls. With the single-path collapse there is no non-`note` route, so `note`'s mechanics are *always* executed here.

Concrete failure scenario: user runs `/command-handoff ~/projects/mind/mind_api`; the lens resolves `~/projects/mind/mind_api/.ai-factory/handoffs/` and delegates to `note`; `note` needs `mkdir -p` (new foreign dir) and `Write`. With those grants stripped, best case is a permission prompt on every handoff (a behavior change spec 20's "behavior byte-equivalent except the destination fix" forbids), worst case the write is blocked.

Note also that the plan's own tool list is internally inconsistent: it keeps `Bash(ls *)` and `Glob` "for the lens's own reads," but the lens does not scan or number — `note` does. If `Bash(ls *)` is retained because the agent runs `note`'s numbering scan, then `Bash(mkdir *)` and `Write` must equally be retained because the agent runs `note`'s directory-create and file-write. You cannot justify keeping the read-side note grant while dropping the write-side note grants.

The closest existing precedent confirms the correct move: `roadmap-decompose` (loads `roadmap-engine` → `note`) keeps `Write` in its `allowed-tools` even though it delegates note-writing. The plan strips `Write` from `command-handoff`, going *further* than any note-caller in the repo, with no evidence it is safe.

Fix: **keep the frontmatter grant set as-is** — `Read Write Bash(ls *) Bash(mkdir *) Glob Skill` — and change Task 2 bullet 1 to "frontmatter stays functional and unchanged: `loads: note`, and `allowed-tools` retains `note`'s full grant set plus `Skill` (the agent executes `note`'s mkdir/Write inline)." Task 3's verification should assert the grant set is preserved, not that mkdir/Write were dropped. This is the safe reading and the only one consistent with spec 20's byte-equivalence mandate.

### Positive Notes
- **Destination fix is correctly specified.** Task 2's invariant framing — a named `$ARGUMENTS` path is the **project root only**, destination always `<root>/.ai-factory/handoffs/`, current project when unset, no new parameters/modes — matches spec 20 exactly and is mechanically sound against `note`'s destination hook (which uses `<destination>` verbatim for mkdir/scan/path).
- **Byte-equivalence discipline is well-structured.** Task 1's read-only policy inventory (meaning-tree mandate, next-step-scoped map, 11-section grid verbatim, tree-completeness gate + pointer exemption, verbosity override, semantic-slug rule, minimal pointer contract) as an in-session checklist that Task 3 walks is the right way to protect a "behavior byte-equivalent" rewrite.
- **Live-baseline honesty.** Task 3 correctly flags that the spec's pre/post session-baseline check needs a real mineable session and is user-run, refusing to fabricate a baseline — exactly right for a plan-review-then-orchestrator pipeline.
- **Composition boundary respected** throughout (top loads engine, three hooks as the delegation surface, no engine mass inlined).

### Minor
- `argument-hint: ""` (current) is not addressed by the plan. The command now meaningfully accepts an optional project-root path. Spec 20 frames destination "as an invariant of the artifact, not a rule about arguments" and mandates "no new parameters," so leaving the hint empty is defensible — but the rewrite should consciously decide rather than carry it over by accident. Non-blocking.
- The rewrite must not carry over the literal `Read `$ARGUMENTS`` line (`:13`), which reads the argument as a *file*; under the new invariant `$ARGUMENTS` is a project-root directory. Task 2's whole-file rewrite covers this, but the editor should be explicit. Non-blocking.

Resolve Critical Issue 1 (revise Task 2 bullet 1 and the matching Task 3 check to preserve the frontmatter grant set) and the plan is ready.
