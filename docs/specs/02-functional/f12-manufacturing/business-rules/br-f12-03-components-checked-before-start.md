🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-03 Components checked before start

# 📏 BR-F12-03 Components checked before start

**Status:** ✅ specified

## Statement

An order starts when its components are available; otherwise the missing ones are shown and only the planner can start
it anyway.

## Why

See [D312](../../../06-decisions/f12-manufacturing/d312-manufacturing-coverage.md).

## Examples

| Case | Result |
|---|---|
| 2 of 3 components in stock | Start refused, the missing one shown |

## Applies to

Every F12 use case concerned.

## Exceptions

None.

## Configurable

Start with missing components: allowed to the planner, or never.

## Open questions

None.

---

⬅️ [BR-F12-02 An order keeps its versions](br-f12-02-an-order-keeps-its-versions.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-04 Lots traced both ways](br-f12-04-lots-traced-both-ways.md)
