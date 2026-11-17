🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-04 Empty a site before closing it

# 📏 BR-F1-04 Empty a site before closing it

**Status:** ✅ specified

## Statement

A site can be closed only when it holds no stock and no staff.

## Why

Nothing is left on a closed site. See
[D64](../../../06-decisions/f01-administration/d64-empty-a-site-before-closing.md).

## Examples

| Case | Result |
|---|---|
| The Lyon yard holds 40 items and 3 employees | Closing refused; simple-ERP lists the 40 items and the 3 employees |
| Stock moved and staff moved to other sites | The site closes |
| The head office | Cannot be closed; another site must become head office first |

## Applies to

- [UC-F1-02 Add or change a site](../use-cases/02-manage-sites/uc-f01-02-add-or-change-a-site.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-03 A company is usable once set up](br-f01-03-company-usable-once-set-up.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-05 Document numbering](br-f01-05-document-numbering.md)
