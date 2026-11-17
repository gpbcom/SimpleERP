🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D99 Archive, never delete

# 📜 D99 Archive, never delete

**Status:** ✅ decided

## Context

Whether a custom field or a new record type can be deleted once it holds data.

## Options

- Archive, never delete.
- Delete with its data.

## Choice

Archived, never deleted: it is hidden from forms and lists, its data is kept and exportable, and it can be restored. It
can be deleted only while empty.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

No configuration change ever loses data.

## Related

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md)
- [BR-F2-01](../../02-functional/f02-no-code-configuration/business-rules/br-f02-01-archive-never-delete.md)

---

⬅️ [D98 Who holds the Configurator role](d98-who-configures.md) · ⬆️ [Up](README.md) ·
➡️ [D100 Where custom data appears](d100-custom-data-exposure.md)
