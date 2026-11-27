🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-07 One account per email

# 📏 BR-F1-07 One account per email

**Status:** ✅ specified

## Statement

An email address belongs to at most one user in a company.

## Why

An email identifies a user for invitations, sign-in and notifications. See
[D69](../../../06-decisions/f01-administration/d69-one-account-per-email.md).

## Examples

| Case | Result |
|---|---|
| Inviting marie@acme.fr, who is active | Refused; Marie's user page opens |
| Inviting marie@acme.fr, who is deactivated | Refused; her page opens with "Reactivate" |
| Same email in another company of the same platform | Allowed: companies are separate (D19) |

## Applies to

- [UC-F1-03 Invite a user](../use-cases/03-user-lifecycle/uc-f01-03-invite-a-user.md)
- [UC-F1-13 Provision users from the identity provider](../use-cases/10-bring-users-in-at-scale/uc-f01-13-provision-users-from-the-identity-provider.md)
- [UC-F1-14 Invite users in bulk](../use-cases/10-bring-users-in-at-scale/uc-f01-14-invite-users-in-bulk.md)
- [UC-F1-15 Administer the users of one's own site](../use-cases/10-bring-users-in-at-scale/uc-f01-15-administer-the-users-of-ones-own-site.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-06 Invitation link valid 48 hours](br-f01-06-invitation-link-valid-48-hours.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-08 Rights add up](br-f01-08-rights-add-up.md)
