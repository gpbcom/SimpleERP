🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-17 Operators sign in only where qualified

# 📏 BR-F12-17 Operators sign in only where qualified

**Status:** ✅ specified

## Statement

An operator signs in at a work centre only if they hold its required qualifications, verified and current: they are the
requirements of the operation "sign in at a work centre"
([E-F12-17](../data/e-f12-17-qualification-requirement.md)), checked by
[BR-F9-25](../../f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md). A supervisor may allow a
supervised trainee, logged with a reason
([BR-F9-34](../../f09-hr-and-projects/business-rules/br-f09-34-overrides-logged-with-a-reason.md)); not where
the country pack marks the qualification as legal without a supervised exception
([BR-F9-26](../../f09-hr-and-projects/business-rules/br-f09-26-legal-requirements-never-relaxed.md)).

## Why

Untrained people on machines cause accidents.

## Examples

| Case | Result |
|---|---|
| Press safety expired | Refused |
| Supervised trainee | Allowed, logged |

## Applies to

- [UC-F12-22 Require operator qualifications per work centre](../use-cases/10-people-and-tools/uc-f12-22-require-operator-qualifications-per-work-centre.md)
- [BR-F9-25 Required attributes exclude a candidate](../../f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md)
- [E-F12-17 Qualification requirement](../data/e-f12-17-qualification-requirement.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F12-16 Only calibrated instruments record checks](br-f12-16-only-calibrated-instruments-record-checks.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F12-18 The schedule never exceeds capacity](br-f12-18-the-schedule-never-exceeds-capacity.md)
