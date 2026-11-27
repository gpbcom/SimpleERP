---
name: release
description: Release SimpleERP - start the release workflow on develop, which runs every test suite, writes the changelog, the release notes and the test reports on release/<version>, and lets automerge merge it into master, tag it, publish it and bring it back to develop, with no commit or merge by hand (TKT-26). Use when the person types /release, optionally with a version such as /release 1.0.0, or asks to release or to bring master up to date.
---

# Release

A release reaches `master` by itself (TKT-26, `.claude/rules/tickets.md`). This skill starts it and follows it.

0. Read the repository from `.claude/harness.json` (`repo`, `gpbcom/SimpleERP` today):
   `REPO=$(python3 -c 'import json; print(json.load(open(".claude/harness.json"))["repo"])')`, and use `-R "$REPO"`
   in every `gh` command below.
1. Check `gh secret list -R "$REPO"` lists `RELEASE_TOKEN`. If it does not, stop and give the person the README
   section "🚢 Releases": the token is theirs to create.
2. Say what will be released: `git fetch -q origin`, the last tag (`git tag --list 'v*' --sort=-v:refname | head -1`)
   and `git log --oneline --first-parent <last tag or origin/master>..origin/develop | wc -l` pull requests.
3. Start it (the PreToolUse hook asks the person first):
   `gh workflow run release.yml -R "$REPO" --ref develop` and `-f version=<x.y.z>` when the person gave one.
4. Follow it: find the run with `gh run list -R "$REPO" --workflow release.yml --limit 1`, then watch it in the
   background (`gh run watch <id> -R "$REPO" --exit-status`). When it ends, report each job with ✅ or ❌.
5. Then follow the pull request `Release v<version>` to `master` and its way back to `develop`
   (`gh pr list -R "$REPO" --state all --head release/<version>`) until both are merged, and give the person the
   GitHub release of SimpleERP v<version> (`gh release view v<version> -R "$REPO" --json url`), the changelog and the
   test report verdict.

Never commit, merge, tag or push anything by hand for a release: when a step fails, report the failing job with its
log and stop. `ERP_GITFLOW_BYPASS=1` is the person's own bypass of the git hooks: never set it for a release.
