🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-02 Rates dated by period

# 📏 BR-F13-02 Rates dated by period

**Status:** ✅ specified

## Statement

A pay run uses the rates and rules in force for its pay period; a correction of a past month uses that month's.

## Why

See [D365](../../../06-decisions/f13-payroll/d365-payroll-coverage.md).

## Examples

| Case | Result |
|---|---|
| Correct March in July | March rates |

## Applies to

Every F13 use case concerned.

- [UC-F13-16 Simulate pay and costs](../use-cases/04-events/uc-f13-16-simulate-pay-and-costs.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F13-01 Payroll follows the country pack](br-f13-01-payroll-follows-the-country-pack.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F13-03 Inputs closed before the run](br-f13-03-inputs-closed-before-the-run.md)
