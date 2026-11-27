🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-01 The till follows the country pack

# 📏 BR-F10-01 The till follows the country pack

**Status:** ✅ specified

## Statement

Every sale, correction, closure and archive follows the till rules of the company's country pack; in France:
[CR-FR-024 Till software holds a certificate or an attestation](../../../10-country-packs/france/point-of-sale/cr-fr-024-certified-till-software.md),
[CR-FR-025 Data recorded for each sale](../../../10-country-packs/france/point-of-sale/cr-fr-025-sale-data-recorded.md),
[CR-FR-026 Till data is inalterable](../../../10-country-packs/france/point-of-sale/cr-fr-026-till-inalterability.md),
[CR-FR-027 Till security and training mode](../../../10-country-packs/france/point-of-sale/cr-fr-027-till-security.md),
[CR-FR-028 Daily, monthly and yearly closures](../../../10-country-packs/france/point-of-sale/cr-fr-028-till-closures.md),
[CR-FR-029 Till data kept six years](../../../10-country-packs/france/point-of-sale/cr-fr-029-till-data-kept-six-years.md),
[CR-FR-030 Till archives](../../../10-country-packs/france/point-of-sale/cr-fr-030-till-archives.md).

## Why

See [D296](../../../06-decisions/f10-point-of-sale/d296-till-certified-before-france.md).

## Examples

| Case | Result |
|---|---|
| A paid order is edited | Refused: a refund or a new order is made |
| A day ends with the session open | Closed automatically at the set time, with its daily closure |

## Applies to

Every F10 use case concerned.

- [UC-F10-21 Accept meal vouchers within the daily cap](../use-cases/08-vouchers-and-age-checks/uc-f10-21-accept-meal-vouchers-within-the-daily-cap.md)

- [UC-F10-27 Sell tax-free to a visitor from outside the EU](../use-cases/10-clienteling-transfers-and-tax-free/uc-f10-27-sell-tax-free-to-a-visitor-from-outside-the-eu.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-F10-02 One session per till, counted at closing](br-f10-02-one-session-per-till.md)
