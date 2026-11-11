# <KEY> — <TITLE>

<One line: services, front ends and packages touched, what is deliberately not touched, the branch (to come or existing). Issue: https://github.com/<owner>/<repo>/issues/<n>.>

**Status (<DATE>):** <same icon as PROGRESS.md's current step> <⏳ documentation folder created; implementation waits for the owner's go | 🔄 step N in progress | ⏸️ paused, see STATUS.md | ⏳ in review, PR #… | ✅ done>.

## The feature

<3 to 6 sentences in plain words, for someone who has not read the ticket: the problem today, what changes, who benefits, where it is seen (screen, endpoint, file, job).>

| Before | After |
|---|---|
| <today's behaviour> | <target behaviour> |

## Files

| File | What it holds |
|---|---|
| [TICKET.md](TICKET.md) | The GitHub issue (topics T1…), the acceptance criteria AC1…AC<n>, the attachments described |
| [PLAN.md](PLAN.md) | Decisions, steps, AC → tests → validation, development rules, scope. **Takes precedence** over IMPLEMENTATION.md |
| [IMPLEMENTATION.md](IMPLEMENTATION.md) | The implementation choices and their justification, the exact list of files modified, per file today vs target |
| [TESTS-CATALOG.md](TESTS-CATALOG.md) | Every test per acceptance criterion and the AC → tests matrix |
| [TESTS-NOTICE.md](TESTS-NOTICE.md) | How to run each test level for this feature |
| [EXPLAIN.md](EXPLAIN.md) | DOC-1 hand-over document. §6 (risks, questions, decision log) from plan time; the rest at hand-over |
| [PROGRESS.md](PROGRESS.md) | Progress per step, times, stage validation, documentation, release note, pull request, reviews, final verification |
| [RELEASE-NOTE.md](RELEASE-NOTE.md) | DOC-3: what the ticket gives users, written at hand-over |
| [attachments/](attachments/) | The <n> files attached to the GitHub issue |
| [tests-evidences/](tests-evidences/README.md) | Evidence of every run (TEST-8), every report kept (TEST-9). Archive: <pre-release `evidence-<KEY>` link> |

Related: <[GH-xxxxx](../GH-xxxxx/README.md) (relation), or "none">.
