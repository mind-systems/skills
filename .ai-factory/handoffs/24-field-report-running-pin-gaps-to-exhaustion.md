# Handoff — field report: running the gap pass to exhaustion, and what the loop looked like doing it

**Processed:** `[]` — whoever reads this marks it; a marked handoff is spent.

A field report from a project that runs the paired loop daily. It carries no state you need and no request. One long session planned two roadmap phases documentation-first, then walked every one of their tasks into the code with `command-pin-gaps`, one task at a time, to exhaustion. That is an unusual amount of one skill run under controlled conditions, and what it turned up says something about several skills and about the loop itself.

Everything below happened. Where a claim is about a skill, it is about the skill as written, checked against what the run actually did.

## The highest-yield lens in the run is in none of the skills

`command-pin-gaps` names three hole classes — value, meaning, blast-radius. Mid-run the user added a fourth check by hand, and it outproduced all three:

> Watch that superseded or rejected material does not survive inside a task as though it were ratified.

It has two shapes, opposite in direction. **Prose stating as law a model the task deletes** — a rename changes types and the comments around them keep describing the old shape, so the file argues with its own code. And **a decision the governing documents already made, offered by the spec as a suggestion** — "recommended", "may be revised during implementation", "this task's own choice" — which invites an implementer to re-decide what is not theirs.

The two worst findings of the whole run were both this class, and neither is a value, meaning or blast-radius hole under the current definitions:

A task that deletes a symmetric rendezvous model left the canonical proto tree's own header comment stating that model as law — *"matched to the waiting registration by subscription_id, in either arrival order"* — in the file that a **different** task's spec points its implementer at as ground truth, in a repository whose sibling has never built its half and would have had that handoff as its only account. No task in the roadmap touched that comment: the deleting task's scope was one source directory, and the proto tree is not in it.

A spec offered its refusal answer as "this task's own choice… may be revised if a closer precedent surfaces during implementation" while the governing REST document had already ratified exactly that answer. The hedge and the ratification sat one file apart.

The generalisation worth carrying into the skill: **a task that changes a shape owns the prose that describes that shape, and the carriers are routinely outside the directory the task edits** — a types file the spec never names, a proto tree, a test file's header, a class docstring. Nothing compiles prose and no test reads it.

## Three corollaries the gap pass's own rules are missing

**Enumeration beats description — and the assertions that rot are the negative ones.** The rule that a blast-radius hole is repaired by "a sweep whose enumeration goes into the task spec, never a sentence saying something may need updating" was the single most productive line in the skill. Twice it cost whole files that a descriptive clause would not have led anyone to. But it needs a corollary the run discovered the hard way: **when a change removes a collaborator, the assertions that break are the negative ones, and they go vacuous rather than red.** Two suites asserted `expect(mock.method).not.toHaveBeenCalled()`. After the change nothing calls that mock at all, so both keep passing while testing nothing, and they read green in every report. A failing test is visible; a silently vacuous one is not.

**A requirement can be unsatisfiable in the code it lands on.** A spec was given a logging requirement — record the cause of a stream-acquisition failure. The handler's `catch` binds no error at all. Pinning *what to record* without checking *what is in scope to record it from* leaves an implementer choosing between an unannounced shape change and a quietly weaker line — and the weaker line is likelier, because it still satisfies the sentence. The pass should ask, for any requirement it pins, whether the values it names are reachable where it lands.

**Verifying a spec's evidence is not verifying its instruction.** On a task whose subject was inaccurate comments, four of five cited sites were checked for drift and the fifth's quote confirmed — while the *repair text* for that fifth was itself wrong and would have had the implementer write a fresh untrue comment. Both halves of every item need checking: is the claim still true, and would doing what it says be right.

## A rename's unit is the vocabulary, not the type

One task renamed a field that turned out to be declared by several structurally independent types — an exported interface, a resolved type, two inline value types in constant maps, and a local interface in a consuming service. The spec renamed one and leaned on a type-check pass as its completeness argument. Against independent declarations the compiler is not a witness: a green build is compatible with most of the names surviving, producing exactly the half-converted vocabulary the task existed to retire.

The question that catches it is not "who reads this name" but **"how many places declare it"**. Reads are pulled along by the compiler; declarations are not. Worth stating wherever a pass judges a rename.

## Section numbers are position addresses, and we did not notice

The project's reference rule forbids `file:line` and we spent a large part of the session purging it. Meanwhile the deciding half cited a governing document's section by number, consistently and **wrongly**, all session — the rule it kept pointing at lived one section over — and it propagated into contract lines, several task specs, a handoff and the shared buffer before the applying half caught it while writing against the document rather than from memory.

The repair the user ruled is not better numbering: **the name alone, no number.** A citation now reads as the section's title or the bolded rule it names. The reason is not rot — nothing had been renumbered — it is that a wrong number looks exactly like a right one, while a wrong title does not. Any skill that holds the address-by-name rule should say that `§ N` is the same defect as `file:line`, because we plainly did not read it that way.

## `note`'s numbering fights the directories it writes into

`note` writes a four-digit zero-padded prefix. Two directories in the project it was asked to write into are numbered unpadded — the task-spec directory and the handoffs directory, this file's own included. Minting through `note` would drop `0139-…` beside `138-…`.

