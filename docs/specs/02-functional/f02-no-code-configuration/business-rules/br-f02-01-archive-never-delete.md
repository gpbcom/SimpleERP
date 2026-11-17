🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F2-01 Archive, never delete

# 📏 BR-F2-01 Archive, never delete

**Status:** ✅ specified

## Statement

A custom field or a record type that holds data can be archived, never deleted; it can be deleted only while empty.

## Why

No configuration change loses data. See
[D99](../../../06-decisions/f02-no-code-configuration/d99-archive-never-delete.md).

## Examples

| Case | Result |
|---|---|
| Delete the field "site manager", filled on 300 quotes | Refused; "Archive" offered |
| Archive it | Hidden from forms and lists; the 300 values kept and exportable |
| Restore it | Shown again with its values |
| Delete a new field never filled | Allowed |

## Applies to

UC-F2-01 Add a custom field; UC-F2-04 Create a new record type (planned).

- [UC-F2-23 See the impact of a change before publishing](../use-cases/10-change-safely/uc-f02-23-see-the-impact-of-a-change-before-publishing.md)

- [UC-F2-26 Find unused configuration](../use-cases/10-change-safely/uc-f02-26-find-unused-configuration.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-F2-02 Custom data follows permissions](br-f02-02-custom-data-follows-permissions.md)
