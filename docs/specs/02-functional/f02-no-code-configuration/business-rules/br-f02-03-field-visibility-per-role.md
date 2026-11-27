🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F2-03 Field visibility per role

# 📏 BR-F2-03 Field visibility per role

**Status:** ✅ specified

## Statement

A custom field limited to some roles is shown, sent and answered about only to users holding one of those roles; "see"
lets them read it, "see and change" lets them edit it.

## Why

An HR-only field must stay with HR, on every channel. See
[D102](../../../06-decisions/f02-no-code-configuration/d102-field-visibility-per-role.md).

## Examples

| Field | Limited to | A sales person | An HR user |
|---|---|---|---|
| "Disability status" on employees | HR, see and change | Never sees it, not in the API nor the AI assistant | Sees and edits it |
| "Credit limit" on customers | Accounting see and change, Sales see | Reads it | (not concerned) |

## Applies to

- [UC-F2-01](../use-cases/01-configure-a-record-type/uc-f02-01-add-a-custom-field-to-a-record-type.md); BR-F2-02.
- [UC-F2-27 Set field-level rights and validation rules](../use-cases/11-rights-translations-and-approvals/uc-f02-27-set-field-level-rights-and-validation-rules.md)

## Exceptions

The IT provider administrator sees everything (D90).

## Configurable

Yes: per custom field.

## Open questions

None.

---

⬅️ [BR-F2-02 Custom data follows permissions](br-f02-02-custom-data-follows-permissions.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-04 Computed fields are read-only](br-f02-04-computed-fields-are-read-only.md)
