🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F21-04 Data kept when a module is off

# 📏 BR-F21-04 Data kept when a module is off

**Status:** ✅ specified

## Statement

Switching a module off hides it and keeps its data, read-only for the roles that had it, until the company deletes it
explicitly.

## Why

See [D395](../../../06-decisions/f21-onboarding-and-modules/d395-onboarding-and-modules-coverage.md).

## Examples

| Case | Result |
|---|---|
| Switch off Payroll | Payslips kept, read-only |

## Applies to

Every F21 use case concerned.

## Exceptions

None.

## Configurable

Deletion.

## Open questions

None.

---

⬅️ [BR-F21-03 Dependencies explained, never hidden](br-f21-03-dependencies-explained.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F21-05 Plain words with examples](br-f21-05-plain-words-with-examples.md)
