# Review — command-handoff: note mode emits short chat pointer, not full re-dump

## Scope
Reviewed `git diff HEAD` and `git status`. The only behavioral code change is `src/commands/command-handoff.md` (a skill/command spec — executable agent instructions, not runtime code). Other staged files are artifacts: `ROADMAP.md`, the spec note, the plan `.md`/`.json`, and the plan-review. Read `command-handoff.md` in full.

## Assessment against the milestone

The milestone required: (1) file gets the full handoff skeleton unchanged, (2) chat gets only a short pointer (path + 3–5 line orientation), (3) chat mode unaffected, (4) self-check gate applies to the file only.

- **(1) File unchanged** — sub-steps a–c (lines 112–116) are byte-for-byte the prior logic: `ls` for highest `<NN>`, semantic slug, verbatim Write to `.ai-factory/handoffs/<NN>-<slug>.md`. ✓
- **(2) Chat pointer** — new step 2 (lines 118–132) emits path + frame (§1) + next step (§4) + optional work-unit count, explicitly forbids re-emitting the full body, and is paste-back-able. Matches spec exactly. ✓
- **(3) Chat mode** — line 106 untouched. ✓
- **(4) Self-check scoping** — line 100 now splits the gate: chat mode → chat output; note mode → file content, with the chat pointer explicitly exempt from the proportionality gate. ✓

## Correctness / consistency checks

- **No orphaned references.** The old "Emit the handoff prompt to chat (same as chat mode)" step and the old sub-step (d) "report the path … as a one-line confirmation" were both removed; (d)'s intent is folded into the new pointer (path confirmation is part of the pointer). No dangling cross-reference to a "step 2" that no longer means "persist". ✓
- **Section references valid.** Pointer cites "section 1 (frame)" and "section 4 (next step)" — these match the skeleton headings `## 1. Frame` and `## 4. Next step` in Step 2. ✓
- **Numbering coherent.** Reordered to file-first (1) then pointer (2); sub-steps a–d collapsed to a–c since (d) was promoted. Internally consistent. ✓
- **Frontmatter still accurate.** Top description ("optionally persist the handoff as a durable note") does not promise a chat re-dump, so it remains correct under the new behavior. ✓
- **No tooling/permission impact.** `allowed-tools: Write Bash(ls *)` still covers the note-mode operations; the pointer is plain chat output needing no tool. ✓

## Findings
None. The change is minimal, internally consistent, and fully satisfies the spec. No bugs, security, or correctness issues.

REVIEW_PASS
