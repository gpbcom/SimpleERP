🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-03 Updates only when compatible

# 📏 BR-F14-03 Updates only when compatible

**Status:** ✅ specified

## Statement

An update installs only if it declares compatibility with the running version and passes its migration on a copy first.

## Why

See [D368](../../../06-decisions/f14-plugin-store/d368-plugin-store-coverage.md).

## Examples

| Case | Result |
|---|---|
| Plugin for 2.x on 3.0 | Not offered |

## Applies to

Every F14 use case concerned.

- [UC-F14-25 Roll out a release in stages](../use-cases/06-release-channels-and-rollback/uc-f14-25-roll-out-a-release-in-stages.md)
- [UC-F14-28 Roll back to the previous version](../use-cases/06-release-channels-and-rollback/uc-f14-28-roll-back-to-the-previous-version.md)

## Exceptions

None.

## Configurable

Automatic or manual updates.

## Open questions

None.

---

⬅️ [BR-F14-02 Permissions shown before install](br-f14-02-permissions-shown-before-install.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F14-04 Uninstall keeps an export](br-f14-04-uninstall-keeps-an-export.md)
