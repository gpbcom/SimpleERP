🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-22 Rounds respect travel, skills, continuity and working time

# 📏 BR-F9-22 Rounds respect travel, skills, continuity and working time

**Status:** ✅ specified

## Statement

The route optimiser, the scheduling engine run on the visits of a round, places a visit only with someone who has the
skills its request type requires ([BR-F9-25](br-f09-25-required-attributes-exclude.md)), within its time window and the
person's working time, counting travel time between visits; it prefers the person's usual carer, as the objective of
continuity ([BR-F9-35](br-f09-35-default-order-of-objectives.md)).

## Why

The shared rounds capability of D457 for home care, transport and representatives.

## Examples

| Case | Result |
|---|---|
| Visit needs nursing skill | Only nurses |
| Round over 10 hours | Refused |
| Usual carer free | Preferred |

## Applies to

- [UC-F9-30 Plan rounds and optimise routes](../use-cases/11-capacity-rounds-and-partners/uc-f09-30-plan-rounds-and-optimise-routes.md)
- [UC-F9-33 Schedule a work request](../use-cases/12-schedule-customer-requests/uc-f09-33-schedule-a-work-request.md)
- [UC-F9-34 Run the automatic scheduling](../use-cases/12-schedule-customer-requests/uc-f09-34-run-the-automatic-scheduling.md)
- [UC-F9-35 Re-plan after a change](../use-cases/12-schedule-customer-requests/uc-f09-35-re-plan-after-a-change.md)

## Exceptions

None.

## Configurable

The skills each request type requires (UC-F2-30), and the order of the objectives (BR-F9-35, D517). The time
window and the working time: no.

## Open questions

None.

---

⬅️ [BR-F9-21 Planned load stays within available hours](br-f09-21-planned-load-stays-within-available-hours.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F9-23 Customers validate milestones they see](br-f09-23-customers-validate-milestones-they-see.md)
