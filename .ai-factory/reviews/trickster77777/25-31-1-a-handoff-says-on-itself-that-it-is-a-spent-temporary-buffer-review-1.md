## Code Review — 31.1 a handoff says on itself that it is a spent, temporary buffer

**Plan:** `.ai-factory/plans/trickster77777/25-31-1-a-handoff-says-on-itself-that-it-is-a-spent-temporary-buffer.md`
**Spec:** `.ai-factory/specs/trickster77777/106-handoff-processed-mark.md`
**Changed under `src/`:** `src/commands/command-handoff.md` (+20 −3) — the only file. The rest of the working tree is this task's own plan/plan-review artifacts under `.ai-factory/`.

### What changed, read in full

The file was read end-to-end (139 lines), not only the diff. Five edits landed, one per plan item:

1. `description:` (`:2-8`) — the closing sentence now names the entity and its lifetime ("a temporary memory buffer that carries context from one session to the next, spent once read, persisted under `.ai-factory/handoffs/`"); `durable` is gone from the block. The two preceding sentences are untouched.
2. Grid skeleton (`:33`) — the mark line inserted on its own line, blank-line-separated, between the `# Handoff — <semantic slug …>` title (`:31`) and `## 1. Frame` (`:35`). No section name, order, or other skeleton line changed.
3. **Prose shape.** (`:90-96`) — the paragraph now opens by stating that the file begins with the `# Handoff — <slug>` title and, directly beneath it, the mark line, reproduced verbatim in its own `~~~` fence; the original causal-thread sentence continues as "From there it flows into prose …", with the rest of the paragraph intact.
4. Step 2 **Template** bullet (`:107`) — the mark line named as the one exception in either shape: literal template text, reproduced verbatim into the written file, not a placeholder description, nothing mined into it, blank-skeleton rule inapplicable. No claim about `note`'s internals.
5. `## Holding a handoff` (`:133-139`) — a non-numbered closing section carrying the rule.

### Verification (counts taken on a whitespace-normalized read, per the spec's method)

| Check | Result |
|---|---|
| mark between `# Handoff` title and `## 1. Frame` (line indices 30 / 32 / 34) | ✅ |
| mark literal byte-identical to the corpus form (`.ai-factory/handoffs/17:3`) | ✅ exact match, backticks included |
| prose-shape directive names both the `# Handoff — <slug>` title and the mark line beneath it | ✅ |
| Template hook's literal/verbatim exemption stated | ✅ |
| `durable` in the `description:` block | 0 ✅ (the one remaining `durable` in the file is `:96` "the durable next step" — the unrelated pre-existing sense the plan preserves) |
| four parts of the body rule: audience / processed never edited / only unprocessed edited, flip `[x]` for `[ ]` and nothing else / spent previous part ⇒ new handoff | ✅ each present (`:135`, `:137`) |
| `**Date:**`, `**Source:**`, `roadmap-prune` | 0 / 0 / 0 ✅ |
| `cite`, `cited`, `citation`, case-insensitive | 0 ✅ |
| body rule under a non-numbered heading (no `## Step 4`) | ✅ `## Holding a handoff` |
| literal + reader-flips sentence occur twice file-wide (grid fence + prose fence), as the plan pins | ✅ 2 / 2 — position-scoped, both intended |
| `git diff HEAD -- src/skills/` | empty ✅ — no skill gains a read of the mark |
| `git diff HEAD --stat -- src/ active/ docs/ CLAUDE.md` | exactly `src/commands/command-handoff.md` ✅ |

### Runtime / correctness checks

- **Frontmatter still parses.** The `description:` stays a `>-` folded block with all continuation lines indented two spaces; no line-initial token that could break the scalar. `argument-hint`, `allowed-tools`, `loads: note` unchanged — no new grant was needed and none was taken.
- **The symlink path is intact.** `active/commands/command-handoff.md` → `../../src/commands/command-handoff.md`; `diff` of the two reads identical, so `~/.claude/commands` picks the change up with no second tracked blob.
- **The new fence does not collide with the skeleton fence.** The prose-shape block (`:92-94`) is a separate `~~~` pair opened and closed after the skeleton's own pair closes at `:88`; the mark literal's backticks are inline code inside it, not a fence delimiter. Both blocks render and both are unambiguously delimited.
- **The write path is unchanged.** `note` still performs mining, numbering, `mkdir`, and the write; the mark reaches the file through the template hook `note` already honors ("the note body follows the caller's directive verbatim", `src/skills/note/SKILL.md` § Hooks). `note` was not touched, so no cross-file contract moved.
- **Nothing scans the mark.** No step anywhere reads it, no skill was given one, and the mark is not a protocol token — it is prose addressed to a reader. `roadmap-prune:447` still reads "Do not touch `handoffs/` — it is never swept", untouched.
- **No downstream text drifted.** Repo-wide, "durable note" / "Always persists" survive only in the roadmap contract line and the spec, where they describe the pre-change state by design. No doc states the handoff format or calls it durable, so `Docs: no` holds. Phase 33.1's four surfaces (`roadmap-engine`, `roadmap-outline`, `roadmap-prune`, `orchestrator-artifacts`) are untouched, and `agent-architect`'s pre-compact buffer-path handoff keeps working — the new rule forbids editing a spent handoff, not writing a new one.
- **Existing handoffs are not backfilled**, as the spec requires; handoffs 15–18 already carry the literal in both states, so the corpus stays one form.

### Non-findings considered and dismissed

- *Description dropped the word "Always".* The pre-change sentence read "Always persists the handoff as a durable note under …"; the new one asserts persistence as a property of the result ("persisted under `.ai-factory/handoffs/`"), and the unconditional write is still stated in the body (Step 2 delegates numbering/`mkdir`/write to `note`; Step 3's pointer names "the path of the written file"). No behavioral guarantee is lost — wording only.
- *Closing paragraph `:139` naming the grounding guarantee.* This is the one sentence at the point of reliance that `.ai-factory/ARCHITECTURE.md` § "Composition: mechanism vs policy" permits, and the spec's guard explicitly allows naming it here. It states no rule about what may cite a handoff, and it declines to restate the guarantee further.
- *"the skeleton above" in Step 2 with two fenced blocks now in Step 1.* The bullet disambiguates by shape ("for the grid shape, the skeleton above … for the prose shape, a free-form body directive"), so the referent stays unambiguous.

No bugs, security issues, or correctness problems found; every spec verification count passes and the blast radius is exactly the one file.

REVIEW_PASS
