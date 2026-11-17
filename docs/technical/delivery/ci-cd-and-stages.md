# CI/CD and stages

simple-erp is built, tested and released by GitHub Actions. Branches follow GitFlow, and every commit can be tried on
two ephemeral stages, dev and QA, before it is released.

## Branches (GitFlow, rule GIT-8)

```mermaid
gitGraph
    commit id: "v0.1.0" tag: "v0.1.0"
    branch develop
    checkout develop
    branch feature/GH-12-customers
    commit id: "tests"
    commit id: "code"
    checkout develop
    merge feature/GH-12-customers
    branch release/0.2.0
    commit id: "changelog"
    checkout master
    merge release/0.2.0 tag: "v0.2.0"
    checkout develop
    merge master
```

| Branch | From | Into | Name |
|---|---|---|---|
| feature, bugfix | `develop` | `develop` | `feature/GH-<n>-<slug>`, `bugfix/GH-<n>-<slug>` |
| release | `develop` | `master`, then back into `develop` | `release/<x.y.z>` |
| hotfix | `master` | `master`, then back into `develop` | `hotfix/<x.y.z>-GH-<n>-<slug>` |

`develop` is the default branch, so `Closes #<n>` in a pull request closes its issue when it merges.

## Workflows

| Workflow | Runs on | Does |
|---|---|---|
| `ci.yml` | Every push to a GitFlow branch, every pull request | Detects the changed services and front ends; ruff, mypy, pytest (reports kept); the harness tools' checks; `project-docs check` (DOC-2) and `release-notes check` (DOC-3); then `images.yml` for what changed |
| `images.yml` | Called by CI | Builds one image per changed service and front end (repository root as context), and pushes it to GHCR as `ghcr.io/<owner>/simple-erp-<name>:<sha>` from `develop` and `master` only |
| `stage.yml` | Push to `develop` (dev), push to `release/**` and `hotfix/**` (QA), or by hand | The ephemeral stage, below |
| `release.yml` | A `v<x.y.z>` tag | Tags the commit's images `:<x.y.z>` and `:latest`, and creates the GitHub Release with the changelog section, the issues' release notes and the QA reports |

`.github/scripts/detect-components.sh` lists the services and front ends that have a Dockerfile, and those a change
touches. A change in `packages/`, `uv.lock`, `pyproject.toml` or `compose.e2e.yaml` touches all of them.

## Stages: dev and QA

A stage is one run of `stage.yml`: it checks out the commit, starts its images with `compose.e2e.yaml` on the runner,
runs the tests against them, uploads every report, and records a GitHub Deployment on the `dev` or `qa` environment.
Nothing is hosted, so there is no stage to book and nothing to pay for besides Actions minutes.

| | dev | QA |
|---|---|---|
| Question | Does this commit work? | Is this commit fit to release? |
| Runs on | Every push to `develop`, and by hand for a feature branch | Every push to `release/**` and `hotfix/**`, and by hand for a pull request (GIT-6) |
| Tests | Smoke test, unit tests, Bruno, Playwright `@smoke` | The same with the full Playwright suite, the upgrade test from the previous release, and the dependency check |
| Gate | None | The owner's explicit yes before each run (GIT-6); the plan does not allow a required reviewer on a private repository |

```bash
gh workflow run stage.yml --ref <branch> -f stage=dev -f ref=<commit>
gh workflow run stage.yml --ref <branch> -f stage=qa -f ref=<commit>
```

**Why both:** they answer different questions. Dev runs on every integration and catches a broken commit in minutes;
QA runs the slow, release-grade checks once per candidate, behind an approval. Both follow GitFlow: `develop` goes to
dev, `release/*` to QA, and a tag on `master` makes the release. The free plan's 2,000 Actions minutes a month cover it
because QA runs only on release and hotfix branches and once per ticket.

Until the first service has a Dockerfile and `compose.e2e.yaml` exists, a stage run is the command line smoke test
and the unit tests on the commit.

## Releases

1. `release/<x.y.z>` from `develop`; `release-notes build <x.y.z>` writes the `CHANGELOG.md` section.
2. The QA stage runs on the branch; its pull request into `master` is merged.
3. The merge commit is tagged `v<x.y.z>` and the tag pushed: `release.yml` publishes.
4. `master` is merged back into `develop`.

## Target design (specified in GH-2, not built yet)

**Pipeline (D419).** GitHub Actions runs the pipeline of `AGENT.md` (changed services only, checks, images, Playwright
against the real images, publish from `develop` or `master`). Images are signed (D415) and pushed to a European
container registry (for example Scaleway's or OVHcloud's), mirrored to GitHub's registry for self-hosters. The dev and
QA stages stay ephemeral runs on runners (`stage.yml`); a long-lived staging and production follow in
[DevOps](../operations/devops.md).

Decided in [D419](../../specs/06-decisions/technical/d419-ci-cd-and-registry.md).

Last reviewed: 2026-11-12 (GH-2)