That makes `roadmap-outline-deep`'s instruction — "invoke `note` only for a phase that has no pointer yet" — impossible to follow literally without corrupting the destination's convention, so the applying half wrote the file directly under `note`'s content contract instead. That is the right call for the file and a defect in the skill. A padding hook, or a rule that the width matches what the destination already uses, would close it.

## `roadmap-outline-deep`'s phase note assumes an order that does not always hold

The skill defines a phase note as *"what decomposition cuts tasks from"* — written from the divergence, ahead of the tasks. One phase here was built the other way: straight from a prune's deferred observations into contract lines, and only then deepened. With the task lines already sitting there, the mining lens took the nearest structured thing and produced one entry per task, keyed by task number.

That is a second home for what the contract lines already say, and it rotted inside a single session — describing two designs that had been replaced and missing two tasks added later. The user's ruling, worth lifting into the skill: **a phase note describes the area of code that diverges and names the documentary surface where one exists; task keys never appear in it, because the contract line is a task's only home.** And when deepening a phase that already has tasks: read the tasks to find the ground, then write the ground — never let the task set become the note's structure.

## The buffer outgrew its own definition

`architect-editor-engine` says deferral entries remain the buffer's primary content. In this run they were a small minority. The settled zone carried the entire working memory of a long session — every ruling, every method lesson — and a **per-task ledger** of what the pass found and closed, appended as each round shut.

That mattered concretely: the applying half was stopped mid-run and a fresh one spawned, carrying none of its predecessor's accumulated history. Everything that survived the transition survived because it was in the buffer. The ledger also stopped the deciding half from re-deriving closed ground, which over fourteen consecutive rounds is a real saving.

Suggestion: name the ledger as a legitimate long-run use of the settled zone. A pass that runs to exhaustion over many units needs somewhere to put per-unit outcomes that is neither conversation nor a shared artifact, and the buffer is already that place in practice.

## On the research round that "carries no second opinion"

`agent-architect` says a report on the architect's own delegated legwork carries no second opinion — the hand answered the head's own question, so agreement is echo rather than evidence. That is right about **judgement**. It reads too strongly for **fact-finding**.

Nearly every best catch in this run came from exactly that round: the deciding half sent a `REPORT-ONLY` asking the other to run the pass independently on one task, walked the same task itself, and reconciled. What came back was not an opinion to be echoed — it was checkable, and it was checked, on the files, every time. Several of those findings the deciding half did not have; several of its own survived the other way; and twice it withdrew its own on the other's evidence.

The distinction that seems to hold: **an echo is a risk when the round asks for a verdict; it is not when the round asks for facts that can be verified independently of who reported them.** Worth a clause, because the current wording discourages the most productive thing the loop did all session.

## What the ceremony cost, and what it was worth

"Nothing closes a round before the report on it exists" was observed strictly through fourteen rounds. It is expensive — the deciding half finishes its own walk and then has nothing publishable, so it spends a turn saying so. What made that tolerable was a habit that emerged rather than being prescribed: **the holding message carries verified raw facts and no verdict.** "The pattern carries the case-insensitive flag" is a fact; "the spec's claim about it is wrong" is the verdict, and only the second has to wait. That kept the user informed without contaminating the other half, and it is the shape worth recommending rather than a bare "still working".

The strict reading did earn itself. In the two rounds where the other half's finding differed from the deciding half's, knowing it had been reached independently is what made the reconcile mean anything.

## Mistakes from this side, named

**Batching the pass across tasks.** The run opened by sending three tasks in one round. The user's correction was immediate and right: each task is an atomic unit and the pass runs on it individually, because a finding that only makes sense beside another task's context is not a finding about the task in hand. Round count is not a cost worth optimising against here.

**Talking myself out of a real finding.** A local interface declaring the same name as the type being renamed was found and dismissed — the file was already in the blast radius, so its usages would follow. An independently declared type is not a usage of another type. The other half found it again and it became the run's most consequential repair.

**Reading only the part of a file the spec pointed at.** A proto's message definitions were verified; the six lines of prose above them were not, and those lines stated the model the phase deletes. When a spec says "read file X as it actually is", that means the whole file, not the part the spec is interested in.

**Over-applying a good rule.** The user's no-counting rule is about a number that can drift out of step with the list it summarises. It was applied to pairs named in the same sentence that counts them, which cannot drift, and precision was lost for nothing. The user's word for it was that we had bent the stick too far. The sharp form: a number goes only when the sentence would still read true after someone adds a member without touching it.

## The one thing worth saying about empty results

One task went through the pass and produced nothing. Both halves checked the two risks that could have sunk it, both risks were real questions, and both closed on the facts. Nothing was written.

Both `command-pin-gaps` and `roadmap-decompose-skeleton` say in passing that most units pass through untouched, and both are easy to read past. It deserves to be louder in each, because the pressure to justify a pass by finding something is real and it is what turns a lens into a habit of finding. Across this run the outcomes were genuinely uneven — one task needed nothing, one needed splitting, one needed a single number deleted, and one needed most of its completeness argument rebuilt. That unevenness is the evidence the lens is working.
