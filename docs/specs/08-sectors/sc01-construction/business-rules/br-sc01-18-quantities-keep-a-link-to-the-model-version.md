🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏗️ [SC01 Construction](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC01-18 Quantities keep a link to the model version

# 📏 BR-SC01-18 Quantities keep a link to the model version

**Status:** ✅ specified

## Statement

Every quantity taken from a model keeps the link to the model version it came from; a quantity never changes silently
when a new version is imported, and a line already signed changes only through an amendment.

## Why

A quote built from a model must answer the question "which drawing was this priced on?" in a dispute, and a silent
change would alter a price the customer agreed to. The owner asked for BIM quantities
([D545](../../../06-decisions/sectors/d545-benchmark-gaps-sc01-construction.md)).

## Examples

| Case | Result |
|---|---|
| Slab 412.6 m2 from version 3 | the lot shows 412.6 m2 and version 3 |
| Version 4 says 428.1 m2 | listed as +15.5, applied only when accepted |
| Quote line signed by the customer | the change waits for an amendment |
| Element with no lot | listed as unmapped, not priced |

## Applies to

- [UC-SC01-18](../use-cases/06-revision-developers-bim-and-grants/uc-sc01-18-take-quantities-from-a-bim-model.md)
- [E-SC01-17 BIM import](../data/e-sc01-17-bim-import.md)
- [E-SC01-02 Quote lot](../data/e-sc01-02-quote-lot.md)

## Exceptions

None.

## Configurable

The units and the conversion table, by the site manager.

## Open questions

None.

---

⬅️ [BR-SC01-17 Calls for funds follow the legal stage caps](br-sc01-17-calls-for-funds-follow-the-legal-stage-caps.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC01-19 Grants need the RGE label at signature](br-sc01-19-grants-need-the-rge-label-at-signature.md)
