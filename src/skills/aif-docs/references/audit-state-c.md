# State C: Improve Existing Docs

#### 2.1: Audit current documentation

Check for:
- **README length** — is it still a landing page (<150 lines)?
- **Missing topics** — are there aspects of the project not documented?
- **Stale content** — do docs reference files/APIs that no longer exist? Conditional on the referent: flag staleness only for surfaces whose code exists; where the code does not exist, the doc is the spec and this check does not apply
- **Broken links** — verify all internal links point to existing files/anchors
- **Consistency** — same formatting style across all docs
- **Legacy README table** — does README still carry a documentation index table? Flag it as a legacy layout and propose moving the index to CLAUDE.md's `## Documentation` section
- **Coordination-trio staleness** — on every run, check README, the CLAUDE.md `## Documentation` index, and ARCHITECTURE.md for drift. Refresh what this skill owns (README length/pointer line, the CLAUDE.md index rows). For ARCHITECTURE.md, check for staleness but do not edit it — it stays read-only here (Step 0, Artifact Ownership); flag any drift found for the user or `aif-architecture` to fix
- **Standards compliance** — does existing documentation match the current skill standards? (see 2.1.1)

#### 2.1.1: Standards compliance check

Check existing docs against current Core Principles for gaps (stale formats). For the full compliance table and auto-fix rules → read `REVIEW-CHECKLISTS.md` (Standards Compliance section).

**When gaps are found**, include them in the audit report alongside content issues (Step 2.2). Treat them as regular improvements — show the plan and get user approval before applying.

#### 2.2: Propose improvements

```
Documentation audit results:

✅ README is lean (105 lines)
⚠️  <resolved docs dir>/api.md is missing — project has 12 API endpoints
⚠️  <resolved docs dir>/configuration.md references old env var DB_HOST (now DATABASE_URL)
❌ <resolved docs dir>/getting-started.md links to setup.md which doesn't exist

Proposed fixes:
1. Create <resolved docs dir>/api.md with endpoint reference
2. Update DATABASE_URL in <resolved docs dir>/configuration.md
3. Fix broken link in <resolved docs dir>/getting-started.md

Apply fixes?
```
