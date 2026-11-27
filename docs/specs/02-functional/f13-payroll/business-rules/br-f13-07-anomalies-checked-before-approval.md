🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-07 Anomalies checked before approval

# 📏 BR-F13-07 Anomalies checked before approval

**Status:** ✅ specified

## Statement

A pay run shows its anomalies (variations, negative nets, missing inputs) and is approved only when each is cleared or
accepted.

## Why

See [D365](../../../06-decisions/f13-payroll/d365-payroll-coverage.md).

## Examples

| Case | Result |
|---|---|
| Net down 30 % | Anomaly to accept |

## Applies to

Every F13 use case concerned.

## Exceptions

None.

## Configurable

Thresholds.

## Open questions

None.

---

⬅️ [BR-F13-06 Withholding at the sent rate](br-f13-06-withholding-at-the-sent-rate.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F13-08 Payslip in the legal format](br-f13-08-payslip-in-the-legal-format.md)
