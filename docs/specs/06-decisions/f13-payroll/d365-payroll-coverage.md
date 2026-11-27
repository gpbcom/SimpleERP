🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 💶 [Decisions: F13 Payroll (plugin)](README.md) ›
📜 D365 Payroll coverage

# 📜 D365 Payroll coverage

**Status:** ✅ decided

## Context

The owner asked that F13 cover everything the benchmark's payroll offers (D30), with French law.

## Options

- Everything, plus French law.
- Pay inputs only, external payroll.

## Choice

Everything: company and employee payroll set-up, pay inputs from F9, gross to net, collective-agreement rules,
withholding tax, the pay-run check, clarified digital payslips, SEPA payments, the monthly social declaration and its
returns, corrections, contributions, accounting entries, sick leave, end of contract, simulations, benefits, yearly
reports, rate updates from the country pack, and the AI assistant; rates and rules updated each 1 January and 1 July
through the country pack.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Twenty use cases (D367); every feature reachable from the AI assistant (BR-F3-34).

Revised by D445 on 2026-11-12: the employer's copy of a payslip is kept 5 years; electronic payslips stay available 50
years from issue (CR-FR-182).

## Related

- [F13 Payroll](../../02-functional/f13-payroll/README.md)

---

⬅️ [D364 SC16 use cases](../sectors/d364-sc16-use-cases.md) · ⬆️ [Up](README.md) ·
➡️ [D366 Payroll officer persona](d366-payroll-officer-persona.md)
