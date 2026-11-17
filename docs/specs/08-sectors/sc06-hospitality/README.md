🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🍽️ SC06 Restaurant and hospitality

# 🍽️ SC06 Restaurant and hospitality

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D332 to D334.

## Summary

What restaurants and hotels add to F10 Point of sale: costed recipes, allergens and labels, hygiene records,
perishables, tips and staff meals; rooms, rates, bookings through channel managers, check-in and check-out,
housekeeping, one folio per stay, the tourist tax, meal vouchers and performance
([D332](../../06-decisions/sectors/d332-hospitality-sector-coverage.md)).

## Profile

Restaurants, cafés, bars and hotels, from one venue to small groups, many seasonal and part-time staff.

## Personas

[U28 Hotel receptionist](../../01-users/personas/u28-hotel-receptionist.md),
[U18 Waiter](../../01-users/personas/u18-waiter.md), [U19 Kitchen staff](../../01-users/personas/u19-kitchen-staff.md),
[U17 Cashier](../../01-users/personas/u17-cashier.md),
[U23 Store manager](../../01-users/personas/u23-store-manager.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, roles and sites: one site per restaurant
  or hotel.
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  the shared booking engine for rooms,
  [UC-F2-18](../../02-functional/f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md),
  [UC-F2-19](../../02-functional/f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-19-book-a-resource.md),
  and offline tablet forms for hygiene and housekeeping.
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on the hotel or restaurant,
  [UC-SC06-15](use-cases/03-rooms-and-bookings/uc-sc06-15-ask-the-assistant-about-the-hotel-or-restaurant.md).
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): ingredients, perishables, counts.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): shifts for many part-time staff.
- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md): restaurant and bar service, meal
  vouchers,
  [UC-F10-21](../../02-functional/f10-point-of-sale/use-cases/08-vouchers-and-age-checks/uc-f10-21-accept-meal-vouchers-within-the-daily-cap.md),
  folios charged from the till.
- [F12 Manufacturing (plugin)](../../02-functional/f12-manufacturing/README.md): kitchen recipes on the shared recipes
  capability,
  [UC-F12-31](../../02-functional/f12-manufacturing/use-cases/09-recipes-and-batches/uc-f12-31-define-a-recipe-and-produce-in-batches.md).
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): pay inputs: tips, staff meals, the
  hotels-and-restaurants agreement,
  [UC-F13-30](../../02-functional/f13-payroll/use-cases/09-collective-agreements-by-family/uc-f13-30-apply-the-hotels-and-restaurants-agreement.md).
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F2-18 Make a record type bookable](../../02-functional/f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md),
  [UC-F12-31 Define a recipe and produce in batches](../../02-functional/f12-manufacturing/use-cases/09-recipes-and-batches/uc-f12-31-define-a-recipe-and-produce-in-batches.md).

## Technical capabilities used

- [T1 Companies and data isolation](../../03-technical/t01-companies-and-data-isolation/README.md)
- [T2 Identity and access](../../03-technical/t02-identity-and-access/README.md)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)
- [T4 Plugin runtime](../../03-technical/t04-plugin-runtime/README.md) (the sector pack)
- [T5 API and webhooks](../../03-technical/t05-api-and-webhooks/README.md)
- [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md) (the AI assistant)
- [T8 RAG platform](../../03-technical/t08-rag-platform/README.md)
- [T9 Install, backups and updates](../../03-technical/t09-install-backups-and-updates/README.md)
- [T10 Translations and notifications](../../03-technical/t10-translations-and-notifications/README.md)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack's rules)
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (channel managers, delivery
  platforms)

Also: offline tablets (REQ-T05-07).

## Example company

- [Restaurant and hospitality](../../01-users/example-companies/hospitality.md)

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🎁 |  | [Sector pack](sector-pack.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Manufacturing](../sc05-manufacturing/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Transport and logistics](../sc07-transport/README.md)
