---
name: release-notes
description: Write the release note and the changelog entry of every simple-erp ticket, and assemble them at a release (rule DOC-3). Mode `ticket` (at hand-over, before the pull request) writes docs/tickets/GH-<n>/RELEASE-NOTE.md for users and the versioned fragment changelog.d/GH-<n>.<type>.md (Keep a Changelog types added/changed/deprecated/removed/fixed/security, **Breaking:** marker), then posts the note on the issue as a `<!-- release-note -->` comment after the push. Mode `release` (on release/<x.y.z> or a hotfix branch) suggests the semantic version, builds the CHANGELOG.md section from the fragments and deletes them, and prepares the GitHub Release body that release.yml publishes with the QA reports. Use at every ticket hand-over, when preparing a release or hotfix, when asked for release notes, a changelog or the next version number, and when CI's release-notes check fails.
argument-hint: [ticket GH-<n> | release <x.y.z>]
---

# Release notes and changelog (DOC-3)

Arguments: `$ARGUMENTS`: the mode and the ticket key or version.

**The tool:** `.claude/skills/release-notes/bin/release-notes`:

| Command | Does |
|---|---|
| `check [--ticket <KEY>] [--branch <name>]` | Prints nothing when DOC-3 holds on the branch (by default the one checked out): on a `feature/` or `bugfix/` branch, exactly one fragment `changelog.d/GH-<n>.<type>.md` with a known type; on a `release/` or `hotfix/` branch, the version's `CHANGELOG.md` section and an empty `changelog.d/` (a hotfix's own fragment excepted until it is built); with `--ticket`, the ticket's `RELEASE-NOTE.md` with no placeholder left |
| `next-version` | Suggests the next version from the last `v<x.y.z>` tag and the fragment types (`conf/changelog-types.yaml`): removed or **Breaking:** bumps major, added, changed or deprecated bumps minor, fixed or security bumps patch |
| `build <x.y.z>` | Adds `## [x.y.z] - <date>` to `CHANGELOG.md` under `## [Unreleased]`, grouped by type in the catalogue's order, each line ending with its issue link, and deletes the fragments it used |
| `release-body <x.y.z>` | Prints the GitHub Release body: the version's CHANGELOG section, then each issue's `<!-- release-note -->` comment (read with `GITHUB_TOKEN` or `gh auth token`), then the upgrade notes. `release.yml` runs it |

## Mode `ticket`, at hand-over

1. **Read** TICKET.md, EXPLAIN.md §2 (what changed for users) and §6 (limits), and the branch's changes.
2. **Write `docs/tickets/<KEY>/RELEASE-NOTE.md`** from [templates/RELEASE-NOTE.md](templates/RELEASE-NOTE.md), for users: what is new and for whom, how to use it, upgrade notes, known limits, links. Plain British English, no em dashes, no internal names, no secret.
3. **Write `changelog.d/<KEY>.<type>.md`**: one to three lines, in the past tense of a changelog ("Customers can be archived from their page."), with the type that fits the main change. A breaking change starts with `**Breaking:**` and its upgrade note is mandatory. Commit it with the ticket (`[GH-<n>] docs: release note`).
4. **Check:** `release-notes check --ticket <KEY>` prints nothing. Log both files in PROGRESS.md's "Release note" section.
5. **After the push** (GIT-1), post the note on the issue: `gh issue comment <n> --body-file docs/tickets/<KEY>/RELEASE-NOTE.md` (the file starts with `<!-- release-note -->`). Log the comment link. When the note changes later, edit that comment, never post a second one.

## Mode `release`, on `release/<x.y.z>` or `hotfix/<x.y.z>-GH-<n>-<slug>`

1. `release-notes next-version` and agree the version with the owner (GIT-8 names the branch after it).
2. `release-notes build <x.y.z>`; read the new section; commit (`release: <x.y.z> changelog`).
3. `release-notes check` prints nothing.
4. The QA stage runs on the release branch (GIT-6), then the pull request into `master`. Once merged, the owner's yes for the tag (GIT-1): `git tag -a v<x.y.z> -m "simple-erp <x.y.z>"` on the merge commit and `git push origin v<x.y.z>`. `release.yml` publishes the images and the Release with `release-notes release-body <x.y.z>` and the QA reports.
5. Merge `master` back into `develop` through a pull request.
