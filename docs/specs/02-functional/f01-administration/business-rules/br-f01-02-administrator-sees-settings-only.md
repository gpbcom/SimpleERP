🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-02 Administrator sees settings only

# 📏 BR-F1-02 Administrator sees settings only

**Status:** ✅ specified

## Statement

The administrator role manages settings, users and roles, and sees no business data unless the same user also holds a
business role.

## Why

Least privilege: salaries stay with HR, invoices with accounting. See
[D57](../../../06-decisions/f01-administration/d57-administrator-sees-settings-only.md).

## Examples

| Case | Result |
|---|---|
| An administrator opens the employees list | Refused, unless they also hold the HR role |
| An administrator edits the HR role's record rules | Allowed: it is a setting |
| An owner holds the administrator and owner roles | Sees settings and the owner's business data |

## Applies to

Every use case of F1, and every screen showing business data.

- [UC-F1-17 See my team's accounts and pending requests](../use-cases/11-team-delegation-and-access-review/uc-f01-17-see-my-teams-accounts-and-pending-requests.md)

- [UC-F1-22 Search the audit trail and export it to a SIEM](../use-cases/13-security-and-audit/uc-f01-22-search-the-audit-trail-and-export-it-to-a-siem.md)

## Exceptions

The IT provider administrator can enter any client company at any time
([D53](../../../06-decisions/ux/d53-provider-access-always.md)) and sees everything there: the administrator role and
every business role ([D90](../../../06-decisions/f01-administration/d90-provider-sees-everything.md)); each session is
visible to the client ([D89](../../../06-decisions/f01-administration/d89-provider-sessions-visible.md)).

## Configurable

⬜ To be specified with UC-F1-06.

## Open questions

None.

---

⬅️ [BR-F1-01 Offboarding hand-over](br-f01-01-offboarding-hand-over.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-03 A company is usable once set up](br-f01-03-company-usable-once-set-up.md)
