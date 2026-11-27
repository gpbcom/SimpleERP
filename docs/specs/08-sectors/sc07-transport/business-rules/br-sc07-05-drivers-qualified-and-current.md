🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🚛 [SC07 Transport and logistics](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC07-05 Drivers qualified and current

# 📏 BR-SC07-05 Drivers qualified and current

**Status:** ✅ specified

## Statement

(Proposed) A driver is assigned only with a valid licence, driver card and training: legal requirements of the trip's
request type
[BR-F9-26](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-26-legal-requirements-never-relaxed.md),
checked by
[BR-F9-25](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md);
renewals are reminded; in France:
[CR-FR-119 Drivers' initial and continuous training](../../../10-country-packs/france/transport/cr-fr-119-driver-training.md).

## Why

(Proposed) The renewal period is still to read.

## Examples

| Case | Result |
|---|---|
| Training expired | Not assignable |

## Applies to

Every SC07 use case concerned, and
[E-F2-25 Request type](../../../02-functional/f02-no-code-configuration/data/e-f02-25-request-type.md).

## Exceptions

None.

## Configurable

Reminder delays.

## Open questions

None.

---

⬅️ [BR-SC07-04 Documents on board complete](br-sc07-04-documents-on-board-complete.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC07-06 Proof of delivery closes the stop](br-sc07-06-proof-of-delivery-closes-the-stop.md)
