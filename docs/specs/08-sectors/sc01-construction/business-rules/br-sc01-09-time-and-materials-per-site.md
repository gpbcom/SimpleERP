🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏗️ [SC01 Construction](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC01-09 Time and materials per site

# 📏 BR-SC01-09 Time and materials per site

**Status:** ✅ specified

## Statement

Every hour and every material is charged to a site and a lot. Entries made offline on the phone follow the shared
offline forms: kept on the phone and synced in order, conflicts shown,
[BR-F2-21 Offline forms keep only what is needed and sync in order](../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

## Why

See [D316](../../../06-decisions/sectors/d316-construction-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| 8 h entered offline | Synced when back online, charged to site S-14, lot 2 |

## Applies to

Every SC01 use case concerned.

## Exceptions

None.

## Configurable

Lots per site.

## Open questions

None.

---

⬅️ [BR-SC01-08 Declarations before digging](br-sc01-08-declarations-before-digging.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC01-10 Acceptance starts the warranties](br-sc01-10-acceptance-starts-the-warranties.md)
