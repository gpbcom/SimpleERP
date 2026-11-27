🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 💶 [Decisions: F13 Payroll (plugin)](README.md) ›
📜 D445 Electronic payslips available 50 years from issue

# 📜 D445 Electronic payslips available 50 years from issue

**Status:** ✅ decided

## Context

R7: three payslip retention values (CR-FR-182, Q12, CR-FR-047). A web-fetch agent read service-public F559 and F10029 on
2026-11-12: the employer keeps its copy 5 years; electronic payslips are available 50 years from issue, or a second
option the two pages state differently (6 years after retirement on F559, until age 75 on F10029); neither page names
the article.

## Options

- The 50-year option, which satisfies both pages.
- Wait for Q12.

## Choice

The employer's copy is kept 5 years; electronic payslips stay available 50 years from issue, the option that satisfies
both official pages. The pages' discrepancy on the second option stays in Q12.

## Decided by

The owner, on 2026-11-12 at 14:57, after a web-fetch agent read the official pages (R7, PROGRESS.md, step 21).

## Consequences

Revises D365's payslip archive. CR-FR-182, CR-FR-047 and BR-F13-13 say so; Q12 keeps the discrepancy.

## Related

- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md)
- [Q12 Payslip availability period](../../07-questions/q12-payslip-availability-period.md)
- [D365](d365-payroll-coverage.md)
- Independent review of 2026-11-12 (the independent review of 2026-11-12, not kept in the repository)

---

⬅️ [D444 Backup targets per edition](../technical/d444-backups-per-edition.md) · ⬆️ [Up](README.md) ·
➡️ [D446 Privacy and retention specified](../security-and-compliance/d446-privacy-specified.md)
