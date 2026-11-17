🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-08 Rights add up

# 📏 BR-F1-08 Rights add up

**Status:** ✅ specified

## Statement

A user holding several roles has every right of each role; where two roles' record rules differ, the more permissive
applies.

## Why

Combined jobs need no combined role. See [D72](../../../06-decisions/f01-administration/d72-several-roles.md).

## Examples

| Roles | Result |
|---|---|
| Sales (own customers) and Manager (site's customers) | Sees every customer of the site |
| Employee and HR | Sees every employee record (HR) and their own self-service (Employee) |
| Administrator and Owner | Settings and the owner's business data (BR-F1-02) |

## Applies to

- [UC-F1-04](../use-cases/03-user-lifecycle/uc-f01-04-change-a-users-role-or-site.md); every permission check (T2).
- [UC-F1-18 Run an access review campaign](../use-cases/11-team-delegation-and-access-review/uc-f01-18-run-an-access-review-campaign.md)
- [UC-F1-20 Create and revoke API tokens and service accounts](../use-cases/12-portal-accounts-and-integrations/uc-f01-20-create-and-revoke-api-tokens-and-service-accounts.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-07 One account per email](br-f01-07-one-account-per-email.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-09 Dated changes](br-f01-09-dated-changes.md)
