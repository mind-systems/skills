# Plan Review: 19.2 — aif: grant `Bash(ln *)` for the AGENTS.md symlink step

## Code Review Summary

**Files Reviewed:** 1 plan + 1 target file (`src/skills/aif/SKILL.md`), cross-checked against the task spec, the contract line, and the phase's governing spec
**Risk Level:** 🟢 Low

### Context Gates

- **Architecture** — `.ai-factory/ARCHITECTURE.md` present. The change is a single frontmatter token on one skill; it crosses no module boundary and touches neither the engine/lens composition rule nor any `loads:` edge. No misalignment.
- **Rules** — `.ai-factory/RULES.md` absent (WARN, non-blocking). No project rule file constrains frontmatter grant syntax; the repo's own convention was used as the reference instead (see below).
- **Roadmap** — linkage present and correct. `.ai-factory/roadmaps/trickster77777.md` L16 carries the `[ ] 19.2` contract line, whose `Spec:` tag resolves to `.ai-factory/specs/trickster77777/80-aif-ln-grant-for-agents-symlink.md` — the spec the plan cites. Phase 19's `Governing spec: docs/sakshi-harness/sakshi-harness.md` names the AGENTS.md→CLAUDE.md symlink as a harness contract requirement, which is exactly the step this grant unblocks. Plan, contract line, task spec, and governing spec agree.
- **skill-context** — `.ai-factory/skill-context/aif-review/SKILL.md` absent (WARN, non-blocking). No project-specific review overrides to apply.

### Critical Issues

None.

### Verification performed

Every grounded claim in the plan was checked against the live file rather than taken on description:

- **Current L5 value** — plan states `allowed-tools: Read Glob Grep Write Bash(mkdir *) Skill AskUserQuestion`. Live L5 matches byte-for-byte. The plan's assertion that 19.1 has already landed and dropped `Bash(node *update-config.mjs*)` is confirmed on two independent surfaces: the grant is absent from L5, and the roadmap marks 19.1 `[x]`. The shared-line guard is therefore already satisfied by the ordering that actually occurred — the plan's target value preserves 19.1's edit.
- **The 19.1-not-yet-landed fallback** (plan L32) is now counterfactual, but it is written as a conditional keyed on what the implementer reads live (*"if the live line still carries…"*), so it degrades correctly rather than misleading. Keeping it costs nothing and guards against a rollback.
- **Line-number drift, correctly caught** — the spec cites `## AGENTS.md Generation` at L199–207 with the command at L204. Live: section at **L156**, command at **L161**. The plan flags this drift explicitly and pins the live numbers as authoritative. This is the right call and the right direction of deference — ground truth over a stale description. Verified independently: `grep -n 'AGENTS.md Generation'` → 156, `grep -n 'ln '` → 161.
- **Grant pattern syntax** — `Bash(ln *)` is a prefix pattern; the actual command `ln -sfn CLAUDE.md AGENTS.md` begins with `ln ` and matches. It also matches the repo's settled convention for scoped Bash grants (`Bash(mkdir *)`, `Bash(ls *)`, `Bash(git *)`, `Bash(rm *)`, `Bash(find *)` across eighteen skills and commands). Placement immediately after `Bash(mkdir *)` keeps the `Bash(...)` entries contiguous, matching `aif-docs`, `note`, and `roadmap-prune`.
- **Minimal grant** — `Bash(ln *)` and nothing broader, per both the spec's guard and the contract line's explicit "not a broader `Bash(*)`". Honored literally.
- **No sibling gap** — swept every `SKILL.md` and command for `ln` invocations; `src/skills/aif/SKILL.md:161` is the only one repo-wide. The spec's claim that this is the sole `ln` invocation holds not just within the file but across the package, so this task closes the gap completely and leaves no analogous ungranted step behind.

### Positive Notes

- **The plan re-grounded rather than inherited.** It did not copy the spec's L199–207 citation forward; it read the file, found the drift, and said so with the live numbers and a precedence rule. That is the discipline the global CLAUDE.md asks for — a description drifted, code won — and it converts a stale reference from a trap into a documented correction.
- **The shared-line hazard is handled as state, not as hope.** Rather than assuming an ordering, the plan states the verified current value *and* supplies a conditional branch for the other ordering. An implementer landing this edit cannot silently clobber 19.1's work in either world.
- **Scope discipline is stated positively and negatively.** "Edit line 5 only", "do not touch `## AGENTS.md Generation`", "no other frontmatter field, no body text" — with the reason attached (*"It is correct as written"*), so the implementer knows the section was considered and deliberately excluded, not overlooked.
- **The verification step is falsifiable.** `grep -n 'allowed-tools'` plus "a single changed line in `git diff`" is a check that can actually fail — it pins presence, absence, and blast radius together.

PLAN_REVIEW_PASS
