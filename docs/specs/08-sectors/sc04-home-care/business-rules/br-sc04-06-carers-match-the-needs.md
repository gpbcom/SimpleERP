🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏠 [SC04 Home care](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC04-06 Carers match the needs

# 📏 BR-SC04-06 Carers match the needs

**Status:** ✅ specified

## Statement

A carer is assigned only with the skills and qualifications the care plan needs: they are required attributes of the
home-care visit's request type, completed by the care plan's needs on each visit's work request, and checked by
[BR-F9-25](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md); the
recipient's preferences are respected where possible, as the customer-preference objective
[BR-F9-35](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-35-default-order-of-objectives.md).

## Why

See [D326](../../../06-decisions/sectors/d326-home-care-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| Plan needs a qualified carer | Only qualified carers proposed |

## Applies to

Every SC04 use case concerned, and
[E-F2-25 Request type](../../../02-functional/f02-no-code-configuration/data/e-f02-25-request-type.md).

## Exceptions

None.

## Configurable

Skills per task, as the required attributes of each visit's request type.

## Open questions

None.

---

⬅️ [BR-SC04-05 Rounds count travel time](br-sc04-05-rounds-count-travel-time.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC04-07 Visit times from check-in](br-sc04-07-visit-times-from-check-in.md)
