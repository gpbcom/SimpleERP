🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F22-20 Carbon figures carry their method and source

# 📏 BR-F22-20 Carbon figures carry their method and source

**Status:** 🔄 waiting for the owner

## Statement

Every carbon figure shown or exported carries its method, the source and year of its emission factor, and whether it was
measured or estimated; an estimate shows its range, and a figure with no source is not shown.

## Why

A figure that cannot be explained cannot be defended in a report. The owner asked for the carbon of compute
([D541](../../../06-decisions/f22-unified-cost-management/d541-benchmark-gaps-f22-unified-cost-management.md)); the same
principle holds for purchases
[BR-F7-17](../../f07-purchasing-and-stock/business-rules/br-f07-17-carbon-figures-say-how-they-were-computed.md).

## Examples

| Case | Result |
|---|---|
| Machine power and hours known, national factor | figure shown as measured, with factor and year |
| Provider publishes no figure | estimate with a range, marked estimated |
| No factor for the year | no figure, the missing factor named |
| An export of the figures | each line carries its method and source |
| A figure typed over by hand | not possible: figures are computed |

## Applies to

- [UC-F22-29](../use-cases/08-credits-saas-and-carbon/uc-f22-29-measure-the-carbon-of-compute.md)
- [BR-F7-17](../../f07-purchasing-and-stock/business-rules/br-f07-17-carbon-figures-say-how-they-were-computed.md)

## Exceptions

None.

## Configurable

The emission factor and its source, by the owner, within the country pack's list.

## Open questions

None.

---

⬅️ [BR-F22-19 Unused seats are flagged before renewal](br-f22-19-unused-seats-are-flagged-before-renewal.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F22-21](br-f22-21-routing-never-goes-below-a-tasks-quality-bar.md)
