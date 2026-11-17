🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-27 Inputs are frozen once handed over

# 📏 BR-F13-27 Inputs are frozen once handed over

**Status:** 🔄 waiting for the owner

## Statement

Once the inputs of a month are handed over to the payroll firm they are frozen: no input of that month can be added,
changed or deleted until a correction handover reopens the employees concerned, and the first handover stays in the
history.

## Why

The firm calculates from the file it received; changing the inputs afterwards would make the payslips and the company's
records disagree. The owner asked for outsourced payroll
([D532](../../../06-decisions/f13-payroll/d532-benchmark-gaps-f13-payroll.md)); the freeze is the same idea as the lock
of [BR-F13-10 Pay run locked after payment](br-f13-10-pay-run-locked-after-payment.md).

## Examples

| Case | Result |
|---|---|
| An input edited after the file was sent | refused, a correction handover is offered |
| A correction for one employee | only that employee is reopened |
| A new employee hired after the freeze | added through a correction handover |
| A handover frozen but not sent | still frozen, the officer can send it |
| A returned file for the wrong month | refused |

## Applies to

- [UC-F13-37](../use-cases/10-special-contracts-and-outsourcing/uc-f13-37-hand-pay-inputs-to-an-outsourced-payroll-firm.md)
- [E-F13-30 Payroll handover](../data/e-f13-30-payroll-handover.md)
- [E-F13-03 Pay input](../data/e-f13-03-pay-input.md)

## Exceptions

None.

## Configurable

The tolerance on the net of a line, by the payroll officer.

## Open questions

None.

---

⬅️ [BR-F13-26 Days worked never exceed the package](br-f13-26-days-worked-never-exceed-the-package.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F13-28 Delegation hours are paid as work time](br-f13-28-delegation-hours-are-paid-as-work-time.md)
