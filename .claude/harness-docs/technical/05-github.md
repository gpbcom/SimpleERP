# 5. GitHub

## Repository `gpbcom/simple-erp` (private)

| Setting | Value |
|---|---|
| Branches | `master` (released), `develop` (default branch), GitFlow branches (GIT-8) |
| Merge | Squash for features and bugfixes, merge commits for release and back-merges; branches deleted on merge |
| Environments | `dev`, `qa` (deployment records only: no required reviewer on this plan) |
| Labels | `type:*`, `priority:*`, `area:*` |
| Security | Dependabot alerts and security updates on; `dependabot.yml` for uv, Actions, Docker, npm |
| Templates | `.github/ISSUE_TEMPLATE/{feature,bug}.yml`, `.github/pull_request_template.md` |

## Project board #6 "simple-erp"

Fields **Status** (Backlog, Ready, In progress, In review, QA, Done), **Priority** and **Kind** ("Type" is reserved
by GitHub). Their IDs are in `ticket-docs/conf/github.yaml`; `ticket-docs board GH-n "<Status>"` moves a card through
`gh api graphql`. Views and built-in automations (auto-add issues, closed or merged → Done) are set in the web page:
the API cannot.

## Workflows

| Workflow | Trigger | Jobs |
|---|---|---|
| `ci.yml` | Push to a GitFlow branch, pull requests | detect, ruff, mypy, pytest, harness tools, documentation and changelog, images |
| `images.yml` | Called by CI | One image per changed service and front end; pushed to GHCR from `develop` and `master` only |
| `stage.yml` | Push to `develop` (dev), `release/**` and `hotfix/**` (QA), dispatch | The ephemeral stage: compose up, smoke, unit, Bruno, Playwright, upgrade test (QA), DEP-1 (QA), reports artifact, deployment record |
| `release.yml` | Tag `v*.*.*` | Version tags on the images, GitHub Release with `release-notes release-body` and the QA reports |

Rules for workflows (DEP-4): every third-party action pinned to a full commit SHA; read-only permissions at the top,
write permissions per job.

## What the free plan does not allow, and the fallbacks

| Not available on a private repository | Fallback |
|---|---|
| Required reviewers on the `qa` environment (HTTP 422) | The owner's explicit yes before each QA run (GIT-6) |
| Branch rulesets and protection (HTTP 403) | The `git-gate` hook refuses commits and pushes on `master` and `develop` (GIT-8); CI still runs on every pull request |

Both come back by upgrading the plan or making the repository public; then add the ruleset (PR required, checks
`ruff`, `mypy`, `pytest`, `harness tools`, `documentation and changelog`) and the `qa` reviewer.
