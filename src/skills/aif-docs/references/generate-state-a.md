# State A: Generate from Scratch

#### 2.1: Analyze project for documentation topics

Explore the codebase and identify documentation topics:

```
Always include:
- getting-started.md    (installation, setup, quick start)

Include if relevant:
- architecture.md       (if project has clear architecture: services, modules, layers)
- api.md                (if project exposes API endpoints)
- configuration.md      (if project has config files, env vars, feature flags)
- deployment.md         (if Dockerfile, CI/CD, deploy scripts exist)
- contributing.md       (if open-source or team project)
- security.md           (if auth, permissions, or security patterns exist)
- testing.md            (if test suite exists)
- cli.md                (if project has CLI commands)
```

**Ask the user:**

```
I've analyzed your project and suggest these documentation pages:

1. getting-started.md — Installation, setup, quick start
2. architecture.md — Project structure and patterns
3. api.md — API endpoints reference
4. configuration.md — Environment variables and config

AskUserQuestion: Would you like to generate these documentation pages?

Options:
1. Generate all of these
2. Let me pick which ones
3. Add more topics
```

**Based on choice:**
- Generate all → proceed to generate README.md and all listed doc files in the resolved docs directory
- Let me pick → present each topic for individual approval, generate only approved
- Add more topics → ask what additional topics to include, confirm final list, then generate

#### 2.2: Generate README.md

Structure (aim for ~80-120 lines):

```markdown
# Project Name

> One-line tagline describing the project.

Brief 2-3 sentence description of what this project does and why it exists.

## Quick Start

\`\`\`bash
# Installation steps (1-3 commands)
\`\`\`

## Key Features

- **Feature 1** — brief description
- **Feature 2** — brief description
- **Feature 3** — brief description

## Example

\`\`\`
# Show a real usage example — this is where users decide "I want this"
\`\`\`

---

See [documentation](<readme-to-docs-dir>/) for full docs.

## License

MIT (or whatever is in the project)
```

**Key rules for README:**
- Logo/badge line at the top (if project has one)
- Tagline as blockquote
- Quick Start with real installation commands (detect from package manager)
- Key Features as bullet list (3-6 items, scannable)
- Real usage example that shows the "wow factor"
- Single pointer line to the docs directory (no index table)
- License at the bottom
- **NO long descriptions, NO full API reference, NO configuration details**

Then update the CLAUDE.md Documentation Index — see the body's "Update the CLAUDE.md Documentation Index" section.

#### 2.3: Generate documentation files in the resolved docs directory

For each approved topic, create a doc file:

```markdown
# Topic Title

Content organized by subtopic with headers, code examples, and tables.
Keep each section self-contained.
```

Content guidelines per topic → read `topic-guides.md` when generating State A pages.
