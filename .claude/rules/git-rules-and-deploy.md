# Git and deploy rules

These rules apply to simple-erp. They apply to anyone who commits, pushes, opens a pull request or starts a stage run, people and AI agents alike.

## How this file works

- Each rule has an ID that never changes: `GIT-<n>` for git rules, `DEP-<n>` for deploy rules. Reviews and discussions can cite it.
- New rules are added at the end of their section with the next free ID and a row in the summary table. A rule that is dropped stays in the file, marked **Withdrawn** with the date, so that its ID is never reused.
- Each rule uses the same parts: **Rule**, **Why**, **How to apply**, and a **Check** when one can be run.
- The tracker is GitHub: an issue `#<n>` is the ticket `GH-<n>`, and the project board "simple-erp" holds its status.
- Rules GIT-1 to GIT-7 and DEP-1 to DEP-3 come from the harness this one was adapted from (2026-11-10).

| ID | Rule | Enforced since |
|---|---|---|
| [GIT-1](#git-1--wait-for-authorization-before-squashing-or-pushing) | Wait for authorization before squashing or pushing commits | 2026-11-10 |
| [GIT-2](#git-2--withdrawn) | ~~Never change ars-common-bootstrap from a project~~ **Withdrawn 2026-11-10:** simple-erp has no shared submodule | 2026-11-10 |
| [GIT-3](#git-3--once-the-pull-request-is-open-move-the-issue-to-in-review) | Once the pull request is open, move the issue to **In review** on the project board | 2026-11-10 |
| [GIT-4](#git-4--squash-the-branch-into-one-commit-before-its-pull-request-is-opened) | Squash the branch into one commit before its pull request is opened, after saving its history | 2026-11-10 |
| [GIT-5](#git-5--the-pull-request-description-has-10-lines-at-most-and-is-recorded-in-progressmd) | The pull request description has 10 lines at most, closes its issue, and is recorded in the ticket's PROGRESS.md | 2026-11-10 |
| [GIT-6](#git-6--the-qa-run-starts-only-once-every-previous-step-has-passed) | The QA stage run of a pull request starts only once every previous step has passed, and is announced on the pull request | 2026-11-10 |
| [GIT-7](#git-7--a-pull-request-is-fixed-only-in-its-tickets-own-claude-session) | A pull request is fixed, rebased or pushed only in its ticket's own Claude session | 2026-11-10 |
| [GIT-8](#git-8--branches-follow-gitflow) | Branches follow GitFlow: names, bases, targets, releases, hotfixes and version tags | 2026-11-10 |
| GIT-9 | Reserved: every piece of work is an issue on the board, its Status following the work ([issue #4](https://github.com/gpbcom/simple-erp/issues/4), not written yet) | — |
| [GIT-10](#git-10--a-feature-is-a-parent-issue-made-of-labelled-tickets) | A feature is a parent issue made of tickets (sub-issues); each ticket has exactly one component label, allowed by the feature's family, and follows the ticket format | 2026-11-11 |
| [DEP-1](#dep-1--every-dependency-file-resolves-and-installs-before-a-push-or-a-stage-run) | Every dependency file resolves and installs, on each runtime and platform the pipeline uses, before a push or a stage run | 2026-11-10 |
| [DEP-2](#dep-2--a-version-change-keeps-the-file-and-its-copies-consistent) | A version change regenerates lock files with their own command, and moves every copy of the pin | 2026-11-10 |
| [DEP-3](#dep-3--a-dependency-error-in-a-workflow-log-is-a-failure) | A dependency error in a GitHub Actions log is a failure, even when the job ends green | 2026-11-10 |
| [DEP-4](#dep-4--workflows-pin-their-actions-and-grant-write-permissions-per-job) | Workflows pin every third-party action to a full commit SHA, and grant write permissions per job only | 2026-11-10 |

## Git

### GIT-1 — Wait for authorization before squashing or pushing

**Rule:** do not squash or push commits until the branch owner has explicitly said yes. This includes:
- squashing: `git rebase` with squash or fixup, or `git reset --soft` followed by a new commit;
- pushing: `git push`, and `git push --force-with-lease` after a rebase;
- tags pushed to GitHub, and the release branches' merges into `master`.

You can commit locally without asking.

**Why:**
- A push is visible to reviewers and starts workflows.
- A squash rewrites history. Once it is pushed, it is hard to undo.
- The branch owner decides when the work is ready to be shared and how its history looks.

**How to apply:**
1. When the work is ready, ask first. Show the branch and the remote, the commits that will be squashed, and the message of the resulting commit.
2. Squash and push only after an explicit yes.
3. A yes covers that one squash or push. Ask again for each new one.

### GIT-2 — Withdrawn

**Withdrawn 2026-11-10:** simple-erp has no shared git submodule. The ID is kept so that it is never reused.

### GIT-3 — Once the pull request is open, move the issue to In review

**Rule:** as soon as a ticket's branch is pushed and its pull request is open, move its issue to **In review** in the "simple-erp" project (field **Status**). Do it in the same session, right after opening the pull request. A new push that answers a review or a failed QA run moves it back to **In review** too.

The statuses are: **Backlog**, **Ready**, **In progress** (the branch exists), **In review** (the pull request is open), **QA** (the QA run of GIT-6 is started), **Done** (merged; GitHub closes the issue through "Closes #n").

**Why:** the board tells everyone what waits for a review and which version: the pull request's.

**How to apply:**
1. Check that the push went through and that the pull request is open on the ticket's branch.
2. Set the issue's project item to **In review**: `ticket-docs board <KEY> "In review"`, which reads the board's IDs from `.claude/skills/ticket-docs/conf/github.yaml` and calls `updateProjectV2ItemFieldValue` through `gh api graphql` (the token needs the `project` scope).
3. Write in the ticket's PROGRESS.md the change made, with its date. If it fails (missing `project` scope on the token), say so with the error.

### GIT-4 — Squash the branch into one commit before its pull request is opened

**Rule:** before the pull request of a ticket is opened, the ticket's commits are squashed into **one commit** on top of the target branch. While the pull request is open, the branch keeps one commit: a review fix is folded into it, then pushed with `--force-with-lease`. **Before every squash**, the branch's commits are saved with `ticket-docs history-bundle <KEY>`, so that the order tests → red run → code (TEST-7) stays provable.

**Why:**
- The reviewer reads one change, and `develop` gets one commit per ticket, easy to find and to revert.
- Work-in-progress commits say nothing to whoever reads the history later.
- QA tests exactly one version: the commit of the pull request.

**How to apply:**
1. Commit locally as often as needed. TEST-7 needs at least a tests-only commit before each code commit.
2. When the work is ready: `ticket-docs history-bundle <KEY>`, `git fetch origin`, rebase onto the target, then squash: run `git merge-base HEAD origin/develop`, then `git reset --soft <that commit>` (two commands: `git-gate` refuses a reset whose commit it cannot read).
3. **The owner allows the squash commit**, in their own terminal: `ticket-docs allow-squash <KEY>`, typing back the random code it shows on `/dev/tty`. It writes a one-shot permit for this branch, `HEAD` and staged tree, valid 30 minutes. Only then one `git commit` titled `[GH-<n>] <type>: <summary>` passes `git-gate`, although it adds tests and code together (TEST-7). A Claude session cannot grant the permit by mistake: Claude's Bash has no terminal, `git-gate` refuses `allow-squash` and any command naming the permits folder, and `file-gate` refuses a Write or Edit there.
   **What these barriers stop, and what they cannot:** `git-gate`, `file-gate` and the `/dev/tty` code stop accidents and a Claude session going down the wrong path: a squash without the owner, a permit or an AI cost ledger written by a tool call, `allow-squash` or `raise-cap` run from Claude's Bash (it has no terminal). They cannot stop a deliberate forgery by a process running as the same user, which can write any file and drive a pseudo-terminal: Claude runs as the owner's own user and there is no other account to hold a secret. `ticket-docs check <KEY>` at hand-over, CI and the review are the enforcement of TEST-7 and GIT-4.
4. Before squashing, and again before pushing, ask (GIT-1).

**Check before opening the pull request (or pushing a fix):** this must print `1` (`origin/master` for a hotfix or release target):

```bash
git rev-list --count origin/develop..HEAD
```

### GIT-5 — The pull request description has 10 lines at most and is recorded in PROGRESS.md

**Rule:** the description of a ticket's pull request has **10 lines at most**, blank lines included, and contains `Closes #<n>`. The same text, with the pull request link and the date, is written in the ticket's PROGRESS.md, "Pull request" section, every time it is created or changed. `.github/pull_request_template.md` gives the shape.

**Why:** a reviewer reads a short description. The details (plan, tests, evidence) live in the ticket folder and its archive.

**How to apply:**
1. Write the description first: the issue and its title, what changes and why, how it was tested (with the evidence archive link), what to look at or what is left out. No "see the chat", no secret.
2. Copy it into PROGRESS.md's "Pull request" section, in a ```` ```text ```` block.
3. Open the pull request with that text (`gh pr create --base develop --body-file pr-description.txt`).

**Check before opening or editing the pull request:** this must print nothing:

```bash
awk 'END { if (NR > 10) print "PR description: " NR " lines, 10 at most" }' pr-description.txt
grep -q 'Closes #[0-9]' pr-description.txt || echo "PR description: no 'Closes #<n>'"
```

### GIT-6 — The QA run starts only once every previous step has passed

**Rule:** the QA stage run of a pull request's commit is started, and announced on the pull request, **only once every previous step is complete and successful**:

1. the local checks pass, with their evidence (TEST-8);
2. the dev stage run of the same commit passes (`stage.yml`, stage `dev`), with its evidence;
3. the branch is one commit (GIT-4), pushed (GIT-1), its pull request open with its description (GIT-5), and its CI checks green.

Then:

```bash
gh workflow run stage.yml --ref <branch> -f stage=qa -f ref=<the pull request's head commit>
```

**Ask the owner's explicit yes before starting it**, showing the commit, the pull request and the evidence of each step above: the plan of the repository does not allow a required reviewer on the `qa` environment of a private repository, so this yes is the QA gate. A yes covers one QA run. Once the run is started, post on the pull request a comment whose first line is exactly `QA run: <run URL> on <commit>`, and move the issue to **QA** (GIT-3).

**Why:** the QA run is the release-grade test (full Playwright suite, upgrade test, dependency scan). Started on a commit that failed earlier, it wastes the approver's time and the Actions minutes, and announces a version that is not a candidate.

**How to apply:**
1. Check each step above in PROGRESS.md: every one ✅ with its evidence, on the commit the pull request shows.
2. Start the run, post the comment, update the board.
3. When the run ends, download its reports into `tests-evidences/qa-<date>-<check>/` (TEST-9). The QA row of PROGRESS.md's "Stage validation" is ✅ only with that folder.
4. A new commit (a review fix) gets a new QA run once its own steps have passed again.

**Check after starting:** `gh run list --workflow stage.yml --commit <sha>` lists a `qa` run for the pull request's head commit.

### GIT-7 — A pull request is fixed only in its ticket's own Claude session

**Rule:** every operation on a ticket's pull request (rebase, conflict resolution, a fix for a failed check or stage run, squash, push, the QA run of GIT-6) runs in **the ticket's own Claude session**: the one registered with `pr-watch register <KEY>`. Never in another ticket's session, a new session, a forked one, a headless `claude -p`, a cloud routine or a CI agent. A session open in a terminal is never resumed a second time elsewhere.

**Why:** the ticket's session holds the ticket's context (decisions, reviews, evidence, times) and its rules already loaded. An operation done elsewhere is missing from that history and from the ticket folder, and a second writer on the same transcript corrupts it.

**How to apply:**
- Register the pull request with its session right after opening it (`pr-watch register <KEY>`).
- The PR watcher only detects problems and reopens that session in VS Code with `/pr-watch <KEY>` typed. It never pushes, rebases or changes a working tree, and fetches into `refs/pr-watch/*` only.
- GIT-1 still applies in that session.

**Check before pushing:** `pr-watch status` lists the pull request with the current session (`echo $CLAUDE_CODE_SESSION_ID`) as its owner.

### GIT-8 — Branches follow GitFlow

**Rule:**

| Branch | Starts from | Merges into | Name |
|---|---|---|---|
| `master` | | | What is released. Every commit is tagged `v<x.y.z>` |
| `develop` | `master` | | The integration branch, and the default branch on GitHub |
| feature | `develop` | `develop` (pull request) | `feature/GH-<n>-<slug>` |
| bugfix | `develop` | `develop` (pull request) | `bugfix/GH-<n>-<slug>` |
| release | `develop` | `master` (pull request), then back into `develop` | `release/<x.y.z>` |
| hotfix | `master` | `master` (pull request), then back into `develop` | `hotfix/<x.y.z>-GH-<n>-<slug>` |

- `<slug>` is lower-case words joined by `-`. `<x.y.z>` is the semantic version (`changelog.py next-version` suggests it).
- Nobody commits on `master` or `develop` directly. Every change reaches them through a pull request.
- **A release:** `release/<x.y.z>` from `develop`; `release-notes release <x.y.z>` builds `CHANGELOG.md` (DOC-3); the QA stage runs on the branch; its pull request into `master` is merged; the merge commit is tagged `v<x.y.z>` and the tag pushed (GIT-1), which starts `release.yml`; then `master` is merged back into `develop`.
- **A hotfix:** the same from `master`, with its own issue, version and changelog fragment.
- `harness_core.models.branches.BranchName` reads these names. The harness refuses a branch that starts with a GitFlow prefix but misses its shape.
- GitHub rulesets need GitHub Pro on a private repository, so **the harness enforces this rule**: the `git-gate` hook (`ticket-docs git-gate`) refuses a `git push` of `master` or `develop`, and a commit on either of them. The first push of the two branches (2026-11-10) is the only direct one.

**Why:** each branch's role is in its name, so people, the workflows and the harness's checks all know what a branch may do and where it goes.

**Check before pushing a new branch:** this must print nothing:

```bash
git branch --show-current | grep -vxE 'master|develop|feature/GH-[0-9]+-[a-z0-9]+(-[a-z0-9]+)*|bugfix/GH-[0-9]+-[a-z0-9]+(-[a-z0-9]+)*|release/[0-9]+\.[0-9]+\.[0-9]+|hotfix/[0-9]+\.[0-9]+\.[0-9]+-GH-[0-9]+-[a-z0-9]+(-[a-z0-9]+)*'
```


### GIT-10 — A feature is a parent issue made of labelled tickets

**Rule:** work is planned on GitHub as features made of tickets, like epics and stories.

1. **A feature** is an issue labelled `feature` and exactly one **family** label: `HARNESS`, `SPECS`, `PRODUCT` or `TESTS`. Its tickets are its GitHub **sub-issues**. **A feature is never empty**: it has at least one ticket.
2. **A ticket** is a sub-issue of exactly one feature, with **exactly one component label**: `HARNESS`, `SPECS`, `INFRA`, `BACKEND`, `FRONTEND`, `E2E-TESTS`, `LOAD-TESTS` or `UNIT-TESTS`. The secondary labels `type:*` and `priority:*` stay; there is no `area:*` label.
3. **The family decides the components:**

   | Feature family | Its tickets may be |
   |---|---|
   | `HARNESS` | `HARNESS` only |
   | `SPECS` | `SPECS` only |
   | `PRODUCT` | `INFRA`, `BACKEND`, `FRONTEND`, `E2E-TESTS`, `LOAD-TESTS`, `UNIT-TESTS`, alone or mixed, at the developer's will |
   | `TESTS` | `E2E-TESTS`, `LOAD-TESTS`, `UNIT-TESTS`, alone or mixed: a test campaign of its own |

4. **One ticket, one delivery:** each ticket has its own branch (`feature|bugfix/GH-<n>-<slug>`, GIT-8), pull request, ticket folder and board card. A feature is closed when all its tickets are.
5. **A ticket's title** is `[LABEL] Verb phrase`, the label being its component, under 80 characters: `[BACKEND] Store a customer with its VAT number`.
6. **A ticket's body** has these sections, in this order:

   | Section | Holds |
   |---|---|
   | `## Description` | A user story (`As a <persona>, I want … so that …`, personas from `docs/specs/01-users`) and/or the problems and goals |
   | `## Implementation` | Bullets **Approach**, **Where** (services, front ends, packages, files), **Contracts** (API, entity, configuration, event), **Open questions** |
   | `## Acceptance criteria` | A task list of numbered criteria, `- [ ] **AC1** Given …, when …, then … (<reference>)`, each naming the spec rule or decision it proves, plus non-regression criteria |
   | `## Tests` | A table `ID \| Level \| Proves \| AC`: the tests planned per criterion and level (unit, GUI Playwright, E2E stage, Bruno API); every criterion has at least one |
   | `## References` | A table `ID \| What \| Link`, **at least one**: product and test tickets reference the specifications (`fNN`, `tNN`, `dNNN` decisions, `br-fNN-NN` business rules, `e-fNN-NN` entities, UX screens, non-functional pages, country rules); `HARNESS` tickets reference harness rules (`CS-n`, `GIT-n`, `DEP-n`, `TEST-n`, `DOC-n`) |
   | `## Attachments` | The relevant spec files: images shown inline, Markdown files linked |

7. **Every reference and attachment is a permalink pinned to a commit**: `https://github.com/gpbcom/simple-erp/blob/<40-character commit>/<path>`, so the ticket never changes meaning when the specifications move on.
8. **A feature's body** has the sections `## Goal`, `## Specifications delivered`, `## Out of scope`, `## Tickets`.

The test labels (`TESTS`, `E2E-TESTS`, `LOAD-TESTS`, `UNIT-TESTS`) were added on 2026-11-11 (issue #21).

The machine-readable version of this rule is `.claude/skills/ticket-docs/conf/issue-rules.yaml` (families, components, matrix, title pattern, sections, reference patterns).

**Source:** the owner, 2026-11-11, after an interview on the ticket format; the existing issues were backfilled the same day (features #15 harness, #16 specifications, #17 CI/CD).

**Why:**
- A feature groups the tickets that deliver one goal, and the board shows its progress through its sub-issues.
- One label per ticket says which part of the system it changes; the family matrix keeps harness and specification work apart from product work.
- One format, with references pinned to the specifications, lets anyone check that a ticket implements what was decided, and lets the ticket folder (`ticket-docs create`) take its acceptance criteria unchanged.

**How to apply:**
1. Before any work, find or create the feature, then create the ticket under it from `.claude/skills/ticket-docs/templates/` (until `ticket-docs new-feature` and `new-ticket` exist, issue #18: `gh issue create`, then `gh api -X POST repos/gpbcom/simple-erp/issues/<feature>/sub_issues -F sub_issue_id=<ticket id>`).
2. Write the body in the format above; pin every `docs/specs/…` and `.claude/…` link to the commit it was read at.
3. Put the ticket on the board with its Status (GIT-9, issue #4).
4. Never give a ticket a second component label: split it into two tickets instead.

**Check (until `ticket-docs check-issues` exists, issue #18):** this must print nothing:

```bash
gh api graphql -f query='query{ repository(owner:"gpbcom", name:"simple-erp"){ issues(first:100, states:[OPEN,CLOSED]){ nodes{ number title labels(first:10){ nodes{ name } } parent{ number labels(first:10){ nodes{ name } } } subIssues(first:50){ totalCount } } } } }' --jq '
  .data.repository.issues.nodes[] | ([.labels.nodes[].name]) as $l
  | if ($l | index("feature")) then
      ([$l[] | select(. == "HARNESS" or . == "SPECS" or . == "PRODUCT" or . == "TESTS")] | length) as $f
      | if $f != 1 then "#\(.number): a feature needs exactly one family label"
        elif .subIssues.totalCount == 0 then "#\(.number): empty feature" else empty end
    else
      ([$l[] | select(. == "HARNESS" or . == "SPECS" or . == "INFRA" or . == "BACKEND" or . == "FRONTEND" or . == "E2E-TESTS" or . == "LOAD-TESTS" or . == "UNIT-TESTS")]) as $c
      | if ($c | length) != 1 then "#\(.number): a ticket needs exactly one component label"
        elif .parent == null then "#\(.number): a ticket needs a parent feature"
        else ([.parent.labels.nodes[].name | select(. == "HARNESS" or . == "SPECS" or . == "PRODUCT" or . == "TESTS")][0]) as $fam
          | if ($fam == "HARNESS" or $fam == "SPECS") and $c[0] != $fam then "#\(.number): a \($fam) feature holds only \($fam) tickets"
            elif $fam == "PRODUCT" and ($c[0] == "HARNESS" or $c[0] == "SPECS") then "#\(.number): a PRODUCT feature holds only INFRA, BACKEND, FRONTEND or test tickets"
            elif $fam == "TESTS" and ($c[0] | endswith("-TESTS") | not) then "#\(.number): a TESTS feature holds only E2E-TESTS, LOAD-TESTS or UNIT-TESTS tickets"
            elif (.title | test("^\\[[A-Z0-9][A-Z0-9-]*\\] ") | not) or (.title | startswith("[" + $c[0] + "] ") | not) then "#\(.number): title must start with [\($c[0])]"
            else empty end end end'
```

## Deploy

simple-erp is deployed by GitHub Actions. The stages are ephemeral: `stage.yml` starts the commit's images on a runner, runs the tests and records a GitHub Deployment on the `dev` or `qa` environment. `release.yml` publishes the images and the GitHub Release of a `v<x.y.z>` tag.

### DEP-1 — Every dependency file resolves and installs before a push or a stage run

**Rule:** before you push a branch or start a stage run, check that every dependency file of the repository resolves without a conflict and installs, for every runtime version and platform that installs it: the version the project declares (`.python-version`, `engines`, the image's base), every version a workflow uses, and the platforms of the runner and the images (Linux x86_64, and arm64 when an image targets it). The check covers every file, not only the ones the branch changes.

**Why:** the pipeline installs the files as they are. A conflict stops the stage run before anything is tested, and the unit tests do not catch it when they run from another environment.

**How to apply:** run each resolver from the repository root. Each must succeed:
- uv projects (the root, `services/*`, `packages/*`, `.claude/skills`): `uv lock --check` in each project folder that has a `uv.lock`;
- Node projects (`frontends/*`): `npm ci` then `npm ls --all`;
- images: `docker build` of each image the branch changes.

Run it again after a rebase on `develop`.

### DEP-2 — A version change keeps the file and its copies consistent

**Rule:** when you change the version of a dependency, in the same commit:
1. **A lock file is regenerated, never edited by hand**, limited to the packages that move (`uv lock --upgrade-package <package>`, `npm install <package>@<version>`). The diff shows only those packages and what they require.
2. **Every copy of the pin moves together**: the same dependency declared in several `pyproject.toml` or `package.json` files gets the same version.

Then DEP-1 must pass. Write each move in the commit message: `<package> <old> -> <new> (<reason>)`.

**Why:** a lock file edited by hand loses its consistency with its source, and copies that drift apart make one service run with one version and its neighbour with another.

**Check before committing:** `git diff origin/develop -- '*.lock' '*lock.json'` shows only the packages you meant to move.

### DEP-3 — A dependency error in a workflow log is a failure

**Rule:** after each CI, stage or release run of a branch, search its log for dependency errors. One found means the run failed, even when the job ends green. Fix it under DEP-1 and DEP-2, or, if it is not yours to fix, report it with the log line and record it in the ticket's evidence.

**Why:** some steps go on after a failed install. A run that "passed" can hide an error that blocks the next stage.

**How to apply:** save the log into the run's evidence folder, then search it. This must print nothing:

```bash
gh run view <run-id> --log > <evidence folder>/actions.log
grep -n -E "ResolutionImpossible|Cannot install|conflicting dependencies|No solution found|requires .*, but you have|No matching distribution|Failed to build|ERESOLVE|Conflicting peer dependency|unmet peer|ERR_PNPM_" <evidence folder>/actions.log
```

### DEP-4 — Workflows pin their actions and grant write permissions per job

**Rule:** in `.github/workflows/`:
- every third-party action is referenced by its full 40-character commit SHA, with its version as a comment: `uses: docker/login-action@<sha> # v3.7.0`. A tag or a branch (`@v3`, `@main`) is never used. Dependabot (`github-actions`) proposes the new SHAs;
- the workflow-level `permissions` are read-only (`contents: read`); a job that writes (packages, contents, deployments, issues) declares exactly what it needs at job level.

**Source:** 2026-11-10, a security review of this repository's first workflows: actions referenced by tag in jobs holding `packages: write` and `contents: write`.

**Why:** a tag can be moved to other code by whoever controls the action's repository, and that code then runs with the job's token. A SHA cannot change. Per-job permissions keep a compromised step from writing where its job never needed to.

**Check before committing a workflow:** this must print nothing:

```bash
grep -nE '^\s*(- )?uses:\s' .github/workflows/*.yml | grep -vE '@[0-9a-f]{40}( |$)|uses:\s*\./'
```

