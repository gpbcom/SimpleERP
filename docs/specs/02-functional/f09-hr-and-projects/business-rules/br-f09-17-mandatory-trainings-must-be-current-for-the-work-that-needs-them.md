🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-17 Mandatory trainings must be current for the work that needs them

# 📏 BR-F9-17 Mandatory trainings must be current for the work that needs them

**Status:** ✅ specified

## Statement

Work that needs a mandatory training or certification cannot be planned for a person whose training is expired: the
training is a required attribute of the work's request type or operation, checked by
[BR-F9-25](br-f09-25-required-attributes-exclude.md), always required
([BR-F9-26](br-f09-26-legal-requirements-never-relaxed.md)), and an expired one does not count
([BR-F9-27](br-f09-27-unverified-attributes-do-not-count.md)); reminders start before the expiry (Proposed: 90 days).

## Why

Drivers, carers and operators may not work without them.

## Examples

| Case | Result |
|---|---|
| Driver training expired | Shift refused |
| Expires in 90 days | Reminder |

## Applies to

- [UC-F9-25 Run the training plan with OPCO funding](../use-cases/09-train-and-protect/uc-f09-25-run-the-training-plan-with-opco-funding.md)
- [UC-F9-33 Schedule a work request](../use-cases/12-schedule-customer-requests/uc-f09-33-schedule-a-work-request.md)
- [E-F2-25 Request type](../../f02-no-code-configuration/data/e-f02-25-request-type.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F9-16 HR duties follow the headcount](br-f09-16-hr-duties-follow-the-headcount.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-18 A work accident is declared within 48 hours](br-f09-18-a-work-accident-is-declared-within-48-hours.md)
