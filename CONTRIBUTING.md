# Contributing to SimpleERP

Thank you for helping. This page says how a change reaches SimpleERP: where to start, which branch to use, how the
roadmap tickets are worked, how to sign your commits and which checks must pass.

Everyone taking part follows the [Code of conduct](CODE_OF_CONDUCT.md). A security problem is never reported in a
public issue: see [SECURITY.md](SECURITY.md).

## Before you start

- **Read the specifications.** SimpleERP is specified before it is built: [docs/specs/](docs/specs/README.md) holds
  the vision, the features F1 to F25, the technical capabilities T1 to T13, the decisions and the roadmap. A change
  implements what they say; a change of behaviour starts with a change of the specification.
- **Find or open an issue.** Roadmap work is a ticket of the GitHub project **SimpleERP roadmap**. A bug report or a
  feature request uses one of the [issue forms](https://github.com/gpbcom/SimpleERP/issues/new/choose); a maintainer
  approves it before anyone works on it.
- **Read [AGENT.md](AGENT.md).** It is the rulebook for code: layout, layers, file shape, typing, naming, docstrings,
  exceptions, logging, models and tests.

## Branches (GitFlow)

`develop` is the default branch and holds the next release; `master` holds the releases. Both change only through pull
requests, merged with a merge commit. Nobody commits on them directly.

| Branch | Starts from | Goes to | For |
|---|---|---|---|
| `feature/<name>` | `develop` | `develop` | A new capability or a change |
| `feature/tickets` | `develop` | `develop` | The roadmap tickets worked by the harness, shared by every running ticket |
| `feature/harness-<name>` | `develop` | `develop` | A change of the Claude Code harness |
| `bugfix/<name>` | `develop` | `develop` | A fix of something not released yet |
| `release/<version>` | `develop` | `master`, then back to `develop` | A release, made by the release workflow |
| `hotfix/<name>` | `master` | `master`, then back to `develop` | An urgent fix of a released version |

The `gitflow` workflow checks every pull request: the branch is a GitFlow branch, it targets the right base, and a
ticket's title starts with its ID (`T2.04: ...`). Once per clone, turn on the git hooks that refuse the rest:

```bash
python3 .claude/scripts/tickets/tickets.py setup
```

## How a roadmap ticket is worked

Roadmap tickets have IDs `T<phase>.<nn>` (`T2.04`) and are built by Claude Code agents under the rules of
[.claude/rules/tickets.md](.claude/rules/tickets.md). A person approves twice:

1. `/ticket-plan T2.04` writes `docs/tickets/T2.04/TICKET.md`, from the specifications only, and a task graph in
   `PLAN.md`, then stops.
2. The person reads the plan and sets `**Plan:** 🟢 Approved`.
3. `/ticket-run T2.04` builds the work in parallel waves, tests first, integrates it, runs the checks, reviews it and
   writes `EXPLAIN.md` and `IMPLEMENTATION.md`, then stops with `**Push:** 🟡 Awaiting code review`.
4. The person reviews the code and sets `**Push:** 🟢 Approved`, then runs `/ticket-run T2.04` again.
5. The ticket becomes one commit on `feature/tickets` with its pull request to `develop` (`Closes #<issue>`), merged by
   the `automerge` workflow once every check passes.

`/board` shows what is ready, running, in review and done. A contribution made without the harness follows the same
spirit: one issue, tests first, one focused pull request.

## Sign your commits (DCO)

Contributors keep their copyright and sign each commit with the
[Developer Certificate of Origin](https://developercertificate.org/), version 1.1
([D376](docs/specs/06-decisions/vision/d376-contributions-dco-then-foundation.md)). There is no CLA and no copyright
transfer, so the code can never be relicensed: it stays AGPL-3.0.

The sign-off is a line at the end of the commit message, with your real name and the email of your commit:

```text
Signed-off-by: Jane Doe <jane.doe@example.org>
```

`git commit -s` adds it. To sign commits you already made on your branch:

```bash
git commit --amend -s --no-edit        # the last commit
git rebase --signoff develop           # every commit of the branch
```

By signing off, you certify that you wrote the change or have the right to submit it under the project's licence.

## Code rules

- [AGENT.md](AGENT.md) is the rulebook, and the tests of `tests/conventions/` enforce the parts a test can check.
- **Tests come first.** Write the tests, see them fail, then write the code. A bug fix starts with a test that
  reproduces the bug.
- Each layer of a service calls only the one below it: `api` → `service` → `storage`, all of them using `models`.
  A service never imports another service; what they share goes in `backend/shared/` or, for a public contract, in
  `backend/models/`.
- Plain British English in docstrings, messages and documentation, and no em dashes.
- **Dependencies** must be compatible with AGPL-3.0. A lock file is regenerated with its own tool (`uv lock`,
  `pnpm install`), never edited by hand.
- **No secret, token or personal data** in code, configuration, tests, logs or issues.

## Run the checks

```bash
uv sync
uv run ruff check <the folders you changed>
uv run ruff format <the files you edited>
uv run mypy <the source folders you changed>
uv run --package <service> pytest backend/services/<service>/tests -n 2
uv run pytest tests/<folder> -n 2
```

Run tests one file or one folder at a time, and format only the files you edited. The exact commands per service and
per front end are in [AGENT.md](AGENT.md#commands). A front end is tested with Playwright against the real images
started by `compose.e2e.yaml`, never against a development server.

CI runs the same checks on every push and pull request, for the parts the change touches. All of them must pass.

## Specifications and documentation

- A specification page follows the shape of its template in [docs/specs/_templates/](docs/specs/_templates/README.md),
  has its own ID, and states nothing the product owner has not decided; a suggestion is marked "(Proposed)".
- A change that alters what users see or how the code is built updates [docs/functional/](docs/functional/README.md)
  or [docs/technical/](docs/technical/README.md) in the same pull request.

## Pull requests

- One topic per pull request, from a GitFlow branch, to `develop` (a hotfix to `master`).
- Fill the [template](.github/pull_request_template.md): what, why, the issue it closes, how it was tested.
- Every commit is signed off, and every check passes.
- A maintainer reviews it. Once a pull request carries the `automerge` label, the `automerge` workflow merges it as
  soon as every check passes.

## Licence

By contributing, you agree that your contribution is licensed under the [GNU AGPL-3.0](LICENSE), like the rest of
SimpleERP. Plugins and sector packs are AGPL-3.0 too
([D377](docs/specs/06-decisions/vision/d377-plugins-agpl-only.md)).
