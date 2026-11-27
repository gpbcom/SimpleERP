🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🌾 [SC13 Agriculture and food](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC13-04 Withdrawal before sale

# 📏 BR-SC13-04 Withdrawal before sale

**Status:** ✅ specified

## Statement

Milk, eggs or animals under a withdrawal period cannot be sold: their lots stay blocked until the period ends. In
France each treatment is recorded with its withdrawal period, even when it is nil, and kept 5 years:
[CR-FR-163 Livestock health register and withdrawal periods](../../../10-country-packs/france/agriculture/cr-fr-163-livestock-health-register.md).

## Why

The livestock register records each veterinary medicine given, the animals treated, the route, the daily dose and the
start and end dates, or the prescription, and is kept at least 5 years after the year of the last entry (CR-FR-163,
arrêté du 5 juin 2000). The withdrawal period is the minimum time between the last administration and obtaining food from the
animal that keeps the food free of harmful residues (Regulation (EU) 2019/6, art. 4(34) and 108); the texts read state no
ban on selling as such, so blocking the lot is how SimpleERP keeps food from being obtained before the period ends.

## Examples

| Case | Result |
|---|---|
| Cow treated 2 days ago, 4-day withdrawal | Milk lot blocked |

## Applies to

Every SC13 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-SC13-03 Animals notified on time](br-sc13-03-animals-notified-on-time.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC13-05 Aid declared from the records](br-sc13-05-aid-declared-from-the-records.md)
