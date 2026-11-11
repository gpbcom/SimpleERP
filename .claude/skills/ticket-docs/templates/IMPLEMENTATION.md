# <KEY> — Implementation: choices, justification, files

**[PLAN.md](PLAN.md) takes precedence** over this file. "Today" is `<repository>` @ `<base commit>` (<branch>); line numbers are on that commit.

**Not started.** <Or: implemented up to step N, see [PROGRESS.md](PROGRESS.md).>

## 0. Files modified — exact list

The single list of files this ticket touches (PLAN.md points here). Grouped by project, then kind, then path in alphabetical order. Test IDs refer to [TESTS-CATALOG.md](TESTS-CATALOG.md).

**Check G02** (local checks and final step): `git diff --name-only origin/develop` lists exactly the files of §0.1…§0.<n>, nothing else.

### 0.1 `<repository>` — `<stack or folder>` (branch `<branch>`, from `<base commit>`)

| Kind | File | Change | Section | Tests |
|---|---|---|---|---|
| New | `<path>` | <what> | [§2](#2-path) | <IDs> |
| Modified | `<path>` | <what> | | |
| Deleted | `<path>` | <why> | | |

### 0.<n> Outside the PR

<Ticket folder, local tools, scenarios not committed — or "Nothing besides this folder".>

### 0.<n> Checked, unchanged

| Project / file | Why it was checked | Why it stays unchanged |
|---|---|---|
| `<path>` | <reason> | <reason> |

## 1. Implementation choices

One block per technical choice. The ID is the decision's ID in [EXPLAIN.md §6.3](EXPLAIN.md#63-decision-log), which keeps the one-line decision; the reasoning lives only here.

| # | Choice | Status |
|---|---|---|
| D<n> | <one line> | <Proposed | approved by the owner (<date>) | amended by D<m>> |

### D<n> — <short title>

- **Context:** <the problem the code must solve, with file:line today>.
- **Options considered:**
  1. <option> — <pros> / <cons>.
  2. <option> — <pros> / <cons>.
- **Choice:** <option retained>.
- **Justification:** <why it wins: existing code reused (CS-1), contract compatibility, performance, testability, the ticket's rule, the owner's constraint>.
- **Consequences:** <files (§0), tests (IDs), risks (EXPLAIN §6.1 IDs), what becomes harder later>.
- **ACs served:** <AC IDs>.

## 2. `<path>`

**Today** (`<base commit>`, lines <a>–<b>): <what it does>.

**Target:** <what it will do>, following D<n>.

```<language>
// Sketch: shows the intent; the final code follows the repository's conventions.
```

**Deviations** (filled during the implementation, also logged in PROGRESS.md): <none yet>.
