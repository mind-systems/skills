# Handoff — correcting my own previous claim about `allowed-tools`, and one finding that outlives it

> Cross-repo handoff from a consumer project (`~/projects/digital_ocean`), 2026-08-09, second version. **The first version of this file was wrong and is withdrawn — its text is replaced by what follows.** It claimed the whitespace form of `allowed-tools` was undocumented and asked for a sweep of `src/skills/`. Both renderings are documented; no sweep is warranted. Two things survive: one defect this repository already knows about, and one it does not — twenty of twenty-one skills here cannot be packaged or uploaded.

## 1. Withdrawn: the syntax claim

The first version asserted that `allowed-tools` accepts only comma separation and `Bash(cmd:*)` patterns, that the whitespace form traced to a third-party generator's specification, and that this family had propagated a mistake across twenty files.

The official documentation says otherwise, and I should have opened it before writing:

> `allowed-tools` — Tools Claude can use without asking permission during the turn that invokes this skill. The grant clears when you send your next message. **Accepts a space- or comma-separated string, or a YAML list.**

Its own normative example is whitespace-separated with space-wildcards, the exact form this family uses:

```yaml
allowed-tools: Bash(git add *) Bash(git commit *) Bash(git status *)
```

**And the field's meaning was also stated backwards.** It grants, it does not restrict:

> It does not restrict which tools are available: every tool remains callable, and your permission settings still govern tools that are not listed.

The restricting field is `disallowed-tools` — "Tools removed from Claude's available pool while this skill is active" — which nothing in this family currently uses, and which is the field to reach for if a skill should genuinely be prevented from calling something.

**How the error happened, since this repository runs the same investigation pattern.** I surveyed installed skills and read a reference document, and treated both as specifications. The reference was `plugin-dev/skills/command-development/references/frontmatter-reference.md` — commands inside one plugin, which documents two forms and simply omits the third. The survey was house style. Separately I grepped the shipped bundle for a sentence a reviewer had quoted, found it, and treated finding the string as confirming what it described — without establishing which field the sentence belonged to. None of that is a source. The page at `code.claude.com/docs/en/skills` settles every one of these questions in two paragraphs.

## 2. Survives: the scanner only catches one dialect

`upstream/ai-factory/aif-skill-generator/scripts/security-scan.py:127` flags unrestricted shell with:

```python
r'(allowed-tools|allowed_tools)\s*:\s*.*(Bash\s*$|Bash\s+[^(])'
```

Both alternatives assume whitespace separation. `Bash\s*$` catches a trailing bare `Bash`; `Bash\s+[^(]` catches `Bash` followed by whitespace then a non-paren. In the comma form — equally valid — a bare grant reads `allowed-tools: Bash, Read`: after `Bash` comes a comma, not whitespace, and it is not end of line. **Neither alternative matches, and the scanner passes a skill requesting unrestricted shell.**

This is unaffected by §1. Whichever dialect a skill uses, the check should catch a bare `Bash`, and today it catches it in one.

Worth noting what a bare `Bash` now means, given the field grants rather than restricts: it pre-approves *every* command for the whole invoking turn. That is a larger hole than it appeared under the wrong reading, which makes the scanner gap worth closing rather than deferring.

## 3. New: twenty of twenty-one skills here cannot be packaged or uploaded

This one did not come from the original investigation and is not affected by its errors. Same documentation page:

> Claude Code accepts every field in the table above. Outside Claude Code, you can use only the fields in the Agent Skills spec.

| Distribution path | Fields allowed |
|---|---|
| Claude Code skills at any level, including plugin skills | every field |
| claude.ai uploads, the Skills API, packaging with `package_skill.py` | `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` |

> If you include any field the spec doesn't allow, packaging or upload **fails with a hard error** instead of ignoring the field:
> ```
> Unexpected key(s) in SKILL.md frontmatter: argument-hint. Allowed properties are: allowed-tools, compatibility, description, license, metadata, name
> ```

Counted across `src/skills/` just now — frontmatter keys in use, against the six the spec permits:

| Key | Files | In the spec's six |
|---|---|---|
| `name` | 21 | yes |
| `description` | 21 | yes |
| `allowed-tools` | 18 | yes |
| `argument-hint` | 16 | **no** |
| `disable-model-invocation` | 15 | **no** |
| `loads` | 10 | **no** |
| `user-invocable` | 7 | **no** |
| `metadata` | 1 | yes |

**Twenty of twenty-one skills carry at least one field outside the spec.** All of them load correctly in Claude Code, which accepts every field — so nothing is broken today. But `CLAUDE.md` here documents `npx skills publish <path>` as this repository's publishing step, and the failure mode on that path is a hard error, not a silently dropped key.

This is a real fork rather than a defect, and it belongs to this repository, not to me: either publishing is not actually a goal for these skills and the extra fields stay, or it is, and the four Claude Code-only fields need somewhere else to live. `loads:` is the interesting one — it is this family's own invention, it carries the dependency graph the architecture depends on, and it has no home in the spec's six. Worth deciding deliberately rather than discovering at the first publish.

## 4. What is not asked for

No sweep of `src/skills/`, no change to any `allowed-tools` value, no change to what any skill may do. §1 withdrew all of that. §2 is one regex. §3 is a decision, and its answer may well be "we do not publish these, leave it".

The consumer project's own task, for the record, has stopped changing `allowed-tools` at all: its two skills keep the value they already had, and the only guard it retains is against a bare `Bash` — grounded now in the grant reading, where a bare grant means every command runs unprompted for the turn.
