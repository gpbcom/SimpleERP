# How to use the harness

The short version. Details: [functional](functional/README.md) · [technical](technical/README.md).

## Work on a ticket

1. **Write the issue** on GitHub (templates: feature, bug). It is the ticket `GH-<n>`.
2. **Start:** in a new Claude session, say *"Create the documentation folder for GH-<n>"*. Claude reads the issue
   and the code, writes `docs/tickets/GH-<n>/` (plan, acceptance criteria, risks and questions), and stops.
3. **Review the plan** (`PLAN.md`, `EXPLAIN.md` §6), answer its questions on the issue, then say *"Go"*.
4. **Claude implements, tests first:** for each step, the tests are committed alone, seen failing (red run
   recorded), then the code, then the green run. Nothing is called "passing" without its evidence folder.
5. **Answer the gates** when Claude asks: each squash, each push, each QA run.
6. **Hand over:** say *"Hand over GH-<n>"*. Claude runs everything on the final commit and on the dev stage, audits
   the requirements, updates `README.md` and the functional and technical documentation, writes the release note
   and the changelog fragment, then (on your yes) squashes, pushes and opens the pull request, starts the QA stage,
   and archives the ticket folder to the pre-release `evidence-GH-<n>`.
7. **Review:** Claude follows the review comments (pr-review-followup) until a round has nothing left.

Keep one session per ticket: the PR watcher reopens that session when its pull request needs something.

## When the PR watcher calls

| You see | Do |
|---|---|
| A Claude tab opens with `/pr-watch GH-<n>` typed | Press **Enter**. Claude fixes, then asks before pushing |
| A notification "type /pr-watch GH-<n> in its terminal session" | Type it in that terminal |
| The same notification every hour | Press Enter in the session, or `pr-watch ack GH-<n>` to silence it |

Overview of all pull requests: `docs/tickets/pull-request-summary/README.md`.

## Release

Say *"Prepare release 0.2.0"* (or ask for the next version). Claude creates `release/0.2.0`, builds `CHANGELOG.md`
from `changelog.d/`, runs the QA stage, opens the pull request into `master`, and after your yes tags `v0.2.0`:
`release.yml` publishes the images and the GitHub Release with the release notes and the QA reports.

## Paid AI tests

Claude runs them through `ai-cost run` (max **$20 per ticket**). A test marked `llm` refuses to run otherwise. To
raise a blocked ticket's cap, in your own terminal:

```bash
.claude/skills/ai-test-cost/bin/ai-cost status GH-<n>
.claude/skills/ai-test-cost/bin/ai-cost raise-cap GH-<n> 30
```

## Add a rule

Say *"From now on, …"*. Claude writes it into the right file of `.claude/rules/` with the next ID (CS-17, GIT-9,
TEST-10, DOC-4…) or into `AGENT.md`, and applies it from then on.

## Useful commands

```bash
.claude/skills/ticket-docs/bin/ticket-docs check GH-<n>     # is the ticket folder complete?
.claude/skills/ticket-docs/bin/ticket-docs report-index     # every test run of every ticket
.claude/skills/project-docs/bin/project-docs check           # is the documentation complete?
.claude/skills/release-notes/bin/release-notes next-version  # the next semantic version
.claude/skills/pr-watch/bin/pr-watch status                  # watched pull requests
gh workflow run stage.yml --ref <branch> -f stage=dev -f ref=$(git rev-parse HEAD)   # a dev stage run
```

## First-time setup (once per machine)

```bash
gh auth login                                   # then:
gh auth refresh -h github.com -s project,read:user
cd .claude/skills && uv sync                    # the tools' environment
.claude/skills/pr-watch/bin/pr-watch install-units
systemctl --user enable --now claude-pr-watch.timer
```

## If something is stuck

| Problem | Fix |
|---|---|
| GitHub tools gone from Claude | `/mcp` → reconnect, or restart the session |
| "This command calls a paid AI" | Expected: Claude must wrap it in `ai-cost run` |
| "Production code before its red tests" | Expected: the tests come first, committed alone, with a recorded red run |
| The board does not move | `gh auth status` must list the `project` scope |
| Watcher silent | `systemctl --user status claude-pr-watch.timer`, `journalctl --user -u claude-pr-watch` |
