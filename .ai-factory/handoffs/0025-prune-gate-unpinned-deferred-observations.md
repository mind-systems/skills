# Handoff — the prune gate stops on 169 unpinned deferred observations

**Processed:** `[ ]` — whoever reads this marks it; a marked handoff is spent.

## 1. Frame

The skills repo's only roadmap is fully closed — 53 `[x]` tasks, not one `[ ]` — and a prune of everything was ordered, but `/roadmap-prune` refused at its own Step 0 gate because 169 deferred observations across 88 review files carry no status marker, so nothing was pruned, swept, or edited — the originating session's context isn't available here; trust these files, not memory.

## 2. Read-first map

One work-unit: unblock the gate. The next action is a dedicated resolution session that disposes of every unpinned observation and pins it. Everything below is scoped to that action, not to the prune that follows it.

### Must-read now (minimal rehydration set)

- `~/.claude/skills/orchestrator-artifacts/SKILL.md` § 6 "Status-marker grammar" — the exact syntax you will be writing 169 times and the dedup rule that collapses most of them; also § 5, which defines the entry line you are pinning. ← lead with this; the whole resolution is an application of these two sections
- `~/.claude/skills/roadmap-prune/SKILL.md` § "Step 0 — Deferred-observations gate" — the judge your work will face on the re-run: what it scans (repo-wide, any depth), what it accepts as pinned, and its explicit refusal to be engineered around
- `.ai-factory/roadmaps/trickster77777.md` — the roadmap under prune; read it to see that there is **no open task anywhere in it** (this is what constrains your disposal options, see § 4) and to place each observation's phase
- The regenerated list of the 169 unpinned entries — it does not exist on disk; produce it first with the command in § 10. It is ~116 KB of raw text and must not be echoed into chat wholesale.

### Read on demand

- `.ai-factory/specs/trickster77777/` — the task specs that entries' `Affects:` fields point at; open one only when an entry names it, never as a sweep
- `.ai-factory/ARCHITECTURE.md` — the prune's `## Features` target. Irrelevant to resolution; needed only on the eventual prune re-run, where its `## Features` header version marker decides whether the legacy self-heal pre-pass (Step 4.2a) fires. That marker was never read this session — the run stopped nine steps earlier.
- `docs/paired-loop.md`, `docs/reference-by-name.md`, `docs/sakshi-harness/skill-cycle.md` — governing specs named on the phase headers the heaviest observation clusters sit under; consult when an entry's `Affects:` target is a doc rather than a skill
- `src/skills/<name>/SKILL.md` — the actual leaves most `[fixed]` dispositions would land in

## 3. Current state

**Done:**

- Ran `/roadmap-prune` with argument "всё закрытое" (prune everything closed). It stopped at Step 0 and made zero edits.
- Established the target: there is **no** `.ai-factory/ROADMAP.md` in this repo. The sole roadmap is the named one, `.ai-factory/roadmaps/trickster77777.md` (318 lines, 78 KB), so a prune here is a named-roadmap prune with stem `trickster77777` throughout.
- Scanned the gate's full scope — 156 files under `.ai-factory/plan-reviews/trickster77777/` and `.ai-factory/reviews/trickster77777/`. 107 of them carry a `## Deferred observations` section.
- Counted: **169 unpinned entries across 88 files**; 41 entries already pinned. Of the unpinned, 157 are canonical `- Affects: …` lines and 12 are bare bullets inside the same section with no `Affects:` prefix — the latter live in `reviews/trickster77777/11-25-2-…-review-1.md` (1) and in both rounds of `reviews/trickster77777/21-28-1-…-review-1.md` / `-review-2.md` (11 between them). They are entries all the same and the gate counts them.
- Rolled the unpinned up by phase: 20 — 7; 21 — 1; 23 — 2; 25 — 4; 26 — 31; 28 — 35; 29 — 12; 30 — 7; 33 — 4; 34 — 11; 35 — 4; 36 — 10; 37 — 9; 38 — 2; 39 — 6; 40 — 24. Phases 28, 26 and 40 hold just over half of everything.
- Measured the volume: 169 lines, ~116 KB of entry text, median entry 659 characters, longest 1904. Even truncated to 150 characters per entry the listing is 48.7 KB — which is why the chat report gave counts and a regeneration command instead of the verbatim list the gate's wording asks for.
- Verified the pinned/unpinned discriminator empirically (§ 10).
- Established the constraint that shapes the next step: the roadmap holds **53 `[x]` and 0 `[ ]`**. Phases 41–49 exist as headers with preamble prose but have never been decomposed — zero task lines under any of them. There is therefore no open task in the repository whose spec could receive a `[routed → <path>]` marker today.

