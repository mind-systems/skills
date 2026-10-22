# Plan: 80.3 — The answers become questions, and the rescue pauses on the report

## Context
`src/skills/task-rescue/SKILL.md` still routes a stop into classes and categories, each mapped to a repair depth. Step 3 ends on a set root sentence. Step 4 and § 5.5 then ask the user through `AskUserQuestion` menus, and § "What NOT to do" repeats the steps. This task changes four things:
- Steps 2 and 3 become two facts and five questions.
- Step 4, § 5.5 and § "What NOT to do" are removed.
- The rescue writes its report with the repair and rollback it intends, then stops until the user gives the word in the conversation. Only after that does it apply the repair and rollback and add to the report.
- The frontmatter and the opening paragraphs are updated to match.

The task spec `.ai-factory/specs/trickster77777/0255-the-answers-become-questions-and-the-rescue-pauses-on-the-report.md` is authoritative. Its § "What must be true after" gives the required behaviour but does not pin any text word for word. The after-texts below are drafts. Write them in the skill's existing register and keep the file's hard wrap at about 86 columns. The phase's governing spec is `docs/names-and-reasons-not-laws.md`. Every new sentence must be a name, a reason, a fact or a question. None may be an answer written in advance. Phase note: `.ai-factory/specs/trickster77777/0226-a-rescue-repairs-to-the-root-and-the-root-may-be-something-to-remove.md`.

Assumptions:
- **Narrative sentence that is removed.** Step 3 has a narrative sentence: "Describe what the task spec / contract line stated wrongly or left ambiguous, and how the plan or code went wrong as a consequence". It is removed along with the root sentence. It assumes the root is always a spec defect, which is the same fixed answer the spec removes. Questions 2 to 4 now cover that ground. The prose-form rules for the narrative stay: chronological, round by round, no tables or bullets, findings woven in as evidence, and "may name a round and the reviewer".
- **Two sentences that stay, each in its current step:**
  - In Step 3, the sentence about inconsistent artifact formats ("don't hardcode heading names"). It is a fact about the artifacts, not a routed answer, and the spec's removal list does not include it.
  - In Step 2, the pointer that sends signal semantics to `orchestrator-artifacts`, kept as a single line. It lives only in Step 2, because the escalation fact there reads the last-line signal it defines. Step 3 gets no copy of it.
- **Step 1 wording.** The words "at some repair depths" in Step 1's capture paragraph become "in some rollback states". Under the spec's breakage rule, "repair depths" names a depth choice that no longer exists.
- **Where the intended repair goes in the report.** § 5.7's template gets one new section, `## Intended repair`, placed after `## Who found what`. The first write must hold the intended repair and rollback beside the diagnosis and the finders section, and the template is "given literally". The answer to question five (open tasks carrying the same gap) and an escalation's options also go in this section.
- **Intended rollback.** It is one of Step 5's four states, or a statement that the task's state is left as it is. The second case covers, for example, a commit-as-is or an escalation still unresolved. Step 5's four states are not changed.
- **Defect-chain sentence in the narrative is reworded.** Step 3's narrative paragraph says the story is "what the implementation did, what defect the review found, what the fix changed, and what new defect that fix introduced". It is reworded so it describes events without assuming a defect: "what each round did, what its review found, and what the next round changed". The reason is the same one that removes its twin "Describe what…" sentence. A narrative fixed as a defect chain is an answer written in advance, and neither of Step 2's facts produces such a chain: an escalation can have zero review rounds, and a no-diff run has no defect. Two more changes in the same paragraph follow for the same reason:
  - Its opening "Tell the story of the implementation attempt" becomes "Tell the story of the attempt". Most stops happen in planning, before any implementation exists.
  - "Weave reviewer findings from the recurring rounds (2+) into the narrative" becomes "Weave reviewer findings from every round the narrative tells into it". The "(2+)" qualifier is what remains of the deleted "Recurring issues … determine the repair depth" paragraph, and without that paragraph it has no definition. It also presets question 1's answer. A stall where each round brings a new finding (cases `0037`, `0039`, `0044`) would then weave in none of its findings, even though their non-recurrence is exactly the evidence question 1 asks about.
- **"What NOT to do" fences go with no new home.** Three of the section's bullets are not moved anywhere:
  - "Do not keep stale artifacts at the chosen rollback depth" is already carried by Step 5's rollback states, which say what each one deletes.
  - "Do not add implementation details to the task or task spec — keep constraints at the *what* level" fences the logic of a repair.
  - "Do not invent a new rollback procedure or a fifth depth-menu entry" fences menus that no longer exist.

  The task spec's § "What is true now" separates the section's restatements from these fences. The fences go without a home, and the implementer must not move them into Step 3 or Step 5.
