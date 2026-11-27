🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-07 Kept working across upgrades

# 📏 BR-F19-07 Kept working across upgrades

**Status:** ✅ specified

## Statement

Every generated feature's tests run against each new SimpleERP version before it reaches the customer; a failure is
fixed by the publisher before the upgrade.

## Why

See [D389](../../../06-decisions/f19-feature-factory/d389-generated-features-are-plugins.md).

## Examples

| Case | Result |
|---|---|
| Test fails on 3.2 | Upgrade held for that customer, fix queued |

## Applies to

Every F19 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F19-06 Tried on a copy first](br-f19-06-tried-on-a-copy-first.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F19-08 Ordered by the owner or an administrator](br-f19-08-ordered-by-owner-or-admin.md)
