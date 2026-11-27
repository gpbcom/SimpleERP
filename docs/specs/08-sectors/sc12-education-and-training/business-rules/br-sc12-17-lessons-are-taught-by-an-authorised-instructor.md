🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🎓 [SC12 Education and training](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC12-17 Lessons are taught by an authorised instructor

# 📏 BR-SC12-17 Lessons are taught by an authorised instructor

**Status:** ✅ specified

## Statement

A driving lesson is booked and given only by an instructor whose authorisation to teach is valid on the day and covers
the licence category, in a vehicle that is registered and inspected. A lesson with an instructor whose authorisation has
lapsed is refused.

## Why

A lesson by an unauthorised instructor is unlawful, can void the learner's hours and exposes the school to a penalty and
the loss of its approval. The owner asked for driving schools
([D556](../../../06-decisions/sectors/d556-benchmark-gaps-sc12-education-and-training.md)). The values come
from the France pack, written later.

## Examples

| Case | Result |
|---|---|
| Authorised for B until 2028-03-31, lesson 2026-11-21 | booked |
| Authorisation ended yesterday | refused |
| Authorised for B, lesson in category A | refused |
| Vehicle inspection overdue | the vehicle is not offered |
| Authorisation ends in 60 days | the coordinator is told |

## Applies to

- [UC-SC12-22](../use-cases/06-apprentices-driving-nurseries-and-canteens/uc-sc12-22-run-a-driving-school.md)
- [E-SC12-21 Driving lesson](../data/e-sc12-21-driving-lesson.md)
- [E-SC12-11 Trainer profile](../data/e-sc12-11-trainer-profile.md)

## Exceptions

None.

## Configurable

The warning delay before an authorisation ends (60 days by default), by the coordinator.

## Open questions

None.

---

⬅️ [BR-SC12-16](br-sc12-16-funding-follows-the-contracts-support-level.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC12-18 Hourly funding follows the CAF scale](br-sc12-18-hourly-funding-follows-the-caf-scale.md)
