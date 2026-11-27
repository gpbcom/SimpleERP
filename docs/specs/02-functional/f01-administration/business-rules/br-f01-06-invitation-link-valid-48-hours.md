🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-06 Invitation link valid 48 hours

# 📏 BR-F1-06 Invitation link valid 48 hours

**Status:** ✅ specified

## Statement

An invitation link works for 48 hours after it is sent, once; resending an invitation cancels the previous
link.

## Why

Short-lived links limit the harm of a forwarded or leaked email. See
[D68](../../../06-decisions/f01-administration/d68-invitation-valid-48-hours.md).

## Examples

| Case | Result |
|---|---|
| Opened 20 hours after sending | The user sets their password and two-factor |
| Opened 50 hours after sending | Expired: the page says so and tells them to ask for a new one |
| Opened a second time after use | Refused |
| Opened after a resend | The old link is refused, the new one works |

## Applies to

- [UC-F1-03 Invite a user](../use-cases/03-user-lifecycle/uc-f01-03-invite-a-user.md)
- [UC-F1-14 Invite users in bulk](../use-cases/10-bring-users-in-at-scale/uc-f01-14-invite-users-in-bulk.md)
- [UC-F1-19 Manage portal accounts](../use-cases/12-portal-accounts-and-integrations/uc-f01-19-manage-portal-accounts.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-05 Document numbering](br-f01-05-document-numbering.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-07 One account per email](br-f01-07-one-account-per-email.md)
