🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-06 Automated checks before review

# 📏 BR-F14-06 Automated checks before review

**Status:** ✅ specified

## Statement

A submitted version passes tests, the conventions, licence and dependency scans, and the vulnerability scan before human
review.

## Why

See [D368](../../../06-decisions/f14-plugin-store/d368-plugin-store-coverage.md).

## Examples

| Case | Result |
|---|---|
| Vulnerable dependency | Rejected with the report |

## Applies to

Every F14 use case concerned.

- [UC-F14-21 Check a plugin's bill of materials and licences](../use-cases/03-publish/uc-f14-21-check-a-plugins-bill-of-materials-and-licences.md)

## Exceptions

None.

## Configurable

Checks.

## Open questions

None.

---

⬅️ [BR-F14-05 Licences checked, offline tolerant](br-f14-05-licences-checked-offline-tolerant.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F14-07 Releases signed](br-f14-07-releases-signed.md)
