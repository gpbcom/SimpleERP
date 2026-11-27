🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🔧 [No-code configuration](README.md) ›
🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | U07 Administrator | Configurator (U02, U16, U13, U12) | Every user |
|---|---|---|---|
| Custom fields, statuses, forms, record types (UC-F2-01 to 04) | yes | on record types their roles see | no |
| Personal list views (UC-F2-03) | yes | yes | yes |
| Document and email templates (UC-F2-05, 06) | yes | yes | no |
| Sender address (UC-F2-06) | yes | no | no |
| Rules and workflows (UC-F2-07, 08) | yes | yes, within their own rights | no |
| Publish (UC-F2-09) | yes | their own drafts | no |
| Roll back (UC-F2-10) | yes | no | no |
| Export a pack (UC-F2-11) | yes | yes | no |
| Import, publish to the store (UC-F2-11) | yes | no | no |
| Request types (UC-F2-30) | yes | on record types their roles see | no |

## Record rules

Configurators act only on the record types their other roles can see
([D96](../../06-decisions/f02-no-code-configuration/d96-configurator-role.md)); rule and workflow accounts never exceed
their author (BR-F2-12).

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
