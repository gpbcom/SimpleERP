🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-23 Rollback restores the previous version and data

# 📏 BR-F14-23 Rollback restores the previous version and data

**Status:** ✅ specified

## Statement

Before every update the runtime keeps the previous version and a snapshot of the plugin's data; an administrator may
roll back within 30 days, which restores both and logs it; data entered since the update is exported first.

## Why

An update that breaks work must be undone without losing data (D471, BR-F14-03).

## Examples

| Case | Result |
|---|---|
| Update on 2026-11-02, rollback on 2026-11-05 | passes: 2.3.1 and its data restored, the 3 days' changes exported |
| Rollback after 45 days | fails: snapshot gone limit 30 days |
| Rollback of a version withdrawn for security | fails: refused (BR-F14-12) |

## Applies to

- [UC-F14-28 Roll back to the previous version](../use-cases/06-release-channels-and-rollback/uc-f14-28-roll-back-to-the-previous-version.md)
- [UC-F14-03 Update with compatibility checks](../use-cases/01-find-and-install/uc-f14-03-update-with-compatibility-checks.md)

## Exceptions

Security withdrawals forbid going back to the vulnerable version.

## Configurable

The administrator may keep snapshots longer within the storage plan.

## Open questions

None.

---

⬅️ [BR-F14-22](br-f14-22-support-terms-shown-before-purchase-and-measured.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F14-24 Test instances hold demo data only](br-f14-24-test-instances-hold-demo-data-only.md)
