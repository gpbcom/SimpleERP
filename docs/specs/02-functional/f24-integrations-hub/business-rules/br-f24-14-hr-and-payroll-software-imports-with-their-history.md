🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🔌 [F24 Integrations hub](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F24-14 HR and payroll software imports with their history

# 📏 BR-F24-14 HR and payroll software imports with their history

**Status:** ✅ specified

## Statement

A connection to Silae, PayFit or Lucca imports employees, contracts, absences and pay history into F9 and F13 with their
dates; the source stays the owner of the data until the company switches, and then the sync stops.

## Why

Companies use these tools before F13 exists (D481); personal data follows the country pack (BR-F24-01).

## Examples

| Case | Result |
|---|---|
| PayFit with 48 employees and 24 months of payslips | passes: imported with dates |
| Lucca absences synced daily while Lucca is used | passes |
| Switch to F13 on 2027-01-01 | passes: sync stopped, history kept |

## Applies to

- [UC-F24-23 Bring HR and payroll data from Silae, PayFit or Lucca](../use-cases/06-business-tools/uc-f24-23-bring-hr-and-payroll-data-from-silae-payfit-or-lucca.md)

## Exceptions

None.

## Configurable

The data kinds to import and the history length.

## Open questions

None.

---

⬅️ [BR-F24-13](br-f24-13-automation-tools-through-signed-webhooks-and-the-api.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F24-15](br-f24-15-the-e-invoicing-platform-connected-step-by-step.md)