- **No outside references.** Nothing outside this file cites Step 4, § 5.5 or this skill's § "What NOT to do" (checked by grep over `src/`, `docs/` and `../orchestrator/`). `orchestrator-artifacts` § "Sidecar fields" still finds the closed set in § "Valid sidecar `step` states", which is untouched.

## Settings
- Testing: no
- Logging: minimal
- Docs: no

## Tasks

### Edit `src/skills/task-rescue/SKILL.md`

- [x] **Move `$TARGET_FILE` resolution and the contract-line locate into Step 1; shorten the governing-spec read**
  Files: `src/skills/task-rescue/SKILL.md`
  In § "Step 1 — Discover artifacts", replace the paragraph headed **Read the phase's governing spec and phase note.** with two short paragraphs. Place them before **Capture the report facts.**, because the sidecar bullet there says "`$TARGET_FILE` is already resolved above".
  1. **Resolve `$TARGET_FILE` and locate the task.** If an explicit argument names a file, use `.ai-factory/<that file>`. Otherwise use the roadmap in play, as `roadmap-engine`'s "Named roadmaps" resolution gives it. The roadmap in play is the one whose contract line carries the slug. Read it and locate the contract line that matches the slug. Do not carry over Step 4's test-sibling guess from keywords.
  2. **Read the governing spec and phase note**, in one sentence: the rescue locates the task's phase in `$TARGET_FILE` and reads in full every document that the phase header or intro names as `Governing spec:` or `Phase note:`. Drop the guards: "unconditional, not suspicion-based", "proceed as today", "additive to Step 4's…", and the missing-file sentence.

  Keep "ask the user which task to rescue" in the slug paragraph as it is. In **Capture the report facts.**, change "at some repair depths" to "in some rollback states". Leave the rest of Step 1 untouched, including the capture bullets and **Read every artifact file found**.

- [x] **Rewrite Step 2 as the two facts** (depends on Move `$TARGET_FILE` resolution…)
  Files: `src/skills/task-rescue/SKILL.md`
  Retitle the step with a heading that promises no depth, e.g. `## Step 2 — What a stop can look like`. Replace the body:
  - Remove the "internal routing signal" framing.
  - Remove all five classifications (Escalated, Plan-phase, Implement-phase, Stale implementer session, Non-convergence), each with its depth routing.
  - Remove the lightweight-severity paragraph and its "state the diagnosis … in this order" instruction.

  New body:
  - One line saying that signal semantics (`PLAN_REVIEW_PASS`, `REVIEW_PASS`, the last-line requirement) are defined in `orchestrator-artifacts`.
  - Two facts, stated as facts with their reasons and nothing that routes to a repair:
    1. **An escalation is read first.** An escalating agent (planner, implementer, or either reviewer) writes `ESCALATION` on the last line of the artifact it owns. For a planner or an implementer, that artifact is the plan file, possibly with no plan-review on disk. The sidecar reads `step: escalated`, and the missing decision is in the artifact's escalation section. Read this before anything else: otherwise a plan with no plan-review reads as unfinished planning.
    2. **A resumed implementer can return with no diff.** Every review then reports the product files identical to HEAD, although the plan was ratified. No spec, plan or code defect exists. The gap is in the pipeline's record of the attempt.