**In-flight:**

- Nothing. The prune is parked, not half-done. No sweep began, no `[x]` line was deleted, no spec or artifact was removed, no `## Features` row was written.

**Uncommitted working-tree state:**

- None at the time of the scan — clean tree at HEAD `9024e38 Roadmap update` on branch `dev`.
- This handoff file itself is the one new untracked path.

## 4. Next step

Open a **dedicated resolution session** against `/Users/max/projects/sakshi/skills` and work the 169 entries to zero unpinned. Concretely, in this order:

1. **Regenerate the list to a file, not to chat** — the command in § 10. Then immediately group it, because 169 is a count of occurrences, not of problems: most tasks ran two or three review rounds and each round's file restates the same observation. Group by `(task key from the filename, e.g. 28-2` + `Affects:` target + gist`)`. The number of distinct findings is far below 169 and that is the number the session actually costs.
2. **Decide each distinct finding once**, then pin **every** occurrence of it across that task's review files — the dedup rule in `orchestrator-artifacts` § 6 makes this obligatory, not an optimisation. Deciding per file instead of per finding is the way this session goes wrong.
3. **The disposal choice is constrained here.** `[routed → <path>]` requires the path to resolve to an editable surface — the task spec of an **open** task, never a completed or frozen one. There are no open tasks. So either the finding is fixed in place and pinned `[fixed]`, or it is evaluated as moot/stale/already-handled and pinned `[dismissed]` — **or** a phase among 41–49 is decomposed first (via `/roadmap-decompose`) so that a real open task with a real spec exists to route into. Several of the clusters look like exactly that case: they describe work the outlined-but-undecomposed phases already exist to do. **Put this choice to the user before spending the session** — it decides whether this is a fix-and-dismiss pass or a decompose-then-route pass, and the two have very different costs.
4. **Re-run `/roadmap-prune`** once the gate reads zero unpinned. Expect it to then proceed through the named-roadmap path: sweep `plans/trickster77777/`, `plan-reviews/trickster77777/`, `reviews/trickster77777/` (never the flat dirs, never `test-runs/` — this is a main roadmap, not a test one), delete the 51 captured `Spec:` paths and the `Phase note:` paths of phases it empties, and write `## Features` rows into `.ai-factory/ARCHITECTURE.md`.

## 5. Working discipline

- **Never commit without explicit permission.** Uncommitted changes are assumed intentional. `roadmap-prune` in particular ends with everything in the working tree and commits only when told, with the message exactly `Roadmap prune` — no body, no prefix, no co-author line.
- **The gate is not negotiable.** The prune parks; it is not engineered around. Do not narrow the scan's scope, do not edit the gate, do not pin an entry you have not actually disposed of, do not run a partial prune. The gate passing is the resolution's proof, and a manufactured pass destroys the only signal the mechanism has.
- **Confirm the disposal strategy before executing it** (§ 4 item 3). That question is the user's, not the agent's.
- **Memory is never written** unless the user says one of the explicit trigger phrases.
- Report what actually happened — if a finding was dismissed because it was too expensive to chase, say that in the session, not `[fixed]`.

## 6. Error log

