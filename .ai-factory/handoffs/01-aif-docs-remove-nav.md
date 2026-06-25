# Handoff — aif-docs-remove-nav

## 1. Frame
Remove nav headers and "See Also" footers from `aif-docs` SKILL.md — these constructs
are banned by global CLAUDE.md rules that take precedence over the skill template.

## 2. Read-first map

### Must-read now
- `/Users/max/.claude/CLAUDE.md` — global rules banning nav links and See Also (exact wording there)
- `/Users/max/projects/skills/src/skills/aif-docs/SKILL.md` — the skill to edit; nav/footer rules are in Core Principles 4 and the "See Also" footer in Step 2.3 doc template

### Read on demand
- `/Users/max/projects/orchestrator/docs/*.md` — real docs where the mistake was made and rolled back (the generated nav headers were reverted this session)

## 3. Current state

**Done:**
- Identified the conflict: SKILL.md Core Principle 4 mandates prev/next nav headers; global CLAUDE.md explicitly bans them
- Identified: SKILL.md mandates "See Also" footer on every doc page; global CLAUDE.md explicitly bans it
- Rolled back the nav headers that were incorrectly added to orchestrator docs this session

**In-flight:**
- The SKILL.md itself has NOT been edited yet — nav/footer requirements are still in the skill

**Uncommitted working-tree state:**
- none (orchestrator docs rollback was not committed either — check `git status` in `/Users/max/projects/orchestrator`)

## 4. Next step
Edit `/Users/max/projects/skills/src/skills/aif-docs/SKILL.md`:
1. Remove Core Principle 4 (prev/next navigation header rule) entirely
2. Remove the "See Also" footer requirement from Core Principles
3. Strip nav header lines and "See Also" sections from the doc file templates in Step 2.3
4. Check the Step 4 review checklist — remove any nav/See Also compliance checks there too

## 5. Working discipline
Show diff before applying. The skill file is shared infrastructure — one wrong edit breaks all projects using it.

## 6. Error log
- **Wrong**: added `[← Prev](...)` nav headers and planned "See Also" sections to all 6 orchestrator docs pages, following SKILL.md Core Principle 4
- **Correct**: global `~/.claude/CLAUDE.md` has explicit bans: "No prev/next navigation links. Never add..." and "No 'See Also' sections. Never add...". Global rules override skill templates. The additions were rolled back.

## 9. Hard rules
- Global `~/.claude/CLAUDE.md` overrides skill-level templates — when they conflict, global wins
- No prev/next nav links in any doc file (global rule)
- No "See Also" sections in any doc file (global rule)
