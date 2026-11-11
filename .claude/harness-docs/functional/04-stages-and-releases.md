# 4. Stages and releases

## Branches

GitFlow (GIT-8): `feature/GH-<n>-<slug>` and `bugfix/GH-<n>-<slug>` from `develop`; `release/<x.y.z>` from `develop`
into `master`; `hotfix/<x.y.z>-GH-<n>-<slug>` from `master`. Nobody commits on `master` or `develop` directly.

## Dev and QA

A stage is one run of the `stage.yml` workflow: the commit's images start on a GitHub runner, the tests run against
them, the reports are uploaded, and a deployment is recorded on the `dev` or `qa` environment. Nothing to book,
nothing hosted.

| | dev | QA |
|---|---|---|
| When | Every push to `develop`; by hand for a ticket's commit | Every push to `release/*` and `hotfix/*`; by hand for a pull request, once everything before it passed (GIT-6) |
| What | Smoke, unit, Bruno, Playwright `@smoke` | All of it, the full Playwright suite, the upgrade test, the dependency check |
| Who approves | Nobody | You: Claude asks your yes before each QA run (GIT-6) |

Claude records each run's reports in the ticket folder (`record-run --run-id`).

## Releases

1. "Prepare release x.y.z": `release/x.y.z` from `develop`, `CHANGELOG.md` built from `changelog.d/`.
2. QA runs on the branch; the pull request into `master` is merged.
3. On your yes, the merge commit is tagged `vx.y.z` and pushed: the images get the version tag, and the GitHub
   Release gets the changelog, the issues' release notes and the QA reports.
4. `master` is merged back into `develop`.

A hotfix follows the same path from `master`.
