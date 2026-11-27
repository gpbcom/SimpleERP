🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-22 A change that breaks something is not published unread

# 📏 BR-F2-22 A change that breaks something is not published unread

**Status:** ✅ specified

## Statement

A change whose impact list holds a broken item is published only once the configurator fixed or accepted each broken
item.

## Why

Renaming one field can silently break a plugin or an integration.

## Examples

| Case | Result |
|---|---|
| Broken integration not accepted | Publish refused |
| Every broken item accepted | Published, owners told |

## Applies to

- [UC-F2-23 See the impact of a change before publishing](../use-cases/10-change-safely/uc-f02-23-see-the-impact-of-a-change-before-publishing.md)
- [UC-F2-26 Find unused configuration](../use-cases/10-change-safely/uc-f02-26-find-unused-configuration.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-21](br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-23 A failing test case blocks the publish](br-f02-23-a-failing-test-case-blocks-the-publish.md)
