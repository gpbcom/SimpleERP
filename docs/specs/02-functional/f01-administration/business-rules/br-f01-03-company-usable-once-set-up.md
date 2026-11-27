🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-03 A company is usable once set up

# 📏 BR-F1-03 A company is usable once set up

**Status:** ✅ specified

## Statement

A company is usable only once its seven setup steps are done; until then its users see only the setup wizard.

## Why

The owner wants every step done before use. See
[D59](../../../06-decisions/f01-administration/d59-every-setup-step-required.md).

## Examples

| Case | Result |
|---|---|
| Steps 1 to 6 done, step 7 not | Users see the setup wizard only |
| Step 4 answered "none" | Step 4 is done |
| All seven steps done | The home screen opens for every user |

## Applies to

- [UC-F1-01 Set up a new company](../use-cases/01-guided-setup/uc-f01-01-set-up-a-new-company.md)
- [UC-F1-23 Close a company and export all its data](../use-cases/14-close-a-company/uc-f01-23-close-a-company-and-export-all-its-data.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-02 Administrator sees settings only](br-f01-02-administrator-sees-settings-only.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-04 Empty a site before closing it](br-f01-04-empty-a-site-before-closing-it.md)
