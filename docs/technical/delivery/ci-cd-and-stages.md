# CI/CD and stages

SimpleERP is built, tested and released by GitHub Actions. Branches follow GitFlow, every pull request is merged by
the `automerge` workflow once its checks pass, and every commit can be tried on two ephemeral stages, dev and QA,
before it is released.

## Branches (GitFlow, rule TKT-15)

```mermaid
gitGraph
    commit id: "v0.1.0" tag: "v0.1.0"
    branch develop
    checkout develop
    branch feature/tickets
    commit id: "T2.04"
    commit id: "T2.05"
    checkout develop
    merge feature/tickets
    branch release/0.2.0
    commit id: "changelog, notes, reports"
    checkout master
    merge release/0.2.0 tag: "v0.2.0"
    checkout develop
    merge release/0.2.0
```

| Branch | From | Into | Name |
|---|---|---|---|
| tickets | `develop` | `develop`, one pull request per ticket | `feature/tickets`, shared by every running roadmap ticket (TKT-16) |
| feature, bugfix | `develop` | `develop` | `feature/<name>` (`feature/harness-<name>` for the harness), `bugfix/<name>` |
| release | `develop` | `master`, then back into `develop` | `release/<version>`, written by `release.yml` (TKT-26) |
| hotfix | `master` | `master`, then back into `develop` | `hotfix/<name>` |

- `develop` is the default branch, so `Closes #<n>` in a pull request closes its issue when it merges. Each finished
  ticket is one commit with its own `Closes #<issue>`, titled with its ID (`T2.04: <title>`).
- `develop` and `master` change only through pull requests, merged with a merge commit. The git hooks of `.githooks/`
  (`python3 .claude/scripts/tickets/tickets.py setup`) refuse a commit or a push on them, a branch outside GitFlow and a
  ticket commit without its ID.
- A branch lives as long as its work: `tickets.py branches` gives each branch its verdict, only a live branch is
  rebased onto `develop`, and `tickets.py prune` deletes the merged ones after a backup bundle (TKT-25).

## Workflows

The pipeline below comes with the CI/CD change that follows the harness port. Until it is merged,
`.github/workflows/` holds the earlier `ci`, `images`, `stage` and `release` workflows.

| Workflow | Runs on | Does |
|---|---|---|
| `ci.yml` | Every push to a GitFlow branch, every pull request to `develop` or `master` | Detects what changed, then calls `python.yml`, `typescript.yml`, `terraform.yml` and `images.yml` for the services, packages, front ends and Terraform folders concerned; one final job fails when any of them failed. Every run keeps its test reports as `test-report-*` artifacts, failed runs included |
| `python.yml` | Called by CI | For each changed Python package: `uv sync --locked`, `ruff check`, `ruff format --check`, `mypy` and `pytest -n 2` with its JUnit report, then the contract check of every service with an `openapi.json` (`.github/scripts/check_contract.sh`, REQ-T05-05): the committed document must equal the generated one, and against the document of the pull request's base or of the push's previous commit, no path, operation, parameter, schema or property may be removed and no type may change. Additions pass, and with no base document only the stale check runs; and the repository-level tests of `tests/` |
| `typescript.yml` | Called by CI | For each changed front end and TypeScript package: `pnpm install --frozen-lockfile`, lint, type check and tests |
| `terraform.yml` | Called by CI | For each changed Terraform folder (a root or a module of `infra/terraform/`): `terraform fmt -check -recursive`, `init -backend=false`, `validate` and `terraform test` where the folder has a `tests/` folder, with its JUnit report kept as `test-report-terraform-*` |
| `images.yml` | Called by CI | Builds one image per changed service and front end (repository root as context), runs Playwright against the real images of `compose.e2e.yaml`, then signs and pushes the images tagged with the commit SHA, from `develop` and `master` only |
| `gitflow.yml` | Every pull request | Checks that the branch is a GitFlow branch, that it targets the right base, and that a ticket's title starts with its ID |
| `automerge.yml` | A pull request labelled `automerge` whose checks passed | Merges it with a merge commit once every check passed on its head commit, which closes its issue, then deletes its head branch unless it moved. For a release: tags `v<version>`, publishes the GitHub release and brings the branch back to `develop` |
| `release.yml` | By hand on `develop` (`/release`) | Runs every suite of CI, writes the changelog, the release notes and the test reports on `release/<version>`, and opens its pull request to `master` labelled `automerge` |
| `stage.yml` | `develop` (dev), `release/**` and `hotfix/**` (QA), or by hand | The ephemeral stage, below |

