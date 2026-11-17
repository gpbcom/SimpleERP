🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-02 Permissions shown before install

# 📏 BR-F14-02 Permissions shown before install

**Status:** ✅ specified

## Statement

A plugin's requested permissions (data, connectors, AI, outside calls) are shown and accepted before install; a new
permission in an update asks again.

## Why

See [D368](../../../06-decisions/f14-plugin-store/d368-plugin-store-coverage.md).

## Examples

| Case | Result |
|---|---|
| Update asks for email access | Consent asked again |

## Applies to

Every F14 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F14-01 The store follows the country pack](br-f14-01-store-follows-the-country-pack.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F14-03 Updates only when compatible](br-f14-03-updates-only-when-compatible.md)
