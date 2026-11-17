🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-20 Similar features are shown before any quote

# 📏 BR-F19-20 Similar features are shown before any quote

**Status:** 🔄 waiting for the owner

## Statement

The similar features of the hosted store and of the plugin store are shown to the owner before any quote is prepared for
a request, and the quote waits until the owner has chosen one to install or has said that none fits.

## Why

A feature that already exists costs less, is already tested and is kept up to date for everyone; building a copy wastes
the customer's money. The owner asked to see similar features before ordering
([D538](../../../06-decisions/f19-feature-factory/d538-benchmark-gaps-f19-feature-factory.md)).

## Examples

| Case | Result |
|---|---|
| A request close to a promoted feature | listed before the quote |
| Nothing close | the screen says so and the request goes on |
| The owner installs a close feature | the request is closed with no charge |
| A feature withdrawn as harmful | never listed |
| The owner skips the list | not possible: the quote waits for a choice |

## Applies to

- [UC-F19-27](../use-cases/07-catalogue-and-co-funding/uc-f19-27-see-similar-features-before-ordering.md)
- [E-F19-01 Feature request](../data/e-f19-01-feature-request.md)

## Exceptions

None.

## Configurable

The number of results shown and the lowest closeness listed, by the simple-ERP team.

## Open questions

None.

---

⬅️ [BR-F19-19 Factory billing posted to accounting](br-f19-19-factory-billing-posted-to-accounting.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F19-21 Fixed-price changes keep their price](br-f19-21-fixed-price-changes-keep-their-price.md)
