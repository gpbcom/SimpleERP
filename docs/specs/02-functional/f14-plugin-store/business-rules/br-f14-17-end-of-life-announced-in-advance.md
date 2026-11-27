🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-17 End of life announced in advance

# 📏 BR-F14-17 End of life announced in advance

**Status:** 🔄 waiting for the owner

## Statement

A publisher ending a plugin announces it at least (Proposed) 6 months ahead, keeps security fixes until the end date,
and points installers to an export or an alternative; installs keep running after the end date without updates.

## Why

Companies rely on the plugin's data and need time to move (D471).

## Examples

| Case | Result |
|---|---|
| Notice on 2026-12-01 for an end on 2027-06-30 | passes |
| Notice on 2026-12-01 for an end on 2027-01-15 | fails: refused as shorter than the minimum notice |
| Vulnerability found after the end date | passes: withdrawal rules apply (BR-F14-12) |

## Applies to

- [UC-F14-22 Deprecate a plugin and announce its end of life](../use-cases/07-plugin-end-of-life/uc-f14-22-deprecate-a-plugin-and-announce-its-end-of-life.md)

## Exceptions

A legal or security emergency follows BR-F14-12 instead.

## Configurable

The store operator sets the minimum notice, (Proposed) 6 months at least.

## Open questions

None.

---

⬅️ [BR-F14-16 Dependencies listed and licence-compatible](br-f14-16-dependencies-listed-and-licence-compatible.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F14-18 Abandoned plugins can be taken over](br-f14-18-abandoned-plugins-can-be-taken-over.md)
