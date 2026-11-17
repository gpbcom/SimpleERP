🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) ›
🛟 [Hosted support assistant (hosted edition)](README.md) › 🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Administrator (U07) | Employee (U01) | Owner (U13) | Hosting engineer (U48) |
|---|---|---|---|---|
| Open, follow, rate, export | ✅ | own | ✅ | ✅ |
| Allow screenshots | ✅ | own | ✅ | - |
| Approve a fix or restore | - | - | ask | ✅ |
| Incidents, status page | read | read | read | ✅ |
| Assistant rights, masking | - | - | - | ✅ |
| Support plan | read | - | ✅ | - |

## Record rules

- The AI assistant reads only the customer's namespace (BR-F20-03).
- An employee sees only their own requests.

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
