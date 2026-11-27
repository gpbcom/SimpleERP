🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏛️ [SC20 Public bodies](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC20-10 Bookings follow the council's rates

# 📏 BR-SC20-10 Bookings follow the council's rates

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A booking uses the rate the council voted for the citizen's class and takes a deposit, and it is refused when the hall
is already booked or the number of people is above the safety capacity.

## Why

A rate outside the voted ones is irregular and a crowd above the capacity is a safety risk
([D564](../../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md)). The rates are those the council
votes. (⚖️ lawyer review before launch, D574) The France-pack rule on the safety capacity of a hall is still to write: to read the
fire-safety rules of venues open to the public (Code de la construction et de l'habitation R143-1 and following, arrêté
of 25 June 1980).

## Examples

| Case | Result |
|---|---|
| Resident booking | resident rate and deposit |
| Association booking | association rate, insurance proof asked |
| 120 people in a hall of 100 | refused |
| Hall already booked | free dates offered |
| Damage after use | deposit kept, title for the difference |

## Applies to

- [UC-SC20-10](../use-cases/03-citizen-services/uc-sc20-10-book-halls-and-equipment.md)
- [E-SC20-09 Hall booking](../data/e-sc20-09-hall-booking.md)
- [E-SC20-09 Hall booking](../data/e-sc20-09-hall-booking.md)
- [E-F2-18](../../../02-functional/f02-no-code-configuration/data/e-f02-18-resource-booking.md)

## Exceptions

None.

## Configurable

The rates by class and the deposits, voted by the council.

## Open questions

None.

---

⬅️ [BR-SC20-09 Requests are acknowledged with a deadline](br-sc20-09-requests-are-acknowledged-with-a-deadline.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC20-11](br-sc20-11-payments-go-to-the-public-treasurys-channel.md)
