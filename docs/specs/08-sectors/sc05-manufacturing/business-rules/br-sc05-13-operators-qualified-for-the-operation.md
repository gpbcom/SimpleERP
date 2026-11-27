🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏭 [SC05 Manufacturing](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC05-13 Operators qualified for the operation

# 📏 BR-SC05-13 Operators qualified for the operation

**Status:** ✅ specified

## Statement

An operator starts an operation only when they hold the qualification it requires
([E-SC05-13 Operation qualification](../data/e-sc05-13-operation-qualification.md)), verified and current: a requirement
of the operation "start a manufacturing operation", checked by
[BR-F9-25](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md).

## Why

See [D329](../../../06-decisions/sectors/d329-manufacturing-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| Not qualified on welding | Start refused, supervisor called |

## Applies to

Every SC05 use case concerned, and
[BR-F9-25 Required attributes exclude a candidate](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md).

## Exceptions

None.

## Configurable

Qualifications per operation, as the requirements of the operation (BR-F9-25).

## Open questions

None.

---

⬅️ [BR-SC05-12 Instruments calibrated before use](br-sc05-12-instruments-calibrated-before-use.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC05-14 Objectives reviewed yearly](br-sc05-14-objectives-reviewed-yearly.md)
