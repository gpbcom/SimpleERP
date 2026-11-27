🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D551 Benchmark gaps of SC07 Transport

# 📜 D551 Benchmark gaps of SC07 Transport

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four situations
that transport suites handle and SC07 did not: passenger transport, house removals, last-mile courier rounds and freight
forwarding with customs. Each carries a legal duty (the licence for the vehicle class, the binding signed quote, the
proof of delivery, the EORI number on a customs entry).

## Options

- G151 Passenger transport: passenger trips with a licence check on each assignment, or the goods trip reused with a
  note on the driver.
- G152 Removals: removals with a signed quote and a list of items with their condition, or an ordinary transport order.
- G153 Last-mile courier: parcel rounds with a next step for each failure, or deliveries closed with no follow-up.
- G154 Freight forwarding: a shipment file with the customs declaration and the EORI check, or the customs work done
  outside the system.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC07 gets four use cases in one new flow, FL-SC07-07, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist).

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G151 | Passenger transport | UC-SC07-21: drivers assigned only with the licence for the vehicle class | "Passenger transport" |
| G152 | Removals | UC-SC07-22: removal quotes that bind once signed | "Removals" |
| G153 | Last-mile courier | UC-SC07-23: a failed delivery given a new slot or a relay point | "Last-mile courier" |
| G154 | Freight forwarding | UC-SC07-24: customs entries that carry the EORI number | "Freight forwarding" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC07 Transport").

## Consequences

- G151 Passenger transport:
  [UC-SC07-21](../../08-sectors/sc07-transport/use-cases/07-passengers-removals-courier-and-freight/uc-sc07-21-run-passenger-transport.md),
  [S-SC07-21](../../08-sectors/sc07-transport/screens/07-passengers-removals-courier-and-freight/s-sc07-21-passenger-transport.md)
  and
  [BR-SC07-16](../../08-sectors/sc07-transport/business-rules/br-sc07-16-drivers-hold-the-licence-for-the-vehicle-class.md),
  with [E-SC07-18](../../08-sectors/sc07-transport/data/e-sc07-18-passenger-trip.md) Passenger trip and its list
  [S-SC07-L18](../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l18-passenger-trips.md).
- G152 Removals:
  [UC-SC07-22](../../08-sectors/sc07-transport/use-cases/07-passengers-removals-courier-and-freight/uc-sc07-22-quote-and-run-house-removals.md),
  [S-SC07-22](../../08-sectors/sc07-transport/screens/07-passengers-removals-courier-and-freight/s-sc07-22-removals.md)
  and [BR-SC07-17](../../08-sectors/sc07-transport/business-rules/br-sc07-17-the-removal-quote-binds-once-signed.md),
  with [E-SC07-19](../../08-sectors/sc07-transport/data/e-sc07-19-removal.md) Removal and its list
  [S-SC07-L19](../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l19-removals.md).
- G153 Last-mile courier:
  [UC-SC07-23](../../08-sectors/sc07-transport/use-cases/07-passengers-removals-courier-and-freight/uc-sc07-23-run-last-mile-rounds.md),
  [S-SC07-23](../../08-sectors/sc07-transport/screens/07-passengers-removals-courier-and-freight/s-sc07-23-last-mile.md)
  and
  [BR-SC07-18](../../08-sectors/sc07-transport/business-rules/br-sc07-18-a-failed-delivery-gets-a-new-slot-or-a-relay-point.md),
  with [E-SC07-20](../../08-sectors/sc07-transport/data/e-sc07-20-parcel.md) Parcel and its list
  [S-SC07-L20](../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l20-parcels.md).
- G154 Freight forwarding:
  [UC-SC07-24](../../08-sectors/sc07-transport/use-cases/07-passengers-removals-courier-and-freight/uc-sc07-24-forward-freight-and-clear-customs.md),
  [S-SC07-24](../../08-sectors/sc07-transport/screens/07-passengers-removals-courier-and-freight/s-sc07-24-freight-forwarding.md)
  and [BR-SC07-19](../../08-sectors/sc07-transport/business-rules/br-sc07-19-customs-entries-carry-the-eori-number.md),
  with [E-SC07-21](../../08-sectors/sc07-transport/data/e-sc07-21-shipment-file.md) Shipment file and its list
  [S-SC07-L21](../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l21-shipment-files.md).
- Drawn in [FL-SC07-07](../../08-sectors/sc07-transport/flows/fl-sc07-07-passengers-removals-courier-and-freight.md)
  Passengers, removals, courier and freight.

## Related

- [FL-SC07-07](../../08-sectors/sc07-transport/flows/fl-sc07-07-passengers-removals-courier-and-freight.md)
- [D335 Transport sector coverage](d335-transport-sector-coverage.md)
- [D337 SC07 use cases](d337-sc07-use-cases.md)
- [U29 Dispatcher](../../01-users/personas/u29-dispatcher.md)

---

⬅️ [D550 Benchmark gaps of SC06 Hospitality](d550-benchmark-gaps-sc06-hospitality.md) · ⬆️ [Up](README.md) ·
➡️ [D552 Benchmark gaps of SC08 Non-profit](d552-benchmark-gaps-sc08-non-profit.md)
