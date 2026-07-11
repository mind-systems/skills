# roadmap-engine: named-roadmap contract — resolution, owner line, spec destination

Governing spec: `docs/multiuser-roadmaps.md` — the ratified multiuser design. This task adds its mechanism tier to the engine; where this spec and the ТЗ disagree, the ТЗ wins.

## Current state

`src/skills/roadmap-engine/SKILL.md` knows one fixed default everywhere: the two-tier section pins spec notes to `.ai-factory/specs/<NN>-<slug>.md` and passes destination `.ai-factory/specs/` to `note`'s hook; the maintenance flow's hook (c) says the caller resolves `$TARGET_FILE` but the engine offers no shared resolution for a multiuser project. Nothing defines how "my roadmap" resolves, what guards a named roadmap against a foreign writer, or where a named roadmap's specs land. The family is the mechanism's natural home: ≥2 callers (outline, decompose, skeleton, rescue, pin-gaps, test-coverage) need the identical rule.

## Change

Add one **"Named roadmaps"** section to the engine (mechanism only, no policy):

1. **Resolution order** for the roadmap in play: explicit argument (path or filename) → "my roadmap" when requested — `.ai-factory/roadmaps/<slug>.md` — → default `.ai-factory/ROADMAP.md`. The engine never infers multiuser mode; a caller reaches "my" only when the user asks for it or context names it.
2. **Slug derivation:** local-part of `git config user.email`, lowercased, every non-alphanumeric run collapsed to one hyphen (`kg.wmservice@gmail.com` → `kg-wmservice`); fallback — slugified `user.name` when email is unset.
3. **Owner line:** the first line of every named roadmap is `> Owner: <full email>`, written at creation. Every resolution of "my roadmap" verifies it against the current git identity; mismatch → hard stop naming the owner and the two exits (fix git identity / pass the name explicitly). No silent fallback.
4. **Test sibling:** a named roadmap's test roadmap is `.ai-factory/roadmaps/<slug>-tests.md` — always derived from the roadmap in play, never independently from identity; same owner line, same single-writer.
5. **Spec destination:** a named roadmap's spec notes land in `.ai-factory/specs/<slug>/` — passed through `note`'s existing destination hook; numbering is per-directory as already built. The default roadmap keeps flat `.ai-factory/specs/`.

## Files & types

- edit `src/skills/roadmap-engine/SKILL.md` only.

## Guards

- Defaults byte-stable: a project with no `.ai-factory/roadmaps/` sees zero behavior change; the existing two-tier text and flow steps stay byte-identical apart from the new section and the `<NN>`-scan sentence gaining the named-destination variant.
- `note` is **not** touched — destination is an existing hook value, not a mechanism change.
- Engine stays caller-agnostic: no caller names in the new section (note 38's boundary).
- No orchestrator wording — its roadmap path is an environment setting in its own repo (out of scope per the direction preamble).

## Verification

- The section states all five items above; `grep -n "Owner:" src/skills/roadmap-engine/SKILL.md` hits the contract.
- A dry read of the resolution with no argument and no multiuser request yields `.ai-factory/ROADMAP.md` — the default path is unchanged.
