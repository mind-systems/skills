# aif-plan Examples

`/aif-plan` takes a single `<description>` argument — there are no mode keywords or
subcommands. It always produces one named plan file at
`.ai-factory/plans/<NN>-<slug>.md`, then stops.

## Argument

```text
/aif-plan Add product search API
-> description="Add product search API"
```

The entire argument is the description. There is no `fast`/`full`/`--parallel`/
`--list`/`--cleanup` parsing, and no branch or worktree is created.

## Flow Scenarios

### Scenario 1: Small feature (fewer than 5 tasks)

```text
/aif-plan Add product search API

-> Step 0:   reads DESCRIPTION.md / ARCHITECTURE.md for context
-> Step 1:   1-2 Explore agents map the relevant area
-> Step 1.2: asks preferences — tests? logging level? docs? constraints?
             (user: no tests, minimal logging, no docs)
-> Step 3:   2-3 Explore agents investigate patterns and integration points
-> Step 4:   TaskCreate — 4 tasks, ordered by dependency, each with file paths + logging
-> Step 5:   saves plan to .ai-factory/plans/03-add-product-search-api.md
             (03 = highest existing NN + 1); no Commit Plan section (fewer than 5 tasks)
-> Step 6:   STOP — user runs /aif-implement when ready
```

### Scenario 2: Larger feature (5+ tasks, commit checkpoints)

```text
/aif-plan Add user authentication with OAuth

-> Step 0-3: context, recon, preferences (tests: yes, logging: standard, docs: yes),
             deep parallel exploration
-> Step 4:   TaskCreate — 8 tasks with blockedBy dependencies
-> Step 5:   saves plan to .ai-factory/plans/04-add-user-authentication-with-oauth.md,
             including a Commit Plan section (5+ tasks -> checkpoints every 3-5 tasks)
-> Step 6:   STOP
```

### Scenario 3: First plan in an empty plans directory

```text
/aif-plan Set up structured logging

-> No numbered files in .ai-factory/plans/ yet -> NN starts at 01
-> saves plan to .ai-factory/plans/01-set-up-structured-logging.md
-> STOP
```