- **Assumed a default `ROADMAP.md` existed.** The first instinct was to read `.ai-factory/ROADMAP.md`; the directory listing has no such file. Corrected by enumerating `.ai-factory/roadmaps/`, which holds exactly one file, `trickster77777.md`. Any agent arriving here with prune muscle-memory will make the same mistake — the repo is multiuser-shaped with a single named roadmap and no default pair.
- **First pass over the entries treated every `-` bullet in the section as a canonical `- Affects:` entry.** Refining the scan to separate the two shapes found 12 bullets that carry no `Affects:` prefix. Both shapes are entries and both must be pinned; the correction mattered for understanding the corpus, not for the verdict (169 either way).
- **Planned to echo all 169 entries into chat, as the gate's wording literally directs.** Abandoned on measurement: 48.7 KB even after truncating each entry to 150 characters. Replaced with counts, a per-phase rollup, and the verbatim regeneration command. Do not retry the verbatim echo — regenerate to a file and work from there.
- **Reported the checkout's git identity from the session's `userEmail` context block instead of from git**, and so announced an owner/operator mismatch that does not exist: the block carries the Claude account email, while the `gitStatus` block gives only `Git user: max` with no address. `git config user.email` is `trickster77777@gmail.com` — identical to the roadmap's `> Owner:` line, which is where the roadmap's name comes from in the first place. Read the identity with `git config user.email`; the session context is not a source for it.
- **Nearly reported a phase-level rollup keyed off the file's `<seq>` prefix rather than the task key.** The filenames are `<seq>-<N>-<M>-<slug>-<genre>-<round>.md`, so the sequence number and the phase number are different leading integers in the same name — stripping the wrong one silently produces a plausible, wrong table.

## 7. Orientation

- **`.ai-factory/ROADMAP.md` vs `.ai-factory/roadmaps/trickster77777.md`** — the first does not exist. Every path in this repo's artifact tree carries the `trickster77777` stem segment: `specs/trickster77777/`, `plans/trickster77777/`, `plan-reviews/trickster77777/`, `reviews/trickster77777/`.
- **The roadmap's owner is this checkout's git identity.** The first line reads `> Owner: trickster77777@gmail.com`, and `git config user.email` in this checkout is the same address (from `~/.gitconfig`; every recent commit is authored by it). The roadmap's name is the local-part of that address, which is why the stem is `trickster77777` — derive it from `git config user.email`, never from the Claude account email the session context reports, which is a different address entirely and produced a false mismatch when it was read as the git identity once already.
- **Step 0 gate vs Step 7.5 citation scan.** Both scan and both report; only Step 0 refuses. Step 7.5 is report-only by construction and its findings never block anything. Do not conflate "the prune printed a list of problems" with "the prune was blocked" — this session was blocked by Step 0 and never reached 7.5.
- **`[dismissed]` passes the gate exactly as `[fixed]` does.** The gate counts markers, not judgement. That is deliberate — the judgement is the resolution session's, recorded in its pins — and it is also exactly how this mechanism gets hollowed out if someone is in a hurry.
- **Two review genres, one section.** `plan-reviews/` and `reviews/` both carry `## Deferred observations` and the gate scans both. 55 of the 88 unpinned-bearing files are plan-reviews, 33 are reviews.
- **`---STOP---` is the literal last line of the roadmap file**, not an artifact of how it was printed.
- **Phases 41–49 are headers without tasks.** They are outlined, not decomposed. A grep for `[ ]` returning nothing does not mean the roadmap is finished — it means the seam sits at the end of phase 40 and the next nine phases have never been decomposed.

## 8. Domain model spine

Settled; do not re-litigate:

