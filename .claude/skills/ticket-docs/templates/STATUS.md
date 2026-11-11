# <KEY> — Status of <step or topic>

**Legend:** ⏸️ paused · ▶️ resumed · ✅ done / PASS · 🔄 in progress · ⬜ to do · ⏳ waiting · ❌ failed · ⚠️ warning / invalid run · 🚫 out of scope · 💻 local · 🟦 dev stage · 🟪 QA stage

<Newest entry first. A rebase conflict alone does not pause the ticket: say so in one line here ("The ticket is not paused: … goes on in PROGRESS.md") and use the rebase-conflict entry at the end of this template. On resume, add "## ▶️ <date>: resumed — <what changed>" above the pause entry and keep the pause text below as history. Later milestones get their own entry on top ("## ✅ <date>: done — …").>

## ⏸️ <DATE>: <step> paused on <reason in a few words>

**Paused by the owner on <DATE>, <HH:MM>:** "<his words>". Nothing is pushed or deployed after that point.

### In short

<3 to 5 sentences: what is done, what blocks, what is ready to go once unblocked.>

### The issue

**What happens.** ❌ <observed behaviour, with the exact error, stage, run id>. Evidence: [<file>](tests-evidences/<folder>/<file>).

**Cause.** <what is known, with file:line; or "unknown yet: what was ruled out">.

**What it proves anyway.** ✅ <what the failed run still shows works, or "nothing">.

### State left behind

| | Where | Branch / commit | State |
|---|---|---|---|
| <✅ / ⚠️> | 💻 `<repository>` (worktree `<path>`) | `<branch>` @ `<commit>` | <pushed / local only / uncommitted changes, saved as [patch](tests-evidences/<folder>/<name>.patch)> |
| <✅ / ❌ / ⬜> | 🟦 Dev stage `dev` | `<commit deployed>` | <what it runs, last result; who else uses it> |
| <✅ / ❌ / ⬜> | 🟪 QA stage `qa` | `<commit deployed>` | <what it runs, last result; who else uses it> |
| <⏳> | GitHub | — | <status> |

### How to resume

- [ ] ⬜ <prerequisite: `gh auth status`, an answer from …, a permission granted>
- [ ] ⬜ Re-check the stages (`gh run list --workflow stage.yml`): the dev and QA stages may have been taken meanwhile
- [ ] ⬜ <exact step, command>
- [ ] ⬜ <checks to re-run on 💻 / 🟦 / 🟪, and their evidence folders>
- [ ] ⬜ PROGRESS.md and README.md back to the current step

### Open questions

- ⏳ <question, who must answer>

<!-- Rebase-conflict entry (ticket-docs skill, "Rebase conflicts"): copy it at the top of the file, one per conflict. -->

## ❌ <DATE>: rebase conflict on <target branch> in `<file>` (<the dev stage run #n | local rebase | …>)

### In short

<3 to 5 sentences: what stopped, why, how it was resolved, where it stands.>

### Conflict

| | |
|---|---|
| **Detected** | <date time, build number and parameters, branch, commit> |
| **Console** | <the exact lines, e.g. `ERROR_MSG='Conflict => Need manual rebase'`> ([evidence](tests-evidences/<folder>/<file>)) |
| **Effect** | <❌ nothing deployed; what each stage still runs; the remote branch unchanged> |
| **Branch base vs target** | <base commit; the target's commits ahead and the tickets they belong to> |
| **Files** | <`git merge-tree --write-tree --name-only --messages <target> HEAD`: the CONFLICT files, the auto-merged ones; whether the base pull request alone merges cleanly> |
| **Cause** | <which target commit touched the same lines, and how (both appended at the end, a renamed symbol, …)> |

### Resolution

1. <the commands run, local first (GIT-1 allows a local rebase)>
2. **Chosen resolution: <keep both sides | take ours | take theirs | rewrite>.** <why>
3. <⚠️ every mistake made while resolving, how it was caught, how it was fixed, whether it was ever pushed — or "No mistake.">
4. <the commits before and after; the force-push with the owner's yes and its date (GIT-1)>

### Verification

| Check | Result | Evidence |
|---|---|---|
| No conflict marker in the commit | <✅ `grep -c '^<<<<<<<'` = 0> | |
| The resolved file adds exactly the branch's change | <✅ diff size vs the commit before the rebase> | |
| Both sides present (when both were kept) | <✅ symbols of each side> | |
| DEP-1, tsc, lint, unit, rule checks on the new base | <✅ counts> | [<folder>](tests-evidences/<folder>/README.md) |
| Pipeline rebase and deploy after the resolution | <🔄 / ✅ build, result> | [<folder>](tests-evidences/<folder>/README.md) |

### State left behind

| | Where | Branch / commit | State |
|---|---|---|---|
| <✅> | 💻 `<repository>` (worktree `<path>`) | `<branch>` @ `<commit>` on `<base>` | <pushed / local> |
| <🔄 / ✅> | 🟦 Dev stage `dev` | `<commit>` | <deploying / runs it> |

### How to resume

- [ ] ⬜ <what is left; the precautions for the next rebase>

