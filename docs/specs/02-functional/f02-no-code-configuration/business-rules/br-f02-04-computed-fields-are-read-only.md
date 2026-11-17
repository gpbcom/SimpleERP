🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F2-04 Computed fields are read-only

# 📏 BR-F2-04 Computed fields are read-only

**Status:** ✅ specified

## Statement

A computed field is never typed: it is calculated from its formula each time one of its inputs changes; a
formula can only use fields of the same record and of linked records.

## Why

A value calculated from others must stay consistent with them. See
[D101](../../../06-decisions/f02-no-code-configuration/d101-custom-field-types.md).

## Examples

| Formula | Inputs | Value |
|---|---|---|
| price - cost | 120, 80 | 40 |
| a field of a linked customer | Acme's credit limit | 5,000 EUR |
| an input left empty | price empty | empty, not an error |

## Applies to

- [UC-F2-01](../use-cases/01-configure-a-record-type/uc-f02-01-add-a-custom-field-to-a-record-type.md)

## Exceptions

None.

## Configurable

The formula, per field.

## Open questions

None.

---

⬅️ [BR-F2-03 Field visibility per role](br-f02-03-field-visibility-per-role.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-05 Core statuses are locked](br-f02-05-core-statuses-are-locked.md)
