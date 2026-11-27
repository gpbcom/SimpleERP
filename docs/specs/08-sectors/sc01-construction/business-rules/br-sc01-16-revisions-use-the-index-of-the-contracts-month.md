🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏗️ [SC01 Construction](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC01-16 Revisions use the index of the contract's month

# 📏 BR-SC01-16 Revisions use the index of the contract's month

**Status:** ✅ specified

## Statement

A progress bill is revised with the index of the month the contract names for it, read from the series of its formula,
never with the index of the day it is issued. When that index is not published yet, the bill is revised provisionally
with the last published index and corrected when the real one appears.

## Why

A contract's clause fixes which month's index applies; using another month changes the price the customer owes and
starts disputes. The owner asked for price revision indices
([D545](../../../06-decisions/sectors/d545-benchmark-gaps-sc01-construction.md)). The France-pack rule is
[CR-FR-224 Price revision with BT and TP indices](../../../10-country-packs/france/construction/cr-fr-224-price-revision-indices.md).

## Examples

| Case | Result |
|---|---|
| Bill of March, index of March published | revised with the March index |
| Bill of April, April index not published | revised with the March index, provisional |
| April index published a month later | a correction line for the difference |
| Clause with a +8 % cap, revision of +9.3 % | the revision is cut to +8 % |
| Bill month before the base month | no revision |

## Applies to

- [UC-SC01-16](../use-cases/06-revision-developers-bim-and-grants/uc-sc01-16-revise-prices-with-the-bt-and-tp-indices.md)
- [E-SC01-15 Revision formula](../data/e-sc01-15-revision-formula.md)
- [E-SC01-06 Progress bill](../data/e-sc01-06-progress-bill.md)
- France-pack rule:
  [CR-FR-224 Price revision with BT and TP indices](../../../10-country-packs/france/construction/cr-fr-224-price-revision-indices.md)

## Exceptions

None.

## Configurable

The delay after which a provisional revision is reminded (three months by default), by accounting.

## Open questions

None.

---

⬅️ [BR-SC01-15 Leave through the fund](br-sc01-15-leave-through-the-fund.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC01-17 Calls for funds follow the legal stage caps](br-sc01-17-calls-for-funds-follow-the-legal-stage-caps.md)
