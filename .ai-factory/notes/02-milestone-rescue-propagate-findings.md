# milestone-rescue: Propagate Findings to Open Milestones

**Date:** 2026-04-11
**Source:** conversation context — tradeoxy_gui / neiry_kit exploration session

## Key Findings

- After rescuing a failed milestone, the skill stops — but the root cause issues (recurring gotchas, mechanical error patterns, scope gaps) often apply to other open milestones of the same type.
- A "do NOT do X" constraint discovered from a failed bridge milestone is almost certainly missing from sibling bridge milestones that haven't run yet.
- The skill should add a Step 5.5 that scans remaining open milestones for the same gaps and proposes propagating fix clauses.

## Details

### The gap

`milestone-rescue` currently:
1. Reads failed artifacts
2. Classifies failure mode
3. Extracts issues
4. Proposes update to the failed milestone
5. Cleans up artifacts → **stops**

Missing: cross-milestone propagation of findings.

### Concrete example (neiry_kit)

`DeviceLocatorBridge` failed because of a threading gotcha: "use `NewLocalRef` under lock, not raw pointer copy — prevents use-after-free if `DeleteGlobalRef` runs concurrently". After rescue, this clause was added to `DeviceLocatorBridge`.

But `NfbBridge`, `EmotionsBridge`, `CardioBridge`, `ProductivityBridge` — all open at the time — had the same pattern in their descriptions without the constraint. Each subsequently failed for the same reason.

If the skill had propagated the finding after the first failure, 4 subsequent failures would have been prevented.

### Proposed Step 5.5

After applying the ROADMAP.md update:

1. Scan all remaining `- [ ]` milestones in ROADMAP.md
2. For each **recurring** or **mechanical-error** issue from Step 3: check if any open milestone touches the same files, APIs, or patterns
3. If matches found, present a single question:

```
These open milestones may have the same gaps. Apply the same fix?

→ MilestoneA: + <proposed clause>
→ MilestoneB: + <proposed clause>

Options:
1. Apply all
2. Review each individually
3. Skip
```

### Signal strength

- **Recurring issues** (appeared in 2+ rounds of the failed milestone) → highest priority to propagate; the implementer couldn't fix it even with a patch, meaning the description is the only reliable enforcement mechanism
- **Mechanical errors** → propagate to milestones with similar patterns (same bridge type, same threading model, same API family)
- **Specification gaps** → propagate only if the open milestone is in the same domain

### Skill file to update

`/Users/max/.claude/skills/milestone-rescue/SKILL.md` — add Step 5.5 between the current Step 5 (apply + clean up) and the end of the workflow.