- [x] **Rewrite Step 3 as five questions, the narrative, the intended repair and the stop** (depends on Rewrite Step 2 as the two facts)
  Files: `src/skills/task-rescue/SKILL.md`
  Retitle the step with a heading that promises no depth, e.g. `## Step 3 — Ask the stalled task`.

  Keep:
  - The opening sentence about scanning every artifact for problems and improvement requests.
  - The sentence about inconsistent formats and not hardcoding heading names.

  Remove:
  - The "Recurring issues … determine the repair depth" paragraph.
  - The root-cause categories list and the escalation-not-in-list note.
  - The paragraph that judges findings against the governing spec and phase note.
  - The "dominant root cause … carry into Step 4" sentence.
  - "printed before the Step 4 depth menu".
  - The stale-implementer and escalation special forms.
  - The "Describe what the task spec / contract line stated wrongly…" sentence (see Assumptions).
  - The root-cause sentence paragraph.
  - The "Attach the root-cause category…" paragraph.

  New body, in order:
  1. **The five questions**, put to the stalled task. Say that the rescue answers them by reading and that none of them routes to a repair:
     1. Does the same finding recur, or is it a new one each round while severity falls?
     2. Did the spec leave the planner something to decide or enumerate?
     3. Is anything the spec says false of the code, or did its own text (a check or a fence) cause the findings?
     4. Should the task exist as written, and is the system ready for it?
     5. Do open tasks below carry the same gap?
  2. **The diagnosis**, kept in its prose form: a chronological narrative, round by round, in complete sentences, with one short paragraph per round as the natural shape. Its length scales with the number of rounds. Findings are woven in as quotes or paraphrases. No tables and no fragment-style bullets. It may name a round and the reviewer. It no longer ends on a fixed sentence.

     Reword the sentence "Tell the story of the implementation attempt as a sequence of events — what the implementation did, what defect the review found, what the fix changed, and what new defect that fix introduced — round by round" so it describes events without assuming a defect or an implementation, e.g. "Tell the story of the attempt as a sequence of events — what each round did, what its review found, and what the next round changed — round by round".

     Also replace "Weave reviewer findings from the recurring rounds (2+) into the narrative as quotes or paraphrases, as evidence" with "Weave reviewer findings from every round the narrative tells into it as quotes or paraphrases, as evidence". See Assumptions for both changes.
  3. **The intended repair.** The rescue decides the repair and the rollback state it intends. If the stop escalated, the report tells it as a decision for the user, with its options.
  4. **First write of the report.** Keep the existing **Write the durable report.** paragraph, which is made per § "Step 5.7 — Write the durable report" through `note`, and keep the returned path. There is one exception: its opening clause "Step 3 ends with the first write of the durable report." becomes "Step 3 makes the first write of the durable report." The step now ends on the stop in item 5. Add that this first write holds the diagnosis, the section on who found what, and the intended repair and rollback. § 5.7's "The first write happens at the end of Step 3" stays true and is not changed.
  5. **The stop.** The rescue then stops. In the conversation it says where the report lies and that it waits for the user's word. The diagnosis lives in the report, not in the chat. Prescribe no question form and no menu.

- [x] **Delete Step 4 and § 5.5** (depends on Rewrite Step 3…)
  Files: `src/skills/task-rescue/SKILL.md`
  - Delete the whole § "Step 4 — Choose repair depth", from its heading to the `---` before Step 5. Its resolution and contract-line locate now live in Step 1.
  - Delete the whole § "Step 5.5 — Propagate findings to open tasks" with its trailing `---`.
  - Keep the names and numbers of the later steps (5, 5.6, 5.7) as they are.

- [x] **Open Step 5 on the user's word and drop the option-keyed paragraphs** (depends on Delete Step 4 and § 5.5)
  Files: `src/skills/task-rescue/SKILL.md`
  - Replace Step 5's opening sentence ("applies the repair Step 4's choice names…") with this: on the user's word, Step 5 applies the repair the report intends and rolls the task back to the state it names, as that word steers them. Applying a clause to an open task the report names under question five is part of what the word releases.
  - Delete the four paragraphs keyed to options, each with its `---` separator: **Non-convergence:**, **Escalated — option 1**, **Escalated — option 2**, **Escalated — option 3**.
  - Leave **Deleting files.**, **Writing the sidecar.**, **Rollback states.** and § "Valid sidecar `step` states" untouched.

- [x] **Update § 5.6's pin timing** (depends on Open Step 5 on the user's word…)
  Files: `src/skills/task-rescue/SKILL.md`
  In § "Step 5.6 — Pin disposed observations", change one sentence: "Pin at the moment of the judgment — routing or dismissal — not at session end." It says instead that a pin is written when the repair is applied, on the user's word, and not at the moment of a judgment made before it. With the pause in place, the judgment can come in Step 3, before the word that releases every other write. Leave the rest of § 5.6 as it stands.

