🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F12-02 An order keeps its versions

# 📏 BR-F12-02 An order keeps its versions

**Status:** ✅ specified

## Statement

A manufacturing order keeps the bill of materials and routing versions it was released with; a change to them goes
through an engineering change, approved, and applies to the next orders.

## Why

See [D312](../../../06-decisions/f12-manufacturing/d312-manufacturing-coverage.md).

## Examples

| Case | Result |
|---|---|
| BoM v4 approved during order MO-311 | MO-311 stays on v3 |

## Applies to

Every F12 use case concerned.

- [UC-F12-28 Publish versioned work instructions](../use-cases/10-people-and-tools/uc-f12-28-publish-versioned-work-instructions.md)

## Exceptions

None.

## Configurable

Approvers per product category.

## Open questions

None.

---

⬅️ [BR-F12-01 Manufacturing follows the country pack](br-f12-01-manufacturing-follows-the-country-pack.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F12-03 Components checked before start](br-f12-03-components-checked-before-start.md)