- **The pruning slice is every `[x]` task.** Retention is only by explicit user instruction at invocation; absent that, history lives in git and in ARCHITECTURE.md. — `roadmap-prune` § "Step 1 — Identify the pruning slice"
- **A named-roadmap prune touches only its own stem's subdirectories.** Never the flat `plans/`/`plan-reviews/`/`reviews/`, never a sibling stem's. — `roadmap-prune` § "Step 5 — Sweep completed artifacts and specs"
- **Deletion goes only through captured tokens** — the pruned `[x]` lines' `Spec:` tags and emptied phases' `Phase note:` pointers. No spec directory is ever scanned or swept. — same section
- **Markers are append-only and live at the end of the entry line.** Entry text and `Affects:` are never rewritten; markers only accumulate. The reviewer never writes them — only the resolution session does. — `orchestrator-artifacts` § 6
- **A `[routed → <path>]` target must be an open task's spec** — never a completed or frozen surface. — `orchestrator-artifacts` § 6
- **A review carrying only deferred observations still passes.** They are non-findings; the gate is about disposal, not about review verdicts. — `orchestrator-artifacts` § 5
- **Legacy markers still count as pinned** — `[promoted → <path>]`, `[audit-corroborated]`, `[audit-dismissed]`, `[unrouted-reported]`. Retired from the active vocabulary, honoured where they already sit; history is never rewritten. — `orchestrator-artifacts` § 6

## 9. Hard rules

- No commit without explicit permission; the prune's own commit message, when authorised, is exactly `Roadmap prune`.
- Memory is written only on an explicit trigger phrase.
- Handoffs, notes and specs are written in English regardless of the conversation language; the conversation here was Russian and the chat report was Russian, this file is English.
- **A tension to surface, not to resolve silently:** the global discipline holds a chat session to planning only — it does not edit code on its own initiative. But the gate's resolution protocol explicitly authorises `[fixed]`, which means editing skill bodies in place. The resolution session is therefore *not* a plan-only chat, and the authorisation for each in-place fix should be confirmed with the user rather than assumed from the protocol. In this repo the "code" being fixed is skill bodies and docs, which makes the boundary blurrier, not clearer.
- Reserved-words conformance binds skill bodies, skill descriptions and the system docs — not the free prose of a review entry or of this handoff. Do not "fix" an observation's wording on vocabulary grounds; pin it or dispose of it.

## 10. Cross-cutting contracts / invariants checklist

**The regeneration command** (verified this session; the single highest-leverage artifact it produced). Run from `/Users/max/projects/sakshi/skills`:

```bash
awk 'FNR==1{s=0} /^## /{s=($0~/^## Deferred observations/); next}
     s && /^[[:space:]]*-[[:space:]]/ && $0 !~ /\[[^]]+\][[:space:]]*$/ {printf "%s:%d — %s\n", FILENAME, FNR, $0}' \
  $(find .ai-factory/plan-reviews .ai-factory/reviews -type f -name '*.md' | sort)
```

Invert the trailing condition to `$0 ~ /\[[^]]+\][[:space:]]*$/` to list what is already pinned. Redirect to a file outside the repo; do not print it into chat.

**The pinned discriminator:** an entry line is pinned when it ends with a bracketed status-marker suffix — regex `\[[^]]+\][[:space:]]*$`, one or more markers, space-separated. Anything else is unpinned.

**The marker vocabulary, exact spellings** — `[fixed]`, `[routed → <path>]` (a Unicode arrow `→`, not `->`), `[dismissed]`.

**Numbers that must stay consistent across any account of this state:**

| Quantity | Value |
|---|---|
| Review files scanned (both genres, repo-wide) | 156 |
| Files carrying a `## Deferred observations` section | 107 |
| Unpinned entries | 169 |
| Files holding at least one unpinned entry | 88 |
| Already-pinned entries | 41 |
| Unpinned entries in canonical `- Affects:` form | 157 |
| Unpinned entries as bare bullets | 12 |
| `[x]` tasks in the roadmap | 53 |
| `[ ]` tasks in the roadmap | 0 |
| `Spec:` tags on task lines | 51 |
| `Phase note:` tokens in phase preambles | 14 |
| Direction headers (`## `) | 30 |
| Phase headers (`### Phase`), numbered 19–49 | 31 |

Two of the 53 `[x]` lines carry no `Spec:` tag — they contribute nothing to the sweep and must never have a path synthesised for them.

**Fixed strings:** stem `trickster77777`; section heading `## Deferred observations`; entry lead `- Affects: `; prune commit message `Roadmap prune`. These are protocol tokens — byte-exact, whatever the surrounding prose does.
