# Review: 38.2 — `roadmap-test-coverage`'s own numbering scan joins the family rule

**Changed:** `src/skills/roadmap-test-coverage/SKILL.md` (one hunk, § "Layer 4 — Deep Research (parallel agents)", the "Determine next note number:" definition site). Plan and plan-review files are new artifacts, not reviewed as code.

## Read in full
`src/skills/roadmap-test-coverage/SKILL.md` (437 lines), the task spec `126-…`, the plan, and `src/skills/note/SKILL.md` § "Step 3"/"Step 4" for the family shape being matched.

## Verified against the plan's whole-file checks
- `grep -n '\[0-9\]\[0-9\]\|two-digit\|start at `01`'` → no hits.
- `maxdepth 1` appears exactly once (the Layer 4 command).
- `9999` appears only in the Layer 4 bound paragraph (three lines, one paragraph); `0001` present as the default and the range start.
- `.ai-factory/specs/<NN>-<slug>.md` consumer sites: 7 before, 7 after — untouched, inherit the new `<NN>` definition.
- Frontmatter (`loads:`, `allowed-tools`) byte-identical to HEAD; the new command string still opens with `find`, inside the `Bash(find *)` grant.
- File is 437 lines, under the 500-line bound.
- Family sweep `grep -rn '\[0-9\]\[0-9\]' src/skills src/commands` now hits only `src/skills/aif-plan/SKILL.md` — the dormant carrier the contract leaves alone.

## Verified at runtime (macOS BSD `find`/`sort`)
- New command against `.ai-factory/specs/trickster77777` → `126-test-coverage-numbering-joins-the-family-rule.md` (the old `| sort | tail -1` form returns `99-…`): numeric comparison holds.
- New command against the flat `.ai-factory/specs` (holds only the `trickster77777/` subdirectory) → empty output: `-maxdepth 1` excludes the subdirectory, and the empty-directory default (`0001`) is the path the prose takes.
- `-exec basename {} \;` strips the leading path so `sort -n` sees a numeric key; without it every line would key to 0.

## Correctness of the prose
- Read and write are stated as two rules (any-length read via `^[0-9]+-.*\.md$`, four-digit write), matching `note` line-for-line in meaning — the read side is not narrowed to four digits.
- Bound predicate carries the "or greater" clause; the stop is placed after `Store as $NEXT_NOTE_NUM` and before "Launch one `Explore` agent per area", so no agent is spawned at the bound. The report line mirrors `note`'s form with the destination named.
- `mkdir -p` still precedes the scan; at the bound the directory necessarily already exists, so this is a no-op, not a write — consistent with "writes nothing".
- Parallel structure, agent prompt template, Critical Rules 3 and 6 untouched. Destination stays the flat `.ai-factory/specs/` as the spec pins; the named-roadmap `<slug>/` contradiction is left open as recorded.

## Findings
None. The one cosmetic note — the report-line code span wraps across two source lines (`… nothing\nwritten.`) — renders as a single span with a space in CommonMark and reads unambiguously; no change needed.

REVIEW_PASS
