🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🛡️ [Administration](README.md) ›
🔔 Notifications

# 🔔 Notifications

**Status:** ✅ specified

## Notifications

| Event | To | Use case |
|---|---|---|
| Invitation | the person invited (email) | UC-F1-03 |
| Invitation accepted or expired | the administrator | UC-F1-03 |
| Setup done | the administrator | UC-F1-01 |
| Site changed, made head office or closed | the site's manager | UC-F1-02 |
| Roles or site changed | the user; the old and new site managers | UC-F1-04 |
| Items handed over | the colleague | UC-F1-05 |
| Former-employee access | the leaver (email) | UC-F1-05 |
| Role rights shrank | the role's users | UC-F1-06 |
| Connection down or new tools | the administrators | UC-F1-07 |
| AI provider failing | the administrators | UC-F1-08 |
| Single sign-on on or off; secret expiring | every user; the administrators | UC-F1-09 |
| Provider session started | the client's administrators | UC-F1-11 |
| GDPR register to review | the administrators | UC-F1-12 |

## Channels

In-app (the bell) and email; each user can turn emails off per kind
([D92](../../06-decisions/f01-administration/d92-notification-channels.md)). Invitations and the former-employee access
are emails only, since their reader has no account yet or any more.

## Open questions

None.

---

⬅️ [Permissions](permissions.md) · ⬆️ [Up](README.md) · ➡️ [Reports](reports.md)
