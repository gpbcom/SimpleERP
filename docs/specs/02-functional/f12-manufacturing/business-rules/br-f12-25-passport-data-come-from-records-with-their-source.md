🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-25 Passport data come from records with their source

# 📏 BR-F12-25 Passport data come from records with their source

**Status:** ✅ specified

## Statement

Each passport field shows its source (bill of materials, compliance file, energy, entered by hand); a passport with a
required field missing is not published.

## Why

A passport must be traceable to evidence.

## Examples

| Case | Result |
|---|---|
| Repair info missing | Not published |

## Applies to

- [UC-F12-30 Build the digital product passport](../use-cases/13-energy-passport-and-work-in-progress/uc-f12-30-build-the-digital-product-passport.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F12-24 Energy is allocated by meter, else by time](br-f12-24-energy-is-allocated-by-meter-else-by-time.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F12-26](br-f12-26-recipes-scale-to-the-batch-and-keep-their-tolerances.md)
