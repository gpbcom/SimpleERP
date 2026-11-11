# 2. Tests and evidence

Three rules make every test result trustworthy and traceable.

## Tests before code (TEST-7)

For every code step, in this order, with no exemption:

1. Claude writes the tests and commits them **alone**.
2. Claude runs them and records the **red run**: they must fail, and only because the code is missing.
3. Claude writes the code and commits it.
4. Claude records the **green run** on that commit.

A guard (`git-gate` hook) refuses a commit of production code when no red run was recorded since the last green one,
or when new tests come in the same commit as the code. Before the branch is squashed into one commit, its history is
saved in the ticket folder, so the order stays provable.

## Nothing passes without its evidence (TEST-8)

Every run that proves something is recorded with `ticket-docs record-run`, into
`tests-evidences/<where>-<date>-<check>/`: the exact command, the commit it ran on, the raw output, the reports and the
verdict. Without such a folder, "it passes" is not a result, in a reply, a ticket document or a pull request.

## Every report is kept (TEST-9)

| Kind | Kept |
|---|---|
| Unit | `report.xml` (JUnit), `report.html`, the console |
| GUI (Playwright) | The HTML report, `results.json`, screenshots, traces and videos of failures |
| E2E (stages, Bruno) | The run's artifacts and log, Bruno's reports |

Failed, red and invalid runs are kept too. `docs/tickets/README.md` indexes every run of every ticket. Each ticket
folder is archived on GitHub (`evidence-GH-<n>`), and each release carries its QA reports.