A change in `backend/models/`, `backend/shared/`, `frontend/packages/`, `uv.lock` or `pnpm-lock.yaml` selects every
service and front end (`AGENT.md`, "CI/CD"). A change to a service's committed OpenAPI document, `backend/services/<service>/openapi.json`, selects its service and image, and also every front-end project and front-end image, so that the stale check of the generated client in `frontend/packages/api-client` runs on the regenerated document. A change under `infra/terraform/` selects every Terraform folder, because
the modules are shared, and the repository-level tests of `tests/`. `ticket_tree.py finish`, run by `/ticket-run`, labels a ticket's pull request `automerge`,
so a ticket reaches `develop` with no merge by hand; a failing check leaves the pull request open for the person.

## Stages: dev and QA

A stage is one run of `stage.yml`: it checks out the commit, starts its images with `compose.e2e.yaml` on the runner,
runs the tests against them, uploads every report, and records a GitHub Deployment on the `dev` or `qa` environment.
Nothing is hosted, so there is no stage to book and nothing to pay for besides Actions minutes.

| | dev | QA |
|---|---|---|
| Question | Does this commit work? | Is this commit fit to release? |
| Runs on | Every push to `develop`, and by hand for a branch | Every push to `release/**` and `hotfix/**`, and by hand |
| Tests | Smoke test, unit tests, Bruno, Playwright `@smoke` | The same with the full Playwright suite, the upgrade test from the previous release, and the dependency check |

```bash
gh workflow run stage.yml --ref <branch> -f stage=dev -f ref=<commit>
gh workflow run stage.yml --ref <branch> -f stage=qa -f ref=<commit>
```

**Why both:** they answer different questions. Dev runs on every integration and catches a broken commit in minutes;
QA runs the slow, release-grade checks once per candidate. Both follow GitFlow: `develop` goes to dev, `release/*` to
QA, and a tag on `master` makes the release.

`compose.e2e.yaml` at the repository root is the stack every stage and the end-to-end tests start. It runs `platform`,
`backoffice` and PostgreSQL from the images named `${ERP_IMAGE_PREFIX}-<name>:${ERP_IMAGE_TAG}`, waits for every health
check to pass, publishes the back office and the API for Playwright and Bruno, and keeps the database private to the
stack. To start it locally, set the two variables and run the command:

```bash
ERP_IMAGE_PREFIX=ghcr.io/gpbcom/simpleerp ERP_IMAGE_TAG=<tag> docker compose -f compose.e2e.yaml up --detach --wait
```

It runs the same images as the Compose profiles of `infra/compose/`.

## Releases

A release reaches `master` by itself (TKT-26). The person starts it from Claude Code with `/release`, or from a
terminal:

```bash
gh workflow run release.yml --ref develop                  # the next minor version after the last v* tag
gh workflow run release.yml --ref develop -f version=1.0.0
```

1. `release.yml` runs every suite of CI on the commit of `develop`, with everything selected.
2. Only when all pass, it writes on `release/<version>`: a new section of `CHANGELOG.md`, and in
   `docs/releases/v<version>/` the release notes, the test report and the raw reports. No release is written without
   its test reports.
3. `automerge.yml` merges the release into `master` once every check passed, tags it `v<version>` and publishes the
   GitHub release with its notes.
4. `automerge.yml` brings `release/<version>` back to `develop` by its own pull request, then deletes it.

Nobody commits or merges by hand. The secret `RELEASE_TOKEN`, a token of the repository with contents, pull requests
and workflows in write, lets the release's pull requests start CI and its merge carry `.github/workflows/`; without it
the release stops at once and says so.

## Target design (specified in GH-2, not built yet)

**Pipeline (D419).** GitHub Actions runs the pipeline of `AGENT.md` (changed services only, checks, images, Playwright
against the real images, publish from `develop` or `master`). Images are signed (D415) and pushed to a European
container registry (for example Scaleway's or OVHcloud's), mirrored to GitHub's registry for self-hosters. The dev and
QA stages stay ephemeral runs on runners (`stage.yml`); a long-lived staging and production follow in
[DevOps](../operations/devops.md).

Decided in [D419](../../specs/06-decisions/technical/d419-ci-cd-and-registry.md).

Last reviewed: 2026-11-28
