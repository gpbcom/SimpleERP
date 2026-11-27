🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-33 Sessions end on role change or revocation

# 📏 BR-F1-33 Sessions end on role change or revocation

**Status:** ✅ specified

## Statement

Every session of a user ends, and their trusted devices are revoked, as soon as the user's role, site or rights change,
their account is deactivated, their password is reset, or an administrator or the user revokes the session; the next
request from that device is refused and the user signs in again with the new rights.

## Why

A session opened with old rights must not outlive them: an employee moved to another site or a leaver must not keep
reading what the old role allowed. The owner's answer: "Sessions and devices"
([D520](../../../06-decisions/f01-administration/d520-benchmark-gaps-f01-administration.md)).

## Examples

| Case | Result |
|---|---|
| A user moves from the Paris site to the Lyon site | every session ends within 1 minute, the user signs in again |
| A leaver is deactivated ([BR-F1-21](br-f01-21-deprovisioned-users-are-deactivated-never-deleted.md)) | every session ends and trusted devices are revoked |
| The user resets their password | every other session ends, the current one stays |
| The user ends their phone session | that session ends, the others stay |
| An API token ([BR-F1-27](br-f01-27-tokens-are-scoped-dated-and-shown-once.md)) | unchanged: tokens are revoked on their own screen |

## Applies to

- [UC-F1-24 Manage sessions and trusted devices](../use-cases/15-security-and-group-data/uc-f01-24-manage-sessions-and-trusted-devices.md)
- [UC-F1-04 Change a user's role or site](../use-cases/03-user-lifecycle/uc-f01-04-change-a-users-role-or-site.md)
- [UC-F1-05 Deactivate and offboard a user](../use-cases/03-user-lifecycle/uc-f01-05-deactivate-and-offboard-a-user.md)
- [E-F1-23 User session](../data/e-f01-23-user-session.md)

## Exceptions

A change of the user's display name or phone number does not end sessions.

## Configurable

No: the rule is fixed; the length of a session and the trusted period are set in the security policy.

## Open questions

None.

---

⬅️ [BR-F1-32 Records on a map only for roles with the map right](br-f01-32-map-right-for-planners-and-managers.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F1-34](br-f01-34-purges-are-logged-and-never-touch-legal-records.md)
