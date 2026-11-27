🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🚛 [SC07 Transport and logistics](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC07-09 Dangerous goods checked

# 📏 BR-SC07-09 Dangerous goods checked

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A load of dangerous goods needs its document, a trained driver and an equipped vehicle; the driver's
dangerous-goods training is a legal requirement of the dangerous-goods trip's request type
[BR-F9-26](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-26-legal-requirements-never-relaxed.md),
checked by
[BR-F9-25](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md);
in France: [CR-FR-121 Dangerous goods (ADR)](../../../10-country-packs/france/transport/cr-fr-121-dangerous-goods.md).

## Why

(⚖️ lawyer review before launch, D574) The documents and the exemption thresholds are still to read: ADR 5.4, 8.2 and 1.1.3.6, in
the edition in force (CR-FR-121).

## Examples

| Case | Result |
|---|---|
| Driver without the certificate | Not assignable |

## Applies to

Every SC07 use case concerned, and
[E-F2-25 Request type](../../../02-functional/f02-no-code-configuration/data/e-f02-25-request-type.md).

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-SC07-08 Location only while working](br-sc07-08-location-only-while-working.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC07-10 Vehicles inspected on time](br-sc07-10-vehicles-inspected-on-time.md)
