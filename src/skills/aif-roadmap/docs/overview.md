# aif-roadmap — Overview

## What it does

Creates and maintains `.ai-factory/ROADMAP.md` — a strategic list of milestones for
a project. Each milestone is a high-level capability, not a granular task. Tasks live
in plans (`.ai-factory/plans/`); milestones live in the roadmap.

---

## ROADMAP.md format

```markdown
# Project Roadmap — project-name

> one-line project vision

## Milestones

- [ ] **Feature name** — short description of what this achieves
- [ ] **Feature name** — short description
- [x] **Feature name** — short description (completed)
```

No `## Completed` table. Completed milestones stay in the list marked `[x]` until
`roadmap-prune` runs and moves them into ARCHITECTURE.md as features with commit hashes.
The roadmap is not a history log — it is a forward-looking list with a short trail of
recently closed items for context.

---

## Relationship to other skills

```
aif-roadmap    → writes milestones into ROADMAP.md
aif-plan       → takes a milestone and creates a detailed task plan
roadmap-prune  → collapses [x] milestones into ARCHITECTURE.md features with hashes
temporal-tree  → reads those hashes to reconstruct decision context from git
```

`aif-roadmap` is the top of the chain. It does not know about commit hashes or
ARCHITECTURE.md — that is `roadmap-prune`'s concern.

---

## Milestone granularity

A milestone answers: "what capability did we add to the system?"

Too granular (task-level):
- ❌ Add `exchangeId` field to `Subscription` model
- ❌ Update factory callers to pass `subscription.exchangeId`

Right level (milestone):
- ✅ UserExchange model — per-user exchange accounts with credentials

Too coarse:
- ❌ Trading system

Rule of thumb: if you can deliver it in 1–3 weeks and explain it in one sentence to
a new team member — it's the right size.

---

## Ordering rule

Milestones are ordered by dependency, not priority. If B depends on A being done, A
comes first. This reflects the natural sequence of delivery and makes the roadmap
readable as a narrative: "first we built X, then X enabled Y."

When adding a new milestone, place it after the milestones it depends on.
