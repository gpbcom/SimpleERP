🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-01 Key personal data is validated

# 📏 BR-F9-01 Key personal data is validated

**Status:** ✅ specified

## Statement

An employee updates their own details; a change of bank account or family status takes effect only after HR validates
it; every change is logged.

## Why

See [D288](../../../06-decisions/f09-hr-and-projects/d288-employee-self-service.md).

## Examples

| Case | Result |
|---|---|
| New address | Applied |
| New IBAN | Waits for HR, then used for the next payslip |

## Applies to

Every F9 use case concerned.

## Exceptions

None.

## Configurable

Yes: which fields need validation.

## Open questions

None.

---

⬆️ [Up](README.md) ·
➡️ [BR-F9-02 HR data stays with HR and the person](br-f09-02-hr-data-stays-with-hr-and-the-person.md)
