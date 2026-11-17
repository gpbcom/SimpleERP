🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D101 Custom field types

# 📜 D101 Custom field types

**Status:** ✅ decided

## Context

Which field types a custom field can have.

## Options

- Text, number, date, yes/no and list (always).
- Money, percentage, duration.
- Link to a record.
- Files and images.
- Computed (formula).
- String fields, locations, phone numbers (added by the owner).

## Choice

Fourteen types: text, string, number, date, yes/no, list, money, percentage, duration, link to a record, files and
images, computed (formula), location (address and coordinates), phone number.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The record type editor offers these types.

## Related

- [UC-F2-01](../../02-functional/f02-no-code-configuration/use-cases/01-configure-a-record-type/uc-f02-01-add-a-custom-field-to-a-record-type.md)

---

⬅️ [D100 Where custom data appears](d100-custom-data-exposure.md) · ⬆️ [Up](README.md) ·
➡️ [D102 Field visibility per role](d102-field-visibility-per-role.md)
