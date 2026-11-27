🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-20 Advances recovered from the next pay

# 📏 BR-F13-20 Advances recovered from the next pay

**Status:** ✅ specified

## Statement

A pay advance never exceeds the net already earned in the month and is recovered from the next pay; a loan beyond that
is a separate repayment plan approved by the owner.

## Why

An advance is pay already earned; a larger sum is a loan the employee repays (D470).

## Examples

| Case | Result |
|---|---|
| Advance of 300.00 EUR on 15 March, net earned 1 050.00 EUR | passes: recovered on the March payslip |
| Advance of 1 500.00 EUR on 10 March, net earned 700.00 EUR | fails: refused, a loan is offered instead |

## Applies to

- [UC-F13-27 Grant a pay advance](../use-cases/08-deductions-savings-and-leave-pay/uc-f13-27-grant-a-pay-advance.md)
- [UC-F13-09 Pay employees by SEPA transfer](../use-cases/03-declarations-and-payments/uc-f13-09-pay-employees-by-sepa-transfer.md)

## Exceptions

The owner may approve a loan with its repayment plan.

## Configurable

The company may cap advances at a lower amount.

## Open questions

None.

---

⬅️ [BR-F13-19 Garnishment within the attachable portion](br-f13-19-garnishment-within-the-attachable-portion.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F13-21 Profit-sharing once the threshold is reached](br-f13-21-profit-sharing-once-the-threshold-is-reached.md)
