## Plan Review Summary

**Plan:** `.ai-factory/plans/trickster77777/10-60-1-a-dead-hand-stops-being-a-stop.md`
**Task:** 60.1, a dead hand stops being a stop (named roadmap `.ai-factory/roadmaps/trickster77777.md`, Phase 60)
**Files the plan targets:** 1 (`src/skills/agent-architect/SKILL.md`)
**Risk Level:** 🟢 Low

### Context Gates

- **Roadmap:** OK. The plan's `# Plan: 60.1 — a dead hand stops being a stop` heading matches the unchecked contract line 60.1 in `.ai-factory/roadmaps/trickster77777.md`. I read its `Spec:` (`167-a-dead-hand-stops-being-a-stop.md`), the phase note (`166-a-dead-hand-is-remade-without-a-pause.md`), and the phase's `Governing spec:` `docs/paired-loop.md` § "How the memory begins, and how it survives". The replacement wording is consistent with that section: "nothing is asked before the next one is made", and "What a fresh hand costs is context, not permission".
- **Architecture:** OK. The edit changes only one policy paragraph in a lens skill (`agent-architect`). The shared engine (`architect-editor-engine`) and `src/agents/editor.md` stay as they are, which matches the spec's claim that the editor side has no matching stop. I checked this myself: `grep -n "dead\|respawn" src/agents/editor.md` returns nothing.
- **Rules:** WARN (non-blocking). `.ai-factory/RULES.md` is not present.
- **Skill-context:** `.ai-factory/skill-context/aif-review/SKILL.md` is not present.

### Ground-truth verification

I checked each of the plan's claims against the files:

- **Target paragraph:** the last paragraph of § "Spawn once, message thereafter" opens "If the send fails, the editor is dead: report to the user **before anything" and ends "it silently is the defect.". The `## Relay on the marker; author the apply work-order and your own legwork` heading follows it directly. The plan is correct.
- **The "Leaving both buffers live" paragraph:** it quotes "Losing the editor is never fatal; losing it silently is the defect". The new wording keeps that sentence verbatim, so the quote stays accurate. The plan is correct.
- **The liveness-probe paragraph:** it ends "the rule below for a dead editor governs". That pointer is generic and stays true. The plan is correct.
- **Removed phrases:** "warm context", "respawn", "self-contained per round", "resent as-is", and "eager with authored" occur in `src/` and `docs/` only inside the target paragraph. The plan is correct.
- **Replacement text:** the text the plan quotes matches the spec's § "What must be true after" block word for word once the `> ` prefixes are removed, including the bold `**must be**`. The plan is correct.

### Critical Issues

None.

### Issues

1. **The blast-radius sweep's "no others" expectation is wrong as written, and the step cannot confirm its "two places" claim.**
   The plan's second task runs
   `grep -rln "sent onward\|auto-replayed\|editor is never fatal" src/ docs/ .ai-factory/`
   and says to "Expect these files and no others", listing five files. I ran that command against the current tree and it returns **six**. The extra one is the plan file itself (`.ai-factory/plans/trickster77777/10-60-1-a-dead-hand-stops-being-a-stop.md`), because the plan quotes all three phrases. By the time the implementer runs the sweep, this plan-review file will match too, since it quotes the phrases. Any later review file for the task may match as well. So the implementer will get a result that contradicts the plan's stated expectation. They then have to guess whether that is a real blast-radius hit, or they may "fix" a pipeline artifact that should not be touched.
   There is a second problem in the same step. `-l` prints only file names, so the plan's check that `SKILL.md` "should now match only on 'editor is never fatal' in two places" and that "sent onward"/"auto-replayed" are gone cannot be read from that output.
   **Fix:**
   - Add the task's own pipeline artifacts under `.ai-factory/plans/trickster77777/10-60-1-…`, `.ai-factory/plan-reviews/trickster77777/10-60-1-…`, and `.ai-factory/reviews/trickster77777/10-60-1-…` to the list of expected, leave-untouched matches. Alternatively, run the sweep with `--exclude-dir=plans --exclude-dir=plan-reviews --exclude-dir=reviews`.
   - For the per-occurrence check, add a line-level grep such as `grep -n "sent onward\|auto-replayed\|editor is never fatal" src/skills/agent-architect/SKILL.md`. It should return exactly two lines, both on "editor is never fatal": one in the "Leaving both buffers live" paragraph and one at the end of the new paragraph.

2. **The wrapping instruction leaves room to break the sweep's own substring.**
   The plan says to hard-wrap "at about 72–76 columns" and that the spec's line breaks are "fine to reuse". If the implementer rewraps on their own instead of reusing those breaks, "Losing the editor is never fatal" can split between "editor" and "is". The line-level check in issue 1 would then quietly find only one occurrence, which is the line-wrap trap the spec's § "What breaks on contact" warns about. The spec's breaks keep `editor is never fatal; losing it silently is the defect.` on one line.
   **Fix:** tell the implementer to **use** the spec block's line breaks exactly, not just allow it. Then the result is deterministic and the two-occurrence check holds.

### Positive Notes

- The plan follows the task spec's scope exactly. It changes one paragraph, sets explicit boundaries against touching the probe paragraph, the "Leaving both buffers live" paragraph, and `editor.md`, and correctly leaves the other architect's buffer (`.ai-factory/notes/01-architect-buffer.md`) out of scope.
- It checked the only place in the file that quotes the old wording (the "Leaving both buffers live" paragraph) and confirmed the carried-forward sentence keeps it accurate. That is the check the spec's sweep note says an earlier version of the spec missed.
- It keeps the deliberate `**must be**` bold and gives the spec's reason for it.
