🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🤖 [Assistant](README.md) › 🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Every internal persona | Configurators | Knowledge editors | HR, administrator, owner |
|---|---|---|---|---|
| Ask, about the screen, find, guide | ✅ within their rights | ✅ | ✅ | ✅ |
| Changes through the AI assistant | ✅ within their rights, confirmed | ✅ | ✅ | ✅ |
| Outside tools | per connection row of their role (D80) | as their role | as their role | ✅ set them up |
| Personal connections | allowed services only | ✅ | ✅ | ✅ choose services |
| Knowledge: read | within each item's audience | ✅ | ✅ | ✅ |
| Knowledge: propose | ✅ | ✅ | ✅ | ✅ |
| Knowledge: add, change, approve | - | - | their folders | ✅ all |
| Configuration requests: answer | - | ✅ | - | ✅ administrator |
| Share conversations | ✅ own | ✅ own | ✅ own | ✅ own, never others' |
| Assistant settings, usage dashboard | - | - | - | administrator, owner |

## Record rules

- The AI assistant has no rights of its own: every read and change uses the user's
  ([BR-F3-02](business-rules/br-f03-02-answers-use-only-what-the-user-may-see.md)).
- Nobody, administrators included, reads another user's conversation unless it is shared with them
  ([BR-F3-33](business-rules/br-f03-33-usage-reports-never-show-content.md)).
- A shared conversation continues as the reader's own copy, with the reader's rights
  ([BR-F3-25](business-rules/br-f03-25-shared-conversations-continue-as-a-copy.md)).
- Everyone uses the AI assistant, each for their own requests; the tools that would read or change what the user's role
  may not are disabled ([BR-F3-34](business-rules/br-f03-34-every-capability-is-reachable-from-the-assistant.md),
  [D519](../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)).

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