- [x] **Update § 5.7 for the intended repair and the post-repair section** (depends on Update § 5.6's pin timing)
  Files: `src/skills/task-rescue/SKILL.md`
  - In **Extending the file.**, rewrite the sentence about the repair's section without the word "first". It becomes "the section appended once the repair is done, on the user's word". That section records what the repair did, the rollback state the task was left in, and what was deleted or kept. Remove "the depth chosen, the escalation option taken, or the non-convergence choice made".
    - The reason: while the rescue waits, the user's and a head's readings are appended under their dates before the repair. The rescue report of this very task (`rescue-reports/skills/10-80-3-…`) holds such a section ahead of the repair's. So "first" would be false, and it could be read as forbidding appends during the pause.
    - Keep the paragraph's last sentence ("When the first write returned no path…, nothing is appended…") as it is, because it is about the first write, not the first append.
  - In the template, after `## Who found what` and its bullet, add:
    ```
    ## Intended repair

    <the repair the rescue intends, and the rollback state it intends — one of Step 5's
    four, or that the task's state is left as it is; for an escalation, the decision and
    its options; the open tasks below that carry the same gap, each with what it would gain>
    ```
  - In the paragraph after the template, cut "The title phrase names what stopped the run, never a root-cause claim — a branch that produces no root cause still needs a title" down to "The title phrase names what stopped the run, never a root-cause claim." Delete the next sentence in full ("Where Step 3 produced no root-cause sentence and no category — … invented to fill it.").
  - In the finders paragraph after the template, name the finders section by its heading. "the finders live only in this section, outside it" becomes "the finders live only in `## Who found what`, outside it", and "The section holds one bullet per finding the diagnosis names" becomes "`## Who found what` holds one bullet per finding the diagnosis names". The new `## Intended repair` then cannot be read as the section meant.
  - In **When the write cannot happen.**, drop "and complete the rescue anyway", so the sentence says "say so plainly to the user" and ends there. This is the whole change: add no resolution of a failed first write, in this paragraph or in Step 3's stop. Keep the rest of the paragraph: never invent a fallback path, never use a directory inside the rescued project, never invoke `note` a second time, never defer the write.
  - Leave the destination and the hooks untouched.

- [x] **Delete § "What NOT to do"** (depends on Update § 5.7…)
  Files: `src/skills/task-rescue/SKILL.md`
  - Delete the `---` before the section, the section heading and all its bullets. The file ends after § 5.7's "When the write cannot happen." paragraph.
  - The section's restatements already live once in the step that acts on each:
    - committed files and other slugs in Step 5;
    - stale artifacts in Step 5's rollback states;
    - reading every round in Step 1;
    - the governing-spec read in Step 1;
    - pinning only what was evaluated in § 5.6;
    - escalation first in Step 2.
  - Its two fences on repair logic ("what, not how" and "no new rollback procedure or fifth menu entry") go with no new home. Do not move them into Step 3 or Step 5 (see Assumptions).

### Frame

- [x] **Rewrite the `description:` and the opening paragraphs** (depends on Delete § "What NOT to do")
  Files: `src/skills/task-rescue/SKILL.md`
  - **`description:`** Say what the skill does now. It reads failed orchestrator artifacts (plans, plan-reviews, code reviews) and writes its report with the intended repair and rollback. It waits for the user's word, then repairs to the depth of the root cause and rolls the task's state back so the orchestrator re-validates from there. Keep the clause that it checks open tasks below for the same gap. Keep the trigger sentence word for word ("PLAN_REVIEW_PASS never achieved", "REVIEW_PASS never achieved", "rescue", "milestone failed", "pipeline stopped"). Stay ≤ 1024 chars; check the length with `wc -c` over the folded text.
  - **Frontmatter:** leave `allowed-tools` (including `AskUserQuestion`), `argument-hint`, `loads:` and `disable-model-invocation` unchanged.
  - **Opening paragraphs:**
    - Keep the tripwire sentence ("how the failure was noticed, not what failed"), with "exhausting its iteration limit" widened so that it covers an escalation, which stops before its budget is spent.
    - Rewrite the subject sentence to name what the rescue looks at: what the stopped task needs, read from the artifacts it left. It fixes neither the root's kind nor its place. The reason is the one Assumptions gives for the removed "Describe what…" sentence: Step 2's two facts say a no-diff run and an escalation are not defects, and question 4 exists because the root may lie above the task. The sentence's tail ("diagnoses how deep that defect reaches (…), and repairs to exactly that depth") says instead that the repair reaches as deep as the root cause, steered by the user's word.
    - In the second paragraph, keep the two-tier sentence. Rewrite "The repair is depth-keyed …" so that it lists no closed reach: a repair may go above the task, for example by putting a phase in front of it, closing a phase, or deleting the task. The source of this reach is cases `0024` and `0038` in the phase note. That is for the implementer only: the skill names no case and no note number. Delete "The user picks the depth; an explicit "fix Y / delete X" overrides."
  - **Load-once paragraphs:** leave both untouched.

- [x] **Run the spec's sweep and reconcile** (depends on Rewrite the `description:` and the opening paragraphs)
  Files: `src/skills/task-rescue/SKILL.md`
  Run `grep -n -E "AskUserQuestion|categor|flag|routing|menu|Step 4|Step 5.5|What NOT" src/skills/task-rescue/SKILL.md`. The only hits allowed are:
  - the `allowed-tools` line;
  - § 5.6's "routing", if the changed sentence keeps it, since it means pinning there;
  - § 5.6's "for `roadmap-prune`'s gate to flag".

  Also grep for these leftovers, which must return nothing: `depth menu|chosen depth|classification|root-cause sentence|Diagnosis Report|option [123]|first appended|Step 3 ends with`. Fix any stray hit in the step that owns it. Confirm that the table of valid states and the four rollback states are byte-identical to HEAD, and that § 5.6 differs only in the one sentence its task changes (`git diff` shows no other hunk inside them).
