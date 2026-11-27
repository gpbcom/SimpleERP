🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏛️ [SC20 Public bodies](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC20-14 Pay follows the index points of the grade

# 📏 BR-SC20-14 Pay follows the index points of the grade

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

The basic pay of a civil servant is computed from the index number of their grade and step and the value of the index
point of the pack for the month, never from a typed amount. Supplements come from the pack, and a difference from the
last month is explained before the run.

## Why

A pay computed from a typed amount drifts from the statute and an error is recovered from the employee
([D564](../../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md)). The index point is read in
[CR-FR-252 Public-sector contributions](../../../10-country-packs/france/payroll/cr-fr-252-public-sector-contributions.md):
the yearly pay of the majored index 100 is 5 907.34 EUR since 2023-07-01 (décret n° 85-1148, art. 3). (⚖️ lawyer
review before launch, D574) The statutory pay supplements are still to read: décret n° 85-1148 (residence allowance, family supplement) and
the bonus texts of each cadre.

## Examples

| Case | Result |
|---|---|
| Index 410, 5 907.34 EUR a year for index 100 | basic pay 2,018.34 a month |
| No step for an employee | not computed, listed |
| New point value from 1 July | used from that date |
| Part-time | reduced by the statutory fraction |
| Retroactive step change | back pay on its own line |

## Applies to

- [UC-SC20-14](../use-cases/04-public-hr-and-pay/uc-sc20-14-compute-statutory-pay.md)
- [E-SC20-11 Grade](../data/e-sc20-11-grade.md)
- [E-F13-16 Rate set](../../../02-functional/f13-payroll/data/e-f13-16-rate-set.md)

## Exceptions

None.

## Configurable

The supplements and the point value, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC20-13 Step changes follow the seniority rules](br-sc20-13-step-changes-follow-the-seniority-rules.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC20-15 Contributions follow the employee's scheme](br-sc20-15-contributions-follow-the-employees-scheme.md)
