# <KEY> — <where> <DATE>: <check>

Written by `ticket-docs record-run`. Edit only the **What**, **IDs / ACs** and **Notes**.

| | |
|---|---|
| **What** | <what this run proves> |
| **Command** | `<exact command, credentials read from the environment, never pasted>` |
| **Commit** | `<40-character commit hash>` on `<branch>` |
| **Kind** | <unit | gui | e2e | check> |
| **Where** | <local | ci | dev | qa> |
| **Date** | <DATE> <HH:MM> |
| **Result** | <✅ PASS n/n | ❌ FAIL: what | 🔴 RED n failed (expected, TEST-7) | ⚠️ INVALID: environment failure, re-run in [folder](../<folder>/README.md)> |
| **IDs / ACs** | <catalogue IDs> · <AC IDs> |

## Artefacts

| File | Holds |
|---|---|
| [console.txt](console.txt) | The raw console output |
| [report.xml](report.xml) | JUnit report (unit) |
| [report.html](report.html) | HTML report (unit) |
| [playwright-report/index.html](playwright-report/index.html) | Playwright HTML report (gui, e2e) |
| [results.json](results.json) | Playwright JSON results (gui, e2e) |
| [actions.log](actions.log) | The Actions run log, searched for DEP-3 (ci, dev, qa) |
| [artifacts/](artifacts/) | The Actions run's artifacts, downloaded (ci, dev, qa) |

## Notes

<Anything a reader needs to trust the result: data used, what was compared, known unrelated failures and why they are unrelated.>
