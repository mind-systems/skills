# Skills Roadmap

> Generic AI Factory skills — reusable slash-command packages for Claude Code.

## Milestones

- [x] **roadmap-decompose: enforce atomicity via deployability test** — `roadmap-decompose/SKILL.md` currently states "one atomic task / one concern / one reason to revert" as a declaration but has no enforcement step. The rule is too abstract to apply consistently — concerns slip in through "while I'm here" additions (e.g. adding a service method inside a component task). Fix: add a mandatory **Atomicity Gate** step that runs after each task description is drafted, before it is saved. The gate asks one question: **"Can the first half be deployed without the second half and still make sense?"** — if yes, split into two tasks. This is the only atomicity criterion; drop the file-count and verb-count heuristics as too noisy. Concretely: in Mode 1 (Step 1.3) after drafting each milestone, and in Mode 2 (Step 2.4) after drafting each new task — pause and apply the gate. If the answer is yes, split and apply the gate again to each half recursively until no half is independently deployable. Add this as **Step 1.3.1** and **Step 2.4.1** in the skill body. The gate question and split instruction should appear verbatim in the skill so the agent always uses the same wording.
