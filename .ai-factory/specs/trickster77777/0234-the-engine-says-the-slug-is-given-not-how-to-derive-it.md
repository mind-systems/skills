# 83.2 — the engine says the slug is given, not how to derive it

## What is true now

`src/skills/roadmap-engine/SKILL.md`, § "Named roadmaps", paragraph **Slug derivation**, reads: "the local-part of `git config user.email`, lowercased, every non-alphanumeric run collapsed to a single hyphen (`john.doe@example.com` → `john-doe`); fallback — slugified `user.name` when email is unset." Every session that loads the engine carries that rule. As 82.1 leaves it, the same section writes the user's placeholder `<user-slug>` in the roadmap path, the spec directory and the test sibling. The same section's **Owner line** paragraph verifies a roadmap's first line, `> Owner: <full email>`, against the current git identity, which is the full email and not the slug.

As 83.1 leaves it, `scripts/user-slug.sh` in the engine's directory prints the bare slug as one line and is the one home of the derivation in the skills' text; as 83.3 leaves setup, the session's hook puts the label `The user's slug: ` before that output.

## What must be true after

In `src/skills/roadmap-engine/SKILL.md`, § "Named roadmaps", the paragraph reads:

"**Slug derivation:** the user's slug is given at session start, as the line `The user's slug: <user-slug>`; a session that holds no such line runs `scripts/user-slug.sh` and takes its output as the slug."

The rule's text, the example and the fallback leave the engine. The rest of the section stands.

## What breaks on contact

**Rule:** a text breaks on this change if it sends a reader to the engine for how the slug is derived.

**Sweep:**
```
grep -rn "Slug derivation" src docs CLAUDE.md
grep -rn "slug/owner mechanics" src docs CLAUDE.md
```

**Finding.** The search for `Slug derivation` returns the engine's paragraph alone, the target. The search for `slug/owner mechanics` returns pointers in `roadmap-decompose`, `roadmap-outline`, `roadmap-test-coverage`, `task-rescue`, `temporal-tree` and `command-pin-gaps` to the engine's "Named roadmaps" section; the section still holds the resolution order, the owner line and the test sibling, so each pointer stays true.
