🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🛡️ [Administration](README.md) ›
🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | U07 Administrator | U13 Owner | U02 Manager | U11 IT provider administrator |
|---|---|---|---|---|
| Guided setup (UC-F1-01) | yes | as administrator | no | yes |
| Sites (UC-F1-02) | yes | as administrator | own site's hours and contacts | yes |
| Users: invite, change, offboard (UC-F1-03 to 05) | yes | as administrator | no | yes |
| Roles and record rules (UC-F1-06) | yes | as administrator | no | yes |
| Connections, AI, single sign-on (UC-F1-07 to 09) | yes | as administrator | no | yes |
| Client companies (UC-F1-10, 11) | no | no | no | yes |
| Reports and GDPR register (UC-F1-12) | yes | yes | no | yes |

The administrator sees settings only ([BR-F1-02](business-rules/br-f01-02-administrator-sees-settings-only.md)); the IT
provider sees everything ([D90](../../06-decisions/f01-administration/d90-provider-sees-everything.md)).

## Record rules

F1 is where record rules are set ([BR-F1-12](business-rules/br-f01-12-record-rule-kinds.md)); F1's own screens have
none.

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
