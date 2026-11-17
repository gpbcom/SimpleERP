🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-04 Uninstall keeps an export

# 📏 BR-F14-04 Uninstall keeps an export

**Status:** ✅ specified

## Statement

Uninstalling a plugin exports its data first and keeps the export for the set period.

## Why

See [D368](../../../06-decisions/f14-plugin-store/d368-plugin-store-coverage.md).

## Examples

| Case | Result |
|---|---|
| Uninstall | Export kept 90 days |

## Applies to

Every F14 use case concerned.

- [UC-F14-22 Deprecate a plugin and announce its end of life](../use-cases/07-plugin-end-of-life/uc-f14-22-deprecate-a-plugin-and-announce-its-end-of-life.md)
- [UC-F14-04 Uninstall and export the plugin's data](../use-cases/01-find-and-install/uc-f14-04-uninstall-and-export-the-plugin-s-data.md)

## Exceptions

None.

## Configurable

Period.

## Open questions

None.

---

⬅️ [BR-F14-03 Updates only when compatible](br-f14-03-updates-only-when-compatible.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F14-05 Licences checked, offline tolerant](br-f14-05-licences-checked-offline-tolerant.md)
