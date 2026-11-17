🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💼 [SC03 Services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC03-13 Skills kept current

# 📏 BR-SC03-13 Skills kept current

**Status:** ✅ specified

## Statement

Skills and certifications carry their level and expiry; staffing an engagement is a request type whose skills and
certifications, at their level, are required attributes checked by
[BR-F9-25](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md), and only
current ones count.

## Why

See [D323](../../../06-decisions/sectors/d323-services-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| Certification expired | Not proposed for that role |

## Applies to

Every SC03 use case concerned, and
[E-F2-25 Request type](../../../02-functional/f02-no-code-configuration/data/e-f02-25-request-type.md).

## Exceptions

None.

## Configurable

Skills catalogue; the skills and levels each staffing request type requires.

## Open questions

None.

---

⬅️ [BR-SC03-12 Clients see only their engagements](br-sc03-12-client-sees-only-their-engagements.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC03-14 Payment terms within the law](br-sc03-14-payment-terms-in-the-law.md)
