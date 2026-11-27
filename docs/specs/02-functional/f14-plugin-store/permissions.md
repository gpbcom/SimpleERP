🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🧰 [Plugin store](README.md) › 🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Administrator (U07) | Owner (U13) | Publisher (U46) | Store operator (U11) | Accounting (U05) |
|---|---|---|---|---|---|
| Browse, install, update, uninstall | ✅ | read | - | ✅ private store | - |
| Buy, licences, seats | ✅ | ✅ approve | - | - | read invoices |
| Rate and review | ✅ | ✅ | answer | moderate | - |
| Submit, release, prices | - | - | ✅ own plugins | - | - |
| Security review, signing | - | - | - | ✅ | - |
| Payouts, seller reports | - | - | read own | ✅ | ✅ |
| Withdraw, moderate | - | - | - | ✅ | - |

## Record rules

- A publisher sees only its own plugins, releases, revenue and reviews.
- Signed releases and check reports are read-only (BR-F14-07).
- A company sees only its own installations and licences.

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
